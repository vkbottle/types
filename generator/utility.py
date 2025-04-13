import itertools
import keyword


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

    if keyword.iskeyword(s) or s == "model":
        s = s + "_"
    elif s[0].isdigit():
        s = "f__" + s
    s = s.replace(" ", "_")
    if s.isupper():
        return s
    return snake_case(s)


def instring(s: str) -> str:
    return s.replace("'", "\\'").replace('"', '\\"')


__all__ = ("camelcase", "snake_case", "makesafe", "instring")
