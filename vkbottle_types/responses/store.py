import inspect
import typing

from vkbottle_types.objects import BaseSticker, StoreProduct, StoreStickersKeyword

from .base_response import BaseResponse


class GetFavoriteStickersResponse(BaseResponse):
    response: typing.Optional["GetFavoriteStickersResponseModel"] = None


class GetProductsResponse(BaseResponse):
    response: typing.Optional["GetProductsResponseModel"] = None


class GetStickersKeywordsResponse(BaseResponse):
    response: typing.Optional["GetStickersKeywordsResponseModel"] = None


GetFavoriteStickersResponseModel = typing.List[BaseSticker]


GetProductsResponseModel = typing.List[StoreProduct]


class GetStickersKeywordsResponseModel(BaseResponse):
    count: typing.Optional[int] = None
    dictionary: typing.Optional[typing.List["StoreStickersKeyword"]] = None
    chunks_count: typing.Optional[int] = None
    chunks_hash: typing.Optional[str] = None


for item in locals().copy().values():
    if inspect.isclass(item) and issubclass(item, BaseResponse):
        item.update_forward_refs()
