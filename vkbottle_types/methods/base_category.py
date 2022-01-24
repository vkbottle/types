import typing

if typing.TYPE_CHECKING:
    from vkbottle import ABCAPI

# from typing import NamedTuple
# RequestMethod = NamedTuple("RequestMethod", [("base_name", str), ("method_name", str), ("params", dict)])


T = typing.TypeVar("T")


class BaseCategory:
    def __init__(self, api: "ABCAPI"):
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
            typing.Tuple[typing.Tuple[typing.Union[str, typing.List[str]], ...], T], ...
        ],
        default: T,
        params: dict,
    ) -> T:
        """Choices model depending on params"""
        for items in sorted(dependent, key=lambda x: len(x[0])):
            keys, model = items
            for key in keys:
                if isinstance(key, str) and params.get(key) is None:
                    break
                elif isinstance(key, list) and params.get(key[0]) not in key[1:]:
                    break
            else:
                return model

        return default

    @classmethod
    def construct_api(cls, api: "ABCAPI") -> typing.Type["BaseCategory"]:
        cls.api = api
        return cls
