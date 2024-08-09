import dataclasses
import typing
from collections import OrderedDict

import dataclass_factory

from .parse_types import (
    PRIMITIVE_TYPES,
    Ready,
    get_complex_type,
    get_responses,
    get_type,
    transform_ref,
)
from .utility import camelcase, snake_case


@dataclasses.dataclass
class WithRef:
    ref: str | None = None
    type: str | None = None
    definition: "Definition | None" = None
    properties: dict = dataclasses.field(default_factory=lambda: {})


@dataclasses.dataclass
class MethodParameter:
    name: str
    type: str | list[str] | dict | Ready

    required: bool = False
    description: str | None = None
    default: str | int | bool | None = None

    format: str | None = None
    items: dict = dataclasses.field(default_factory=lambda: {})

    def get_type(self) -> str:
        return get_type(self.type, self.items)

    def get_default(self, default: typing.Any | None = None, tp: str | None = None) -> str:
        default_val = default or self.default
        tp = tp or self.type  # type: ignore

        if not self.required:
            return "None"

        if default is None and tp == "array":
            return "None"

        if isinstance(tp, list):
            result = None
            for t in tp:
                res = self.get_default(default_val, t)
                if res != "None":
                    result = res
                    break
            return "None" if result is None else result

        if isinstance(default_val, int) and tp in ("boolean", "bool"):
            return repr(bool(default_val))
        if isinstance(default_val, int) and tp in ("integer", "int"):
            return repr(default_val)
        if isinstance(default_val, (int, float)) and tp in ("number", "float"):
            return repr(float(default_val))
        return str(default_val)

    @property
    def has_default(self) -> bool:
        return not self.required or self.default is not None

    @classmethod
    def new_dependant(cls, orig: "MethodParameter") -> "MethodParameter":
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
            dependant.required = True
            dependant.default = None
            return dependant

        if isinstance(dependant.type, Ready):
            if dependant.type.value == "typing.Literal[True]":
                dependant.type = Ready("typing.Literal[False]")
                dependant.default = None
                dependant.required = False
                return dependant
            if dependant.type.value == "typing.Literal[False]":
                orig.type = "boolean"
                orig.required = False
                orig.default = None
                return orig

        dependant.required = not dependant.required
        return dependant


@dataclasses.dataclass
class Method:
    name: str
    access_token_type: list[str]
    parameters: list[MethodParameter] = dataclasses.field(
        default_factory=lambda: [],
    )
    responses: dict[str, WithRef] = dataclasses.field(default_factory=lambda: {})
    errors: list[WithRef] = dataclasses.field(default_factory=lambda: [])
    timeout: int | None = dataclasses.field(default=None)
    dependant_parameters: list[str] = dataclasses.field(default_factory=lambda: [])

    def __post_init__(self) -> None:
        self.dependant_parameters = self.dependant_parameters or self.get_dependant_params()

    def get_dependant_params(self) -> list[str]:
        dependant_params: set[str] = set()

        for name in self.responses.copy():
            if name == "response":
                continue
            original_name = name.removesuffix("Response").removesuffix("_")
            dep_params = set(map(snake_case, original_name.split("_")))
            if not any(self.param_exists(param) for param in dep_params):
                continue
            dependant_params |= dep_params

        return list(dependant_params)

    def param_exists(self, param_name: str) -> bool:
        return any(param.name == param_name for param in self.parameters)

    def get_dependants(self) -> list["Method"]:
        if len(self.responses) > 1:
            dependant_responses = typing.cast(dict, self.responses.copy())
            dependant_responses.pop("response", None)
            dependant_responses = OrderedDict[str, dict[str, str]](
                **dependant_responses,
                response=self.responses.get("response"),  # type: ignore
            )
            dependants = []
            method_params: dict[str, MethodParameter] = {}
            dependant_params: set[str] = set(self.dependant_parameters)

            for name, response in dependant_responses.items():
                if response is None:
                    continue

                if name != "response":
                    original_param_names = (
                        name.removeprefix("response")
                        .removesuffix("Response")
                        .removesuffix("_")
                        .replace("Response", "")
                    )
                    dependant_params = dependant_params | set(
                        x
                        for x in map(snake_case, original_param_names.split("_"))
                        if x not in PRIMITIVE_TYPES
                    )
                    dependant_found = False
                else:
                    dependant_found = bool(self.dependant_parameters)

                for param in list(method_params.copy().values()) or self.parameters:
                    if param.name not in dependant_params:
                        method_params[param.name] = param
                    else:
                        dependant_found = True
                        new_dep = param.new_dependant(param)
                        method_params[param.name] = new_dep

                        if new_dep is param:
                            dependant_params.remove(param.name)
                        else:
                            dependant_params.add(param.name)

                if dependant_found:
                    dependants.append(
                        Method(
                            self.name,
                            self.access_token_type,
                            parameters=list(method_params.values()),
                            responses={"response": response},  # type: ignore
                            dependant_parameters=list(dependant_params),
                        )
                    )
                elif name != "response" and name in self.responses:
                    self.responses.pop(name)

            return dependants
        return []

    def get_dependants_dependant_parameters(self) -> dict[str, str]:
        dependant_parameters = {}
        response_model: str | None = (
            self.responses.get("response", {}).get("response_hint", {}).get("hint", None)  # type: ignore
        )

        for dependant in self.get_dependants():
            for dependant_parameter in dependant.dependant_parameters:
                dependant_response_model = dependant.get_response_model()
                if (
                    response_model == dependant_response_model
                    or dependant_parameter in dependant_parameters
                ):
                    continue
                dependant_parameters[dependant_parameter] = dependant_response_model

        return dependant_parameters

    def get_responses_hints(self) -> list[str]:
        return list(
            set(
                get_complex_type(response, response=True)
                for response in get_responses(self.responses)  # type: ignore
            )
        )

    def get_response_hint(self) -> str:
        responses = get_responses(self.responses)  # type: ignore
        if not responses:
            return "typing.Dict[str, typing.Any]"
        if len(responses) > 1:
            responses_hints = self.get_responses_hints()
            if len(responses_hints) == 1 or not self.get_dependants():
                return responses_hints[0]
            return "typing.Union[{}]".format(", ".join(responses_hints))
        return get_complex_type(responses[0], response=True)

    def get_response_model(self) -> str:
        responses = get_responses(self.responses)  # type: ignore
        if not responses:
            return "DictResponse"
        return get_complex_type(responses[0])  # type: ignore

    @property
    def is_single_response(self) -> bool:
        return len(self.responses) <= 1

    @property
    def sorted_parameters(self) -> list["MethodParameter"]:
        required = []
        optional = []

        for param in self.parameters:
            if not param.has_default:
                required.append(param)
            else:
                optional.append(param)

        required.sort(key=lambda param: param.name)
        optional.sort(key=lambda param: param.name)

        if not self.dependant_parameters:
            return required + optional

        dependant_required = []
        dependant_optional = []

        for param_name in self.dependant_parameters:
            for index, param in enumerate(required.copy()):
                if param.name == param_name:
                    dependant_required.append(required.pop(index))

            for index, param in enumerate(optional.copy()):
                if param.name == param_name:
                    dependant_optional.append(optional.pop(index))

        return (required + dependant_required) + (dependant_optional + optional)


def wrap_optional(func):
    def wrapper(self: "Property", **kw: typing.Any) -> str:
        response = func(self, **kw)
        if self.is_optional:
            response = "typing.Optional[{}]".format(response)
        return response

    return wrapper


@dataclasses.dataclass
class Property:
    name: str
    type: str | list[str] | None = dataclasses.field(default=None)
    description: str | None = dataclasses.field(default=None)
    default: typing.Any | None = dataclasses.field(default=None)
    enum: list[str | int] = dataclasses.field(default_factory=lambda: [])
    enumNames: list[str] = dataclasses.field(default_factory=lambda: [])  # noqa: N815
    items: dict = dataclasses.field(default_factory=lambda: {})
    ref: str | None = dataclasses.field(default=None)
    required: bool = dataclasses.field(default=False)
    data: dict = dataclasses.field(default_factory=lambda: {})

    @wrap_optional
    def get_type(
        self,
        hint: bool = False,
        response: bool = False,
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

        if t == "dict" and response:
            return "typing.Dict[str, typing.Any]"
        return t

    @property
    def is_optional(self) -> bool:
        return not self.required

    def get_default_value(self, model_name: str | None = None) -> typing.Any | None:
        if self.default is None:
            return None
        if self.enum and model_name:
            for i, enum in enumerate(self.enum):
                if enum == self.default:
                    return model_name + "." + self.enumNames[i].replace(" ", "_").upper()
        if self.type == "boolean":
            return bool(self.default)
        return self.default


@dataclasses.dataclass
class Definition:
    type: str
    allOf: list[WithRef] = dataclasses.field(default_factory=lambda: [])  # noqa: N815
    properties: list[Property] = dataclasses.field(default_factory=lambda: [])  # why list?
    enum: list[str | int] = dataclasses.field(default_factory=lambda: [])
    enumNames: list[str] = dataclasses.field(default_factory=lambda: [])  # noqa: N815
    sub_definitions: dict[str, "Definition"] = dataclasses.field(default_factory=lambda: {})
    items: typing.Any | None = None
    ref: str | None = None
    name: str | None = None

    _bases: list[str] = dataclasses.field(default_factory=lambda: [])
    _default_base: str = "BaseModel"
    _default_base_response: str = "BaseResponse"

    def get_response_definition(self) -> "Definition | None":
        for prop in self.properties:
            if prop.name != "response":
                continue
            if prop.data.get("enum"):
                return Definition(
                    type="enum",
                    enum=prop.data["enum"],
                    enumNames=prop.data.get("enumNames", []),
                )
            if prop.data.get("type") == "object":
                properties = [
                    factory.load({"name": pname, **p}, Property)
                    for pname, p in prop.data.get("properties", {}).items()
                ]
                return Definition(type="object", allOf=self.allOf, properties=properties)
        return None

    def get_properties(self) -> typing.List[Property]:
        return sorted(self.properties, key=lambda x: x.is_optional)

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

    def get_bases(self, response: bool = False) -> list[str]:
        if self._bases:
            return self._bases

        if self.allOf:
            base_sub_definitions: dict[str, list[str]] = {
                transform_ref(base.ref): list(base.definition.sub_definitions.keys())
                for base in self.allOf
                if base.ref and base.definition
            }
            refs = [transform_ref(base.ref) for base in self.allOf if base.ref]

            for ref in refs.copy():
                if ref in base_sub_definitions:
                    for sub_def in base_sub_definitions[ref]:
                        if sub_def in refs:
                            refs.remove(ref)

            for base in self.allOf:
                if base.properties:
                    for propname, prop in base.properties.items():
                        self.properties.append(factory.load({"name": propname, **prop}, Property))
                    pass

            self._bases = refs
            return self._bases

        self._bases = [self._default_base if not response else self._default_base_response]
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
    methods: list[Method] = dataclasses.field(default_factory=lambda: [])
    objects: Objects | None = None
    responses: Objects | None = None


ref_schema: dataclass_factory.Schema = dataclass_factory.Schema(name_mapping={"ref": "$ref"})
factory = dataclass_factory.Factory(
    schemas={WithRef: ref_schema, Property: ref_schema, Definition: ref_schema},
)


__all__ = (
    "Method",
    "MethodParameter",
    "Property",
    "Definition",
    "Objects",
    "Category",
    "factory",
)
