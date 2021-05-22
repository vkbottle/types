import inspect
import typing
from .base_response import BaseResponse
from vkbottle_types.objects import StorageValue


class GetKeysResponse(BaseResponse):
    response: typing.Optional["GetKeysResponseModel"] = None


class GetResponse(BaseResponse):
    response: typing.Optional["GetResponseModel"] = None


GetKeysResponseModel = typing.List[str]


GetResponseModel = typing.List[StorageValue]


for item in locals().copy().values():
    if inspect.isclass(item) and issubclass(item, BaseResponse):
        item.update_forward_refs()
