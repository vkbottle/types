from vkbottle_types.base_model import BaseModel, Field
from vkbottle_types.objects import (
    GroupsGroupFull,
    MarketGlobalSearchFilters,
    MarketMarketAlbum,
    MarketMarketCategoryTree,
    MarketMarketItem,
    MarketMarketItemBasicWithGroup,
    MarketMarketItemFull,
    MarketOrder,
    MarketOrderItem,
    MarketProperty,
    MarketServicesViewType,
    MarketUploadPhotoData,
    PhotosPhoto,
    UsersUserFull,
    WallWallComment,
)
from vkbottle_types.responses.base_response import BaseResponse


class MarketAddAlbumResponseModel(BaseModel):
    market_album_id: int | None = Field(
        default=None,
    )
    albums_count: int | None = Field(
        default=None,
    )


class MarketAddAlbumResponse(BaseResponse):
    response: "MarketAddAlbumResponseModel" = Field()


class MarketAddPropertyVariantResponseModel(BaseModel):
    variant_id: int = Field()


class MarketAddPropertyVariantResponse(BaseResponse):
    response: "MarketAddPropertyVariantResponseModel" = Field()


class MarketAddPropertyResponseModel(BaseModel):
    property_id: int = Field()


class MarketAddPropertyResponse(BaseResponse):
    response: "MarketAddPropertyResponseModel" = Field()


class MarketAddResponseModel(BaseModel):
    market_item_id: int = Field()


class MarketAddResponse(BaseResponse):
    response: "MarketAddResponseModel" = Field()


class MarketCreateCommentResponse(BaseResponse):
    response: int = Field()


class MarketGetAlbumByIdResponseModel(BaseModel):
    count: int = Field()
    items: list["MarketMarketAlbum"] = Field()


class MarketGetAlbumByIdResponse(BaseResponse):
    response: "MarketGetAlbumByIdResponseModel" = Field()


class MarketGetAlbumsResponseModel(BaseModel):
    count: int = Field()
    items: list["MarketMarketAlbum"] = Field()


class MarketGetAlbumsResponse(BaseResponse):
    response: "MarketGetAlbumsResponseModel" = Field()


class MarketGetByIdExtendedResponseModel(BaseModel):
    count: int = Field()
    items: list["MarketMarketItemFull"] = Field()


class MarketGetByIdExtendedResponse(BaseResponse):
    response: "MarketGetByIdExtendedResponseModel" = Field()


class MarketGetByIdResponseModel(BaseModel):
    count: int = Field()
    items: list["MarketMarketItem"] = Field()


class MarketGetByIdResponse(BaseResponse):
    response: "MarketGetByIdResponseModel" = Field()


class MarketGetCategoriesNewResponseModel(BaseModel):
    items: list["MarketMarketCategoryTree"] = Field()


class MarketGetCategoriesNewResponse(BaseResponse):
    response: "MarketGetCategoriesNewResponseModel" = Field()


class MarketGetCommentsResponseModel(BaseModel):
    count: int = Field()
    items: list["WallWallComment"] = Field()
    profiles: list["UsersUserFull"] | None = Field(
        default=None,
    )
    groups: list["GroupsGroupFull"] | None = Field(
        default=None,
    )


class MarketGetCommentsResponse(BaseResponse):
    response: "MarketGetCommentsResponseModel" = Field()


class MarketGetFavesForAttachResponseModel(BaseModel):
    market_items: list["MarketMarketItem"] = Field()
    next_from: int | None = Field(
        default=None,
    )


class MarketGetFavesForAttachResponse(BaseResponse):
    response: "MarketGetFavesForAttachResponseModel" = Field()


class MarketGetGroupOrdersResponseModel(BaseModel):
    count: int = Field()
    items: list["MarketOrder"] = Field()


class MarketGetGroupOrdersResponse(BaseResponse):
    response: "MarketGetGroupOrdersResponseModel" = Field()


class MarketGetOrderByIdResponseModel(BaseModel):
    order: "MarketOrder | None" = Field(
        default=None,
    )


class MarketGetOrderByIdResponse(BaseResponse):
    response: "MarketGetOrderByIdResponseModel" = Field()


class MarketGetOrderItemsResponseModel(BaseModel):
    count: int = Field()
    items: list["MarketOrderItem"] = Field()


class MarketGetOrderItemsResponse(BaseResponse):
    response: "MarketGetOrderItemsResponseModel" = Field()


class MarketGetOrdersExtendedResponseModel(BaseModel):
    count: int = Field()
    items: list["MarketOrder"] = Field()
    groups: list["GroupsGroupFull"] | None = Field(
        default=None,
    )


class MarketGetOrdersExtendedResponse(BaseResponse):
    response: "MarketGetOrdersExtendedResponseModel" = Field()


class MarketGetOrdersResponseModel(BaseModel):
    count: int = Field()
    items: list["MarketOrder"] = Field()


class MarketGetOrdersResponse(BaseResponse):
    response: "MarketGetOrdersResponseModel" = Field()


class MarketGetPropertiesResponseModel(BaseModel):
    items: list["MarketProperty"] = Field()
    count: int = Field()


class MarketGetPropertiesResponse(BaseResponse):
    response: "MarketGetPropertiesResponseModel" = Field()


class MarketGetExtendedResponseModel(BaseModel):
    count: int = Field()
    items: list["MarketMarketItemFull"] = Field()
    variants: list["MarketMarketItemFull"] | None = Field(
        default=None,
    )


class MarketGetExtendedResponse(BaseResponse):
    response: "MarketGetExtendedResponseModel" = Field()


class MarketGetResponseModel(BaseModel):
    count: int = Field()
    items: list["MarketMarketItem"] = Field()
    variants: list["MarketMarketItem"] | None = Field(
        default=None,
    )


class MarketGetResponse(BaseResponse):
    response: "MarketGetResponseModel" = Field()


class MarketGroupItemsResponseModel(BaseModel):
    item_group_id: int = Field()


class MarketGroupItemsResponse(BaseResponse):
    response: "MarketGroupItemsResponseModel" = Field()


class MarketPhotoIdBulkResponse(BaseResponse):
    response: list["MarketUploadPhotoData"] = Field()


class MarketPhotoIdResponseModel(BaseModel):
    photo_id: int = Field()
    photo: "PhotosPhoto | None" = Field(
        default=None,
    )


class MarketPhotoIdResponse(BaseResponse):
    response: "MarketPhotoIdResponseModel" = Field()


class MarketSearchBasicResponseModel(BaseModel):
    count: int = Field()
    total: int = Field()
    items: list["MarketMarketItemBasicWithGroup"] = Field()
    has_more: bool | None = Field(
        default=None,
    )


class MarketSearchBasicResponse(BaseResponse):
    response: "MarketSearchBasicResponseModel" = Field()


class MarketSearchExtendedResponseModel(BaseModel):
    count: int = Field()
    view_type: "MarketServicesViewType" = Field()
    items: list["MarketMarketItemFull"] = Field()
    variants: list["MarketMarketItemFull"] | None = Field(
        default=None,
    )


class MarketSearchExtendedResponse(BaseResponse):
    response: "MarketSearchExtendedResponseModel" = Field()


class MarketSearchResponseModel(BaseModel):
    count: int = Field()
    view_type: "MarketServicesViewType" = Field()
    items: list["MarketMarketItem"] = Field()
    variants: list["MarketMarketItem"] | None = Field(
        default=None,
    )
    groups: list["GroupsGroupFull"] | None = Field(
        default=None,
    )
    filters: "MarketGlobalSearchFilters | None" = Field(
        default=None,
    )


class MarketSearchResponse(BaseResponse):
    response: "MarketSearchResponseModel" = Field()
