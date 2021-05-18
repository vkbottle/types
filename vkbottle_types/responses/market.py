import inspect
import typing

from vkbottle_types.objects import (
    BaseBoolInt,
    GroupsGroupFull,
    MarketMarketAlbum,
    MarketMarketCategory,
    MarketMarketCategoryTree,
    MarketMarketItem,
    MarketMarketItemFull,
    MarketOrder,
    MarketOrderItem,
    MarketServicesViewType,
    WallWallComment,
)

from .base_response import BaseResponse


class AddAlbumResponse(BaseResponse):
    response: typing.Optional["AddAlbumResponseModel"] = None


class AddResponse(BaseResponse):
    response: typing.Optional["AddResponseModel"] = None


class CreateCommentResponse(BaseResponse):
    response: typing.Optional["CreateCommentResponseModel"] = None


class DeleteCommentResponse(BaseResponse):
    response: typing.Optional["DeleteCommentResponseModel"] = None


class GetAlbumByIdResponse(BaseResponse):
    response: typing.Optional["GetAlbumByIdResponseModel"] = None


class GetAlbumsResponse(BaseResponse):
    response: typing.Optional["GetAlbumsResponseModel"] = None


class GetByIdExtendedResponse(BaseResponse):
    response: typing.Optional["GetByIdExtendedResponseModel"] = None


class GetByIdResponse(BaseResponse):
    response: typing.Optional["GetByIdResponseModel"] = None


class GetCategoriesNewResponse(BaseResponse):
    response: typing.Optional["GetCategoriesNewResponseModel"] = None


class GetCategoriesResponse(BaseResponse):
    response: typing.Optional["GetCategoriesResponseModel"] = None


class GetCommentsResponse(BaseResponse):
    response: typing.Optional["GetCommentsResponseModel"] = None


class GetGroupOrdersResponse(BaseResponse):
    response: typing.Optional["GetGroupOrdersResponseModel"] = None


class GetOrderByIdResponse(BaseResponse):
    response: typing.Optional["GetOrderByIdResponseModel"] = None


class GetOrderItemsResponse(BaseResponse):
    response: typing.Optional["GetOrderItemsResponseModel"] = None


class GetOrdersExtendedResponse(BaseResponse):
    response: typing.Optional["GetOrdersExtendedResponseModel"] = None


class GetOrdersResponse(BaseResponse):
    response: typing.Optional["GetOrdersResponseModel"] = None


class GetExtendedResponse(BaseResponse):
    response: typing.Optional["GetExtendedResponseModel"] = None


class GetResponse(BaseResponse):
    response: typing.Optional["GetResponseModel"] = None


class RestoreCommentResponse(BaseResponse):
    response: typing.Optional["RestoreCommentResponseModel"] = None


class SearchExtendedResponse(BaseResponse):
    response: typing.Optional["SearchExtendedResponseModel"] = None


class SearchResponse(BaseResponse):
    response: typing.Optional["SearchResponseModel"] = None


class AddAlbumResponseModel(BaseResponse):
    market_album_id: typing.Optional[int] = None


class AddResponseModel(BaseResponse):
    market_item_id: typing.Optional[int] = None


CreateCommentResponseModel = int


DeleteCommentResponseModel = BaseBoolInt


class GetAlbumByIdResponseModel(BaseResponse):
    count: typing.Optional[int] = None
    items: typing.Optional[typing.List["MarketMarketAlbum"]] = None


class GetAlbumsResponseModel(BaseResponse):
    count: typing.Optional[int] = None
    items: typing.Optional[typing.List["MarketMarketAlbum"]] = None


class GetByIdExtendedResponseModel(BaseResponse):
    count: typing.Optional[int] = None
    items: typing.Optional[typing.List["MarketMarketItemFull"]] = None


class GetByIdResponseModel(BaseResponse):
    count: typing.Optional[int] = None
    items: typing.Optional[typing.List["MarketMarketItem"]] = None


class GetCategoriesNewResponseModel(BaseResponse):
    items: typing.Optional[typing.List["MarketMarketCategoryTree"]] = None


class GetCategoriesResponseModel(BaseResponse):
    count: typing.Optional[int] = None
    items: typing.Optional[typing.List["MarketMarketCategory"]] = None


class GetCommentsResponseModel(BaseResponse):
    count: typing.Optional[int] = None
    items: typing.Optional[typing.List["WallWallComment"]] = None


class GetGroupOrdersResponseModel(BaseResponse):
    count: typing.Optional[int] = None
    items: typing.Optional[typing.List["MarketOrder"]] = None


class GetOrderByIdResponseModel(BaseResponse):
    order: typing.Optional["MarketOrder"] = None


class GetOrderItemsResponseModel(BaseResponse):
    count: typing.Optional[int] = None
    items: typing.Optional[typing.List["MarketOrderItem"]] = None


class GetOrdersExtendedResponseModel(BaseResponse):
    count: typing.Optional[int] = None
    items: typing.Optional[typing.List["MarketOrder"]] = None
    groups: typing.Optional[typing.List["GroupsGroupFull"]] = None


class GetOrdersResponseModel(BaseResponse):
    count: typing.Optional[int] = None
    items: typing.Optional[typing.List["MarketOrder"]] = None


class GetExtendedResponseModel(BaseResponse):
    count: typing.Optional[int] = None
    items: typing.Optional[typing.List["MarketMarketItemFull"]] = None


class GetResponseModel(BaseResponse):
    count: typing.Optional[int] = None
    items: typing.Optional[typing.List["MarketMarketItem"]] = None


RestoreCommentResponseModel = BaseBoolInt


class SearchExtendedResponseModel(BaseResponse):
    count: typing.Optional[int] = None
    view_type: typing.Optional["MarketServicesViewType"] = None
    items: typing.Optional[typing.List["MarketMarketItemFull"]] = None


class SearchResponseModel(BaseResponse):
    count: typing.Optional[int] = None
    view_type: typing.Optional["MarketServicesViewType"] = None
    items: typing.Optional[typing.List["MarketMarketItem"]] = None


for item in locals().copy().values():
    if inspect.isclass(item) and issubclass(item, BaseResponse):
        item.update_forward_refs()
