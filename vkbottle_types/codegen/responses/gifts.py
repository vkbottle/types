import inspect
import typing

from vkbottle_types.objects import GiftsGift

from .base_response import BaseResponse


class GetResponse(BaseResponse):
    response: "GetResponseModel"


class GetResponseModel(BaseResponse):
    count: typing.Optional[int] = None
    items: typing.Optional[typing.List["GiftsGift"]] = None


for item in locals().copy().values():
    if inspect.isclass(item) and issubclass(item, BaseResponse):
        item.update_forward_refs()


__all__ = ("GetResponse",)
