from typing import Optional, List

from vkbottle_types.objects import (
    MarketMarketCategory,
    MarketMarketItem,
    WallWallComment,
    MarketMarketItemFull,
    MarketMarketAlbum,
    BaseBoolInt,
)
from .base_response import BaseResponse


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

DeleteCommentResponseModel = Optional[BaseBoolInt]


class GetAlbumByIdResponseModel(BaseResponse):
    count: Optional[int] = None
    items: Optional[List["MarketMarketAlbum"]] = None


class GetAlbumsResponseModel(BaseResponse):
    count: Optional[int] = None
    items: Optional[List["MarketMarketAlbum"]] = None


class GetByIdExtendedResponseModel(BaseResponse):
    count: Optional[int] = None
    items: Optional[List["MarketMarketItemFull"]] = None


class GetByIdResponseModel(BaseResponse):
    count: Optional[int] = None
    items: Optional[List["MarketMarketItem"]] = None


class GetCategoriesResponseModel(BaseResponse):
    count: Optional[int] = None
    items: Optional[List["MarketMarketCategory"]] = None


class GetCommentsResponseModel(BaseResponse):
    count: Optional[int] = None
    items: Optional[List["WallWallComment"]] = None


class GetExtendedResponseModel(BaseResponse):
    count: Optional[int] = None
    items: Optional[List["MarketMarketItemFull"]] = None


class GetResponseModel(BaseResponse):
    count: Optional[int] = None
    items: Optional[List["MarketMarketItem"]] = None


RestoreCommentResponseModel = Optional[BaseBoolInt]


class SearchExtendedResponseModel(BaseResponse):
    count: Optional[int] = None
    items: Optional[List["MarketMarketItemFull"]] = None


class SearchResponseModel(BaseResponse):
    count: Optional[int] = None
    items: Optional[List["MarketMarketItem"]] = None


AddAlbumResponse.update_forward_refs()
AddResponse.update_forward_refs()
CreateCommentResponse.update_forward_refs()
DeleteCommentResponse.update_forward_refs()
GetAlbumByIdResponse.update_forward_refs()
GetAlbumsResponse.update_forward_refs()
GetByIdExtendedResponse.update_forward_refs()
GetByIdResponse.update_forward_refs()
GetCategoriesResponse.update_forward_refs()
GetCommentsResponse.update_forward_refs()
GetExtendedResponse.update_forward_refs()
GetResponse.update_forward_refs()
RestoreCommentResponse.update_forward_refs()
SearchExtendedResponse.update_forward_refs()
SearchResponse.update_forward_refs()
