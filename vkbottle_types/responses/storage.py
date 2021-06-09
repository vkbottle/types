import inspect
import typing
from .base_response import BaseResponse
from vkbottle_types.objects import StorageValue


class GetKeysResponse(BaseResponse):
    response: typing.List[str] = None


class GetResponse(BaseResponse):
    response: typing.List["StorageValue"] = None


for item in locals().copy().values():
    if inspect.isclass(item) and issubclass(item, BaseResponse):
        item.update_forward_refs()
