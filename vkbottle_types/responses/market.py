import inspect
import typing
from .base_response import BaseResponse
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
    WallWallComment
)


class AddAlbumResponse(BaseResponse):
    response: "AddAlbumResponseModel" = None


class AddResponse(BaseResponse):
    response: "AddResponseModel" = None


class CreateCommentResponse(BaseResponse):
    response: int = None


class DeleteCommentResponse(BaseResponse):
    response: BaseBoolInt = None


class GetAlbumByIdResponse(BaseResponse):
    response: "GetAlbumByIdResponseModel" = None


class GetAlbumsResponse(BaseResponse):
    response: "GetAlbumsResponseModel" = None


class GetByIdExtendedResponse(BaseResponse):
    response: "GetByIdExtendedResponseModel" = None


class GetByIdResponse(BaseResponse):
    response: "GetByIdResponseModel" = None


class GetCategoriesNewResponse(BaseResponse):
    response: "GetCategoriesNewResponseModel" = None


class GetCategoriesResponse(BaseResponse):
    response: "GetCategoriesResponseModel" = None


class GetCommentsResponse(BaseResponse):
    response: "GetCommentsResponseModel" = None


class GetGroupOrdersResponse(BaseResponse):
    response: "GetGroupOrdersResponseModel" = None


class GetOrderByIdResponse(BaseResponse):
    response: "GetOrderByIdResponseModel" = None


class GetOrderItemsResponse(BaseResponse):
    response: "GetOrderItemsResponseModel" = None


class GetOrdersExtendedResponse(BaseResponse):
    response: "GetOrdersExtendedResponseModel" = None


class GetOrdersResponse(BaseResponse):
    response: "GetOrdersResponseModel" = None


class GetExtendedResponse(BaseResponse):
    response: "GetExtendedResponseModel" = None


class GetResponse(BaseResponse):
    response: "GetResponseModel" = None


class RestoreCommentResponse(BaseResponse):
    response: BaseBoolInt = None


class SearchExtendedResponse(BaseResponse):
    response: "SearchExtendedResponseModel" = None


class SearchResponse(BaseResponse):
    response: "SearchResponseModel" = None


class AddAlbumResponseModel(BaseResponse):
    market_album_id: typing.Optional[int] = None


class AddResponseModel(BaseResponse):
    market_item_id: typing.Optional[int] = None


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
