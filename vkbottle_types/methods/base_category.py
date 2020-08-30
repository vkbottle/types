import typing

if typing.TYPE_CHECKING:
    from vkbottle import API

# from typing import NamedTuple
# RequestMethod = NamedTuple("RequestMethod", [("base_name", str), ("method_name", str), ("params", dict)])


class BaseCategory:
    def __init__(self, api: "API"):
        self.api = api

    @classmethod
    def get_set_params(cls, params: dict) -> dict:
        exclude_params = params.copy()
        exclude_params.update(params["kwargs"])
        exclude_params.pop("kwargs")
        return {
            k if not k.endswith("_") else k[:-1]: v
            for k, v in exclude_params.items()
            if k != "self" and v is not None
        }

    @classmethod
    def construct_api(cls, api: "API") -> "BaseCategory":
        cls.api = api
        return cls
