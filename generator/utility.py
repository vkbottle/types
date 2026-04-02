import itertools
import keyword

BUILTIN_TYPES = frozenset(("list", "dict", "str", "int", "float", "bool", "set", "frozenset", "tuple", "bytes"))


def camelcase(s: str) -> str:
    return "".join(word[0].upper() + word[1:] for word in s.split("_"))


def snake_case(s: str) -> str:
    """Converts string into snake case.

    >>> snake_case("camelCase")
    >>> 'camel_case'
    >>> snake_case("PascalCase")
    >>> 'pascal_case'
    >>> snake_case("getSafeURL")
    >>> 'get_safe_url'
    """

    new_s = ""
    for first, second in itertools.zip_longest(s, s[1:], fillvalue=""):
        if first.islower() and second.isupper():
            new_s += first + "_"
        else:
            new_s += first.lower()
    return new_s


def makesafe(s: str) -> str:
    """Transforms arbitrary string into python-declarable name."""

    if keyword.iskeyword(s) or s == "model" or s in BUILTIN_TYPES:
        s = s + "_"
    elif s[0].isdigit():
        s = "f__" + s
    s = s.replace(" ", "_")
    if s.isupper():
        return s
    return snake_case(s)


def makesafe_method_name(s: str) -> str:
    if keyword.iskeyword(s):
        return s + "_"
    if s in ("dict", "list"):
        return "get_" + s
    return s


def instring(s: str) -> str:
    return s.replace("'", "\\'").replace('"', '\\"')


__all__ = ("camelcase", "instring", "makesafe", "makesafe_method_name", "snake_case")
