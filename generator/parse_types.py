import dataclasses
import re
import typing

from .utility import camelcase

PATTERN_PROPERTIES_RESPONSE = re.compile(r"^([a-zA-Z0-9_]+)?[rR]esponse$")

IMPORTS_CACHE = set()
# that line above.. ofc its shit but im too lazy rn!! sry ^^
# i hate shitingletons but generator lib is not rly in uz rn but ok FIXME

PRIMITIVE_TYPES = {
    "integer": "int",
    "string": "str",
    "boolean": "bool",
    "number": "float",
    "Integer": "int",
    "String": "str",
    "Boolean": "bool",
    "Number": "float",
}


@dataclasses.dataclass
class Ready:
    value: str


def get_responses(responses: dict[str, dict[str, str]]) -> list[dict[str, str]]:
    if not responses:
        return []
    return [
        value
        for key, value in responses.items()
        if PATTERN_PROPERTIES_RESPONSE.match(key) is not None
        or (key != "response" and key.startswith("response"))
    ]


def transform_ref(ref_link: str) -> str:
    name = camelcase(ref_link.split("/")[-1])
    return name


def get_complex_type(type_dct: dict, response: bool = False, hint: bool = False) -> str:
    if (type_ := type_dct.get("type")) and type_ != "object":
        return get_type(type_, type_dct.get("items", type_dct), hint=hint)
    elif ref := type_dct.get("$ref"):
        transformed = transform_ref(ref)
        if response:
            if "response_hint" in type_dct:
                return type_dct["response_hint"]["hint"]
            return transformed + "Model"
        else:
            IMPORTS_CACHE.add(transformed)
        if hint:
            transformed = repr(transformed)
        return transformed

    raise RuntimeError(f"Cannot process complex type {type_dct}")


def get_type(
    type_name: str | list[str] | dict | Ready, items: dict | None = None, hint: bool = False
) -> str:
    if isinstance(type_name, Ready):
        if hint:
            return repr(type_name.value)
        return type_name.value

    items = items or {}

    match type_name:
        case "string":
            if literals := items.get("enum"):
                return "typing.Literal[{}]".format(", ".join(repr(literal) for literal in literals))
            return "str"
        case "array":
            return "typing.List[{}]".format(get_complex_type(items, hint=hint))
        case "object":
            if "$ref" in items:
                return get_complex_type(items, hint=True)
            return "dict"
        case str(type_name):
            if type_name not in PRIMITIVE_TYPES:
                raise RuntimeError(f"{type_name} not in primitive types")
            return PRIMITIVE_TYPES[type_name]
        case list(lst):
            return "typing.Union{}".format([get_type(name, {}, hint=True) for name in lst])

    raise RuntimeError(f"Cannot process {type_name} (items={items})")


__all__ = ("get_type", "get_complex_type", "Ready", "transform_ref", "get_responses")
