import inspect
import typing

from vkbottle_types.objects import StorageValue

from .base_response import BaseResponse


class GetKeysResponse(BaseResponse):
    response: typing.List[str]


class GetResponse(BaseResponse):
    response: typing.List["StorageValue"]


for item in locals().copy().values():
    if inspect.isclass(item) and issubclass(item, BaseResponse):
        item.update_forward_refs()


__all__ = (
    "GetKeysResponse",
    "GetResponse",
)
