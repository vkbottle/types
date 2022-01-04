import typing

if typing.TYPE_CHECKING:
    from vkbottle import API

# from typing import NamedTuple
# RequestMethod = NamedTuple("RequestMethod", [("base_name", str), ("method_name", str), ("params", dict)])


T = typing.TypeVar("T")


class BaseCategory:
    def __init__(self, api: "API"):
        self.api = api

    @classmethod
    def get_set_params(cls, params: dict) -> dict:
        exclude_params = params.copy()
        exclude_params.update(params["kwargs"])
        exclude_params.pop("kwargs")
        return {
            k if not k.startswith("_") else k[1:]: v
            for k, v in exclude_params.items()
            if k != "self" and v is not None
        }

    @classmethod
    def get_model(
        cls,
        dependent: typing.Tuple[
            typing.Tuple[typing.Union[typing.Tuple[str, ...], typing.List[str]], T], ...
        ],
        default: T,
        params: dict,
    ) -> T:
        for items in sorted(dependent, key=lambda x: len(x[0])):
            ks, model = items
            if isinstance(ks, tuple):
                if all(params.get(k) is not None for k in ks):
                    return model
            elif isinstance(ks, list):
                arg, *ks = ks
                if any(arg == k for k in ks):
                    return model
        return default

    @classmethod
    def construct_api(cls, api: "API") -> typing.Type["BaseCategory"]:
        cls.api = api
        return cls
