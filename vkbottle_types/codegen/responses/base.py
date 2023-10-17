import typing
import enum
from vkbottle_types.responses.base_response import BaseResponse, BaseModel
from vkbottle_types.base_model import Field

from vkbottle_types.objects import (
    BaseLinkButtonAction,
    BaseLinkApplicationStore,
    BaseLinkButtonActionType,
    BaseLinkButton,
    MarketPrice,
    BaseLinkProduct,
    BaseImage,
    BaseStickerAnimation,
    BaseRequestParam,
    PhotosPhoto,
    BaseGeoCoordinates,
    BaseLinkProductStatus,
    BaseStickerNew,
    BaseLinkRating,
    BaseCropPhotoRect,
    BaseLinkButtonStyle,
    WallWallComment,
    BasePlace,
    BaseLinkProductCategory,
    BaseLinkApplication,
    BaseBoolInt,
    LinkTargetObject,
    VideoVideoFull,
    WallWallpostCommentsDonut,
    BaseCropPhotoCrop,
    BaseOwnerCoverCropParams,
)


class BaseBoolIntResponseModel(enum.IntEnum):
    NO = 0

    YES = 1


class BaseBoolIntResponse(BaseResponse):
    response: "BaseBoolIntResponseModel"


class BaseCityResponseModel(BaseModel):
    id: int = Field(
        description="City ID",
    )

    title: str = Field(
        description="City title",
    )


class BaseCityResponse(BaseResponse):
    response: "BaseCityResponseModel"


class BaseCommentsInfoResponseModel(BaseModel):
    can_post: typing.Optional[bool] = Field(
        default=None,
        description="Information whether current user can comment the post",
    )

    can_open: typing.Optional[bool] = Field(
        default=None,
    )

    can_close: typing.Optional[bool] = Field(
        default=None,
    )

    can_view: typing.Optional[bool] = Field(
        default=None,
        description="Information whether current user can view the comments",
    )

    count: typing.Optional[int] = Field(
        default=None,
        description="Comments number",
    )

    groups_can_post: typing.Optional[bool] = Field(
        default=None,
        description="Information whether groups can comment the post",
    )

    donut: typing.Optional["WallWallpostCommentsDonut"] = Field(
        default=None,
    )

    list: typing.Optional[typing.List[WallWallComment]] = Field(
        default=None,
    )


class BaseCommentsInfoResponse(BaseResponse):
    response: "BaseCommentsInfoResponseModel"


class BaseCountryResponseModel(BaseModel):
    id: int = Field(
        description="Country ID",
    )

    title: str = Field(
        description="Country title",
    )


class BaseCountryResponse(BaseResponse):
    response: "BaseCountryResponseModel"


class BaseCropPhotoResponseModel(BaseModel):
    photo: "PhotosPhoto" = Field()

    crop: "BaseCropPhotoCrop" = Field()

    rect: "BaseCropPhotoRect" = Field()


class BaseCropPhotoResponse(BaseResponse):
    response: "BaseCropPhotoResponseModel"


class BaseCropPhotoCropResponseModel(BaseModel):
    x: float = Field(
        description="Coordinate X of the left upper corner",
    )

    y: float = Field(
        description="Coordinate Y of the left upper corner",
    )

    x2: float = Field(
        description="Coordinate X of the right lower corner",
    )

    y2: float = Field(
        description="Coordinate Y of the right lower corner",
    )


class BaseCropPhotoCropResponse(BaseResponse):
    response: "BaseCropPhotoCropResponseModel"


class BaseCropPhotoRectResponseModel(BaseModel):
    x: float = Field(
        description="Coordinate X of the left upper corner",
    )

    y: float = Field(
        description="Coordinate Y of the left upper corner",
    )

    x2: float = Field(
        description="Coordinate X of the right lower corner",
    )

    y2: float = Field(
        description="Coordinate Y of the right lower corner",
    )


class BaseCropPhotoRectResponse(BaseResponse):
    response: "BaseCropPhotoRectResponseModel"


class BaseErrorResponseModel(BaseModel):
    error_code: int = Field(
        description="Error code",
    )

    error_subcode: typing.Optional[int] = Field(
        default=None,
        description="Error subcode",
    )

    error_msg: typing.Optional[str] = Field(
        default=None,
        description="Error message",
    )

    error_text: typing.Optional[str] = Field(
        default=None,
        description="Localized error message",
    )

    request_params: typing.Optional[typing.List[BaseRequestParam]] = Field(
        default=None,
    )


class BaseErrorResponse(BaseResponse):
    response: "BaseErrorResponseModel"


class BaseGeoResponseModel(BaseModel):
    coordinates: typing.Optional["BaseGeoCoordinates"] = Field(
        default=None,
    )

    place: typing.Optional["BasePlace"] = Field(
        default=None,
    )

    showmap: typing.Optional[int] = Field(
        default=None,
        description="Information whether a map is showed",
    )

    type: typing.Optional[str] = Field(
        default=None,
        description="Place type",
    )


class BaseGeoResponse(BaseResponse):
    response: "BaseGeoResponseModel"


class BaseGeoCoordinatesResponseModel(BaseModel):
    latitude: float = Field()

    longitude: float = Field()


class BaseGeoCoordinatesResponse(BaseResponse):
    response: "BaseGeoCoordinatesResponseModel"


class BaseGradientPointResponseModel(BaseModel):
    color: str = Field(
        description="Hex color code without #",
    )

    position: float = Field(
        description="Point position",
    )


class BaseGradientPointResponse(BaseResponse):
    response: "BaseGradientPointResponseModel"


class BaseImageResponseModel(BaseModel):
    url: str = Field(
        description="Image url",
    )

    width: int = Field(
        description="Image width",
    )

    height: int = Field(
        description="Image height",
    )

    id: typing.Optional[str] = Field(
        default=None,
    )

    theme: typing.Optional[typing.Literal["light", "dark"]] = Field(
        default=None,
    )


class BaseImageResponse(BaseResponse):
    response: "BaseImageResponseModel"


class BaseLangResponseModel(enum.Enum):
    RU = "ru"

    UA = "ua"

    BE = "be"

    EN = "en"

    ES = "es"

    FI = "fi"

    DE = "de"

    IT = "it"


class BaseLangResponse(BaseResponse):
    response: "BaseLangResponseModel"


class BaseLikesResponseModel(BaseModel):
    count: typing.Optional[int] = Field(
        default=None,
        description="Likes number",
    )

    user_likes: typing.Optional[bool] = Field(
        default=None,
        description="Information whether current user likes the photo",
    )


class BaseLikesResponse(BaseResponse):
    response: "BaseLikesResponseModel"


class BaseLikesInfoResponseModel(BaseModel):
    can_like: bool = Field(
        description="Information whether current user can like the post",
    )

    count: int = Field(
        description="Likes number",
    )

    user_likes: bool = Field(
        description="Information whether current uer has liked the post",
    )

    can_publish: typing.Optional[bool] = Field(
        default=None,
        description="Information whether current user can repost",
    )

    repost_disabled: typing.Optional[bool] = Field(
        default=None,
        description="Remove repost feature for post",
    )


class BaseLikesInfoResponse(BaseResponse):
    response: "BaseLikesInfoResponseModel"


class BaseLinkResponseModel(BaseLinkNoProduct):
    text: typing.Optional[str] = Field(
        default=None,
    )

    product: typing.Optional["BaseLinkProduct"] = Field(
        default=None,
    )


class BaseLinkResponse(BaseResponse):
    response: "BaseLinkResponseModel"


class BaseLinkApplicationResponseModel(BaseModel):
    app_id: typing.Optional[float] = Field(
        default=None,
        description="Application Id",
    )

    store: typing.Optional["BaseLinkApplicationStore"] = Field(
        default=None,
    )


class BaseLinkApplicationResponse(BaseResponse):
    response: "BaseLinkApplicationResponseModel"


class BaseLinkApplicationStoreResponseModel(BaseModel):
    id: typing.Optional[float] = Field(
        default=None,
        description="Store Id",
    )

    name: typing.Optional[str] = Field(
        default=None,
        description="Store name",
    )


class BaseLinkApplicationStoreResponse(BaseResponse):
    response: "BaseLinkApplicationStoreResponseModel"


class BaseLinkButtonResponseModel(BaseModel):
    action: typing.Optional["BaseLinkButtonAction"] = Field(
        default=None,
        description="Button action",
    )

    title: typing.Optional[str] = Field(
        default=None,
        description="Button title",
    )

    block_id: typing.Optional[str] = Field(
        default=None,
        description="Target block id",
    )

    section_id: typing.Optional[str] = Field(
        default=None,
        description="Target section id",
    )

    artist_id: typing.Optional[str] = Field(
        default=None,
        description="artist id",
    )

    curator_id: typing.Optional[int] = Field(
        default=None,
        description="curator id",
    )

    album_id: typing.Optional[int] = Field(
        default=None,
        description="Video album id",
    )

    owner_id: typing.Optional[int] = Field(
        default=None,
        description="Owner id",
    )

    icon: typing.Optional[str] = Field(
        default=None,
        description="Button icon name, e.g. 'phone' or 'gift'",
    )

    style: typing.Optional["BaseLinkButtonStyle"] = Field(
        default=None,
    )

    audio_id: typing.Optional[int] = Field(
        default=None,
    )

    hashtag: typing.Optional[str] = Field(
        default=None,
    )


class BaseLinkButtonResponse(BaseResponse):
    response: "BaseLinkButtonResponseModel"


class BaseLinkButtonActionResponseModel(BaseModel):
    type: "BaseLinkButtonActionType" = Field()

    url: typing.Optional[str] = Field(
        default=None,
        description="Action URL",
    )

    consume_reason: typing.Optional[str] = Field(
        default=None,
    )


class BaseLinkButtonActionResponse(BaseResponse):
    response: "BaseLinkButtonActionResponseModel"


class BaseLinkButtonActionTypeResponseModel(enum.Enum):
    OPEN_URL = "open_url"

    MARKET_CLEAR_RECENT_QUERIES = "market_clear_recent_queries"

    CLOSE_WEB_APP = "close_web_app"

    OPEN_SEARCH_TAB = "open_search_tab"

    IMPORT_CONTACTS = "import_contacts"

    ADD_FRIENDS = "add_friends"

    ONBOARDING = "onboarding"


class BaseLinkButtonActionTypeResponse(BaseResponse):
    response: "BaseLinkButtonActionTypeResponseModel"


class BaseLinkButtonStyleResponseModel(enum.Enum):
    PRIMARY = "primary"

    SECONDARY = "secondary"


class BaseLinkButtonStyleResponse(BaseResponse):
    response: "BaseLinkButtonStyleResponseModel"


class BaseLinkNoProductResponseModel(BaseModel):
    url: str = Field(
        description="Link URL",
    )

    application: typing.Optional["BaseLinkApplication"] = Field(
        default=None,
    )

    button: typing.Optional["BaseLinkButton"] = Field(
        default=None,
    )

    caption: typing.Optional[str] = Field(
        default=None,
        description="Link caption",
    )

    description: typing.Optional[str] = Field(
        default=None,
        description="Link description",
    )

    id: typing.Optional[str] = Field(
        default=None,
        description="Link ID",
    )

    is_favorite: typing.Optional[bool] = Field(
        default=None,
    )

    photo: typing.Optional["PhotosPhoto"] = Field(
        default=None,
    )

    preview_page: typing.Optional[str] = Field(
        default=None,
        description="String ID of the page with article preview",
    )

    preview_url: typing.Optional[str] = Field(
        default=None,
        description="URL of the page with article preview",
    )

    rating: typing.Optional["BaseLinkRating"] = Field(
        default=None,
    )

    title: typing.Optional[str] = Field(
        default=None,
        description="Link title",
    )

    target_object: typing.Optional["LinkTargetObject"] = Field(
        default=None,
    )

    is_external: typing.Optional[bool] = Field(
        default=None,
        description="Information whether the current link is external",
    )

    video: typing.Optional["VideoVideoFull"] = Field(
        default=None,
        description="Video from link",
    )


class BaseLinkNoProductResponse(BaseResponse):
    response: "BaseLinkNoProductResponseModel"


class BaseLinkProductResponseModel(BaseModel):
    price: "MarketPrice" = Field()

    merchant: typing.Optional[str] = Field(
        default=None,
    )

    category: typing.Optional["BaseLinkProductCategory"] = Field(
        default=None,
    )

    geo: typing.Optional["BaseGeoCoordinates"] = Field(
        default=None,
    )

    distance: typing.Optional[int] = Field(
        default=None,
    )

    city: typing.Optional[str] = Field(
        default=None,
    )

    status: typing.Optional["BaseLinkProductStatus"] = Field(
        default=None,
    )

    orders_count: typing.Optional[int] = Field(
        default=None,
    )

    type: typing.Optional[typing.Literal["product"]] = Field(
        default=None,
    )


class BaseLinkProductResponse(BaseResponse):
    response: "BaseLinkProductResponseModel"


class BaseLinkProductCategoryResponseModel(BaseModel):
    pass


class BaseLinkProductCategoryResponse(BaseResponse):
    response: "BaseLinkProductCategoryResponseModel"


class BaseLinkProductStatusResponseModel(enum.Enum):
    ACTIVE = "active"

    BLOCKED = "blocked"

    SOLD = "sold"

    DELETED = "deleted"

    ARCHIVED = "archived"


class BaseLinkProductStatusResponse(BaseResponse):
    response: "BaseLinkProductStatusResponseModel"


class BaseLinkRatingResponseModel(BaseModel):
    reviews_count: typing.Optional[int] = Field(
        default=None,
        description="Count of reviews",
    )

    stars: typing.Optional[float] = Field(
        default=None,
        description="Count of stars",
    )

    type: typing.Optional[typing.Literal["rating"]] = Field(
        default=None,
    )


class BaseLinkRatingResponse(BaseResponse):
    response: "BaseLinkRatingResponseModel"


class BaseMessageErrorResponseModel(BaseModel):
    code: typing.Optional[int] = Field(
        default=None,
        description="Error code",
    )

    description: typing.Optional[str] = Field(
        default=None,
        description="Error message",
    )


class BaseMessageErrorResponse(BaseResponse):
    response: "BaseMessageErrorResponseModel"


class BaseNameCaseResponseModel(enum.Enum):
    NOM = "Nom"

    GEN = "Gen"

    DAT = "Dat"

    ACC = "Acc"

    INS = "Ins"

    ABL = "Abl"


class BaseNameCaseResponse(BaseResponse):
    response: "BaseNameCaseResponseModel"


class BaseObjectResponseModel(BaseModel):
    id: int = Field(
        description="Object ID",
    )

    title: str = Field(
        description="Object title",
    )


class BaseObjectResponse(BaseResponse):
    response: "BaseObjectResponseModel"


class BaseObjectCountResponseModel(BaseModel):
    count: typing.Optional[int] = Field(
        default=None,
        description="Items count",
    )


class BaseObjectCountResponse(BaseResponse):
    response: "BaseObjectCountResponseModel"


class BaseObjectWithNameResponseModel(BaseModel):
    id: int = Field(
        description="Object ID",
    )

    name: str = Field(
        description="Object name",
    )


class BaseObjectWithNameResponse(BaseResponse):
    response: "BaseObjectWithNameResponseModel"


class BaseOwnerCoverResponseModel(BaseModel):
    enabled: bool = Field(
        description="Information whether cover is enabled",
    )

    images: typing.Optional[typing.List[BaseImage]] = Field(
        default=None,
    )

    crop_params: typing.Optional["BaseOwnerCoverCropParams"] = Field(
        default=None,
    )

    original_image: typing.Optional["BaseImage"] = Field(
        default=None,
    )

    photo_id: typing.Optional[int] = Field(
        default=None,
    )


class BaseOwnerCoverResponse(BaseResponse):
    response: "BaseOwnerCoverResponseModel"


class BaseOwnerCoverCropParamsResponseModel(BaseModel):
    x: typing.Optional[int] = Field(
        default=None,
    )

    y: typing.Optional[int] = Field(
        default=None,
    )

    width: typing.Optional[int] = Field(
        default=None,
    )

    height: typing.Optional[int] = Field(
        default=None,
    )


class BaseOwnerCoverCropParamsResponse(BaseResponse):
    response: "BaseOwnerCoverCropParamsResponseModel"


class BasePlaceResponseModel(BaseModel):
    address: typing.Optional[str] = Field(
        default=None,
        description="Place address",
    )

    checkins: typing.Optional[int] = Field(
        default=None,
        description="Checkins number",
    )

    city: typing.Optional[str] = Field(
        default=None,
        description="City name",
    )

    country: typing.Optional[str] = Field(
        default=None,
        description="Country name",
    )

    created: typing.Optional[int] = Field(
        default=None,
        description="Date of the place creation in Unixtime",
    )

    icon: typing.Optional[str] = Field(
        default=None,
        description="URL of the place's icon",
    )

    id: typing.Optional[int] = Field(
        default=None,
        description="Place ID",
    )

    latitude: typing.Optional[float] = Field(
        default=None,
        description="Place latitude",
    )

    longitude: typing.Optional[float] = Field(
        default=None,
        description="Place longitude",
    )

    title: typing.Optional[str] = Field(
        default=None,
        description="Place title",
    )

    type: typing.Optional[str] = Field(
        default=None,
        description="Place type",
    )


class BasePlaceResponse(BaseResponse):
    response: "BasePlaceResponseModel"


class BasePropertyExistsResponseModel(enum.IntEnum):
    PROPERTY_EXISTS = 1


class BasePropertyExistsResponse(BaseResponse):
    response: "BasePropertyExistsResponseModel"


class BaseRepostsInfoResponseModel(BaseModel):
    count: int = Field(
        description="Total reposts counter. Sum of wall and mail reposts counters",
    )

    wall_count: typing.Optional[int] = Field(
        default=None,
        description="Wall reposts counter",
    )

    mail_count: typing.Optional[int] = Field(
        default=None,
        description="Mail reposts counter",
    )

    user_reposted: typing.Optional[bool] = Field(
        default=None,
        description="Information whether current user has reposted the post",
    )


class BaseRepostsInfoResponse(BaseResponse):
    response: "BaseRepostsInfoResponseModel"


class BaseRequestParamResponseModel(BaseModel):
    key: str = Field(
        description="Parameter name",
    )

    value: str = Field(
        description="Parameter value",
    )


class BaseRequestParamResponse(BaseResponse):
    response: "BaseRequestParamResponseModel"


class BaseSexResponseModel(enum.IntEnum):
    UNKNOWN = 0

    FEMALE = 1

    MALE = 2


class BaseSexResponse(BaseResponse):
    response: "BaseSexResponseModel"


class BaseStickerResponseModel(BaseModel):
    pass


class BaseStickerResponse(BaseResponse):
    response: "BaseStickerResponseModel"


class BaseStickerAnimationResponseModel(BaseModel):
    type: typing.Optional[typing.Literal["light", "dark"]] = Field(
        default=None,
        description="Type of animation script",
    )

    url: typing.Optional[str] = Field(
        default=None,
        description="URL of animation script",
    )


class BaseStickerAnimationResponse(BaseResponse):
    response: "BaseStickerAnimationResponseModel"


class BaseStickerNewResponseModel(BaseModel):
    sticker_id: typing.Optional[int] = Field(
        default=None,
        description="Sticker ID",
    )

    product_id: typing.Optional[int] = Field(
        default=None,
        description="Pack ID",
    )

    images: typing.Optional[typing.List[BaseImage]] = Field(
        default=None,
    )

    images_with_background: typing.Optional[typing.List[BaseImage]] = Field(
        default=None,
    )

    animation_url: typing.Optional[str] = Field(
        default=None,
        description="URL of sticker animation script",
    )

    animations: typing.Optional[typing.List[BaseStickerAnimation]] = Field(
        default=None,
        description="Array of sticker animation script objects",
    )

    is_allowed: typing.Optional[bool] = Field(
        default=None,
        description="Information whether the sticker is allowed",
    )


class BaseStickerNewResponse(BaseResponse):
    response: "BaseStickerNewResponseModel"


class BaseStickerOldResponseModel(BaseModel):
    id: typing.Optional[int] = Field(
        default=None,
        description="Sticker ID",
    )

    product_id: typing.Optional[int] = Field(
        default=None,
        description="Pack ID",
    )

    width: typing.Optional[int] = Field(
        default=None,
        description="Width in px",
    )

    height: typing.Optional[int] = Field(
        default=None,
        description="Height in px",
    )

    photo_128: typing.Optional[str] = Field(
        default=None,
        description="URL of the preview image with 128 px in height",
    )

    photo_256: typing.Optional[str] = Field(
        default=None,
        description="URL of the preview image with 256 px in height",
    )

    photo_352: typing.Optional[str] = Field(
        default=None,
        description="URL of the preview image with 352 px in height",
    )

    photo_512: typing.Optional[str] = Field(
        default=None,
        description="URL of the preview image with 512 px in height",
    )

    photo_64: typing.Optional[str] = Field(
        default=None,
        description="URL of the preview image with 64 px in height",
    )

    is_allowed: typing.Optional[bool] = Field(
        default=None,
        description="Information whether the sticker is allowed",
    )


class BaseStickerOldResponse(BaseResponse):
    response: "BaseStickerOldResponseModel"


BaseStickersListResponseModel = typing.List["BaseStickerNew"]


class BaseStickersListResponse(BaseResponse):
    response: "BaseStickersListResponseModel"


class BaseUploadServerResponseModel(BaseModel):
    upload_url: str = Field(
        description="Upload URL",
    )


class BaseUploadServerResponse(BaseResponse):
    response: "BaseUploadServerResponseModel"


class BaseUserGroupFieldsResponseModel(enum.Enum):
    ABOUT = "about"

    ACTION_BUTTON = "action_button"

    ACTIVITIES = "activities"

    ACTIVITY = "activity"

    ADDRESSES = "addresses"

    ADMIN_LEVEL = "admin_level"

    AGE_LIMITS = "age_limits"

    AUTHOR_ID = "author_id"

    BAN_INFO = "ban_info"

    BDATE = "bdate"

    BLACKLISTED = "blacklisted"

    BLACKLISTED_BY_ME = "blacklisted_by_me"

    BOOKS = "books"

    CAN_BAN = "can_ban"

    CAN_CREATE_TOPIC = "can_create_topic"

    CAN_MESSAGE = "can_message"

    CAN_POST = "can_post"

    CAN_SEE_ALL_POSTS = "can_see_all_posts"

    CAN_SEE_AUDIO = "can_see_audio"

    CAN_SEND_FRIEND_REQUEST = "can_send_friend_request"

    CAN_UPLOAD_VIDEO = "can_upload_video"

    CAN_WRITE_PRIVATE_MESSAGE = "can_write_private_message"

    CAREER = "career"

    CITY = "city"

    COMMON_COUNT = "common_count"

    CONNECTIONS = "connections"

    CONTACTS = "contacts"

    COUNTERS = "counters"

    COUNTRY = "country"

    COVER = "cover"

    CROP_PHOTO = "crop_photo"

    DEACTIVATED = "deactivated"

    DESCRIPTION = "description"

    DOMAIN = "domain"

    EDUCATION = "education"

    EXPORTS = "exports"

    FINISH_DATE = "finish_date"

    FIXED_POST = "fixed_post"

    FOLLOWERS_COUNT = "followers_count"

    FRIEND_STATUS = "friend_status"

    GAMES = "games"

    HAS_MARKET_APP = "has_market_app"

    HAS_MOBILE = "has_mobile"

    HAS_PHOTO = "has_photo"

    HOME_TOWN = "home_town"

    ID = "id"

    INTERESTS = "interests"

    IS_ADMIN = "is_admin"

    IS_CLOSED = "is_closed"

    IS_FAVORITE = "is_favorite"

    IS_FRIEND = "is_friend"

    IS_BEST_FRIEND = "is_best_friend"

    IS_HIDDEN_FROM_FEED = "is_hidden_from_feed"

    IS_MEMBER = "is_member"

    IS_MESSAGES_BLOCKED = "is_messages_blocked"

    CAN_SEND_NOTIFY = "can_send_notify"

    IS_SUBSCRIBED = "is_subscribed"

    LAST_SEEN = "last_seen"

    LINKS = "links"

    LISTS = "lists"

    MAIDEN_NAME = "maiden_name"

    MAIN_ALBUM_ID = "main_album_id"

    MAIN_SECTION = "main_section"

    MARKET = "market"

    MEMBER_STATUS = "member_status"

    MEMBERS_COUNT = "members_count"

    MILITARY = "military"

    MOVIES = "movies"

    MUSIC = "music"

    NAME = "name"

    NICKNAME = "nickname"

    OCCUPATION = "occupation"

    ONLINE = "online"

    ONLINE_STATUS = "online_status"

    PERSONAL = "personal"

    PHONE = "phone"

    PHOTO_100 = "photo_100"

    PHOTO_200 = "photo_200"

    PHOTO_200_ORIG = "photo_200_orig"

    PHOTO_400_ORIG = "photo_400_orig"

    PHOTO_50 = "photo_50"

    PHOTO_ID = "photo_id"

    PHOTO_MAX = "photo_max"

    PHOTO_MAX_ORIG = "photo_max_orig"

    PHOTO_AVG_COLOR = "photo_avg_color"

    QUOTES = "quotes"

    RELATION = "relation"

    RELATIVES = "relatives"

    SCHOOLS = "schools"

    SCREEN_NAME = "screen_name"

    SEX = "sex"

    SITE = "site"

    START_DATE = "start_date"

    STATUS = "status"

    TIMEZONE = "timezone"

    TRENDING = "trending"

    TV = "tv"

    TYPE = "type"

    UNIVERSITIES = "universities"

    VERIFIED = "verified"

    WALL_COMMENTS = "wall_comments"

    WIKI_PAGE = "wiki_page"

    FIRST_NAME = "first_name"

    FIRST_NAME_ACC = "first_name_acc"

    FIRST_NAME_DAT = "first_name_dat"

    FIRST_NAME_GEN = "first_name_gen"

    LAST_NAME = "last_name"

    LAST_NAME_ACC = "last_name_acc"

    LAST_NAME_DAT = "last_name_dat"

    LAST_NAME_GEN = "last_name_gen"

    CAN_SUBSCRIBE_STORIES = "can_subscribe_stories"

    IS_SUBSCRIBED_STORIES = "is_subscribed_stories"

    VK_ADMIN_STATUS = "vk_admin_status"

    CAN_UPLOAD_STORY = "can_upload_story"

    CLIPS_COUNT = "clips_count"

    IMAGE_STATUS = "image_status"

    IS_NFT = "is_nft"

    IS_NFT_PHOTO = "is_nft_photo"


class BaseUserGroupFieldsResponse(BaseResponse):
    response: "BaseUserGroupFieldsResponseModel"


class BaseUserIdResponseModel(BaseModel):
    user_id: typing.Optional[int] = Field(
        default=None,
        description="User ID",
    )


class BaseUserIdResponse(BaseResponse):
    response: "BaseUserIdResponseModel"
