import re
import keyword


def camelcase(s: str) -> str:
    return "".join(word[0].upper() + word[1:] for word in s.split("_"))


def snake_case(s: str) -> str:
    return re.sub(r"(?<!^)(?=[A-Z])", "_", s).lower()


def makesafe(s: str) -> str:
    """Transforms arbitrary string into python-declarable name"""
    if keyword.iskeyword(s) or s[0].isdigit():
        s = "_" + s
    return s.replace(" ", "_")


def instring(s: str) -> str:
    return s.replace("'", "\\'").replace('"', '\\"')
