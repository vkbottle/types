import typing
from typing import Optional

from vkbottle_types.objects import wall, market, base
from .base_response import BaseResponse


class AddAlbumResponse(BaseResponse):
    response: Optional["AddAlbumResponseModel"] = None


class AddResponse(BaseResponse):
    response: Optional["AddResponseModel"] = None


class CreateCommentResponse(BaseResponse):
    response: Optional[int] = None


class DeleteCommentResponse(BaseResponse):
    response: Optional[typing.List["base.BoolInt"]] = None


class GetAlbumByIdResponse(BaseResponse):
    response: Optional["GetAlbumByIdResponseModel"] = None


class GetAlbumsResponse(BaseResponse):
    response: Optional["GetAlbumsResponseModel"] = None


class GetByIdExtendedResponse(BaseResponse):
    response: Optional["GetByIdExtendedResponseModel"] = None


class GetByIdResponse(BaseResponse):
    response: Optional["GetByIdResponseModel"] = None


class GetCategoriesResponse(BaseResponse):
    response: Optional["GetCategoriesResponseModel"] = None


class GetCommentsResponse(BaseResponse):
    response: Optional["GetCommentsResponseModel"] = None


class GetExtendedResponse(BaseResponse):
    response: Optional["GetExtendedResponseModel"] = None


class GetResponse(BaseResponse):
    response: Optional["GetResponseModel"] = None


class RestoreCommentResponse(BaseResponse):
    response: Optional[typing.List["base.BoolInt"]] = None


class SearchExtendedResponse(BaseResponse):
    response: Optional["SearchExtendedResponseModel"] = None


class SearchResponse(BaseResponse):
    response: Optional["SearchResponseModel"] = None


class AddAlbumResponseModel(BaseResponse):
    market_album_id: Optional[int] = None


class AddResponseModel(BaseResponse):
    market_item_id: Optional[int] = None


class GetAlbumByIdResponseModel(BaseResponse):
    count: Optional[int] = None
    items: Optional[typing.List["market.MarketAlbum"]] = None


class GetAlbumsResponseModel(BaseResponse):
    count: Optional[int] = None
    items: Optional[typing.List["market.MarketAlbum"]] = None


class GetByIdExtendedResponseModel(BaseResponse):
    count: Optional[int] = None
    items: Optional[typing.List["market.MarketItemFull"]] = None


class GetByIdResponseModel(BaseResponse):
    count: Optional[int] = None
    items: Optional[typing.List["market.MarketItem"]] = None


class GetCategoriesResponseModel(BaseResponse):
    count: Optional[int] = None
    items: Optional[typing.List["market.MarketCategory"]] = None


class GetCommentsResponseModel(BaseResponse):
    count: Optional[int] = None
    items: Optional[typing.List["wall.WallComment"]] = None


class GetExtendedResponseModel(BaseResponse):
    count: Optional[int] = None
    items: Optional[typing.List["market.MarketItemFull"]] = None


class GetResponseModel(BaseResponse):
    count: Optional[int] = None
    items: Optional[typing.List["market.MarketItem"]] = None


class SearchExtendedResponseModel(BaseResponse):
    count: Optional[int] = None
    items: Optional[typing.List["market.MarketItemFull"]] = None


class SearchResponseModel(BaseResponse):
    count: Optional[int] = None
    items: Optional[typing.List["market.MarketItem"]] = None
