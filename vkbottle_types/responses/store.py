import inspect
import typing
from .base_response import BaseResponse
from vkbottle_types.objects import BaseSticker, StoreProduct, StoreStickersKeyword


class GetFavoriteStickersResponse(BaseResponse):
    response: typing.List["BaseSticker"] = None


class GetProductsResponse(BaseResponse):
    response: typing.List["StoreProduct"] = None


class GetStickersKeywordsResponse(BaseResponse):
    response: "GetStickersKeywordsResponseModel" = None


class GetStickersKeywordsResponseModel(BaseResponse):
    count: typing.Optional[int] = None
    dictionary: typing.Optional[typing.List["StoreStickersKeyword"]] = None
    chunks_count: typing.Optional[int] = None
    chunks_hash: typing.Optional[str] = None


for item in locals().copy().values():
    if inspect.isclass(item) and issubclass(item, BaseResponse):
        item.update_forward_refs()
