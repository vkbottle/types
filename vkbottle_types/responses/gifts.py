import inspect
import typing
from .base_response import BaseResponse
from vkbottle_types.objects import GiftsGift


class GetResponse(BaseResponse):
    response: typing.Optional["GetResponseModel"] = None


class GetResponseModel(BaseResponse):
    count: typing.Optional[int] = None
    items: typing.Optional[typing.List["GiftsGift"]] = None


for item in locals().copy().values():
    if inspect.isclass(item) and issubclass(item, BaseResponse):
        item.update_forward_refs()
