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
from vkbottle_types.responses.base_response import BaseResponse


class AddAlbumResponse(BaseResponse):
    response: "AddAlbumResponseModel"


class AddResponse(BaseResponse):
    response: "AddResponseModel"


class CreateCommentResponse(BaseResponse):
    response: int


class DeleteCommentResponse(BaseResponse):
    response: BaseBoolInt


class GetAlbumByIdResponse(BaseResponse):
    response: "GetAlbumByIdResponseModel"


class GetAlbumsResponse(BaseResponse):
    response: "GetAlbumsResponseModel"


class GetByIdExtendedResponse(BaseResponse):
    response: "GetByIdExtendedResponseModel"


class GetByIdResponse(BaseResponse):
    response: "GetByIdResponseModel"


class GetCategoriesNewResponse(BaseResponse):
    response: "GetCategoriesNewResponseModel"


class GetCategoriesResponse(BaseResponse):
    response: "GetCategoriesResponseModel"


class GetCommentsResponse(BaseResponse):
    response: "GetCommentsResponseModel"


class GetGroupOrdersResponse(BaseResponse):
    response: "GetGroupOrdersResponseModel"


class GetOrderByIdResponse(BaseResponse):
    response: "GetOrderByIdResponseModel"


class GetOrderItemsResponse(BaseResponse):
    response: "GetOrderItemsResponseModel"


class GetOrdersExtendedResponse(BaseResponse):
    response: "GetOrdersExtendedResponseModel"


class GetOrdersResponse(BaseResponse):
    response: "GetOrdersResponseModel"


class GetExtendedResponse(BaseResponse):
    response: "GetExtendedResponseModel"


class GetResponse(BaseResponse):
    response: "GetResponseModel"


class RestoreCommentResponse(BaseResponse):
    response: BaseBoolInt


class SearchExtendedResponse(BaseResponse):
    response: "SearchExtendedResponseModel"


class SearchResponse(BaseResponse):
    response: "SearchResponseModel"


class AddAlbumResponseModel(BaseResponse):
    market_album_id: typing.Optional[int] = None
    albums_count: typing.Optional[int] = None


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
    variants: typing.Optional[typing.List["MarketMarketItemFull"]] = None


class GetResponseModel(BaseResponse):
    count: typing.Optional[int] = None
    items: typing.Optional[typing.List["MarketMarketItem"]] = None
    variants: typing.Optional[typing.List["MarketMarketItem"]] = None


class SearchExtendedResponseModel(BaseResponse):
    count: typing.Optional[int] = None
    view_type: typing.Optional["MarketServicesViewType"] = None
    items: typing.Optional[typing.List["MarketMarketItemFull"]] = None
    variants: typing.Optional[typing.List["MarketMarketItemFull"]] = None


class SearchResponseModel(BaseResponse):
    count: typing.Optional[int] = None
    view_type: typing.Optional["MarketServicesViewType"] = None
    items: typing.Optional[typing.List["MarketMarketItem"]] = None
    variants: typing.Optional[typing.List["MarketMarketItem"]] = None
    groups: typing.Optional[typing.List["GroupsGroupFull"]] = None


__all__ = (
    "AddAlbumResponse",
    "AddAlbumResponseModel",
    "AddResponse",
    "AddResponseModel",
    "BaseBoolInt",
    "CreateCommentResponse",
    "DeleteCommentResponse",
    "GetAlbumByIdResponse",
    "GetAlbumByIdResponseModel",
    "GetAlbumsResponse",
    "GetAlbumsResponseModel",
    "GetByIdExtendedResponse",
    "GetByIdExtendedResponseModel",
    "GetByIdResponse",
    "GetByIdResponseModel",
    "GetCategoriesNewResponse",
    "GetCategoriesNewResponseModel",
    "GetCategoriesResponse",
    "GetCategoriesResponseModel",
    "GetCommentsResponse",
    "GetCommentsResponseModel",
    "GetExtendedResponse",
    "GetExtendedResponseModel",
    "GetGroupOrdersResponse",
    "GetGroupOrdersResponseModel",
    "GetOrderByIdResponse",
    "GetOrderByIdResponseModel",
    "GetOrderItemsResponse",
    "GetOrderItemsResponseModel",
    "GetOrdersExtendedResponse",
    "GetOrdersExtendedResponseModel",
    "GetOrdersResponse",
    "GetOrdersResponseModel",
    "GetResponse",
    "GetResponseModel",
    "GroupsGroupFull",
    "MarketMarketAlbum",
    "MarketMarketCategory",
    "MarketMarketCategoryTree",
    "MarketMarketItem",
    "MarketMarketItemFull",
    "MarketOrder",
    "MarketOrderItem",
    "MarketServicesViewType",
    "RestoreCommentResponse",
    "SearchExtendedResponse",
    "SearchExtendedResponseModel",
    "SearchResponse",
    "SearchResponseModel",
    "WallWallComment",
)
