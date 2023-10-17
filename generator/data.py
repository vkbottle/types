import dataclasses
import dataclass_factory
import typing
from .utility import snake_case, camelcase
from .types import get_type, Ready, get_any, get_complex_type, transform_ref


@dataclasses.dataclass
class WithRef:
    ref: str | None = None
    type: str | None = None
    properties: dict | list | None = None


@dataclasses.dataclass
class MethodParameter:
    name: str
    type: str | list[str] | dict

    required: bool = False
    description: str | None = None
    default: str | int | bool | None = None

    format: str | None = None
    items: dict | None = None

    def get_type(self) -> str:
        return get_type(self.type, self.items)

    def get_default(self) -> str:
        if isinstance(self.default, str):
            return repr(self.default)
        return str(self.default)

    @property
    def has_default(self) -> bool:
        return not self.required or self.default is not None

    @classmethod
    def new_dependant(self, orig: "MethodParameter") -> "MethodParameter":
        dependant = MethodParameter(
            orig.name,
            orig.type,
            orig.required,
            orig.description,
            orig.default,
            orig.format,
            orig.items,
        )
        if dependant.type == "boolean":
            dependant.type = Ready("typing.Literal[True]")
            dependant.default = True
            dependant.required = True
        else:
            dependant.required = True
        return dependant


@dataclasses.dataclass
class Method:
    name: str
    access_token_type: list[str]
    parameters: list[MethodParameter] | None = dataclasses.field(
        default_factory=lambda: []
    )
    responses: dict[str, WithRef] | None = None
    errors: list[WithRef] | None = None
    timeout: int | None = None

    dependant_parameters: list[str] | None = None

    def get_dependants(self) -> list["Method"]:
        if len(self.responses) > 1:
            dependant_responses = self.responses.copy()
            dependant_responses.pop("response", None)
            dependants = []

            for name, response in dependant_responses.items():
                original_param_names = name.removesuffix("Response").removesuffix("_")
                param_names = list(map(snake_case, original_param_names.split("_")))

                dependants.append(
                    Method(
                        self.name,
                        self.access_token_type,
                        [
                            param
                            if param.name not in param_names
                            else param.new_dependant(param)
                            for param in self.parameters
                        ],
                        {"response": response},
                        dependant_parameters=param_names,
                    )
                )
            return dependants
        return []

    def get_response_hint(self, category_name: str) -> str:
        response = get_any(
            self.responses, "response", "baseResponse", "deprecatedResponse"
        )
        if not response:
            return "typing.Union[{}]".format(
                ", ".join(
                    get_complex_type(response, response=True)
                    for response in self.responses.values()
                )
            )
        return get_complex_type(response, response=True)

    def get_response_model(self, category_name: str) -> str:
        response = get_any(
            self.responses, "response", "baseResponse", "deprecatedResponse"
        )
        if not response:
            return "None"
        return get_complex_type(response)

    @property
    def is_single_response(self) -> bool:
        return len(self.responses) == 1

    @property
    def sorted_parameters(self) -> list["Method"]:
        required = []
        optional = []
        for param in self.parameters:
            if param.required:
                required.append(param)
            else:
                optional.append(param)
        return required + optional


def wrap_optional(func):
    def wrapper(self: "Property", **kw) -> str:
        response = func(self, **kw)
        if self.is_optional:
            response = "typing.Optional[{}]".format(response)
        return response

    return wrapper


@dataclasses.dataclass
class Property:
    name: str
    type: str | list[str] | None = None
    description: str | None = None
    items: dict | None = None
    ref: str | None = None
    required: bool = False
    data: dict | None = None

    @wrap_optional
    def get_type(
        self,
        hint: bool = False,
        literal_to_enum: bool = False,
        definition_name: str | None = None,
    ) -> str:
        if not self.type:
            ct = get_complex_type({"$ref": self.ref}, hint=True)

            if ct == "'BaseBoolInt'":
                return "bool"

            return ct

        t = get_type(self.type, self.items or self.data, hint=hint)
        if literal_to_enum and t.startswith("typing.Literal"):
            if not definition_name:
                raise LookupError("Definition name is required")
            propname = camelcase(definition_name) + camelcase(self.name)
            return repr(propname)
        return t

    @property
    def is_optional(self) -> bool:
        return not self.required


@dataclasses.dataclass
class Definition:
    type: str
    allOf: list[WithRef] = dataclasses.field(default_factory=lambda: [])
    properties: typing.List[Property] | None = None  # why list?
    enum: list[str | int] | None = None
    enumNames: list[str] | None = None
    items: typing.Any | None = None
    name: str | None = None

    _bases: list[str] | None = None
    _default_base: str = "BaseModel"

    def get_properties(self) -> typing.Iterable[tuple[str, Property]]:
        props = [factory.load(prop, Property) for prop in self.properties or []]
        return sorted(props, key=lambda x: x.is_optional)

    def get_enums(self, definition_name: str) -> typing.Iterator["Definition"]:
        for prop in self.get_properties():
            if prop.type == "string" and (prop.data or {}).get("enum"):
                yield Definition(
                    "enum",
                    enum=prop.data["enum"],
                    name=camelcase(definition_name) + camelcase(prop.name),
                )

    def get_typehint(self) -> str:
        assert self.type != "object"
        return get_complex_type(dataclasses.asdict(self), hint=True)

    def get_bases(self) -> list[str]:
        if self._bases is not None:
            return self._bases

        if self.allOf:
            refs = [transform_ref(base.ref) for base in self.allOf if base.ref]
            for base in self.allOf:
                if base.properties:
                    for propname, prop in base.properties.items():
                        if self.properties is None:
                            self.properties = []
                        self.properties.append({**prop, "name": propname})
                    pass
            self._bases = refs
            return self._bases

        self._bases = [self._default_base]
        return self._bases


@dataclasses.dataclass
class Objects:
    title: str
    definitions: dict[str, Definition] = dataclasses.field(default_factory=lambda: {})
    version: str | None = None
    description: str | None = None


@dataclasses.dataclass
class Category:
    name: str
    methods: list[Method] | None = None
    objects: Objects | None = None
    responses: Objects | None = None


ref_schema = dataclass_factory.Schema(name_mapping={"ref": "$ref"})
factory = dataclass_factory.Factory(schemas={WithRef: ref_schema, Property: ref_schema})
