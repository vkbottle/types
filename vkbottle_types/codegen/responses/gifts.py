import typing

from vkbottle_types.objects import GiftsGift
from vkbottle_types.responses.base_response import BaseResponse


class GetResponse(BaseResponse):
    response: "GetResponseModel"


class GetResponseModel(BaseResponse):
    count: typing.Optional[int] = None
    items: typing.Optional[typing.List["GiftsGift"]] = None


__all__ = (
    "GetResponse",
    "GetResponseModel",
    "GiftsGift",
)
