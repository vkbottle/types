from .base_response import BaseResponse
from vkbottle_types.objects import market, wall, base
from typing import Optional, Any, List, Union
import typing


class AddAlbumResponse(BaseResponse):
    response: Optional["AddAlbumResponseModel"] = None


class AddResponse(BaseResponse):
    response: Optional["AddResponseModel"] = None


class CreateCommentResponse(BaseResponse):
    response: Optional["CreateCommentResponseModel"] = None


class DeleteCommentResponse(BaseResponse):
    response: Optional["DeleteCommentResponseModel"] = None


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
    response: Optional["RestoreCommentResponseModel"] = None


class SearchExtendedResponse(BaseResponse):
    response: Optional["SearchExtendedResponseModel"] = None


class SearchResponse(BaseResponse):
    response: Optional["SearchResponseModel"] = None


class AddAlbumResponseModel(BaseResponse):
    market_album_id: Optional[int] = None


class AddResponseModel(BaseResponse):
    market_item_id: Optional[int] = None


CreateCommentResponseModel = int


DeleteCommentResponseModel = Optional["base.BoolInt"]


class GetAlbumByIdResponseModel(BaseResponse):
    count: Optional[int] = None
    items: Optional[List["market.MarketAlbum"]] = None


class GetAlbumsResponseModel(BaseResponse):
    count: Optional[int] = None
    items: Optional[List["market.MarketAlbum"]] = None


class GetByIdExtendedResponseModel(BaseResponse):
    count: Optional[int] = None
    items: Optional[List["market.MarketItemFull"]] = None


class GetByIdResponseModel(BaseResponse):
    count: Optional[int] = None
    items: Optional[List["market.MarketItem"]] = None


class GetCategoriesResponseModel(BaseResponse):
    count: Optional[int] = None
    items: Optional[List["market.MarketCategory"]] = None


class GetCommentsResponseModel(BaseResponse):
    count: Optional[int] = None
    items: Optional[List["wall.WallComment"]] = None


class GetExtendedResponseModel(BaseResponse):
    count: Optional[int] = None
    items: Optional[List["market.MarketItemFull"]] = None


class GetResponseModel(BaseResponse):
    count: Optional[int] = None
    items: Optional[List["market.MarketItem"]] = None


RestoreCommentResponseModel = Optional["base.BoolInt"]


class SearchExtendedResponseModel(BaseResponse):
    count: Optional[int] = None
    items: Optional[List["market.MarketItemFull"]] = None


class SearchResponseModel(BaseResponse):
    count: Optional[int] = None
    items: Optional[List["market.MarketItem"]] = None
