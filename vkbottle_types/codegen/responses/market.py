import typing
from vkbottle_types.responses.base_response import BaseResponse, BaseModel
from vkbottle_types.base_model import Field

from vkbottle_types.objects import (
    MarketOwnerType,
    BaseLink,
    MarketMarketCategoryNested,
    MarketMarketItem,
    BaseImage,
    MarketPrice,
    PhotosPhoto,
    BaseBoolInt,
    MarketCurrency,
    MarketMarketItemAvailability,
    BaseRepostsInfo,
    BaseCity,
    MarketMarketCategoryTreeView,
    MarketMarketCategoryTree,
    MarketOrderItem,
    BaseLikes,
    MarketItemPromotionInfo,
    MarketItemOwnerInfo,
    MarketMarketCategory,
    BaseCountry,
)


class MarketCurrencyResponseModel(BaseModel):
    id: int = Field(
        description="Currency ID",
    )

    name: str = Field(
        description="Currency sign",
    )

    title: str = Field(
        description="Currency title",
    )


class MarketCurrencyResponse(BaseResponse):
    response: "MarketCurrencyResponseModel"


class MarketGlobalSearchFiltersResponseModel(BaseModel):
    city: typing.Optional["BaseCity"] = Field(
        default=None,
    )

    country: typing.Optional["BaseCountry"] = Field(
        default=None,
    )


class MarketGlobalSearchFiltersResponse(BaseResponse):
    response: "MarketGlobalSearchFiltersResponseModel"


class MarketItemOwnerInfoResponseModel(BaseModel):
    avatar: typing.Optional[typing.List[BaseImage]] = Field(
        default=None,
        description="Avatar of the group",
    )

    name: typing.Optional[str] = Field(
        default=None,
        description="Name of the group",
    )

    category: typing.Optional[str] = Field(
        default=None,
        description="Category of the item or description of the group",
    )

    category_url: typing.Optional[str] = Field(
        default=None,
        description="Link to the section of the group",
    )

    is_corporated_market: typing.Optional[bool] = Field(
        default=None,
        description="Is the group is VK corporated market",
    )

    market_type: typing.Optional["MarketOwnerType"] = Field(
        default=None,
        description="Type of the market group",
    )


class MarketItemOwnerInfoResponse(BaseResponse):
    response: "MarketItemOwnerInfoResponseModel"


class MarketItemPromotionInfoResponseModel(BaseModel):
    is_available: typing.Optional[bool] = Field(
        default=None,
        description="Can the item be promoted?",
    )


class MarketItemPromotionInfoResponse(BaseResponse):
    response: "MarketItemPromotionInfoResponseModel"


class MarketMarketAlbumResponseModel(BaseModel):
    id: int = Field(
        description="Market album ID",
    )

    owner_id: int = Field(
        description="Market album owner's ID",
    )

    title: str = Field(
        description="Market album title",
    )

    count: int = Field(
        description="Items number",
    )

    updated_time: int = Field(
        description="Date when album has been updated last time in Unixtime",
    )

    is_main: typing.Optional[bool] = Field(
        default=None,
        description="Is album main for owner",
    )

    is_hidden: typing.Optional[bool] = Field(
        default=None,
        description="Is album hidden",
    )

    photo: typing.Optional["PhotosPhoto"] = Field(
        default=None,
    )

    type: typing.Optional[int] = Field(
        default=None,
        description="Type of album",
    )

    is_blur_enabled: typing.Optional[bool] = Field(
        default=None,
        description="Is album needed to be blurred (18+) or not",
    )


class MarketMarketAlbumResponse(BaseResponse):
    response: "MarketMarketAlbumResponseModel"


class MarketMarketCategoryResponseModel(BaseModel):
    pass


class MarketMarketCategoryResponse(BaseResponse):
    response: "MarketMarketCategoryResponseModel"


class MarketMarketCategoryNestedResponseModel(BaseModel):
    id: int = Field(
        description="Category ID",
    )

    name: str = Field(
        description="Category name",
    )

    is_v2: typing.Optional[bool] = Field(
        default=None,
        description="Is v2 category",
    )

    parent: typing.Optional["MarketMarketCategoryNested"] = Field(
        default=None,
    )


class MarketMarketCategoryNestedResponse(BaseResponse):
    response: "MarketMarketCategoryNestedResponseModel"


class MarketMarketCategoryTreeResponseModel(BaseModel):
    id: int = Field(
        description="Category ID",
    )

    name: str = Field(
        description="Category name",
    )

    icon_name: typing.Optional[str] = Field(
        default=None,
        description="Icon name",
    )

    children: typing.Optional[typing.List[MarketMarketCategoryTree]] = Field(
        default=None,
    )

    view: typing.Optional["MarketMarketCategoryTreeView"] = Field(
        default=None,
    )

    url: typing.Optional[str] = Field(
        default=None,
        description="SEO-friendly URL to page with category's items",
    )


class MarketMarketCategoryTreeResponse(BaseResponse):
    response: "MarketMarketCategoryTreeResponseModel"


class MarketMarketCategoryTreeViewResponseModel(BaseModel):
    type: typing.Optional[typing.Literal["tab_root"]] = Field(
        default=None,
    )

    selected: typing.Optional[bool] = Field(
        default=None,
    )

    root_path: typing.Optional[typing.List[str]] = Field(
        default=None,
    )


class MarketMarketCategoryTreeViewResponse(BaseResponse):
    response: "MarketMarketCategoryTreeViewResponseModel"


class MarketMarketItemResponseModel(BaseModel):
    availability: "MarketMarketItemAvailability" = Field()

    category: "MarketMarketCategory" = Field()

    description: str = Field(
        description="Item description",
    )

    id: int = Field(
        description="Item ID",
    )

    owner_id: int = Field(
        description="Item owner's ID",
    )

    price: "MarketPrice" = Field()

    title: str = Field(
        description="Item title",
    )

    access_key: typing.Optional[str] = Field(
        default=None,
        description="Access key for the market item",
    )

    button_title: typing.Optional[str] = Field(
        default=None,
        description="Title for button for url",
    )

    category_v2: typing.Optional["MarketMarketCategory"] = Field(
        default=None,
    )

    date: typing.Optional[int] = Field(
        default=None,
        description="Date when the item has been created in Unixtime",
    )

    external_id: typing.Optional[str] = Field(
        default=None,
    )

    is_favorite: typing.Optional[bool] = Field(
        default=None,
    )

    is_owner: typing.Optional[bool] = Field(
        default=None,
    )

    is_adult: typing.Optional[bool] = Field(
        default=None,
    )

    thumb_photo: typing.Optional[str] = Field(
        default=None,
        description="URL of the preview image",
    )

    url: typing.Optional[str] = Field(
        default=None,
        description="URL to item",
    )

    variants_grouping_id: typing.Optional[int] = Field(
        default=None,
    )

    is_main_variant: typing.Optional[bool] = Field(
        default=None,
    )

    sku: typing.Optional[str] = Field(
        default=None,
    )

    stock_amount: typing.Optional[int] = Field(
        default=None,
        description="Inventory balances",
    )

    post_id: typing.Optional[int] = Field(
        default=None,
        description="Attach for post id",
    )

    post_owner_id: typing.Optional[int] = Field(
        default=None,
        description="Attach for post owner id",
    )


class MarketMarketItemResponse(BaseResponse):
    response: "MarketMarketItemResponseModel"


class MarketMarketItemAvailabilityResponseModel(enum.IntEnum):
    AVAILABLE = 0

    REMOVED = 1

    UNAVAILABLE = 2


class MarketMarketItemAvailabilityResponse(BaseResponse):
    response: "MarketMarketItemAvailabilityResponseModel"


class MarketMarketItemBasicResponseModel(BaseModel):
    id: int = Field(
        description="Item ID",
    )

    owner_id: int = Field(
        description="Item owner's ID",
    )

    title: str = Field(
        description="Item title",
    )

    price: "MarketPrice" = Field()

    thumb_photo: typing.Optional[str] = Field(
        default=None,
        description="URL of the preview image",
    )

    is_favorite: typing.Optional[bool] = Field(
        default=None,
    )


class MarketMarketItemBasicResponse(BaseResponse):
    response: "MarketMarketItemBasicResponseModel"


class MarketMarketItemBasicWithGroupResponseModel(MarketMarketItemBasic):
    is_group_verified: typing.Optional[bool] = Field(
        default=None,
    )

    group_name: typing.Optional[str] = Field(
        default=None,
    )

    group_link: typing.Optional[str] = Field(
        default=None,
    )

    is_owner: typing.Optional[bool] = Field(
        default=None,
    )

    is_adult: typing.Optional[bool] = Field(
        default=None,
    )


class MarketMarketItemBasicWithGroupResponse(BaseResponse):
    response: "MarketMarketItemBasicWithGroupResponseModel"


class MarketMarketItemFullResponseModel(MarketMarketItem):
    albums_ids: typing.Optional[typing.List[int]] = Field(
        default=None,
    )

    photos: typing.Optional[typing.List[PhotosPhoto]] = Field(
        default=None,
    )

    can_comment: typing.Optional[bool] = Field(
        default=None,
        description="Information whether current use can comment the item",
    )

    can_repost: typing.Optional[bool] = Field(
        default=None,
        description="Information whether current use can repost the item",
    )

    likes: typing.Optional["BaseLikes"] = Field(
        default=None,
    )

    reposts: typing.Optional["BaseRepostsInfo"] = Field(
        default=None,
    )

    views_count: typing.Optional[int] = Field(
        default=None,
        description="Views number",
    )

    wishlist_item_id: typing.Optional[int] = Field(
        default=None,
        description="Object identifier in wishlist of viewer",
    )

    rating: typing.Optional[float] = Field(
        default=None,
        description="Rating of product",
    )

    orders_count: typing.Optional[int] = Field(
        default=None,
        description="Count of product orders",
    )

    cancel_info: typing.Optional["BaseLink"] = Field(
        default=None,
        description="Information for cancel and revert order",
    )

    user_agreement_info: typing.Optional[str] = Field(
        default=None,
        description="User agreement info",
    )

    ad_id: typing.Optional[int] = Field(
        default=None,
        description="Contains ad ID if it has",
    )

    owner_info: typing.Optional["MarketItemOwnerInfo"] = Field(
        default=None,
        description="Information about the group where the item is placed",
    )

    can_edit: typing.Optional[bool] = Field(
        default=None,
        description="Can the item be updated by current user?",
    )

    can_delete: typing.Optional[bool] = Field(
        default=None,
        description="Can item be deleted by current user?",
    )

    can_show_convert_to_service: typing.Optional[bool] = Field(
        default=None,
        description="Can the item be converted from a product into a service?",
    )

    promotion: typing.Optional["MarketItemPromotionInfo"] = Field(
        default=None,
        description="Information about promotion of the item",
    )

    vk_pay_discount: typing.Optional[int] = Field(
        default=None,
        description="The amount of the discount if VK Pay is used for payment",
    )


class MarketMarketItemFullResponse(BaseResponse):
    response: "MarketMarketItemFullResponseModel"


class MarketOrderResponseModel(BaseModel):
    id: int = Field()

    group_id: int = Field()

    user_id: int = Field()

    date: int = Field()

    status: int = Field()

    items_count: int = Field()

    total_price: "MarketPrice" = Field()

    display_order_id: typing.Optional[str] = Field(
        default=None,
    )

    track_number: typing.Optional[str] = Field(
        default=None,
    )

    track_link: typing.Optional[str] = Field(
        default=None,
    )

    comment: typing.Optional[str] = Field(
        default=None,
    )

    address: typing.Optional[str] = Field(
        default=None,
    )

    merchant_comment: typing.Optional[str] = Field(
        default=None,
    )

    weight: typing.Optional[int] = Field(
        default=None,
    )

    discount: typing.Optional["MarketPrice"] = Field(
        default=None,
    )

    preview_order_items: typing.Optional[typing.List[MarketOrderItem]] = Field(
        default=None,
        description="Several order items for preview",
    )

    cancel_info: typing.Optional["BaseLink"] = Field(
        default=None,
        description="Information for cancel and revert order",
    )

    comment_for_user: typing.Optional[str] = Field(
        default=None,
        description="Seller comment for user",
    )

    is_viewed_by_admin: typing.Optional[bool] = Field(
        default=None,
    )

    date_viewed: typing.Optional[int] = Field(
        default=None,
    )

    can_add_review: typing.Optional[bool] = Field(
        default=None,
        description="Extended field. Can current viewer add review for at least one item in this order",
    )


class MarketOrderResponse(BaseResponse):
    response: "MarketOrderResponseModel"


class MarketOrderItemResponseModel(BaseModel):
    owner_id: int = Field()

    item_id: int = Field()

    price: "MarketPrice" = Field()

    quantity: int = Field()

    item: "MarketMarketItem" = Field()

    title: typing.Optional[str] = Field(
        default=None,
    )

    photo: typing.Optional["PhotosPhoto"] = Field(
        default=None,
    )

    variants: typing.Optional[typing.List[str]] = Field(
        default=None,
    )

    can_add_review: typing.Optional[bool] = Field(
        default=None,
        description="Extended field. Can current viewer add review for this ordered item",
    )


class MarketOrderItemResponse(BaseResponse):
    response: "MarketOrderItemResponseModel"


class MarketOwnerTypeResponseModel(enum.Enum):
    BASE = "base"

    PRO = "pro"

    DISABLED = "disabled"


class MarketOwnerTypeResponse(BaseResponse):
    response: "MarketOwnerTypeResponseModel"


class MarketPriceResponseModel(BaseModel):
    amount: str = Field(
        description="Amount",
    )

    currency: "MarketCurrency" = Field()

    text: str = Field(
        description="Text",
    )

    amount_to: typing.Optional[str] = Field(
        default=None,
        description="Amount to for price_type=2",
    )

    price_type: typing.Optional[int] = Field(
        default=None,
    )

    price_unit: typing.Optional[int] = Field(
        default=None,
    )

    discount_rate: typing.Optional[int] = Field(
        default=None,
    )

    old_amount: typing.Optional[str] = Field(
        default=None,
    )

    old_amount_text: typing.Optional[str] = Field(
        default=None,
        description="Textual representation of old price",
    )


class MarketPriceResponse(BaseResponse):
    response: "MarketPriceResponseModel"


class MarketServicesViewTypeResponseModel(enum.IntEnum):
    CARDS = 1

    ROWS = 2


class MarketServicesViewTypeResponse(BaseResponse):
    response: "MarketServicesViewTypeResponseModel"
