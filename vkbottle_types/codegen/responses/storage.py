import typing

from vkbottle_types.objects import StorageValue
from vkbottle_types.responses.base_response import BaseResponse


class GetKeysResponse(BaseResponse):
    response: typing.List[str]


class GetResponse(BaseResponse):
    response: typing.List["StorageValue"]


__all__ = (
    "GetKeysResponse",
    "GetResponse",
    "StorageValue",
)
