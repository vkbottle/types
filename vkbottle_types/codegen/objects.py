import datetime

import typing_extensions as typing

from vkbottle_types.base_model import BaseEnumMeta, BaseModel, Field, IntEnum, StrEnum


class BaseBoolInt(IntEnum, metaclass=BaseEnumMeta):
    NO = 0
    YES = 1


class BaseCity(BaseModel):
    """Model: `BaseCity`"""

    id: int = Field()
    """City ID."""

    title: str = Field()
    """City title."""


class BaseCommentsInfo(BaseModel):
    """Model: `BaseCommentsInfo`"""

    can_post: bool | None = Field(
        default=None,
    )
    """Information whether current user can comment the post."""

    can_open: bool | None = Field(
        default=None,
    )
    """Property `BaseCommentsInfo.can_open`."""

    can_close: bool | None = Field(
        default=None,
    )
    """Property `BaseCommentsInfo.can_close`."""

    can_view: bool | None = Field(
        default=None,
    )
    """Information whether current user can view the comments."""

    count: int | None = Field(
        default=None,
    )
    """Comments number."""

    groups_can_post: bool | None = Field(
        default=None,
    )
    """Information whether groups can comment the post."""

    donut: "WallWallpostCommentsDonut | None" = Field(
        default=None,
    )
    """Property `BaseCommentsInfo.donut`."""

    list_: list["WallWallComment"] | None = Field(
        default=None,
        alias="list",
    )
    """Property `BaseCommentsInfo.list`."""


class BaseCountry(BaseModel):
    """Model: `BaseCountry`"""

    id: int = Field()
    """Country ID."""

    title: str = Field()
    """Country title."""


class BaseCropPhoto(BaseModel):
    """Model: `BaseCropPhoto`"""

    photo: "PhotosPhoto" = Field()
    """Property `BaseCropPhoto.photo`."""

    crop: "BaseCropPhotoCrop" = Field()
    """Property `BaseCropPhoto.crop`."""

    rect: "BaseCropPhotoRect" = Field()
    """Property `BaseCropPhoto.rect`."""


class BaseCropPhotoCrop(BaseModel):
    """Model: `BaseCropPhotoCrop`"""

    x: float = Field()
    """Coordinate X of the left upper corner."""

    y: float = Field()
    """Coordinate Y of the left upper corner."""

    x2: float = Field()
    """Coordinate X of the right lower corner."""

    y2: float = Field()
    """Coordinate Y of the right lower corner."""


class BaseCropPhotoRect(BaseModel):
    """Model: `BaseCropPhotoRect`"""

    x: float = Field()
    """Coordinate X of the left upper corner."""

    y: float = Field()
    """Coordinate Y of the left upper corner."""

    x2: float = Field()
    """Coordinate X of the right lower corner."""

    y2: float = Field()
    """Coordinate Y of the right lower corner."""


class BaseErrorInnerType(StrEnum, metaclass=BaseEnumMeta):
    BASE_ERROR = "base_error"


class BaseError(BaseModel):
    """Model: `BaseError`"""

    inner_type: "BaseErrorInnerType" = Field()
    """Property `BaseError.inner_type`."""

    error_code: int = Field()
    """Error code."""

    error_subcode: int | None = Field(
        default=None,
    )
    """Error subcode."""

    error_msg: str | None = Field(
        default=None,
    )
    """Error message."""

    error_text: str | None = Field(
        default=None,
    )
    """Localized error message."""

    request_params: list["BaseRequestParam"] | None = Field(
        default=None,
    )
    """Property `BaseError.request_params`."""


class BaseGeo(BaseModel):
    """Model: `BaseGeo`"""

    coordinates: "BaseGeoCoordinates | None" = Field(
        default=None,
    )
    """Property `BaseGeo.coordinates`."""

    place: "BasePlace | None" = Field(
        default=None,
    )
    """Property `BaseGeo.place`."""

    showmap: int | None = Field(
        default=None,
    )
    """Information whether a map is showed."""

    type: str | None = Field(
        default=None,
    )
    """Place type."""


class BaseGeoCoordinates(BaseModel):
    """Model: `BaseGeoCoordinates`"""

    latitude: float = Field()
    """Property `BaseGeoCoordinates.latitude`."""

    longitude: float = Field()
    """Property `BaseGeoCoordinates.longitude`."""


class BaseGradientPoint(BaseModel):
    """Model: `BaseGradientPoint`"""

    color: str = Field()
    """Hex color code without #."""

    position: float = Field()
    """Point position."""


class BaseImageTheme(StrEnum, metaclass=BaseEnumMeta):
    LIGHT = "light"
    DARK = "dark"


class BaseImage(BaseModel):
    """Model: `BaseImage`"""

    url: str = Field()
    """Image url."""

    width: int = Field()
    """Image width."""

    height: int = Field()
    """Image height."""

    id: str | None = Field(
        default=None,
    )
    """Property `BaseImage.id`."""

    theme: "BaseImageTheme | None" = Field(
        default=None,
    )
    """Property `BaseImage.theme`."""


class BaseLang(StrEnum, metaclass=BaseEnumMeta):
    RU = "ru"
    UA = "ua"
    BE = "be"
    EN = "en"
    ES = "es"
    FI = "fi"
    DE = "de"
    IT = "it"


class BaseLikes(BaseModel):
    """Model: `BaseLikes`"""

    count: int | None = Field(
        default=None,
    )
    """Likes number."""

    user_likes: bool | None = Field(
        default=None,
    )
    """Information whether current user likes the photo."""


class BaseLikesInfo(BaseModel):
    """Model: `BaseLikesInfo`"""

    can_like: bool = Field()
    """Information whether current user can like the post."""

    count: int = Field()
    """Likes number."""

    user_likes: bool = Field()
    """Information whether current uer has liked the post."""

    can_publish: bool | None = Field(
        default=None,
    )
    """Information whether current user can repost."""

    can_like_as_author: bool | None = Field(
        default=None,
    )
    """Whether user can like comment as author."""

    can_like_by_group: bool | None = Field(
        default=None,
    )
    """Whether current owner of the group can like the reply."""

    author_liked: bool | None = Field(
        default=None,
    )
    """Information whether post author liked the reply."""

    group_liked: bool | None = Field(
        default=None,
    )
    """Information whether group liked the reply."""

    repost_disabled: bool | None = Field(
        default=None,
    )
    """Remove repost feature for post."""


class BaseLinkApplication(BaseModel):
    """Model: `BaseLinkApplication`"""

    app_id: float | None = Field(
        default=None,
    )
    """Application Id."""

    store: "BaseLinkApplicationStore | None" = Field(
        default=None,
    )
    """Property `BaseLinkApplication.store`."""


class BaseLinkApplicationStore(BaseModel):
    """Model: `BaseLinkApplicationStore`"""

    id: float | None = Field(
        default=None,
    )
    """Store Id."""

    name: str | None = Field(
        default=None,
    )
    """Store name."""


class BaseLinkButton(BaseModel):
    """Model: `BaseLinkButton`"""

    action: "BaseLinkButtonAction | None" = Field(
        default=None,
    )
    """Button action."""

    title: str | None = Field(
        default=None,
    )
    """Button title."""

    block_id: str | None = Field(
        default=None,
    )
    """Target block id."""

    section_id: str | None = Field(
        default=None,
    )
    """Target section id."""

    artist_id: str | None = Field(
        default=None,
    )
    """artist id."""

    curator_id: int | None = Field(
        default=None,
    )
    """curator id."""

    album_id: int | None = Field(
        default=None,
    )
    """Video album id."""

    owner_id: int | None = Field(
        default=None,
    )
    """Owner id."""

    icon: str | None = Field(
        default=None,
    )
    """Button icon name, e.g. \'phone\' or \'gift\'."""

    style: "BaseLinkButtonStyle | None" = Field(
        default=None,
    )
    """Property `BaseLinkButton.style`."""

    audio_id: int | None = Field(
        default=None,
    )
    """Property `BaseLinkButton.audio_id`."""

    hashtag: str | None = Field(
        default=None,
    )
    """Property `BaseLinkButton.hashtag`."""


class BaseLinkButtonAction(BaseModel):
    """Model: `BaseLinkButtonAction`"""

    type: "BaseLinkButtonActionType" = Field()
    """Property `BaseLinkButtonAction.type`."""

    url: str | None = Field(
        default=None,
    )
    """Action URL."""

    consume_reason: str | None = Field(
        default=None,
    )
    """Property `BaseLinkButtonAction.consume_reason`."""


class BaseLinkButtonActionType(StrEnum, metaclass=BaseEnumMeta):
    OPEN_URL = "open_url"
    MARKET_CLEAR_RECENT_QUERIES = "market_clear_recent_queries"
    CLOSE_WEB_APP = "close_web_app"
    ADD_PLAYLIST = "add_playlist"
    OPEN_SEARCH_TAB = "open_search_tab"
    OPEN_SEARCH_FILTERS = "open_search_filters"
    RESET_SEARCH_FILTERS = "reset_search_filters"
    IMPORT_CONTACTS = "import_contacts"
    ADD_FRIENDS = "add_friends"
    ONBOARDING = "onboarding"
    SHOW_FILTERS = "show_filters"


class BaseLinkButtonStyle(StrEnum, metaclass=BaseEnumMeta):
    UPDATES = "updates"
    DEFAULT = "default"
    PRIMARY = "primary"
    SECONDARY = "secondary"
    NEGATIVE = "negative"
    TERTIARY = "tertiary"
    FLOAT_BOTTOM = "float_bottom"
    CELL_BUTTON_CENTERED_ICON = "cell_button_centered_icon"
    BORDERLESS_WITH_ICON = "borderless_with_icon"
    GRAY = "gray"
    FLAT = "flat"
    OUTLINE_WITH_CHEVRON = "outline_with_chevron"
    INLINE = "inline"
    MODAL = "modal"
    RIGHT_BUTTON = "right_button"
    AFTER_TOOLBAR = "after_toolbar"


class BaseLinkNoProduct(BaseModel):
    """Model: `BaseLinkNoProduct`"""

    url: str = Field()
    """Link URL."""

    application: "BaseLinkApplication | None" = Field(
        default=None,
    )
    """Property `BaseLinkNoProduct.application`."""

    button: "BaseLinkButton | None" = Field(
        default=None,
    )
    """Property `BaseLinkNoProduct.button`."""

    caption: str | None = Field(
        default=None,
    )
    """Link caption."""

    description: str | None = Field(
        default=None,
    )
    """Link description."""

    id: str | None = Field(
        default=None,
    )
    """Link ID."""

    is_favorite: bool | None = Field(
        default=None,
    )
    """Property `BaseLinkNoProduct.is_favorite`."""

    photo: "PhotosPhoto | None" = Field(
        default=None,
    )
    """Property `BaseLinkNoProduct.photo`."""

    preview_page: str | None = Field(
        default=None,
    )
    """String ID of the page with article preview."""

    preview_url: str | None = Field(
        default=None,
    )
    """URL of the page with article preview."""

    rating: "BaseLinkRating | None" = Field(
        default=None,
    )
    """Property `BaseLinkNoProduct.rating`."""

    title: str | None = Field(
        default=None,
    )
    """Link title."""

    target_object: "LinkTargetObject | None" = Field(
        default=None,
    )
    """Property `BaseLinkNoProduct.target_object`."""

    is_external: bool | None = Field(
        default=None,
    )
    """Information whether the current link is external."""

    video: "VideoVideoFull | None" = Field(
        default=None,
    )
    """Video from link."""


class BaseLinkProductType(StrEnum, metaclass=BaseEnumMeta):
    PRODUCT = "product"


class BaseLinkProduct(BaseModel):
    """Model: `BaseLinkProduct`"""

    price: "MarketPrice" = Field()
    """Property `BaseLinkProduct.price`."""

    merchant: str | None = Field(
        default=None,
    )
    """Property `BaseLinkProduct.merchant`."""

    category: "BaseLinkProductCategory | None" = Field(
        default=None,
    )
    """Property `BaseLinkProduct.category`."""

    geo: "BaseGeoCoordinates | None" = Field(
        default=None,
    )
    """Property `BaseLinkProduct.geo`."""

    distance: int | None = Field(
        default=None,
    )
    """Property `BaseLinkProduct.distance`."""

    city: str | None = Field(
        default=None,
    )
    """Property `BaseLinkProduct.city`."""

    status: "BaseLinkProductStatus | None" = Field(
        default=None,
    )
    """Property `BaseLinkProduct.status`."""

    orders_count: int | None = Field(
        default=None,
    )
    """Property `BaseLinkProduct.orders_count`."""

    type: "BaseLinkProductType | None" = Field(
        default=None,
    )
    """Property `BaseLinkProduct.type`."""


class BaseLinkProductCategory(BaseModel):
    """Model: `BaseLinkProductCategory`"""


class BaseLinkProductStatus(StrEnum, metaclass=BaseEnumMeta):
    ACTIVE = "active"
    BLOCKED = "blocked"
    SOLD = "sold"
    DELETED = "deleted"
    ARCHIVED = "archived"


class BaseLinkRatingType(StrEnum, metaclass=BaseEnumMeta):
    RATING = "rating"


class BaseLinkRating(BaseModel):
    """Model: `BaseLinkRating`"""

    reviews_count: int | None = Field(
        default=None,
    )
    """Count of reviews."""

    stars: float | None = Field(
        default=None,
    )
    """Count of stars."""

    type: "BaseLinkRatingType | None" = Field(
        default=None,
    )
    """Property `BaseLinkRating.type`."""


class BaseMessageError(BaseModel):
    """Model: `BaseMessageError`"""

    code: int | None = Field(
        default=None,
    )
    """Error code."""

    description: str | None = Field(
        default=None,
    )
    """Error message."""


class BaseNameCase(StrEnum, metaclass=BaseEnumMeta):
    NOM = "Nom"
    GEN = "Gen"
    DAT = "Dat"
    ACC = "Acc"
    INS = "Ins"
    ABL = "Abl"


class BaseObject(BaseModel):
    """Model: `BaseObject`"""

    id: int = Field()
    """Object ID."""

    title: str = Field()
    """Object title."""


class BaseObjectCount(BaseModel):
    """Model: `BaseObjectCount`"""

    count: int | None = Field(
        default=None,
    )
    """Items count."""


class BaseObjectWithName(BaseModel):
    """Model: `BaseObjectWithName`"""

    id: int = Field()
    """Object ID."""

    name: str = Field()
    """Object name."""


class BaseOwnerCover(BaseModel):
    """Model: `BaseOwnerCover`"""

    enabled: bool = Field()
    """Information whether cover is enabled."""

    images: list["BaseImage"] | None = Field(
        default=None,
    )
    """Property `BaseOwnerCover.images`."""

    crop_params: "BaseOwnerCoverCropParams | None" = Field(
        default=None,
    )
    """Property `BaseOwnerCover.crop_params`."""

    original_image: "BaseImage | None" = Field(
        default=None,
    )
    """Property `BaseOwnerCover.original_image`."""

    photo_id: int | None = Field(
        default=None,
    )
    """Property `BaseOwnerCover.photo_id`."""


class BaseOwnerCoverCropParams(BaseModel):
    """Model: `BaseOwnerCoverCropParams`"""

    x: int | None = Field(
        default=None,
    )
    """Property `BaseOwnerCoverCropParams.x`."""

    y: int | None = Field(
        default=None,
    )
    """Property `BaseOwnerCoverCropParams.y`."""

    width: int | None = Field(
        default=None,
    )
    """Property `BaseOwnerCoverCropParams.width`."""

    height: int | None = Field(
        default=None,
    )
    """Property `BaseOwnerCoverCropParams.height`."""


class BasePlace(BaseModel):
    """Model: `BasePlace`"""

    address: str | None = Field(
        default=None,
    )
    """Place address."""

    checkins: int | None = Field(
        default=None,
    )
    """Checkins number."""

    city: str | None = Field(
        default=None,
    )
    """City name."""

    created: int | None = Field(
        default=None,
    )
    """Date of the place creation in Unixtime."""

    icon: str | None = Field(
        default=None,
    )
    """URL of the place\'s icon."""

    id: int | None = Field(
        default=None,
    )
    """Place ID."""

    latitude: float | None = Field(
        default=None,
    )
    """Place latitude."""

    longitude: float | None = Field(
        default=None,
    )
    """Place longitude."""

    title: str | None = Field(
        default=None,
    )
    """Place title."""

    type: str | None = Field(
        default=None,
    )
    """Place type."""


class BasePropertyExists(IntEnum, metaclass=BaseEnumMeta):
    PROPERTY_EXISTS = 1


class BaseRepostsInfo(BaseModel):
    """Count of views
    Model: `BaseRepostsInfo`
    """

    count: int = Field()
    """Total reposts counter. Sum of wall and mail reposts counters."""

    wall_count: int | None = Field(
        default=None,
    )
    """Wall reposts counter."""

    mail_count: int | None = Field(
        default=None,
    )
    """Mail reposts counter."""

    user_reposted: bool | None = Field(
        default=None,
    )
    """Information whether current user has reposted the post."""


class BaseRequestParam(BaseModel):
    """Model: `BaseRequestParam`"""

    key: str = Field()
    """Parameter name."""

    value: str = Field()
    """Parameter value."""


class BaseSex(IntEnum, metaclass=BaseEnumMeta):
    UNKNOWN = 0
    FEMALE = 1
    MALE = 2


class BaseStickerInnerType(StrEnum, metaclass=BaseEnumMeta):
    BASE_STICKER_NEW = "base_sticker_new"


class BaseSticker(BaseModel):
    """Model: `BaseSticker`"""

    inner_type: "BaseStickerInnerType" = Field()
    """Property `BaseSticker.inner_type`."""

    sticker_id: int | None = Field(
        default=None,
    )
    """Sticker ID."""

    product_id: int | None = Field(
        default=None,
    )
    """Pack ID."""

    images: list["BaseImage"] | None = Field(
        default=None,
    )
    """Property `BaseSticker.images`."""

    images_with_background: list["BaseImage"] | None = Field(
        default=None,
    )
    """Property `BaseSticker.images_with_background`."""

    animation_url: str | None = Field(
        default=None,
    )
    """URL of sticker animation script."""

    animations: list["BaseStickerAnimation"] | None = Field(
        default=None,
    )
    """Array of sticker animation script objects."""

    is_allowed: bool | None = Field(
        default=None,
    )
    """Information whether the sticker is allowed."""


class BaseStickerAnimationType(StrEnum, metaclass=BaseEnumMeta):
    LIGHT = "light"
    DARK = "dark"


class BaseStickerAnimation(BaseModel):
    """Model: `BaseStickerAnimation`"""

    type: "BaseStickerAnimationType | None" = Field(
        default=None,
    )
    """Type of animation script."""

    url: str | None = Field(
        default=None,
    )
    """URL of animation script."""


class BaseStickerNewInnerType(StrEnum, metaclass=BaseEnumMeta):
    BASE_STICKER_NEW = "base_sticker_new"


class BaseStickerNew(BaseModel):
    """Model: `BaseStickerNew`"""

    inner_type: "BaseStickerNewInnerType" = Field()
    """Property `BaseStickerNew.inner_type`."""

    sticker_id: int | None = Field(
        default=None,
    )
    """Sticker ID."""

    product_id: int | None = Field(
        default=None,
    )
    """Pack ID."""

    images: list["BaseImage"] | None = Field(
        default=None,
    )
    """Property `BaseStickerNew.images`."""

    images_with_background: list["BaseImage"] | None = Field(
        default=None,
    )
    """Property `BaseStickerNew.images_with_background`."""

    animation_url: str | None = Field(
        default=None,
    )
    """URL of sticker animation script."""

    animations: list["BaseStickerAnimation"] | None = Field(
        default=None,
    )
    """Array of sticker animation script objects."""

    is_allowed: bool | None = Field(
        default=None,
    )
    """Information whether the sticker is allowed."""


class BaseUploadServer(BaseModel):
    """Model: `BaseUploadServer`"""

    upload_url: str = Field()
    """Upload URL."""


class BaseUserGroupFields(StrEnum, metaclass=BaseEnumMeta):
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
    IS_VERIFIED = "is_verified"
    URL = "url"


class BaseUserId(BaseModel):
    """Model: `BaseUserId`"""

    user_id: int | None = Field(
        default=None,
    )
    """User ID."""


class UsersCareer(BaseModel):
    """Model: `UsersCareer`"""

    city_id: int | None = Field(
        default=None,
    )
    """City ID."""

    city_name: str | None = Field(
        default=None,
    )
    """City name."""

    company: str | None = Field(
        default=None,
    )
    """Company name."""

    from_: int | None = Field(
        default=None,
        alias="from",
    )
    """From year."""

    group_id: int | None = Field(
        default=None,
    )
    """Community ID."""

    id: int | None = Field(
        default=None,
    )
    """Career ID."""

    position: str | None = Field(
        default=None,
    )
    """Position."""

    until: int | None = Field(
        default=None,
    )
    """Till year."""


class UsersExports(BaseModel):
    """Model: `UsersExports`"""

    facebook: int | None = Field(
        default=None,
    )
    """Property `UsersExports.facebook`."""

    livejournal: int | None = Field(
        default=None,
    )
    """Property `UsersExports.livejournal`."""

    twitter: int | None = Field(
        default=None,
    )
    """Property `UsersExports.twitter`."""


class UsersFields(StrEnum, metaclass=BaseEnumMeta):
    FIRST_NAME_NOM = "first_name_nom"
    FIRST_NAME_GEN = "first_name_gen"
    FIRST_NAME_DAT = "first_name_dat"
    FIRST_NAME_ACC = "first_name_acc"
    FIRST_NAME_INS = "first_name_ins"
    FIRST_NAME_ABL = "first_name_abl"
    LAST_NAME_NOM = "last_name_nom"
    LAST_NAME_GEN = "last_name_gen"
    LAST_NAME_DAT = "last_name_dat"
    LAST_NAME_ACC = "last_name_acc"
    LAST_NAME_INS = "last_name_ins"
    LAST_NAME_ABL = "last_name_abl"
    PHOTO_ID = "photo_id"
    VERIFIED = "verified"
    SEX = "sex"
    BDATE = "bdate"
    BDATE_VISIBILITY = "bdate_visibility"
    CITY = "city"
    HOME_TOWN = "home_town"
    HAS_PHOTO = "has_photo"
    PHOTO = "photo"
    PHOTO_REC = "photo_rec"
    PHOTO_50 = "photo_50"
    PHOTO_100 = "photo_100"
    PHOTO_200_ORIG = "photo_200_orig"
    PHOTO_200 = "photo_200"
    PHOTO_400 = "photo_400"
    PHOTO_400_ORIG = "photo_400_orig"
    PHOTO_BIG = "photo_big"
    PHOTO_MEDIUM = "photo_medium"
    PHOTO_MEDIUM_REC = "photo_medium_rec"
    PHOTO_MAX = "photo_max"
    PHOTO_MAX_ORIG = "photo_max_orig"
    PHOTO_MAX_SIZE = "photo_max_size"
    THIRD_PARTY_BUTTONS = "third_party_buttons"
    ONLINE = "online"
    LISTS = "lists"
    DOMAIN = "domain"
    HAS_MOBILE = "has_mobile"
    CONTACTS = "contacts"
    LANGUAGE = "language"
    SITE = "site"
    EDUCATION = "education"
    UNIVERSITIES = "universities"
    SCHOOLS = "schools"
    STATUS = "status"
    LAST_SEEN = "last_seen"
    FOLLOWERS_COUNT = "followers_count"
    COUNTERS = "counters"
    COMMON_COUNT = "common_count"
    ONLINE_INFO = "online_info"
    OCCUPATION = "occupation"
    NICKNAME = "nickname"
    RELATIVES = "relatives"
    RELATION = "relation"
    PERSONAL = "personal"
    CONNECTIONS = "connections"
    EXPORTS = "exports"
    WALL_COMMENTS = "wall_comments"
    WALL_DEFAULT = "wall_default"
    ACTIVITIES = "activities"
    ACTIVITY = "activity"
    INTERESTS = "interests"
    MUSIC = "music"
    MOVIES = "movies"
    TV = "tv"
    BOOKS = "books"
    IS_NO_INDEX = "is_no_index"
    NO_INDEX = "no_index"
    GAMES = "games"
    ABOUT = "about"
    QUOTES = "quotes"
    CAN_POST = "can_post"
    CAN_SEE_ALL_POSTS = "can_see_all_posts"
    CAN_SEE_AUDIO = "can_see_audio"
    CAN_SEE_GIFTS = "can_see_gifts"
    WORK = "work"
    PLACES = "places"
    CAN_WRITE_PRIVATE_MESSAGE = "can_write_private_message"
    CAN_SEND_FRIEND_REQUEST = "can_send_friend_request"
    CAN_UPLOAD_DOC = "can_upload_doc"
    CAN_BAN = "can_ban"
    IS_FAVORITE = "is_favorite"
    IS_HIDDEN_FROM_FEED = "is_hidden_from_feed"
    TIMEZONE = "timezone"
    SCREEN_NAME = "screen_name"
    MAIDEN_NAME = "maiden_name"
    CROP_PHOTO = "crop_photo"
    IS_FRIEND = "is_friend"
    IS_BEST_FRIEND = "is_best_friend"
    FRIEND_STATUS = "friend_status"
    CAREER = "career"
    MILITARY = "military"
    BLACKLISTED = "blacklisted"
    BLACKLISTED_BY_ME = "blacklisted_by_me"
    CAN_SUBSCRIBE_POSTS = "can_subscribe_posts"
    DESCRIPTIONS = "descriptions"
    TRENDING = "trending"
    MUTUAL = "mutual"
    FRIENDSHIP_WEEKS = "friendship_weeks"
    CAN_INVITE_TO_CHATS = "can_invite_to_chats"
    STORIES_ARCHIVE_COUNT = "stories_archive_count"
    HAS_UNSEEN_STORIES = "has_unseen_stories"
    VIDEO_LIVE = "video_live"
    VIDEO_LIVE_LEVEL = "video_live_level"
    VIDEO_LIVE_COUNT = "video_live_count"
    CLIPS_COUNT = "clips_count"
    SERVICE_DESCRIPTION = "service_description"
    CAN_SEE_WISHES = "can_see_wishes"
    IS_SUBSCRIBED_PODCASTS = "is_subscribed_podcasts"
    CAN_SUBSCRIBE_PODCASTS = "can_subscribe_podcasts"
    ANIMATED_AVATAR = "animated_avatar"
    OWNER_STATE = "owner_state"
    IS_VERIFIED = "is_verified"
    OAUTH_LINKED = "oauth_linked"
    OAUTH_VERIFICATION = "oauth_verification"
    PROMOTION_ALLOWANCE = "promotion_allowance"


class UsersLastSeen(BaseModel):
    """Model: `UsersLastSeen`"""

    platform: int | None = Field(
        default=None,
    )
    """Type of the platform that used for the last authorization."""

    time: int | None = Field(
        default=None,
    )
    """Last visit date (in Unix time)."""


class UsersMilitary(BaseModel):
    """Model: `UsersMilitary`"""

    unit: str = Field()
    """Unit name."""

    unit_id: int = Field()
    """Unit ID."""

    from_: int | None = Field(
        default=None,
        alias="from",
    )
    """From year."""

    id: int | None = Field(
        default=None,
    )
    """Military ID."""

    until: int | None = Field(
        default=None,
    )
    """Till year."""


class UsersOccupationType(StrEnum, metaclass=BaseEnumMeta):
    SCHOOL = "school"
    UNIVERSITY = "university"
    WORK = "work"


class UsersOccupation(BaseModel):
    """Model: `UsersOccupation`"""

    id: int | None = Field(
        default=None,
    )
    """ID of school, university, company group."""

    name: str | None = Field(
        default=None,
    )
    """Name of occupation."""

    type: "UsersOccupationType | None" = Field(
        default=None,
    )
    """Type of occupation."""

    graduate_year: int | None = Field(
        default=None,
    )
    """Property `UsersOccupation.graduate_year`."""

    city_id: int | None = Field(
        default=None,
    )
    """Property `UsersOccupation.city_id`."""


class UsersOnlineInfoStatus(StrEnum, metaclass=BaseEnumMeta):
    RECENTLY = "recently"
    LAST_WEEK = "last_week"
    LAST_MONTH = "last_month"
    LONG_AGO = "long_ago"
    NOT_SHOW = "not_show"


class UsersOnlineInfo(BaseModel):
    """Model: `UsersOnlineInfo`"""

    visible: bool = Field()
    """Whether you can see real online status of user or not."""

    last_seen: int | None = Field(
        default=None,
    )
    """Last time we saw user being active."""

    is_online: bool | None = Field(
        default=None,
    )
    """Whether user is currently online or not."""

    app_id: int | None = Field(
        default=None,
    )
    """Application id from which user is currently online or was last seen online."""

    is_mobile: bool | None = Field(
        default=None,
    )
    """Is user online from desktop app or mobile app."""

    status: "UsersOnlineInfoStatus | None" = Field(
        default=None,
    )
    """In case user online is not visible, it indicates approximate timeframe of user online."""


class UsersPersonal(BaseModel):
    """Model: `UsersPersonal`"""

    alcohol: int | None = Field(
        default=None,
    )
    """User\'s views on alcohol."""

    inspired_by: str | None = Field(
        default=None,
    )
    """User\'s inspired by."""

    langs: list[str] | None = Field(
        default=None,
    )
    """Property `UsersPersonal.langs`."""

    langs_full: list["DatabaseLanguageFull"] | None = Field(
        default=None,
    )
    """User\'s languages with full info."""

    life_main: int | None = Field(
        default=None,
    )
    """User\'s personal priority in life."""

    people_main: int | None = Field(
        default=None,
    )
    """User\'s personal priority in people."""

    political: int | None = Field(
        default=None,
    )
    """User\'s political views."""

    religion: str | None = Field(
        default=None,
    )
    """User\'s religion."""

    religion_id: int | None = Field(
        default=None,
    )
    """User\'s religion id."""

    smoking: int | None = Field(
        default=None,
    )
    """User\'s views on smoking."""


class UsersRelativeType(StrEnum, metaclass=BaseEnumMeta):
    PARENT = "parent"
    CHILD = "child"
    GRANDPARENT = "grandparent"
    GRANDCHILD = "grandchild"
    SIBLING = "sibling"


class UsersRelative(BaseModel):
    """Model: `UsersRelative`"""

    type: "UsersRelativeType" = Field()
    """Relative type."""

    birth_date: str | None = Field(
        default=None,
    )
    """Date of child birthday (format dd.mm.yyyy)."""

    id: int | None = Field(
        default=None,
    )
    """Relative ID."""

    name: str | None = Field(
        default=None,
    )
    """Name of relative."""


class UsersSchool(BaseModel):
    """Model: `UsersSchool`"""

    city: int | None = Field(
        default=None,
    )
    """City ID."""

    class_: str | None = Field(
        default=None,
        alias="class",
    )
    """School class letter."""

    class_id: int | None = Field(
        default=None,
    )
    """School class id."""

    id: str | None = Field(
        default=None,
    )
    """School ID."""

    name: str | None = Field(
        default=None,
    )
    """School name."""

    type: int | None = Field(
        default=None,
    )
    """School type ID."""

    type_str: str | None = Field(
        default=None,
    )
    """School type name."""

    year_from: int | None = Field(
        default=None,
    )
    """Year the user started to study."""

    year_graduated: int | None = Field(
        default=None,
    )
    """Graduation year."""

    year_to: int | None = Field(
        default=None,
    )
    """Year the user finished to study."""

    speciality: str | None = Field(
        default=None,
    )
    """Property `UsersSchool.speciality`."""


class UsersSubscriptionsItem(BaseModel):
    """Model: `UsersSubscriptionsItem`"""


class UsersUniversity(BaseModel):
    """Model: `UsersUniversity`"""

    chair: int | None = Field(
        default=None,
    )
    """Chair ID."""

    chair_name: str | None = Field(
        default=None,
    )
    """Chair name."""

    city: int | None = Field(
        default=None,
    )
    """City ID."""

    education_form: str | None = Field(
        default=None,
    )
    """Education form."""

    education_form_id: int | None = Field(
        default=None,
    )
    """Education form id."""

    education_status: str | None = Field(
        default=None,
    )
    """Education status."""

    education_status_id: int | None = Field(
        default=None,
    )
    """Education status id."""

    faculty: int | None = Field(
        default=None,
    )
    """Faculty ID."""

    faculty_name: str | None = Field(
        default=None,
    )
    """Faculty name."""

    graduation: int | None = Field(
        default=None,
    )
    """Graduation year."""

    id: int | None = Field(
        default=None,
    )
    """University ID."""

    name: str | None = Field(
        default=None,
    )
    """University name."""

    university_group_id: int | None = Field(
        default=None,
    )
    """Property `UsersUniversity.university_group_id`."""


class UsersUserConnections(BaseModel):
    """Model: `UsersUserConnections`"""

    skype: str = Field()
    """User\'s Skype nickname."""

    facebook: str = Field()
    """User\'s Facebook account."""

    twitter: str = Field()
    """User\'s Twitter account."""

    instagram: str = Field()
    """User\'s Instagram account."""

    facebook_name: str | None = Field(
        default=None,
    )
    """User\'s Facebook name."""

    livejournal: str | None = Field(
        default=None,
    )
    """User\'s Livejournal account."""


class UsersUserCounters(BaseModel):
    """Model: `UsersUserCounters`"""

    albums: int | None = Field(
        default=None,
    )
    """Albums number."""

    badges: int | None = Field(
        default=None,
    )
    """Badges number."""

    audios: int | None = Field(
        default=None,
    )
    """Audios number."""

    followers: int | None = Field(
        default=None,
    )
    """Followers number."""

    friends: int | None = Field(
        default=None,
    )
    """Friends number."""

    gifts: int | None = Field(
        default=None,
    )
    """Gifts number."""

    groups: int | None = Field(
        default=None,
    )
    """Communities number."""

    notes: int | None = Field(
        default=None,
    )
    """Notes number."""

    online_friends: int | None = Field(
        default=None,
    )
    """Online friends number."""

    pages: int | None = Field(
        default=None,
    )
    """Public pages number."""

    photos: int | None = Field(
        default=None,
    )
    """Photos number."""

    subscriptions: int | None = Field(
        default=None,
    )
    """Subscriptions number."""

    user_photos: int | None = Field(
        default=None,
    )
    """Number of photos with user."""

    user_videos: int | None = Field(
        default=None,
    )
    """Number of videos with user."""

    videos: int | None = Field(
        default=None,
    )
    """Videos number."""

    video_playlists: int | None = Field(
        default=None,
    )
    """Playlists number."""

    new_photo_tags: int | None = Field(
        default=None,
    )
    """Property `UsersUserCounters.new_photo_tags`."""

    new_recognition_tags: int | None = Field(
        default=None,
    )
    """Property `UsersUserCounters.new_recognition_tags`."""

    mutual_friends: int | None = Field(
        default=None,
    )
    """Property `UsersUserCounters.mutual_friends`."""

    friends_followers: int | None = Field(
        default=None,
    )
    """Property `UsersUserCounters.friends_followers`."""

    posts: int | None = Field(
        default=None,
    )
    """Property `UsersUserCounters.posts`."""

    articles: int | None = Field(
        default=None,
    )
    """Property `UsersUserCounters.articles`."""

    wishes: int | None = Field(
        default=None,
    )
    """Property `UsersUserCounters.wishes`."""

    podcasts: int | None = Field(
        default=None,
    )
    """Property `UsersUserCounters.podcasts`."""

    clips: int | None = Field(
        default=None,
    )
    """Property `UsersUserCounters.clips`."""

    clips_followers: int | None = Field(
        default=None,
    )
    """Property `UsersUserCounters.clips_followers`."""

    videos_followers: int | None = Field(
        default=None,
    )
    """Videos followers number."""

    clips_views: int | None = Field(
        default=None,
    )
    """Property `UsersUserCounters.clips_views`."""

    clips_likes: int | None = Field(
        default=None,
    )
    """Property `UsersUserCounters.clips_likes`."""


class UsersUserMin(BaseModel):
    """Model: `UsersUserMin`"""

    id: int = Field()
    """User ID."""

    deactivated: str | None = Field(
        default=None,
    )
    """Returns if a profile is deleted or blocked."""

    first_name: str | None = Field(
        default=None,
    )
    """User first name."""

    hidden: int | None = Field(
        default=None,
    )
    """Returns if a profile is hidden.."""

    last_name: str | None = Field(
        default=None,
    )
    """User last name."""

    can_access_closed: bool | None = Field(
        default=None,
    )
    """Property `UsersUserMin.can_access_closed`."""

    is_closed: bool | None = Field(
        default=None,
    )
    """Property `UsersUserMin.is_closed`."""


class UsersUserRelation(IntEnum, metaclass=BaseEnumMeta):
    NOT_SPECIFIED = 0
    SINGLE = 1
    IN_A_RELATIONSHIP = 2
    ENGAGED = 3
    MARRIED = 4
    COMPLICATED = 5
    ACTIVELY_SEARCHING = 6
    IN_LOVE = 7
    IN_A_CIVIL_UNION = 8


class UsersUserSettingsXtr(BaseModel):
    """Model: `UsersUserSettingsXtr`"""

    home_town: str = Field()
    """User\'s hometown."""

    status: str = Field()
    """User status."""

    connections: "UsersUserConnections | None" = Field(
        default=None,
    )
    """Property `UsersUserSettingsXtr.connections`."""

    bdate: str | None = Field(
        default=None,
    )
    """User\'s date of birth."""

    bdate_visibility: int | None = Field(
        default=None,
    )
    """Information whether user\'s birthdate are hidden."""

    city: "BaseCity | None" = Field(
        default=None,
    )
    """Property `UsersUserSettingsXtr.city`."""

    first_name: str | None = Field(
        default=None,
    )
    """User first name."""

    last_name: str | None = Field(
        default=None,
    )
    """User last name."""

    maiden_name: str | None = Field(
        default=None,
    )
    """User maiden name."""

    name_request: "AccountNameRequest | None" = Field(
        default=None,
    )
    """Property `UsersUserSettingsXtr.name_request`."""

    personal: "UsersPersonal | None" = Field(
        default=None,
    )
    """Property `UsersUserSettingsXtr.personal`."""

    phone: str | None = Field(
        default=None,
    )
    """User phone number with some hidden digits."""

    relation: "UsersUserRelation | None" = Field(
        default=None,
    )
    """User relationship status."""

    relation_partner: "UsersUserMin | None" = Field(
        default=None,
    )
    """Property `UsersUserSettingsXtr.relation_partner`."""

    relation_pending: bool | None = Field(
        default=None,
    )
    """Information whether relation status is pending."""

    relation_requests: list["UsersUserMin"] | None = Field(
        default=None,
    )
    """Property `UsersUserSettingsXtr.relation_requests`."""

    screen_name: str | None = Field(
        default=None,
    )
    """Domain name of the user\'s page."""

    sex: "BaseSex | None" = Field(
        default=None,
    )
    """User sex."""

    status_audio: "AudioAudio | None" = Field(
        default=None,
    )
    """Property `UsersUserSettingsXtr.status_audio`."""

    interests: "AccountUserSettingsInterests | None" = Field(
        default=None,
    )
    """Property `UsersUserSettingsXtr.interests`."""

    languages: list[str] | None = Field(
        default=None,
    )
    """Property `UsersUserSettingsXtr.languages`."""


class UsersUserType(StrEnum, metaclass=BaseEnumMeta):
    PROFILE = "profile"


class UsersUsersArray(BaseModel):
    """Model: `UsersUsersArray`"""

    count: int = Field()
    """Users number."""

    items: list[int] = Field()
    """Property `UsersUsersArray.items`."""


class MessagesActionOneOf(BaseModel):
    """Model: `MessagesActionOneOf`"""

    type: "MessagesMessageActionStatus" = Field()
    """Property `MessagesActionOneOf.type`."""

    conversation_message_id: int | None = Field(
        default=None,
    )
    """Message ID."""

    email: str | None = Field(
        default=None,
    )
    """Email address for chat_invite_user or chat_kick_user actions."""

    member_id: int | None = Field(
        default=None,
    )
    """User or email peer ID."""

    message: str | None = Field(
        default=None,
    )
    """Message body of related message."""

    photo: "MessagesMessageActionPhoto | None" = Field(
        default=None,
    )
    """Property `MessagesActionOneOf.photo`."""

    text: str | None = Field(
        default=None,
    )
    """New chat title for chat_create and chat_title_update actions."""


class MessagesAudioMessage(BaseModel):
    """Model: `MessagesAudioMessage`"""

    duration: int = Field()
    """Audio message duration in seconds."""

    id: int = Field()
    """Audio message ID."""

    link_mp3: str = Field()
    """MP3 file URL."""

    link_ogg: str = Field()
    """OGG file URL."""

    owner_id: int = Field()
    """Audio message owner ID."""

    waveform: list[int] = Field()
    """Property `MessagesAudioMessage.waveform`."""

    access_key: str | None = Field(
        default=None,
    )
    """Access key for audio message."""

    transcript_error: int | None = Field(
        default=None,
    )
    """Property `MessagesAudioMessage.transcript_error`."""


class MessagesBaseMessage(BaseModel):
    """Model: `MessagesBaseMessage`"""

    conversation_message_id: int = Field()
    """Unique auto-incremented number for all messages with this peer."""

    date: datetime.datetime = Field()
    """Date when the message has been sent in Unixtime."""

    from_id: int = Field()
    """Message author\'s ID."""

    id: int = Field()
    """Message ID."""

    text: str = Field()
    """Message text."""

    version: int = Field()
    """Property `MessagesBaseMessage.version`."""

    out: bool = Field()
    """Information whether the message is outcoming."""

    peer_id: int = Field()
    """Peer ID."""

    action: "MessagesActionOneOf | None" = Field(
        default=None,
    )
    """Property `MessagesBaseMessage.action`."""

    admin_author_id: int | None = Field(
        default=None,
    )
    """Only for messages from community. Contains user ID of community admin, who sent this message.."""

    attachments: list["MessagesMessageAttachment"] | None = Field(
        default=None,
    )
    """Property `MessagesBaseMessage.attachments`."""

    deleted: bool | None = Field(
        default=None,
    )
    """Is it an deleted message."""

    fwd_messages: "MessagesFwdMessages | None" = Field(
        default=None,
    )
    """Property `MessagesBaseMessage.fwd_messages`."""

    geo: "BaseGeo | None" = Field(
        default=None,
    )
    """Property `MessagesBaseMessage.geo`."""

    is_cropped: bool | None = Field(
        default=None,
    )
    """this message is cropped for bot."""

    keyboard: "MessagesKeyboard | None" = Field(
        default=None,
    )
    """Property `MessagesBaseMessage.keyboard`."""

    payload: str | None = Field(
        default=None,
    )
    """Property `MessagesBaseMessage.payload`."""

    update_time: int | None = Field(
        default=None,
    )
    """Date when the message has been updated in Unixtime."""

    is_silent: bool | None = Field(
        default=None,
    )
    """Is silent message, push without sound."""

    is_unavailable: bool | None = Field(
        default=None,
    )
    """Is message unavailable for some reason, including its id equals 0."""

    random_id: int | None = Field(
        default=None,
    )
    """ID used for sending messages. It returned only for outgoing messages."""

    ref: str | None = Field(
        default=None,
    )
    """Property `MessagesBaseMessage.ref`."""

    ref_source: str | None = Field(
        default=None,
    )
    """Property `MessagesBaseMessage.ref_source`."""


class MessagesChat(BaseModel):
    """Model: `MessagesChat`"""

    admin_id: int = Field()
    """Chat creator ID."""

    id: int = Field()
    """Chat ID."""

    type: str = Field()
    """Chat type."""

    users: list[int] = Field()
    """Property `MessagesChat.users`."""

    members_count: int = Field()
    """Count members in a chat."""

    kicked: bool | None = Field(
        default=None,
    )
    """Shows that user has been kicked from the chat."""

    left: bool | None = Field(
        default=None,
    )
    """Shows that user has been left the chat."""

    photo_100: str | None = Field(
        default=None,
    )
    """URL of the preview image with 100 px in width."""

    photo_200: str | None = Field(
        default=None,
    )
    """URL of the preview image with 200 px in width."""

    photo_50: str | None = Field(
        default=None,
    )
    """URL of the preview image with 50 px in width."""

    push_settings: "MessagesChatPushSettings | None" = Field(
        default=None,
    )
    """Property `MessagesChat.push_settings`."""

    title: str | None = Field(
        default=None,
    )
    """Chat title."""

    is_default_photo: bool | None = Field(
        default=None,
    )
    """If provided photo is default."""

    is_group_channel: bool | None = Field(
        default=None,
    )
    """If chat is group channel."""


class MessagesChatFull(BaseModel):
    """Model: `MessagesChatFull`"""

    admin_id: int = Field()
    """Chat creator ID."""

    id: int = Field()
    """Chat ID."""

    type: str = Field()
    """Chat type."""

    users: list["MessagesUserXtrInvitedBy"] = Field()
    """Property `MessagesChatFull.users`."""

    members_count: int = Field()
    """Count members in a chat."""

    kicked: bool | None = Field(
        default=None,
    )
    """Shows that user has been kicked from the chat."""

    left: bool | None = Field(
        default=None,
    )
    """Shows that user has been left the chat."""

    photo_100: str | None = Field(
        default=None,
    )
    """URL of the preview image with 100 px in width."""

    photo_200: str | None = Field(
        default=None,
    )
    """URL of the preview image with 200 px in width."""

    photo_50: str | None = Field(
        default=None,
    )
    """URL of the preview image with 50 px in width."""

    push_settings: "MessagesChatPushSettings | None" = Field(
        default=None,
    )
    """Property `MessagesChatFull.push_settings`."""

    title: str | None = Field(
        default=None,
    )
    """Chat title."""

    is_default_photo: bool | None = Field(
        default=None,
    )
    """If provided photo is default."""

    is_group_channel: bool | None = Field(
        default=None,
    )
    """If chat is group channel."""


class MessagesChatPreview(BaseModel):
    """Model: `MessagesChatPreview`"""

    admin_id: int = Field()
    """Property `MessagesChatPreview.admin_id`."""

    members: list[int] = Field()
    """Property `MessagesChatPreview.members`."""

    title: str = Field()
    """Property `MessagesChatPreview.title`."""

    joined: bool | None = Field(
        default=None,
    )
    """Property `MessagesChatPreview.joined`."""

    local_id: int | None = Field(
        default=None,
    )
    """Property `MessagesChatPreview.local_id`."""

    members_count: int | None = Field(
        default=None,
    )
    """Property `MessagesChatPreview.members_count`."""

    is_member: bool | None = Field(
        default=None,
    )
    """Property `MessagesChatPreview.is_member`."""

    photo: "MessagesChatSettingsPhoto | None" = Field(
        default=None,
    )
    """Property `MessagesChatPreview.photo`."""

    is_don: bool | None = Field(
        default=None,
    )
    """Property `MessagesChatPreview.is_don`."""

    is_nft: bool | None = Field(
        default=None,
    )
    """Property `MessagesChatPreview.is_nft`."""

    is_group_channel: bool | None = Field(
        default=None,
    )
    """Property `MessagesChatPreview.is_group_channel`."""

    button: "BaseLinkButton | None" = Field(
        default=None,
    )
    """Property `MessagesChatPreview.button`."""


class MessagesChatPushSettings(BaseModel):
    """Model: `MessagesChatPushSettings`"""

    disabled_until: int | None = Field(
        default=None,
    )
    """Time until that notifications are disabled."""

    sound: bool | None = Field(
        default=None,
    )
    """Information whether the sound is on."""


class MessagesChatRestrictions(BaseModel):
    """Model: `MessagesChatRestrictions`"""

    admins_promote_users: bool | None = Field(
        default=None,
    )
    """Only admins can promote users to admins."""

    only_admins_edit_info: bool | None = Field(
        default=None,
    )
    """Only admins can change chat info."""

    only_admins_edit_pin: bool | None = Field(
        default=None,
    )
    """Only admins can edit pinned message."""

    only_admins_invite: bool | None = Field(
        default=None,
    )
    """Only admins can invite users to this chat."""

    only_admins_kick: bool | None = Field(
        default=None,
    )
    """Only admins can kick users from this chat."""


class MessagesChatSettings(BaseModel):
    """Model: `MessagesChatSettings`"""

    owner_id: int = Field()
    """Property `MessagesChatSettings.owner_id`."""

    title: str = Field()
    """Chat title."""

    state: "MessagesChatSettingsState" = Field()
    """Property `MessagesChatSettings.state`."""

    acl: "MessagesChatSettingsAcl" = Field()
    """Property `MessagesChatSettings.acl`."""

    members_count: int | None = Field(
        default=None,
    )
    """Property `MessagesChatSettings.members_count`."""

    friends_count: int | None = Field(
        default=None,
    )
    """Property `MessagesChatSettings.friends_count`."""

    pinned_messages_count: int | None = Field(
        default=None,
    )
    """Property `MessagesChatSettings.pinned_messages_count`."""

    pinned_message: "MessagesPinnedMessage | None" = Field(
        default=None,
    )
    """Property `MessagesChatSettings.pinned_message`."""

    photo: "MessagesChatSettingsPhoto | None" = Field(
        default=None,
    )
    """Property `MessagesChatSettings.photo`."""

    admin_ids: list[int] | None = Field(
        default=None,
    )
    """Ids of chat admins."""

    active_ids: list[int] | None = Field(
        default=None,
    )
    """Property `MessagesChatSettings.active_ids`."""

    is_group_channel: bool | None = Field(
        default=None,
    )
    """Property `MessagesChatSettings.is_group_channel`."""

    permissions: "MessagesChatSettingsPermissions | None" = Field(
        default=None,
    )
    """Property `MessagesChatSettings.permissions`."""

    is_disappearing: bool | None = Field(
        default=None,
    )
    """Property `MessagesChatSettings.is_disappearing`."""

    theme: str | None = Field(
        default=None,
    )
    """Property `MessagesChatSettings.theme`."""

    disappearing_chat_link: str | None = Field(
        default=None,
    )
    """Property `MessagesChatSettings.disappearing_chat_link`."""

    is_service: bool | None = Field(
        default=None,
    )
    """Property `MessagesChatSettings.is_service`."""


class MessagesChatSettingsAcl(BaseModel):
    """Model: `MessagesChatSettingsAcl`"""

    can_change_info: bool = Field()
    """Can you change photo, description and name."""

    can_change_invite_link: bool = Field()
    """Can you change invite link for this chat."""

    can_change_pin: bool = Field()
    """Can you pin/unpin message for this chat."""

    can_invite: bool = Field()
    """Can you invite other peers in chat."""

    can_promote_users: bool = Field()
    """Can you promote simple users to chat admins."""

    can_see_invite_link: bool = Field()
    """Can you see invite link for this chat."""

    can_moderate: bool = Field()
    """Can you moderate (delete) other users\' messages."""

    can_copy_chat: bool = Field()
    """Can you copy chat."""

    can_call: bool = Field()
    """Can you init group call in the chat."""

    can_use_mass_mentions: bool = Field()
    """Can you use mass mentions."""

    can_change_service_type: bool | None = Field(
        default=None,
    )
    """Can you change chat service type."""


class MessagesChatSettingsPermissionsInvite(StrEnum, metaclass=BaseEnumMeta):
    OWNER = "owner"
    OWNER_AND_ADMINS = "owner_and_admins"
    ALL = "all"


class MessagesChatSettingsPermissionsChangeInfo(StrEnum, metaclass=BaseEnumMeta):
    OWNER = "owner"
    OWNER_AND_ADMINS = "owner_and_admins"
    ALL = "all"


class MessagesChatSettingsPermissionsChangePin(StrEnum, metaclass=BaseEnumMeta):
    OWNER = "owner"
    OWNER_AND_ADMINS = "owner_and_admins"
    ALL = "all"


class MessagesChatSettingsPermissionsUseMassMentions(StrEnum, metaclass=BaseEnumMeta):
    OWNER = "owner"
    OWNER_AND_ADMINS = "owner_and_admins"
    ALL = "all"


class MessagesChatSettingsPermissionsSeeInviteLink(StrEnum, metaclass=BaseEnumMeta):
    OWNER = "owner"
    OWNER_AND_ADMINS = "owner_and_admins"
    ALL = "all"


class MessagesChatSettingsPermissionsCall(StrEnum, metaclass=BaseEnumMeta):
    OWNER = "owner"
    OWNER_AND_ADMINS = "owner_and_admins"
    ALL = "all"


class MessagesChatSettingsPermissionsChangeAdmins(StrEnum, metaclass=BaseEnumMeta):
    OWNER = "owner"
    OWNER_AND_ADMINS = "owner_and_admins"


class MessagesChatSettingsPermissions(BaseModel):
    """Model: `MessagesChatSettingsPermissions`"""

    invite: "MessagesChatSettingsPermissionsInvite | None" = Field(
        default=None,
    )
    """Who can invite users to chat."""

    change_info: "MessagesChatSettingsPermissionsChangeInfo | None" = Field(
        default=None,
    )
    """Who can change chat info."""

    change_pin: "MessagesChatSettingsPermissionsChangePin | None" = Field(
        default=None,
    )
    """Who can change pinned message."""

    use_mass_mentions: "MessagesChatSettingsPermissionsUseMassMentions | None" = Field(
        default=None,
    )
    """Who can use mass mentions."""

    see_invite_link: "MessagesChatSettingsPermissionsSeeInviteLink | None" = Field(
        default=None,
    )
    """Who can see invite link."""

    call: "MessagesChatSettingsPermissionsCall | None" = Field(
        default=None,
    )
    """Who can make calls."""

    change_admins: "MessagesChatSettingsPermissionsChangeAdmins | None" = Field(
        default=None,
    )
    """Who can change admins."""


class MessagesChatSettingsPhoto(BaseModel):
    """Model: `MessagesChatSettingsPhoto`"""

    photo_50: str | None = Field(
        default=None,
    )
    """URL of the preview image with 50px in width."""

    photo_100: str | None = Field(
        default=None,
    )
    """URL of the preview image with 100px in width."""

    photo_200: str | None = Field(
        default=None,
    )
    """URL of the preview image with 200px in width."""

    is_default_photo: bool | None = Field(
        default=None,
    )
    """If provided photo is default."""

    is_default_call_photo: bool | None = Field(
        default=None,
    )
    """If provided photo is default call photo."""


class MessagesChatSettingsState(StrEnum, metaclass=BaseEnumMeta):
    IN = "in"
    KICKED = "kicked"
    LEFT = "left"
    OUT = "out"


class MessagesConversationSpecialServiceType(StrEnum, metaclass=BaseEnumMeta):
    BUSINESS_NOTIFY = "business_notify"


class MessagesConversation(BaseModel):
    """Model: `MessagesConversation`"""

    peer: "MessagesConversationPeer" = Field()
    """Property `MessagesConversation.peer`."""

    last_message_id: int = Field()
    """ID of the last message in conversation."""

    last_conversation_message_id: int = Field()
    """Conversation message ID of the last message in conversation."""

    in_read: int = Field()
    """Last message user have read."""

    out_read: int = Field()
    """Last outcoming message have been read by the opponent."""

    version: int = Field()
    """Property `MessagesConversation.version`."""

    sort_id: "MessagesConversationSortId | None" = Field(
        default=None,
    )
    """Property `MessagesConversation.sort_id`."""

    unread_count: int | None = Field(
        default=None,
    )
    """Unread messages number."""

    is_marked_unread: bool | None = Field(
        default=None,
    )
    """Is this conversation unread."""

    out_read_by: "MessagesOutReadBy | None" = Field(
        default=None,
    )
    """Property `MessagesConversation.out_read_by`."""

    important: bool | None = Field(
        default=None,
    )
    """Property `MessagesConversation.important`."""

    unanswered: bool | None = Field(
        default=None,
    )
    """Property `MessagesConversation.unanswered`."""

    special_service_type: "MessagesConversationSpecialServiceType | None" = Field(
        default=None,
    )
    """Property `MessagesConversation.special_service_type`."""

    message_request_data: "MessagesMessageRequestData | None" = Field(
        default=None,
    )
    """Property `MessagesConversation.message_request_data`."""

    mentions: list[int] | None = Field(
        default=None,
    )
    """Ids of messages with mentions."""

    current_keyboard: "MessagesKeyboard | None" = Field(
        default=None,
    )
    """Property `MessagesConversation.current_keyboard`."""

    push_settings: "MessagesPushSettings | None" = Field(
        default=None,
    )
    """Property `MessagesConversation.push_settings`."""

    can_write: "MessagesConversationCanWrite | None" = Field(
        default=None,
    )
    """Property `MessagesConversation.can_write`."""

    chat_settings: "MessagesChatSettings | None" = Field(
        default=None,
    )
    """Property `MessagesConversation.chat_settings`."""

    style: str | None = Field(
        default=None,
    )
    """Property `MessagesConversation.style`."""

    peer_flags: int | None = Field(
        default=None,
    )
    """Property `MessagesConversation.peer_flags`."""


class MessagesConversationCanWrite(BaseModel):
    """Model: `MessagesConversationCanWrite`"""

    allowed: bool = Field()
    """Property `MessagesConversationCanWrite.allowed`."""

    reason: int | None = Field(
        default=None,
    )
    """Property `MessagesConversationCanWrite.reason`."""

    until: int | None = Field(
        default=None,
    )
    """Property `MessagesConversationCanWrite.until`."""


class MessagesConversationMember(BaseModel):
    """Model: `MessagesConversationMember`"""

    member_id: int = Field()
    """Property `MessagesConversationMember.member_id`."""

    can_kick: bool | None = Field(
        default=None,
    )
    """Is it possible for user to kick this member."""

    is_restricted_to_write: bool | None = Field(
        default=None,
    )
    """Does this member have write permission."""

    invited_by: int | None = Field(
        default=None,
    )
    """Property `MessagesConversationMember.invited_by`."""

    is_admin: bool | None = Field(
        default=None,
    )
    """Property `MessagesConversationMember.is_admin`."""

    is_owner: bool | None = Field(
        default=None,
    )
    """Property `MessagesConversationMember.is_owner`."""

    is_message_request: bool | None = Field(
        default=None,
    )
    """Property `MessagesConversationMember.is_message_request`."""

    join_date: datetime.datetime | None = Field(
        default=None,
    )
    """Property `MessagesConversationMember.join_date`."""

    request_date: datetime.datetime | None = Field(
        default=None,
    )
    """Message request date."""


class MessagesConversationPeer(BaseModel):
    """Model: `MessagesConversationPeer`"""

    id: int = Field()
    """Property `MessagesConversationPeer.id`."""

    type: "MessagesConversationPeerType" = Field()
    """Property `MessagesConversationPeer.type`."""

    local_id: int | None = Field(
        default=None,
    )
    """Property `MessagesConversationPeer.local_id`."""


class MessagesConversationPeerType(StrEnum, metaclass=BaseEnumMeta):
    CHAT = "chat"
    EMAIL = "email"
    USER = "user"
    GROUP = "group"


class MessagesConversationSortId(BaseModel):
    """Model: `MessagesConversationSortId`"""

    major_id: int = Field()
    """Major id for sorting conversations."""

    minor_id: int = Field()
    """Minor id for sorting conversations."""


class MessagesConversationWithMessage(BaseModel):
    """Model: `MessagesConversationWithMessage`"""

    conversation: "MessagesConversation" = Field()
    """Property `MessagesConversationWithMessage.conversation`."""

    last_message: "MessagesMessage | None" = Field(
        default=None,
    )
    """Property `MessagesConversationWithMessage.last_message`."""


class MessagesDeleteFullResponseItem(BaseModel):
    """Model: `MessagesDeleteFullResponseItem`"""

    peer_id: int | None = Field(
        default=None,
    )
    """Property `MessagesDeleteFullResponseItem.peer_id`."""

    message_id: int | None = Field(
        default=None,
    )
    """Property `MessagesDeleteFullResponseItem.message_id`."""

    conversation_message_id: int | None = Field(
        default=None,
    )
    """Property `MessagesDeleteFullResponseItem.conversation_message_id`."""

    response: bool | None = Field(
        default=None,
    )
    """Property `MessagesDeleteFullResponseItem.response`."""

    error: "BaseMessageError | None" = Field(
        default=None,
    )
    """Property `MessagesDeleteFullResponseItem.error`."""


class MessagesForeignMessage(BaseModel):
    """Model: `MessagesForeignMessage`"""

    conversation_message_id: int = Field()
    """Conversation message ID."""

    date: datetime.datetime = Field()
    """Date when the message was created."""

    from_id: int = Field()
    """Message author\'s ID."""

    text: str = Field()
    """Message text."""

    attachments: list["MessagesMessageAttachment"] | None = Field(
        default=None,
    )
    """Property `MessagesForeignMessage.attachments`."""

    fwd_messages: list["MessagesForeignMessage"] | None = Field(
        default=None,
    )
    """Property `MessagesForeignMessage.fwd_messages`."""

    geo: "BaseGeo | None" = Field(
        default=None,
    )
    """Property `MessagesForeignMessage.geo`."""

    id: int | None = Field(
        default=None,
    )
    """Message ID."""

    peer_id: int | None = Field(
        default=None,
    )
    """Peer ID."""

    reply_message: "MessagesForeignMessage | None" = Field(
        default=None,
    )
    """Property `MessagesForeignMessage.reply_message`."""

    update_time: int | None = Field(
        default=None,
    )
    """Date when the message has been updated in Unixtime."""

    was_listened: bool | None = Field(
        default=None,
    )
    """Was the audio message inside already listened by you."""

    payload: str | None = Field(
        default=None,
    )
    """Additional data sent along with message for developer convenience."""


class MessagesForward(BaseModel):
    """Model: `MessagesForward`"""

    owner_id: int | None = Field(
        default=None,
    )
    """Messages owner_id."""

    peer_id: int | None = Field(
        default=None,
    )
    """Messages peer_id."""

    conversation_message_ids: list[int] | None = Field(
        default=None,
    )
    """Property `MessagesForward.conversation_message_ids`."""

    cmids: list[int] | None = Field(
        default=None,
    )
    """Property `MessagesForward.cmids`."""

    message_ids: list[int] | None = Field(
        default=None,
    )
    """Property `MessagesForward.message_ids`."""

    is_reply: bool | None = Field(
        default=None,
    )
    """If you need to reply to a message."""


MessagesFwdMessages: typing.TypeAlias = list[list["MessagesForeignMessage"]]


class MessagesGetConversationById(BaseModel):
    """Model: `MessagesGetConversationById`"""

    count: int = Field()
    """Total number."""

    items: list["MessagesConversation"] = Field()
    """Property `MessagesGetConversationById.items`."""


class MessagesGetConversationMembers(BaseModel):
    """Model: `MessagesGetConversationMembers`"""

    items: list["MessagesConversationMember"] = Field()
    """Property `MessagesGetConversationMembers.items`."""

    count: int = Field()
    """Chat members count."""

    chat_restrictions: "MessagesChatRestrictions | None" = Field(
        default=None,
    )
    """Property `MessagesGetConversationMembers.chat_restrictions`."""

    profiles: list["UsersUserFull"] | None = Field(
        default=None,
    )
    """Property `MessagesGetConversationMembers.profiles`."""

    groups: list["GroupsGroupFull"] | None = Field(
        default=None,
    )
    """Property `MessagesGetConversationMembers.groups`."""


class MessagesGetInviteLinkByOwnerResponseItem(BaseModel):
    """Model: `MessagesGetInviteLinkByOwnerResponseItem`"""

    owner_id: int = Field()
    """Property `MessagesGetInviteLinkByOwnerResponseItem.owner_id`."""

    link: str | None = Field(
        default=None,
    )
    """Property `MessagesGetInviteLinkByOwnerResponseItem.link`."""

    error: "BaseMessageError | None" = Field(
        default=None,
    )
    """Property `MessagesGetInviteLinkByOwnerResponseItem.error`."""


class MessagesGraffiti(BaseModel):
    """Model: `MessagesGraffiti`"""

    id: int = Field()
    """Graffiti ID."""

    owner_id: int = Field()
    """Graffiti owner ID."""

    url: str = Field()
    """Graffiti URL."""

    width: int = Field()
    """Graffiti width."""

    height: int = Field()
    """Graffiti height."""

    access_key: str | None = Field(
        default=None,
    )
    """Access key for graffiti."""


class MessagesHistoryAttachment(BaseModel):
    """Model: `MessagesHistoryAttachment`"""

    attachment: "MessagesHistoryMessageAttachment" = Field()
    """Property `MessagesHistoryAttachment.attachment`."""

    date: datetime.datetime = Field()
    """Message sending time."""

    message_id: int = Field()
    """Message ID."""

    cmid: int = Field()
    """Conversation Message ID."""

    from_id: int = Field()
    """Message author\'s ID."""

    message_expire_ttl: int | None = Field(
        default=None,
    )
    """Message Exipire ttl."""

    forward_level: int | None = Field(
        default=None,
    )
    """Forward level (optional)."""

    was_listened: bool | None = Field(
        default=None,
    )
    """Property `MessagesHistoryAttachment.was_listened`."""

    position: int | None = Field(
        default=None,
    )
    """Attachment position in the Message."""


class MessagesHistoryMessageAttachment(BaseModel):
    """Model: `MessagesHistoryMessageAttachment`"""

    type: "MessagesHistoryMessageAttachmentType" = Field()
    """Property `MessagesHistoryMessageAttachment.type`."""

    audio: "AudioAudio | None" = Field(
        default=None,
    )
    """Property `MessagesHistoryMessageAttachment.audio`."""

    audio_message: "MessagesAudioMessage | None" = Field(
        default=None,
    )
    """Property `MessagesHistoryMessageAttachment.audio_message`."""

    doc: "DocsDoc | None" = Field(
        default=None,
    )
    """Property `MessagesHistoryMessageAttachment.doc`."""

    graffiti: "MessagesGraffiti | None" = Field(
        default=None,
    )
    """Property `MessagesHistoryMessageAttachment.graffiti`."""

    market: "MarketMarketItem | None" = Field(
        default=None,
    )
    """Property `MessagesHistoryMessageAttachment.market`."""

    photo: "PhotosPhoto | None" = Field(
        default=None,
    )
    """Property `MessagesHistoryMessageAttachment.photo`."""


class MessagesHistoryMessageAttachmentType(StrEnum, metaclass=BaseEnumMeta):
    APP_ACTION = "app_action"
    AUDIO = "audio"
    DOC = "doc"
    LINK = "link"
    MARKET = "market"
    PHOTO = "photo"
    VIDEO = "video"
    WALL = "wall"
    GRAFFITI = "graffiti"
    AUDIO_MESSAGE = "audio_message"


class MessagesKeyboard(BaseModel):
    """Model: `MessagesKeyboard`"""

    one_time: bool = Field()
    """Should this keyboard disappear on first use."""

    buttons: list[list["MessagesKeyboardButton"]] = Field()
    """Property `MessagesKeyboard.buttons`."""

    author_id: int | None = Field(
        default=None,
    )
    """Community or bot, which set this keyboard."""

    inline: bool | None = Field(
        default=None,
    )
    """Property `MessagesKeyboard.inline`."""


class MessagesKeyboardButtonColor(StrEnum, metaclass=BaseEnumMeta):
    DEFAULT = "default"
    POSITIVE = "positive"
    NEGATIVE = "negative"
    PRIMARY = "primary"


class MessagesKeyboardButton(BaseModel):
    """Model: `MessagesKeyboardButton`"""

    action: "MessagesKeyboardButtonPropertyAction" = Field()
    """Property `MessagesKeyboardButton.action`."""

    color: "MessagesKeyboardButtonColor | None" = Field(
        default=None,
    )
    """Button color."""


class MessagesKeyboardButtonActionCallbackType(StrEnum, metaclass=BaseEnumMeta):
    CALLBACK = "callback"


class MessagesKeyboardButtonActionCallback(BaseModel):
    """Description of the action, that should be performed on button click
    Model: `MessagesKeyboardButtonActionCallback`
    """

    label: str = Field()
    """Label for button."""

    type: "MessagesKeyboardButtonActionCallbackType" = Field()
    """Property `MessagesKeyboardButtonActionCallback.type`."""

    payload: str | None = Field(
        default=None,
    )
    """Additional data sent along with message for developer convenience."""


class MessagesKeyboardButtonActionLocationType(StrEnum, metaclass=BaseEnumMeta):
    LOCATION = "location"


class MessagesKeyboardButtonActionLocation(BaseModel):
    """Description of the action, that should be performed on button click
    Model: `MessagesKeyboardButtonActionLocation`
    """

    type: "MessagesKeyboardButtonActionLocationType" = Field()
    """Property `MessagesKeyboardButtonActionLocation.type`."""

    payload: str | None = Field(
        default=None,
    )
    """Additional data sent along with message for developer convenience."""


class MessagesKeyboardButtonActionOpenAppType(StrEnum, metaclass=BaseEnumMeta):
    OPEN_APP = "open_app"


class MessagesKeyboardButtonActionOpenApp(BaseModel):
    """Description of the action, that should be performed on button click
    Model: `MessagesKeyboardButtonActionOpenApp`
    """

    app_id: int = Field()
    """Fragment value in app link like vk.com/app{app_id}_-654321#hash."""

    label: str = Field()
    """Label for button."""

    owner_id: int = Field()
    """Fragment value in app link like vk.com/app123456_{owner_id}#hash."""

    type: "MessagesKeyboardButtonActionOpenAppType" = Field()
    """Property `MessagesKeyboardButtonActionOpenApp.type`."""

    hash: str | None = Field(
        default=None,
    )
    """Fragment value in app link like vk.com/app123456_-654321#{hash}."""

    payload: str | None = Field(
        default=None,
    )
    """Additional data sent along with message for developer convenience."""


class MessagesKeyboardButtonActionOpenLinkType(StrEnum, metaclass=BaseEnumMeta):
    OPEN_LINK = "open_link"


class MessagesKeyboardButtonActionOpenLink(BaseModel):
    """Description of the action, that should be performed on button click
    Model: `MessagesKeyboardButtonActionOpenLink`
    """

    label: str = Field()
    """Label for button."""

    link: str = Field()
    """link for button."""

    type: "MessagesKeyboardButtonActionOpenLinkType" = Field()
    """Property `MessagesKeyboardButtonActionOpenLink.type`."""

    payload: str | None = Field(
        default=None,
    )
    """Additional data sent along with message for developer convenience."""


class MessagesKeyboardButtonActionOpenPhotoType(StrEnum, metaclass=BaseEnumMeta):
    OPEN_PHOTO = "open_photo"


class MessagesKeyboardButtonActionOpenPhoto(BaseModel):
    """Description of the action, that should be performed on button click
    Model: `MessagesKeyboardButtonActionOpenPhoto`
    """

    type: "MessagesKeyboardButtonActionOpenPhotoType" = Field()
    """Property `MessagesKeyboardButtonActionOpenPhoto.type`."""


class MessagesKeyboardButtonActionTextType(StrEnum, metaclass=BaseEnumMeta):
    TEXT = "text"


class MessagesKeyboardButtonActionText(BaseModel):
    """Description of the action, that should be performed on button click
    Model: `MessagesKeyboardButtonActionText`
    """

    label: str = Field()
    """Label for button."""

    type: "MessagesKeyboardButtonActionTextType" = Field()
    """Property `MessagesKeyboardButtonActionText.type`."""

    payload: str | None = Field(
        default=None,
    )
    """Additional data sent along with message for developer convenience."""


class MessagesKeyboardButtonActionVkpayType(StrEnum, metaclass=BaseEnumMeta):
    VKPAY = "vkpay"


class MessagesKeyboardButtonActionVkpay(BaseModel):
    """Description of the action, that should be performed on button click
    Model: `MessagesKeyboardButtonActionVkpay`
    """

    hash: str = Field()
    """Fragment value in app link like vk.com/app123456_-654321#{hash}."""

    type: "MessagesKeyboardButtonActionVkpayType" = Field()
    """Property `MessagesKeyboardButtonActionVkpay.type`."""

    payload: str | None = Field(
        default=None,
    )
    """Additional data sent along with message for developer convenience."""


class MessagesKeyboardButtonPropertyAction(BaseModel):
    """Model: `MessagesKeyboardButtonPropertyAction`"""


class MessagesLastActivity(BaseModel):
    """Model: `MessagesLastActivity`"""

    online: bool = Field()
    """Information whether user is online."""

    time: int = Field()
    """Time when user was online in Unixtime."""


class MessagesLongpollMessages(BaseModel):
    """Model: `MessagesLongpollMessages`"""


class MessagesLongpollParams(BaseModel):
    """Model: `MessagesLongpollParams`"""

    server: str = Field()
    """Server URL."""

    key: str = Field()
    """Key."""

    ts: int = Field()
    """Timestamp."""

    pts: int | None = Field(
        default=None,
    )
    """Persistent timestamp."""


class MessagesMessageAction(BaseModel):
    """Model: `MessagesMessageAction`"""

    type: "MessagesMessageActionStatus" = Field()
    """Property `MessagesMessageAction.type`."""

    conversation_message_id: int | None = Field(
        default=None,
    )
    """Message ID."""

    email: str | None = Field(
        default=None,
    )
    """Email address for chat_invite_user or chat_kick_user actions."""

    member_id: int | None = Field(
        default=None,
    )
    """User or email peer ID."""

    message: str | None = Field(
        default=None,
    )
    """Message body of related message."""

    photo: "MessagesMessageActionPhoto | None" = Field(
        default=None,
    )
    """Property `MessagesMessageAction.photo`."""

    text: str | None = Field(
        default=None,
    )
    """New chat title for chat_create and chat_title_update actions."""


class MessagesMessageActionPhoto(BaseModel):
    """Model: `MessagesMessageActionPhoto`"""

    photo_50: str = Field()
    """URL of the preview image with 50px in width."""

    photo_100: str = Field()
    """URL of the preview image with 100px in width."""

    photo_200: str = Field()
    """URL of the preview image with 200px in width."""


class MessagesMessageActionStatus(StrEnum, metaclass=BaseEnumMeta):
    CHAT_PHOTO_UPDATE = "chat_photo_update"
    CHAT_PHOTO_REMOVE = "chat_photo_remove"
    CHAT_CREATE = "chat_create"
    CHAT_TITLE_UPDATE = "chat_title_update"
    CHAT_INVITE_USER = "chat_invite_user"
    CHAT_KICK_USER = "chat_kick_user"
    CHAT_PIN_MESSAGE = "chat_pin_message"
    CHAT_UNPIN_MESSAGE = "chat_unpin_message"
    CHAT_INVITE_USER_BY_LINK = "chat_invite_user_by_link"
    CHAT_INVITE_USER_BY_MESSAGE_REQUEST = "chat_invite_user_by_message_request"
    CHAT_SCREENSHOT = "chat_screenshot"


class MessagesMessageAttachment(BaseModel):
    """Model: `MessagesMessageAttachment`"""

    type: "MessagesMessageAttachmentType" = Field()
    """Property `MessagesMessageAttachment.type`."""

    audio: "AudioAudio | None" = Field(
        default=None,
    )
    """Property `MessagesMessageAttachment.audio`."""

    audio_message: "MessagesAudioMessage | None" = Field(
        default=None,
    )
    """Property `MessagesMessageAttachment.audio_message`."""

    call: "CallsCall | None" = Field(
        default=None,
    )
    """Property `MessagesMessageAttachment.call`."""

    doc: "DocsDoc | None" = Field(
        default=None,
    )
    """Property `MessagesMessageAttachment.doc`."""

    gift: "GiftsLayout | None" = Field(
        default=None,
    )
    """Property `MessagesMessageAttachment.gift`."""

    graffiti: "MessagesGraffiti | None" = Field(
        default=None,
    )
    """Property `MessagesMessageAttachment.graffiti`."""

    market: "MarketMarketItem | None" = Field(
        default=None,
    )
    """Property `MessagesMessageAttachment.market`."""

    market_market_album: "MarketMarketAlbum | None" = Field(
        default=None,
    )
    """Property `MessagesMessageAttachment.market_market_album`."""

    photo: "PhotosPhoto | None" = Field(
        default=None,
    )
    """Property `MessagesMessageAttachment.photo`."""

    sticker: "BaseSticker | None" = Field(
        default=None,
    )
    """Property `MessagesMessageAttachment.sticker`."""

    story: "StoriesStory | None" = Field(
        default=None,
    )
    """Property `MessagesMessageAttachment.story`."""

    wall_reply: "WallWallComment | None" = Field(
        default=None,
    )
    """Property `MessagesMessageAttachment.wall_reply`."""

    poll: "PollsPoll | None" = Field(
        default=None,
    )
    """Property `MessagesMessageAttachment.poll`."""


class MessagesMessageAttachmentType(StrEnum, metaclass=BaseEnumMeta):
    PHOTO = "photo"
    AUDIO = "audio"
    VIDEO = "video"
    VIDEO_PLAYLIST = "video_playlist"
    DOC = "doc"
    LINK = "link"
    MARKET = "market"
    GIFT = "gift"
    STICKER = "sticker"
    WALL = "wall"
    WALL_REPLY = "wall_reply"
    ARTICLE = "article"
    POLL = "poll"
    PODCASTS = "podcasts"
    CALL = "call"
    GRAFFITI = "graffiti"
    AUDIO_MESSAGE = "audio_message"


class MessagesMessageRequestData(BaseModel):
    """Model: `MessagesMessageRequestData`"""

    status: str | None = Field(
        default=None,
    )
    """Status of message request."""

    inviter_id: int | None = Field(
        default=None,
    )
    """Message request sender id."""

    request_date: datetime.datetime | None = Field(
        default=None,
    )
    """Message request date."""


class MessagesMessagesArray(BaseModel):
    """Model: `MessagesMessagesArray`"""

    count: int | None = Field(
        default=None,
    )
    """Property `MessagesMessagesArray.count`."""

    items: list["MessagesMessage"] | None = Field(
        default=None,
    )
    """Property `MessagesMessagesArray.items`."""


class MessagesOutReadBy(BaseModel):
    """Model: `MessagesOutReadBy`"""

    count: int | None = Field(
        default=None,
    )
    """Property `MessagesOutReadBy.count`."""

    member_ids: list[int] | None = Field(
        default=None,
    )
    """Property `MessagesOutReadBy.member_ids`."""


class MessagesPinnedMessage(BaseModel):
    """Model: `MessagesPinnedMessage`"""

    conversation_message_id: int = Field()
    """Unique auto-incremented number for all messages with this peer."""

    id: int = Field()
    """Message ID."""

    date: datetime.datetime = Field()
    """Date when the message has been sent in Unixtime."""

    from_id: int = Field()
    """Message author\'s ID."""

    peer_id: int = Field()
    """Peer ID."""

    text: str = Field()
    """Message text."""

    attachments: list["MessagesMessageAttachment"] | None = Field(
        default=None,
    )
    """Property `MessagesPinnedMessage.attachments`."""

    fwd_messages: list["MessagesForeignMessage"] | None = Field(
        default=None,
    )
    """Forwarded messages."""

    geo: "BaseGeo | None" = Field(
        default=None,
    )
    """Property `MessagesPinnedMessage.geo`."""

    reply_message: "MessagesForeignMessage | None" = Field(
        default=None,
    )
    """Property `MessagesPinnedMessage.reply_message`."""

    keyboard: "MessagesKeyboard | None" = Field(
        default=None,
    )
    """Property `MessagesPinnedMessage.keyboard`."""

    out: bool | None = Field(
        default=None,
    )
    """Information whether the message is outcoming."""

    important: bool | None = Field(
        default=None,
    )
    """Is it an important message."""


class MessagesPushSettings(BaseModel):
    """Model: `MessagesPushSettings`"""

    disabled_forever: bool = Field()
    """Information whether push notifications are disabled forever."""

    no_sound: bool = Field()
    """Information whether the sound is on."""

    disabled_until: int | None = Field(
        default=None,
    )
    """Time until what notifications are disabled."""

    disabled_mentions: bool | None = Field(
        default=None,
    )
    """Information whether the mentions are disabled."""

    disabled_mass_mentions: bool | None = Field(
        default=None,
    )
    """Information whether the mass mentions (like \'@all\', \'@online\') are disabled."""


class MessagesReactionAssetItem(BaseModel):
    """Model: `MessagesReactionAssetItem`"""

    reaction_id: int = Field()
    """Property `MessagesReactionAssetItem.reaction_id`."""

    links: "MessagesReactionAssetItemLinks" = Field()
    """Liks to reactions assets for each asset type."""


class MessagesReactionAssetItemLinks(BaseModel):
    """Model: `MessagesReactionAssetItemLinks`"""

    big_animation: str = Field()
    """Big reaction animation json file."""

    small_animation: str = Field()
    """Small reaction animation json file."""

    static: str = Field()
    """Reaction image file."""


class MessagesReactionCounterResponseItem(BaseModel):
    """Model: `MessagesReactionCounterResponseItem`"""

    reaction_id: int = Field()
    """Property `MessagesReactionCounterResponseItem.reaction_id`."""

    count: int = Field()
    """Property `MessagesReactionCounterResponseItem.count`."""

    user_ids: list[int] = Field()
    """Property `MessagesReactionCounterResponseItem.user_ids`."""


class MessagesReactionCountersResponseItem(BaseModel):
    """Model: `MessagesReactionCountersResponseItem`"""

    cmid: int = Field()
    """Property `MessagesReactionCountersResponseItem.cmid`."""

    counters: list["MessagesReactionCounterResponseItem"] = Field()
    """Property `MessagesReactionCountersResponseItem.counters`."""


class MessagesReactionResponseItem(BaseModel):
    """Model: `MessagesReactionResponseItem`"""

    user_id: int = Field()
    """Property `MessagesReactionResponseItem.user_id`."""

    reaction_id: int = Field()
    """Property `MessagesReactionResponseItem.reaction_id`."""


class MessagesSendUserIdsResponseItem(BaseModel):
    """Model: `MessagesSendUserIdsResponseItem`"""

    peer_id: int = Field()
    """Property `MessagesSendUserIdsResponseItem.peer_id`."""

    message_id: int = Field()
    """Property `MessagesSendUserIdsResponseItem.message_id`."""

    conversation_message_id: int = Field()
    """Property `MessagesSendUserIdsResponseItem.conversation_message_id`."""

    error: "BaseMessageError | None" = Field(
        default=None,
    )
    """Property `MessagesSendUserIdsResponseItem.error`."""


class MessagesTemplateActionTypeNames(StrEnum, metaclass=BaseEnumMeta):
    TEXT = "text"
    START = "start"
    LOCATION = "location"
    VKPAY = "vkpay"
    OPEN_APP = "open_app"
    OPEN_PHOTO = "open_photo"
    OPEN_LINK = "open_link"
    CALLBACK = "callback"
    INTENT_SUBSCRIBE = "intent_subscribe"
    INTENT_UNSUBSCRIBE = "intent_unsubscribe"
    OPEN_MODAL_VIEW = "open_modal_view"


class MessagesUserTypeForXtrInvitedBy(StrEnum, metaclass=BaseEnumMeta):
    PROFILE = "profile"
    GROUP = "group"


class AccountAccountCounters(BaseModel):
    """Model: `AccountAccountCounters`"""

    app_requests: int | None = Field(
        default=None,
    )
    """New app requests number."""

    events: int | None = Field(
        default=None,
    )
    """New events number."""

    faves: int | None = Field(
        default=None,
    )
    """New faves number."""

    friends: int | None = Field(
        default=None,
    )
    """New friends requests number."""

    friends_recommendations: int | None = Field(
        default=None,
    )
    """New friends recommendations number."""

    gifts: int | None = Field(
        default=None,
    )
    """New gifts number."""

    groups: int | None = Field(
        default=None,
    )
    """New groups number."""

    messages: int | None = Field(
        default=None,
    )
    """New messages number. Will be removed when messages.getCounters is released.."""

    memories: int | None = Field(
        default=None,
    )
    """New memories number."""

    notes: int | None = Field(
        default=None,
    )
    """New notes number."""

    notifications: int | None = Field(
        default=None,
    )
    """New notifications number."""

    photos: int | None = Field(
        default=None,
    )
    """New photo tags number."""


class AccountCountersFilter(StrEnum, metaclass=BaseEnumMeta):
    APP_REQUESTS = "app_requests"
    EVENTS = "events"
    FRIENDS = "friends"
    FRIENDS_RECOMMENDATIONS = "friends_recommendations"
    GAMES = "games"
    GIFTS = "gifts"
    GROUPS = "groups"
    MESSAGES = "messages"
    NOTES = "notes"
    NOTIFICATIONS = "notifications"
    PHOTOS = "photos"
    FAVES = "faves"
    MEMORIES = "memories"


class AccountInfo(BaseModel):
    """Model: `AccountInfo`"""

    f__2fa_required: bool | None = Field(
        default=None,
        alias="2fa_required",
    )
    """Two factor authentication is enabled."""

    https_required: bool | None = Field(
        default=None,
    )
    """Information whether HTTPS-only is enabled."""

    intro: int | None = Field(
        default=None,
    )
    """Information whether user has been processed intro."""

    lang: int | None = Field(
        default=None,
    )
    """Language ID."""

    no_wall_replies: bool | None = Field(
        default=None,
    )
    """Information whether wall comments should be hidden."""

    own_posts_default: bool | None = Field(
        default=None,
    )
    """Information whether only owners posts should be shown."""


class AccountNameRequest(BaseModel):
    """Model: `AccountNameRequest`"""

    first_name: str | None = Field(
        default=None,
    )
    """First name in request."""

    id: int | None = Field(
        default=None,
    )
    """Request ID needed to cancel the request."""

    last_name: str | None = Field(
        default=None,
    )
    """Last name in request."""

    status: "AccountNameRequestStatus | None" = Field(
        default=None,
    )
    """Property `AccountNameRequest.status`."""

    lang: str | None = Field(
        default=None,
    )
    """Text to display to user."""

    link_href: str | None = Field(
        default=None,
    )
    """href for link in lang field."""

    link_label: str | None = Field(
        default=None,
    )
    """label to display for link in lang field."""


class AccountNameRequestStatus(StrEnum, metaclass=BaseEnumMeta):
    SUCCESS = "success"
    PROCESSING = "processing"
    DECLINED = "declined"
    WAS_ACCEPTED = "was_accepted"
    WAS_DECLINED = "was_declined"
    DECLINED_WITH_LINK = "declined_with_link"
    RESPONSE = "response"
    RESPONSE_WITH_LINK = "response_with_link"


class AccountOfferLinkType(StrEnum, metaclass=BaseEnumMeta):
    PROFILE = "profile"
    GROUP = "group"
    APP = "app"


class AccountOffer(BaseModel):
    """Model: `AccountOffer`"""

    description: str | None = Field(
        default=None,
    )
    """Offer description."""

    id: int | None = Field(
        default=None,
    )
    """Offer ID."""

    img: str | None = Field(
        default=None,
    )
    """URL of the preview image."""

    instruction: str | None = Field(
        default=None,
    )
    """Instruction how to process the offer."""

    instruction_html: str | None = Field(
        default=None,
    )
    """Instruction how to process the offer (HTML format)."""

    price: int | None = Field(
        default=None,
    )
    """Offer price."""

    short_description: str | None = Field(
        default=None,
    )
    """Offer short description."""

    tag: str | None = Field(
        default=None,
    )
    """Offer tag."""

    title: str | None = Field(
        default=None,
    )
    """Offer title."""

    currency_amount: float | None = Field(
        default=None,
    )
    """Currency amount."""

    link_id: int | None = Field(
        default=None,
    )
    """Link id."""

    link_type: "AccountOfferLinkType | None" = Field(
        default=None,
    )
    """Link type."""


class AccountPushConversations(BaseModel):
    """Model: `AccountPushConversations`"""

    count: int | None = Field(
        default=None,
    )
    """Items count."""

    items: list["AccountPushConversationsItem"] | None = Field(
        default=None,
    )
    """Property `AccountPushConversations.items`."""


class AccountPushConversationsItem(BaseModel):
    """Model: `AccountPushConversationsItem`"""

    disabled_until: int = Field()
    """Time until that notifications are disabled in seconds."""

    peer_id: int = Field()
    """Peer ID."""

    sound: bool = Field()
    """Information whether the sound are enabled."""

    disabled_mentions: bool | None = Field(
        default=None,
    )
    """Information whether the mentions are disabled."""

    disabled_mass_mentions: bool | None = Field(
        default=None,
    )
    """Information whether the mass mentions (like \'@all\', \'@online\') are disabled. Can be affected by \'disabled_mentions\'."""


class AccountPushParams(BaseModel):
    """Model: `AccountPushParams`"""

    msg: list["AccountPushParamsMode"] | None = Field(
        default=None,
    )
    """Property `AccountPushParams.msg`."""

    chat: list["AccountPushParamsMode"] | None = Field(
        default=None,
    )
    """Property `AccountPushParams.chat`."""

    like: list["AccountPushParamsSettings"] | None = Field(
        default=None,
    )
    """Property `AccountPushParams.like`."""

    repost: list["AccountPushParamsSettings"] | None = Field(
        default=None,
    )
    """Property `AccountPushParams.repost`."""

    comment: list["AccountPushParamsSettings"] | None = Field(
        default=None,
    )
    """Property `AccountPushParams.comment`."""

    mention: list["AccountPushParamsSettings"] | None = Field(
        default=None,
    )
    """Property `AccountPushParams.mention`."""

    reply: list["AccountPushParamsOnoff"] | None = Field(
        default=None,
    )
    """Property `AccountPushParams.reply`."""

    new_post: list["AccountPushParamsOnoff"] | None = Field(
        default=None,
    )
    """Property `AccountPushParams.new_post`."""

    wall_post: list["AccountPushParamsOnoff"] | None = Field(
        default=None,
    )
    """Property `AccountPushParams.wall_post`."""

    wall_publish: list["AccountPushParamsOnoff"] | None = Field(
        default=None,
    )
    """Property `AccountPushParams.wall_publish`."""

    friend: list["AccountPushParamsOnoff"] | None = Field(
        default=None,
    )
    """Property `AccountPushParams.friend`."""

    friend_found: list["AccountPushParamsOnoff"] | None = Field(
        default=None,
    )
    """Property `AccountPushParams.friend_found`."""

    friend_accepted: list["AccountPushParamsOnoff"] | None = Field(
        default=None,
    )
    """Property `AccountPushParams.friend_accepted`."""

    group_invite: list["AccountPushParamsOnoff"] | None = Field(
        default=None,
    )
    """Property `AccountPushParams.group_invite`."""

    group_accepted: list["AccountPushParamsOnoff"] | None = Field(
        default=None,
    )
    """Property `AccountPushParams.group_accepted`."""

    birthday: list["AccountPushParamsOnoff"] | None = Field(
        default=None,
    )
    """Property `AccountPushParams.birthday`."""

    event_soon: list["AccountPushParamsOnoff"] | None = Field(
        default=None,
    )
    """Property `AccountPushParams.event_soon`."""

    app_request: list["AccountPushParamsOnoff"] | None = Field(
        default=None,
    )
    """Property `AccountPushParams.app_request`."""

    sdk_open: list["AccountPushParamsOnoff"] | None = Field(
        default=None,
    )
    """Property `AccountPushParams.sdk_open`."""


class AccountPushParamsMode(StrEnum, metaclass=BaseEnumMeta):
    ON = "on"
    OFF = "off"
    NO_SOUND = "no_sound"
    NO_TEXT = "no_text"


class AccountPushParamsOnoff(StrEnum, metaclass=BaseEnumMeta):
    ON = "on"
    OFF = "off"
    NO_SOUND = "no_sound"


class AccountPushParamsSettings(StrEnum, metaclass=BaseEnumMeta):
    ON = "on"
    OFF = "off"
    FR_OF_FR = "fr_of_fr"
    NO_SOUND = "no_sound"


class AccountPushSettings(BaseModel):
    """Model: `AccountPushSettings`"""

    disabled: bool | None = Field(
        default=None,
    )
    """Information whether notifications are disabled."""

    disabled_until: int | None = Field(
        default=None,
    )
    """Time until that notifications are disabled in Unixtime."""

    settings: "AccountPushParams | None" = Field(
        default=None,
    )
    """Property `AccountPushSettings.settings`."""

    conversations: "AccountPushConversations | None" = Field(
        default=None,
    )
    """Property `AccountPushSettings.conversations`."""


class AccountUserSettingsInterest(BaseModel):
    """Model: `AccountUserSettingsInterest`"""

    title: str = Field()
    """Property `AccountUserSettingsInterest.title`."""

    value: str = Field()
    """Property `AccountUserSettingsInterest.value`."""


class AccountUserSettingsInterests(BaseModel):
    """Model: `AccountUserSettingsInterests`"""

    activities: "AccountUserSettingsInterest | None" = Field(
        default=None,
    )
    """Property `AccountUserSettingsInterests.activities`."""

    interests: "AccountUserSettingsInterest | None" = Field(
        default=None,
    )
    """Property `AccountUserSettingsInterests.interests`."""

    music: "AccountUserSettingsInterest | None" = Field(
        default=None,
    )
    """Property `AccountUserSettingsInterests.music`."""

    tv: "AccountUserSettingsInterest | None" = Field(
        default=None,
    )
    """Property `AccountUserSettingsInterests.tv`."""

    movies: "AccountUserSettingsInterest | None" = Field(
        default=None,
    )
    """Property `AccountUserSettingsInterests.movies`."""

    books: "AccountUserSettingsInterest | None" = Field(
        default=None,
    )
    """Property `AccountUserSettingsInterests.books`."""

    games: "AccountUserSettingsInterest | None" = Field(
        default=None,
    )
    """Property `AccountUserSettingsInterests.games`."""

    quotes: "AccountUserSettingsInterest | None" = Field(
        default=None,
    )
    """Property `AccountUserSettingsInterests.quotes`."""

    about: "AccountUserSettingsInterest | None" = Field(
        default=None,
    )
    """Property `AccountUserSettingsInterests.about`."""


class AddressFields(StrEnum, metaclass=BaseEnumMeta):
    ID = "id"
    TITLE = "title"
    ADDRESS = "address"
    ADDITIONAL_ADDRESS = "additional_address"
    COUNTRY_ID = "country_id"
    CITY_ID = "city_id"
    CITY = "city"
    METRO_STATION_ID = "metro_station_id"
    METRO_STATION = "metro_station"
    LATITUDE = "latitude"
    LONGITUDE = "longitude"
    DISTANCE = "distance"
    WORK_INFO_STATUS = "work_info_status"
    TIMETABLE = "timetable"
    PHONE = "phone"
    TIME_OFFSET = "time_offset"


class AdsAccessRole(StrEnum, metaclass=BaseEnumMeta):
    ADMIN = "admin"
    MANAGER = "manager"
    REPORTS = "reports"


class AdsAccessRolePublic(StrEnum, metaclass=BaseEnumMeta):
    MANAGER = "manager"
    REPORTS = "reports"


class AdsAccesses(BaseModel):
    """Model: `AdsAccesses`"""

    client_id: str | None = Field(
        default=None,
    )
    """Client ID."""

    role: "AdsAccessRole | None" = Field(
        default=None,
    )
    """Property `AdsAccesses.role`."""


class AdsAccount(BaseModel):
    """Model: `AdsAccount`"""

    access_role: "AdsAccessRole" = Field()
    """Property `AdsAccount.access_role`."""

    account_id: int = Field()
    """Account ID."""

    account_status: bool = Field()
    """Information whether account is active."""

    account_type: "AdsAccountType" = Field()
    """Property `AdsAccount.account_type`."""

    account_name: str = Field()
    """Account name."""

    can_view_budget: bool = Field()
    """Can user view account budget."""


class AdsAccountType(StrEnum, metaclass=BaseEnumMeta):
    GENERAL = "general"
    AGENCY = "agency"


class AdsAd(BaseModel):
    """Model: `AdsAd`"""

    ad_format: int = Field()
    """Ad format."""

    ad_platform: int | str = Field()
    """Ad platform."""

    all_limit: str = Field()
    """Total limit."""

    approved: "AdsAdApproved" = Field()
    """Property `AdsAd.approved`."""

    campaign_id: int = Field()
    """Campaign ID."""

    cost_type: "AdsAdCostType" = Field()
    """Property `AdsAd.cost_type`."""

    id: int = Field()
    """Ad ID."""

    name: str = Field()
    """Ad title."""

    status: "AdsAdStatus" = Field()
    """Property `AdsAd.status`."""

    category1_id: int | None = Field(
        default=None,
    )
    """Category ID."""

    category2_id: int | None = Field(
        default=None,
    )
    """Additional category ID."""

    cpc: str | None = Field(
        default=None,
    )
    """Cost of a click, kopecks."""

    cpm: str | None = Field(
        default=None,
    )
    """Cost of 1000 impressions, kopecks."""

    cpa: str | None = Field(
        default=None,
    )
    """Cost of an action, kopecks."""

    ocpm: str | None = Field(
        default=None,
    )
    """Cost of 1000 impressions optimized, kopecks."""

    autobidding: bool | None = Field(
        default=None,
    )
    """Autobidding."""

    autobidding_max_cost: str | None = Field(
        default=None,
    )
    """Max cost of target actions for autobidding, kopecks."""

    disclaimer_medical: bool | None = Field(
        default=None,
    )
    """Information whether disclaimer is enabled."""

    disclaimer_specialist: bool | None = Field(
        default=None,
    )
    """Information whether disclaimer is enabled."""

    disclaimer_supplements: bool | None = Field(
        default=None,
    )
    """Information whether disclaimer is enabled."""

    disclaimer_credits: bool | None = Field(
        default=None,
    )
    """Information whether disclaimer is enabled."""

    impressions_limit: int | None = Field(
        default=None,
    )
    """Impressions limit."""

    impressions_limit_period: int | None = Field(
        default=None,
    )
    """Impressions limit period."""

    impressions_limited: bool | None = Field(
        default=None,
    )
    """Information whether impressions are limited."""

    video: bool | None = Field(
        default=None,
    )
    """Information whether the ad is a video."""

    day_limit: str | None = Field(
        default=None,
    )
    """Day limit."""

    goal_type: int | None = Field(
        default=None,
    )
    """Goal type."""

    user_goal_type: int | None = Field(
        default=None,
    )
    """User goal type."""

    age_restriction: int | None = Field(
        default=None,
    )
    """Age restriction."""

    conversion_pixel_id: int | None = Field(
        default=None,
    )
    """Conversion pixel id."""

    conversion_event_id: int | None = Field(
        default=None,
    )
    """Conversion event id."""

    create_time: int | None = Field(
        default=None,
    )
    """Create time."""

    update_time: int | None = Field(
        default=None,
    )
    """Update time."""

    start_time: int | None = Field(
        default=None,
    )
    """Start time."""

    stop_time: int | None = Field(
        default=None,
    )
    """Stop time."""

    publisher_platforms_auto: bool | None = Field(
        default=None,
    )
    """Publisher platform auto."""

    publisher_platforms: str | None = Field(
        default=None,
    )
    """Publisher platforms."""

    link_url: str | None = Field(
        default=None,
    )
    """Link url."""

    link_owner_id: int | None = Field(
        default=None,
    )
    """Link owner id."""

    link_id: int | None = Field(
        default=None,
    )
    """Link id."""

    has_campaign_budget_optimization: bool | None = Field(
        default=None,
    )
    """Has campaign budget optimization."""

    events_retargeting_groups: list["AdsEventsRetargetingGroup"] | None = Field(
        default=None,
    )
    """Events retargeting groups."""

    weekly_schedule_hours: list[str] | None = Field(
        default=None,
    )
    """Weekly schedule hours."""

    weekly_schedule_use_holidays: int | None = Field(
        default=None,
    )
    """Weekly schedule use holidays."""

    ad_platform_no_ad_network: int | None = Field(
        default=None,
    )
    """Ad platform no ad network."""

    ad_platform_no_wall: int | None = Field(
        default=None,
    )
    """Ad platform no wall."""

    disclaimer_finance: int | None = Field(
        default=None,
    )
    """Disclaimer finance."""

    disclaimer_finance_name: str | None = Field(
        default=None,
    )
    """Disclaimer finance name."""

    disclaimer_finance_license_no: str | None = Field(
        default=None,
    )
    """Disclaimer finance license no."""

    is_promo: bool | None = Field(
        default=None,
    )
    """is promo."""

    suggested_criteria: int | None = Field(
        default=None,
    )
    """Suggested criteria."""

    link_type: int | None = Field(
        default=None,
    )
    """Link type."""


class AdsAdApproved(IntEnum, metaclass=BaseEnumMeta):
    NOT_MODERATED = 0
    PENDING_MODERATION = 1
    APPROVED = 2
    REJECTED = 3


class AdsAdCostType(IntEnum, metaclass=BaseEnumMeta):
    PER_CLICKS = 0
    PER_IMPRESSIONS = 1
    PER_ACTIONS = 2
    PER_IMPRESSIONS_OPTIMIZED = 3


class AdsAdLayout(BaseModel):
    """Model: `AdsAdLayout`"""

    ad_format: int = Field()
    """Ad format."""

    campaign_id: int = Field()
    """Campaign ID."""

    cost_type: "AdsAdCostType" = Field()
    """Property `AdsAdLayout.cost_type`."""

    description: str = Field()
    """Ad description."""

    id: int = Field()
    """Ad ID."""

    image_src: str = Field()
    """Image URL."""

    link_url: str = Field()
    """URL of advertised object."""

    link_type: int = Field()
    """Type of advertised object."""

    title: str = Field()
    """Ad title."""

    image_src_2x: str | None = Field(
        default=None,
    )
    """URL of the preview image in double size."""

    link_domain: str | None = Field(
        default=None,
    )
    """Domain of advertised object."""

    preview_link: str | None = Field(
        default=None,
    )
    """link to preview an ad as it is shown on the website."""

    video: bool | None = Field(
        default=None,
    )
    """Information whether the ad is a video."""

    social: bool | None = Field(
        default=None,
    )
    """Social."""

    okved: str | None = Field(
        default=None,
    )
    """Okved."""

    age_restriction: int | None = Field(
        default=None,
    )
    """Age restriction."""

    goal_type: int | None = Field(
        default=None,
    )
    """Goal type."""

    link_title: str | None = Field(
        default=None,
    )
    """Link title."""

    link_button: str | None = Field(
        default=None,
    )
    """Link button."""

    repeat_video: int | None = Field(
        default=None,
    )
    """Repeat video."""

    video_src_240: str | None = Field(
        default=None,
    )
    """Video source 240p."""

    video_src_360: str | None = Field(
        default=None,
    )
    """Video source 360p."""

    video_src_480: str | None = Field(
        default=None,
    )
    """Video source 480p."""

    video_src_720: str | None = Field(
        default=None,
    )
    """Video source 720p."""

    video_src_1080: str | None = Field(
        default=None,
    )
    """Video source 1080p."""

    video_src_1440: str | None = Field(
        default=None,
    )
    """Video source 1440p."""

    video_src_2160: str | None = Field(
        default=None,
    )
    """Video source 2160p."""

    video_image_src: str | None = Field(
        default=None,
    )
    """Video image source."""

    video_image_src_2x: str | None = Field(
        default=None,
    )
    """Video image source 2x."""

    video_duration: int | None = Field(
        default=None,
    )
    """Video duration."""

    icon_src: str | None = Field(
        default=None,
    )
    """Icon source."""

    icon_src_2x: str | None = Field(
        default=None,
    )
    """Icon source 2x."""

    post: "AdsPost | None" = Field(
        default=None,
    )
    """Property `AdsAdLayout.post`."""

    stories_data: "AdsStories | None" = Field(
        default=None,
    )
    """Property `AdsAdLayout.stories_data`."""

    clips_list: list["AdsClipItem"] | None = Field(
        default=None,
    )
    """Property `AdsAdLayout.clips_list`."""


class AdsAdStatus(IntEnum, metaclass=BaseEnumMeta):
    STOPPED = 0
    STARTED = 1
    DELETED = 2


class AdsCampaign(BaseModel):
    """Model: `AdsCampaign`"""

    all_limit: str = Field()
    """Campaign\'s total limit, rubles."""

    day_limit: str = Field()
    """Campaign\'s day limit, rubles."""

    id: int = Field()
    """Campaign ID."""

    name: str = Field()
    """Campaign title."""

    start_time: int = Field()
    """Campaign start time, as Unixtime."""

    status: "AdsCampaignStatus" = Field()
    """Property `AdsCampaign.status`."""

    stop_time: int = Field()
    """Campaign stop time, as Unixtime."""

    type: "AdsCampaignType" = Field()
    """Property `AdsCampaign.type`."""

    ads_count: int | None = Field(
        default=None,
    )
    """Amount of active ads in campaign."""

    create_time: int | None = Field(
        default=None,
    )
    """Campaign create time, as Unixtime."""

    goal_type: int | None = Field(
        default=None,
    )
    """Campaign goal type."""

    user_goal_type: int | None = Field(
        default=None,
    )
    """Campaign user goal type."""

    is_cbo_enabled: bool | None = Field(
        default=None,
    )
    """Shows if Campaign Budget Optimization is on."""

    update_time: int | None = Field(
        default=None,
    )
    """Campaign update time, as Unixtime."""

    views_limit: int | None = Field(
        default=None,
    )
    """Limit of views per user per campaign."""


class AdsCampaignStatus(IntEnum, metaclass=BaseEnumMeta):
    STOPPED = 0
    STARTED = 1
    DELETED = 2


class AdsCampaignType(StrEnum, metaclass=BaseEnumMeta):
    NORMAL = "normal"
    VK_APPS_MANAGED = "vk_apps_managed"
    MOBILE_APPS = "mobile_apps"
    PROMOTED_POSTS = "promoted_posts"
    ADAPTIVE_ADS = "adaptive_ads"
    STORIES = "stories"


class AdsCategory(BaseModel):
    """Model: `AdsCategory`"""

    id: int = Field()
    """Category ID."""

    name: str = Field()
    """Category name."""

    subcategories: list["AdsCategory"] | None = Field(
        default=None,
    )
    """Property `AdsCategory.subcategories`."""


class AdsClient(BaseModel):
    """Model: `AdsClient`"""

    all_limit: str = Field()
    """Client\'s total limit, rubles."""

    day_limit: str = Field()
    """Client\'s day limit, rubles."""

    id: int = Field()
    """Client ID."""

    name: str = Field()
    """Client name."""

    ord_data: "AdsOrdData | None" = Field(
        default=None,
    )
    """Ord data."""


class AdsClipItem(BaseModel):
    """Model: `AdsClipItem`"""

    video_id: int | None = Field(
        default=None,
    )
    """Video id."""

    preview_url: str | None = Field(
        default=None,
    )
    """Preview url."""

    link: "AdsClipItemLink | None" = Field(
        default=None,
    )
    """Property `AdsClipItem.link`."""


class AdsClipItemLink(BaseModel):
    """Link
    Model: `AdsClipItemLink`
    """

    text: str | None = Field(
        default=None,
    )
    """Text."""

    key: str | None = Field(
        default=None,
    )
    """Key."""

    url: str | None = Field(
        default=None,
    )
    """Url."""


class AdsCreateAdStatus(BaseModel):
    """Model: `AdsCreateAdStatus`"""

    id: int = Field()
    """Ad ID."""

    post_id: int | None = Field(
        default=None,
    )
    """Stealth Post ID."""

    error_code: int | None = Field(
        default=None,
    )
    """Error code."""

    error_desc: str | None = Field(
        default=None,
    )
    """Error description."""


class AdsCreateCampaignStatus(BaseModel):
    """Model: `AdsCreateCampaignStatus`"""

    id: int = Field()
    """Campaign ID."""

    error_code: int | None = Field(
        default=None,
    )
    """Error code."""

    error_desc: str | None = Field(
        default=None,
    )
    """Error description."""


class AdsCreateClientsStatus(BaseModel):
    """Model: `AdsCreateClientsStatus`"""

    id: int = Field()
    """Client ID."""

    error_code: int | None = Field(
        default=None,
    )
    """Error code."""

    error_desc: str | None = Field(
        default=None,
    )
    """Error description."""


class AdsCriteria(BaseModel):
    """Model: `AdsCriteria`"""

    age_from: str | None = Field(
        default=None,
    )
    """Age from."""

    age_to: str | None = Field(
        default=None,
    )
    """Age to."""

    apps: str | None = Field(
        default=None,
    )
    """Apps IDs."""

    apps_not: str | None = Field(
        default=None,
    )
    """Apps IDs to except."""

    birthday: str | None = Field(
        default=None,
    )
    """Days to birthday."""

    cities: str | None = Field(
        default=None,
    )
    """Cities IDs."""

    cities_not: str | None = Field(
        default=None,
    )
    """Cities IDs to except."""

    districts: str | None = Field(
        default=None,
    )
    """Districts IDs."""

    groups: str | None = Field(
        default=None,
    )
    """Communities IDs."""

    interest_categories: str | None = Field(
        default=None,
    )
    """Interests categories IDs."""

    interests: str | None = Field(
        default=None,
    )
    """Interests."""

    paying: str | None = Field(
        default=None,
    )
    """Information whether the user has proceeded VK payments before."""

    positions: str | None = Field(
        default=None,
    )
    """Positions IDs."""

    religions: str | None = Field(
        default=None,
    )
    """Religions IDs."""

    retargeting_groups: str | None = Field(
        default=None,
    )
    """Retargeting groups ids."""

    retargeting_groups_not: str | None = Field(
        default=None,
    )
    """Retargeting groups NOT ids."""

    school_from: str | None = Field(
        default=None,
    )
    """School graduation year from."""

    school_to: str | None = Field(
        default=None,
    )
    """School graduation year to."""

    schools: str | None = Field(
        default=None,
    )
    """Schools IDs."""

    sex: "AdsCriteriaSex | None" = Field(
        default=None,
    )
    """Property `AdsCriteria.sex`."""

    stations: str | None = Field(
        default=None,
    )
    """Stations IDs."""

    statuses: str | None = Field(
        default=None,
    )
    """Relationship statuses."""

    streets: str | None = Field(
        default=None,
    )
    """Streets IDs."""

    travellers: str | None = Field(
        default=None,
    )
    """Travellers."""

    ab_test: str | None = Field(
        default=None,
    )
    """AB test."""

    uni_from: str | None = Field(
        default=None,
    )
    """University graduation year from."""

    uni_to: str | None = Field(
        default=None,
    )
    """University graduation year to."""

    user_browsers: str | None = Field(
        default=None,
    )
    """Browsers."""

    user_devices: str | None = Field(
        default=None,
    )
    """Devices."""

    user_os: str | None = Field(
        default=None,
    )
    """Operating systems."""

    suggested_criteria: str | None = Field(
        default=None,
    )
    """Suggested criteria."""

    groups_not: str | None = Field(
        default=None,
    )
    """Group not."""

    price_list_audience_type: str | None = Field(
        default=None,
    )
    """Price list audience type."""

    count: str | None = Field(
        default=None,
    )
    """Count."""

    groups_active_formula: str | None = Field(
        default=None,
    )
    """Group active formula."""

    interest_categories_formula: str | None = Field(
        default=None,
    )
    """Interest categories formula."""

    groups_formula: str | None = Field(
        default=None,
    )
    """Groups formula."""

    groups_active: str | None = Field(
        default=None,
    )
    """Groups active."""

    group_types: str | None = Field(
        default=None,
    )
    """Group types."""

    key_phrases: str | None = Field(
        default=None,
    )
    """Key phrases."""

    key_phrases_days: str | None = Field(
        default=None,
    )
    """Key phrases days."""

    geo_near: str | None = Field(
        default=None,
    )
    """Geo near."""

    geo_point_type: str | None = Field(
        default=None,
    )
    """Geo point type."""

    price_list_id: str | None = Field(
        default=None,
    )
    """Price list id."""

    groups_recommended: str | None = Field(
        default=None,
    )
    """Groups recommended ids."""

    groups_active_recommended: str | None = Field(
        default=None,
    )
    """Groups active recommended ids."""

    music_artists_formula: str | None = Field(
        default=None,
    )
    """Music artists formula."""

    price_list_retargeting_formula: str | None = Field(
        default=None,
    )
    """Price list retargeting formula."""

    tags: str | None = Field(
        default=None,
    )
    """Tags."""

    browsers: str | None = Field(
        default=None,
    )
    """Browsers."""

    mobile_os_min_version: str | None = Field(
        default=None,
    )
    """Mobile os min version."""

    mobile_apps_events_formula: str | None = Field(
        default=None,
    )
    """Mobile apps events formula."""

    mobile_os_max_version: str | None = Field(
        default=None,
    )
    """Mobile os max version."""

    operators: str | None = Field(
        default=None,
    )
    """operators."""

    wifi_only: str | None = Field(
        default=None,
    )
    """wifi_only."""

    mobile_manufacturers: str | None = Field(
        default=None,
    )
    """mobile_manufacturers."""


class AdsCriteriaSex(StrEnum, metaclass=BaseEnumMeta):
    f__0 = "0"
    f__1 = "1"
    f__2 = "2"


class AdsDemoStats(BaseModel):
    """Model: `AdsDemoStats`"""

    id: int | None = Field(
        default=None,
    )
    """Object ID."""

    stats: list["AdsDemostatsFormat"] | None = Field(
        default=None,
    )
    """Property `AdsDemoStats.stats`."""

    type: "AdsObjectType | None" = Field(
        default=None,
    )
    """Property `AdsDemoStats.type`."""


class AdsDemographicStatsPeriodItemBase(BaseModel):
    """Model: `AdsDemographicStatsPeriodItemBase`"""

    clicks_rate: float | None = Field(
        default=None,
    )
    """Clicks rate."""

    impressions_rate: float | None = Field(
        default=None,
    )
    """Impressions rate."""


class AdsDemostatsFormat(BaseModel):
    """Model: `AdsDemostatsFormat`"""

    age: list["AdsStatsAge"] | None = Field(
        default=None,
    )
    """Property `AdsDemostatsFormat.age`."""

    cities: list["AdsStatsCities"] | None = Field(
        default=None,
    )
    """Property `AdsDemostatsFormat.cities`."""

    day: str | None = Field(
        default=None,
    )
    """Day as YYYY-MM-DD."""

    day_from: str | None = Field(
        default=None,
    )
    """Property `AdsDemostatsFormat.day_from`."""

    day_to: str | None = Field(
        default=None,
    )
    """Property `AdsDemostatsFormat.day_to`."""

    month: str | None = Field(
        default=None,
    )
    """Month as YYYY-MM."""

    overall: int | None = Field(
        default=None,
    )
    """1 if period=overall."""

    sex: list["AdsStatsSex"] | None = Field(
        default=None,
    )
    """Property `AdsDemostatsFormat.sex`."""

    sex_age: list["AdsStatsSexAge"] | None = Field(
        default=None,
    )
    """Property `AdsDemostatsFormat.sex_age`."""


class AdsEventsRetargetingGroup(BaseModel):
    """Model: `AdsEventsRetargetingGroup`"""

    id: int | None = Field(
        default=None,
    )
    """Property `AdsEventsRetargetingGroup.id`."""

    value: list[int] | None = Field(
        default=None,
    )
    """Property `AdsEventsRetargetingGroup.value`."""


class AdsFloodStats(BaseModel):
    """Model: `AdsFloodStats`"""

    left: int = Field()
    """Requests left."""

    refresh: int = Field()
    """Time to refresh in seconds."""

    stats_by_user: list["AdsFloodStatsByUserItem"] | None = Field(
        default=None,
    )
    """Used requests per user."""


class AdsFloodStatsByUserItem(BaseModel):
    """Model: `AdsFloodStatsByUserItem`"""

    user_id: int = Field()
    """User ID."""

    requests_count: int = Field()
    """Used requests."""


class AdsLinkStatus(BaseModel):
    """Model: `AdsLinkStatus`"""

    status: str = Field()
    """Link status."""

    description: str | None = Field(
        default=None,
    )
    """Reject reason."""

    redirect_url: str | None = Field(
        default=None,
    )
    """URL."""


class AdsLookalikeRequestStatus(StrEnum, metaclass=BaseEnumMeta):
    SEARCH_IN_PROGRESS = "search_in_progress"
    SEARCH_FAILED = "search_failed"
    SEARCH_DONE = "search_done"
    SAVE_IN_PROGRESS = "save_in_progress"
    SAVE_FAILED = "save_failed"
    SAVE_DONE = "save_done"


class AdsLookalikeRequestSourceType(StrEnum, metaclass=BaseEnumMeta):
    RETARGETING_GROUP = "retargeting_group"


class AdsLookalikeRequest(BaseModel):
    """Model: `AdsLookalikeRequest`"""

    id: int = Field()
    """Lookalike request ID."""

    create_time: int = Field()
    """Lookalike request create time, as Unixtime."""

    update_time: int = Field()
    """Lookalike request update time, as Unixtime."""

    status: "AdsLookalikeRequestStatus" = Field()
    """Lookalike request status."""

    source_type: "AdsLookalikeRequestSourceType" = Field()
    """Lookalike request source type."""

    scheduled_delete_time: int | None = Field(
        default=None,
    )
    """Time by which lookalike request would be deleted, as Unixtime."""

    source_retargeting_group_id: int | None = Field(
        default=None,
    )
    """Retargeting group id, which was used as lookalike seed."""

    source_name: str | None = Field(
        default=None,
    )
    """Lookalike request seed name (retargeting group name)."""

    audience_count: int | None = Field(
        default=None,
    )
    """Lookalike request seed audience size."""

    save_audience_levels: list["AdsLookalikeRequestSaveAudienceLevel"] | None = Field(
        default=None,
    )
    """Property `AdsLookalikeRequest.save_audience_levels`."""


class AdsLookalikeRequestSaveAudienceLevel(BaseModel):
    """Model: `AdsLookalikeRequestSaveAudienceLevel`"""

    level: int | None = Field(
        default=None,
    )
    """Save audience level id, which is used in save audience queries."""

    audience_count: int | None = Field(
        default=None,
    )
    """Saved audience audience size for according level."""


class AdsMobileStatItem(BaseModel):
    """Model: `AdsMobileStatItem`"""

    key: str | None = Field(
        default=None,
    )
    """Property `AdsMobileStatItem.key`."""

    value: float | None = Field(
        default=None,
    )
    """Property `AdsMobileStatItem.value`."""


class AdsMusician(BaseModel):
    """Model: `AdsMusician`"""

    id: int = Field()
    """Targeting music artist ID."""

    original_id: str = Field()
    """Music artist ID as in VKMusic."""

    name: str = Field()
    """Music artist name."""

    avatar: str | None = Field(
        default=None,
    )
    """Music artist photo."""


class AdsObjectType(StrEnum, metaclass=BaseEnumMeta):
    AD = "ad"
    CAMPAIGN = "campaign"
    CLIENT = "client"
    OFFICE = "office"


class AdsOrdClientType(StrEnum, metaclass=BaseEnumMeta):
    PERSON = "person"
    INDIVIDUAL = "individual"
    LEGAL = "legal"
    FOREIGN = "foreign"
    UNKNOWN = "unknown"


class AdsOrdData(BaseModel):
    """Model: `AdsOrdData`"""

    client_type: "AdsOrdClientType" = Field()
    """Property `AdsOrdData.client_type`."""

    client_name: str = Field()
    """Property `AdsOrdData.client_name`."""

    phone: str = Field()
    """Property `AdsOrdData.phone`."""

    contract_number: str = Field()
    """Property `AdsOrdData.contract_number`."""

    contract_date: str = Field()
    """Property `AdsOrdData.contract_date`."""

    contract_type: str = Field()
    """Property `AdsOrdData.contract_type`."""

    contract_object: str = Field()
    """Property `AdsOrdData.contract_object`."""

    with_vat: bool = Field()
    """Property `AdsOrdData.with_vat`."""

    inn: str | None = Field(
        default=None,
    )
    """Property `AdsOrdData.inn`."""

    agency_phone: str | None = Field(
        default=None,
    )
    """Property `AdsOrdData.agency_phone`."""

    subagent: "AdsOrdSubagent | None" = Field(
        default=None,
    )
    """Property `AdsOrdData.subagent`."""


class AdsOrdSubagent(BaseModel):
    """Model: `AdsOrdSubagent`"""

    type: "AdsOrdClientType" = Field()
    """Property `AdsOrdSubagent.type`."""

    name: str = Field()
    """Property `AdsOrdSubagent.name`."""

    phone: str = Field()
    """Property `AdsOrdSubagent.phone`."""

    inn: str | None = Field(
        default=None,
    )
    """Property `AdsOrdSubagent.inn`."""


class AdsPost(BaseModel):
    """Model: `AdsPost`"""

    id: int | None = Field(
        default=None,
    )
    """Post id."""

    from_id: int | None = Field(
        default=None,
    )
    """From id."""

    owner_id: int | None = Field(
        default=None,
    )
    """Owner id."""

    date: datetime.datetime | None = Field(
        default=None,
    )
    """Date."""

    edited: int | None = Field(
        default=None,
    )
    """Edited date."""

    is_pinned: int | None = Field(
        default=None,
    )
    """Is pinned."""

    marked_as_ads: int | None = Field(
        default=None,
    )
    """Marked as ads."""

    ads_easy_promote: "AdsPostEasyPromote | None" = Field(
        default=None,
    )
    """Property `AdsPost.ads_easy_promote`."""

    donut: "AdsPostDonut | None" = Field(
        default=None,
    )
    """Property `AdsPost.donut`."""

    comments: "AdsPostComments | None" = Field(
        default=None,
    )
    """Property `AdsPost.comments`."""

    copyright: "WallPostCopyright | None" = Field(
        default=None,
    )
    """Property `AdsPost.copyright`."""

    short_text_rate: float | None = Field(
        default=None,
    )
    """Short text rate."""

    type: str | None = Field(
        default=None,
    )
    """Type."""

    is_favorite: bool | None = Field(
        default=None,
    )
    """Is favorite."""

    likes: "AdsPostLikes | None" = Field(
        default=None,
    )
    """Property `AdsPost.likes`."""

    views: "AdsPostViews | None" = Field(
        default=None,
    )
    """Property `AdsPost.views`."""

    post_type: str | None = Field(
        default=None,
    )
    """Post type."""

    reposts: "AdsPostReposts | None" = Field(
        default=None,
    )
    """Property `AdsPost.reposts`."""

    text: str | None = Field(
        default=None,
    )
    """Text."""

    is_promoted_post_stealth: bool | None = Field(
        default=None,
    )
    """Is promoted post stealth."""

    hash: str | None = Field(
        default=None,
    )
    """Hash."""

    owner: "AdsPostOwner | None" = Field(
        default=None,
    )
    """Property `AdsPost.owner`."""

    attachments: list["WallWallpostAttachment"] | None = Field(
        default=None,
    )
    """Property `AdsPost.attachments`."""

    created_by: int | None = Field(
        default=None,
    )
    """Created by."""

    carousel_offset: int | None = Field(
        default=None,
    )
    """Carousel offset."""

    can_edit: int | None = Field(
        default=None,
    )
    """Can edit."""

    can_delete: int | None = Field(
        default=None,
    )
    """Can delete."""

    can_pin: int | None = Field(
        default=None,
    )
    """Can pin."""


class AdsPostComments(BaseModel):
    """Comments
    Model: `AdsPostComments`
    """

    count: int | None = Field(
        default=None,
    )
    """Count."""


class AdsPostDonut(BaseModel):
    """Donut
    Model: `AdsPostDonut`
    """

    is_donut: bool | None = Field(
        default=None,
    )
    """Is donut."""


class AdsPostEasyPromote(BaseModel):
    """Ads easy promote
    Model: `AdsPostEasyPromote`
    """

    type: int | None = Field(
        default=None,
    )
    """Type."""

    text: str | None = Field(
        default=None,
    )
    """Text."""

    label_text: str | None = Field(
        default=None,
    )
    """Label text."""

    button_text: str | None = Field(
        default=None,
    )
    """Button text."""

    is_ad_not_easy: bool | None = Field(
        default=None,
    )
    """Is ad not easy."""

    ad_id: int | None = Field(
        default=None,
    )
    """Ad id."""

    top_union_id: int | None = Field(
        default=None,
    )
    """Top union id."""


class AdsPostLikes(BaseModel):
    """Likes
    Model: `AdsPostLikes`
    """

    can_like: int | None = Field(
        default=None,
    )
    """Can like."""

    count: int | None = Field(
        default=None,
    )
    """Count."""

    user_likes: int | None = Field(
        default=None,
    )
    """User likes."""


class AdsPostOwner(BaseModel):
    """Owner
    Model: `AdsPostOwner`
    """

    id: int | None = Field(
        default=None,
    )
    """Owner id."""

    name: str | None = Field(
        default=None,
    )
    """Name."""

    photo: str | None = Field(
        default=None,
    )
    """Photo url."""

    url: str | None = Field(
        default=None,
    )
    """Profile url."""


class AdsPostReposts(BaseModel):
    """Reposts
    Model: `AdsPostReposts`
    """

    count: int | None = Field(
        default=None,
    )
    """Count."""

    wall_count: int | None = Field(
        default=None,
    )
    """Wall count."""

    mail_count: int | None = Field(
        default=None,
    )
    """Mail count."""


class AdsPostViews(BaseModel):
    """Views
    Model: `AdsPostViews`
    """

    count: int | None = Field(
        default=None,
    )
    """Count."""


class AdsPromotedPostReach(BaseModel):
    """Model: `AdsPromotedPostReach`"""

    hide: int = Field()
    """Hides amount."""

    id: int = Field()
    """Object ID from \'ids\' parameter."""

    join_group: int = Field()
    """Community joins."""

    links: int = Field()
    """Link clicks."""

    reach_subscribers: int = Field()
    """Subscribers reach."""

    reach_total: int = Field()
    """Total reach."""

    report: int = Field()
    """Reports amount."""

    to_group: int = Field()
    """Community clicks."""

    unsubscribe: int = Field()
    """\'Unsubscribe\' events amount."""

    video_views_100p: int | None = Field(
        default=None,
    )
    """Video views for 100 percent."""

    video_views_25p: int | None = Field(
        default=None,
    )
    """Video views for 25 percent."""

    video_views_3s: int | None = Field(
        default=None,
    )
    """Video views for 3 seconds."""

    video_views_10s: int | None = Field(
        default=None,
    )
    """Video views for 10 seconds."""

    video_views_50p: int | None = Field(
        default=None,
    )
    """Video views for 50 percent."""

    video_views_75p: int | None = Field(
        default=None,
    )
    """Video views for 75 percent."""

    video_views_start: int | None = Field(
        default=None,
    )
    """Video starts."""

    pretty_cards_clicks: int | None = Field(
        default=None,
    )
    """Pretty cards clicks."""


class AdsRejectReason(BaseModel):
    """Model: `AdsRejectReason`"""

    comment: str | None = Field(
        default=None,
    )
    """Comment text."""

    rules: list["AdsRules"] | None = Field(
        default=None,
    )
    """Property `AdsRejectReason.rules`."""


class AdsRules(BaseModel):
    """Model: `AdsRules`"""

    help_url: str | bool | None = Field(
        default=None,
    )
    """Help url."""

    help_label: str | None = Field(
        default=None,
    )
    """Label."""

    content_html: str | None = Field(
        default=None,
    )
    """Content Html."""

    help_chat: bool | None = Field(
        default=None,
    )
    """Help chat."""


class AdsStatisticClickActionType(StrEnum, metaclass=BaseEnumMeta):
    LOAD = "load"
    IMPRESSION = "impression"
    CLICK_DEEPLINK = "click_deeplink"
    CLICK = "click"
    CLICK_POST_OWNER = "click_post_owner"
    CLICK_POST_LINK = "click_post_link"
    CLICK_PRETTY_CARD = "click_pretty_card"
    LIKE_POST = "like_post"
    SHARE_POST = "share_post"
    VIDEO_START = "video_start"
    VIDEO_PAUSE = "video_pause"
    VIDEO_RESUME = "video_resume"
    VIDEO_PLAY_3S = "video_play_3s"
    VIDEO_PLAY_10S = "video_play_10s"
    VIDEO_PLAY_25 = "video_play_25"
    VIDEO_PLAY_50 = "video_play_50"
    VIDEO_PLAY_75 = "video_play_75"
    VIDEO_PLAY_95 = "video_play_95"
    VIDEO_PLAY_100 = "video_play_100"
    VIDEO_VOLUME_ON = "video_volume_on"
    VIDEO_VOLUME_OFF = "video_volume_off"
    VIDEO_FULLSCREEN_ON = "video_fullscreen_on"
    VIDEO_FULLSCREEN_OFF = "video_fullscreen_off"
    HIDE = "hide"


class AdsStatisticClickAction(BaseModel):
    """Model: `AdsStatisticClickAction`"""

    type: "AdsStatisticClickActionType | None" = Field(
        default=None,
    )
    """Property `AdsStatisticClickAction.type`."""

    url: str | None = Field(
        default=None,
    )
    """Property `AdsStatisticClickAction.url`."""


class AdsStats(BaseModel):
    """Model: `AdsStats`"""

    id: int | None = Field(
        default=None,
    )
    """Object ID."""

    stats: list["AdsStatsFormat"] | None = Field(
        default=None,
    )
    """Property `AdsStats.stats`."""

    type: "AdsObjectType | None" = Field(
        default=None,
    )
    """Property `AdsStats.type`."""

    views_times: "AdsStatsViewsTimes | None" = Field(
        default=None,
    )
    """Property `AdsStats.views_times`."""


class AdsStatsFormat(BaseModel):
    """Model: `AdsStatsFormat`"""

    clicks: int | None = Field(
        default=None,
    )
    """Clicks number."""

    link_external_clicks: int | None = Field(
        default=None,
    )
    """External clicks number."""

    day: str | None = Field(
        default=None,
    )
    """Day as YYYY-MM-DD."""

    impressions: int | None = Field(
        default=None,
    )
    """Impressions number."""

    join_rate: int | None = Field(
        default=None,
    )
    """Events number."""

    month: str | None = Field(
        default=None,
    )
    """Month as YYYY-MM."""

    year: int | None = Field(
        default=None,
    )
    """Year as YYYY."""

    overall: int | None = Field(
        default=None,
    )
    """1 if period=overall."""

    reach: int | None = Field(
        default=None,
    )
    """Reach ."""

    spent: str | None = Field(
        default=None,
    )
    """Spent funds."""

    video_plays_unique_started: int | None = Field(
        default=None,
    )
    """Video plays unique started count."""

    video_plays_unique_3_seconds: int | None = Field(
        default=None,
    )
    """Video plays unique 3 seconds count."""

    video_plays_unique_10_seconds: int | None = Field(
        default=None,
    )
    """Video plays unique 10 seconds count."""

    video_plays_unique_25_percents: int | None = Field(
        default=None,
    )
    """Video plays unique 25 percents count."""

    video_plays_unique_50_percents: int | None = Field(
        default=None,
    )
    """Video plays unique 50 percents count."""

    video_plays_unique_75_percents: int | None = Field(
        default=None,
    )
    """Video plays unique 75 percents count."""

    video_plays_unique_100_percents: int | None = Field(
        default=None,
    )
    """Video plays unique 100 percents count."""

    effective_cost_per_click: str | None = Field(
        default=None,
    )
    """Effective cost per click."""

    effective_cost_per_mille: str | None = Field(
        default=None,
    )
    """Effective cost per mille."""

    effective_cpf: str | None = Field(
        default=None,
    )
    """Effective cpf."""

    effective_cost_per_message: str | None = Field(
        default=None,
    )
    """Effective cost per message."""

    message_sends: int | None = Field(
        default=None,
    )
    """Message sends count."""

    message_sends_by_any_user: int | None = Field(
        default=None,
    )
    """Message sends by anu user."""

    conversions_external: int | None = Field(
        default=None,
    )
    """Conversions external."""

    conversion_count: int | None = Field(
        default=None,
    )
    """Conversions count."""

    conversion_cr: str | None = Field(
        default=None,
    )
    """Conversions CR."""

    day_from: str | None = Field(
        default=None,
    )
    """Day from."""

    day_to: str | None = Field(
        default=None,
    )
    """Day to."""

    ctr: str | None = Field(
        default=None,
    )
    """Ctr."""

    uniq_views_count: int | None = Field(
        default=None,
    )
    """Unique views count."""

    mobile_app_stat: list["AdsMobileStatItem"] | None = Field(
        default=None,
    )
    """Mobile app stat."""


class AdsStatsSexValue(StrEnum, metaclass=BaseEnumMeta):
    F = "f"
    M = "m"


class AdsStatsViewsTimes(BaseModel):
    """Model: `AdsStatsViewsTimes`"""

    views_ads_times_1: int | None = Field(
        default=None,
    )
    """Property `AdsStatsViewsTimes.views_ads_times_1`."""

    views_ads_times_2: int | None = Field(
        default=None,
    )
    """Property `AdsStatsViewsTimes.views_ads_times_2`."""

    views_ads_times_3: int | None = Field(
        default=None,
    )
    """Property `AdsStatsViewsTimes.views_ads_times_3`."""

    views_ads_times_4: int | None = Field(
        default=None,
    )
    """Property `AdsStatsViewsTimes.views_ads_times_4`."""

    views_ads_times_5: str | None = Field(
        default=None,
    )
    """Property `AdsStatsViewsTimes.views_ads_times_5`."""

    views_ads_times_6: int | None = Field(
        default=None,
    )
    """Property `AdsStatsViewsTimes.views_ads_times_6`."""

    views_ads_times_7: int | None = Field(
        default=None,
    )
    """Property `AdsStatsViewsTimes.views_ads_times_7`."""

    views_ads_times_8: int | None = Field(
        default=None,
    )
    """Property `AdsStatsViewsTimes.views_ads_times_8`."""

    views_ads_times_9: int | None = Field(
        default=None,
    )
    """Property `AdsStatsViewsTimes.views_ads_times_9`."""

    views_ads_times_10: int | None = Field(
        default=None,
    )
    """Property `AdsStatsViewsTimes.views_ads_times_10`."""

    views_ads_times_11_plus: int | None = Field(
        default=None,
    )
    """Property `AdsStatsViewsTimes.views_ads_times_11_plus`."""


class AdsStories(BaseModel):
    """Model: `AdsStories`"""

    stories: list["AdsStoryItem"] | None = Field(
        default=None,
    )
    """Property `AdsStories.stories`."""

    owner: "AdsStoriesOwner | None" = Field(
        default=None,
    )
    """Property `AdsStories.owner`."""

    stories_disclaimers_text: str | None = Field(
        default=None,
    )
    """Stories disclaimers text."""


class AdsStoriesOwner(BaseModel):
    """Model: `AdsStoriesOwner`"""

    id: int | bool | None = Field(
        default=None,
    )
    """Owner id."""

    href: str | None = Field(
        default=None,
    )
    """Href."""

    name: str | None = Field(
        default=None,
    )
    """Name."""

    photo: str | None = Field(
        default=None,
    )
    """Photo."""

    verify: str | None = Field(
        default=None,
    )
    """Verify."""

    gender: str | None = Field(
        default=None,
    )
    """Gender."""

    name_get: str | None = Field(
        default=None,
    )
    """Name get."""

    first_name: str | None = Field(
        default=None,
        alias="firstName",
    )
    """First name."""

    first_name_gen: str | None = Field(
        default=None,
    )
    """First name gen."""

    first_name_ins: str | None = Field(
        default=None,
    )
    """First name ins."""

    can_follow: bool | None = Field(
        default=None,
    )
    """Can follow."""


class AdsStoryItem(BaseModel):
    """Model: `AdsStoryItem`"""

    id: int | None = Field(
        default=None,
    )
    """Story id."""

    owner_id: int | None = Field(
        default=None,
    )
    """Owner id."""

    raw_id: str | None = Field(
        default=None,
    )
    """Story raw id."""

    date: str | None = Field(
        default=None,
    )
    """Date."""

    time: int | None = Field(
        default=None,
    )
    """Time."""

    type: str | None = Field(
        default=None,
    )
    """Type."""

    unread: bool | None = Field(
        default=None,
    )
    """Is unread."""

    can_like: bool | None = Field(
        default=None,
        alias="canLike",
    )
    """Can like."""

    can_comment: bool | None = Field(
        default=None,
    )
    """Can comment."""

    can_share: bool | None = Field(
        default=None,
    )
    """Can share."""

    can_remove: bool | None = Field(
        default=None,
    )
    """Can remove."""

    can_manage: bool | None = Field(
        default=None,
    )
    """Can manage."""

    can_ask: bool | None = Field(
        default=None,
    )
    """Can ask."""

    can_ask_anonymous: bool | None = Field(
        default=None,
    )
    """Can ask anonymous."""

    is_profile_question: bool | None = Field(
        default=None,
        alias="isProfileQuestion",
    )
    """Is profile question."""

    stats: "AdsStoryItemStats | None" = Field(
        default=None,
    )
    """Property `AdsStoryItem.stats`."""

    link: "AdsStoryItemLink | None" = Field(
        default=None,
    )
    """Property `AdsStoryItem.link`."""

    photo_url: str | None = Field(
        default=None,
    )
    """Photo url."""

    preview_url: str | None = Field(
        default=None,
    )
    """Preview url."""

    track_code: str | None = Field(
        default=None,
    )
    """Track code."""

    is_part_of_narrative: bool | None = Field(
        default=None,
        alias="isPartOfNarrative",
    )
    """Is part of narrative."""

    is_ads: bool | None = Field(
        default=None,
        alias="isAds",
    )
    """Is ads."""

    video_url: str | None = Field(
        default=None,
    )
    """Video url."""

    first_frame: str | None = Field(
        default=None,
    )
    """First frame."""

    small_preview: str | None = Field(
        default=None,
    )
    """Small preview."""

    is_liked: bool | None = Field(
        default=None,
        alias="isLiked",
    )
    """Is liked."""


class AdsStoryItemLink(BaseModel):
    """Model: `AdsStoryItemLink`"""

    key: str | None = Field(
        default=None,
    )
    """Key."""

    text: str | None = Field(
        default=None,
    )
    """Text."""

    url: str | None = Field(
        default=None,
    )
    """Url."""

    raw_url: str | None = Field(
        default=None,
    )
    """Raw url."""


class AdsStoryItemStats(BaseModel):
    """Model: `AdsStoryItemStats`"""

    follow: "AdsStoryItemStatsFollow | None" = Field(
        default=None,
    )
    """Property `AdsStoryItemStats.follow`."""

    url_view: "AdsStoryItemStatsUrlView | None" = Field(
        default=None,
    )
    """Property `AdsStoryItemStats.url_view`."""


class AdsStoryItemStatsFollow(BaseModel):
    """Follow event stats
    Model: `AdsStoryItemStatsFollow`
    """

    event_type: str | None = Field(
        default=None,
    )
    """Event type."""

    rhash: str | None = Field(
        default=None,
    )
    """Event hash."""


class AdsStoryItemStatsUrlView(BaseModel):
    """Url view event stats
    Model: `AdsStoryItemStatsUrlView`
    """

    event_type: str | None = Field(
        default=None,
    )
    """Event type."""

    rhash: str | None = Field(
        default=None,
    )
    """Event hash."""


class AdsTargStats(BaseModel):
    """Model: `AdsTargStats`"""

    audience_count: int = Field()
    """Audience."""

    recommended_cpc: str | None = Field(
        default=None,
    )
    """Recommended CPC value for 50% reach (old format)."""

    recommended_cpm: str | None = Field(
        default=None,
    )
    """Recommended CPM value for 50% reach (old format)."""

    recommended_cpc_50: str | None = Field(
        default=None,
    )
    """Recommended CPC value for 50% reach."""

    recommended_cpm_50: str | None = Field(
        default=None,
    )
    """Recommended CPM value for 50% reach."""

    recommended_cpc_70: str | None = Field(
        default=None,
    )
    """Recommended CPC value for 70% reach."""

    recommended_cpm_70: str | None = Field(
        default=None,
    )
    """Recommended CPM value for 70% reach."""

    recommended_cpc_90: str | None = Field(
        default=None,
    )
    """Recommended CPC value for 90% reach."""

    recommended_cpm_90: str | None = Field(
        default=None,
    )
    """Recommended CPM value for 90% reach."""

    total_alive_audience: int | None = Field(
        default=None,
    )
    """Total alive audience."""


class AdsTargSuggestions(BaseModel):
    """Model: `AdsTargSuggestions`"""

    id: int | None = Field(
        default=None,
    )
    """Object ID."""

    name: str | None = Field(
        default=None,
    )
    """Object name."""

    type: str | None = Field(
        default=None,
    )
    """Object type."""

    parent: str | None = Field(
        default=None,
    )
    """Parent."""


class AdsTargSuggestionsCities(BaseModel):
    """Model: `AdsTargSuggestionsCities`"""

    id: int | None = Field(
        default=None,
    )
    """Object ID."""

    name: str | None = Field(
        default=None,
    )
    """Object name."""

    parent: str | None = Field(
        default=None,
    )
    """Parent object."""


class AdsTargSuggestionsRegions(BaseModel):
    """Model: `AdsTargSuggestionsRegions`"""

    id: int | None = Field(
        default=None,
    )
    """Object ID."""

    name: str | None = Field(
        default=None,
    )
    """Object name."""

    type: str | None = Field(
        default=None,
    )
    """Object type."""


class AdsTargSuggestionsSchools(BaseModel):
    """Model: `AdsTargSuggestionsSchools`"""

    desc: str | None = Field(
        default=None,
    )
    """Full school title."""

    id: int | None = Field(
        default=None,
    )
    """School ID."""

    name: str | None = Field(
        default=None,
    )
    """School title."""

    parent: str | None = Field(
        default=None,
    )
    """City name."""

    type: "AdsTargSuggestionsSchoolsType | None" = Field(
        default=None,
    )
    """Property `AdsTargSuggestionsSchools.type`."""


class AdsTargSuggestionsSchoolsType(StrEnum, metaclass=BaseEnumMeta):
    SCHOOL = "school"
    UNIVERSITY = "university"
    FACULTY = "faculty"
    CHAIR = "chair"


class AdsTargetGroup(BaseModel):
    """Model: `AdsTargetGroup`"""

    id: int | None = Field(
        default=None,
    )
    """Group ID."""

    name: str | None = Field(
        default=None,
    )
    """Group name."""

    is_audience: bool | None = Field(
        default=None,
    )
    """Is audience."""

    is_shared: bool | None = Field(
        default=None,
    )
    """Is shared."""

    file_source: bool | None = Field(
        default=None,
    )
    """File source."""

    api_source: bool | None = Field(
        default=None,
    )
    """API source."""

    lookalike_source: bool | None = Field(
        default=None,
    )
    """File source."""

    audience_count: int | None = Field(
        default=None,
    )
    """Audience."""

    domain: str | None = Field(
        default=None,
    )
    """Site domain."""

    lifetime: int | None = Field(
        default=None,
    )
    """Number of days for user to be in group."""

    pixel: str | None = Field(
        default=None,
    )
    """Pixel code."""

    target_pixel_id: int | None = Field(
        default=None,
    )
    """Target Pixel id."""

    target_pixel_rules: list["AdsTargetGroupTargetPixelRule"] | None = Field(
        default=None,
    )
    """Target Pixel rules."""

    last_updated: int | None = Field(
        default=None,
    )
    """Last updated."""


class AdsTargetGroupTargetPixelRule(BaseModel):
    """Model: `AdsTargetGroupTargetPixelRule`"""

    url_full_match: str | None = Field(
        default=None,
    )
    """Property `AdsTargetGroupTargetPixelRule.url_full_match`."""

    event_full_match: str | None = Field(
        default=None,
    )
    """Property `AdsTargetGroupTargetPixelRule.event_full_match`."""

    url_substrings_match: list[str] | None = Field(
        default=None,
    )
    """Property `AdsTargetGroupTargetPixelRule.url_substrings_match`."""

    event_substrings_match: list[str] | None = Field(
        default=None,
    )
    """Property `AdsTargetGroupTargetPixelRule.event_substrings_match`."""

    url_regex_match: str | None = Field(
        default=None,
    )
    """Property `AdsTargetGroupTargetPixelRule.url_regex_match`."""

    event_regex_match: str | None = Field(
        default=None,
    )
    """Property `AdsTargetGroupTargetPixelRule.event_regex_match`."""


class AdsTargetPixelInfo(BaseModel):
    """Model: `AdsTargetPixelInfo`"""

    target_pixel_id: int = Field()
    """Property `AdsTargetPixelInfo.target_pixel_id`."""

    name: str = Field()
    """Property `AdsTargetPixelInfo.name`."""

    domain: str = Field()
    """Property `AdsTargetPixelInfo.domain`."""

    category_id: int = Field()
    """Property `AdsTargetPixelInfo.category_id`."""

    last_updated: int = Field()
    """Property `AdsTargetPixelInfo.last_updated`."""

    pixel: str = Field()
    """Property `AdsTargetPixelInfo.pixel`."""


class AdsUpdateOfficeUsersResult(BaseModel):
    """Model: `AdsUpdateOfficeUsersResult`"""

    user_id: int = Field()
    """Property `AdsUpdateOfficeUsersResult.user_id`."""

    is_success: bool = Field()
    """Property `AdsUpdateOfficeUsersResult.is_success`."""

    error: "BaseError | None" = Field(
        default=None,
    )
    """Property `AdsUpdateOfficeUsersResult.error`."""


class AdsUpdateAdsStatus(BaseModel):
    """Model: `AdsUpdateAdsStatus`"""

    id: int = Field()
    """Ad ID."""

    error_code: int | None = Field(
        default=None,
    )
    """Error code."""

    error_desc: str | None = Field(
        default=None,
    )
    """Error description."""


class AdsUpdateClientsStatus(BaseModel):
    """Model: `AdsUpdateClientsStatus`"""

    id: int = Field()
    """Client ID."""

    error_code: int | None = Field(
        default=None,
    )
    """Error code."""

    error_desc: str | None = Field(
        default=None,
    )
    """Error description."""


class AdsUserSpecification(BaseModel):
    """Model: `AdsUserSpecification`"""

    user_id: int = Field()
    """Property `AdsUserSpecification.user_id`."""

    role: "AdsAccessRolePublic" = Field()
    """Property `AdsUserSpecification.role`."""

    grant_access_to_all_clients: bool | None = Field(
        default=None,
    )
    """Property `AdsUserSpecification.grant_access_to_all_clients`."""

    client_ids: list[int] | None = Field(
        default=None,
    )
    """Property `AdsUserSpecification.client_ids`."""

    view_budget: bool | None = Field(
        default=None,
    )
    """Property `AdsUserSpecification.view_budget`."""


class AdsUserSpecificationCutted(BaseModel):
    """Model: `AdsUserSpecificationCutted`"""

    user_id: int = Field()
    """Property `AdsUserSpecificationCutted.user_id`."""

    role: "AdsAccessRolePublic" = Field()
    """Property `AdsUserSpecificationCutted.role`."""

    client_id: int | None = Field(
        default=None,
    )
    """Property `AdsUserSpecificationCutted.client_id`."""

    view_budget: bool | None = Field(
        default=None,
    )
    """Property `AdsUserSpecificationCutted.view_budget`."""


class AdsUsers(BaseModel):
    """Model: `AdsUsers`"""

    accesses: list["AdsAccesses"] = Field()
    """Property `AdsUsers.accesses`."""

    user_id: int = Field()
    """User ID."""


class AppWidgetsPhoto(BaseModel):
    """Model: `AppWidgetsPhoto`"""

    id: str = Field()
    """Image ID."""

    images: list["BaseImage"] = Field()
    """Property `AppWidgetsPhoto.images`."""


class AppWidgetsPhotos(BaseModel):
    """Model: `AppWidgetsPhotos`"""

    count: int | None = Field(
        default=None,
    )
    """Property `AppWidgetsPhotos.count`."""

    items: list["AppWidgetsPhoto"] | None = Field(
        default=None,
    )
    """Property `AppWidgetsPhotos.items`."""


class AppsAppFields(StrEnum, metaclass=BaseEnumMeta):
    AUTHOR_GROUP = "author_group"
    AUTHOR_ID = "author_id"
    AUTHOR_URL = "author_url"
    BANNER_1120 = "banner_1120"
    BANNER_560 = "banner_560"
    BANNER_186 = "banner_186"
    BANNER_896 = "banner_896"
    ICON_16 = "icon_16"
    ICON_25 = "icon_25"
    ICON_50 = "icon_50"
    ICON_100 = "icon_100"
    ICON_200 = "icon_200"
    ICON_128 = "icon_128"
    ICON_256 = "icon_256"
    IS_NEW = "is_new"
    NEW = "new"
    IS_HTML5_APP = "is_html5_app"
    PUSH_ENABLED = "push_enabled"
    CATALOG_BANNER = "catalog_banner"
    FRIENDS = "friends"
    CATALOG_POSITION = "catalog_position"
    DESCRIPTION = "description"
    GENRE = "genre"
    GENRE_ID = "genre_id"
    INTERNATIONAL = "international"
    IS_IN_CATALOG = "is_in_catalog"
    INSTALLED = "installed"
    LEADERBOARD_TYPE = "leaderboard_type"
    MEMBERS_COUNT = "members_count"
    PLATFORM_ID = "platform_id"
    PUBLISHED_DATE = "published_date"
    SCREEN_NAME = "screen_name"
    SECTION = "section"
    TYPE = "type"
    ID = "id"
    TITLE = "title"
    AUTHOR_OWNER_ID = "author_owner_id"
    IS_INSTALLED = "is_installed"
    ICON_139 = "icon_139"
    ICON_150 = "icon_150"
    ICON_278 = "icon_278"
    ICON_576 = "icon_576"
    BACKGROUND_LOADER_COLOR = "background_loader_color"
    LOADER_ICON = "loader_icon"
    ICON_75 = "icon_75"
    OPEN_IN_EXTERNAL_BROWSER = "open_in_external_browser"
    AD_CONFIG = "ad_config"
    SCREEN_ORIENTATION = "screen_orientation"


class AppsAppLeaderboardType(IntEnum, metaclass=BaseEnumMeta):
    NOT_SUPPORTED = 0
    LEVELS = 1
    POINTS = 2


class AppsAppMin(BaseModel):
    """Model: `AppsAppMin`"""

    type: "AppsAppType" = Field()
    """Property `AppsAppMin.type`."""

    id: int = Field()
    """Application ID."""

    title: str = Field()
    """Application title."""

    author_owner_id: int | None = Field(
        default=None,
    )
    """Application author\'s ID."""

    is_installed: bool | None = Field(
        default=None,
    )
    """Is application installed."""

    icon_139: str | None = Field(
        default=None,
    )
    """URL of the app icon with 139 px in width."""

    icon_150: str | None = Field(
        default=None,
    )
    """URL of the app icon with 150 px in width."""

    icon_278: str | None = Field(
        default=None,
    )
    """URL of the app icon with 278 px in width."""

    icon_576: str | None = Field(
        default=None,
    )
    """URL of the app icon with 576 px in width."""

    background_loader_color: str | None = Field(
        default=None,
    )
    """Hex color code without hash sign."""

    loader_icon: str | None = Field(
        default=None,
    )
    """SVG data."""

    icon_75: str | None = Field(
        default=None,
    )
    """URL of the app icon with 75 px in width."""

    screen_orientation: int | None = Field(
        default=None,
    )
    """Screen orientation."""


class AppsAppType(StrEnum, metaclass=BaseEnumMeta):
    APP = "app"
    GAME = "game"
    SITE = "site"
    STANDALONE = "standalone"
    VK_APP = "vk_app"
    COMMUNITY_APP = "community_app"
    HTML5_GAME = "html5_game"
    MINI_APP = "mini_app"


class AppsCatalogList(BaseModel):
    """Model: `AppsCatalogList`"""

    count: int = Field()
    """Total number."""

    items: list["AppsApp"] = Field()
    """Property `AppsCatalogList.items`."""

    profiles: list["UsersUserMin"] | None = Field(
        default=None,
    )
    """Property `AppsCatalogList.profiles`."""


class AppsCustomSnippetButton(StrEnum, metaclass=BaseEnumMeta):
    BUY = "buy"
    BUY_TICKET = "buy_ticket"
    CONTACT = "contact"
    CREATE = "create"
    ENROLL = "enroll"
    FILL = "fill"
    GO = "go"
    OPEN = "open"
    PLAY = "play"


class AppsCustomSnippet(BaseModel):
    """Model: `AppsCustomSnippet`"""

    vk_ref: list[typing.Literal["snippet_im", "snippet_post"]] | None = Field(
        default=None,
    )
    """Property `AppsCustomSnippet.vk_ref`."""

    group_id: list[int] | None = Field(
        default=None,
    )
    """Property `AppsCustomSnippet.group_id`."""

    hash: list[str] | None = Field(
        default=None,
    )
    """Property `AppsCustomSnippet.hash`."""

    snippet_id: int | None = Field(
        default=None,
    )
    """Property `AppsCustomSnippet.snippet_id`."""

    title: str | None = Field(
        default=None,
    )
    """Property `AppsCustomSnippet.title`."""

    description: str | None = Field(
        default=None,
    )
    """Property `AppsCustomSnippet.description`."""

    expired_at: int | None = Field(
        default=None,
    )
    """Property `AppsCustomSnippet.expired_at`."""

    image_url: str | None = Field(
        default=None,
    )
    """Property `AppsCustomSnippet.image_url`."""

    small_image_url: str | None = Field(
        default=None,
    )
    """Property `AppsCustomSnippet.small_image_url`."""

    button: "AppsCustomSnippetButton | None" = Field(
        default=None,
    )
    """Property `AppsCustomSnippet.button`."""


class AppsLeaderboard(BaseModel):
    """Model: `AppsLeaderboard`"""

    user_id: int = Field()
    """User ID."""

    level: int | None = Field(
        default=None,
    )
    """Level."""

    points: int | None = Field(
        default=None,
    )
    """Points number."""

    score: int | None = Field(
        default=None,
    )
    """Score number."""


class AppsScopeName(StrEnum, metaclass=BaseEnumMeta):
    FRIENDS = "friends"
    PHOTOS = "photos"
    VIDEO = "video"
    PAGES = "pages"
    STATUS = "status"
    NOTES = "notes"
    WALL = "wall"
    DOCS = "docs"
    GROUPS = "groups"
    STATS = "stats"
    MARKET = "market"
    STORIES = "stories"
    APP_WIDGET = "app_widget"
    MESSAGES = "messages"
    MANAGE = "manage"
    NOTIFY = "notify"
    AUDIO = "audio"
    SUPPORT = "support"
    MENU = "menu"
    WALLMENU = "wallmenu"
    ADS = "ads"
    OFFLINE = "offline"
    NOTIFICATIONS = "notifications"
    EMAIL = "email"
    ADSWEB = "adsweb"
    LEADS = "leads"
    GROUP_MESSAGES = "group_messages"
    EXCHANGE = "exchange"
    PHONE = "phone"


class AppsScope(BaseModel):
    """Scope description
    Model: `AppsScope`
    """

    name: "AppsScopeName" = Field()
    """Scope name."""

    title: str | None = Field(
        default=None,
    )
    """Scope title."""


class AppsTestingGroup(BaseModel):
    """Model: `AppsTestingGroup`"""

    user_ids: list[int] = Field()
    """Property `AppsTestingGroup.user_ids`."""

    group_id: int = Field()
    """Property `AppsTestingGroup.group_id`."""

    name: str | None = Field(
        default=None,
    )
    """Property `AppsTestingGroup.name`."""

    webview: str | None = Field(
        default=None,
    )
    """Property `AppsTestingGroup.webview`."""

    platforms: list[typing.Literal["mobile", "web", "mvk"]] | None = Field(
        default=None,
    )
    """Property `AppsTestingGroup.platforms`."""


class AudioAudio(BaseModel):
    """Model: `AudioAudio`"""

    artist: str = Field()
    """Artist name."""

    id: int = Field()
    """Audio ID."""

    owner_id: int = Field()
    """Audio owner\'s ID."""

    title: str = Field()
    """Title."""

    duration: int = Field()
    """Duration in seconds."""

    access_key: str | None = Field(
        default=None,
    )
    """Access key for the audio."""

    url: str | None = Field(
        default=None,
    )
    """URL of mp3 file."""

    stream_duration: int | None = Field(
        default=None,
    )
    """Stream duration in seconds."""

    date: datetime.datetime | None = Field(
        default=None,
    )
    """Date when uploaded."""

    album_id: int | None = Field(
        default=None,
    )
    """Album ID."""

    performer: str | None = Field(
        default=None,
    )
    """Performer name."""

    file_size: int | None = Field(
        default=None,
    )
    """Примерный объем памяти занимаемый аудио на устройстве. Реализовано только для эпизодов подкастов."""


class BoardDefaultOrder(IntEnum, metaclass=BaseEnumMeta):
    DESC_UPDATED = 1
    DESC_CREATED = 2
    ASC_UPDATED = -1
    ASC_CREATED = -2


class BoardTopic(BaseModel):
    """Model: `BoardTopic`"""

    comments: int | None = Field(
        default=None,
    )
    """Comments number."""

    created: int | None = Field(
        default=None,
    )
    """Date when the topic has been created in Unixtime."""

    created_by: int | None = Field(
        default=None,
    )
    """Creator ID."""

    id: int | None = Field(
        default=None,
    )
    """Topic ID."""

    is_closed: bool | None = Field(
        default=None,
    )
    """Information whether the topic is closed."""

    is_fixed: bool | None = Field(
        default=None,
    )
    """Information whether the topic is fixed."""

    title: str | None = Field(
        default=None,
    )
    """Topic title."""

    updated: int | None = Field(
        default=None,
    )
    """Date when the topic has been updated in Unixtime."""

    updated_by: int | None = Field(
        default=None,
    )
    """ID of user who updated the topic."""

    first_comment: str | None = Field(
        default=None,
    )
    """First comment text."""

    last_comment: str | None = Field(
        default=None,
    )
    """Last comment text."""


class BoardTopicComment(BaseModel):
    """Model: `BoardTopicComment`"""

    date: datetime.datetime = Field()
    """Date when the comment has been added in Unixtime."""

    from_id: int = Field()
    """Author ID."""

    id: int = Field()
    """Comment ID."""

    text: str = Field()
    """Comment text."""

    attachments: list["WallCommentAttachment"] | None = Field(
        default=None,
    )
    """Property `BoardTopicComment.attachments`."""

    real_offset: int | None = Field(
        default=None,
    )
    """Real position of the comment."""

    can_edit: bool | None = Field(
        default=None,
    )
    """Information whether current user can edit the comment."""

    likes: "BaseLikesInfo | None" = Field(
        default=None,
    )
    """Property `BoardTopicComment.likes`."""


class BugtrackerAddCompanyGroupsMembersError(BaseModel):
    """Model: `BugtrackerAddCompanyGroupsMembersError`"""

    group_id: int = Field()
    """Property `BugtrackerAddCompanyGroupsMembersError.group_id`."""

    user_id: int = Field()
    """Property `BugtrackerAddCompanyGroupsMembersError.user_id`."""


class BugtrackerAttachmentType(StrEnum, metaclass=BaseEnumMeta):
    PHOTO = "photo"
    DOC = "doc"


class BugtrackerAttachment(BaseModel):
    """Model: `BugtrackerAttachment`"""

    type: "BugtrackerAttachmentType" = Field()
    """Property `BugtrackerAttachment.type`."""

    doc: "DocsDoc | None" = Field(
        default=None,
    )
    """Property `BugtrackerAttachment.doc`."""

    photo: "PhotosPhoto | None" = Field(
        default=None,
    )
    """Property `BugtrackerAttachment.photo`."""


class BugtrackerBugreport(BaseModel):
    """Model: `BugtrackerBugreport`"""

    id: int = Field()
    """Property `BugtrackerBugreport.id`."""

    title: str = Field()
    """Property `BugtrackerBugreport.title`."""

    owner_id: int = Field()
    """Property `BugtrackerBugreport.owner_id`."""

    created: int = Field()
    """Property `BugtrackerBugreport.created`."""

    updated: int = Field()
    """Property `BugtrackerBugreport.updated`."""

    company_id: int = Field()
    """Property `BugtrackerBugreport.company_id`."""

    original_id: int | None = Field(
        default=None,
    )
    """Property `BugtrackerBugreport.original_id`."""

    clones_count: int | None = Field(
        default=None,
    )
    """Property `BugtrackerBugreport.clones_count`."""

    description: str | None = Field(
        default=None,
    )
    """Property `BugtrackerBugreport.description`."""

    state_actual: str | None = Field(
        default=None,
    )
    """Property `BugtrackerBugreport.state_actual`."""

    state_supposed: str | None = Field(
        default=None,
    )
    """Property `BugtrackerBugreport.state_supposed`."""

    phone: str | None = Field(
        default=None,
    )
    """Property `BugtrackerBugreport.phone`."""

    comments_count: int | None = Field(
        default=None,
    )
    """Property `BugtrackerBugreport.comments_count`."""

    can_remove: bool | None = Field(
        default=None,
    )
    """Property `BugtrackerBugreport.can_remove`."""

    can_change_status: bool | None = Field(
        default=None,
    )
    """Property `BugtrackerBugreport.can_change_status`."""

    can_bookmark: bool | None = Field(
        default=None,
    )
    """Property `BugtrackerBugreport.can_bookmark`."""

    is_bookmarked: bool | None = Field(
        default=None,
    )
    """Property `BugtrackerBugreport.is_bookmarked`."""

    can_edit: bool | None = Field(
        default=None,
    )
    """Property `BugtrackerBugreport.can_edit`."""

    can_export_to_trackers: bool | None = Field(
        default=None,
    )
    """Property `BugtrackerBugreport.can_export_to_trackers`."""

    can_export_to_csv: bool | None = Field(
        default=None,
    )
    """Property `BugtrackerBugreport.can_export_to_csv`."""

    can_add_moder_comment: bool | None = Field(
        default=None,
    )
    """Property `BugtrackerBugreport.can_add_moder_comment`."""

    can_add_hidden_comment: bool | None = Field(
        default=None,
    )
    """Property `BugtrackerBugreport.can_add_hidden_comment`."""

    can_view_history: bool | None = Field(
        default=None,
    )
    """Property `BugtrackerBugreport.can_view_history`."""

    is_deleted: bool | None = Field(
        default=None,
    )
    """Property `BugtrackerBugreport.is_deleted`."""

    can_restore: bool | None = Field(
        default=None,
    )
    """Property `BugtrackerBugreport.can_restore`."""

    is_vulnerability: bool | None = Field(
        default=None,
    )
    """Property `BugtrackerBugreport.is_vulnerability`."""

    is_severity_by_moderator: bool | None = Field(
        default=None,
    )
    """Property `BugtrackerBugreport.is_severity_by_moderator`."""

    hidden_docs: bool | None = Field(
        default=None,
    )
    """Property `BugtrackerBugreport.hidden_docs`."""

    is_confidential: bool | None = Field(
        default=None,
    )
    """Property `BugtrackerBugreport.is_confidential`."""

    private_comment: str | None = Field(
        default=None,
    )
    """Property `BugtrackerBugreport.private_comment`."""

    can_change_product: bool | None = Field(
        default=None,
    )
    """Property `BugtrackerBugreport.can_change_product`."""

    tournament_score: int | None = Field(
        default=None,
    )
    """Property `BugtrackerBugreport.tournament_score`."""

    moderator_user_id: int | None = Field(
        default=None,
    )
    """Property `BugtrackerBugreport.moderator_user_id`."""

    moderated: int | None = Field(
        default=None,
    )
    """Property `BugtrackerBugreport.moderated`."""

    screen_reader: int | None = Field(
        default=None,
    )
    """Property `BugtrackerBugreport.screen_reader`."""

    status_auto_update_ts: int | None = Field(
        default=None,
    )
    """Property `BugtrackerBugreport.status_auto_update_ts`."""

    status_auto_update_reason: int | None = Field(
        default=None,
    )
    """Property `BugtrackerBugreport.status_auto_update_reason`."""

    product_has_wishes: bool | None = Field(
        default=None,
    )
    """Property `BugtrackerBugreport.product_has_wishes`."""


class BugtrackerBugreportSubscribeState(BaseModel):
    """Model: `BugtrackerBugreportSubscribeState`"""

    can_set_subscribe: bool = Field()
    """Property `BugtrackerBugreportSubscribeState.can_set_subscribe`."""

    is_subscribed: bool | None = Field(
        default=None,
    )
    """Property `BugtrackerBugreportSubscribeState.is_subscribed`."""

    set_subscribe_hash: str | None = Field(
        default=None,
    )
    """Property `BugtrackerBugreportSubscribeState.set_subscribe_hash`."""


class BugtrackerComment(BaseModel):
    """Model: `BugtrackerComment`"""

    bugreport_id: int = Field()
    """Property `BugtrackerComment.bugreport_id`."""

    comment_id: int = Field()
    """Property `BugtrackerComment.comment_id`."""

    created: int = Field()
    """Property `BugtrackerComment.created`."""

    text: str = Field()
    """Property `BugtrackerComment.text`."""

    meta_text: str | None = Field(
        default=None,
    )
    """Property `BugtrackerComment.meta_text`."""

    from_id: int | None = Field(
        default=None,
    )
    """Property `BugtrackerComment.from_id`."""

    author_name: str | None = Field(
        default=None,
    )
    """Property `BugtrackerComment.author_name`."""

    author_photo: str | None = Field(
        default=None,
    )
    """Property `BugtrackerComment.author_photo`."""

    can_edit: bool | None = Field(
        default=None,
    )
    """Property `BugtrackerComment.can_edit`."""

    can_remove: bool | None = Field(
        default=None,
    )
    """Property `BugtrackerComment.can_remove`."""

    is_hidden: bool | None = Field(
        default=None,
    )
    """Property `BugtrackerComment.is_hidden`."""

    attachments: list["BugtrackerAttachment"] | None = Field(
        default=None,
    )
    """Property `BugtrackerComment.attachments`."""

    is_unread: bool | None = Field(
        default=None,
    )
    """Property `BugtrackerComment.is_unread`."""

    author: "BugtrackerCommentAuthor | None" = Field(
        default=None,
    )
    """Property `BugtrackerComment.author`."""

    is_attachments_hidden: bool | None = Field(
        default=None,
    )
    """Property `BugtrackerComment.is_attachments_hidden`."""


class BugtrackerCommentAuthor(BaseModel):
    """Model: `BugtrackerCommentAuthor`"""

    author_id: int | None = Field(
        default=None,
    )
    """Property `BugtrackerCommentAuthor.author_id`."""

    name: str | None = Field(
        default=None,
    )
    """Property `BugtrackerCommentAuthor.name`."""

    photo: str | None = Field(
        default=None,
    )
    """Property `BugtrackerCommentAuthor.photo`."""

    moder_name: str | None = Field(
        default=None,
    )
    """Property `BugtrackerCommentAuthor.moder_name`."""

    moder_number: int | None = Field(
        default=None,
    )
    """Property `BugtrackerCommentAuthor.moder_number`."""

    link: str | None = Field(
        default=None,
    )
    """Property `BugtrackerCommentAuthor.link`."""


class BugtrackerCompanyMember(BaseModel):
    """Model: `BugtrackerCompanyMember`"""

    user_id: int = Field()
    """Property `BugtrackerCompanyMember.user_id`."""

    company_id: int = Field()
    """Property `BugtrackerCompanyMember.company_id`."""

    role: int = Field()
    """Property `BugtrackerCompanyMember.role`."""

    role_name: str = Field()
    """Property `BugtrackerCompanyMember.role_name`."""

    ts: int = Field()
    """Property `BugtrackerCompanyMember.ts`."""

    groups_count: int = Field()
    """Property `BugtrackerCompanyMember.groups_count`."""

    products_count: int = Field()
    """Property `BugtrackerCompanyMember.products_count`."""

    reporter_url: str = Field()
    """Property `BugtrackerCompanyMember.reporter_url`."""

    groups: list[int] | None = Field(
        default=None,
    )
    """Property `BugtrackerCompanyMember.groups`."""

    products: list["BugtrackerCompanyMemberProduct"] | None = Field(
        default=None,
    )
    """Property `BugtrackerCompanyMember.products`."""


class BugtrackerCompanyMemberProduct(BaseModel):
    """Model: `BugtrackerCompanyMemberProduct`"""

    id: int = Field()
    """Property `BugtrackerCompanyMemberProduct.id`."""

    access: int = Field()
    """Property `BugtrackerCompanyMemberProduct.access`."""

    status: int = Field()
    """Property `BugtrackerCompanyMemberProduct.status`."""

    title: str | None = Field(
        default=None,
    )
    """Property `BugtrackerCompanyMemberProduct.title`."""

    photo_url: str | None = Field(
        default=None,
    )
    """Property `BugtrackerCompanyMemberProduct.photo_url`."""

    licence_status_text: str | None = Field(
        default=None,
    )
    """Property `BugtrackerCompanyMemberProduct.licence_status_text`."""


class CallbackAppPayload(BaseModel):
    """Model: `CallbackAppPayload`"""

    user_id: int = Field()
    """Property `CallbackAppPayload.user_id`."""

    app_id: int = Field()
    """Property `CallbackAppPayload.app_id`."""

    payload: str = Field()
    """Property `CallbackAppPayload.payload`."""


class CallbackAudioNew(BaseModel):
    """Model: `CallbackAudioNew`"""

    artist: str = Field()
    """Artist name."""

    id: int = Field()
    """Audio ID."""

    owner_id: int = Field()
    """Audio owner\'s ID."""

    title: str = Field()
    """Title."""

    duration: int = Field()
    """Duration in seconds."""

    access_key: str | None = Field(
        default=None,
    )
    """Access key for the audio."""

    url: str | None = Field(
        default=None,
    )
    """URL of mp3 file."""

    stream_duration: int | None = Field(
        default=None,
    )
    """Stream duration in seconds."""

    date: datetime.datetime | None = Field(
        default=None,
    )
    """Date when uploaded."""

    album_id: int | None = Field(
        default=None,
    )
    """Album ID."""

    performer: str | None = Field(
        default=None,
    )
    """Performer name."""

    file_size: int | None = Field(
        default=None,
    )
    """Примерный объем памяти занимаемый аудио на устройстве. Реализовано только для эпизодов подкастов."""


class CallbackBase(BaseModel):
    """Model: `CallbackBase`"""

    type: "CallbackType" = Field()
    """Property `CallbackBase.type`."""

    group_id: int = Field()
    """Property `CallbackBase.group_id`."""

    event_id: str = Field()
    """Unique event id. If it passed twice or more - you should ignore it.."""

    v: str = Field()
    """API object version."""

    secret: str | None = Field(
        default=None,
    )
    """Property `CallbackBase.secret`."""


class CallbackBoardPostDelete(BaseModel):
    """Model: `CallbackBoardPostDelete`"""

    topic_owner_id: int = Field()
    """Property `CallbackBoardPostDelete.topic_owner_id`."""

    topic_id: int = Field()
    """Property `CallbackBoardPostDelete.topic_id`."""

    id: int = Field()
    """Property `CallbackBoardPostDelete.id`."""

    deleter_id: int | None = Field(
        default=None,
    )
    """Property `CallbackBoardPostDelete.deleter_id`."""


class CallbackBoardPostEdit(BaseModel):
    """Model: `CallbackBoardPostEdit`"""

    date: datetime.datetime = Field()
    """Date when the comment has been added in Unixtime."""

    from_id: int = Field()
    """Author ID."""

    id: int = Field()
    """Comment ID."""

    text: str = Field()
    """Comment text."""

    attachments: list["WallCommentAttachment"] | None = Field(
        default=None,
    )
    """Property `CallbackBoardPostEdit.attachments`."""

    real_offset: int | None = Field(
        default=None,
    )
    """Real position of the comment."""

    can_edit: bool | None = Field(
        default=None,
    )
    """Information whether current user can edit the comment."""

    likes: "BaseLikesInfo | None" = Field(
        default=None,
    )
    """Property `CallbackBoardPostEdit.likes`."""


class CallbackBoardPostNew(BaseModel):
    """Model: `CallbackBoardPostNew`"""

    date: datetime.datetime = Field()
    """Date when the comment has been added in Unixtime."""

    from_id: int = Field()
    """Author ID."""

    id: int = Field()
    """Comment ID."""

    text: str = Field()
    """Comment text."""

    attachments: list["WallCommentAttachment"] | None = Field(
        default=None,
    )
    """Property `CallbackBoardPostNew.attachments`."""

    real_offset: int | None = Field(
        default=None,
    )
    """Real position of the comment."""

    can_edit: bool | None = Field(
        default=None,
    )
    """Information whether current user can edit the comment."""

    likes: "BaseLikesInfo | None" = Field(
        default=None,
    )
    """Property `CallbackBoardPostNew.likes`."""


class CallbackBoardPostRestore(BaseModel):
    """Model: `CallbackBoardPostRestore`"""

    date: datetime.datetime = Field()
    """Date when the comment has been added in Unixtime."""

    from_id: int = Field()
    """Author ID."""

    id: int = Field()
    """Comment ID."""

    text: str = Field()
    """Comment text."""

    attachments: list["WallCommentAttachment"] | None = Field(
        default=None,
    )
    """Property `CallbackBoardPostRestore.attachments`."""

    real_offset: int | None = Field(
        default=None,
    )
    """Real position of the comment."""

    can_edit: bool | None = Field(
        default=None,
    )
    """Information whether current user can edit the comment."""

    likes: "BaseLikesInfo | None" = Field(
        default=None,
    )
    """Property `CallbackBoardPostRestore.likes`."""


class CallbackDonutMoneyWithdraw(BaseModel):
    """Model: `CallbackDonutMoneyWithdraw`"""

    amount: float = Field()
    """Property `CallbackDonutMoneyWithdraw.amount`."""

    amount_without_fee: float = Field()
    """Property `CallbackDonutMoneyWithdraw.amount_without_fee`."""


class CallbackDonutMoneyWithdrawError(BaseModel):
    """Model: `CallbackDonutMoneyWithdrawError`"""

    reason: str = Field()
    """Property `CallbackDonutMoneyWithdrawError.reason`."""


class CallbackDonutSubscriptionCancelled(BaseModel):
    """Model: `CallbackDonutSubscriptionCancelled`"""

    user_id: int | None = Field(
        default=None,
    )
    """Property `CallbackDonutSubscriptionCancelled.user_id`."""


class CallbackDonutSubscriptionCreate(BaseModel):
    """Model: `CallbackDonutSubscriptionCreate`"""

    amount: int = Field()
    """Property `CallbackDonutSubscriptionCreate.amount`."""

    amount_without_fee: float = Field()
    """Property `CallbackDonutSubscriptionCreate.amount_without_fee`."""

    user_id: int | None = Field(
        default=None,
    )
    """Property `CallbackDonutSubscriptionCreate.user_id`."""


class CallbackDonutSubscriptionExpired(BaseModel):
    """Model: `CallbackDonutSubscriptionExpired`"""

    user_id: int | None = Field(
        default=None,
    )
    """Property `CallbackDonutSubscriptionExpired.user_id`."""


class CallbackDonutSubscriptionPriceChanged(BaseModel):
    """Model: `CallbackDonutSubscriptionPriceChanged`"""

    amount_old: int = Field()
    """Property `CallbackDonutSubscriptionPriceChanged.amount_old`."""

    amount_new: int = Field()
    """Property `CallbackDonutSubscriptionPriceChanged.amount_new`."""

    user_id: int | None = Field(
        default=None,
    )
    """Property `CallbackDonutSubscriptionPriceChanged.user_id`."""

    amount_diff: float | None = Field(
        default=None,
    )
    """Property `CallbackDonutSubscriptionPriceChanged.amount_diff`."""

    amount_diff_without_fee: float | None = Field(
        default=None,
    )
    """Property `CallbackDonutSubscriptionPriceChanged.amount_diff_without_fee`."""


class CallbackDonutSubscriptionProlonged(BaseModel):
    """Model: `CallbackDonutSubscriptionProlonged`"""

    amount: int = Field()
    """Property `CallbackDonutSubscriptionProlonged.amount`."""

    amount_without_fee: float = Field()
    """Property `CallbackDonutSubscriptionProlonged.amount_without_fee`."""

    user_id: int | None = Field(
        default=None,
    )
    """Property `CallbackDonutSubscriptionProlonged.user_id`."""


CallbackFwdMessages: typing.TypeAlias = list[list["CallbackForeignMessage"]]


class CallbackGroupChangePhoto(BaseModel):
    """Model: `CallbackGroupChangePhoto`"""

    user_id: int = Field()
    """Property `CallbackGroupChangePhoto.user_id`."""

    photo: "PhotosPhoto" = Field()
    """Property `CallbackGroupChangePhoto.photo`."""


class CallbackGroupChangeSettings(BaseModel):
    """Model: `CallbackGroupChangeSettings`"""

    user_id: int = Field()
    """Property `CallbackGroupChangeSettings.user_id`."""

    changes: "CallbackGroupSettingsChanges | None" = Field(
        default=None,
    )
    """Property `CallbackGroupChangeSettings.changes`."""


class CallbackGroupJoin(BaseModel):
    """Model: `CallbackGroupJoin`"""

    user_id: int = Field()
    """Property `CallbackGroupJoin.user_id`."""

    join_type: "CallbackGroupJoinType" = Field()
    """Property `CallbackGroupJoin.join_type`."""


class CallbackGroupJoinType(StrEnum, metaclass=BaseEnumMeta):
    JOIN = "join"
    UNSURE = "unsure"
    ACCEPTED = "accepted"
    APPROVED = "approved"
    REQUEST = "request"


class CallbackGroupLeave(BaseModel):
    """Model: `CallbackGroupLeave`"""

    user_id: int | None = Field(
        default=None,
    )
    """Property `CallbackGroupLeave.user_id`."""

    self: bool | None = Field(
        default=None,
    )
    """Property `CallbackGroupLeave.self`."""


class CallbackGroupMarket(IntEnum, metaclass=BaseEnumMeta):
    DISABLED = 0
    OPEN = 1


class CallbackGroupOfficerRole(IntEnum, metaclass=BaseEnumMeta):
    NONE = 0
    MODERATOR = 1
    EDITOR = 2
    ADMINISTRATOR = 3


class CallbackGroupOfficersEdit(BaseModel):
    """Model: `CallbackGroupOfficersEdit`"""

    admin_id: int = Field()
    """Property `CallbackGroupOfficersEdit.admin_id`."""

    user_id: int = Field()
    """Property `CallbackGroupOfficersEdit.user_id`."""

    level_old: "CallbackGroupOfficerRole" = Field()
    """Property `CallbackGroupOfficersEdit.level_old`."""

    level_new: "CallbackGroupOfficerRole" = Field()
    """Property `CallbackGroupOfficersEdit.level_new`."""


class CallbackGroupSettingsChanges(BaseModel):
    """Model: `CallbackGroupSettingsChanges`"""

    title: "CallbackGroupSettingsChangesStringValues | None" = Field(
        default=None,
    )
    """Property `CallbackGroupSettingsChanges.title`."""

    screen_name: "CallbackGroupSettingsChangesStringValues | None" = Field(
        default=None,
    )
    """Property `CallbackGroupSettingsChanges.screen_name`."""

    event_start_date: "CallbackGroupSettingsChangesIntegerValues | None" = Field(
        default=None,
    )
    """Property `CallbackGroupSettingsChanges.event_start_date`."""

    event_finish_date: "CallbackGroupSettingsChangesIntegerValues | None" = Field(
        default=None,
    )
    """Property `CallbackGroupSettingsChanges.event_finish_date`."""

    event_group_id: "CallbackGroupSettingsChangesIntegerValues | None" = Field(
        default=None,
    )
    """Property `CallbackGroupSettingsChanges.event_group_id`."""

    donations: "CallbackGroupSettingsChangesIntegerValues | None" = Field(
        default=None,
    )
    """Property `CallbackGroupSettingsChanges.donations`."""

    wall: "CallbackGroupSettingsChangesIntegerValues | None" = Field(
        default=None,
    )
    """Property `CallbackGroupSettingsChanges.wall`."""

    replies: "CallbackGroupSettingsChangesIntegerValues | None" = Field(
        default=None,
    )
    """Property `CallbackGroupSettingsChanges.replies`."""

    topics: "CallbackGroupSettingsChangesIntegerValues | None" = Field(
        default=None,
    )
    """Property `CallbackGroupSettingsChanges.topics`."""

    photos: "CallbackGroupSettingsChangesIntegerValues | None" = Field(
        default=None,
    )
    """Property `CallbackGroupSettingsChanges.photos`."""

    docs: "CallbackGroupSettingsChangesIntegerValues | None" = Field(
        default=None,
    )
    """Property `CallbackGroupSettingsChanges.docs`."""

    messages: "CallbackGroupSettingsChangesIntegerValues | None" = Field(
        default=None,
    )
    """Property `CallbackGroupSettingsChanges.messages`."""

    market: "CallbackGroupSettingsChangesIntegerValues | None" = Field(
        default=None,
    )
    """Property `CallbackGroupSettingsChanges.market`."""

    market_wiki: "CallbackGroupSettingsChangesIntegerValues | None" = Field(
        default=None,
    )
    """Property `CallbackGroupSettingsChanges.market_wiki`."""

    board: "CallbackGroupSettingsChangesIntegerValues | None" = Field(
        default=None,
    )
    """Property `CallbackGroupSettingsChanges.board`."""

    links: "CallbackGroupSettingsChangesIntegerValues | None" = Field(
        default=None,
    )
    """Property `CallbackGroupSettingsChanges.links`."""

    audio: "CallbackGroupSettingsChangesIntegerValues | None" = Field(
        default=None,
    )
    """Property `CallbackGroupSettingsChanges.audio`."""

    video: "CallbackGroupSettingsChangesIntegerValues | None" = Field(
        default=None,
    )
    """Property `CallbackGroupSettingsChanges.video`."""

    can_post_topics: "CallbackGroupSettingsChangesIntegerValues | None" = Field(
        default=None,
    )
    """Property `CallbackGroupSettingsChanges.can_post_topics`."""

    can_post_albums: "CallbackGroupSettingsChangesIntegerValues | None" = Field(
        default=None,
    )
    """Property `CallbackGroupSettingsChanges.can_post_albums`."""

    can_post_video: "CallbackGroupSettingsChangesIntegerValues | None" = Field(
        default=None,
    )
    """Property `CallbackGroupSettingsChanges.can_post_video`."""

    disable_market_comments: "CallbackGroupSettingsChangesIntegerValues | None" = Field(
        default=None,
    )
    """Property `CallbackGroupSettingsChanges.disable_market_comments`."""

    status_default: "CallbackGroupSettingsChangesIntegerValues | None" = Field(
        default=None,
    )
    """Property `CallbackGroupSettingsChanges.status_default`."""

    access: "CallbackGroupSettingsChangesIntegerValues | None" = Field(
        default=None,
    )
    """Property `CallbackGroupSettingsChanges.access`."""

    email: "CallbackGroupSettingsChangesStringValues | None" = Field(
        default=None,
    )
    """Property `CallbackGroupSettingsChanges.email`."""

    country_id: "CallbackGroupSettingsChangesIntegerValues | None" = Field(
        default=None,
    )
    """Property `CallbackGroupSettingsChanges.country_id`."""

    city_id: "CallbackGroupSettingsChangesIntegerValues | None" = Field(
        default=None,
    )
    """Property `CallbackGroupSettingsChanges.city_id`."""

    address: "CallbackGroupSettingsChangesStringValues | None" = Field(
        default=None,
    )
    """Property `CallbackGroupSettingsChanges.address`."""

    description: "CallbackGroupSettingsChangesStringValues | None" = Field(
        default=None,
    )
    """Property `CallbackGroupSettingsChanges.description`."""

    website: "CallbackGroupSettingsChangesStringValues | None" = Field(
        default=None,
    )
    """Property `CallbackGroupSettingsChanges.website`."""

    phone: "CallbackGroupSettingsChangesStringValues | None" = Field(
        default=None,
    )
    """Property `CallbackGroupSettingsChanges.phone`."""

    age_limits: "CallbackGroupSettingsChangesIntegerValues | None" = Field(
        default=None,
    )
    """Property `CallbackGroupSettingsChanges.age_limits`."""

    category_v2: "CallbackGroupSettingsChangesIntegerValues | None" = Field(
        default=None,
    )
    """Property `CallbackGroupSettingsChanges.category_v2`."""

    public_category: "CallbackGroupSettingsChangesIntegerValues | None" = Field(
        default=None,
    )
    """Property `CallbackGroupSettingsChanges.public_category`."""

    public_subcategory: "CallbackGroupSettingsChangesIntegerValues | None" = Field(
        default=None,
    )
    """Property `CallbackGroupSettingsChanges.public_subcategory`."""


class CallbackGroupSettingsChangesIntegerValues(BaseModel):
    """Model: `CallbackGroupSettingsChangesIntegerValues`"""

    old_value: int | None = Field(
        default=None,
    )
    """Property `CallbackGroupSettingsChangesIntegerValues.old_value`."""

    new_value: int | None = Field(
        default=None,
    )
    """Property `CallbackGroupSettingsChangesIntegerValues.new_value`."""


class CallbackGroupSettingsChangesStringValues(BaseModel):
    """Model: `CallbackGroupSettingsChangesStringValues`"""

    old_value: str | None = Field(
        default=None,
    )
    """Property `CallbackGroupSettingsChangesStringValues.old_value`."""

    new_value: str | None = Field(
        default=None,
    )
    """Property `CallbackGroupSettingsChangesStringValues.new_value`."""


class CallbackInfoForBots(BaseModel):
    """Model: `CallbackInfoForBots`"""

    button_actions: list["MessagesTemplateActionTypeNames"] | None = Field(
        default=None,
    )
    """Property `CallbackInfoForBots.button_actions`."""

    keyboard: bool | None = Field(
        default=None,
    )
    """client has support keyboard."""

    inline_keyboard: bool | None = Field(
        default=None,
    )
    """client has support inline keyboard."""

    carousel: bool | None = Field(
        default=None,
    )
    """client has support carousel."""

    lang_id: int | None = Field(
        default=None,
    )
    """client or user language id."""


class CallbackLikeAddRemoveObjectType(StrEnum, metaclass=BaseEnumMeta):
    VIDEO = "video"
    PHOTO = "photo"
    POST = "post"
    COMMENT = "comment"
    NOTE = "note"
    TOPIC_COMMENT = "topic_comment"
    PHOTO_COMMENT = "photo_comment"
    VIDEO_COMMENT = "video_comment"
    MARKET = "market"
    MARKET_COMMENT = "market_comment"


class CallbackLikeAddRemove(BaseModel):
    """Model: `CallbackLikeAddRemove`"""

    liker_id: int = Field()
    """Property `CallbackLikeAddRemove.liker_id`."""

    object_type: "CallbackLikeAddRemoveObjectType" = Field()
    """Property `CallbackLikeAddRemove.object_type`."""

    object_owner_id: int = Field()
    """Property `CallbackLikeAddRemove.object_owner_id`."""

    object_id: int = Field()
    """Property `CallbackLikeAddRemove.object_id`."""

    post_id: int = Field()
    """Property `CallbackLikeAddRemove.post_id`."""

    thread_reply_id: int | None = Field(
        default=None,
    )
    """Property `CallbackLikeAddRemove.thread_reply_id`."""


class CallbackMarketComment(BaseModel):
    """Model: `CallbackMarketComment`"""

    id: int = Field()
    """Property `CallbackMarketComment.id`."""

    from_id: int = Field()
    """Property `CallbackMarketComment.from_id`."""

    date: datetime.datetime = Field()
    """Property `CallbackMarketComment.date`."""

    text: str | None = Field(
        default=None,
    )
    """Property `CallbackMarketComment.text`."""

    market_owner_id: int | None = Field(
        default=None,
    )
    """Property `CallbackMarketComment.market_owner_id`."""

    photo_id: int | None = Field(
        default=None,
    )
    """Property `CallbackMarketComment.photo_id`."""


class CallbackMarketCommentDelete(BaseModel):
    """Model: `CallbackMarketCommentDelete`"""

    owner_id: int = Field()
    """Property `CallbackMarketCommentDelete.owner_id`."""

    id: int = Field()
    """Property `CallbackMarketCommentDelete.id`."""

    user_id: int = Field()
    """Property `CallbackMarketCommentDelete.user_id`."""

    item_id: int = Field()
    """Property `CallbackMarketCommentDelete.item_id`."""


class CallbackMessageAllow(BaseModel):
    """Model: `CallbackMessageAllow`"""

    user_id: int = Field()
    """Property `CallbackMessageAllow.user_id`."""

    key: str = Field()
    """Property `CallbackMessageAllow.key`."""


class CallbackMessageDeny(BaseModel):
    """Model: `CallbackMessageDeny`"""

    user_id: int = Field()
    """Property `CallbackMessageDeny.user_id`."""


class CallbackMessageEvent(BaseModel):
    """Model: `CallbackMessageEvent`"""

    user_id: int = Field()
    """Property `CallbackMessageEvent.user_id`."""

    peer_id: int = Field()
    """Property `CallbackMessageEvent.peer_id`."""

    event_id: str = Field()
    """Property `CallbackMessageEvent.event_id`."""

    payload: str = Field()
    """Property `CallbackMessageEvent.payload`."""

    conversation_message_id: int | None = Field(
        default=None,
    )
    """Property `CallbackMessageEvent.conversation_message_id`."""


class CallbackMessageNew(BaseModel):
    """Model: `CallbackMessageNew`"""

    client_info: "CallbackInfoForBots | None" = Field(
        default=None,
    )
    """Property `CallbackMessageNew.client_info`."""

    message: "CallbackMessage | None" = Field(
        default=None,
    )
    """Property `CallbackMessageNew.message`."""


class CallbackMessageObject(BaseModel):
    """Model: `CallbackMessageObject`"""

    client_info: "CallbackInfoForBots | None" = Field(
        default=None,
    )
    """Property `CallbackMessageObject.client_info`."""

    message: "CallbackMessage | None" = Field(
        default=None,
    )
    """Property `CallbackMessageObject.message`."""


class CallbackMessageReactionEvent(BaseModel):
    """Model: `CallbackMessageReactionEvent`"""

    reacted_id: int = Field()
    """Property `CallbackMessageReactionEvent.reacted_id`."""

    peer_id: int = Field()
    """Property `CallbackMessageReactionEvent.peer_id`."""

    cmid: int = Field()
    """Property `CallbackMessageReactionEvent.cmid`."""

    reaction_id: int | None = Field(
        default=None,
    )
    """Property `CallbackMessageReactionEvent.reaction_id`."""


class CallbackMessageRead(BaseModel):
    """Model: `CallbackMessageRead`"""

    from_id: int = Field()
    """Property `CallbackMessageRead.from_id`."""

    peer_id: int = Field()
    """Property `CallbackMessageRead.peer_id`."""

    read_message_id: int = Field()
    """Property `CallbackMessageRead.read_message_id`."""

    conversation_message_id: int = Field()
    """Property `CallbackMessageRead.conversation_message_id`."""


class CallbackMessageTypingStateState(StrEnum, metaclass=BaseEnumMeta):
    MESSAGE_TYPING_STATE = "message_typing_state"
    f__0 = "0"
    f__1 = "1"
    f__2 = "2"
    f__3 = "3"
    f__4 = "4"
    f__5 = "5"


class CallbackMessageTypingState(BaseModel):
    """Model: `CallbackMessageTypingState`"""

    from_id: int = Field()
    """Property `CallbackMessageTypingState.from_id`."""

    to_id: int = Field()
    """Property `CallbackMessageTypingState.to_id`."""

    state: "CallbackMessageTypingStateState" = Field()
    """Property `CallbackMessageTypingState.state`."""


class CallbackPhotoCommentDelete(BaseModel):
    """Model: `CallbackPhotoCommentDelete`"""

    id: int = Field()
    """Property `CallbackPhotoCommentDelete.id`."""

    owner_id: int = Field()
    """Property `CallbackPhotoCommentDelete.owner_id`."""

    user_id: int = Field()
    """Property `CallbackPhotoCommentDelete.user_id`."""

    photo_id: int = Field()
    """Property `CallbackPhotoCommentDelete.photo_id`."""

    deleter_id: int = Field()
    """Property `CallbackPhotoCommentDelete.deleter_id`."""


class CallbackPhotoNewVerticalAlign(StrEnum, metaclass=BaseEnumMeta):
    TOP = "top"
    MIDDLE = "middle"
    BOTTOM = "bottom"


class CallbackPhotoNew(BaseModel):
    """Model: `CallbackPhotoNew`"""

    album_id: int = Field()
    """Album ID."""

    date: datetime.datetime = Field()
    """Date when uploaded."""

    id: int = Field()
    """Photo ID."""

    owner_id: int = Field()
    """Photo owner\'s ID."""

    has_tags: bool = Field()
    """Whether photo has attached tag links."""

    access_key: str | None = Field(
        default=None,
    )
    """Access key for the photo."""

    height: int | None = Field(
        default=None,
    )
    """Original photo height."""

    images: list["PhotosImage"] | None = Field(
        default=None,
    )
    """Property `CallbackPhotoNew.images`."""

    lat: float | None = Field(
        default=None,
    )
    """Latitude."""

    long: float | None = Field(
        default=None,
    )
    """Longitude."""

    photo_256: str | None = Field(
        default=None,
    )
    """URL of image with 2560 px width."""

    thumb_hash: str | None = Field(
        default=None,
    )
    """Thumb Hash."""

    can_comment: bool | None = Field(
        default=None,
    )
    """Information whether current user can comment the photo."""

    place: str | None = Field(
        default=None,
    )
    """Property `CallbackPhotoNew.place`."""

    post_id: int | None = Field(
        default=None,
    )
    """Post ID."""

    sizes: list["PhotosPhotoSizes"] | None = Field(
        default=None,
    )
    """Property `CallbackPhotoNew.sizes`."""

    square_crop: str | None = Field(
        default=None,
    )
    """Property `CallbackPhotoNew.square_crop`."""

    text: str | None = Field(
        default=None,
    )
    """Photo caption."""

    user_id: int | None = Field(
        default=None,
    )
    """ID of the user who have uploaded the photo."""

    width: int | None = Field(
        default=None,
    )
    """Original photo width."""

    likes: "BaseLikes | None" = Field(
        default=None,
    )
    """Property `CallbackPhotoNew.likes`."""

    comments: "BaseObjectCount | None" = Field(
        default=None,
    )
    """Property `CallbackPhotoNew.comments`."""

    reposts: "BaseRepostsInfo | None" = Field(
        default=None,
    )
    """Property `CallbackPhotoNew.reposts`."""

    tags: "BaseObjectCount | None" = Field(
        default=None,
    )
    """Property `CallbackPhotoNew.tags`."""

    hidden: "BasePropertyExists | None" = Field(
        default=None,
    )
    """Returns if the photo is hidden above the wall."""

    real_offset: int | None = Field(
        default=None,
    )
    """Real position of the photo."""

    vertical_align: "CallbackPhotoNewVerticalAlign | None" = Field(
        default=None,
    )
    """Sets vertical alignment of a photo."""


class CallbackPollVoteNew(BaseModel):
    """Model: `CallbackPollVoteNew`"""

    owner_id: int = Field()
    """Property `CallbackPollVoteNew.owner_id`."""

    poll_id: int = Field()
    """Property `CallbackPollVoteNew.poll_id`."""

    option_id: int = Field()
    """Property `CallbackPollVoteNew.option_id`."""

    user_id: int = Field()
    """Property `CallbackPollVoteNew.user_id`."""


class CallbackType(StrEnum, metaclass=BaseEnumMeta):
    AUDIO_NEW = "audio_new"
    BOARD_POST_NEW = "board_post_new"
    BOARD_POST_EDIT = "board_post_edit"
    BOARD_POST_RESTORE = "board_post_restore"
    BOARD_POST_DELETE = "board_post_delete"
    CONFIRMATION = "confirmation"
    GROUP_LEAVE = "group_leave"
    GROUP_JOIN = "group_join"
    GROUP_CHANGE_PHOTO = "group_change_photo"
    GROUP_CHANGE_SETTINGS = "group_change_settings"
    GROUP_OFFICERS_EDIT = "group_officers_edit"
    LEAD_FORMS_NEW = "lead_forms_new"
    MARKET_COMMENT_NEW = "market_comment_new"
    MARKET_COMMENT_DELETE = "market_comment_delete"
    MARKET_COMMENT_EDIT = "market_comment_edit"
    MARKET_COMMENT_RESTORE = "market_comment_restore"
    MARKET_ORDER_NEW = "market_order_new"
    MARKET_ORDER_EDIT = "market_order_edit"
    MESSAGE_NEW = "message_new"
    MESSAGE_REPLY = "message_reply"
    MESSAGE_EDIT = "message_edit"
    MESSAGE_ALLOW = "message_allow"
    MESSAGE_DENY = "message_deny"
    MESSAGE_READ = "message_read"
    MESSAGE_TYPING_STATE = "message_typing_state"
    MESSAGES_EDIT = "messages_edit"
    MESSAGE_REACTION_EVENT = "message_reaction_event"
    PHOTO_NEW = "photo_new"
    PHOTO_COMMENT_NEW = "photo_comment_new"
    PHOTO_COMMENT_DELETE = "photo_comment_delete"
    PHOTO_COMMENT_EDIT = "photo_comment_edit"
    PHOTO_COMMENT_RESTORE = "photo_comment_restore"
    POLL_VOTE_NEW = "poll_vote_new"
    USER_BLOCK = "user_block"
    USER_UNBLOCK = "user_unblock"
    VIDEO_NEW = "video_new"
    VIDEO_COMMENT_NEW = "video_comment_new"
    VIDEO_COMMENT_DELETE = "video_comment_delete"
    VIDEO_COMMENT_EDIT = "video_comment_edit"
    VIDEO_COMMENT_RESTORE = "video_comment_restore"
    WALL_POST_NEW = "wall_post_new"
    WALL_REPLY_NEW = "wall_reply_new"
    WALL_REPLY_EDIT = "wall_reply_edit"
    WALL_REPLY_DELETE = "wall_reply_delete"
    WALL_REPLY_RESTORE = "wall_reply_restore"
    WALL_REPOST = "wall_repost"
    WALL_SCHEDULE_POST_NEW = "wall_schedule_post_new"
    WALL_SCHEDULE_POST_DELETE = "wall_schedule_post_delete"


class CallbackUserBlock(BaseModel):
    """Model: `CallbackUserBlock`"""

    admin_id: int = Field()
    """Property `CallbackUserBlock.admin_id`."""

    user_id: int = Field()
    """Property `CallbackUserBlock.user_id`."""

    unblock_date: datetime.datetime = Field()
    """Property `CallbackUserBlock.unblock_date`."""

    reason: int = Field()
    """Property `CallbackUserBlock.reason`."""

    comment: str | None = Field(
        default=None,
    )
    """Property `CallbackUserBlock.comment`."""


class CallbackUserUnblock(BaseModel):
    """Model: `CallbackUserUnblock`"""

    admin_id: int = Field()
    """Property `CallbackUserUnblock.admin_id`."""

    user_id: int = Field()
    """Property `CallbackUserUnblock.user_id`."""

    by_end_date: datetime.datetime = Field()
    """Property `CallbackUserUnblock.by_end_date`."""


class CallbackVideoCommentDelete(BaseModel):
    """Model: `CallbackVideoCommentDelete`"""

    id: int = Field()
    """Property `CallbackVideoCommentDelete.id`."""

    owner_id: int = Field()
    """Property `CallbackVideoCommentDelete.owner_id`."""

    deleter_id: int = Field()
    """Property `CallbackVideoCommentDelete.deleter_id`."""

    video_id: int = Field()
    """Property `CallbackVideoCommentDelete.video_id`."""


class CallbackVideoNew(BaseModel):
    """Model: `CallbackVideoNew`"""

    artist: str = Field()
    """Artist name."""

    id: int = Field()
    """Audio ID."""

    owner_id: int = Field()
    """Audio owner\'s ID."""

    title: str = Field()
    """Title."""

    duration: int = Field()
    """Duration in seconds."""

    access_key: str | None = Field(
        default=None,
    )
    """Access key for the audio."""

    url: str | None = Field(
        default=None,
    )
    """URL of mp3 file."""

    stream_duration: int | None = Field(
        default=None,
    )
    """Stream duration in seconds."""

    date: datetime.datetime | None = Field(
        default=None,
    )
    """Date when uploaded."""

    album_id: int | None = Field(
        default=None,
    )
    """Album ID."""

    performer: str | None = Field(
        default=None,
    )
    """Performer name."""

    file_size: int | None = Field(
        default=None,
    )
    """Примерный объем памяти занимаемый аудио на устройстве. Реализовано только для эпизодов подкастов."""


class CallbackVkpayTransaction(BaseModel):
    """Model: `CallbackVkpayTransaction`"""

    amount: int = Field()
    """Property `CallbackVkpayTransaction.amount`."""

    from_id: int = Field()
    """Property `CallbackVkpayTransaction.from_id`."""

    description: str = Field()
    """Property `CallbackVkpayTransaction.description`."""

    date: datetime.datetime = Field()
    """Property `CallbackVkpayTransaction.date`."""

    payload: str | None = Field(
        default=None,
    )
    """Property `CallbackVkpayTransaction.payload`."""


class CallbackWallCommentDelete(BaseModel):
    """Model: `CallbackWallCommentDelete`"""

    owner_id: int = Field()
    """Property `CallbackWallCommentDelete.owner_id`."""

    id: int = Field()
    """Property `CallbackWallCommentDelete.id`."""

    user_id: int = Field()
    """Property `CallbackWallCommentDelete.user_id`."""

    post_id: int = Field()
    """Property `CallbackWallCommentDelete.post_id`."""


class CallbackWallPostNewInnerType(StrEnum, metaclass=BaseEnumMeta):
    WALL_WALLPOST = "wall_wallpost"


class CallbackWallPostNew(BaseModel):
    """Model: `CallbackWallPostNew`"""

    inner_type: "CallbackWallPostNewInnerType" = Field()
    """Property `CallbackWallPostNew.inner_type`."""

    access_key: str | None = Field(
        default=None,
    )
    """Access key to private object."""

    is_deleted: bool | None = Field(
        default=None,
    )
    """Property `CallbackWallPostNew.is_deleted`."""

    deleted_reason: str | None = Field(
        default=None,
    )
    """Property `CallbackWallPostNew.deleted_reason`."""

    deleted_details: str | None = Field(
        default=None,
    )
    """Property `CallbackWallPostNew.deleted_details`."""

    donut_miniapp_url: str | None = Field(
        default=None,
    )
    """Property `CallbackWallPostNew.donut_miniapp_url`."""

    attachments: list["WallWallpostAttachment"] | None = Field(
        default=None,
    )
    """Property `CallbackWallPostNew.attachments`."""

    copyright: "WallPostCopyright | None" = Field(
        default=None,
    )
    """Information about the source of the post."""

    date: datetime.datetime | None = Field(
        default=None,
    )
    """Date of publishing in Unixtime."""

    edited: int | None = Field(
        default=None,
    )
    """Date of editing in Unixtime."""

    from_id: int | None = Field(
        default=None,
    )
    """Post author ID."""

    geo: "WallGeo | None" = Field(
        default=None,
    )
    """Property `CallbackWallPostNew.geo`."""

    id: int | None = Field(
        default=None,
    )
    """Post ID."""

    is_archived: bool | None = Field(
        default=None,
    )
    """Is post archived, only for post owners."""

    is_favorite: bool | None = Field(
        default=None,
    )
    """Information whether the post in favorites list."""

    likes: "BaseLikesInfo | None" = Field(
        default=None,
    )
    """Count of likes."""

    owner_id: int | None = Field(
        default=None,
    )
    """Wall owner\'s ID."""

    post_id: int | None = Field(
        default=None,
    )
    """If post type \'reply\', contains original post ID."""

    parents_stack: list[int] | None = Field(
        default=None,
    )
    """If post type \'reply\', contains original parent IDs stack."""

    post_source: "WallPostSource | None" = Field(
        default=None,
    )
    """Property `CallbackWallPostNew.post_source`."""

    post_type: "WallPostType | None" = Field(
        default=None,
    )
    """Property `CallbackWallPostNew.post_type`."""

    reposts: "BaseRepostsInfo | None" = Field(
        default=None,
    )
    """Property `CallbackWallPostNew.reposts`."""

    signer_id: int | None = Field(
        default=None,
    )
    """Post signer ID."""

    text: str | None = Field(
        default=None,
    )
    """Post text."""

    views: "WallViews | None" = Field(
        default=None,
    )
    """Count of views."""


class CallbackWallReplyEdit(BaseModel):
    """Model: `CallbackWallReplyEdit`"""

    id: int = Field()
    """Comment ID."""

    from_id: int = Field()
    """Author ID."""

    date: datetime.datetime = Field()
    """Date when the comment has been added in Unixtime."""

    text: str = Field()
    """Comment text."""

    can_edit: bool | None = Field(
        default=None,
    )
    """Property `CallbackWallReplyEdit.can_edit`."""

    post_id: int | None = Field(
        default=None,
    )
    """Property `CallbackWallReplyEdit.post_id`."""

    owner_id: int | None = Field(
        default=None,
    )
    """Property `CallbackWallReplyEdit.owner_id`."""

    parents_stack: list[int] | None = Field(
        default=None,
    )
    """Property `CallbackWallReplyEdit.parents_stack`."""

    photo_id: int | None = Field(
        default=None,
    )
    """Property `CallbackWallReplyEdit.photo_id`."""

    video_id: int | None = Field(
        default=None,
    )
    """Property `CallbackWallReplyEdit.video_id`."""

    attachments: list["WallWallpostAttachment"] | None = Field(
        default=None,
    )
    """Property `CallbackWallReplyEdit.attachments`."""

    donut: "WallWallCommentDonut | None" = Field(
        default=None,
    )
    """Property `CallbackWallReplyEdit.donut`."""

    likes: "BaseLikesInfo | None" = Field(
        default=None,
    )
    """Property `CallbackWallReplyEdit.likes`."""

    real_offset: int | None = Field(
        default=None,
    )
    """Real position of the comment."""

    reply_to_user: int | None = Field(
        default=None,
    )
    """Replied user ID."""

    reply_to_comment: int | None = Field(
        default=None,
    )
    """Replied comment ID."""

    thread: "CommentThread | None" = Field(
        default=None,
    )
    """Property `CallbackWallReplyEdit.thread`."""

    is_from_post_author: bool | None = Field(
        default=None,
    )
    """Whether post is by author of the post or not."""

    deleted: bool | None = Field(
        default=None,
    )
    """Property `CallbackWallReplyEdit.deleted`."""

    pid: int | None = Field(
        default=None,
    )
    """Photo ID."""


class CallbackWallReplyNew(BaseModel):
    """Model: `CallbackWallReplyNew`"""

    id: int = Field()
    """Comment ID."""

    from_id: int = Field()
    """Author ID."""

    date: datetime.datetime = Field()
    """Date when the comment has been added in Unixtime."""

    text: str = Field()
    """Comment text."""

    can_edit: bool | None = Field(
        default=None,
    )
    """Property `CallbackWallReplyNew.can_edit`."""

    post_id: int | None = Field(
        default=None,
    )
    """Property `CallbackWallReplyNew.post_id`."""

    owner_id: int | None = Field(
        default=None,
    )
    """Property `CallbackWallReplyNew.owner_id`."""

    parents_stack: list[int] | None = Field(
        default=None,
    )
    """Property `CallbackWallReplyNew.parents_stack`."""

    photo_id: int | None = Field(
        default=None,
    )
    """Property `CallbackWallReplyNew.photo_id`."""

    video_id: int | None = Field(
        default=None,
    )
    """Property `CallbackWallReplyNew.video_id`."""

    attachments: list["WallWallpostAttachment"] | None = Field(
        default=None,
    )
    """Property `CallbackWallReplyNew.attachments`."""

    donut: "WallWallCommentDonut | None" = Field(
        default=None,
    )
    """Property `CallbackWallReplyNew.donut`."""

    likes: "BaseLikesInfo | None" = Field(
        default=None,
    )
    """Property `CallbackWallReplyNew.likes`."""

    real_offset: int | None = Field(
        default=None,
    )
    """Real position of the comment."""

    reply_to_user: int | None = Field(
        default=None,
    )
    """Replied user ID."""

    reply_to_comment: int | None = Field(
        default=None,
    )
    """Replied comment ID."""

    thread: "CommentThread | None" = Field(
        default=None,
    )
    """Property `CallbackWallReplyNew.thread`."""

    is_from_post_author: bool | None = Field(
        default=None,
    )
    """Whether post is by author of the post or not."""

    deleted: bool | None = Field(
        default=None,
    )
    """Property `CallbackWallReplyNew.deleted`."""

    pid: int | None = Field(
        default=None,
    )
    """Photo ID."""


class CallbackWallReplyRestore(BaseModel):
    """Model: `CallbackWallReplyRestore`"""

    id: int = Field()
    """Comment ID."""

    from_id: int = Field()
    """Author ID."""

    date: datetime.datetime = Field()
    """Date when the comment has been added in Unixtime."""

    text: str = Field()
    """Comment text."""

    can_edit: bool | None = Field(
        default=None,
    )
    """Property `CallbackWallReplyRestore.can_edit`."""

    post_id: int | None = Field(
        default=None,
    )
    """Property `CallbackWallReplyRestore.post_id`."""

    owner_id: int | None = Field(
        default=None,
    )
    """Property `CallbackWallReplyRestore.owner_id`."""

    parents_stack: list[int] | None = Field(
        default=None,
    )
    """Property `CallbackWallReplyRestore.parents_stack`."""

    photo_id: int | None = Field(
        default=None,
    )
    """Property `CallbackWallReplyRestore.photo_id`."""

    video_id: int | None = Field(
        default=None,
    )
    """Property `CallbackWallReplyRestore.video_id`."""

    attachments: list["WallWallpostAttachment"] | None = Field(
        default=None,
    )
    """Property `CallbackWallReplyRestore.attachments`."""

    donut: "WallWallCommentDonut | None" = Field(
        default=None,
    )
    """Property `CallbackWallReplyRestore.donut`."""

    likes: "BaseLikesInfo | None" = Field(
        default=None,
    )
    """Property `CallbackWallReplyRestore.likes`."""

    real_offset: int | None = Field(
        default=None,
    )
    """Real position of the comment."""

    reply_to_user: int | None = Field(
        default=None,
    )
    """Replied user ID."""

    reply_to_comment: int | None = Field(
        default=None,
    )
    """Replied comment ID."""

    thread: "CommentThread | None" = Field(
        default=None,
    )
    """Property `CallbackWallReplyRestore.thread`."""

    is_from_post_author: bool | None = Field(
        default=None,
    )
    """Whether post is by author of the post or not."""

    deleted: bool | None = Field(
        default=None,
    )
    """Property `CallbackWallReplyRestore.deleted`."""

    pid: int | None = Field(
        default=None,
    )
    """Photo ID."""


class CallbackWallRepostInnerType(StrEnum, metaclass=BaseEnumMeta):
    WALL_WALLPOST = "wall_wallpost"


class CallbackWallRepost(BaseModel):
    """Model: `CallbackWallRepost`"""

    inner_type: "CallbackWallRepostInnerType" = Field()
    """Property `CallbackWallRepost.inner_type`."""

    access_key: str | None = Field(
        default=None,
    )
    """Access key to private object."""

    is_deleted: bool | None = Field(
        default=None,
    )
    """Property `CallbackWallRepost.is_deleted`."""

    deleted_reason: str | None = Field(
        default=None,
    )
    """Property `CallbackWallRepost.deleted_reason`."""

    deleted_details: str | None = Field(
        default=None,
    )
    """Property `CallbackWallRepost.deleted_details`."""

    donut_miniapp_url: str | None = Field(
        default=None,
    )
    """Property `CallbackWallRepost.donut_miniapp_url`."""

    attachments: list["WallWallpostAttachment"] | None = Field(
        default=None,
    )
    """Property `CallbackWallRepost.attachments`."""

    copyright: "WallPostCopyright | None" = Field(
        default=None,
    )
    """Information about the source of the post."""

    date: datetime.datetime | None = Field(
        default=None,
    )
    """Date of publishing in Unixtime."""

    edited: int | None = Field(
        default=None,
    )
    """Date of editing in Unixtime."""

    from_id: int | None = Field(
        default=None,
    )
    """Post author ID."""

    geo: "WallGeo | None" = Field(
        default=None,
    )
    """Property `CallbackWallRepost.geo`."""

    id: int | None = Field(
        default=None,
    )
    """Post ID."""

    is_archived: bool | None = Field(
        default=None,
    )
    """Is post archived, only for post owners."""

    is_favorite: bool | None = Field(
        default=None,
    )
    """Information whether the post in favorites list."""

    likes: "BaseLikesInfo | None" = Field(
        default=None,
    )
    """Count of likes."""

    owner_id: int | None = Field(
        default=None,
    )
    """Wall owner\'s ID."""

    post_id: int | None = Field(
        default=None,
    )
    """If post type \'reply\', contains original post ID."""

    parents_stack: list[int] | None = Field(
        default=None,
    )
    """If post type \'reply\', contains original parent IDs stack."""

    post_source: "WallPostSource | None" = Field(
        default=None,
    )
    """Property `CallbackWallRepost.post_source`."""

    post_type: "WallPostType | None" = Field(
        default=None,
    )
    """Property `CallbackWallRepost.post_type`."""

    reposts: "BaseRepostsInfo | None" = Field(
        default=None,
    )
    """Property `CallbackWallRepost.reposts`."""

    signer_id: int | None = Field(
        default=None,
    )
    """Post signer ID."""

    text: str | None = Field(
        default=None,
    )
    """Post text."""

    views: "WallViews | None" = Field(
        default=None,
    )
    """Count of views."""


class CallsCall(BaseModel):
    """Model: `CallsCall`"""

    initiator_id: int = Field()
    """Caller initiator."""

    receiver_id: int = Field()
    """Caller receiver."""

    state: "CallsEndState" = Field()
    """Property `CallsCall.state`."""

    time: int = Field()
    """Timestamp for call."""

    duration: int | None = Field(
        default=None,
    )
    """Call duration."""

    video: bool | None = Field(
        default=None,
    )
    """Was this call initiated as video call."""

    participants: "CallsParticipants | None" = Field(
        default=None,
    )
    """Property `CallsCall.participants`."""


class CallsEndState(StrEnum, metaclass=BaseEnumMeta):
    CANCELED_BY_INITIATOR = "canceled_by_initiator"
    CANCELED_BY_RECEIVER = "canceled_by_receiver"
    REACHED = "reached"


class CallsParticipants(BaseModel):
    """Model: `CallsParticipants`"""

    list_: list[int] | None = Field(
        default=None,
        alias="list",
    )
    """Property `CallsParticipants.list`."""

    count: int | None = Field(
        default=None,
    )
    """Participants count."""


class CallsShortCredentials(BaseModel):
    """These credentials may be used to join a call without knowing a VK Join Link
    Model: `CallsShortCredentials`
    """

    id: str = Field()
    """Short numeric ID of a call."""

    password: str = Field()
    """Password that can be used to join a call by short numeric ID."""

    link_without_password: str = Field()
    """Link without a password."""

    link_with_password: str = Field()
    """Link with a password."""


class CommentThread(BaseModel):
    """Model: `CommentThread`"""

    count: int = Field()
    """Comments number."""

    items: list["WallWallComment"] | None = Field(
        default=None,
    )
    """Property `CommentThread.items`."""

    can_post: bool | None = Field(
        default=None,
    )
    """Information whether current user can comment the post."""

    show_reply_button: bool | None = Field(
        default=None,
    )
    """Information whether recommended to display reply button."""

    groups_can_post: bool | None = Field(
        default=None,
    )
    """Information whether groups can comment the post."""

    author_replied: bool | None = Field(
        default=None,
    )
    """Information whether author commented the thread."""


DatabaseCitiesFields: typing.TypeAlias = str


class DatabaseCityById(BaseModel):
    """Model: `DatabaseCityById`"""

    id: int = Field()
    """Object ID."""

    title: str = Field()
    """Object title."""


class DatabaseFaculty(BaseModel):
    """Model: `DatabaseFaculty`"""

    id: int | None = Field(
        default=None,
    )
    """Faculty ID."""

    title: str | None = Field(
        default=None,
    )
    """Faculty title."""


class DatabaseLanguageFull(BaseModel):
    """Model: `DatabaseLanguageFull`"""

    id: int = Field()
    """Language ID."""

    native_name: str = Field()
    """Language native name."""


class DatabaseRegion(BaseModel):
    """Model: `DatabaseRegion`"""

    id: int | None = Field(
        default=None,
    )
    """Region ID."""

    title: str | None = Field(
        default=None,
    )
    """Region title."""


class DatabaseSchool(BaseModel):
    """Model: `DatabaseSchool`"""

    id: int | None = Field(
        default=None,
    )
    """School ID."""

    title: str | None = Field(
        default=None,
    )
    """School title."""


class DatabaseSchoolClass(BaseModel):
    """Model: `DatabaseSchoolClass`"""

    id: int = Field()
    """Object ID."""

    title: str = Field()
    """Object title."""


class DatabaseStation(BaseModel):
    """Model: `DatabaseStation`"""

    id: int = Field()
    """Station ID."""

    name: str = Field()
    """Station name."""

    city_id: int | None = Field(
        default=None,
    )
    """City ID."""

    color: str | None = Field(
        default=None,
    )
    """Hex color code without #."""


class DatabaseUniversity(BaseModel):
    """Model: `DatabaseUniversity`"""

    id: int | None = Field(
        default=None,
    )
    """University ID."""

    title: str | None = Field(
        default=None,
    )
    """University title."""


class DocsDoc(BaseModel):
    """Model: `DocsDoc`"""

    id: int = Field()
    """Document ID."""

    owner_id: int = Field()
    """Document owner ID."""

    title: str = Field()
    """Document title."""

    size: int = Field()
    """File size in bites."""

    ext: str = Field()
    """File extension."""

    date: datetime.datetime = Field()
    """Date when file has been uploaded in Unixtime."""

    type: int = Field()
    """Document type."""

    url: str | None = Field(
        default=None,
    )
    """File URL."""

    preview: "DocsDocPreview | None" = Field(
        default=None,
    )
    """Property `DocsDoc.preview`."""

    is_licensed: bool | None = Field(
        default=None,
    )
    """Property `DocsDoc.is_licensed`."""

    access_key: str | None = Field(
        default=None,
    )
    """Access key for the document."""

    tags: list[str] | None = Field(
        default=None,
    )
    """Document tags."""


class DocsDocAttachmentType(StrEnum, metaclass=BaseEnumMeta):
    DOC = "doc"
    GRAFFITI = "graffiti"
    AUDIO_MESSAGE = "audio_message"


class DocsDocPreview(BaseModel):
    """Model: `DocsDocPreview`"""

    audio_msg: "DocsDocPreviewAudioMsg | None" = Field(
        default=None,
    )
    """Property `DocsDocPreview.audio_msg`."""

    graffiti: "DocsDocPreviewGraffiti | None" = Field(
        default=None,
    )
    """Property `DocsDocPreview.graffiti`."""

    photo: "DocsDocPreviewPhoto | None" = Field(
        default=None,
    )
    """Property `DocsDocPreview.photo`."""

    video: "DocsDocPreviewVideo | None" = Field(
        default=None,
    )
    """Property `DocsDocPreview.video`."""


class DocsDocPreviewAudioMsg(BaseModel):
    """Model: `DocsDocPreviewAudioMsg`"""

    duration: int = Field()
    """Audio message duration in seconds."""

    link_mp3: str = Field()
    """MP3 file URL."""

    link_ogg: str = Field()
    """OGG file URL."""

    waveform: list[int] = Field()
    """Property `DocsDocPreviewAudioMsg.waveform`."""


class DocsDocPreviewGraffiti(BaseModel):
    """Model: `DocsDocPreviewGraffiti`"""

    src: str = Field()
    """Graffiti file URL."""

    width: int = Field()
    """Graffiti width."""

    height: int = Field()
    """Graffiti height."""


class DocsDocPreviewPhoto(BaseModel):
    """Model: `DocsDocPreviewPhoto`"""

    sizes: list["DocsDocPreviewPhotoSizes"] | None = Field(
        default=None,
    )
    """Property `DocsDocPreviewPhoto.sizes`."""


class DocsDocPreviewPhotoSizes(BaseModel):
    """Model: `DocsDocPreviewPhotoSizes`"""

    src: str = Field()
    """URL of the image."""

    width: int = Field()
    """Width in px."""

    height: int = Field()
    """Height in px."""

    type: "PhotosPhotoSizesType" = Field()
    """Property `DocsDocPreviewPhotoSizes.type`."""


class DocsDocPreviewVideo(BaseModel):
    """Model: `DocsDocPreviewVideo`"""

    src: str = Field()
    """Video URL."""

    width: int = Field()
    """Video\'s width in pixels."""

    height: int = Field()
    """Video\'s height in pixels."""

    file_size: int = Field()
    """Video file size in bites."""


class DocsDocTypes(BaseModel):
    """Model: `DocsDocTypes`"""

    id: int = Field()
    """Doc type ID."""

    name: str = Field()
    """Doc type title."""

    count: int = Field()
    """Number of docs."""


class DonutDonatorSubscriptionInfoStatus(StrEnum, metaclass=BaseEnumMeta):
    ACTIVE = "active"
    EXPIRING = "expiring"


class DonutDonatorSubscriptionInfo(BaseModel):
    """Info about user VK Donut subscription
    Model: `DonutDonatorSubscriptionInfo`
    """

    owner_id: int = Field()
    """Property `DonutDonatorSubscriptionInfo.owner_id`."""

    next_payment_date: datetime.datetime = Field()
    """Property `DonutDonatorSubscriptionInfo.next_payment_date`."""

    amount: int = Field()
    """Property `DonutDonatorSubscriptionInfo.amount`."""

    status: "DonutDonatorSubscriptionInfoStatus" = Field()
    """Property `DonutDonatorSubscriptionInfo.status`."""


class EventsEventAttach(BaseModel):
    """Model: `EventsEventAttach`"""

    button_text: str = Field()
    """text of attach."""

    friends: list[int] = Field()
    """array of friends ids."""

    id: int = Field()
    """event ID."""

    is_favorite: bool = Field()
    """is favorite."""

    text: str = Field()
    """text of attach."""

    address: str | None = Field(
        default=None,
    )
    """address of event."""

    member_status: "GroupsGroupFullMemberStatus | None" = Field(
        default=None,
    )
    """Current user\'s member status."""

    time: int | None = Field(
        default=None,
    )
    """event start time."""


class FaveBookmark(BaseModel):
    """Model: `FaveBookmark`"""

    added_date: datetime.datetime = Field()
    """Timestamp, when this item was bookmarked."""

    seen: bool = Field()
    """Has user seen this item."""

    tags: list["FaveTag"] = Field()
    """Property `FaveBookmark.tags`."""

    type: "FaveBookmarkType" = Field()
    """Item type."""

    link: "BaseLink | None" = Field(
        default=None,
    )
    """Property `FaveBookmark.link`."""

    post: "WallWallpostFull | None" = Field(
        default=None,
    )
    """Property `FaveBookmark.post`."""

    product: "MarketMarketItemFull | None" = Field(
        default=None,
    )
    """Property `FaveBookmark.product`."""

    video: "VideoVideoFull | None" = Field(
        default=None,
    )
    """Property `FaveBookmark.video`."""


class FaveBookmarkType(StrEnum, metaclass=BaseEnumMeta):
    POST = "post"
    VIDEO = "video"
    PRODUCT = "product"
    ARTICLE = "article"
    LINK = "link"
    CLIP = "clip"
    GAME = "game"
    MINI_APP = "mini_app"


class FavePage(BaseModel):
    """Model: `FavePage`"""

    description: str = Field()
    """Some info about user or group."""

    tags: list["FaveTag"] = Field()
    """Property `FavePage.tags`."""

    type: "FavePageType" = Field()
    """Item type."""

    group: "GroupsGroupFull | None" = Field(
        default=None,
    )
    """Property `FavePage.group`."""

    updated_date: datetime.datetime | None = Field(
        default=None,
    )
    """Timestamp, when this page was bookmarked."""

    user: "UsersUserFull | None" = Field(
        default=None,
    )
    """Property `FavePage.user`."""


class FavePageType(StrEnum, metaclass=BaseEnumMeta):
    USER = "user"
    GROUP = "group"
    HINTS = "hints"


class FaveTag(BaseModel):
    """Model: `FaveTag`"""

    id: int | None = Field(
        default=None,
    )
    """Tag id."""

    name: str | None = Field(
        default=None,
    )
    """Tag name."""


class GiftsGift(BaseModel):
    """Model: `GiftsGift`"""

    date: datetime.datetime | None = Field(
        default=None,
    )
    """Date when gist has been sent in Unixtime."""

    from_id: int | None = Field(
        default=None,
    )
    """Gift sender ID."""

    gift: "GiftsLayout | None" = Field(
        default=None,
    )
    """Property `GiftsGift.gift`."""

    gift_hash: str | None = Field(
        default=None,
    )
    """Hash."""

    id: int | None = Field(
        default=None,
    )
    """Gift ID."""

    message: str | None = Field(
        default=None,
    )
    """Comment text."""

    privacy: "GiftsGiftPrivacy | None" = Field(
        default=None,
    )
    """Property `GiftsGift.privacy`."""


class GiftsGiftPrivacy(IntEnum, metaclass=BaseEnumMeta):
    NAME_AND_MESSAGE_FOR_ALL = 0
    NAME_FOR_ALL = 1
    NAME_AND_MESSAGE_FOR_RECIPIENT_ONLY = 2


class GiftsLayout(BaseModel):
    """Model: `GiftsLayout`"""

    id: int = Field()
    """Gift ID."""

    thumb_512: str | None = Field(
        default=None,
    )
    """URL of the preview image with 512 px in width."""

    thumb_256: str | None = Field(
        default=None,
    )
    """URL of the preview image with 256 px in width."""

    thumb_48: str | None = Field(
        default=None,
    )
    """URL of the preview image with 48 px in width."""

    thumb_96: str | None = Field(
        default=None,
    )
    """URL of the preview image with 96 px in width."""

    stickers_product_id: int | None = Field(
        default=None,
    )
    """ID of the sticker pack, if the gift is representing one."""

    is_stickers_style: bool | None = Field(
        default=None,
    )
    """Information whether gift represents a stickers style."""

    build_id: str | None = Field(
        default=None,
    )
    """ID of the build of constructor gift."""

    keywords: str | None = Field(
        default=None,
    )
    """Keywords used for search."""


class GroupsAddress(BaseModel):
    """Model: `GroupsAddress`"""

    id: int = Field()
    """Address id."""

    additional_address: str | None = Field(
        default=None,
    )
    """Additional address to the place (6 floor, left door)."""

    address: str | None = Field(
        default=None,
    )
    """String address to the place (Nevsky, 28)."""

    city_id: int | None = Field(
        default=None,
    )
    """City id of address."""

    city: "DatabaseCityById | None" = Field(
        default=None,
    )
    """City for address."""

    metro_station: "DatabaseStation | None" = Field(
        default=None,
    )
    """Metro for address."""

    country: "BaseCountry | None" = Field(
        default=None,
    )
    """Country for address."""

    distance: int | None = Field(
        default=None,
    )
    """Distance from the point."""

    latitude: float | None = Field(
        default=None,
    )
    """Address latitude."""

    longitude: float | None = Field(
        default=None,
    )
    """Address longitude."""

    metro_station_id: int | None = Field(
        default=None,
    )
    """Metro id of address."""

    phone: str | None = Field(
        default=None,
    )
    """Address phone."""

    time_offset: int | None = Field(
        default=None,
    )
    """Time offset int minutes from utc time."""

    timetable: "GroupsAddressTimetable | None" = Field(
        default=None,
    )
    """Week timetable for the address."""

    title: str | None = Field(
        default=None,
    )
    """Title of the place (Zinger, etc)."""

    work_info_status: "GroupsAddressWorkInfoStatus | None" = Field(
        default=None,
    )
    """Status of information about timetable."""

    place_id: int | None = Field(
        default=None,
    )
    """Property `GroupsAddress.place_id`."""


class GroupsAddressTimetable(BaseModel):
    """Timetable for a week
    Model: `GroupsAddressTimetable`
    """

    fri: "GroupsAddressTimetableDay | None" = Field(
        default=None,
    )
    """Timetable for friday."""

    mon: "GroupsAddressTimetableDay | None" = Field(
        default=None,
    )
    """Timetable for monday."""

    sat: "GroupsAddressTimetableDay | None" = Field(
        default=None,
    )
    """Timetable for saturday."""

    sun: "GroupsAddressTimetableDay | None" = Field(
        default=None,
    )
    """Timetable for sunday."""

    thu: "GroupsAddressTimetableDay | None" = Field(
        default=None,
    )
    """Timetable for thursday."""

    tue: "GroupsAddressTimetableDay | None" = Field(
        default=None,
    )
    """Timetable for tuesday."""

    wed: "GroupsAddressTimetableDay | None" = Field(
        default=None,
    )
    """Timetable for wednesday."""


class GroupsAddressTimetableDay(BaseModel):
    """Timetable for one day
    Model: `GroupsAddressTimetableDay`
    """

    close_time: int = Field()
    """Close time in minutes."""

    open_time: int = Field()
    """Open time in minutes."""

    break_close_time: int | None = Field(
        default=None,
    )
    """Close time of the break in minutes."""

    break_open_time: int | None = Field(
        default=None,
    )
    """Start time of the break in minutes."""


class GroupsAddressWorkInfoStatus(StrEnum, metaclass=BaseEnumMeta):
    NO_INFORMATION = "no_information"
    TEMPORARILY_CLOSED = "temporarily_closed"
    ALWAYS_OPENED = "always_opened"
    TIMETABLE = "timetable"
    FOREVER_CLOSED = "forever_closed"


class GroupsAddressesInfo(BaseModel):
    """Model: `GroupsAddressesInfo`"""

    is_enabled: bool = Field()
    """Information whether addresses is enabled."""

    main_address_id: int | None = Field(
        default=None,
    )
    """Main address id for group."""

    main_address: "GroupsAddress | None" = Field(
        default=None,
    )
    """Main address."""

    count: int | None = Field(
        default=None,
    )
    """Count of addresses."""


class GroupsBanInfo(BaseModel):
    """Model: `GroupsBanInfo`"""

    admin_id: int | None = Field(
        default=None,
    )
    """Administrator ID."""

    comment: str | None = Field(
        default=None,
    )
    """Comment for a ban."""

    comment_visible: bool | None = Field(
        default=None,
    )
    """Show comment for user."""

    is_closed: bool | None = Field(
        default=None,
    )
    """Property `GroupsBanInfo.is_closed`."""

    date: datetime.datetime | None = Field(
        default=None,
    )
    """Date when user has been added to blacklist in Unixtime."""

    end_date: datetime.datetime | None = Field(
        default=None,
    )
    """Date when user will be removed from blacklist in Unixtime."""

    reason: "GroupsBanInfoReason | None" = Field(
        default=None,
    )
    """Property `GroupsBanInfo.reason`."""


class GroupsBanInfoReason(IntEnum, metaclass=BaseEnumMeta):
    OTHER = 0
    SPAM = 1
    VERBAL_ABUSE = 2
    STRONG_LANGUAGE = 3
    FLOOD = 4


class GroupsCallbackServerStatus(StrEnum, metaclass=BaseEnumMeta):
    UNCONFIGURED = "unconfigured"
    FAILED = "failed"
    WAIT = "wait"
    OK = "ok"


class GroupsCallbackServer(BaseModel):
    """Model: `GroupsCallbackServer`"""

    id: int = Field()
    """Property `GroupsCallbackServer.id`."""

    title: str = Field()
    """Property `GroupsCallbackServer.title`."""

    creator_id: int = Field()
    """Property `GroupsCallbackServer.creator_id`."""

    url: str = Field()
    """Property `GroupsCallbackServer.url`."""

    secret_key: str = Field()
    """Property `GroupsCallbackServer.secret_key`."""

    status: "GroupsCallbackServerStatus" = Field()
    """Property `GroupsCallbackServer.status`."""


class GroupsCallbackSettings(BaseModel):
    """Model: `GroupsCallbackSettings`"""

    api_version: str | None = Field(
        default=None,
    )
    """API version used for the events."""

    events: "GroupsLongPollEvents | None" = Field(
        default=None,
    )
    """Property `GroupsCallbackSettings.events`."""


class GroupsContactsItem(BaseModel):
    """Model: `GroupsContactsItem`"""

    user_id: int | None = Field(
        default=None,
    )
    """User ID."""

    desc: str | None = Field(
        default=None,
    )
    """Contact description."""

    phone: str | None = Field(
        default=None,
    )
    """Contact phone."""

    email: str | None = Field(
        default=None,
    )
    """Contact email."""


class GroupsCountersGroup(BaseModel):
    """Model: `GroupsCountersGroup`"""

    addresses: int | None = Field(
        default=None,
    )
    """Addresses number."""

    albums: int | None = Field(
        default=None,
    )
    """Photo albums number."""

    audios: int | None = Field(
        default=None,
    )
    """Audios number."""

    audio_playlists: int | None = Field(
        default=None,
    )
    """Audio playlists number."""

    docs: int | None = Field(
        default=None,
    )
    """Docs number."""

    market: int | None = Field(
        default=None,
    )
    """Market items number."""

    photos: int | None = Field(
        default=None,
    )
    """Photos number."""

    topics: int | None = Field(
        default=None,
    )
    """Topics number."""

    videos: int | None = Field(
        default=None,
    )
    """Videos number."""

    video_playlists: int | None = Field(
        default=None,
    )
    """Playlists number."""

    market_services: int | None = Field(
        default=None,
    )
    """Market services number."""

    podcasts: int | None = Field(
        default=None,
    )
    """Podcasts number."""

    articles: int | None = Field(
        default=None,
    )
    """Articles number."""

    narratives: int | None = Field(
        default=None,
    )
    """Narratives number."""

    clips: int | None = Field(
        default=None,
    )
    """Clips number."""

    clips_followers: int | None = Field(
        default=None,
    )
    """Clips followers number."""

    videos_followers: int | None = Field(
        default=None,
    )
    """Videos followers number."""

    clips_views: int | None = Field(
        default=None,
    )
    """Clips views number."""

    clips_likes: int | None = Field(
        default=None,
    )
    """Clips likes number."""


class GroupsFields(StrEnum, metaclass=BaseEnumMeta):
    ID = "id"
    NAME = "name"
    SCREEN_NAME = "screen_name"
    IS_CLOSED = "is_closed"
    TYPE = "type"
    IS_ADMIN = "is_admin"
    ADMIN_LEVEL = "admin_level"
    IS_MEMBER = "is_member"
    IS_ADVERTISER = "is_advertiser"
    START_DATE = "start_date"
    FINISH_DATE = "finish_date"
    DEACTIVATED = "deactivated"
    PHOTO_50 = "photo_50"
    PHOTO_100 = "photo_100"
    PHOTO_200 = "photo_200"
    PHOTO_200_ORIG = "photo_200_orig"
    PHOTO_400 = "photo_400"
    PHOTO_400_ORIG = "photo_400_orig"
    PHOTO_MAX = "photo_max"
    PHOTO_MAX_ORIG = "photo_max_orig"
    EST_DATE = "est_date"
    PUBLIC_DATE_LABEL = "public_date_label"
    PHOTO_MAX_SIZE = "photo_max_size"
    IS_VIDEO_LIVE_NOTIFICATIONS_BLOCKED = "is_video_live_notifications_blocked"
    VIDEO_LIVE = "video_live"
    MARKET = "market"
    MEMBER_STATUS = "member_status"
    IS_ADULT = "is_adult"
    IS_HIDDEN_FROM_FEED = "is_hidden_from_feed"
    IS_FAVORITE = "is_favorite"
    IS_SUBSCRIBED = "is_subscribed"
    CITY = "city"
    VERIFIED = "verified"
    DESCRIPTION = "description"
    WIKI_PAGE = "wiki_page"
    MEMBERS_COUNT = "members_count"
    MEMBERS_COUNT_TEXT = "members_count_text"
    REQUESTS_COUNT = "requests_count"
    VIDEO_LIVE_LEVEL = "video_live_level"
    VIDEO_LIVE_COUNT = "video_live_count"
    CLIPS_COUNT = "clips_count"
    TEXTLIVES_COUNT = "textlives_count"
    COUNTERS = "counters"
    COVER = "cover"
    CAN_POST = "can_post"
    CAN_SUGGEST = "can_suggest"
    CAN_UPLOAD_STORY = "can_upload_story"
    CAN_UPLOAD_DOC = "can_upload_doc"
    CAN_UPLOAD_VIDEO = "can_upload_video"
    CAN_UPLOAD_CLIP = "can_upload_clip"
    CAN_SEE_ALL_POSTS = "can_see_all_posts"
    CAN_CREATE_TOPIC = "can_create_topic"
    ACTIVITY = "activity"
    FIXED_POST = "fixed_post"
    HAS_PHOTO = "has_photo"
    CROP_PHOTO = "crop_photo"
    STATUS = "status"
    STATUS_AUDIO = "status_audio"
    MAIN_ALBUM_ID = "main_album_id"
    LINKS = "links"
    CONTACTS = "contacts"
    WALL = "wall"
    SITE = "site"
    MAIN_SECTION = "main_section"
    SECONDARY_SECTION = "secondary_section"
    TRENDING = "trending"
    CAN_MESSAGE = "can_message"
    IS_MESSAGES_BLOCKED = "is_messages_blocked"
    CAN_SEND_NOTIFY = "can_send_notify"
    ONLINE_STATUS = "online_status"
    INVITED_BY = "invited_by"
    AGE_LIMITS = "age_limits"
    BAN_INFO = "ban_info"
    HAS_MARKET_APP = "has_market_app"
    USING_VKPAY_MARKET_APP = "using_vkpay_market_app"
    HAS_GROUP_CHANNEL = "has_group_channel"
    ADDRESSES = "addresses"
    MESSAGES = "messages"
    BUSINESS_RATING = "business_rating"
    IS_SUBSCRIBED_PODCASTS = "is_subscribed_podcasts"
    CAN_SUBSCRIBE_PODCASTS = "can_subscribe_podcasts"
    CAN_SUBSCRIBE_POSTS = "can_subscribe_posts"
    LIVE_COVERS = "live_covers"
    STORIES_ARCHIVE_COUNT = "stories_archive_count"
    HAS_UNSEEN_STORIES = "has_unseen_stories"
    CATEGORY = "category"
    CATEGORY0 = "category0"
    CATEGORY1 = "category1"
    RATING = "rating"
    IS_MARKET_MARKET_LINK_ATTACHMENT_ENABLED = "is_market_market_link_attachment_enabled"
    IS_MARKET_MESSAGE_TO_BC_ATTACHMENT_ENABLED = "is_market_message_to_bc_attachment_enabled"
    UNREAD_COUNT = "unread_count"
    VIDEOS_COUNT = "videos_count"


class GroupsFilter(StrEnum, metaclass=BaseEnumMeta):
    ADMIN = "admin"
    EDITOR = "editor"
    MODER = "moder"
    ADVERTISER = "advertiser"
    GROUPS = "groups"
    PUBLICS = "publics"
    EVENTS = "events"
    HAS_ADDRESSES = "has_addresses"


class GroupsGroup(BaseModel):
    """Model: `GroupsGroup`"""

    id: int = Field()
    """Community ID."""

    name: str | None = Field(
        default=None,
    )
    """Community name."""

    screen_name: str | None = Field(
        default=None,
    )
    """Domain of the community page."""

    is_closed: "GroupsGroupIsClosed | None" = Field(
        default=None,
    )
    """Property `GroupsGroup.is_closed`."""

    type: "GroupsGroupType | None" = Field(
        default=None,
    )
    """Property `GroupsGroup.type`."""

    is_admin: bool | None = Field(
        default=None,
    )
    """Information whether current user is administrator."""

    admin_level: "GroupsGroupAdminLevel | None" = Field(
        default=None,
    )
    """Property `GroupsGroup.admin_level`."""

    is_member: bool | None = Field(
        default=None,
    )
    """Information whether current user is member."""

    is_advertiser: bool | None = Field(
        default=None,
    )
    """Information whether current user is advertiser."""

    start_date: datetime.datetime | None = Field(
        default=None,
    )
    """Start date in Unixtime format."""

    finish_date: datetime.datetime | None = Field(
        default=None,
    )
    """Finish date in Unixtime format."""

    verified: bool | None = Field(
        default=None,
    )
    """Information whether community is verified."""

    deactivated: str | None = Field(
        default=None,
    )
    """Information whether community is banned."""

    photo_50: str | None = Field(
        default=None,
    )
    """URL of square photo of the community with 50 pixels in width."""

    photo_100: str | None = Field(
        default=None,
    )
    """URL of square photo of the community with 100 pixels in width."""

    photo_200: str | None = Field(
        default=None,
    )
    """URL of square photo of the community with 200 pixels in width."""

    photo_200_orig: str | None = Field(
        default=None,
    )
    """URL of square photo of the community with 200 pixels in width original."""

    photo_400: str | None = Field(
        default=None,
    )
    """URL of square photo of the community with 400 pixels in width."""

    photo_400_orig: str | None = Field(
        default=None,
    )
    """URL of square photo of the community with 400 pixels in width original."""

    photo_max: str | None = Field(
        default=None,
    )
    """URL of square photo of the community with max pixels in width."""

    photo_max_orig: str | None = Field(
        default=None,
    )
    """URL of square photo of the community with max pixels in width original."""

    est_date: str | None = Field(
        default=None,
    )
    """Established date."""

    public_date_label: str | None = Field(
        default=None,
    )
    """Public date label."""

    photo_max_size: "GroupsPhotoSize | None" = Field(
        default=None,
    )
    """Property `GroupsGroup.photo_max_size`."""

    is_video_live_notifications_blocked: bool | None = Field(
        default=None,
    )
    """Property `GroupsGroup.is_video_live_notifications_blocked`."""

    video_live: "VideoLiveInfo | None" = Field(
        default=None,
    )
    """Property `GroupsGroup.video_live`."""


class GroupsGroupAccess(IntEnum, metaclass=BaseEnumMeta):
    OPEN = 0
    CLOSED = 1
    PRIVATE = 2


class GroupsGroupAdminLevel(IntEnum, metaclass=BaseEnumMeta):
    MODERATOR = 1
    EDITOR = 2
    ADMINISTRATOR = 3


class GroupsGroupAgeLimits(IntEnum, metaclass=BaseEnumMeta):
    UNLIMITED = 1
    F__16_PLUS = 2
    F__18_PLUS = 3


class GroupsGroupAttach(BaseModel):
    """Model: `GroupsGroupAttach`"""

    id: int = Field()
    """group ID."""

    text: str = Field()
    """text of attach."""

    status: str = Field()
    """activity or category of group."""

    size: int = Field()
    """size of group."""

    is_favorite: bool = Field()
    """is favorite."""


class GroupsGroupAudio(IntEnum, metaclass=BaseEnumMeta):
    DISABLED = 0
    OPEN = 1
    LIMITED = 2


class GroupsGroupBanInfo(BaseModel):
    """Model: `GroupsGroupBanInfo`"""

    comment: str | None = Field(
        default=None,
    )
    """Ban comment."""

    end_date: datetime.datetime | None = Field(
        default=None,
    )
    """End date of ban in Unixtime."""

    reason: "GroupsBanInfoReason | None" = Field(
        default=None,
    )
    """Property `GroupsGroupBanInfo.reason`."""


class GroupsGroupCategory(BaseModel):
    """Model: `GroupsGroupCategory`"""

    id: int = Field()
    """Category ID."""

    name: str = Field()
    """Category name."""

    subcategories: list["GroupsGroupSubcategory"] | None = Field(
        default=None,
    )
    """Property `GroupsGroupCategory.subcategories`."""


class GroupsGroupCategoryFull(BaseModel):
    """Model: `GroupsGroupCategoryFull`"""

    id: int = Field()
    """Category ID."""

    name: str = Field()
    """Category name."""

    page_count: int = Field()
    """Pages number."""

    page_previews: list["GroupsGroup"] = Field()
    """Property `GroupsGroupCategoryFull.page_previews`."""

    subcategories: list["GroupsGroupCategory"] | None = Field(
        default=None,
    )
    """Property `GroupsGroupCategoryFull.subcategories`."""


class GroupsGroupCategoryType(BaseModel):
    """Model: `GroupsGroupCategoryType`"""

    id: int = Field()
    """Property `GroupsGroupCategoryType.id`."""

    name: str = Field()
    """Property `GroupsGroupCategoryType.name`."""


class GroupsGroupDocs(IntEnum, metaclass=BaseEnumMeta):
    DISABLED = 0
    OPEN = 1
    LIMITED = 2


class GroupsGroupFullAgeLimits(IntEnum, metaclass=BaseEnumMeta):
    NO = 1
    OVER_16 = 2
    OVER_18 = 3


class GroupsGroupFullMemberStatus(IntEnum, metaclass=BaseEnumMeta):
    NOT_A_MEMBER = 0
    MEMBER = 1
    NOT_SURE = 2
    DECLINED = 3
    HAS_SENT_A_REQUEST = 4
    INVITED = 5


class GroupsGroupFullSection(IntEnum, metaclass=BaseEnumMeta):
    NONE = 0
    PHOTOS = 1
    TOPICS = 2
    AUDIOS = 3
    VIDEOS = 4
    MARKET = 5
    STORIES = 6
    APPS = 7
    FOLLOWERS = 8
    LINKS = 9
    EVENTS = 10
    PLACES = 11
    CONTACTS = 12
    APP_BTNS = 13
    DOCS = 14
    EVENT_COUNTERS = 15
    GROUP_MESSAGES = 16
    ALBUMS = 24
    CATEGORIES = 26
    ADMIN_HELP = 27
    APP_WIDGET = 31
    PUBLIC_HELP = 32
    HS_DONATION_APP = 33
    HS_MARKET_APP = 34
    ADDRESSES = 35
    ARTIST_PAGE = 36
    PODCAST = 37
    ARTICLES = 39
    ADMIN_TIPS = 40
    MENU = 41
    FIXED_POST = 42
    CHATS = 43
    EVERGREEN_NOTICE = 44
    MUSICIANS = 45
    NARRATIVES = 46
    DONUT_DONATE = 47
    CLIPS = 48
    MARKET_CART = 49
    CURATORS = 50
    MARKET_SERVICES = 51
    CLASSIFIEDS = 53
    TEXTLIVES = 54
    DONUT_FOR_DONS = 55
    BADGES = 57
    CHATS_CREATION = 58
    STREAM_CREATION = 59
    RATING = 60
    SERVICE_RATING = 61
    RECOMMENDED_TIPS_WIDGET = 62


class GroupsGroupIsClosed(IntEnum, metaclass=BaseEnumMeta):
    OPEN = 0
    CLOSED = 1
    PRIVATE = 2


class GroupsGroupMarketCurrency(IntEnum, metaclass=BaseEnumMeta):
    RUSSIAN_RUBLES = 643
    UKRAINIAN_HRYVNIA = 980
    KAZAKH_TENGE = 398
    EURO = 978
    US_DOLLARS = 840


class GroupsGroupPhotos(IntEnum, metaclass=BaseEnumMeta):
    DISABLED = 0
    OPEN = 1
    LIMITED = 2


class GroupsGroupPublicCategoryList(BaseModel):
    """Model: `GroupsGroupPublicCategoryList`"""

    id: int | None = Field(
        default=None,
    )
    """Property `GroupsGroupPublicCategoryList.id`."""

    name: str | None = Field(
        default=None,
    )
    """Property `GroupsGroupPublicCategoryList.name`."""

    subcategories: list["GroupsGroupCategoryType"] | None = Field(
        default=None,
    )
    """Property `GroupsGroupPublicCategoryList.subcategories`."""


class GroupsGroupRole(StrEnum, metaclass=BaseEnumMeta):
    MODERATOR = "moderator"
    EDITOR = "editor"
    ADMINISTRATOR = "administrator"
    ADVERTISER = "advertiser"


class GroupsGroupSubcategory(BaseModel):
    """Model: `GroupsGroupSubcategory`"""

    id: int = Field()
    """Object ID."""

    name: str = Field()
    """Object name."""

    genders: list["BaseObjectWithName"] | None = Field(
        default=None,
    )
    """Property `GroupsGroupSubcategory.genders`."""


class GroupsGroupSubject(IntEnum, metaclass=BaseEnumMeta):
    AUTO = 1
    ACTIVITY_HOLIDAYS = 2
    BUSINESS = 3
    PETS = 4
    HEALTH = 5
    DATING_AND_COMMUNICATION = 6
    GAMES = 7
    IT = 8
    CINEMA = 9
    BEAUTY_AND_FASHION = 10
    COOKING = 11
    ART_AND_CULTURE = 12
    LITERATURE = 13
    MOBILE_SERVICES_AND_INTERNET = 14
    MUSIC = 15
    SCIENCE_AND_TECHNOLOGY = 16
    REAL_ESTATE = 17
    NEWS_AND_MEDIA = 18
    SECURITY = 19
    EDUCATION = 20
    HOME_AND_RENOVATIONS = 21
    POLITICS = 22
    FOOD = 23
    INDUSTRY = 24
    TRAVEL = 25
    WORK = 26
    ENTERTAINMENT = 27
    RELIGION = 28
    FAMILY = 29
    SPORTS = 30
    INSURANCE = 31
    TELEVISION = 32
    GOODS_AND_SERVICES = 33
    HOBBIES = 34
    FINANCE = 35
    PHOTO = 36
    ESOTERICS = 37
    ELECTRONICS_AND_APPLIANCES = 38
    EROTIC = 39
    HUMOR = 40
    SOCIETY_HUMANITIES = 41
    DESIGN_AND_GRAPHICS = 42


class GroupsGroupSuggestedPrivacy(IntEnum, metaclass=BaseEnumMeta):
    NONE = 0
    ALL = 1
    SUBSCRIBERS = 2


class GroupsGroupTagColor(StrEnum, metaclass=BaseEnumMeta):
    f__454647 = "454647"
    f__45678f = "45678f"
    f__4bb34b = "4bb34b"
    f__5181b8 = "5181b8"
    f__539b9c = "539b9c"
    f__5c9ce6 = "5c9ce6"
    f__63b9ba = "63b9ba"
    f__6bc76b = "6bc76b"
    f__76787a = "76787a"
    f__792ec0 = "792ec0"
    f__7a6c4f = "7a6c4f"
    f__7ececf = "7ececf"
    f__9e8d6b = "9e8d6b"
    A162DE = "a162de"
    AAAEB3 = "aaaeb3"
    BBAA84 = "bbaa84"
    E64646 = "e64646"
    FF5C5C = "ff5c5c"
    FFA000 = "ffa000"
    FFC107 = "ffc107"


class GroupsGroupTag(BaseModel):
    """Model: `GroupsGroupTag`"""

    id: int = Field()
    """Property `GroupsGroupTag.id`."""

    name: str = Field()
    """Property `GroupsGroupTag.name`."""

    color: "GroupsGroupTagColor" = Field()
    """Property `GroupsGroupTag.color`."""

    uses: int | None = Field(
        default=None,
    )
    """Property `GroupsGroupTag.uses`."""


class GroupsGroupTopics(IntEnum, metaclass=BaseEnumMeta):
    DISABLED = 0
    OPEN = 1
    LIMITED = 2


class GroupsGroupType(StrEnum, metaclass=BaseEnumMeta):
    GROUP = "group"
    PAGE = "page"
    EVENT = "event"


class GroupsGroupVideo(IntEnum, metaclass=BaseEnumMeta):
    DISABLED = 0
    OPEN = 1
    LIMITED = 2


class GroupsGroupWall(IntEnum, metaclass=BaseEnumMeta):
    DISABLED = 0
    OPEN = 1
    LIMITED = 2
    CLOSED = 3


class GroupsGroupWiki(IntEnum, metaclass=BaseEnumMeta):
    DISABLED = 0
    OPEN = 1
    LIMITED = 2


class GroupsGroupsArray(BaseModel):
    """Model: `GroupsGroupsArray`"""

    count: int = Field()
    """Communities number."""

    items: list[int] = Field()
    """Property `GroupsGroupsArray.items`."""


class GroupsLinksItem(BaseModel):
    """Model: `GroupsLinksItem`"""

    name: str | None = Field(
        default=None,
    )
    """Link title."""

    desc: str | None = Field(
        default=None,
    )
    """Link description."""

    edit_title: bool | None = Field(
        default=None,
    )
    """Information whether the link title can be edited."""

    id: int | None = Field(
        default=None,
    )
    """Link ID."""

    photo_100: str | None = Field(
        default=None,
    )
    """URL of square image of the link with 100 pixels in width."""

    photo_50: str | None = Field(
        default=None,
    )
    """URL of square image of the link with 50 pixels in width."""

    url: str | None = Field(
        default=None,
    )
    """Link URL."""

    image_processing: bool | None = Field(
        default=None,
    )
    """Information whether the image on processing."""


class GroupsLiveCovers(BaseModel):
    """Model: `GroupsLiveCovers`"""

    is_enabled: bool = Field()
    """Information whether live covers is enabled."""

    is_scalable: bool | None = Field(
        default=None,
    )
    """Information whether live covers photo scaling is enabled."""

    story_ids: list[str] | None = Field(
        default=None,
    )
    """Property `GroupsLiveCovers.story_ids`."""


class GroupsLongPollEvents(BaseModel):
    """Model: `GroupsLongPollEvents`"""

    audio_new: bool = Field()
    """Property `GroupsLongPollEvents.audio_new`."""

    board_post_delete: bool = Field()
    """Property `GroupsLongPollEvents.board_post_delete`."""

    board_post_edit: bool = Field()
    """Property `GroupsLongPollEvents.board_post_edit`."""

    board_post_new: bool = Field()
    """Property `GroupsLongPollEvents.board_post_new`."""

    board_post_restore: bool = Field()
    """Property `GroupsLongPollEvents.board_post_restore`."""

    group_change_photo: bool = Field()
    """Property `GroupsLongPollEvents.group_change_photo`."""

    group_change_settings: bool = Field()
    """Property `GroupsLongPollEvents.group_change_settings`."""

    group_join: bool = Field()
    """Property `GroupsLongPollEvents.group_join`."""

    group_leave: bool = Field()
    """Property `GroupsLongPollEvents.group_leave`."""

    group_officers_edit: bool = Field()
    """Property `GroupsLongPollEvents.group_officers_edit`."""

    market_comment_delete: bool = Field()
    """Property `GroupsLongPollEvents.market_comment_delete`."""

    market_comment_edit: bool = Field()
    """Property `GroupsLongPollEvents.market_comment_edit`."""

    market_comment_new: bool = Field()
    """Property `GroupsLongPollEvents.market_comment_new`."""

    market_comment_restore: bool = Field()
    """Property `GroupsLongPollEvents.market_comment_restore`."""

    message_allow: bool = Field()
    """Property `GroupsLongPollEvents.message_allow`."""

    message_deny: bool = Field()
    """Property `GroupsLongPollEvents.message_deny`."""

    message_new: bool = Field()
    """Property `GroupsLongPollEvents.message_new`."""

    message_read: bool = Field()
    """Property `GroupsLongPollEvents.message_read`."""

    message_reply: bool = Field()
    """Property `GroupsLongPollEvents.message_reply`."""

    message_typing_state: bool = Field()
    """Property `GroupsLongPollEvents.message_typing_state`."""

    message_edit: bool = Field()
    """Property `GroupsLongPollEvents.message_edit`."""

    photo_comment_delete: bool = Field()
    """Property `GroupsLongPollEvents.photo_comment_delete`."""

    photo_comment_edit: bool = Field()
    """Property `GroupsLongPollEvents.photo_comment_edit`."""

    photo_comment_new: bool = Field()
    """Property `GroupsLongPollEvents.photo_comment_new`."""

    photo_comment_restore: bool = Field()
    """Property `GroupsLongPollEvents.photo_comment_restore`."""

    photo_new: bool = Field()
    """Property `GroupsLongPollEvents.photo_new`."""

    poll_vote_new: bool = Field()
    """Property `GroupsLongPollEvents.poll_vote_new`."""

    user_block: bool = Field()
    """Property `GroupsLongPollEvents.user_block`."""

    user_unblock: bool = Field()
    """Property `GroupsLongPollEvents.user_unblock`."""

    video_comment_delete: bool = Field()
    """Property `GroupsLongPollEvents.video_comment_delete`."""

    video_comment_edit: bool = Field()
    """Property `GroupsLongPollEvents.video_comment_edit`."""

    video_comment_new: bool = Field()
    """Property `GroupsLongPollEvents.video_comment_new`."""

    video_comment_restore: bool = Field()
    """Property `GroupsLongPollEvents.video_comment_restore`."""

    video_new: bool = Field()
    """Property `GroupsLongPollEvents.video_new`."""

    message_reaction_event: bool = Field()
    """Property `GroupsLongPollEvents.message_reaction_event`."""

    wall_post_new: bool = Field()
    """Property `GroupsLongPollEvents.wall_post_new`."""

    wall_reply_delete: bool = Field()
    """Property `GroupsLongPollEvents.wall_reply_delete`."""

    wall_reply_edit: bool = Field()
    """Property `GroupsLongPollEvents.wall_reply_edit`."""

    wall_reply_new: bool = Field()
    """Property `GroupsLongPollEvents.wall_reply_new`."""

    wall_reply_restore: bool = Field()
    """Property `GroupsLongPollEvents.wall_reply_restore`."""

    wall_repost: bool = Field()
    """Property `GroupsLongPollEvents.wall_repost`."""

    wall_schedule_post_new: bool = Field()
    """Property `GroupsLongPollEvents.wall_schedule_post_new`."""

    wall_schedule_post_delete: bool = Field()
    """Property `GroupsLongPollEvents.wall_schedule_post_delete`."""

    donut_subscription_create: bool = Field()
    """Property `GroupsLongPollEvents.donut_subscription_create`."""

    donut_subscription_prolonged: bool = Field()
    """Property `GroupsLongPollEvents.donut_subscription_prolonged`."""

    donut_subscription_cancelled: bool = Field()
    """Property `GroupsLongPollEvents.donut_subscription_cancelled`."""

    donut_subscription_expired: bool = Field()
    """Property `GroupsLongPollEvents.donut_subscription_expired`."""

    donut_subscription_price_changed: bool = Field()
    """Property `GroupsLongPollEvents.donut_subscription_price_changed`."""

    donut_money_withdraw: bool = Field()
    """Property `GroupsLongPollEvents.donut_money_withdraw`."""

    donut_money_withdraw_error: bool = Field()
    """Property `GroupsLongPollEvents.donut_money_withdraw_error`."""

    lead_forms_new: bool | None = Field(
        default=None,
    )
    """Property `GroupsLongPollEvents.lead_forms_new`."""

    market_order_new: bool | None = Field(
        default=None,
    )
    """Property `GroupsLongPollEvents.market_order_new`."""

    market_order_edit: bool | None = Field(
        default=None,
    )
    """Property `GroupsLongPollEvents.market_order_edit`."""


class GroupsLongPollServer(BaseModel):
    """Model: `GroupsLongPollServer`"""

    key: str = Field()
    """Long Poll key."""

    server: str = Field()
    """Long Poll server address."""

    ts: str = Field()
    """Number of the last event."""


class GroupsLongPollSettings(BaseModel):
    """Model: `GroupsLongPollSettings`"""

    events: "GroupsLongPollEvents" = Field()
    """Property `GroupsLongPollSettings.events`."""

    is_enabled: bool = Field()
    """Shows whether Long Poll is enabled."""

    api_version: str | None = Field(
        default=None,
    )
    """API version used for the events."""


class GroupsMarketInfo(BaseModel):
    """Model: `GroupsMarketInfo`"""

    type: str | None = Field(
        default=None,
    )
    """Market type."""

    contact_id: int | None = Field(
        default=None,
    )
    """Contact person ID."""

    currency: "MarketCurrency | None" = Field(
        default=None,
    )
    """Property `GroupsMarketInfo.currency`."""

    currency_text: str | None = Field(
        default=None,
    )
    """Currency name."""

    enabled: bool | None = Field(
        default=None,
    )
    """Information whether the market is enabled."""

    main_album_id: int | None = Field(
        default=None,
    )
    """Main market album ID."""

    price_max: str | None = Field(
        default=None,
    )
    """Maximum price."""

    price_min: str | None = Field(
        default=None,
    )
    """Minimum price."""

    min_order_price: "MarketPrice | None" = Field(
        default=None,
    )
    """Property `GroupsMarketInfo.min_order_price`."""


class GroupsMarketProperties(BaseModel):
    """Model: `GroupsMarketProperties`"""

    market: "GroupsMarketInfo | None" = Field(
        default=None,
    )
    """Property `GroupsMarketProperties.market`."""

    has_market_app: bool | None = Field(
        default=None,
    )
    """Information whether community has installed market app."""

    using_vkpay_market_app: bool | None = Field(
        default=None,
    )
    """Property `GroupsMarketProperties.using_vkpay_market_app`."""


class GroupsMarketState(StrEnum, metaclass=BaseEnumMeta):
    NONE = "none"
    BASIC = "basic"
    ADVANCED = "advanced"


class GroupsMemberRole(BaseModel):
    """Model: `GroupsMemberRole`"""

    id: int = Field()
    """User ID."""

    is_call_operator: bool | None = Field(
        default=None,
    )
    """Allow the manager to accept community calls.."""

    permissions: list["GroupsMemberRolePermission"] | None = Field(
        default=None,
    )
    """Property `GroupsMemberRole.permissions`."""

    role: "GroupsMemberRoleStatus | None" = Field(
        default=None,
    )
    """Property `GroupsMemberRole.role`."""


class GroupsMemberRolePermission(StrEnum, metaclass=BaseEnumMeta):
    ADS = "ads"


class GroupsMemberRoleStatus(StrEnum, metaclass=BaseEnumMeta):
    MODERATOR = "moderator"
    EDITOR = "editor"
    ADMINISTRATOR = "administrator"
    CREATOR = "creator"
    ADVERTISER = "advertiser"


class GroupsMemberStatus(BaseModel):
    """Model: `GroupsMemberStatus`"""

    member: bool = Field()
    """Information whether user is a member of the group."""

    user_id: int = Field()
    """User ID."""


class GroupsMemberStatusFull(BaseModel):
    """Model: `GroupsMemberStatusFull`"""

    member: bool = Field()
    """Information whether user is a member of the group."""

    user_id: int = Field()
    """User ID."""

    can_invite: bool | None = Field(
        default=None,
    )
    """Information whether user can be invited."""

    can_recall: bool | None = Field(
        default=None,
    )
    """Information whether user\'s invite to the group can be recalled."""

    invitation: bool | None = Field(
        default=None,
    )
    """Information whether user has been invited to the group."""

    request: bool | None = Field(
        default=None,
    )
    """Information whether user has send request to the group."""


class GroupsOnlineStatus(BaseModel):
    """Online status of group
    Model: `GroupsOnlineStatus`
    """

    status: "GroupsOnlineStatusType" = Field()
    """Property `GroupsOnlineStatus.status`."""

    minutes: int | None = Field(
        default=None,
    )
    """Estimated time of answer (for status = answer_mark)."""


class GroupsOnlineStatusType(StrEnum, metaclass=BaseEnumMeta):
    NONE = "none"
    ONLINE = "online"
    ANSWER_MARK = "answer_mark"


class GroupsOwnerXtrBanInfoType(StrEnum, metaclass=BaseEnumMeta):
    GROUP = "group"
    PROFILE = "profile"


class GroupsOwnerXtrBanInfo(BaseModel):
    """Model: `GroupsOwnerXtrBanInfo`"""

    ban_info: "GroupsBanInfo | None" = Field(
        default=None,
    )
    """Property `GroupsOwnerXtrBanInfo.ban_info`."""

    group: "GroupsGroup | None" = Field(
        default=None,
    )
    """Information about group if type = group."""

    profile: "UsersUser | None" = Field(
        default=None,
    )
    """Information about group if type = profile."""

    type: "GroupsOwnerXtrBanInfoType | None" = Field(
        default=None,
    )
    """Property `GroupsOwnerXtrBanInfo.type`."""


class GroupsPhotoSize(BaseModel):
    """Model: `GroupsPhotoSize`"""

    height: int = Field()
    """Image height."""

    width: int = Field()
    """Image width."""


class GroupsProfileItem(BaseModel):
    """Model: `GroupsProfileItem`"""

    id: int = Field()
    """User id."""

    photo_50: str = Field()
    """Url for user photo."""

    photo_100: str = Field()
    """Url for user photo."""

    first_name: str = Field()
    """User first name."""

    last_name: str | None = Field(
        default=None,
    )
    """User last name."""

    screen_name: str | None = Field(
        default=None,
    )
    """Domain of the user page."""


class GroupsRoleOptions(StrEnum, metaclass=BaseEnumMeta):
    MODERATOR = "moderator"
    EDITOR = "editor"
    ADMINISTRATOR = "administrator"
    CREATOR = "creator"


class GroupsSectionsListItem(BaseModel):
    """Model: `GroupsSectionsListItem`"""

    id: int = Field()
    """Object ID."""

    title: str = Field()
    """Object title."""


class GroupsSettingsTwitterStatus(StrEnum, metaclass=BaseEnumMeta):
    LOADING = "loading"
    SYNC = "sync"


class GroupsSettingsTwitter(BaseModel):
    """Model: `GroupsSettingsTwitter`"""

    status: "GroupsSettingsTwitterStatus" = Field()
    """Property `GroupsSettingsTwitter.status`."""

    name: str | None = Field(
        default=None,
    )
    """Property `GroupsSettingsTwitter.name`."""


class GroupsSubjectItem(BaseModel):
    """Model: `GroupsSubjectItem`"""

    id: int = Field()
    """Subject ID."""

    name: str = Field()
    """Subject title."""


class GroupsTokenPermissionSetting(BaseModel):
    """Model: `GroupsTokenPermissionSetting`"""

    name: str = Field()
    """Property `GroupsTokenPermissionSetting.name`."""

    setting: int = Field()
    """Property `GroupsTokenPermissionSetting.setting`."""


class LeadFormsAnswer(BaseModel):
    """Model: `LeadFormsAnswer`"""

    key: str = Field()
    """Property `LeadFormsAnswer.key`."""

    answer: "LeadFormsAnswerOneOf" = Field()
    """Property `LeadFormsAnswer.answer`."""


class LeadFormsAnswerItem(BaseModel):
    """Model: `LeadFormsAnswerItem`"""

    value: str = Field()
    """Property `LeadFormsAnswerItem.value`."""

    key: str | None = Field(
        default=None,
    )
    """Property `LeadFormsAnswerItem.key`."""


class LeadFormsAnswerOneOf(BaseModel):
    """Model: `LeadFormsAnswerOneOf`"""


class LeadFormsForm(BaseModel):
    """Model: `LeadFormsForm`"""

    form_id: int = Field()
    """Property `LeadFormsForm.form_id`."""

    group_id: int = Field()
    """Property `LeadFormsForm.group_id`."""

    leads_count: int = Field()
    """Property `LeadFormsForm.leads_count`."""

    url: str = Field()
    """Property `LeadFormsForm.url`."""

    photo: str | None = Field(
        default=None,
    )
    """Property `LeadFormsForm.photo`."""

    name: str | None = Field(
        default=None,
    )
    """Property `LeadFormsForm.name`."""

    title: str | None = Field(
        default=None,
    )
    """Property `LeadFormsForm.title`."""

    description: str | None = Field(
        default=None,
    )
    """Property `LeadFormsForm.description`."""

    confirmation: str | None = Field(
        default=None,
    )
    """Property `LeadFormsForm.confirmation`."""

    site_link_url: str | None = Field(
        default=None,
    )
    """Property `LeadFormsForm.site_link_url`."""

    policy_link_url: str | None = Field(
        default=None,
    )
    """Property `LeadFormsForm.policy_link_url`."""

    questions: list["LeadFormsQuestionItem"] | None = Field(
        default=None,
    )
    """Property `LeadFormsForm.questions`."""

    active: bool | None = Field(
        default=None,
    )
    """Property `LeadFormsForm.active`."""

    pixel_code: str | None = Field(
        default=None,
    )
    """Property `LeadFormsForm.pixel_code`."""

    once_per_user: int | None = Field(
        default=None,
    )
    """Property `LeadFormsForm.once_per_user`."""

    notify_admins: str | None = Field(
        default=None,
    )
    """Property `LeadFormsForm.notify_admins`."""

    notify_emails: str | None = Field(
        default=None,
    )
    """Property `LeadFormsForm.notify_emails`."""


class LeadFormsLead(BaseModel):
    """Model: `LeadFormsLead`"""

    lead_id: int = Field()
    """Property `LeadFormsLead.lead_id`."""

    user_id: int = Field()
    """Property `LeadFormsLead.user_id`."""

    date: datetime.datetime = Field()
    """Property `LeadFormsLead.date`."""

    answers: list["LeadFormsAnswer"] = Field()
    """Property `LeadFormsLead.answers`."""

    ad_id: int | None = Field(
        default=None,
    )
    """Property `LeadFormsLead.ad_id`."""


class LeadFormsQuestionItemType(StrEnum, metaclass=BaseEnumMeta):
    INPUT = "input"
    TEXTAREA = "textarea"
    RADIO = "radio"
    CHECKBOX = "checkbox"
    SELECT = "select"


class LeadFormsQuestionItem(BaseModel):
    """Model: `LeadFormsQuestionItem`"""

    key: str = Field()
    """Property `LeadFormsQuestionItem.key`."""

    type: "LeadFormsQuestionItemType" = Field()
    """Property `LeadFormsQuestionItem.type`."""

    label: str | None = Field(
        default=None,
    )
    """Property `LeadFormsQuestionItem.label`."""

    options: list["LeadFormsQuestionItemOption"] | None = Field(
        default=None,
    )
    """Опции выбора для типов radio, checkbox, select."""


class LeadFormsQuestionItemOption(BaseModel):
    """Model: `LeadFormsQuestionItemOption`"""

    label: str = Field()
    """Property `LeadFormsQuestionItemOption.label`."""

    key: str | None = Field(
        default=None,
    )
    """Property `LeadFormsQuestionItemOption.key`."""


class LikesType(StrEnum, metaclass=BaseEnumMeta):
    POST = "post"
    COMMENT = "comment"
    PHOTO = "photo"
    AUDIO = "audio"
    VIDEO = "video"
    NOTE = "note"
    MARKET = "market"
    PHOTO_COMMENT = "photo_comment"
    VIDEO_COMMENT = "video_comment"
    TOPIC_COMMENT = "topic_comment"
    MARKET_COMMENT = "market_comment"
    SITEPAGE = "sitepage"
    TEXTPOST = "textpost"
    COMMUNITY_REVIEW = "community_review"
    STORY = "story"
    GROUP_LIKE = "group_like"


class LinkTargetObject(BaseModel):
    """Model: `LinkTargetObject`"""

    type: str | None = Field(
        default=None,
    )
    """Object type."""

    owner_id: int | None = Field(
        default=None,
    )
    """Owner ID."""

    item_id: int | None = Field(
        default=None,
    )
    """Item ID."""


class MarketCurrency(BaseModel):
    """Model: `MarketCurrency`"""

    id: int = Field()
    """Currency ID."""

    name: str = Field()
    """Currency sign."""

    title: str = Field()
    """Currency title."""


class MarketGlobalSearchFilters(BaseModel):
    """Model: `MarketGlobalSearchFilters`"""

    city: "BaseCity | None" = Field(
        default=None,
    )
    """Property `MarketGlobalSearchFilters.city`."""

    country: "BaseCountry | None" = Field(
        default=None,
    )
    """Property `MarketGlobalSearchFilters.country`."""


class MarketItemOwnerInfo(BaseModel):
    """Information about the group where the item is placed
    Model: `MarketItemOwnerInfo`
    """

    avatar: list["BaseImage"] | None = Field(
        default=None,
    )
    """Avatar of the group."""

    name: str | None = Field(
        default=None,
    )
    """Name of the group."""

    category: str | None = Field(
        default=None,
    )
    """Category of the item or description of the group."""

    category_url: str | None = Field(
        default=None,
    )
    """Link to the section of the group."""

    is_corporated_market: bool | None = Field(
        default=None,
    )
    """Is the group is VK corporated market."""

    market_type: "MarketOwnerType | None" = Field(
        default=None,
    )
    """Type of the market group."""


class MarketItemPromotionInfo(BaseModel):
    """Information about promotion of the market item
    Model: `MarketItemPromotionInfo`
    """

    is_available: bool | None = Field(
        default=None,
    )
    """Can the item be promoted?."""


class MarketMarketAlbum(BaseModel):
    """Model: `MarketMarketAlbum`"""

    id: int = Field()
    """Market album ID."""

    owner_id: int = Field()
    """Market album owner\'s ID."""

    title: str = Field()
    """Market album title."""

    count: int = Field()
    """Items number."""

    updated_time: int = Field()
    """Date when album has been updated last time in Unixtime."""

    is_main: bool | None = Field(
        default=None,
    )
    """Is album main for owner."""

    is_hidden: bool | None = Field(
        default=None,
    )
    """Is album hidden."""

    photo: "PhotosPhoto | None" = Field(
        default=None,
    )
    """Property `MarketMarketAlbum.photo`."""

    type: int | None = Field(
        default=None,
    )
    """Type of album."""

    is_blur_enabled: bool | None = Field(
        default=None,
    )
    """Is album needed to be blurred (18+) or not."""


class MarketMarketCategoryInnerType(StrEnum, metaclass=BaseEnumMeta):
    MARKET_MARKET_CATEGORY_NESTED = "market_market_category_nested"


class MarketMarketCategory(BaseModel):
    """Model: `MarketMarketCategory`"""

    inner_type: "MarketMarketCategoryInnerType" = Field()
    """Property `MarketMarketCategory.inner_type`."""

    id: int = Field()
    """Category ID."""

    name: str = Field()
    """Category name."""

    is_v2: bool | None = Field(
        default=None,
    )
    """Is v2 category."""

    parent: "MarketMarketCategoryNested | None" = Field(
        default=None,
    )
    """Property `MarketMarketCategory.parent`."""


class MarketMarketCategoryNestedInnerType(StrEnum, metaclass=BaseEnumMeta):
    MARKET_MARKET_CATEGORY_NESTED = "market_market_category_nested"


class MarketMarketCategoryNested(BaseModel):
    """Model: `MarketMarketCategoryNested`"""

    inner_type: "MarketMarketCategoryNestedInnerType" = Field()
    """Property `MarketMarketCategoryNested.inner_type`."""

    id: int = Field()
    """Category ID."""

    name: str = Field()
    """Category name."""

    is_v2: bool | None = Field(
        default=None,
    )
    """Is v2 category."""

    parent: "MarketMarketCategoryNested | None" = Field(
        default=None,
    )
    """Property `MarketMarketCategoryNested.parent`."""


class MarketMarketCategoryTree(BaseModel):
    """Model: `MarketMarketCategoryTree`"""

    id: int = Field()
    """Category ID."""

    name: str = Field()
    """Category name."""

    icon_name: str | None = Field(
        default=None,
    )
    """Icon name."""

    children: list["MarketMarketCategoryTree"] | None = Field(
        default=None,
    )
    """Property `MarketMarketCategoryTree.children`."""

    view: "MarketMarketCategoryTreeView | None" = Field(
        default=None,
    )
    """Property `MarketMarketCategoryTree.view`."""

    url: str | None = Field(
        default=None,
    )
    """SEO-friendly URL to page with category\'s items."""

    seo_name: str | None = Field(
        default=None,
    )
    """SEO-friendly variant of category\'s name."""

    page_title: str | None = Field(
        default=None,
    )
    """Title for category\'s page. Used for SEO."""

    page_description: str | None = Field(
        default=None,
    )
    """Description for category\'s page. Used for SEO."""


class MarketMarketCategoryTreeViewType(StrEnum, metaclass=BaseEnumMeta):
    TAB_ROOT = "tab_root"


class MarketMarketCategoryTreeView(BaseModel):
    """Model: `MarketMarketCategoryTreeView`"""

    type: "MarketMarketCategoryTreeViewType | None" = Field(
        default=None,
    )
    """Property `MarketMarketCategoryTreeView.type`."""

    selected: bool | None = Field(
        default=None,
    )
    """Property `MarketMarketCategoryTreeView.selected`."""

    root_path: list[str] | None = Field(
        default=None,
    )
    """Property `MarketMarketCategoryTreeView.root_path`."""


class MarketMarketItem(BaseModel):
    """Model: `MarketMarketItem`"""

    availability: "MarketMarketItemAvailability" = Field()
    """Property `MarketMarketItem.availability`."""

    category: "MarketMarketCategory" = Field()
    """Property `MarketMarketItem.category`."""

    description: str = Field()
    """Item description."""

    id: int = Field()
    """Item ID."""

    owner_id: int = Field()
    """Item owner\'s ID."""

    price: "MarketPrice" = Field()
    """Property `MarketMarketItem.price`."""

    title: str = Field()
    """Item title."""

    access_key: str | None = Field(
        default=None,
    )
    """Access key for the market item."""

    button_title: str | None = Field(
        default=None,
    )
    """Title for button for url."""

    category_v2: "MarketMarketCategory | None" = Field(
        default=None,
    )
    """Property `MarketMarketItem.category_v2`."""

    date: datetime.datetime | None = Field(
        default=None,
    )
    """Date when the item has been created in Unixtime."""

    external_id: str | None = Field(
        default=None,
    )
    """Property `MarketMarketItem.external_id`."""

    is_favorite: bool | None = Field(
        default=None,
    )
    """Property `MarketMarketItem.is_favorite`."""

    is_owner: bool | None = Field(
        default=None,
    )
    """Property `MarketMarketItem.is_owner`."""

    is_adult: bool | None = Field(
        default=None,
    )
    """Property `MarketMarketItem.is_adult`."""

    thumb_photo: str | None = Field(
        default=None,
    )
    """URL of the preview image."""

    url: str | None = Field(
        default=None,
    )
    """URL to item."""

    variants_grouping_id: int | None = Field(
        default=None,
    )
    """Property `MarketMarketItem.variants_grouping_id`."""

    is_main_variant: bool | None = Field(
        default=None,
    )
    """Property `MarketMarketItem.is_main_variant`."""

    sku: str | None = Field(
        default=None,
    )
    """Property `MarketMarketItem.sku`."""

    stock_amount: int | None = Field(
        default=None,
    )
    """Inventory balances."""

    post_id: int | None = Field(
        default=None,
    )
    """Attach for post id."""

    post_owner_id: int | None = Field(
        default=None,
    )
    """Attach for post owner id."""


class MarketMarketItemAvailability(IntEnum, metaclass=BaseEnumMeta):
    AVAILABLE = 0
    REMOVED = 1
    UNAVAILABLE = 2


class MarketMarketItemBasic(BaseModel):
    """Model: `MarketMarketItemBasic`"""

    id: int = Field()
    """Item ID."""

    owner_id: int = Field()
    """Item owner\'s ID."""

    title: str = Field()
    """Item title."""

    price: "MarketPrice" = Field()
    """Property `MarketMarketItemBasic.price`."""

    thumb_photo: str | None = Field(
        default=None,
    )
    """URL of the preview image."""

    is_favorite: bool | None = Field(
        default=None,
    )
    """Property `MarketMarketItemBasic.is_favorite`."""


class MarketOrder(BaseModel):
    """Model: `MarketOrder`"""

    id: int = Field()
    """Property `MarketOrder.id`."""

    group_id: int = Field()
    """Property `MarketOrder.group_id`."""

    user_id: int = Field()
    """Property `MarketOrder.user_id`."""

    date: datetime.datetime = Field()
    """Property `MarketOrder.date`."""

    status: int = Field()
    """Property `MarketOrder.status`."""

    items_count: int = Field()
    """Property `MarketOrder.items_count`."""

    total_price: "MarketPrice" = Field()
    """Property `MarketOrder.total_price`."""

    display_order_id: str | None = Field(
        default=None,
    )
    """Property `MarketOrder.display_order_id`."""

    track_number: str | None = Field(
        default=None,
    )
    """Property `MarketOrder.track_number`."""

    track_link: str | None = Field(
        default=None,
    )
    """Property `MarketOrder.track_link`."""

    comment: str | None = Field(
        default=None,
    )
    """Property `MarketOrder.comment`."""

    address: str | None = Field(
        default=None,
    )
    """Property `MarketOrder.address`."""

    merchant_comment: str | None = Field(
        default=None,
    )
    """Property `MarketOrder.merchant_comment`."""

    weight: int | None = Field(
        default=None,
    )
    """Property `MarketOrder.weight`."""

    discount: "MarketPrice | None" = Field(
        default=None,
    )
    """Property `MarketOrder.discount`."""

    preview_order_items: list["MarketOrderItem"] | None = Field(
        default=None,
    )
    """Several order items for preview."""

    cancel_info: "BaseLink | None" = Field(
        default=None,
    )
    """Information for cancel and revert order."""

    comment_for_user: str | None = Field(
        default=None,
    )
    """Seller comment for user."""

    is_viewed_by_admin: bool | None = Field(
        default=None,
    )
    """Property `MarketOrder.is_viewed_by_admin`."""

    date_viewed: int | None = Field(
        default=None,
    )
    """Property `MarketOrder.date_viewed`."""

    can_add_review: bool | None = Field(
        default=None,
    )
    """Extended field. Can current viewer add review for at least one item in this order."""


class MarketOrderItem(BaseModel):
    """Model: `MarketOrderItem`"""

    owner_id: int = Field()
    """Property `MarketOrderItem.owner_id`."""

    item_id: int = Field()
    """Property `MarketOrderItem.item_id`."""

    price: "MarketPrice" = Field()
    """Property `MarketOrderItem.price`."""

    quantity: int = Field()
    """Property `MarketOrderItem.quantity`."""

    item: "MarketMarketItem" = Field()
    """Property `MarketOrderItem.item`."""

    title: str | None = Field(
        default=None,
    )
    """Property `MarketOrderItem.title`."""

    photo: "PhotosPhoto | None" = Field(
        default=None,
    )
    """Property `MarketOrderItem.photo`."""

    variants: list[str] | None = Field(
        default=None,
    )
    """Property `MarketOrderItem.variants`."""

    can_add_review: bool | None = Field(
        default=None,
    )
    """Extended field. Can current viewer add review for this ordered item."""


class MarketOwnerType(StrEnum, metaclass=BaseEnumMeta):
    BASE = "base"
    PRO = "pro"
    DISABLED = "disabled"


class MarketPrice(BaseModel):
    """Model: `MarketPrice`"""

    amount: str = Field()
    """Amount."""

    currency: "MarketCurrency" = Field()
    """Property `MarketPrice.currency`."""

    text: str = Field()
    """Text."""

    amount_to: str | None = Field(
        default=None,
    )
    """Amount to for price_type=2."""

    price_type: int | None = Field(
        default=None,
    )
    """Property `MarketPrice.price_type`."""

    price_unit: int | None = Field(
        default=None,
    )
    """Property `MarketPrice.price_unit`."""

    discount_rate: int | None = Field(
        default=None,
    )
    """Property `MarketPrice.discount_rate`."""

    old_amount: str | None = Field(
        default=None,
    )
    """Property `MarketPrice.old_amount`."""

    old_amount_text: str | None = Field(
        default=None,
    )
    """Textual representation of old price."""


class MarketPropertyType(StrEnum, metaclass=BaseEnumMeta):
    TEXT = "text"
    COLOR = "color"


class MarketProperty(BaseModel):
    """Model: `MarketProperty`"""

    id: int = Field()
    """Property `MarketProperty.id`."""

    title: str = Field()
    """Property name."""

    variants: list["MarketPropertyVariant"] = Field()
    """Property `MarketProperty.variants`."""

    type: "MarketPropertyType | None" = Field(
        default=None,
    )
    """Property type."""


class MarketPropertyVariant(BaseModel):
    """Model: `MarketPropertyVariant`"""

    id: int = Field()
    """Property `MarketPropertyVariant.id`."""

    title: str = Field()
    """Property name."""

    value: str | None = Field(
        default=None,
    )
    """Property value corresponding to property type."""


class MarketServicesViewType(IntEnum, metaclass=BaseEnumMeta):
    CARDS = 1
    ROWS = 2


class MarketUploadPhotoData(BaseModel):
    """Model: `MarketUploadPhotoData`"""

    photo_id: int = Field()
    """Photo ID."""

    photo: "PhotosPhoto | None" = Field(
        default=None,
    )
    """Property `MarketUploadPhotoData.photo`."""


class NotesNote(BaseModel):
    """Model: `NotesNote`"""

    comments: int = Field()
    """Comments number."""

    date: datetime.datetime = Field()
    """Date when the note has been created in Unixtime."""

    id: int = Field()
    """Note ID."""

    owner_id: int = Field()
    """Note owner\'s ID."""

    title: str = Field()
    """Note title."""

    view_url: str = Field()
    """URL of the page with note preview."""

    read_comments: int | None = Field(
        default=None,
    )
    """Property `NotesNote.read_comments`."""

    can_comment: bool | None = Field(
        default=None,
    )
    """Information whether current user can comment the note."""

    text: str | None = Field(
        default=None,
    )
    """Note text."""

    text_wiki: str | None = Field(
        default=None,
    )
    """Note text in wiki format."""

    privacy_view: list[str] | None = Field(
        default=None,
    )
    """Property `NotesNote.privacy_view`."""

    privacy_comment: list[str] | None = Field(
        default=None,
    )
    """Property `NotesNote.privacy_comment`."""


class NotesNoteComment(BaseModel):
    """Model: `NotesNoteComment`"""

    date: datetime.datetime = Field()
    """Date when the comment has beed added in Unixtime."""

    id: int = Field()
    """Comment ID."""

    message: str = Field()
    """Comment text."""

    nid: int = Field()
    """Note ID."""

    oid: int = Field()
    """Note ID."""

    uid: int = Field()
    """Comment author\'s ID."""

    reply_to: int | None = Field(
        default=None,
    )
    """ID of replied comment ."""


class NotificationsFeedback(BaseModel):
    """Model: `NotificationsFeedback`"""

    attachments: list["WallWallpostAttachment"] | None = Field(
        default=None,
    )
    """Property `NotificationsFeedback.attachments`."""

    from_id: int | None = Field(
        default=None,
    )
    """Reply author\'s ID."""

    geo: "BaseGeo | None" = Field(
        default=None,
    )
    """Property `NotificationsFeedback.geo`."""

    id: int | None = Field(
        default=None,
    )
    """Item ID."""

    likes: "BaseLikesInfo | None" = Field(
        default=None,
    )
    """Property `NotificationsFeedback.likes`."""

    text: str | None = Field(
        default=None,
    )
    """Reply text."""

    to_id: int | None = Field(
        default=None,
    )
    """Wall owner\'s ID."""


class NotificationsNotificationInnerType(StrEnum, metaclass=BaseEnumMeta):
    NOTIFICATIONS_NOTIFICATION = "notifications_notification"


class NotificationsNotification(BaseModel):
    """Model: `NotificationsNotification`"""

    inner_type: "NotificationsNotificationInnerType" = Field()
    """Property `NotificationsNotification.inner_type`."""

    date: datetime.datetime | None = Field(
        default=None,
    )
    """Date when the event has been occurred."""

    feedback: "NotificationsFeedback | None" = Field(
        default=None,
    )
    """Property `NotificationsNotification.feedback`."""

    parent: "NotificationsNotification | None" = Field(
        default=None,
    )
    """Property `NotificationsNotification.parent`."""

    reply: "NotificationsReply | None" = Field(
        default=None,
    )
    """Property `NotificationsNotification.reply`."""

    type: str | None = Field(
        default=None,
    )
    """Notification type."""


class NotificationsNotificationItemInnerType(StrEnum, metaclass=BaseEnumMeta):
    NOTIFICATIONS_NOTIFICATION = "notifications_notification"


class NotificationsNotificationItem(BaseModel):
    """Model: `NotificationsNotificationItem`"""

    inner_type: "NotificationsNotificationItemInnerType" = Field()
    """Property `NotificationsNotificationItem.inner_type`."""

    date: datetime.datetime | None = Field(
        default=None,
    )
    """Date when the event has been occurred."""

    feedback: "NotificationsFeedback | None" = Field(
        default=None,
    )
    """Property `NotificationsNotificationItem.feedback`."""

    parent: "NotificationsNotification | None" = Field(
        default=None,
    )
    """Property `NotificationsNotificationItem.parent`."""

    reply: "NotificationsReply | None" = Field(
        default=None,
    )
    """Property `NotificationsNotificationItem.reply`."""

    type: str | None = Field(
        default=None,
    )
    """Notification type."""


class NotificationsReply(BaseModel):
    """Model: `NotificationsReply`"""

    date: datetime.datetime | None = Field(
        default=None,
    )
    """Date when the reply has been created in Unixtime."""

    id: int | None = Field(
        default=None,
    )
    """Reply ID."""

    text: int | None = Field(
        default=None,
    )
    """Reply text."""


class NotificationsSendMessageError(BaseModel):
    """Model: `NotificationsSendMessageError`"""

    code: int | None = Field(
        default=None,
    )
    """Error code."""

    description: str | None = Field(
        default=None,
    )
    """Error description."""


class NotificationsSendMessageItem(BaseModel):
    """Model: `NotificationsSendMessageItem`"""

    user_id: int | None = Field(
        default=None,
    )
    """User ID."""

    status: bool | None = Field(
        default=None,
    )
    """Notification status."""

    error: "NotificationsSendMessageError | None" = Field(
        default=None,
    )
    """Property `NotificationsSendMessageItem.error`."""


class OauthError(BaseModel):
    """Model: `OauthError`"""

    error: str = Field()
    """Error type."""

    error_description: str = Field()
    """Error description."""

    redirect_uri: str | None = Field(
        default=None,
    )
    """URI for validation."""


class OrdersAmount(BaseModel):
    """Model: `OrdersAmount`"""

    amounts: list["OrdersAmountItem"] | None = Field(
        default=None,
    )
    """Property `OrdersAmount.amounts`."""

    currency: str | None = Field(
        default=None,
    )
    """Currency name."""


class OrdersAmountItem(BaseModel):
    """Model: `OrdersAmountItem`"""

    amount: float | None = Field(
        default=None,
    )
    """Votes amount in user\'s currency."""

    description: str | None = Field(
        default=None,
    )
    """Amount description."""

    votes: str | None = Field(
        default=None,
    )
    """Votes number."""


class OrdersOrderStatus(StrEnum, metaclass=BaseEnumMeta):
    CREATED = "created"
    CHARGED = "charged"
    REFUNDED = "refunded"
    CHARGEABLE = "chargeable"
    CANCELLED = "cancelled"
    DECLINED = "declined"


class OrdersOrder(BaseModel):
    """Model: `OrdersOrder`"""

    amount: str = Field()
    """Amount."""

    app_order_id: str = Field()
    """App order ID."""

    date: str = Field()
    """Date of creation in Unixtime."""

    id: str = Field()
    """Order ID."""

    item: str = Field()
    """Order item."""

    receiver_id: str = Field()
    """Receiver ID."""

    status: "OrdersOrderStatus" = Field()
    """Order status."""

    user_id: str = Field()
    """User ID."""

    cancel_transaction_id: str | None = Field(
        default=None,
    )
    """Cancel transaction ID."""

    transaction_id: str | None = Field(
        default=None,
    )
    """Transaction ID."""


class OrdersSubscription(BaseModel):
    """Model: `OrdersSubscription`"""

    create_time: int = Field()
    """Date of creation in Unixtime."""

    id: int = Field()
    """Subscription ID."""

    item_id: str = Field()
    """Subscription order item."""

    period: int = Field()
    """Subscription period."""

    period_start_time: int = Field()
    """Date of last period start in Unixtime."""

    price: int = Field()
    """Subscription price."""

    status: str = Field()
    """Subscription status."""

    update_time: int = Field()
    """Date of last change in Unixtime."""

    cancel_reason: str | None = Field(
        default=None,
    )
    """Cancel reason."""

    next_bill_time: int | None = Field(
        default=None,
    )
    """Date of next bill in Unixtime."""

    expire_time: int | None = Field(
        default=None,
    )
    """Subscription expiration time in Unixtime."""

    pending_cancel: bool | None = Field(
        default=None,
    )
    """Pending cancel state."""

    title: str | None = Field(
        default=None,
    )
    """Subscription name."""

    app_id: int | None = Field(
        default=None,
    )
    """Subscription\'s application id."""

    application_name: str | None = Field(
        default=None,
    )
    """Subscription\'s application name."""

    photo_url: str | None = Field(
        default=None,
    )
    """Item photo image url."""

    test_mode: bool | None = Field(
        default=None,
    )
    """Is test subscription."""

    trial_expire_time: int | None = Field(
        default=None,
    )
    """Date of trial expire in Unixtime."""

    is_game: bool | None = Field(
        default=None,
    )
    """Is game (not miniapp) subscription."""


class OwnerState(BaseModel):
    """Model: `OwnerState`"""

    state: int | None = Field(
        default=None,
    )
    """Property `OwnerState.state`."""

    description: str | None = Field(
        default=None,
    )
    """wiki text to describe user state."""


class PagesPrivacySettings(IntEnum, metaclass=BaseEnumMeta):
    COMMUNITY_MANAGERS_ONLY = 0
    COMMUNITY_MEMBERS_ONLY = 1
    EVERYONE = 2


class PagesWikipage(BaseModel):
    """Model: `PagesWikipage`"""

    group_id: int = Field()
    """Community ID."""

    id: int = Field()
    """Page ID."""

    title: str = Field()
    """Page title."""

    views: int = Field()
    """Views number."""

    who_can_edit: "PagesPrivacySettings" = Field()
    """Edit settings of the page."""

    who_can_view: "PagesPrivacySettings" = Field()
    """View settings of the page."""

    created: int = Field()
    """Property `PagesWikipage.created`."""

    edited: int = Field()
    """Property `PagesWikipage.edited`."""

    creator_id: int | None = Field(
        default=None,
    )
    """Page creator ID."""

    creator_name: str | None = Field(
        default=None,
    )
    """Page creator name."""

    editor_id: int | None = Field(
        default=None,
    )
    """Last editor ID."""

    editor_name: str | None = Field(
        default=None,
    )
    """Last editor name."""


class PagesWikipageFull(BaseModel):
    """Model: `PagesWikipageFull`"""

    created: int = Field()
    """Date when the page has been created in Unixtime."""

    edited: int = Field()
    """Date when the page has been edited in Unixtime."""

    group_id: int = Field()
    """Community ID."""

    id: int = Field()
    """Page ID."""

    title: str = Field()
    """Page title."""

    view_url: str = Field()
    """URL of the page preview."""

    views: int = Field()
    """Views number."""

    who_can_edit: "PagesPrivacySettings" = Field()
    """Edit settings of the page."""

    who_can_view: "PagesPrivacySettings" = Field()
    """View settings of the page."""

    creator_id: int | None = Field(
        default=None,
    )
    """Page creator ID."""

    current_user_can_edit: bool | None = Field(
        default=None,
    )
    """Information whether current user can edit the page."""

    current_user_can_edit_access: bool | None = Field(
        default=None,
    )
    """Information whether current user can edit the page access settings."""

    editor_id: int | None = Field(
        default=None,
    )
    """Last editor ID."""

    html: str | None = Field(
        default=None,
    )
    """Page content, HTML."""

    source: str | None = Field(
        default=None,
    )
    """Page content, wiki."""

    url: str | None = Field(
        default=None,
    )
    """URL."""

    parent: str | None = Field(
        default=None,
    )
    """Parent."""

    parent2: str | None = Field(
        default=None,
    )
    """Parent2."""

    owner_id: int | None = Field(
        default=None,
    )
    """Owner ID."""


class PagesWikipageHistory(BaseModel):
    """Model: `PagesWikipageHistory`"""

    id: int = Field()
    """Version ID."""

    length: int = Field()
    """Page size in bytes."""

    date: datetime.datetime = Field()
    """Date when the page has been edited in Unixtime."""

    editor_id: int = Field()
    """Last editor ID."""

    editor_name: str = Field()
    """Last editor name."""


class PhotosImage(BaseModel):
    """Model: `PhotosImage`"""

    height: int | None = Field(
        default=None,
    )
    """Height of the photo in px.."""

    type: "PhotosImageType | None" = Field(
        default=None,
    )
    """Property `PhotosImage.type`."""

    url: str | None = Field(
        default=None,
    )
    """Photo URL.."""

    width: int | None = Field(
        default=None,
    )
    """Width of the photo in px.."""


class PhotosImageType(StrEnum, metaclass=BaseEnumMeta):
    S = "s"
    M = "m"
    X = "x"
    L = "l"
    O = "o"
    P = "p"
    Q = "q"
    R = "r"
    Y = "y"
    Z = "z"
    W = "w"
    BASE = "base"


class PhotosPhotoVerticalAlign(StrEnum, metaclass=BaseEnumMeta):
    TOP = "top"
    MIDDLE = "middle"
    BOTTOM = "bottom"


class PhotosPhoto(BaseModel):
    """Model: `PhotosPhoto`"""

    album_id: int = Field()
    """Album ID."""

    date: datetime.datetime = Field()
    """Date when uploaded."""

    id: int = Field()
    """Photo ID."""

    owner_id: int = Field()
    """Photo owner\'s ID."""

    has_tags: bool = Field()
    """Whether photo has attached tag links."""

    access_key: str | None = Field(
        default=None,
    )
    """Access key for the photo."""

    height: int | None = Field(
        default=None,
    )
    """Original photo height."""

    images: list["PhotosImage"] | None = Field(
        default=None,
    )
    """Property `PhotosPhoto.images`."""

    lat: float | None = Field(
        default=None,
    )
    """Latitude."""

    long: float | None = Field(
        default=None,
    )
    """Longitude."""

    photo_256: str | None = Field(
        default=None,
    )
    """URL of image with 2560 px width."""

    thumb_hash: str | None = Field(
        default=None,
    )
    """Thumb Hash."""

    can_comment: bool | None = Field(
        default=None,
    )
    """Information whether current user can comment the photo."""

    place: str | None = Field(
        default=None,
    )
    """Property `PhotosPhoto.place`."""

    post_id: int | None = Field(
        default=None,
    )
    """Post ID."""

    sizes: list["PhotosPhotoSizes"] | None = Field(
        default=None,
    )
    """Property `PhotosPhoto.sizes`."""

    square_crop: str | None = Field(
        default=None,
    )
    """Property `PhotosPhoto.square_crop`."""

    text: str | None = Field(
        default=None,
    )
    """Photo caption."""

    user_id: int | None = Field(
        default=None,
    )
    """ID of the user who have uploaded the photo."""

    width: int | None = Field(
        default=None,
    )
    """Original photo width."""

    likes: "BaseLikes | None" = Field(
        default=None,
    )
    """Property `PhotosPhoto.likes`."""

    comments: "BaseObjectCount | None" = Field(
        default=None,
    )
    """Property `PhotosPhoto.comments`."""

    reposts: "BaseRepostsInfo | None" = Field(
        default=None,
    )
    """Property `PhotosPhoto.reposts`."""

    tags: "BaseObjectCount | None" = Field(
        default=None,
    )
    """Property `PhotosPhoto.tags`."""

    hidden: "BasePropertyExists | None" = Field(
        default=None,
    )
    """Returns if the photo is hidden above the wall."""

    real_offset: int | None = Field(
        default=None,
    )
    """Real position of the photo."""

    vertical_align: "PhotosPhotoVerticalAlign | None" = Field(
        default=None,
    )
    """Sets vertical alignment of a photo."""


class PhotosPhotoAlbum(BaseModel):
    """Model: `PhotosPhotoAlbum`"""

    created: int = Field()
    """Date when the album has been created in Unixtime."""

    id: int = Field()
    """Photo album ID."""

    owner_id: int = Field()
    """Album owner\'s ID."""

    size: int = Field()
    """Photos number."""

    title: str = Field()
    """Photo album title."""

    updated: int = Field()
    """Date when the album has been updated last time in Unixtime."""

    description: str | None = Field(
        default=None,
    )
    """Photo album description."""

    thumb: "PhotosPhoto | None" = Field(
        default=None,
    )
    """Property `PhotosPhotoAlbum.thumb`."""


class PhotosPhotoAlbumFull(BaseModel):
    """Model: `PhotosPhotoAlbumFull`"""

    id: int = Field()
    """Photo album ID."""

    owner_id: int = Field()
    """Album owner\'s ID."""

    size: int = Field()
    """Photos number."""

    title: str = Field()
    """Photo album title."""

    can_upload: bool | None = Field(
        default=None,
    )
    """Information whether current user can upload photo to the album."""

    comments_disabled: bool | None = Field(
        default=None,
    )
    """Information whether album comments are disabled."""

    created: int | None = Field(
        default=None,
    )
    """Date when the album has been created in Unixtime, not set for system albums."""

    description: str | None = Field(
        default=None,
    )
    """Photo album description."""

    can_delete: bool | None = Field(
        default=None,
    )
    """album can delete."""

    can_include_to_feed: bool | None = Field(
        default=None,
    )
    """album can be selected to feed."""

    is_locked: bool | None = Field(
        default=None,
    )
    """Need show privacy lock at album."""

    sizes: list["PhotosPhotoSizes"] | None = Field(
        default=None,
    )
    """Property `PhotosPhotoAlbumFull.sizes`."""

    thumb_id: int | None = Field(
        default=None,
    )
    """Thumb photo ID."""

    thumb_is_last: bool | None = Field(
        default=None,
    )
    """Information whether the album thumb is last photo."""

    thumb_src: str | None = Field(
        default=None,
    )
    """URL of the thumb image."""

    updated: int | None = Field(
        default=None,
    )
    """Date when the album has been updated last time in Unixtime, not set for system albums."""

    upload_by_admins_only: bool | None = Field(
        default=None,
    )
    """Information whether only community administrators can upload photos."""


class PhotosPhotoSizes(BaseModel):
    """Model: `PhotosPhotoSizes`"""

    height: int = Field()
    """Height in px."""

    type: "PhotosPhotoSizesType" = Field()
    """Property `PhotosPhotoSizes.type`."""

    width: int = Field()
    """Width in px."""

    url: str | None = Field(
        default=None,
    )
    """URL of the image."""

    src: str | None = Field(
        default=None,
    )
    """URL of the image."""


class PhotosPhotoSizesType(StrEnum, metaclass=BaseEnumMeta):
    T = "t"
    S = "s"
    M = "m"
    X = "x"
    O = "o"
    P = "p"
    Q = "q"
    R = "r"
    K = "k"
    L = "l"
    Y = "y"
    Z = "z"
    C = "c"
    W = "w"
    A = "a"
    B = "b"
    E = "e"
    I = "i"
    D = "d"
    J = "j"
    TEMP = "temp"
    H = "h"
    G = "g"
    N = "n"
    F = "f"
    MAX = "max"
    BASE = "base"
    U = "u"
    V = "v"
    ORIG = "orig"


class PhotosPhotoTag(BaseModel):
    """Model: `PhotosPhotoTag`"""

    date: datetime.datetime = Field()
    """Date when tag has been added in Unixtime."""

    id: int = Field()
    """Tag ID."""

    placer_id: int = Field()
    """ID of the tag creator."""

    tagged_name: str = Field()
    """Tag description."""

    user_id: int = Field()
    """Tagged user ID."""

    viewed: bool = Field()
    """Information whether the tag is reviewed."""

    x: float = Field()
    """Coordinate X of the left upper corner."""

    x2: float = Field()
    """Coordinate X of the right lower corner."""

    y: float = Field()
    """Coordinate Y of the left upper corner."""

    y2: float = Field()
    """Coordinate Y of the right lower corner."""

    description: str | None = Field(
        default=None,
    )
    """Tagged description.."""


class PhotosPhotoUpload(BaseModel):
    """Model: `PhotosPhotoUpload`"""

    album_id: int = Field()
    """Album ID."""

    upload_url: str = Field()
    """URL to upload photo."""

    user_id: int = Field()
    """User ID."""

    fallback_upload_url: str | None = Field(
        default=None,
    )
    """Fallback URL if upload_url returned error."""

    group_id: int | None = Field(
        default=None,
    )
    """Group ID."""


class PhotosPhotoXtrTagInfo(BaseModel):
    """Model: `PhotosPhotoXtrTagInfo`"""

    album_id: int = Field()
    """Album ID."""

    date: datetime.datetime = Field()
    """Date when uploaded."""

    id: int = Field()
    """Photo ID."""

    owner_id: int = Field()
    """Photo owner\'s ID."""

    access_key: str | None = Field(
        default=None,
    )
    """Access key for the photo."""

    height: int | None = Field(
        default=None,
    )
    """Original photo height."""

    lat: float | None = Field(
        default=None,
    )
    """Latitude."""

    long: float | None = Field(
        default=None,
    )
    """Longitude."""

    photo_1280: str | None = Field(
        default=None,
    )
    """URL of image with 1280 px width."""

    photo_130: str | None = Field(
        default=None,
    )
    """URL of image with 130 px width."""

    photo_2560: str | None = Field(
        default=None,
    )
    """URL of image with 2560 px width."""

    photo_604: str | None = Field(
        default=None,
    )
    """URL of image with 604 px width."""

    photo_75: str | None = Field(
        default=None,
    )
    """URL of image with 75 px width."""

    photo_807: str | None = Field(
        default=None,
    )
    """URL of image with 807 px width."""

    placer_id: int | None = Field(
        default=None,
    )
    """ID of the tag creator."""

    post_id: int | None = Field(
        default=None,
    )
    """Post ID."""

    sizes: list["PhotosPhotoSizes"] | None = Field(
        default=None,
    )
    """Property `PhotosPhotoXtrTagInfo.sizes`."""

    tag_created: int | None = Field(
        default=None,
    )
    """Date when tag has been added in Unixtime."""

    tag_id: int | None = Field(
        default=None,
    )
    """Tag ID."""

    text: str | None = Field(
        default=None,
    )
    """Photo caption."""

    user_id: int | None = Field(
        default=None,
    )
    """ID of the user who have uploaded the photo."""

    width: int | None = Field(
        default=None,
    )
    """Original photo width."""

    has_tags: bool | None = Field(
        default=None,
    )
    """Whether photo has attached tag links."""


class PhotosTagsSuggestionItem(BaseModel):
    """Model: `PhotosTagsSuggestionItem`"""

    title: str | None = Field(
        default=None,
    )
    """Property `PhotosTagsSuggestionItem.title`."""

    caption: str | None = Field(
        default=None,
    )
    """Property `PhotosTagsSuggestionItem.caption`."""

    type: str | None = Field(
        default=None,
    )
    """Property `PhotosTagsSuggestionItem.type`."""

    buttons: list["PhotosTagsSuggestionItemButton"] | None = Field(
        default=None,
    )
    """Property `PhotosTagsSuggestionItem.buttons`."""

    photo: "PhotosPhoto | None" = Field(
        default=None,
    )
    """Property `PhotosTagsSuggestionItem.photo`."""

    tags: list["PhotosPhotoTag"] | None = Field(
        default=None,
    )
    """Property `PhotosTagsSuggestionItem.tags`."""

    track_code: str | None = Field(
        default=None,
    )
    """Property `PhotosTagsSuggestionItem.track_code`."""


class PhotosTagsSuggestionItemButtonAction(StrEnum, metaclass=BaseEnumMeta):
    CONFIRM = "confirm"
    DECLINE = "decline"
    SHOW_TAGS = "show_tags"


class PhotosTagsSuggestionItemButtonStyle(StrEnum, metaclass=BaseEnumMeta):
    PRIMARY = "primary"
    SECONDARY = "secondary"


class PhotosTagsSuggestionItemButton(BaseModel):
    """Model: `PhotosTagsSuggestionItemButton`"""

    title: str | None = Field(
        default=None,
    )
    """Property `PhotosTagsSuggestionItemButton.title`."""

    action: "PhotosTagsSuggestionItemButtonAction | None" = Field(
        default=None,
    )
    """Property `PhotosTagsSuggestionItemButton.action`."""

    style: "PhotosTagsSuggestionItemButtonStyle | None" = Field(
        default=None,
    )
    """Property `PhotosTagsSuggestionItemButton.style`."""


class PodcastCover(BaseModel):
    """Model: `PodcastCover`"""

    sizes: list["PhotosPhotoSizes"] | None = Field(
        default=None,
    )
    """Property `PodcastCover.sizes`."""


class PodcastExternalData(BaseModel):
    """Model: `PodcastExternalData`"""

    url: str | None = Field(
        default=None,
    )
    """Url of the podcast page."""

    owner_url: str | None = Field(
        default=None,
    )
    """Url of the podcasts owner community."""

    title: str | None = Field(
        default=None,
    )
    """Podcast title."""

    owner_name: str | None = Field(
        default=None,
    )
    """Name of the podcasts owner community."""

    cover: "PodcastCover | None" = Field(
        default=None,
    )
    """Podcast cover."""


class PollsAnswer(BaseModel):
    """Model: `PollsAnswer`"""

    id: int = Field()
    """Answer ID."""

    rate: float = Field()
    """Answer rate in percents."""

    text: str = Field()
    """Answer text."""

    votes: int = Field()
    """Votes number."""


class PollsBackgroundType(StrEnum, metaclass=BaseEnumMeta):
    GRADIENT = "gradient"
    TILE = "tile"
    COLOR = "color"


class PollsBackground(BaseModel):
    """Model: `PollsBackground`"""

    angle: int | None = Field(
        default=None,
    )
    """Gradient angle with 0 on positive X axis."""

    color: str | None = Field(
        default=None,
    )
    """Hex color code without #."""

    height: int | None = Field(
        default=None,
    )
    """Original height of pattern tile."""

    id: int | None = Field(
        default=None,
    )
    """Property `PollsBackground.id`."""

    name: str | None = Field(
        default=None,
    )
    """Property `PollsBackground.name`."""

    images: list["BaseImage"] | None = Field(
        default=None,
    )
    """Pattern tiles."""

    points: list["BaseGradientPoint"] | None = Field(
        default=None,
    )
    """Gradient points."""

    type: "PollsBackgroundType | None" = Field(
        default=None,
    )
    """Property `PollsBackground.type`."""

    width: int | None = Field(
        default=None,
    )
    """Original with of pattern tile."""


class PollsFieldsVoters(BaseModel):
    """Model: `PollsFieldsVoters`"""

    answer_id: int | None = Field(
        default=None,
    )
    """Answer ID."""

    users: "PollsVotersFieldsUsers | None" = Field(
        default=None,
    )
    """Property `PollsFieldsVoters.users`."""

    answer_offset: str | None = Field(
        default=None,
    )
    """Answer offset."""


class PollsFriend(BaseModel):
    """Model: `PollsFriend`"""

    id: int = Field()
    """Property `PollsFriend.id`."""


class PollsPoll(BaseModel):
    """Model: `PollsPoll`"""

    multiple: bool = Field()
    """Information whether the poll with multiple choices."""

    end_date: datetime.datetime = Field()
    """Property `PollsPoll.end_date`."""

    closed: bool = Field()
    """Property `PollsPoll.closed`."""

    is_board: bool = Field()
    """Property `PollsPoll.is_board`."""

    can_edit: bool = Field()
    """Property `PollsPoll.can_edit`."""

    can_vote: bool = Field()
    """Property `PollsPoll.can_vote`."""

    can_report: bool = Field()
    """Property `PollsPoll.can_report`."""

    can_share: bool = Field()
    """Property `PollsPoll.can_share`."""

    answers: list["PollsAnswer"] = Field()
    """Property `PollsPoll.answers`."""

    created: int = Field()
    """Date when poll has been created in Unixtime."""

    id: int = Field()
    """Poll ID."""

    owner_id: int = Field()
    """Poll owner\'s ID."""

    question: str = Field()
    """Poll question."""

    votes: int = Field()
    """Votes number."""

    disable_unvote: bool = Field()
    """Property `PollsPoll.disable_unvote`."""

    anonymous: "PollsPollAnonymous | None" = Field(
        default=None,
    )
    """Property `PollsPoll.anonymous`."""

    friends: list["PollsFriend"] | None = Field(
        default=None,
    )
    """Property `PollsPoll.friends`."""

    answer_id: int | None = Field(
        default=None,
    )
    """Current user\'s answer ID."""

    answer_ids: list[int] | None = Field(
        default=None,
    )
    """Current user\'s answer IDs."""

    embed_hash: str | None = Field(
        default=None,
    )
    """Property `PollsPoll.embed_hash`."""

    photo: "PollsBackground | None" = Field(
        default=None,
    )
    """Property `PollsPoll.photo`."""

    author_id: int | None = Field(
        default=None,
    )
    """Poll author\'s ID."""

    background: "PollsBackground | None" = Field(
        default=None,
    )
    """Property `PollsPoll.background`."""


PollsPollAnonymous: typing.TypeAlias = bool


class PollsVoters(BaseModel):
    """Model: `PollsVoters`"""

    answer_id: int | None = Field(
        default=None,
    )
    """Answer ID."""

    users: "PollsVotersUsers | None" = Field(
        default=None,
    )
    """Property `PollsVoters.users`."""

    answer_offset: str | None = Field(
        default=None,
    )
    """Answer offset."""


class PollsVotersFieldsUsers(BaseModel):
    """Model: `PollsVotersFieldsUsers`"""

    count: int | None = Field(
        default=None,
    )
    """Votes number."""

    items: list["UsersUserFull"] | None = Field(
        default=None,
    )
    """Property `PollsVotersFieldsUsers.items`."""


class PollsVotersUsers(BaseModel):
    """Model: `PollsVotersUsers`"""

    count: int | None = Field(
        default=None,
    )
    """Votes number."""

    items: list[int] | None = Field(
        default=None,
    )
    """Property `PollsVotersUsers.items`."""


class PrettyCardsButtonOneOf(BaseModel):
    """Model: `PrettyCardsButtonOneOf`"""


class PrettyCardsPrettyCardInnerType(StrEnum, metaclass=BaseEnumMeta):
    PRETTYCARDS_PRETTYCARD = "prettyCards_prettyCard"


class PrettyCardsPrettyCard(BaseModel):
    """Model: `PrettyCardsPrettyCard`"""

    inner_type: "PrettyCardsPrettyCardInnerType" = Field()
    """Property `PrettyCardsPrettyCard.inner_type`."""

    card_id: str = Field()
    """Card ID (long int returned as string)."""

    link_url: str = Field()
    """Link URL."""

    photo: str = Field()
    """Photo ID (format \"<owner_id>_<media_id>\")."""

    title: str = Field()
    """Title."""

    button: "PrettyCardsButtonOneOf | None" = Field(
        default=None,
    )
    """Button key."""

    button_text: str | None = Field(
        default=None,
    )
    """Button text in current language."""

    images: list["BaseImage"] | None = Field(
        default=None,
    )
    """Property `PrettyCardsPrettyCard.images`."""

    price: str | None = Field(
        default=None,
    )
    """Price if set (decimal number returned as string)."""

    price_old: str | None = Field(
        default=None,
    )
    """Old price if set (decimal number returned as string)."""


class PrettyCardsPrettyCardOrError(BaseModel):
    """Model: `PrettyCardsPrettyCardOrError`"""


class SearchHint(BaseModel):
    """Model: `SearchHint`"""

    description: str = Field()
    """Object description."""

    type: "SearchHintType" = Field()
    """Property `SearchHint.type`."""

    app: "AppsApp | None" = Field(
        default=None,
    )
    """Property `SearchHint.app`."""

    global_: bool | None = Field(
        default=None,
        alias="global",
    )
    """Information whether the object has been found globally."""

    group: "GroupsGroup | None" = Field(
        default=None,
    )
    """Property `SearchHint.group`."""

    profile: "UsersUserMin | None" = Field(
        default=None,
    )
    """Property `SearchHint.profile`."""

    section: "SearchHintSection | None" = Field(
        default=None,
    )
    """Property `SearchHint.section`."""

    link: "BaseLink | None" = Field(
        default=None,
    )
    """Property `SearchHint.link`."""


class SearchHintSection(StrEnum, metaclass=BaseEnumMeta):
    GROUPS = "groups"
    EVENTS = "events"
    PUBLICS = "publics"
    CORRESPONDENTS = "correspondents"
    PEOPLE = "people"
    FRIENDS = "friends"
    MUTUAL_FRIENDS = "mutual_friends"
    PROMO = "promo"


class SearchHintType(StrEnum, metaclass=BaseEnumMeta):
    GROUP = "group"
    PROFILE = "profile"
    VK_APP = "vk_app"
    APP = "app"
    HTML5_GAME = "html5_game"
    LINK = "link"


class SecureGiveEventStickerItem(BaseModel):
    """Model: `SecureGiveEventStickerItem`"""

    user_id: int | None = Field(
        default=None,
    )
    """Property `SecureGiveEventStickerItem.user_id`."""

    status: str | None = Field(
        default=None,
    )
    """Property `SecureGiveEventStickerItem.status`."""


class SecureLevel(BaseModel):
    """Model: `SecureLevel`"""

    level: int | None = Field(
        default=None,
    )
    """Level."""

    uid: int | None = Field(
        default=None,
    )
    """User ID."""


class SecureSetCounterItem(BaseModel):
    """Model: `SecureSetCounterItem`"""

    id: int = Field()
    """User ID."""

    result: bool = Field()
    """Property `SecureSetCounterItem.result`."""


class SecureSmsNotification(BaseModel):
    """Model: `SecureSmsNotification`"""

    app_id: str | None = Field(
        default=None,
    )
    """Application ID."""

    date: str | None = Field(
        default=None,
    )
    """Date when message has been sent in Unixtime."""

    id: str | None = Field(
        default=None,
    )
    """Notification ID."""

    message: str | None = Field(
        default=None,
    )
    """Messsage text."""

    user_id: str | None = Field(
        default=None,
    )
    """User ID."""


class SecureTokenChecked(BaseModel):
    """Model: `SecureTokenChecked`"""

    date: datetime.datetime | None = Field(
        default=None,
    )
    """Date when access_token has been generated in Unixtime."""

    expire: int | None = Field(
        default=None,
    )
    """Date when access_token will expire in Unixtime."""

    success: int | None = Field(
        default=None,
    )
    """Returns if successfully processed."""

    user_id: int | None = Field(
        default=None,
    )
    """User ID."""


class SecureTransaction(BaseModel):
    """Model: `SecureTransaction`"""

    date: datetime.datetime | None = Field(
        default=None,
    )
    """Transaction date in Unixtime."""

    id: int | None = Field(
        default=None,
    )
    """Transaction ID."""

    uid_from: int | None = Field(
        default=None,
    )
    """From ID."""

    uid_to: int | None = Field(
        default=None,
    )
    """To ID."""

    votes: int | None = Field(
        default=None,
    )
    """Votes number."""


class StatsActivity(BaseModel):
    """Activity stats
    Model: `StatsActivity`
    """

    comments: int | None = Field(
        default=None,
    )
    """Comments number."""

    copies: int | None = Field(
        default=None,
    )
    """Reposts number."""

    hidden: int | None = Field(
        default=None,
    )
    """Hidden from news count."""

    likes: int | None = Field(
        default=None,
    )
    """Likes number."""

    subscribed: int | None = Field(
        default=None,
    )
    """New subscribers count."""

    unsubscribed: int | None = Field(
        default=None,
    )
    """Unsubscribed count."""


class StatsCity(BaseModel):
    """Model: `StatsCity`"""

    count: int | None = Field(
        default=None,
    )
    """Visitors number."""

    name: str | None = Field(
        default=None,
    )
    """City name."""

    value: int | None = Field(
        default=None,
    )
    """City ID."""


class StatsCountry(BaseModel):
    """Model: `StatsCountry`"""

    code: str | None = Field(
        default=None,
    )
    """Country code."""

    count: int | None = Field(
        default=None,
    )
    """Visitors number."""

    name: str | None = Field(
        default=None,
    )
    """Country name."""

    value: int | None = Field(
        default=None,
    )
    """Country ID."""


class StatsPeriod(BaseModel):
    """Model: `StatsPeriod`"""

    activity: "StatsActivity | None" = Field(
        default=None,
    )
    """Property `StatsPeriod.activity`."""

    period_from: "StatsPeriodFromOneOf | None" = Field(
        default=None,
    )
    """Property `StatsPeriod.period_from`."""

    period_to: "StatsPeriodToOneOf | None" = Field(
        default=None,
    )
    """Property `StatsPeriod.period_to`."""

    reach: "StatsReach | None" = Field(
        default=None,
    )
    """Property `StatsPeriod.reach`."""

    visitors: "StatsViews | None" = Field(
        default=None,
    )
    """Property `StatsPeriod.visitors`."""


StatsPeriodFromOneOf: typing.TypeAlias = datetime.datetime


StatsPeriodToOneOf: typing.TypeAlias = datetime.datetime


class StatsReach(BaseModel):
    """Reach stats
    Model: `StatsReach`
    """

    age: list["StatsSexAge"] | None = Field(
        default=None,
    )
    """Property `StatsReach.age`."""

    cities: list["StatsCity"] | None = Field(
        default=None,
    )
    """Property `StatsReach.cities`."""

    countries: list["StatsCountry"] | None = Field(
        default=None,
    )
    """Property `StatsReach.countries`."""

    mobile_reach: int | None = Field(
        default=None,
    )
    """Reach count from mobile devices."""

    reach: int | None = Field(
        default=None,
    )
    """Reach count."""

    reach_subscribers: int | None = Field(
        default=None,
    )
    """Subscribers reach count."""

    sex: list["StatsSexAge"] | None = Field(
        default=None,
    )
    """Property `StatsReach.sex`."""

    sex_age: list["StatsSexAge"] | None = Field(
        default=None,
    )
    """Property `StatsReach.sex_age`."""


class StatsSexAge(BaseModel):
    """Model: `StatsSexAge`"""

    value: str = Field()
    """Sex/age value."""

    count: int | None = Field(
        default=None,
    )
    """Visitors number."""

    reach: int | None = Field(
        default=None,
    )
    """Property `StatsSexAge.reach`."""

    reach_subscribers: int | None = Field(
        default=None,
    )
    """Property `StatsSexAge.reach_subscribers`."""

    count_subscribers: int | None = Field(
        default=None,
    )
    """Property `StatsSexAge.count_subscribers`."""


class StatsViews(BaseModel):
    """Views stats
    Model: `StatsViews`
    """

    age: list["StatsSexAge"] | None = Field(
        default=None,
    )
    """Property `StatsViews.age`."""

    cities: list["StatsCity"] | None = Field(
        default=None,
    )
    """Property `StatsViews.cities`."""

    countries: list["StatsCountry"] | None = Field(
        default=None,
    )
    """Property `StatsViews.countries`."""

    mobile_views: int | None = Field(
        default=None,
    )
    """Number of views from mobile devices."""

    sex: list["StatsSexAge"] | None = Field(
        default=None,
    )
    """Property `StatsViews.sex`."""

    sex_age: list["StatsSexAge"] | None = Field(
        default=None,
    )
    """Property `StatsViews.sex_age`."""

    views: int | None = Field(
        default=None,
    )
    """Views number."""

    visitors: int | None = Field(
        default=None,
    )
    """Visitors number."""


class StatsWallpostStat(BaseModel):
    """Model: `StatsWallpostStat`"""

    post_id: int | None = Field(
        default=None,
    )
    """Property `StatsWallpostStat.post_id`."""

    hide: int | None = Field(
        default=None,
    )
    """Hidings number."""

    join_group: int | None = Field(
        default=None,
    )
    """People have joined the group."""

    links: int | None = Field(
        default=None,
    )
    """Link clickthrough."""

    reach_subscribers: int | None = Field(
        default=None,
    )
    """Subscribers reach."""

    reach_subscribers_count: int | None = Field(
        default=None,
    )
    """Property `StatsWallpostStat.reach_subscribers_count`."""

    reach_total: int | None = Field(
        default=None,
    )
    """Total reach."""

    reach_total_count: int | None = Field(
        default=None,
    )
    """Property `StatsWallpostStat.reach_total_count`."""

    reach_viral: int | None = Field(
        default=None,
    )
    """Property `StatsWallpostStat.reach_viral`."""

    reach_ads: int | None = Field(
        default=None,
    )
    """Property `StatsWallpostStat.reach_ads`."""

    report: int | None = Field(
        default=None,
    )
    """Reports number."""

    to_group: int | None = Field(
        default=None,
    )
    """Clickthrough to community."""

    unsubscribe: int | None = Field(
        default=None,
    )
    """Unsubscribed members."""

    sex_age: list["StatsSexAge"] | None = Field(
        default=None,
    )
    """Property `StatsWallpostStat.sex_age`."""


class StatusStatus(BaseModel):
    """Model: `StatusStatus`"""

    text: str = Field()
    """Status text."""

    audio: "AudioAudio | None" = Field(
        default=None,
    )
    """Property `StatusStatus.audio`."""


class StickersImageSet(BaseModel):
    """Model: `StickersImageSet`"""

    base_url: str = Field()
    """Base URL for images in set."""

    version: int | None = Field(
        default=None,
    )
    """Version number to be appended to the image URL."""

    images: list["BaseImage"] | None = Field(
        default=None,
    )
    """Property `StickersImageSet.images`."""


class StorageValue(BaseModel):
    """Model: `StorageValue`"""

    key: str = Field()
    """Property `StorageValue.key`."""

    value: str = Field()
    """Property `StorageValue.value`."""


class StoreProductType(StrEnum, metaclass=BaseEnumMeta):
    STICKERS = "stickers"


class StoreProduct(BaseModel):
    """Model: `StoreProduct`"""

    id: int = Field()
    """Id of the product."""

    type: "StoreProductType" = Field()
    """Product type."""

    is_new: bool | None = Field(
        default=None,
    )
    """Information whether sticker product wasn\'t used after being purchased."""

    copyright: str | None = Field(
        default=None,
    )
    """Product copyright information."""

    base_id: int | None = Field(
        default=None,
    )
    """Id of the base pack (for sticker pack styles)."""

    style_ids: list[int] | None = Field(
        default=None,
    )
    """Array of style ids available for the sticker pack."""

    purchased: bool | None = Field(
        default=None,
    )
    """Information whether the product is purchased (1 - yes, 0 - no)."""

    active: bool | None = Field(
        default=None,
    )
    """Information whether the product is active (1 - yes, 0 - no)."""

    promoted: bool | None = Field(
        default=None,
    )
    """Information whether the product is promoted (1 - yes, 0 - no)."""

    purchase_date: datetime.datetime | None = Field(
        default=None,
    )
    """Date (Unix time) when the product was purchased."""

    title: str | None = Field(
        default=None,
    )
    """Title of the product."""

    stickers: list["BaseStickerNew"] | None = Field(
        default=None,
    )
    """Property `StoreProduct.stickers`."""

    style_sticker_ids: list[int] | None = Field(
        default=None,
    )
    """Array of style sticker ids (for sticker pack styles)."""

    icon: "StoreProductIcon | None" = Field(
        default=None,
    )
    """Array of icon images or icon set object of the product (for stickers product type)."""

    previews: list["BaseImage"] | None = Field(
        default=None,
    )
    """Array of preview images of the product (for stickers product type)."""

    has_animation: bool | None = Field(
        default=None,
    )
    """Information whether the product is an animated sticker pack (for stickers product type)."""

    subtitle: str | None = Field(
        default=None,
    )
    """Subtitle of the product."""

    payment_region: str | None = Field(
        default=None,
    )
    """Property `StoreProduct.payment_region`."""

    is_vmoji: bool | None = Field(
        default=None,
    )
    """Information whether sticker pack is a vmoji pack."""

    title_lang_key: str | None = Field(
        default=None,
    )
    """Property `StoreProduct.title_lang_key`."""

    description_lang_key: str | None = Field(
        default=None,
    )
    """Property `StoreProduct.description_lang_key`."""

    url: str | None = Field(
        default=None,
    )
    """Property `StoreProduct.url`."""

    is_popup: bool | None = Field(
        default=None,
    )
    """Information whether the product is a sticker pack with popup stickers (for stickers product type)."""


class StoreProductIcon(BaseModel):
    """Model: `StoreProductIcon`"""

    base_url: str = Field()
    """Base URL for images in set."""

    version: int | None = Field(
        default=None,
    )
    """Version number to be appended to the image URL."""

    images: list["BaseImage"] | None = Field(
        default=None,
    )
    """Property `StoreProductIcon.images`."""


class StoreStickersKeyword(BaseModel):
    """Model: `StoreStickersKeyword`"""

    words: list[str] = Field()
    """Property `StoreStickersKeyword.words`."""

    user_stickers: list["BaseStickerNew"] | None = Field(
        default=None,
    )
    """Property `StoreStickersKeyword.user_stickers`."""

    promoted_stickers: list["BaseStickerNew"] | None = Field(
        default=None,
    )
    """Property `StoreStickersKeyword.promoted_stickers`."""

    stickers: list["StoreStickersKeywordSticker"] | None = Field(
        default=None,
    )
    """Property `StoreStickersKeyword.stickers`."""


class StoreStickersKeywordSticker(BaseModel):
    """Model: `StoreStickersKeywordSticker`"""

    pack_id: int = Field()
    """Pack id."""

    sticker_id: int = Field()
    """Sticker id."""


class StoriesClickableArea(BaseModel):
    """Model: `StoriesClickableArea`"""

    x: int = Field()
    """Property `StoriesClickableArea.x`."""

    y: int = Field()
    """Property `StoriesClickableArea.y`."""


class StoriesClickableStickerType(StrEnum, metaclass=BaseEnumMeta):
    HASHTAG = "hashtag"
    MENTION = "mention"
    LINK = "link"
    QUESTION = "question"
    PLACE = "place"
    MARKET_ITEM = "market_item"
    MUSIC = "music"
    STORY_REPLY = "story_reply"
    OWNER = "owner"
    POST = "post"
    POLL = "poll"
    STICKER = "sticker"
    APP = "app"
    SITUATIONAL_THEME = "situational_theme"
    PLAYLIST = "playlist"
    CLIP = "clip"
    VK_VIDEO = "vk_video"
    SITUATIONAL_TEMPLATE = "situational_template"
    SPOILER = "spoiler"
    SERVICE_YC_ITEM = "service_yc_item"


class StoriesClickableStickerStyle(StrEnum, metaclass=BaseEnumMeta):
    TRANSPARENT = "transparent"
    BLUE_GRADIENT = "blue_gradient"
    RED_GRADIENT = "red_gradient"
    UNDERLINE = "underline"
    BLUE = "blue"
    GREEN = "green"
    WHITE = "white"
    QUESTION_REPLY = "question_reply"
    LIGHT = "light"
    IMPRESSIVE = "impressive"
    DARK = "dark"
    ACCENT_BACKGROUND = "accent_background"
    ACCENT_TEXT = "accent_text"
    DARK_UNIQUE = "dark_unique"
    LIGHT_UNIQUE = "light_unique"
    LIGHT_TEXT = "light_text"
    DARK_TEXT = "dark_text"
    BLACK = "black"
    DARK_WITHOUT_BG = "dark_without_bg"
    LIGHT_WITHOUT_BG = "light_without_bg"
    RECTANGLE = "rectangle"
    CIRCLE = "circle"
    POOP = "poop"
    HEART = "heart"
    STAR = "star"
    ALBUM = "album"
    HORIZONTAL = "horizontal"
    EQUALIZER = "equalizer"
    HEADER_META = "header_meta"
    PREVIEW = "preview"
    MINIATURE = "miniature"
    FULLVIEW = "fullview"
    CTA = "cta"
    STICKER = "sticker"
    STICKER_AND_CTA = "sticker_and_cta"
    ACCENT = "accent"


class StoriesClickableStickerSubtype(StrEnum, metaclass=BaseEnumMeta):
    MARKET_ITEM = "market_item"
    ALIEXPRESS_PRODUCT = "aliexpress_product"


class StoriesClickableSticker(BaseModel):
    """Model: `StoriesClickableSticker`"""

    clickable_area: list["StoriesClickableArea"] = Field()
    """Property `StoriesClickableSticker.clickable_area`."""

    id: int = Field()
    """Clickable sticker ID."""

    type: "StoriesClickableStickerType" = Field()
    """Property `StoriesClickableSticker.type`."""

    hashtag: str | None = Field(
        default=None,
    )
    """Property `StoriesClickableSticker.hashtag`."""

    link_object: "BaseLink | None" = Field(
        default=None,
    )
    """Property `StoriesClickableSticker.link_object`."""

    mention: str | None = Field(
        default=None,
    )
    """Property `StoriesClickableSticker.mention`."""

    tooltip_text: str | None = Field(
        default=None,
    )
    """Property `StoriesClickableSticker.tooltip_text`."""

    owner_id: int | None = Field(
        default=None,
    )
    """Property `StoriesClickableSticker.owner_id`."""

    story_id: int | None = Field(
        default=None,
    )
    """Property `StoriesClickableSticker.story_id`."""

    clip_id: int | None = Field(
        default=None,
    )
    """Property `StoriesClickableSticker.clip_id`."""

    video_id: int | None = Field(
        default=None,
    )
    """Property `StoriesClickableSticker.video_id`."""

    question: str | None = Field(
        default=None,
    )
    """Property `StoriesClickableSticker.question`."""

    question_button: str | None = Field(
        default=None,
    )
    """Property `StoriesClickableSticker.question_button`."""

    place_id: int | None = Field(
        default=None,
    )
    """Property `StoriesClickableSticker.place_id`."""

    market_item: "MarketMarketItem | None" = Field(
        default=None,
    )
    """Property `StoriesClickableSticker.market_item`."""

    audio: "AudioAudio | None" = Field(
        default=None,
    )
    """Property `StoriesClickableSticker.audio`."""

    audio_start_time: int | None = Field(
        default=None,
    )
    """Property `StoriesClickableSticker.audio_start_time`."""

    style: "StoriesClickableStickerStyle | None" = Field(
        default=None,
    )
    """Property `StoriesClickableSticker.style`."""

    subtype: "StoriesClickableStickerSubtype | None" = Field(
        default=None,
    )
    """Property `StoriesClickableSticker.subtype`."""

    post_owner_id: int | None = Field(
        default=None,
    )
    """Property `StoriesClickableSticker.post_owner_id`."""

    post_id: int | None = Field(
        default=None,
    )
    """Property `StoriesClickableSticker.post_id`."""

    poll: "PollsPoll | None" = Field(
        default=None,
    )
    """Property `StoriesClickableSticker.poll`."""

    color: str | None = Field(
        default=None,
    )
    """Color, hex format."""

    sticker_id: int | None = Field(
        default=None,
    )
    """Sticker ID."""

    sticker_pack_id: int | None = Field(
        default=None,
    )
    """Sticker pack ID."""

    app: "AppsAppMin | None" = Field(
        default=None,
    )
    """Property `StoriesClickableSticker.app`."""

    app_context: str | None = Field(
        default=None,
    )
    """Additional context for app sticker."""

    has_new_interactions: bool | None = Field(
        default=None,
    )
    """Whether current user has unread interaction with this app."""

    is_broadcast_notify_allowed: bool | None = Field(
        default=None,
    )
    """Whether current user allowed broadcast notify from this app."""

    situational_theme_id: int | None = Field(
        default=None,
    )
    """Property `StoriesClickableSticker.situational_theme_id`."""

    situational_app_url: str | None = Field(
        default=None,
    )
    """Property `StoriesClickableSticker.situational_app_url`."""


class StoriesClickableStickers(BaseModel):
    """Model: `StoriesClickableStickers`"""

    clickable_stickers: list["StoriesClickableSticker"] = Field()
    """Property `StoriesClickableStickers.clickable_stickers`."""

    original_height: int = Field()
    """Property `StoriesClickableStickers.original_height`."""

    original_width: int = Field()
    """Property `StoriesClickableStickers.original_width`."""


class StoriesFeedItemType(StrEnum, metaclass=BaseEnumMeta):
    PROMO_STORIES = "promo_stories"
    STORIES = "stories"
    LIVE_ACTIVE = "live_active"
    LIVE_FINISHED = "live_finished"
    APP_GROUPED_STORIES = "app_grouped_stories"
    DISCOVER = "discover"


class StoriesFeedItem(BaseModel):
    """Model: `StoriesFeedItem`"""

    type: "StoriesFeedItemType" = Field()
    """Type of Feed Item."""

    id: str | None = Field(
        default=None,
    )
    """Property `StoriesFeedItem.id`."""

    owner_id: int | None = Field(
        default=None,
    )
    """Property `StoriesFeedItem.owner_id`."""

    stories: list["StoriesStory"] | None = Field(
        default=None,
    )
    """Author stories."""

    grouped: list["StoriesFeedItem"] | None = Field(
        default=None,
    )
    """Grouped stories of various authors (for types community_grouped_stories/app_grouped_stories type)."""

    app: "AppsAppMin | None" = Field(
        default=None,
    )
    """App, which stories has been grouped (for type app_grouped_stories)."""

    promo_data: "StoriesPromoBlock | None" = Field(
        default=None,
    )
    """Additional data for promo stories (for type promo_stories)."""

    track_code: str | None = Field(
        default=None,
    )
    """Property `StoriesFeedItem.track_code`."""

    has_unseen: bool | None = Field(
        default=None,
    )
    """Property `StoriesFeedItem.has_unseen`."""

    name: str | None = Field(
        default=None,
    )
    """Property `StoriesFeedItem.name`."""


class StoriesPromoBlock(BaseModel):
    """Additional data for promo stories
    Model: `StoriesPromoBlock`
    """

    name: str = Field()
    """Promo story title."""

    photo_50: str = Field()
    """RL of square photo of the story with 50 pixels in width."""

    photo_100: str = Field()
    """RL of square photo of the story with 100 pixels in width."""

    not_animated: bool = Field()
    """Hide animation for promo story."""

    is_advice: bool = Field()
    """Promo story from advice."""


class StoriesReplies(BaseModel):
    """Model: `StoriesReplies`"""

    count: int = Field()
    """Replies number.."""

    new: int | None = Field(
        default=None,
    )
    """New replies number.."""


class StoriesStory(BaseModel):
    """Model: `StoriesStory`"""

    id: int = Field()
    """Story ID.."""

    owner_id: int = Field()
    """Story owner\'s ID.."""

    access_key: str | None = Field(
        default=None,
    )
    """Access key for private object.."""

    can_comment: bool | None = Field(
        default=None,
    )
    """Information whether current user can comment the story (0 - no, 1 - yes).."""

    can_reply: bool | None = Field(
        default=None,
    )
    """Information whether current user can reply to the story (0 - no, 1 - yes).."""

    can_see: bool | None = Field(
        default=None,
    )
    """Information whether current user can see the story (0 - no, 1 - yes).."""

    can_like: bool | None = Field(
        default=None,
    )
    """Information whether current user can like the story.."""

    can_share: bool | None = Field(
        default=None,
    )
    """Information whether current user can share the story (0 - no, 1 - yes).."""

    can_hide: bool | None = Field(
        default=None,
    )
    """Information whether current user can hide the story (0 - no, 1 - yes).."""

    date: datetime.datetime | None = Field(
        default=None,
    )
    """Date when story has been added in Unixtime.."""

    expires_at: int | None = Field(
        default=None,
    )
    """Story expiration time. Unixtime.."""

    is_deleted: bool | None = Field(
        default=None,
    )
    """Information whether the story is deleted (false - no, true - yes).."""

    is_expired: bool | None = Field(
        default=None,
    )
    """Information whether the story is expired (false - no, true - yes).."""

    link: "StoriesStoryLink | None" = Field(
        default=None,
    )
    """Property `StoriesStory.link`."""

    parent_story: "StoriesStory | None" = Field(
        default=None,
    )
    """Property `StoriesStory.parent_story`."""

    parent_story_access_key: str | None = Field(
        default=None,
    )
    """Access key for private object.."""

    parent_story_id: int | None = Field(
        default=None,
    )
    """Parent story ID.."""

    parent_story_owner_id: int | None = Field(
        default=None,
    )
    """Parent story owner\'s ID.."""

    photo: "PhotosPhoto | None" = Field(
        default=None,
    )
    """Property `StoriesStory.photo`."""

    blurred_preview: str | None = Field(
        default=None,
    )
    """url with blured preview image.."""

    replies: "StoriesReplies | None" = Field(
        default=None,
    )
    """Replies counters to current story.."""

    seen: bool | None = Field(
        default=None,
    )
    """Information whether current user has seen the story or not (0 - no, 1 - yes).."""

    type: "StoriesStoryType | None" = Field(
        default=None,
    )
    """Property `StoriesStory.type`."""

    clickable_stickers: "StoriesClickableStickers | None" = Field(
        default=None,
    )
    """Property `StoriesStory.clickable_stickers`."""

    video: "VideoVideoFull | None" = Field(
        default=None,
    )
    """Property `StoriesStory.video`."""

    views: int | None = Field(
        default=None,
    )
    """Views number.."""

    can_ask: bool | None = Field(
        default=None,
    )
    """Information whether story has question sticker and current user can send question to the author."""

    can_ask_anonymous: bool | None = Field(
        default=None,
    )
    """Information whether story has question sticker and current user can send anonymous question to the author."""

    narratives_count: int | None = Field(
        default=None,
    )
    """Property `StoriesStory.narratives_count`."""

    first_narrative_title: str | None = Field(
        default=None,
    )
    """Property `StoriesStory.first_narrative_title`."""

    first_narrative_id: int | None = Field(
        default=None,
    )
    """Property `StoriesStory.first_narrative_id`."""

    can_use_in_narrative: bool | None = Field(
        default=None,
    )
    """Property `StoriesStory.can_use_in_narrative`."""


class StoriesStoryLink(BaseModel):
    """Model: `StoriesStoryLink`"""

    text: str = Field()
    """Link text."""

    url: str = Field()
    """Link URL."""

    link_url_target: str | None = Field(
        default=None,
    )
    """How to open url."""


class StoriesStoryStats(BaseModel):
    """Model: `StoriesStoryStats`"""

    answer: "StoriesStoryStatsStat" = Field()
    """Property `StoriesStoryStats.answer`."""

    bans: "StoriesStoryStatsStat" = Field()
    """Property `StoriesStoryStats.bans`."""

    open_link: "StoriesStoryStatsStat" = Field()
    """Property `StoriesStoryStats.open_link`."""

    replies: "StoriesStoryStatsStat" = Field()
    """Property `StoriesStoryStats.replies`."""

    shares: "StoriesStoryStatsStat" = Field()
    """Property `StoriesStoryStats.shares`."""

    subscribers: "StoriesStoryStatsStat" = Field()
    """Property `StoriesStoryStats.subscribers`."""

    views: "StoriesStoryStatsStat" = Field()
    """Property `StoriesStoryStats.views`."""

    likes: "StoriesStoryStatsStat" = Field()
    """Property `StoriesStoryStats.likes`."""


class StoriesStoryStatsStat(BaseModel):
    """Model: `StoriesStoryStatsStat`"""

    state: "StoriesStoryStatsState" = Field()
    """Property `StoriesStoryStatsStat.state`."""

    count: int | None = Field(
        default=None,
    )
    """Stat value."""


class StoriesStoryStatsState(StrEnum, metaclass=BaseEnumMeta):
    ON = "on"
    OFF = "off"
    HIDDEN = "hidden"


class StoriesStoryType(StrEnum, metaclass=BaseEnumMeta):
    PHOTO = "photo"
    VIDEO = "video"
    LIVE_ACTIVE = "live_active"
    LIVE_FINISHED = "live_finished"


class StoriesUploadLinkText(StrEnum, metaclass=BaseEnumMeta):
    TO_STORE = "to_store"
    VOTE = "vote"
    MORE = "more"
    BOOK = "book"
    ORDER = "order"
    ENROLL = "enroll"
    FILL = "fill"
    SIGNUP = "signup"
    BUY = "buy"
    TICKET = "ticket"
    WRITE = "write"
    OPEN = "open"
    LEARN_MORE = "learn_more"
    VIEW = "view"
    GO_TO = "go_to"
    CONTACT = "contact"
    WATCH = "watch"
    PLAY = "play"
    INSTALL = "install"
    READ = "read"
    CALENDAR = "calendar"
    MARKET_ONLINE_BOOKING = "market_online_booking"
    MARKET_LINK = "market_link"
    MESSAGE_TO_BC = "message_to_bc"


class StoriesUploadResult(BaseModel):
    """Model: `StoriesUploadResult`"""

    upload_result: str | None = Field(
        default=None,
    )
    """Property `StoriesUploadResult.upload_result`."""


class StoriesViewersItem(BaseModel):
    """Model: `StoriesViewersItem`"""

    is_liked: bool = Field()
    """user has like for this object."""

    user_id: int = Field()
    """user id."""

    user: "UsersUserFull | None" = Field(
        default=None,
    )
    """Property `StoriesViewersItem.user`."""


class StreamingStatsEventType(StrEnum, metaclass=BaseEnumMeta):
    POST = "post"
    COMMENT = "comment"
    SHARE = "share"


class StreamingStats(BaseModel):
    """Model: `StreamingStats`"""

    event_type: "StreamingStatsEventType" = Field()
    """Events type."""

    stats: list["StreamingStatsPoint"] = Field()
    """Statistics."""


class StreamingStatsPoint(BaseModel):
    """Model: `StreamingStatsPoint`"""

    timestamp: int = Field()
    """Property `StreamingStatsPoint.timestamp`."""

    value: int = Field()
    """Property `StreamingStatsPoint.value`."""


class FriendsFriendStatus(BaseModel):
    """Model: `FriendsFriendStatus`"""

    friend_status: "FriendsFriendStatusStatus" = Field()
    """Property `FriendsFriendStatus.friend_status`."""

    user_id: int = Field()
    """User ID."""

    sign: str | None = Field(
        default=None,
    )
    """MD5 hash for the result validation."""


class FriendsFriendStatusStatus(IntEnum, metaclass=BaseEnumMeta):
    NOT_A_FRIEND = 0
    OUTCOMING_REQUEST = 1
    INCOMING_REQUEST = 2
    IS_FRIEND = 3


class FriendsFriendsList(BaseModel):
    """Model: `FriendsFriendsList`"""

    id: int = Field()
    """List ID."""

    name: str = Field()
    """List title."""


class FriendsMutualFriend(BaseModel):
    """Model: `FriendsMutualFriend`"""

    common_count: int | None = Field(
        default=None,
    )
    """Total mutual friends number."""

    common_friends: list[int] | None = Field(
        default=None,
    )
    """Property `FriendsMutualFriend.common_friends`."""

    id: int | None = Field(
        default=None,
    )
    """User ID."""


class FriendsOnlineUsers(BaseModel):
    """Model: `FriendsOnlineUsers`"""

    online: list[int] = Field()
    """Property `FriendsOnlineUsers.online`."""

    total_count: int | None = Field(
        default=None,
    )
    """Total online friends number."""


class FriendsOnlineUsersWithMobile(BaseModel):
    """Model: `FriendsOnlineUsersWithMobile`"""

    online: list[int] = Field()
    """Property `FriendsOnlineUsersWithMobile.online`."""

    online_mobile: list[int] = Field()
    """Property `FriendsOnlineUsersWithMobile.online_mobile`."""

    total_count: int | None = Field(
        default=None,
    )
    """Total online friends number."""


class FriendsRequestsMutual(BaseModel):
    """Model: `FriendsRequestsMutual`"""

    count: int | None = Field(
        default=None,
    )
    """Total mutual friends number."""

    users: list[int] | None = Field(
        default=None,
    )
    """Property `FriendsRequestsMutual.users`."""


class UtilsDomainResolved(BaseModel):
    """Model: `UtilsDomainResolved`"""

    object_id: int | None = Field(
        default=None,
    )
    """Object ID."""

    group_id: int | None = Field(
        default=None,
    )
    """Group ID."""

    type: "UtilsDomainResolvedType | None" = Field(
        default=None,
    )
    """Property `UtilsDomainResolved.type`."""


class UtilsDomainResolvedType(StrEnum, metaclass=BaseEnumMeta):
    USER = "user"
    GROUP = "group"
    APPLICATION = "application"
    EVENT = "event"
    PAGE = "page"
    VK_APP = "vk_app"
    COMMUNITY_APPLICATION = "community_application"


class UtilsLastShortenedLink(BaseModel):
    """Model: `UtilsLastShortenedLink`"""

    access_key: str | None = Field(
        default=None,
    )
    """Access key for private stats."""

    key: str | None = Field(
        default=None,
    )
    """Link key (characters after vk.cc/)."""

    short_url: str | None = Field(
        default=None,
    )
    """Short link URL."""

    timestamp: int | None = Field(
        default=None,
    )
    """Creation time in Unixtime."""

    url: str | None = Field(
        default=None,
    )
    """Full URL."""

    views: int | None = Field(
        default=None,
    )
    """Total views number."""


class UtilsLinkChecked(BaseModel):
    """Model: `UtilsLinkChecked`"""

    link: str | None = Field(
        default=None,
    )
    """Link URL."""

    status: "UtilsLinkCheckedStatus | None" = Field(
        default=None,
    )
    """Property `UtilsLinkChecked.status`."""


class UtilsLinkCheckedStatus(StrEnum, metaclass=BaseEnumMeta):
    NOT_BANNED = "not_banned"
    BANNED = "banned"
    PROCESSING = "processing"


class UtilsLinkStats(BaseModel):
    """Model: `UtilsLinkStats`"""

    key: str | None = Field(
        default=None,
    )
    """Link key (characters after vk.cc/)."""

    stats: list["UtilsStats"] | None = Field(
        default=None,
    )
    """Property `UtilsLinkStats.stats`."""


class UtilsLinkStatsExtended(BaseModel):
    """Model: `UtilsLinkStatsExtended`"""

    key: str | None = Field(
        default=None,
    )
    """Link key (characters after vk.cc/)."""

    stats: list["UtilsStatsExtended"] | None = Field(
        default=None,
    )
    """Property `UtilsLinkStatsExtended.stats`."""


class UtilsShortLink(BaseModel):
    """Model: `UtilsShortLink`"""

    access_key: str | None = Field(
        default=None,
    )
    """Access key for private stats."""

    key: str | None = Field(
        default=None,
    )
    """Link key (characters after vk.cc/)."""

    short_url: str | None = Field(
        default=None,
    )
    """Short link URL."""

    url: str | None = Field(
        default=None,
    )
    """Full URL."""


class UtilsStats(BaseModel):
    """Model: `UtilsStats`"""

    timestamp: int | None = Field(
        default=None,
    )
    """Start time."""

    views: int | None = Field(
        default=None,
    )
    """Total views number."""


class UtilsStatsCity(BaseModel):
    """Model: `UtilsStatsCity`"""

    city_id: int | None = Field(
        default=None,
    )
    """City ID."""

    views: int | None = Field(
        default=None,
    )
    """Views number."""


class UtilsStatsCountry(BaseModel):
    """Model: `UtilsStatsCountry`"""

    country_id: int | None = Field(
        default=None,
    )
    """Country ID."""

    views: int | None = Field(
        default=None,
    )
    """Views number."""


class UtilsStatsExtended(BaseModel):
    """Model: `UtilsStatsExtended`"""

    cities: list["UtilsStatsCity"] | None = Field(
        default=None,
    )
    """Property `UtilsStatsExtended.cities`."""

    countries: list["UtilsStatsCountry"] | None = Field(
        default=None,
    )
    """Property `UtilsStatsExtended.countries`."""

    sex_age: list["UtilsStatsSexAge"] | None = Field(
        default=None,
    )
    """Property `UtilsStatsExtended.sex_age`."""

    timestamp: int | None = Field(
        default=None,
    )
    """Start time."""

    views: int | None = Field(
        default=None,
    )
    """Total views number."""


class UtilsStatsSexAge(BaseModel):
    """Model: `UtilsStatsSexAge`"""

    age_range: str | None = Field(
        default=None,
    )
    """Age denotation."""

    female: int | None = Field(
        default=None,
    )
    """ Views by female users."""

    male: int | None = Field(
        default=None,
    )
    """ Views by male users."""


class VideoEpisode(BaseModel):
    """Model: `VideoEpisode`"""

    time: int | None = Field(
        default=None,
    )
    """Seconds from start of the video."""

    text: str | None = Field(
        default=None,
    )
    """Description of episode."""


class VideoLiveCategory(BaseModel):
    """Model: `VideoLiveCategory`"""

    id: int = Field()
    """Property `VideoLiveCategory.id`."""

    label: str = Field()
    """Property `VideoLiveCategory.label`."""

    sublist: list["VideoLiveCategory"] | None = Field(
        default=None,
    )
    """Property `VideoLiveCategory.sublist`."""


class VideoLiveInfo(BaseModel):
    """Model: `VideoLiveInfo`"""

    enabled: bool = Field()
    """Property `VideoLiveInfo.enabled`."""

    is_notifications_blocked: bool | None = Field(
        default=None,
    )
    """Property `VideoLiveInfo.is_notifications_blocked`."""


class VideoLiveSettings(BaseModel):
    """Video live settings
    Model: `VideoLiveSettings`
    """

    can_rewind: bool | None = Field(
        default=None,
    )
    """If user car rewind live or not."""

    is_endless: bool | None = Field(
        default=None,
    )
    """If live is endless or not."""

    max_duration: int | None = Field(
        default=None,
    )
    """Max possible time for rewind."""

    is_clips_live: bool | None = Field(
        default=None,
    )
    """If live in clips apps."""


class VideoPlaylistPrivacyCategory(StrEnum, metaclass=BaseEnumMeta):
    ALL = "all"
    FRIENDS = "friends"
    FRIENDS_OF_FRIENDS = "friends_of_friends"
    FRIENDS_OF_FRIENDS_ONLY = "friends_of_friends_only"
    ONLY_ME = "only_me"


class VideoSaveResult(BaseModel):
    """Model: `VideoSaveResult`"""

    access_key: str | None = Field(
        default=None,
    )
    """Video access key."""

    description: str | None = Field(
        default=None,
    )
    """Video description."""

    owner_id: int | None = Field(
        default=None,
    )
    """Video owner ID."""

    title: str | None = Field(
        default=None,
    )
    """Video title."""

    upload_url: str | None = Field(
        default=None,
    )
    """URL for the video uploading."""

    video_id: int | None = Field(
        default=None,
    )
    """Video ID."""


class VideoStreamInputParams(BaseModel):
    """Model: `VideoStreamInputParams`"""

    url: str | None = Field(
        default=None,
    )
    """Property `VideoStreamInputParams.url`."""

    key: str | None = Field(
        default=None,
    )
    """Property `VideoStreamInputParams.key`."""

    okmp_url: str | None = Field(
        default=None,
    )
    """Property `VideoStreamInputParams.okmp_url`."""

    webrtc_url: str | None = Field(
        default=None,
    )
    """Property `VideoStreamInputParams.webrtc_url`."""


class VideoVideoResponseType(StrEnum, metaclass=BaseEnumMeta):
    MIN = "min"
    FULL = "full"


class VideoVideoType(StrEnum, metaclass=BaseEnumMeta):
    INTERACTIVE = "interactive"
    VIDEO = "video"
    MUSIC_VIDEO = "music_video"
    MOVIE = "movie"
    LIVE = "live"
    SHORT_VIDEO = "short_video"
    STORY = "story"
    VIDEO_MESSAGE = "video_message"


class VideoVideo(BaseModel):
    """Model: `VideoVideo`"""

    response_type: "VideoVideoResponseType | None" = Field(
        default=None,
    )
    """Property `VideoVideo.response_type`."""

    access_key: str | None = Field(
        default=None,
    )
    """Video access key."""

    adding_date: datetime.datetime | None = Field(
        default=None,
    )
    """Date when the video has been added in Unixtime."""

    can_comment: bool | None = Field(
        default=None,
    )
    """Information whether current user can comment the video."""

    can_edit: bool | None = Field(
        default=None,
    )
    """Information whether current user can edit the video."""

    can_delete: bool | None = Field(
        default=None,
    )
    """Information whether current user can delete the video."""

    can_like: bool | None = Field(
        default=None,
    )
    """Information whether current user can like the video."""

    can_repost: int | None = Field(
        default=None,
    )
    """Information whether current user can repost the video."""

    can_subscribe: bool | None = Field(
        default=None,
    )
    """Information whether current user can subscribe to author of the video."""

    can_be_promoted: bool | None = Field(
        default=None,
    )
    """Information whether current user can promote the video."""

    can_add_to_faves: bool | None = Field(
        default=None,
    )
    """Information whether current user can add the video to favourites."""

    can_add: bool | None = Field(
        default=None,
    )
    """Information whether current user can add the video."""

    can_attach_link: bool | None = Field(
        default=None,
    )
    """Information whether current user can attach action button to the video."""

    can_edit_privacy: bool | None = Field(
        default=None,
    )
    """Information whether current user can edit the video privacy."""

    is_private: bool | None = Field(
        default=None,
    )
    """1 if video is private."""

    comments: int | None = Field(
        default=None,
    )
    """Number of comments."""

    date: datetime.datetime | None = Field(
        default=None,
    )
    """Date when video has been uploaded in Unixtime."""

    description: str | None = Field(
        default=None,
    )
    """Video description."""

    duration: int | None = Field(
        default=None,
    )
    """Video duration in seconds."""

    image: list["VideoVideoImage"] | None = Field(
        default=None,
    )
    """Property `VideoVideo.image`."""

    first_frame: list["VideoVideoImage"] | None = Field(
        default=None,
    )
    """Property `VideoVideo.first_frame`."""

    width: int | None = Field(
        default=None,
    )
    """Video width."""

    height: int | None = Field(
        default=None,
    )
    """Video height."""

    id: int | None = Field(
        default=None,
    )
    """Video ID."""

    owner_id: int | None = Field(
        default=None,
    )
    """Video owner ID."""

    user_id: int | None = Field(
        default=None,
    )
    """Id of the user who uploaded the video if it was uploaded to a group by member."""

    title: str | None = Field(
        default=None,
    )
    """Video title."""

    is_favorite: bool | None = Field(
        default=None,
    )
    """Whether video is added to bookmarks."""

    player: str | None = Field(
        default=None,
    )
    """Video embed URL."""

    processing: "BasePropertyExists | None" = Field(
        default=None,
    )
    """Returns if the video is processing."""

    converting: bool | None = Field(
        default=None,
    )
    """1 if  video is being converted."""

    added: bool | None = Field(
        default=None,
    )
    """1 if video is added to user\'s albums."""

    is_subscribed: bool | None = Field(
        default=None,
    )
    """1 if user is subscribed to author of the video."""

    track_code: str | None = Field(
        default=None,
    )
    """Property `VideoVideo.track_code`."""

    repeat: "BasePropertyExists | None" = Field(
        default=None,
    )
    """Information whether the video is repeated."""

    type: "VideoVideoType | None" = Field(
        default=None,
    )
    """Property `VideoVideo.type`."""

    views: int | None = Field(
        default=None,
    )
    """Number of views."""

    local_views: int | None = Field(
        default=None,
    )
    """If video is external, number of views on vk."""

    content_restricted: int | None = Field(
        default=None,
    )
    """Restriction code."""

    content_restricted_message: str | None = Field(
        default=None,
    )
    """Restriction text."""

    balance: int | None = Field(
        default=None,
    )
    """Live donations balance."""

    live: "BasePropertyExists | None" = Field(
        default=None,
    )
    """1 if the video is a live stream."""

    upcoming: "BasePropertyExists | None" = Field(
        default=None,
    )
    """1 if the video is an upcoming stream."""

    live_start_time: int | None = Field(
        default=None,
    )
    """Date in Unixtime when the live stream is scheduled to start by the author."""

    live_notify: bool | None = Field(
        default=None,
    )
    """Whether current user is subscribed to the upcoming live stream notification (if not subscribed to the author)."""

    spectators: int | None = Field(
        default=None,
    )
    """Number of spectators of the stream."""

    platform: str | None = Field(
        default=None,
    )
    """External platform."""

    likes: "BaseLikes | None" = Field(
        default=None,
    )
    """Property `VideoVideo.likes`."""

    reposts: "BaseRepostsInfo | None" = Field(
        default=None,
    )
    """Property `VideoVideo.reposts`."""


class VideoVideoAlbumResponseType(StrEnum, metaclass=BaseEnumMeta):
    MIN = "min"
    FULL = "full"


class VideoVideoAlbum(BaseModel):
    """Model: `VideoVideoAlbum`"""

    id: int = Field()
    """Album ID."""

    owner_id: int = Field()
    """Album owner\'s ID."""

    title: str = Field()
    """Album title."""

    track_code: str | None = Field(
        default=None,
    )
    """Album trackcode."""

    response_type: "VideoVideoAlbumResponseType | None" = Field(
        default=None,
    )
    """Property `VideoVideoAlbum.response_type`."""


class VideoVideoFiles(BaseModel):
    """Model: `VideoVideoFiles`"""

    external: str | None = Field(
        default=None,
    )
    """URL of the external player."""

    mp4_144: str | None = Field(
        default=None,
    )
    """URL of the mpeg4 file with 144p quality."""

    mp4_240: str | None = Field(
        default=None,
    )
    """URL of the mpeg4 file with 240p quality."""

    mp4_360: str | None = Field(
        default=None,
    )
    """URL of the mpeg4 file with 360p quality."""

    mp4_480: str | None = Field(
        default=None,
    )
    """URL of the mpeg4 file with 480p quality."""

    mp4_720: str | None = Field(
        default=None,
    )
    """URL of the mpeg4 file with 720p quality."""

    mp4_1080: str | None = Field(
        default=None,
    )
    """URL of the mpeg4 file with 1080p quality."""

    mp4_1440: str | None = Field(
        default=None,
    )
    """URL of the mpeg4 file with 2K quality."""

    mp4_2160: str | None = Field(
        default=None,
    )
    """URL of the mpeg4 file with 4K quality."""

    flv_320: str | None = Field(
        default=None,
    )
    """URL of the flv file with 320p quality."""


class WallAppPost(BaseModel):
    """Model: `WallAppPost`"""

    id: int | None = Field(
        default=None,
    )
    """Application ID."""

    name: str | None = Field(
        default=None,
    )
    """Application name."""

    photo_130: str | None = Field(
        default=None,
    )
    """URL of the preview image with 130 px in width."""

    photo_604: str | None = Field(
        default=None,
    )
    """URL of the preview image with 604 px in width."""


class WallAttachedNote(BaseModel):
    """Model: `WallAttachedNote`"""

    comments: int = Field()
    """Comments number."""

    date: datetime.datetime = Field()
    """Date when the note has been created in Unixtime."""

    id: int = Field()
    """Note ID."""

    owner_id: int = Field()
    """Note owner\'s ID."""

    read_comments: int = Field()
    """Read comments number."""

    title: str = Field()
    """Note title."""

    view_url: str = Field()
    """URL of the page with note preview."""

    text: str | None = Field(
        default=None,
    )
    """Note text."""

    privacy_view: list[str] | None = Field(
        default=None,
    )
    """Property `WallAttachedNote.privacy_view`."""

    privacy_comment: list[str] | None = Field(
        default=None,
    )
    """Property `WallAttachedNote.privacy_comment`."""

    can_comment: int | None = Field(
        default=None,
    )
    """Property `WallAttachedNote.can_comment`."""

    text_wiki: str | None = Field(
        default=None,
    )
    """Note wiki text."""


class WallCarouselBase(BaseModel):
    """Model: `WallCarouselBase`"""

    carousel_offset: int | None = Field(
        default=None,
    )
    """Index of current carousel element."""


class WallCommentAttachment(BaseModel):
    """Model: `WallCommentAttachment`"""

    type: "WallCommentAttachmentType" = Field()
    """Property `WallCommentAttachment.type`."""

    audio: "AudioAudio | None" = Field(
        default=None,
    )
    """Property `WallCommentAttachment.audio`."""

    doc: "DocsDoc | None" = Field(
        default=None,
    )
    """Property `WallCommentAttachment.doc`."""

    link: "BaseLink | None" = Field(
        default=None,
    )
    """Property `WallCommentAttachment.link`."""

    market: "MarketMarketItem | None" = Field(
        default=None,
    )
    """Property `WallCommentAttachment.market`."""

    market_market_album: "MarketMarketAlbum | None" = Field(
        default=None,
    )
    """Property `WallCommentAttachment.market_market_album`."""

    note: "WallAttachedNote | None" = Field(
        default=None,
    )
    """Property `WallCommentAttachment.note`."""

    page: "PagesWikipageFull | None" = Field(
        default=None,
    )
    """Property `WallCommentAttachment.page`."""

    photo: "PhotosPhoto | None" = Field(
        default=None,
    )
    """Property `WallCommentAttachment.photo`."""

    sticker: "BaseSticker | None" = Field(
        default=None,
    )
    """Property `WallCommentAttachment.sticker`."""

    video: "VideoVideo | None" = Field(
        default=None,
    )
    """Property `WallCommentAttachment.video`."""

    graffiti: "WallGraffiti | None" = Field(
        default=None,
    )
    """Property `WallCommentAttachment.graffiti`."""


class WallCommentAttachmentType(StrEnum, metaclass=BaseEnumMeta):
    PHOTO = "photo"
    AUDIO = "audio"
    AUDIO_PLAYLIST = "audio_playlist"
    VIDEO = "video"
    DOC = "doc"
    LINK = "link"
    NOTE = "note"
    PAGE = "page"
    MARKET_MARKET_ALBUM = "market_market_album"
    MARKET = "market"
    STICKER = "sticker"
    GRAFFITI = "graffiti"


class WallGeoType(StrEnum, metaclass=BaseEnumMeta):
    PLACE = "place"
    POINT = "point"


class WallGeo(BaseModel):
    """Model: `WallGeo`"""

    coordinates: str | None = Field(
        default=None,
    )
    """Coordinates as string. <latitude> <longtitude>."""

    showmap: int | None = Field(
        default=None,
    )
    """Information whether a map is showed."""

    type: "WallGeoType | None" = Field(
        default=None,
    )
    """Place type."""


class WallGetFilter(StrEnum, metaclass=BaseEnumMeta):
    OWNER = "owner"
    OTHERS = "others"
    ALL = "all"
    POSTPONED = "postponed"
    SUGGESTS = "suggests"
    ARCHIVED = "archived"
    DONUT = "donut"


class WallGraffiti(BaseModel):
    """Model: `WallGraffiti`"""

    id: int | None = Field(
        default=None,
    )
    """Graffiti ID."""

    owner_id: int | None = Field(
        default=None,
    )
    """Graffiti owner\'s ID."""

    photo_200: str | None = Field(
        default=None,
    )
    """URL of the preview image with 200 px in width."""

    photo_586: str | None = Field(
        default=None,
    )
    """URL of the preview image with 586 px in width."""

    height: int | None = Field(
        default=None,
    )
    """Graffiti height."""

    url: str | None = Field(
        default=None,
    )
    """Graffiti URL."""

    width: int | None = Field(
        default=None,
    )
    """Graffiti width."""

    access_key: str | None = Field(
        default=None,
    )
    """Access key for graffiti."""


class WallPostCopyright(BaseModel):
    """Model: `WallPostCopyright`"""

    link: str = Field()
    """Property `WallPostCopyright.link`."""

    name: str = Field()
    """Property `WallPostCopyright.name`."""

    type: str = Field()
    """Property `WallPostCopyright.type`."""

    id: int | None = Field(
        default=None,
    )
    """Property `WallPostCopyright.id`."""


class WallPostSource(BaseModel):
    """Model: `WallPostSource`"""

    data: str | None = Field(
        default=None,
    )
    """Additional data."""

    platform: str | None = Field(
        default=None,
    )
    """Platform name."""

    type: "WallPostSourceType | None" = Field(
        default=None,
    )
    """Property `WallPostSource.type`."""

    url: str | None = Field(
        default=None,
    )
    """URL to an external site used to publish the post."""

    link: "BaseLink | None" = Field(
        default=None,
    )
    """Property `WallPostSource.link`."""


class WallPostSourceType(StrEnum, metaclass=BaseEnumMeta):
    VK = "vk"
    WIDGET = "widget"
    API = "api"
    RSS = "rss"
    SMS = "sms"
    MVK = "mvk"


class WallPostType(StrEnum, metaclass=BaseEnumMeta):
    POST = "post"
    COPY = "copy"
    REPLY = "reply"
    POSTPONE = "postpone"
    SUGGEST = "suggest"
    POST_ADS = "post_ads"
    PHOTO = "photo"
    VIDEO = "video"
    CLIP = "clip"


class WallPostedPhoto(BaseModel):
    """Model: `WallPostedPhoto`"""

    id: int | None = Field(
        default=None,
    )
    """Photo ID."""

    owner_id: int | None = Field(
        default=None,
    )
    """Photo owner\'s ID."""

    photo_130: str | None = Field(
        default=None,
    )
    """URL of the preview image with 130 px in width."""

    photo_604: str | None = Field(
        default=None,
    )
    """URL of the preview image with 604 px in width."""


class WallViews(BaseModel):
    """Model: `WallViews`"""

    count: int | None = Field(
        default=None,
    )
    """Count."""


class WallWallComment(BaseModel):
    """Model: `WallWallComment`"""

    id: int = Field()
    """Comment ID."""

    from_id: int = Field()
    """Author ID."""

    date: datetime.datetime = Field()
    """Date when the comment has been added in Unixtime."""

    text: str = Field()
    """Comment text."""

    can_edit: bool | None = Field(
        default=None,
    )
    """Property `WallWallComment.can_edit`."""

    post_id: int | None = Field(
        default=None,
    )
    """Property `WallWallComment.post_id`."""

    owner_id: int | None = Field(
        default=None,
    )
    """Property `WallWallComment.owner_id`."""

    parents_stack: list[int] | None = Field(
        default=None,
    )
    """Property `WallWallComment.parents_stack`."""

    photo_id: int | None = Field(
        default=None,
    )
    """Property `WallWallComment.photo_id`."""

    video_id: int | None = Field(
        default=None,
    )
    """Property `WallWallComment.video_id`."""

    attachments: list["WallWallpostAttachment"] | None = Field(
        default=None,
    )
    """Property `WallWallComment.attachments`."""

    donut: "WallWallCommentDonut | None" = Field(
        default=None,
    )
    """Property `WallWallComment.donut`."""

    likes: "BaseLikesInfo | None" = Field(
        default=None,
    )
    """Property `WallWallComment.likes`."""

    real_offset: int | None = Field(
        default=None,
    )
    """Real position of the comment."""

    reply_to_user: int | None = Field(
        default=None,
    )
    """Replied user ID."""

    reply_to_comment: int | None = Field(
        default=None,
    )
    """Replied comment ID."""

    thread: "CommentThread | None" = Field(
        default=None,
    )
    """Property `WallWallComment.thread`."""

    is_from_post_author: bool | None = Field(
        default=None,
    )
    """Whether post is by author of the post or not."""

    deleted: bool | None = Field(
        default=None,
    )
    """Property `WallWallComment.deleted`."""

    pid: int | None = Field(
        default=None,
    )
    """Photo ID."""


class WallWallCommentDonut(BaseModel):
    """Model: `WallWallCommentDonut`"""

    is_don: bool | None = Field(
        default=None,
    )
    """Means commentator is donator."""

    placeholder: "WallWallCommentDonutPlaceholder | None" = Field(
        default=None,
    )
    """Property `WallWallCommentDonut.placeholder`."""


class WallWallCommentDonutPlaceholder(BaseModel):
    """Model: `WallWallCommentDonutPlaceholder`"""

    text: str = Field()
    """Property `WallWallCommentDonutPlaceholder.text`."""


class WallWallItem(BaseModel):
    """Model: `WallWallItem`"""

    copy_history: list["WallWallpostFull"] | None = Field(
        default=None,
    )
    """Property `WallWallItem.copy_history`."""

    can_edit: bool | None = Field(
        default=None,
    )
    """Information whether current user can edit the post."""

    created_by: int | None = Field(
        default=None,
    )
    """Post creator ID (if post still can be edited)."""

    can_delete: bool | None = Field(
        default=None,
    )
    """Information whether current user can delete the post."""

    can_pin: bool | None = Field(
        default=None,
    )
    """Information whether current user can pin the post."""

    donut: "WallWallpostDonut | None" = Field(
        default=None,
    )
    """Property `WallWallItem.donut`."""

    is_pinned: bool | None = Field(
        default=None,
    )
    """Information whether the post is pinned."""

    comments: "BaseCommentsInfo | None" = Field(
        default=None,
    )
    """Property `WallWallItem.comments`."""

    marked_as_ads: bool | None = Field(
        default=None,
    )
    """Information whether the post is marked as ads."""

    topic_id: int | None = Field(
        default=None,
    )
    """Topic ID. Allowed values can be obtained from newsfeed.getPostTopics method."""

    short_text_rate: float | None = Field(
        default=None,
    )
    """Preview length control parameter."""

    hash: str | None = Field(
        default=None,
    )
    """Hash for sharing."""

    type: "WallPostType | None" = Field(
        default=None,
    )
    """Property `WallWallItem.type`."""

    feedback: "NewsfeedItemWallpostFeedback | None" = Field(
        default=None,
    )
    """Property `WallWallItem.feedback`."""

    to_id: int | None = Field(
        default=None,
    )
    """Property `WallWallItem.to_id`."""


class WallWallpostInnerType(StrEnum, metaclass=BaseEnumMeta):
    WALL_WALLPOST = "wall_wallpost"


class WallWallpost(BaseModel):
    """Model: `WallWallpost`"""

    inner_type: "WallWallpostInnerType" = Field()
    """Property `WallWallpost.inner_type`."""

    access_key: str | None = Field(
        default=None,
    )
    """Access key to private object."""

    is_deleted: bool | None = Field(
        default=None,
    )
    """Property `WallWallpost.is_deleted`."""

    deleted_reason: str | None = Field(
        default=None,
    )
    """Property `WallWallpost.deleted_reason`."""

    deleted_details: str | None = Field(
        default=None,
    )
    """Property `WallWallpost.deleted_details`."""

    donut_miniapp_url: str | None = Field(
        default=None,
    )
    """Property `WallWallpost.donut_miniapp_url`."""

    attachments: list["WallWallpostAttachment"] | None = Field(
        default=None,
    )
    """Property `WallWallpost.attachments`."""

    copyright: "WallPostCopyright | None" = Field(
        default=None,
    )
    """Information about the source of the post."""

    date: datetime.datetime | None = Field(
        default=None,
    )
    """Date of publishing in Unixtime."""

    edited: int | None = Field(
        default=None,
    )
    """Date of editing in Unixtime."""

    from_id: int | None = Field(
        default=None,
    )
    """Post author ID."""

    geo: "WallGeo | None" = Field(
        default=None,
    )
    """Property `WallWallpost.geo`."""

    id: int | None = Field(
        default=None,
    )
    """Post ID."""

    is_archived: bool | None = Field(
        default=None,
    )
    """Is post archived, only for post owners."""

    is_favorite: bool | None = Field(
        default=None,
    )
    """Information whether the post in favorites list."""

    likes: "BaseLikesInfo | None" = Field(
        default=None,
    )
    """Count of likes."""

    owner_id: int | None = Field(
        default=None,
    )
    """Wall owner\'s ID."""

    post_id: int | None = Field(
        default=None,
    )
    """If post type \'reply\', contains original post ID."""

    parents_stack: list[int] | None = Field(
        default=None,
    )
    """If post type \'reply\', contains original parent IDs stack."""

    post_source: "WallPostSource | None" = Field(
        default=None,
    )
    """Property `WallWallpost.post_source`."""

    post_type: "WallPostType | None" = Field(
        default=None,
    )
    """Property `WallWallpost.post_type`."""

    reposts: "BaseRepostsInfo | None" = Field(
        default=None,
    )
    """Property `WallWallpost.reposts`."""

    signer_id: int | None = Field(
        default=None,
    )
    """Post signer ID."""

    text: str | None = Field(
        default=None,
    )
    """Post text."""

    views: "WallViews | None" = Field(
        default=None,
    )
    """Count of views."""


class WallWallpostAttachment(BaseModel):
    """Model: `WallWallpostAttachment`"""

    type: "WallWallpostAttachmentType" = Field()
    """Property `WallWallpostAttachment.type`."""

    access_key: str | None = Field(
        default=None,
    )
    """Access key for the audio."""

    album: "PhotosPhotoAlbum | None" = Field(
        default=None,
    )
    """Property `WallWallpostAttachment.album`."""

    app: "WallAppPost | None" = Field(
        default=None,
    )
    """Property `WallWallpostAttachment.app`."""

    audio: "AudioAudio | None" = Field(
        default=None,
    )
    """Property `WallWallpostAttachment.audio`."""

    doc: "DocsDoc | None" = Field(
        default=None,
    )
    """Property `WallWallpostAttachment.doc`."""

    event: "EventsEventAttach | None" = Field(
        default=None,
    )
    """Property `WallWallpostAttachment.event`."""

    group: "GroupsGroupAttach | None" = Field(
        default=None,
    )
    """Property `WallWallpostAttachment.group`."""

    graffiti: "WallGraffiti | None" = Field(
        default=None,
    )
    """Property `WallWallpostAttachment.graffiti`."""

    link: "BaseLink | None" = Field(
        default=None,
    )
    """Property `WallWallpostAttachment.link`."""

    market: "MarketMarketItem | None" = Field(
        default=None,
    )
    """Property `WallWallpostAttachment.market`."""

    market_album: "MarketMarketAlbum | None" = Field(
        default=None,
    )
    """Property `WallWallpostAttachment.market_album`."""

    note: "NotesNote | None" = Field(
        default=None,
    )
    """Property `WallWallpostAttachment.note`."""

    page: "PagesWikipageFull | None" = Field(
        default=None,
    )
    """Property `WallWallpostAttachment.page`."""

    photo: "PhotosPhoto | None" = Field(
        default=None,
    )
    """Property `WallWallpostAttachment.photo`."""

    poll: "PollsPoll | None" = Field(
        default=None,
    )
    """Property `WallWallpostAttachment.poll`."""

    posted_photo: "WallPostedPhoto | None" = Field(
        default=None,
    )
    """Property `WallWallpostAttachment.posted_photo`."""

    video: "VideoVideoFull | None" = Field(
        default=None,
    )
    """Property `WallWallpostAttachment.video`."""

    clip: "VideoVideoFull | None" = Field(
        default=None,
    )
    """Property `WallWallpostAttachment.clip`."""

    video_playlist: "VideoVideoAlbumFull | None" = Field(
        default=None,
    )
    """Property `WallWallpostAttachment.video_playlist`."""


class WallWallpostAttachmentType(StrEnum, metaclass=BaseEnumMeta):
    PHOTO = "photo"
    PHOTOS_LIST = "photos_list"
    POSTED_PHOTO = "posted_photo"
    AUDIO = "audio"
    AUDIO_PLAYLIST = "audio_playlist"
    VIDEO = "video"
    CLIP = "clip"
    VIDEO_PLAYLIST = "video_playlist"
    DOC = "doc"
    LINK = "link"
    GRAFFITI = "graffiti"
    NOTE = "note"
    APP = "app"
    POLL = "poll"
    PAGE = "page"
    ALBUM = "album"
    MARKET_ALBUM = "market_album"
    MARKET = "market"
    EVENT = "event"
    DONUT_LINK = "donut_link"
    ARTICLE = "article"
    TEXTLIVE = "textlive"
    TEXTPOST = "textpost"
    TEXTPOST_PUBLISH = "textpost_publish"
    SITUATIONAL_THEME = "situational_theme"
    GROUP = "group"
    STICKER = "sticker"
    PODCAST = "podcast"


class WallWallpostCommentsDonut(BaseModel):
    """Model: `WallWallpostCommentsDonut`"""

    placeholder: "WallWallpostCommentsDonutPlaceholder | None" = Field(
        default=None,
    )
    """Property `WallWallpostCommentsDonut.placeholder`."""


class WallWallpostCommentsDonutPlaceholder(BaseModel):
    """Info about paid comments feature
    Model: `WallWallpostCommentsDonutPlaceholder`
    """

    text: str = Field()
    """Property `WallWallpostCommentsDonutPlaceholder.text`."""


class WallWallpostDonutEditMode(StrEnum, metaclass=BaseEnumMeta):
    ALL = "all"
    DURATION = "duration"


class WallWallpostDonut(BaseModel):
    """Info about paid wall post
    Model: `WallWallpostDonut`
    """

    is_donut: bool = Field()
    """Post only for dons."""

    paid_duration: int | None = Field(
        default=None,
    )
    """Value of this field need to pass in wall.post/edit in donut_paid_duration."""

    placeholder: "WallWallpostDonutPlaceholder | None" = Field(
        default=None,
    )
    """If placeholder was respond, text and all attachments will be hidden."""

    can_publish_free_copy: bool | None = Field(
        default=None,
    )
    """Says whether group admin can post free copy of this donut post."""

    edit_mode: "WallWallpostDonutEditMode | None" = Field(
        default=None,
    )
    """Says what user can edit in post about donut properties."""


class WallWallpostDonutPlaceholder(BaseModel):
    """Model: `WallWallpostDonutPlaceholder`"""

    text: str = Field()
    """Property `WallWallpostDonutPlaceholder.text`."""


class NewsfeedCommentsFilters(StrEnum, metaclass=BaseEnumMeta):
    POST = "post"
    PHOTO = "photo"
    VIDEO = "video"
    TOPIC = "topic"
    NOTE = "note"


class NewsfeedCommentsItem(BaseModel):
    """Model: `NewsfeedCommentsItem`"""


class NewsfeedCommentsItemBase(BaseModel):
    """Model: `NewsfeedCommentsItemBase`"""

    type: "NewsfeedNewsfeedItemType" = Field()
    """Property `NewsfeedCommentsItemBase.type`."""

    source_id: int | None = Field(
        default=None,
    )
    """Property `NewsfeedCommentsItemBase.source_id`."""

    date: datetime.datetime | None = Field(
        default=None,
    )
    """Property `NewsfeedCommentsItemBase.date`."""

    post_id: int | None = Field(
        default=None,
    )
    """Property `NewsfeedCommentsItemBase.post_id`."""


class NewsfeedIgnoreItemType(StrEnum, metaclass=BaseEnumMeta):
    WALL = "wall"
    TAG = "tag"
    PROFILEPHOTO = "profilephoto"
    VIDEO = "video"
    PHOTO = "photo"
    AUDIO = "audio"


class NewsfeedItemAudioAudio(BaseModel):
    """Model: `NewsfeedItemAudioAudio`"""

    count: int | None = Field(
        default=None,
    )
    """Audios number."""

    items: list["AudioAudio"] | None = Field(
        default=None,
    )
    """Property `NewsfeedItemAudioAudio.items`."""


class NewsfeedItemBase(BaseModel):
    """Model: `NewsfeedItemBase`"""

    type: "NewsfeedNewsfeedItemType" = Field()
    """Property `NewsfeedItemBase.type`."""

    source_id: int = Field()
    """Item source ID."""

    date: datetime.datetime = Field()
    """Date when item has been added in Unixtime."""

    short_text_rate: float | None = Field(
        default=None,
    )
    """Preview length control parameter."""

    feedback: "NewsfeedItemWallpostFeedback | None" = Field(
        default=None,
    )
    """Property `NewsfeedItemBase.feedback`."""


class NewsfeedItemDigestButtonStyle(StrEnum, metaclass=BaseEnumMeta):
    PRIMARY = "primary"


class NewsfeedItemDigestButton(BaseModel):
    """Model: `NewsfeedItemDigestButton`"""

    title: str = Field()
    """Property `NewsfeedItemDigestButton.title`."""

    style: "NewsfeedItemDigestButtonStyle | None" = Field(
        default=None,
    )
    """Property `NewsfeedItemDigestButton.style`."""


class NewsfeedItemDigestFooterStyle(StrEnum, metaclass=BaseEnumMeta):
    TEXT = "text"
    BUTTON = "button"


class NewsfeedItemDigestFooter(BaseModel):
    """Model: `NewsfeedItemDigestFooter`"""

    style: "NewsfeedItemDigestFooterStyle" = Field()
    """Property `NewsfeedItemDigestFooter.style`."""

    text: str = Field()
    """text for invite to enable smart feed."""

    button: "NewsfeedItemDigestButton | None" = Field(
        default=None,
    )
    """Property `NewsfeedItemDigestFooter.button`."""

    feed_id: str | None = Field(
        default=None,
    )
    """Property `NewsfeedItemDigestFooter.feed_id`."""


class NewsfeedItemDigestHeaderStyle(StrEnum, metaclass=BaseEnumMeta):
    SINGLELINE = "singleline"
    MULTILINE = "multiline"


class NewsfeedItemDigestHeader(BaseModel):
    """Model: `NewsfeedItemDigestHeader`"""

    title: str = Field()
    """Title of the header."""

    style: "NewsfeedItemDigestHeaderStyle" = Field()
    """Property `NewsfeedItemDigestHeader.style`."""

    subtitle: str | None = Field(
        default=None,
    )
    """Subtitle of the header, when title have two strings."""

    badge_text: str | None = Field(
        default=None,
    )
    """Optional field for red badge in Trends feed blocks."""

    button: "NewsfeedItemDigestButton | None" = Field(
        default=None,
    )
    """Property `NewsfeedItemDigestHeader.button`."""


class NewsfeedItemDigestItem(BaseModel):
    """Model: `NewsfeedItemDigestItem`"""

    inner_type: str = Field()
    """Property `NewsfeedItemDigestItem.inner_type`."""

    post: "NewsfeedItemWallpost" = Field()
    """Property `NewsfeedItemDigestItem.post`."""

    text: str | None = Field(
        default=None,
    )
    """Property `NewsfeedItemDigestItem.text`."""

    source_name: str | None = Field(
        default=None,
    )
    """Property `NewsfeedItemDigestItem.source_name`."""

    attachment_index: int | None = Field(
        default=None,
    )
    """Property `NewsfeedItemDigestItem.attachment_index`."""

    attachment: "WallWallpostAttachment | None" = Field(
        default=None,
    )
    """Property `NewsfeedItemDigestItem.attachment`."""

    style: str | None = Field(
        default=None,
    )
    """Property `NewsfeedItemDigestItem.style`."""

    badge_text: str | None = Field(
        default=None,
    )
    """Optional red badge for posts in digest block."""


class NewsfeedItemFriendFriends(BaseModel):
    """Model: `NewsfeedItemFriendFriends`"""

    count: int | None = Field(
        default=None,
    )
    """Number of friends has been added."""

    items: list["BaseUserId"] | None = Field(
        default=None,
    )
    """Property `NewsfeedItemFriendFriends.items`."""


class NewsfeedItemHolidayRecommendationsBlockHeader(BaseModel):
    """Model: `NewsfeedItemHolidayRecommendationsBlockHeader`"""

    title: str | None = Field(
        default=None,
    )
    """Title of the header."""

    subtitle: str | None = Field(
        default=None,
    )
    """Subtitle of the header."""

    image: list["BaseImage"] | None = Field(
        default=None,
    )
    """Property `NewsfeedItemHolidayRecommendationsBlockHeader.image`."""

    action: "BaseLinkButtonAction | None" = Field(
        default=None,
    )
    """Property `NewsfeedItemHolidayRecommendationsBlockHeader.action`."""


class NewsfeedItemPhotoPhotos(BaseModel):
    """Model: `NewsfeedItemPhotoPhotos`"""

    count: int | None = Field(
        default=None,
    )
    """Photos number."""

    items: list["PhotosPhoto"] | None = Field(
        default=None,
    )
    """Property `NewsfeedItemPhotoPhotos.items`."""


class NewsfeedItemPhotoTagPhotoTags(BaseModel):
    """Model: `NewsfeedItemPhotoTagPhotoTags`"""

    count: int | None = Field(
        default=None,
    )
    """Tags number."""

    items: list["PhotosPhoto"] | None = Field(
        default=None,
    )
    """Property `NewsfeedItemPhotoTagPhotoTags.items`."""


class NewsfeedItemPromoButtonAction(BaseModel):
    """Model: `NewsfeedItemPromoButtonAction`"""

    url: str | None = Field(
        default=None,
    )
    """Property `NewsfeedItemPromoButtonAction.url`."""

    type: str | None = Field(
        default=None,
    )
    """Property `NewsfeedItemPromoButtonAction.type`."""

    target: str | None = Field(
        default=None,
    )
    """Property `NewsfeedItemPromoButtonAction.target`."""


class NewsfeedItemPromoButtonImage(BaseModel):
    """Model: `NewsfeedItemPromoButtonImage`"""

    width: int | None = Field(
        default=None,
    )
    """Property `NewsfeedItemPromoButtonImage.width`."""

    height: int | None = Field(
        default=None,
    )
    """Property `NewsfeedItemPromoButtonImage.height`."""

    url: str | None = Field(
        default=None,
    )
    """Property `NewsfeedItemPromoButtonImage.url`."""


class NewsfeedItemVideoVideo(BaseModel):
    """Model: `NewsfeedItemVideoVideo`"""

    count: int | None = Field(
        default=None,
    )
    """Tags number."""

    items: list["VideoVideoFull"] | None = Field(
        default=None,
    )
    """Property `NewsfeedItemVideoVideo.items`."""


class NewsfeedItemWallpostFeedback(BaseModel):
    """Model: `NewsfeedItemWallpostFeedback`"""

    type: "NewsfeedItemWallpostFeedbackType" = Field()
    """Property `NewsfeedItemWallpostFeedback.type`."""

    question: str = Field()
    """Property `NewsfeedItemWallpostFeedback.question`."""

    answers: list["NewsfeedItemWallpostFeedbackAnswer"] | None = Field(
        default=None,
    )
    """Property `NewsfeedItemWallpostFeedback.answers`."""

    stars_count: int | None = Field(
        default=None,
    )
    """Property `NewsfeedItemWallpostFeedback.stars_count`."""

    descriptions: list[str] | None = Field(
        default=None,
    )
    """Property `NewsfeedItemWallpostFeedback.descriptions`."""

    gratitude: str | None = Field(
        default=None,
    )
    """Property `NewsfeedItemWallpostFeedback.gratitude`."""

    track_code: str | None = Field(
        default=None,
    )
    """Property `NewsfeedItemWallpostFeedback.track_code`."""


class NewsfeedItemWallpostFeedbackAnswer(BaseModel):
    """Model: `NewsfeedItemWallpostFeedbackAnswer`"""

    title: str = Field()
    """Property `NewsfeedItemWallpostFeedbackAnswer.title`."""

    id: str = Field()
    """Property `NewsfeedItemWallpostFeedbackAnswer.id`."""


class NewsfeedItemWallpostFeedbackType(StrEnum, metaclass=BaseEnumMeta):
    BUTTONS = "buttons"
    STARS = "stars"


class NewsfeedList(BaseModel):
    """Model: `NewsfeedList`"""

    id: int = Field()
    """List ID."""

    title: str = Field()
    """List title."""


class NewsfeedNewsfeedItem(BaseModel):
    """Model: `NewsfeedNewsfeedItem`"""


class NewsfeedNewsfeedItemType(StrEnum, metaclass=BaseEnumMeta):
    POST = "post"
    PHOTO = "photo"
    PHOTO_TAG = "photo_tag"
    WALL_PHOTO = "wall_photo"
    FRIEND = "friend"
    AUDIO = "audio"
    VIDEO = "video"
    TOPIC = "topic"
    DIGEST = "digest"
    STORIES = "stories"
    NOTE = "note"
    AUDIO_PLAYLIST = "audio_playlist"
    CLIP = "clip"
    CLIPS_RETENTION = "clips_retention"


class WidgetsCommentMedia(BaseModel):
    """Model: `WidgetsCommentMedia`"""

    item_id: int | None = Field(
        default=None,
    )
    """Media item ID."""

    owner_id: int | None = Field(
        default=None,
    )
    """Media owner\'s ID."""

    thumb_src: str | None = Field(
        default=None,
    )
    """URL of the preview image (type=photo only)."""

    type: "WidgetsCommentMediaType | None" = Field(
        default=None,
    )
    """Property `WidgetsCommentMedia.type`."""


class WidgetsCommentMediaType(StrEnum, metaclass=BaseEnumMeta):
    AUDIO = "audio"
    PHOTO = "photo"
    VIDEO = "video"


class WidgetsCommentReplies(BaseModel):
    """Model: `WidgetsCommentReplies`"""

    can_post: bool | None = Field(
        default=None,
    )
    """Information whether current user can comment the post."""

    count: int | None = Field(
        default=None,
    )
    """Comments number."""

    replies: list["WidgetsCommentRepliesItem"] | None = Field(
        default=None,
    )
    """Property `WidgetsCommentReplies.replies`."""

    groups_can_post: bool | None = Field(
        default=None,
    )
    """Information whether groups can comment the post."""

    can_view: bool | None = Field(
        default=None,
    )
    """Information whether current user can view the comments."""


class WidgetsCommentRepliesItem(BaseModel):
    """Model: `WidgetsCommentRepliesItem`"""

    cid: int | None = Field(
        default=None,
    )
    """Comment ID."""

    date: datetime.datetime | None = Field(
        default=None,
    )
    """Date when the comment has been added in Unixtime."""

    likes: "WidgetsWidgetLikes | None" = Field(
        default=None,
    )
    """Property `WidgetsCommentRepliesItem.likes`."""

    text: str | None = Field(
        default=None,
    )
    """Comment text."""

    uid: int | None = Field(
        default=None,
    )
    """User ID."""

    user: "UsersUserFull | None" = Field(
        default=None,
    )
    """Property `WidgetsCommentRepliesItem.user`."""


class WidgetsWidgetComment(BaseModel):
    """Model: `WidgetsWidgetComment`"""

    date: datetime.datetime = Field()
    """Date when the comment has been added in Unixtime."""

    from_id: int = Field()
    """Comment author ID."""

    id: int = Field()
    """Comment ID."""

    post_type: str = Field()
    """Post type."""

    text: str = Field()
    """Comment text."""

    to_id: int = Field()
    """Wall owner."""

    attachments: list["WallCommentAttachment"] | None = Field(
        default=None,
    )
    """Property `WidgetsWidgetComment.attachments`."""

    owner_id: int | None = Field(
        default=None,
    )
    """Wall owner\'s ID."""

    can_delete: bool | None = Field(
        default=None,
    )
    """Information whether current user can delete the comment."""

    comments: "WidgetsCommentReplies | None" = Field(
        default=None,
    )
    """Property `WidgetsWidgetComment.comments`."""

    likes: "BaseLikesInfo | None" = Field(
        default=None,
    )
    """Property `WidgetsWidgetComment.likes`."""

    media: "WidgetsCommentMedia | None" = Field(
        default=None,
    )
    """Property `WidgetsWidgetComment.media`."""

    post_source: "WallPostSource | None" = Field(
        default=None,
    )
    """Property `WidgetsWidgetComment.post_source`."""

    reposts: "BaseRepostsInfo | None" = Field(
        default=None,
    )
    """Property `WidgetsWidgetComment.reposts`."""

    user: "UsersUserFull | None" = Field(
        default=None,
    )
    """Property `WidgetsWidgetComment.user`."""

    is_favorite: bool | None = Field(
        default=None,
    )
    """Information whether the post in favorites list."""

    short_text_rate: float | None = Field(
        default=None,
    )
    """Preview length control parameter."""


class WidgetsWidgetLikes(BaseModel):
    """Model: `WidgetsWidgetLikes`"""

    count: int | None = Field(
        default=None,
    )
    """Likes number."""


class WidgetsWidgetPage(BaseModel):
    """Model: `WidgetsWidgetPage`"""

    comments: "BaseObjectCount | None" = Field(
        default=None,
    )
    """Property `WidgetsWidgetPage.comments`."""

    date: datetime.datetime | None = Field(
        default=None,
    )
    """Date when widgets on the page has been initialized firstly in Unixtime."""

    description: str | None = Field(
        default=None,
    )
    """Page description."""

    id: int | None = Field(
        default=None,
    )
    """Page ID."""

    likes: "BaseObjectCount | None" = Field(
        default=None,
    )
    """Property `WidgetsWidgetPage.likes`."""

    page_id: str | None = Field(
        default=None,
    )
    """page_id parameter value."""

    photo: str | None = Field(
        default=None,
    )
    """URL of the preview image."""

    title: str | None = Field(
        default=None,
    )
    """Page title."""

    url: str | None = Field(
        default=None,
    )
    """Page absolute URL."""


class BaseLink(BaseLinkNoProduct):
    """Model: `BaseLink`"""

    text: str | None = Field(
        default=None,
    )
    """Property `BaseLink.text`."""

    product: "BaseLinkProduct | None" = Field(
        default=None,
    )
    """Property `BaseLink.product`."""


class UsersUser(UsersUserMin):
    """Model: `UsersUser`"""

    sex: "BaseSex | None" = Field(
        default=None,
    )
    """User sex."""

    screen_name: str | None = Field(
        default=None,
    )
    """Domain name of the user\'s page."""

    photo_50: str | None = Field(
        default=None,
    )
    """URL of square photo of the user with 50 pixels in width."""

    photo_100: str | None = Field(
        default=None,
    )
    """URL of square photo of the user with 100 pixels in width."""

    online_info: "UsersOnlineInfo | None" = Field(
        default=None,
    )
    """Property `UsersUser.online_info`."""

    online: bool | None = Field(
        default=None,
    )
    """Information whether the user is online."""

    online_mobile: bool | None = Field(
        default=None,
    )
    """Information whether the user is online in mobile site or application."""

    online_app: int | None = Field(
        default=None,
    )
    """Application ID."""

    verified: bool | None = Field(
        default=None,
    )
    """Information whether the user is verified."""

    trending: bool | None = Field(
        default=None,
    )
    """Information whether the user has a \"fire\" pictogram.."""

    friend_status: "FriendsFriendStatusStatus | None" = Field(
        default=None,
    )
    """Property `UsersUser.friend_status`."""

    mutual: "FriendsRequestsMutual | None" = Field(
        default=None,
    )
    """Property `UsersUser.mutual`."""


class UsersUserFull(UsersUser):
    """Model: `UsersUserFull`"""

    first_name_nom: str | None = Field(
        default=None,
    )
    """User\'s first name in nominative case."""

    first_name_gen: str | None = Field(
        default=None,
    )
    """User\'s first name in genitive case."""

    first_name_dat: str | None = Field(
        default=None,
    )
    """User\'s first name in dative case."""

    first_name_acc: str | None = Field(
        default=None,
    )
    """User\'s first name in accusative case."""

    first_name_ins: str | None = Field(
        default=None,
    )
    """User\'s first name in instrumental case."""

    first_name_abl: str | None = Field(
        default=None,
    )
    """User\'s first name in prepositional case."""

    last_name_nom: str | None = Field(
        default=None,
    )
    """User\'s last name in nominative case."""

    last_name_gen: str | None = Field(
        default=None,
    )
    """User\'s last name in genitive case."""

    last_name_dat: str | None = Field(
        default=None,
    )
    """User\'s last name in dative case."""

    last_name_acc: str | None = Field(
        default=None,
    )
    """User\'s last name in accusative case."""

    last_name_ins: str | None = Field(
        default=None,
    )
    """User\'s last name in instrumental case."""

    last_name_abl: str | None = Field(
        default=None,
    )
    """User\'s last name in prepositional case."""

    nickname: str | None = Field(
        default=None,
    )
    """User nickname."""

    maiden_name: str | None = Field(
        default=None,
    )
    """User maiden name."""

    contact_name: str | None = Field(
        default=None,
    )
    """User contact name."""

    domain: str | None = Field(
        default=None,
    )
    """Domain name of the user\'s page."""

    bdate: str | None = Field(
        default=None,
    )
    """User\'s date of birth."""

    city: "BaseCity | None" = Field(
        default=None,
    )
    """Property `UsersUserFull.city`."""

    timezone: float | None = Field(
        default=None,
    )
    """User\'s timezone."""

    owner_state: "OwnerState | None" = Field(
        default=None,
    )
    """Property `UsersUserFull.owner_state`."""

    photo_200: str | None = Field(
        default=None,
    )
    """URL of square photo of the user with 200 pixels in width."""

    photo_max: str | None = Field(
        default=None,
    )
    """URL of square photo of the user with maximum width."""

    photo_200_orig: str | None = Field(
        default=None,
    )
    """URL of user\'s photo with 200 pixels in width."""

    photo_400_orig: str | None = Field(
        default=None,
    )
    """URL of user\'s photo with 400 pixels in width."""

    photo_max_orig: str | None = Field(
        default=None,
    )
    """URL of user\'s photo of maximum size."""

    photo_id: str | None = Field(
        default=None,
    )
    """ID of the user\'s main photo."""

    has_photo: bool | None = Field(
        default=None,
    )
    """Information whether the user has main photo."""

    has_mobile: bool | None = Field(
        default=None,
    )
    """Information whether the user specified his phone number."""

    is_friend: bool | None = Field(
        default=None,
    )
    """Information whether the user is a friend of current user."""

    is_best_friend: bool | None = Field(
        default=None,
    )
    """Information whether the user is a best friend of current user."""

    wall_comments: bool | None = Field(
        default=None,
    )
    """Information whether current user can comment wall posts."""

    can_post: bool | None = Field(
        default=None,
    )
    """Information whether current user can post on the user\'s wall."""

    can_see_all_posts: bool | None = Field(
        default=None,
    )
    """Information whether current user can see other users\' audio on the wall."""

    can_see_audio: bool | None = Field(
        default=None,
    )
    """Information whether current user can see the user\'s audio."""

    type: "UsersUserType | None" = Field(
        default=None,
    )
    """Property `UsersUserFull.type`."""

    email: str | None = Field(
        default=None,
    )
    """Property `UsersUserFull.email`."""

    skype: str | None = Field(
        default=None,
    )
    """Property `UsersUserFull.skype`."""

    facebook: str | None = Field(
        default=None,
    )
    """Property `UsersUserFull.facebook`."""

    facebook_name: str | None = Field(
        default=None,
    )
    """Property `UsersUserFull.facebook_name`."""

    twitter: str | None = Field(
        default=None,
    )
    """Property `UsersUserFull.twitter`."""

    livejournal: str | None = Field(
        default=None,
    )
    """Property `UsersUserFull.livejournal`."""

    instagram: str | None = Field(
        default=None,
    )
    """Property `UsersUserFull.instagram`."""

    test: bool | None = Field(
        default=None,
    )
    """Property `UsersUserFull.test`."""

    video_live: "VideoLiveInfo | None" = Field(
        default=None,
    )
    """Property `UsersUserFull.video_live`."""

    is_video_live_notifications_blocked: bool | None = Field(
        default=None,
    )
    """Property `UsersUserFull.is_video_live_notifications_blocked`."""

    is_service: bool | None = Field(
        default=None,
    )
    """Property `UsersUserFull.is_service`."""

    service_description: str | None = Field(
        default=None,
    )
    """Property `UsersUserFull.service_description`."""

    photo_rec: str | bool | None = Field(
        default=None,
    )
    """Property `UsersUserFull.photo_rec`."""

    photo_medium: str | bool | None = Field(
        default=None,
    )
    """Property `UsersUserFull.photo_medium`."""

    photo_medium_rec: str | bool | None = Field(
        default=None,
    )
    """Property `UsersUserFull.photo_medium_rec`."""

    photo: str | None = Field(
        default=None,
    )
    """Property `UsersUserFull.photo`."""

    photo_big: str | None = Field(
        default=None,
    )
    """Property `UsersUserFull.photo_big`."""

    photo_400: str | None = Field(
        default=None,
    )
    """Property `UsersUserFull.photo_400`."""

    photo_max_size: "PhotosPhoto | None" = Field(
        default=None,
    )
    """Property `UsersUserFull.photo_max_size`."""

    language: str | None = Field(
        default=None,
    )
    """Property `UsersUserFull.language`."""

    stories_archive_count: int | None = Field(
        default=None,
    )
    """Property `UsersUserFull.stories_archive_count`."""

    has_unseen_stories: bool | None = Field(
        default=None,
    )
    """Property `UsersUserFull.has_unseen_stories`."""

    wall_default: str | None = Field(
        default=None,
    )
    """Property `UsersUserFull.wall_default`."""

    can_call: bool | None = Field(
        default=None,
    )
    """Information whether current user can call."""

    can_call_from_group: bool | None = Field(
        default=None,
    )
    """Information whether group can call user."""

    can_invite_as_voicerooms_speaker: bool | None = Field(
        default=None,
    )
    """Information whether user/group can invite user as voicerooms speakr."""

    can_see_wishes: bool | None = Field(
        default=None,
    )
    """Information whether current user can see the user\'s wishes."""

    can_see_gifts: bool | None = Field(
        default=None,
    )
    """Information whether current user can see the user\'s gifts."""

    interests: str | None = Field(
        default=None,
    )
    """Property `UsersUserFull.interests`."""

    books: str | None = Field(
        default=None,
    )
    """Property `UsersUserFull.books`."""

    tv: str | None = Field(
        default=None,
    )
    """Property `UsersUserFull.tv`."""

    quotes: str | None = Field(
        default=None,
    )
    """Property `UsersUserFull.quotes`."""

    about: str | None = Field(
        default=None,
    )
    """Property `UsersUserFull.about`."""

    games: str | None = Field(
        default=None,
    )
    """Property `UsersUserFull.games`."""

    movies: str | None = Field(
        default=None,
    )
    """Property `UsersUserFull.movies`."""

    activities: str | None = Field(
        default=None,
    )
    """Property `UsersUserFull.activities`."""

    music: str | None = Field(
        default=None,
    )
    """Property `UsersUserFull.music`."""

    can_write_private_message: bool | None = Field(
        default=None,
    )
    """Information whether current user can write private message."""

    can_send_friend_request: bool | None = Field(
        default=None,
    )
    """Information whether current user can send a friend request."""

    can_be_invited_group: bool | None = Field(
        default=None,
    )
    """Information whether current user can be invited to the community."""

    mobile_phone: str | None = Field(
        default=None,
    )
    """User\'s mobile phone number."""

    home_phone: str | None = Field(
        default=None,
    )
    """User\'s additional phone number."""

    site: str | None = Field(
        default=None,
    )
    """User\'s website."""

    status_audio: "AudioAudio | None" = Field(
        default=None,
    )
    """Property `UsersUserFull.status_audio`."""

    status: str | None = Field(
        default=None,
    )
    """User\'s status."""

    activity: str | None = Field(
        default=None,
    )
    """User\'s status."""

    status_app: "AppsAppMin | None" = Field(
        default=None,
    )
    """Property `UsersUserFull.status_app`."""

    last_seen: "UsersLastSeen | None" = Field(
        default=None,
    )
    """Property `UsersUserFull.last_seen`."""

    exports: "UsersExports | None" = Field(
        default=None,
    )
    """Property `UsersUserFull.exports`."""

    crop_photo: "BaseCropPhoto | None" = Field(
        default=None,
    )
    """Property `UsersUserFull.crop_photo`."""

    followers_count: int | None = Field(
        default=None,
    )
    """Number of user\'s followers and friends."""

    video_live_level: int | None = Field(
        default=None,
    )
    """User level in live streams achievements."""

    video_live_count: int | None = Field(
        default=None,
    )
    """Number of user\'s live streams."""

    clips_count: int | None = Field(
        default=None,
    )
    """Number of user\'s clips."""

    blacklisted: bool | None = Field(
        default=None,
    )
    """Information whether current user is in the requested user\'s blacklist.."""

    blacklisted_by_me: bool | None = Field(
        default=None,
    )
    """Information whether the requested user is in current user\'s blacklist."""

    is_favorite: bool | None = Field(
        default=None,
    )
    """Information whether the requested user is in faves of current user."""

    is_hidden_from_feed: bool | None = Field(
        default=None,
    )
    """Information whether the requested user is hidden from current user\'s newsfeed."""

    common_count: int | None = Field(
        default=None,
    )
    """Number of common friends with current user."""

    occupation: "UsersOccupation | None" = Field(
        default=None,
    )
    """Property `UsersUserFull.occupation`."""

    career: list["UsersCareer"] | None = Field(
        default=None,
    )
    """Property `UsersUserFull.career`."""

    military: list["UsersMilitary"] | None = Field(
        default=None,
    )
    """Property `UsersUserFull.military`."""

    university: int | None = Field(
        default=None,
    )
    """University ID."""

    university_name: str | None = Field(
        default=None,
    )
    """University name."""

    university_group_id: int | None = Field(
        default=None,
    )
    """Property `UsersUserFull.university_group_id`."""

    faculty: int | None = Field(
        default=None,
    )
    """Faculty ID."""

    faculty_name: str | None = Field(
        default=None,
    )
    """Faculty name."""

    graduation: int | None = Field(
        default=None,
    )
    """Graduation year."""

    education_form: str | None = Field(
        default=None,
    )
    """Education form."""

    education_status: str | None = Field(
        default=None,
    )
    """User\'s education status."""

    home_town: str | None = Field(
        default=None,
    )
    """User hometown."""

    relation: "UsersUserRelation | None" = Field(
        default=None,
    )
    """User relationship status."""

    relation_partner: "UsersUserMin | None" = Field(
        default=None,
    )
    """Property `UsersUserFull.relation_partner`."""

    personal: "UsersPersonal | None" = Field(
        default=None,
    )
    """Property `UsersUserFull.personal`."""

    universities: list["UsersUniversity"] | None = Field(
        default=None,
    )
    """Property `UsersUserFull.universities`."""

    schools: list["UsersSchool"] | None = Field(
        default=None,
    )
    """Property `UsersUserFull.schools`."""

    relatives: list["UsersRelative"] | None = Field(
        default=None,
    )
    """Property `UsersUserFull.relatives`."""

    is_subscribed_podcasts: bool | None = Field(
        default=None,
    )
    """Information whether current user is subscribed to podcasts."""

    can_subscribe_podcasts: bool | None = Field(
        default=None,
    )
    """Owner in whitelist or not."""

    can_subscribe_posts: bool | None = Field(
        default=None,
    )
    """Can subscribe to wall."""

    counters: "UsersUserCounters | None" = Field(
        default=None,
    )
    """Property `UsersUserFull.counters`."""

    access_key: str | None = Field(
        default=None,
    )
    """Property `UsersUserFull.access_key`."""

    can_upload_doc: bool | None = Field(
        default=None,
    )
    """Property `UsersUserFull.can_upload_doc`."""

    can_ban: bool | None = Field(
        default=None,
    )
    """Information whether the user can be baned (added to black list) by me."""

    hash: str | None = Field(
        default=None,
    )
    """Property `UsersUserFull.hash`."""

    is_no_index: bool | None = Field(
        default=None,
    )
    """Access to user profile is restricted for search engines."""

    contact_id: int | None = Field(
        default=None,
    )
    """Contact person ID."""

    is_message_request: bool | None = Field(
        default=None,
    )
    """Property `UsersUserFull.is_message_request`."""

    descriptions: list[str] | None = Field(
        default=None,
    )
    """Property `UsersUserFull.descriptions`."""

    lists: list[int] | None = Field(
        default=None,
    )
    """Property `UsersUserFull.lists`."""


class UsersUserXtrType(UsersUserFull):
    """Model: `UsersUserXtrType`"""

    type: "UsersUserType | None" = Field(
        default=None,
    )
    """Property `UsersUserXtrType.type`."""


class MessagesUserXtrInvitedBy(UsersUserXtrType):
    """Model: `MessagesUserXtrInvitedBy`"""

    invited_by: int | None = Field(
        default=None,
    )
    """ID of the inviter."""

    name: str | None = Field(
        default=None,
    )
    """Name of group."""

    type: "MessagesUserTypeForXtrInvitedBy | None" = Field(
        default=None,
    )
    """Property `MessagesUserXtrInvitedBy.type`."""


class MessagesGetConversationByIdExtended(MessagesGetConversationById):
    """Model: `MessagesGetConversationByIdExtended`"""

    profiles: list["UsersUserFull"] | None = Field(
        default=None,
    )
    """Property `MessagesGetConversationByIdExtended.profiles`."""

    groups: list["GroupsGroupFull"] | None = Field(
        default=None,
    )
    """Property `MessagesGetConversationByIdExtended.groups`."""


class MessagesMessage(MessagesBaseMessage):
    """Model: `MessagesMessage`"""

    important: bool | None = Field(
        default=None,
    )
    """Is it an important message."""

    is_hidden: bool | None = Field(
        default=None,
    )
    """Property `MessagesMessage.is_hidden`."""

    members_count: int | None = Field(
        default=None,
    )
    """Members number."""

    reply_message: "MessagesForeignMessage | None" = Field(
        default=None,
    )
    """Property `MessagesMessage.reply_message`."""

    reaction_id: int | None = Field(
        default=None,
    )
    """Reaction id set on message."""

    reactions: list["MessagesReactionCounterResponseItem"] | None = Field(
        default=None,
    )
    """Actual reactions counters on this message."""

    last_reaction_id: int | None = Field(
        default=None,
    )
    """Last reaction id set on this message."""

    is_pinned: bool | None = Field(
        default=None,
    )
    """Is message pinned in its conversation."""

    was_listened: bool | None = Field(
        default=None,
    )
    """Was the audio message inside already listened by you."""

    pinned_at: int | None = Field(
        default=None,
    )
    """Date when the message has been pinned in Unixtime."""


class AccountUserSettings(UsersUserMin, UsersUserSettingsXtr):
    """Model: `AccountUserSettings`"""

    photo_200: str | None = Field(
        default=None,
    )
    """URL of square photo of the user with 200 pixels in width."""

    is_service_account: bool | None = Field(
        default=None,
    )
    """flag about service account."""


class AdsStatsAge(AdsDemographicStatsPeriodItemBase):
    """Model: `AdsStatsAge`"""

    value: str | None = Field(
        default=None,
    )
    """Age interval."""


class AdsStatsCities(AdsDemographicStatsPeriodItemBase):
    """Model: `AdsStatsCities`"""

    name: str | None = Field(
        default=None,
    )
    """City name."""

    value: int | str | None = Field(
        default=None,
    )
    """City ID."""


class AdsStatsSex(AdsDemographicStatsPeriodItemBase):
    """Model: `AdsStatsSex`"""

    value: "AdsStatsSexValue | None" = Field(
        default=None,
    )
    """Property `AdsStatsSex.value`."""


class AdsStatsSexAge(AdsDemographicStatsPeriodItemBase):
    """Model: `AdsStatsSexAge`"""

    value: str | None = Field(
        default=None,
    )
    """Sex and age interval."""


class AdsTargSettings(AdsCriteria):
    """Model: `AdsTargSettings`"""

    id: str | None = Field(
        default=None,
    )
    """Ad ID."""

    campaign_id: str | None = Field(
        default=None,
    )
    """Campaign ID."""


class AppsApp(AppsAppMin):
    """Model: `AppsApp`"""

    author_url: str | None = Field(
        default=None,
    )
    """Application author\'s URL."""

    banner_1120: str | None = Field(
        default=None,
    )
    """URL of the app banner with 1120 px in width."""

    banner_560: str | None = Field(
        default=None,
    )
    """URL of the app banner with 560 px in width."""

    icon_16: str | None = Field(
        default=None,
    )
    """URL of the app icon with 16 px in width."""

    is_new: bool | None = Field(
        default=None,
    )
    """Is new flag."""

    push_enabled: bool | None = Field(
        default=None,
    )
    """Is push enabled."""

    friends: list[int] | None = Field(
        default=None,
    )
    """Property `AppsApp.friends`."""

    catalog_position: int | None = Field(
        default=None,
    )
    """Catalog position."""

    description: str | None = Field(
        default=None,
    )
    """Application description."""

    genre: str | None = Field(
        default=None,
    )
    """Genre name."""

    genre_id: int | None = Field(
        default=None,
    )
    """Genre ID."""

    international: bool | None = Field(
        default=None,
    )
    """Information whether the application is multilanguage."""

    is_in_catalog: int | None = Field(
        default=None,
    )
    """Information whether application is in mobile catalog."""

    leaderboard_type: "AppsAppLeaderboardType | None" = Field(
        default=None,
    )
    """Property `AppsApp.leaderboard_type`."""

    members_count: int | None = Field(
        default=None,
    )
    """Members number."""

    platform_id: str | None = Field(
        default=None,
    )
    """Application ID in store."""

    published_date: datetime.datetime | None = Field(
        default=None,
    )
    """Date when the application has been published in Unixtime."""

    screen_name: str | None = Field(
        default=None,
    )
    """Screen name."""

    section: str | None = Field(
        default=None,
    )
    """Application section name."""


class CallbackForeignMessage(MessagesForeignMessage):
    """Model: `CallbackForeignMessage`"""

    is_cropped: bool | None = Field(
        default=None,
    )
    """Property `CallbackForeignMessage.is_cropped`."""

    fwd_messages: list["CallbackForeignMessage"] | None = Field(
        default=None,
    )
    """Property `CallbackForeignMessage.fwd_messages`."""

    reply_message: "CallbackForeignMessage | None" = Field(
        default=None,
    )
    """Property `CallbackForeignMessage.reply_message`."""


class CallbackMessage(MessagesMessage):
    """Model: `CallbackMessage`"""

    influence_score: float | None = Field(
        default=None,
    )
    """Property `CallbackMessage.influence_score`."""

    reply_message: "CallbackForeignMessage | None" = Field(
        default=None,
    )
    """Property `CallbackMessage.reply_message`."""

    fwd_messages: "CallbackFwdMessages | None" = Field(
        default=None,
    )
    """Property `CallbackMessage.fwd_messages`."""


class CallbackPhotoComment(WallWallComment):
    """Model: `CallbackPhotoComment`"""

    photo_owner_id: int = Field()
    """Property `CallbackPhotoComment.photo_owner_id`."""


class CallbackVideoComment(WallWallComment):
    """Model: `CallbackVideoComment`"""

    video_owner_id: int | None = Field(
        default=None,
    )
    """Property `CallbackVideoComment.video_owner_id`."""


class CallbackConfirmation(CallbackBase):
    """Model: `CallbackConfirmation`"""

    type: str | None = Field(
        default=None,
    )
    """Property `CallbackConfirmation.type`."""


class DatabaseCity(BaseObject):
    """Model: `DatabaseCity`"""

    area: str | None = Field(
        default=None,
    )
    """Area title."""

    region: str | None = Field(
        default=None,
    )
    """Region title."""

    important: bool | None = Field(
        default=None,
    )
    """Information whether the city is included in important cities list."""


class GroupsUserXtrRole(UsersUserFull):
    """Model: `GroupsUserXtrRole`"""

    permissions: list["GroupsMemberRolePermission"] | None = Field(
        default=None,
    )
    """Property `GroupsUserXtrRole.permissions`."""

    role: "GroupsRoleOptions | None" = Field(
        default=None,
    )
    """Property `GroupsUserXtrRole.role`."""


class GroupsGroupFull(GroupsGroup, GroupsMarketProperties):
    """Model: `GroupsGroupFull`"""

    member_status: "GroupsGroupFullMemberStatus | None" = Field(
        default=None,
    )
    """Current user\'s member status."""

    is_adult: bool | None = Field(
        default=None,
    )
    """Information whether community is adult."""

    is_hidden_from_feed: bool | None = Field(
        default=None,
    )
    """Information whether community is hidden from current user\'s newsfeed."""

    is_favorite: bool | None = Field(
        default=None,
    )
    """Information whether community is in faves."""

    is_subscribed: bool | None = Field(
        default=None,
    )
    """Information whether current user is subscribed."""

    city: "BaseObject | None" = Field(
        default=None,
    )
    """Property `GroupsGroupFull.city`."""

    description: str | None = Field(
        default=None,
    )
    """Community description."""

    wiki_page: str | None = Field(
        default=None,
    )
    """Community\'s main wiki page title."""

    members_count: int | None = Field(
        default=None,
    )
    """Community members number."""

    members_count_text: str | None = Field(
        default=None,
    )
    """Info about number of users in group."""

    requests_count: int | None = Field(
        default=None,
    )
    """The number of incoming requests to the community."""

    video_live_level: int | None = Field(
        default=None,
    )
    """Community level live streams achievements."""

    video_live_count: int | None = Field(
        default=None,
    )
    """Number of community\'s live streams."""

    clips_count: int | None = Field(
        default=None,
    )
    """Number of community\'s clips."""

    counters: "GroupsCountersGroup | None" = Field(
        default=None,
    )
    """Property `GroupsGroupFull.counters`."""

    textlives_count: int | None = Field(
        default=None,
    )
    """Textlives number."""

    cover: "BaseOwnerCover | None" = Field(
        default=None,
    )
    """Property `GroupsGroupFull.cover`."""

    video_cover: "BaseOwnerCover | None" = Field(
        default=None,
    )
    """Property `GroupsGroupFull.video_cover`."""

    can_post: bool | None = Field(
        default=None,
    )
    """Information whether current user can post on community\'s wall."""

    can_suggest: bool | None = Field(
        default=None,
    )
    """Property `GroupsGroupFull.can_suggest`."""

    can_upload_story: bool | None = Field(
        default=None,
    )
    """Information whether current user can upload story."""

    can_call_to_community: bool | None = Field(
        default=None,
    )
    """Information whether current user can call to community."""

    can_upload_doc: bool | None = Field(
        default=None,
    )
    """Information whether current user can upload doc."""

    can_upload_video: bool | None = Field(
        default=None,
    )
    """Information whether current user can upload video."""

    can_upload_clip: bool | None = Field(
        default=None,
    )
    """Information whether current user can upload clip."""

    can_see_all_posts: bool | None = Field(
        default=None,
    )
    """Information whether current user can see all posts on community\'s wall."""

    can_create_topic: bool | None = Field(
        default=None,
    )
    """Information whether current user can create topic."""

    activity: str | None = Field(
        default=None,
    )
    """Type of group, start date of event or category of public page."""

    fixed_post: int | None = Field(
        default=None,
    )
    """Fixed post ID."""

    has_photo: bool | None = Field(
        default=None,
    )
    """Information whether community has photo."""

    crop_photo: "BaseCropPhoto | None" = Field(
        default=None,
    )
    """Данные о точках, по которым вырезаны профильная и миниатюрная фотографии сообщества."""

    status: str | None = Field(
        default=None,
    )
    """Community status."""

    status_audio: "AudioAudio | None" = Field(
        default=None,
    )
    """Property `GroupsGroupFull.status_audio`."""

    main_album_id: int | None = Field(
        default=None,
    )
    """Community\'s main photo album ID."""

    links: list["GroupsLinksItem"] | None = Field(
        default=None,
    )
    """Property `GroupsGroupFull.links`."""

    contacts: list["GroupsContactsItem"] | None = Field(
        default=None,
    )
    """Property `GroupsGroupFull.contacts`."""

    wall: int | None = Field(
        default=None,
    )
    """Information about wall status in community."""

    site: str | None = Field(
        default=None,
    )
    """Community\'s website."""

    main_section: "GroupsGroupFullSection | None" = Field(
        default=None,
    )
    """Property `GroupsGroupFull.main_section`."""

    secondary_section: "GroupsGroupFullSection | None" = Field(
        default=None,
    )
    """Property `GroupsGroupFull.secondary_section`."""

    trending: bool | None = Field(
        default=None,
    )
    """Information whether the community has a \"fire\" pictogram.."""

    can_message: bool | None = Field(
        default=None,
    )
    """Information whether current user can send a message to community."""

    is_messages_blocked: bool | None = Field(
        default=None,
    )
    """Information whether community can send a message to current user."""

    can_send_notify: bool | None = Field(
        default=None,
    )
    """Information whether community can send notifications by phone number to current user."""

    online_status: "GroupsOnlineStatus | None" = Field(
        default=None,
    )
    """Status of replies in community messages."""

    invited_by: int | None = Field(
        default=None,
    )
    """Inviter ID."""

    age_limits: "GroupsGroupFullAgeLimits | None" = Field(
        default=None,
    )
    """Information whether age limit."""

    ban_info: "GroupsGroupBanInfo | None" = Field(
        default=None,
    )
    """User ban info."""

    has_group_channel: bool | None = Field(
        default=None,
    )
    """Property `GroupsGroupFull.has_group_channel`."""

    addresses: "GroupsAddressesInfo | None" = Field(
        default=None,
    )
    """Info about addresses in groups."""

    is_subscribed_podcasts: bool | None = Field(
        default=None,
    )
    """Information whether current user is subscribed to podcasts."""

    can_subscribe_podcasts: bool | None = Field(
        default=None,
    )
    """Owner in whitelist or not."""

    can_subscribe_posts: bool | None = Field(
        default=None,
    )
    """Can subscribe to wall."""

    live_covers: "GroupsLiveCovers | None" = Field(
        default=None,
    )
    """Live covers state."""

    stories_archive_count: int | None = Field(
        default=None,
    )
    """Property `GroupsGroupFull.stories_archive_count`."""

    has_unseen_stories: bool | None = Field(
        default=None,
    )
    """Property `GroupsGroupFull.has_unseen_stories`."""

    video_notifications_status: str | None = Field(
        default=None,
    )
    """Information about the status of video notifications for the current user.."""

    videos_count: int | None = Field(
        default=None,
    )
    """Community videos number."""


class MarketMarketItemBasicWithGroup(MarketMarketItemBasic):
    """Model: `MarketMarketItemBasicWithGroup`"""

    is_group_verified: bool | None = Field(
        default=None,
    )
    """Property `MarketMarketItemBasicWithGroup.is_group_verified`."""

    group_name: str | None = Field(
        default=None,
    )
    """Property `MarketMarketItemBasicWithGroup.group_name`."""

    group_link: str | None = Field(
        default=None,
    )
    """Property `MarketMarketItemBasicWithGroup.group_link`."""

    is_owner: bool | None = Field(
        default=None,
    )
    """Property `MarketMarketItemBasicWithGroup.is_owner`."""

    is_adult: bool | None = Field(
        default=None,
    )
    """Property `MarketMarketItemBasicWithGroup.is_adult`."""


class MarketMarketItemFull(MarketMarketItem):
    """Model: `MarketMarketItemFull`"""

    albums_ids: list[int] | None = Field(
        default=None,
    )
    """Property `MarketMarketItemFull.albums_ids`."""

    photos: list["PhotosPhoto"] | None = Field(
        default=None,
    )
    """Property `MarketMarketItemFull.photos`."""

    can_comment: bool | None = Field(
        default=None,
    )
    """Information whether current use can comment the item."""

    show_comments: bool | None = Field(
        default=None,
    )
    """Information about whether to show the comments tab."""

    can_repost: bool | None = Field(
        default=None,
    )
    """Information whether current use can repost the item."""

    likes: "BaseLikes | None" = Field(
        default=None,
    )
    """Property `MarketMarketItemFull.likes`."""

    reposts: "BaseRepostsInfo | None" = Field(
        default=None,
    )
    """Property `MarketMarketItemFull.reposts`."""

    views_count: int | None = Field(
        default=None,
    )
    """Views number."""

    wishlist_item_id: int | None = Field(
        default=None,
    )
    """Object identifier in wishlist of viewer."""

    rating: float | None = Field(
        default=None,
    )
    """Rating of product."""

    orders_count: int | None = Field(
        default=None,
    )
    """Count of product orders."""

    cancel_info: "BaseLink | None" = Field(
        default=None,
    )
    """Information for cancel and revert order."""

    user_agreement_info: str | None = Field(
        default=None,
    )
    """User agreement info."""

    ad_id: int | None = Field(
        default=None,
    )
    """Contains ad ID if it has."""

    owner_info: "MarketItemOwnerInfo | None" = Field(
        default=None,
    )
    """Information about the group where the item is placed."""

    can_edit: bool | None = Field(
        default=None,
    )
    """Can the item be updated by current user?."""

    can_delete: bool | None = Field(
        default=None,
    )
    """Can item be deleted by current user?."""

    can_recover: bool | None = Field(
        default=None,
    )
    """Can item be restored by current user?."""

    can_show_convert_to_service: bool | None = Field(
        default=None,
    )
    """Can the item be converted from a product into a service?."""

    promotion: "MarketItemPromotionInfo | None" = Field(
        default=None,
    )
    """Information about promotion of the item."""

    vk_pay_discount: int | None = Field(
        default=None,
    )
    """The amount of the discount if VK Pay is used for payment."""


class PollsPollExtended(PollsPoll):
    """Model: `PollsPollExtended`"""

    profiles: list["UsersUserFull"] | None = Field(
        default=None,
    )
    """Property `PollsPollExtended.profiles`."""


class FriendsRequestsXtrMutual(UsersUserFull):
    """Model: `FriendsRequestsXtrMutual`"""

    user_id: int = Field()
    """User ID."""

    id: int | None = Field(
        default=None,
    )
    """User ID."""

    from_: str | None = Field(
        default=None,
        alias="from",
    )
    """ID of the user by whom friend has been suggested."""

    mutual: "FriendsRequestsMutual | None" = Field(
        default=None,
    )
    """Property `FriendsRequestsXtrMutual.mutual`."""

    track_code: str | None = Field(
        default=None,
    )
    """Property `FriendsRequestsXtrMutual.track_code`."""

    message: str | None = Field(
        default=None,
    )
    """Message sent with a request."""

    timestamp: int | None = Field(
        default=None,
    )
    """Request timestamp."""

    descriptions: list[str] | None = Field(
        default=None,
    )
    """Property `FriendsRequestsXtrMutual.descriptions`."""


class FriendsFriendExtendedStatus(FriendsFriendStatus):
    """Model: `FriendsFriendExtendedStatus`"""

    is_request_unread: bool | None = Field(
        default=None,
    )
    """Is friend request from other user unread."""


class FriendsRequestsXtrMessage(FriendsRequestsXtrMutual):
    """Model: `FriendsRequestsXtrMessage`"""

    message: str | None = Field(
        default=None,
    )
    """Message sent with a request."""


class VideoVideoImage(BaseImage):
    """Model: `VideoVideoImage`"""

    with_padding: "BasePropertyExists | None" = Field(
        default=None,
    )
    """Property `VideoVideoImage.with_padding`."""

    size: str | None = Field(
        default=None,
    )
    """Property `VideoVideoImage.size`."""


class VideoVideoAlbumFull(VideoVideoAlbum):
    """Model: `VideoVideoAlbumFull`"""

    count: int = Field()
    """Total number of videos in album."""

    updated_time: int = Field()
    """Date when the album has been updated last time in Unixtime."""

    image: list["VideoVideoImage"] | None = Field(
        default=None,
    )
    """Album cover image in different sizes."""

    image_blur: "BasePropertyExists | None" = Field(
        default=None,
    )
    """Need blur album thumb or not."""

    is_system: "BasePropertyExists | None" = Field(
        default=None,
    )
    """Information whether album is system."""

    can_edit: bool | None = Field(
        default=None,
    )
    """Is user can edit playlist."""

    can_delete: bool | None = Field(
        default=None,
    )
    """Is user can delete playlist."""

    can_upload: bool | None = Field(
        default=None,
    )
    """Is user can upload video to playlist."""


class VideoVideoFull(VideoVideo):
    """Model: `VideoVideoFull`"""

    files: "VideoVideoFiles | None" = Field(
        default=None,
    )
    """Property `VideoVideoFull.files`."""

    trailer: "VideoVideoFiles | None" = Field(
        default=None,
    )
    """Property `VideoVideoFull.trailer`."""

    episodes: list["VideoEpisode"] | None = Field(
        default=None,
    )
    """List of video episodes with timecodes."""

    live_settings: "VideoLiveSettings | None" = Field(
        default=None,
    )
    """Settings for live stream."""


class WallWallpostFull(WallCarouselBase, WallWallpost):
    """Model: `WallWallpostFull`"""

    copy_history: list["WallWallpostFull"] | None = Field(
        default=None,
    )
    """Property `WallWallpostFull.copy_history`."""

    can_edit: bool | None = Field(
        default=None,
    )
    """Information whether current user can edit the post."""

    created_by: int | None = Field(
        default=None,
    )
    """Post creator ID (if post still can be edited)."""

    can_delete: bool | None = Field(
        default=None,
    )
    """Information whether current user can delete the post."""

    can_pin: bool | None = Field(
        default=None,
    )
    """Information whether current user can pin the post."""

    donut: "WallWallpostDonut | None" = Field(
        default=None,
    )
    """Property `WallWallpostFull.donut`."""

    is_pinned: bool | None = Field(
        default=None,
    )
    """Information whether the post is pinned."""

    comments: "BaseCommentsInfo | None" = Field(
        default=None,
    )
    """Property `WallWallpostFull.comments`."""

    marked_as_ads: bool | None = Field(
        default=None,
    )
    """Information whether the post is marked as ads."""

    topic_id: int | None = Field(
        default=None,
    )
    """Topic ID. Allowed values can be obtained from newsfeed.getPostTopics method."""

    short_text_rate: float | None = Field(
        default=None,
    )
    """Preview length control parameter."""

    hash: str | None = Field(
        default=None,
    )
    """Hash for sharing."""

    type: "WallPostType | None" = Field(
        default=None,
    )
    """Property `WallWallpostFull.type`."""

    feedback: "NewsfeedItemWallpostFeedback | None" = Field(
        default=None,
    )
    """Property `WallWallpostFull.feedback`."""

    to_id: int | None = Field(
        default=None,
    )
    """Property `WallWallpostFull.to_id`."""


class NewsfeedCommentsBase(BaseCommentsInfo):
    """Model: `NewsfeedCommentsBase`"""

    list_: list["WallWallComment"] | None = Field(
        default=None,
        alias="list",
    )
    """Property `NewsfeedCommentsBase.list`."""


class NewsfeedCommentsItemTypeMarket(MarketMarketItem, NewsfeedCommentsItemBase):
    """Model: `NewsfeedCommentsItemTypeMarket`"""

    comments: "NewsfeedCommentsBase | None" = Field(
        default=None,
    )
    """Property `NewsfeedCommentsItemTypeMarket.comments`."""

    likes: "BaseLikes | None" = Field(
        default=None,
    )
    """Property `NewsfeedCommentsItemTypeMarket.likes`."""


class NewsfeedCommentsItemTypeNotes(NewsfeedCommentsItemBase):
    """Model: `NewsfeedCommentsItemTypeNotes`"""

    text: str | None = Field(
        default=None,
    )
    """Property `NewsfeedCommentsItemTypeNotes.text`."""

    comments: "NewsfeedCommentsBase | None" = Field(
        default=None,
    )
    """Property `NewsfeedCommentsItemTypeNotes.comments`."""

    likes: "BaseLikes | None" = Field(
        default=None,
    )
    """Property `NewsfeedCommentsItemTypeNotes.likes`."""


class NewsfeedCommentsItemTypePhoto(PhotosPhoto, NewsfeedCommentsItemBase):
    """Model: `NewsfeedCommentsItemTypePhoto`"""

    comments: "NewsfeedCommentsBase | None" = Field(
        default=None,
    )
    """Property `NewsfeedCommentsItemTypePhoto.comments`."""

    likes: "BaseLikes | None" = Field(
        default=None,
    )
    """Property `NewsfeedCommentsItemTypePhoto.likes`."""


class NewsfeedCommentsItemTypePost(WallWallpostFull, NewsfeedCommentsItemBase):
    """Model: `NewsfeedCommentsItemTypePost`"""

    from_id: int | None = Field(
        default=None,
    )
    """Property `NewsfeedCommentsItemTypePost.from_id`."""

    comments: "NewsfeedCommentsBase | None" = Field(
        default=None,
    )
    """Property `NewsfeedCommentsItemTypePost.comments`."""


class NewsfeedCommentsItemTypeTopic(NewsfeedCommentsItemBase):
    """Model: `NewsfeedCommentsItemTypeTopic`"""

    text: str | None = Field(
        default=None,
    )
    """Property `NewsfeedCommentsItemTypeTopic.text`."""

    comments: "NewsfeedCommentsBase | None" = Field(
        default=None,
    )
    """Property `NewsfeedCommentsItemTypeTopic.comments`."""

    likes: "BaseLikes | None" = Field(
        default=None,
    )
    """Property `NewsfeedCommentsItemTypeTopic.likes`."""


class NewsfeedCommentsItemTypeVideo(VideoVideo, NewsfeedCommentsItemBase):
    """Model: `NewsfeedCommentsItemTypeVideo`"""

    text: str | None = Field(
        default=None,
    )
    """Property `NewsfeedCommentsItemTypeVideo.text`."""

    comments: "NewsfeedCommentsBase | None" = Field(
        default=None,
    )
    """Property `NewsfeedCommentsItemTypeVideo.comments`."""

    likes: "BaseLikes | None" = Field(
        default=None,
    )
    """Property `NewsfeedCommentsItemTypeVideo.likes`."""

    type: str | None = Field(
        default=None,
    )
    """Property `NewsfeedCommentsItemTypeVideo.type`."""


class NewsfeedItemAudio(NewsfeedItemBase):
    """Model: `NewsfeedItemAudio`"""

    audio: "NewsfeedItemAudioAudio | None" = Field(
        default=None,
    )
    """Property `NewsfeedItemAudio.audio`."""

    post_id: int | None = Field(
        default=None,
    )
    """Post ID."""


class NewsfeedItemDigest(NewsfeedItemBase):
    """Model: `NewsfeedItemDigest`"""

    feed_id: str | None = Field(
        default=None,
    )
    """id of feed in digest."""

    items: list["NewsfeedItemDigestItem"] | None = Field(
        default=None,
    )
    """Property `NewsfeedItemDigest.items`."""

    main_post_ids: list[str] | None = Field(
        default=None,
    )
    """Property `NewsfeedItemDigest.main_post_ids`."""

    template: str | None = Field(
        default=None,
    )
    """type of digest."""

    header: "NewsfeedItemDigestHeader | None" = Field(
        default=None,
    )
    """Property `NewsfeedItemDigest.header`."""

    footer: "NewsfeedItemDigestFooter | None" = Field(
        default=None,
    )
    """Property `NewsfeedItemDigest.footer`."""


class NewsfeedItemDigestFullItem(NewsfeedItemBase):
    """Model: `NewsfeedItemDigestFullItem`"""

    inner_type: str = Field()
    """Property `NewsfeedItemDigestFullItem.inner_type`."""

    post: "NewsfeedItemWallpost" = Field()
    """Property `NewsfeedItemDigestFullItem.post`."""

    text: str | None = Field(
        default=None,
    )
    """Property `NewsfeedItemDigestFullItem.text`."""

    source_name: str | None = Field(
        default=None,
    )
    """Property `NewsfeedItemDigestFullItem.source_name`."""

    attachment_index: int | None = Field(
        default=None,
    )
    """Property `NewsfeedItemDigestFullItem.attachment_index`."""

    attachment: "WallWallpostAttachment | None" = Field(
        default=None,
    )
    """Property `NewsfeedItemDigestFullItem.attachment`."""

    style: str | None = Field(
        default=None,
    )
    """Property `NewsfeedItemDigestFullItem.style`."""

    badge_text: str | None = Field(
        default=None,
    )
    """Optional red badge for posts in digest block."""


class NewsfeedItemFriend(NewsfeedItemBase):
    """Model: `NewsfeedItemFriend`"""

    friends: "NewsfeedItemFriendFriends | None" = Field(
        default=None,
    )
    """Property `NewsfeedItemFriend.friends`."""


class NewsfeedItemPhoto(WallCarouselBase, NewsfeedItemBase):
    """Model: `NewsfeedItemPhoto`"""

    photos: "NewsfeedItemPhotoPhotos | None" = Field(
        default=None,
    )
    """Property `NewsfeedItemPhoto.photos`."""

    post_id: int | None = Field(
        default=None,
    )
    """Post ID."""


class NewsfeedItemPhotoTag(WallCarouselBase, NewsfeedItemBase):
    """Model: `NewsfeedItemPhotoTag`"""

    photo_tags: "NewsfeedItemPhotoTagPhotoTags | None" = Field(
        default=None,
    )
    """Property `NewsfeedItemPhotoTag.photo_tags`."""

    post_id: int | None = Field(
        default=None,
    )
    """Post ID."""


class NewsfeedItemPromoButton(NewsfeedItemBase):
    """Model: `NewsfeedItemPromoButton`"""

    text: str | None = Field(
        default=None,
    )
    """Property `NewsfeedItemPromoButton.text`."""

    title: str | None = Field(
        default=None,
    )
    """Property `NewsfeedItemPromoButton.title`."""

    action: "NewsfeedItemPromoButtonAction | None" = Field(
        default=None,
    )
    """Property `NewsfeedItemPromoButton.action`."""

    images: list["NewsfeedItemPromoButtonImage"] | None = Field(
        default=None,
    )
    """Property `NewsfeedItemPromoButton.images`."""


class NewsfeedItemTopic(NewsfeedItemBase):
    """Model: `NewsfeedItemTopic`"""

    post_id: int = Field()
    """Topic post ID."""

    text: str = Field()
    """Post text."""

    comments: "BaseCommentsInfo | None" = Field(
        default=None,
    )
    """Property `NewsfeedItemTopic.comments`."""

    likes: "BaseLikesInfo | None" = Field(
        default=None,
    )
    """Property `NewsfeedItemTopic.likes`."""


class NewsfeedItemVideo(WallCarouselBase, NewsfeedItemBase):
    """Model: `NewsfeedItemVideo`"""

    video: "NewsfeedItemVideoVideo | None" = Field(
        default=None,
    )
    """Property `NewsfeedItemVideo.video`."""

    post_id: int | None = Field(
        default=None,
    )
    """Post ID."""


class NewsfeedItemWallpost(NewsfeedItemBase, WallWallpostFull):
    """Model: `NewsfeedItemWallpost`"""


class NewsfeedListFull(NewsfeedList):
    """Model: `NewsfeedListFull`"""

    no_reposts: bool | None = Field(
        default=None,
    )
    """Information whether reposts hiding is enabled."""

    source_ids: list[int] | None = Field(
        default=None,
    )
    """Property `NewsfeedListFull.source_ids`."""


__all__ = (
    "AccountAccountCounters",
    "AccountCountersFilter",
    "AccountInfo",
    "AccountNameRequest",
    "AccountNameRequestStatus",
    "AccountOffer",
    "AccountOfferLinkType",
    "AccountPushConversations",
    "AccountPushConversationsItem",
    "AccountPushParams",
    "AccountPushParamsMode",
    "AccountPushParamsOnoff",
    "AccountPushParamsSettings",
    "AccountPushSettings",
    "AccountUserSettings",
    "AccountUserSettingsInterest",
    "AccountUserSettingsInterests",
    "AddressFields",
    "AdsAccessRole",
    "AdsAccessRolePublic",
    "AdsAccesses",
    "AdsAccount",
    "AdsAccountType",
    "AdsAd",
    "AdsAdApproved",
    "AdsAdCostType",
    "AdsAdLayout",
    "AdsAdStatus",
    "AdsCampaign",
    "AdsCampaignStatus",
    "AdsCampaignType",
    "AdsCategory",
    "AdsClient",
    "AdsClipItem",
    "AdsClipItemLink",
    "AdsCreateAdStatus",
    "AdsCreateCampaignStatus",
    "AdsCreateClientsStatus",
    "AdsCriteria",
    "AdsCriteriaSex",
    "AdsDemoStats",
    "AdsDemographicStatsPeriodItemBase",
    "AdsDemostatsFormat",
    "AdsEventsRetargetingGroup",
    "AdsFloodStats",
    "AdsFloodStatsByUserItem",
    "AdsLinkStatus",
    "AdsLookalikeRequest",
    "AdsLookalikeRequestSaveAudienceLevel",
    "AdsLookalikeRequestSourceType",
    "AdsLookalikeRequestStatus",
    "AdsMobileStatItem",
    "AdsMusician",
    "AdsObjectType",
    "AdsOrdClientType",
    "AdsOrdData",
    "AdsOrdSubagent",
    "AdsPost",
    "AdsPostComments",
    "AdsPostDonut",
    "AdsPostEasyPromote",
    "AdsPostLikes",
    "AdsPostOwner",
    "AdsPostReposts",
    "AdsPostViews",
    "AdsPromotedPostReach",
    "AdsRejectReason",
    "AdsRules",
    "AdsStatisticClickAction",
    "AdsStatisticClickActionType",
    "AdsStats",
    "AdsStatsAge",
    "AdsStatsCities",
    "AdsStatsFormat",
    "AdsStatsSex",
    "AdsStatsSexAge",
    "AdsStatsSexValue",
    "AdsStatsViewsTimes",
    "AdsStories",
    "AdsStoriesOwner",
    "AdsStoryItem",
    "AdsStoryItemLink",
    "AdsStoryItemStats",
    "AdsStoryItemStatsFollow",
    "AdsStoryItemStatsUrlView",
    "AdsTargSettings",
    "AdsTargStats",
    "AdsTargSuggestions",
    "AdsTargSuggestionsCities",
    "AdsTargSuggestionsRegions",
    "AdsTargSuggestionsSchools",
    "AdsTargSuggestionsSchoolsType",
    "AdsTargetGroup",
    "AdsTargetGroupTargetPixelRule",
    "AdsTargetPixelInfo",
    "AdsUpdateAdsStatus",
    "AdsUpdateClientsStatus",
    "AdsUpdateOfficeUsersResult",
    "AdsUserSpecification",
    "AdsUserSpecificationCutted",
    "AdsUsers",
    "AppWidgetsPhoto",
    "AppWidgetsPhotos",
    "AppsApp",
    "AppsAppFields",
    "AppsAppLeaderboardType",
    "AppsAppMin",
    "AppsAppType",
    "AppsCatalogList",
    "AppsCustomSnippet",
    "AppsCustomSnippetButton",
    "AppsLeaderboard",
    "AppsScope",
    "AppsScopeName",
    "AppsTestingGroup",
    "AudioAudio",
    "BaseBoolInt",
    "BaseCity",
    "BaseCommentsInfo",
    "BaseCountry",
    "BaseCropPhoto",
    "BaseCropPhotoCrop",
    "BaseCropPhotoRect",
    "BaseError",
    "BaseErrorInnerType",
    "BaseGeo",
    "BaseGeoCoordinates",
    "BaseGradientPoint",
    "BaseImage",
    "BaseImageTheme",
    "BaseLang",
    "BaseLikes",
    "BaseLikesInfo",
    "BaseLink",
    "BaseLinkApplication",
    "BaseLinkApplicationStore",
    "BaseLinkButton",
    "BaseLinkButtonAction",
    "BaseLinkButtonActionType",
    "BaseLinkButtonStyle",
    "BaseLinkNoProduct",
    "BaseLinkProduct",
    "BaseLinkProductCategory",
    "BaseLinkProductStatus",
    "BaseLinkProductType",
    "BaseLinkRating",
    "BaseLinkRatingType",
    "BaseMessageError",
    "BaseNameCase",
    "BaseObject",
    "BaseObjectCount",
    "BaseObjectWithName",
    "BaseOwnerCover",
    "BaseOwnerCoverCropParams",
    "BasePlace",
    "BasePropertyExists",
    "BaseRepostsInfo",
    "BaseRequestParam",
    "BaseSex",
    "BaseSticker",
    "BaseStickerAnimation",
    "BaseStickerAnimationType",
    "BaseStickerInnerType",
    "BaseStickerNew",
    "BaseStickerNewInnerType",
    "BaseUploadServer",
    "BaseUserGroupFields",
    "BaseUserId",
    "BoardDefaultOrder",
    "BoardTopic",
    "BoardTopicComment",
    "BugtrackerAddCompanyGroupsMembersError",
    "BugtrackerAttachment",
    "BugtrackerAttachmentType",
    "BugtrackerBugreport",
    "BugtrackerBugreportSubscribeState",
    "BugtrackerComment",
    "BugtrackerCommentAuthor",
    "BugtrackerCompanyMember",
    "BugtrackerCompanyMemberProduct",
    "CallbackAppPayload",
    "CallbackAudioNew",
    "CallbackBase",
    "CallbackBoardPostDelete",
    "CallbackBoardPostEdit",
    "CallbackBoardPostNew",
    "CallbackBoardPostRestore",
    "CallbackConfirmation",
    "CallbackDonutMoneyWithdraw",
    "CallbackDonutMoneyWithdrawError",
    "CallbackDonutSubscriptionCancelled",
    "CallbackDonutSubscriptionCreate",
    "CallbackDonutSubscriptionExpired",
    "CallbackDonutSubscriptionPriceChanged",
    "CallbackDonutSubscriptionProlonged",
    "CallbackForeignMessage",
    "CallbackFwdMessages",
    "CallbackGroupChangePhoto",
    "CallbackGroupChangeSettings",
    "CallbackGroupJoin",
    "CallbackGroupJoinType",
    "CallbackGroupLeave",
    "CallbackGroupMarket",
    "CallbackGroupOfficerRole",
    "CallbackGroupOfficersEdit",
    "CallbackGroupSettingsChanges",
    "CallbackGroupSettingsChangesIntegerValues",
    "CallbackGroupSettingsChangesStringValues",
    "CallbackInfoForBots",
    "CallbackLikeAddRemove",
    "CallbackLikeAddRemoveObjectType",
    "CallbackMarketComment",
    "CallbackMarketCommentDelete",
    "CallbackMessage",
    "CallbackMessageAllow",
    "CallbackMessageDeny",
    "CallbackMessageEvent",
    "CallbackMessageNew",
    "CallbackMessageObject",
    "CallbackMessageReactionEvent",
    "CallbackMessageRead",
    "CallbackMessageTypingState",
    "CallbackMessageTypingStateState",
    "CallbackPhotoComment",
    "CallbackPhotoCommentDelete",
    "CallbackPhotoNew",
    "CallbackPhotoNewVerticalAlign",
    "CallbackPollVoteNew",
    "CallbackType",
    "CallbackUserBlock",
    "CallbackUserUnblock",
    "CallbackVideoComment",
    "CallbackVideoCommentDelete",
    "CallbackVideoNew",
    "CallbackVkpayTransaction",
    "CallbackWallCommentDelete",
    "CallbackWallPostNew",
    "CallbackWallPostNewInnerType",
    "CallbackWallReplyEdit",
    "CallbackWallReplyNew",
    "CallbackWallReplyRestore",
    "CallbackWallRepost",
    "CallbackWallRepostInnerType",
    "CallsCall",
    "CallsEndState",
    "CallsParticipants",
    "CallsShortCredentials",
    "CommentThread",
    "DatabaseCitiesFields",
    "DatabaseCity",
    "DatabaseCityById",
    "DatabaseFaculty",
    "DatabaseLanguageFull",
    "DatabaseRegion",
    "DatabaseSchool",
    "DatabaseSchoolClass",
    "DatabaseStation",
    "DatabaseUniversity",
    "DocsDoc",
    "DocsDocAttachmentType",
    "DocsDocPreview",
    "DocsDocPreviewAudioMsg",
    "DocsDocPreviewGraffiti",
    "DocsDocPreviewPhoto",
    "DocsDocPreviewPhotoSizes",
    "DocsDocPreviewVideo",
    "DocsDocTypes",
    "DonutDonatorSubscriptionInfo",
    "DonutDonatorSubscriptionInfoStatus",
    "EventsEventAttach",
    "FaveBookmark",
    "FaveBookmarkType",
    "FavePage",
    "FavePageType",
    "FaveTag",
    "FriendsFriendExtendedStatus",
    "FriendsFriendStatus",
    "FriendsFriendStatusStatus",
    "FriendsFriendsList",
    "FriendsMutualFriend",
    "FriendsOnlineUsers",
    "FriendsOnlineUsersWithMobile",
    "FriendsRequestsMutual",
    "FriendsRequestsXtrMessage",
    "FriendsRequestsXtrMutual",
    "GiftsGift",
    "GiftsGiftPrivacy",
    "GiftsLayout",
    "GroupsAddress",
    "GroupsAddressTimetable",
    "GroupsAddressTimetableDay",
    "GroupsAddressWorkInfoStatus",
    "GroupsAddressesInfo",
    "GroupsBanInfo",
    "GroupsBanInfoReason",
    "GroupsCallbackServer",
    "GroupsCallbackServerStatus",
    "GroupsCallbackSettings",
    "GroupsContactsItem",
    "GroupsCountersGroup",
    "GroupsFields",
    "GroupsFilter",
    "GroupsGroup",
    "GroupsGroupAccess",
    "GroupsGroupAdminLevel",
    "GroupsGroupAgeLimits",
    "GroupsGroupAttach",
    "GroupsGroupAudio",
    "GroupsGroupBanInfo",
    "GroupsGroupCategory",
    "GroupsGroupCategoryFull",
    "GroupsGroupCategoryType",
    "GroupsGroupDocs",
    "GroupsGroupFull",
    "GroupsGroupFullAgeLimits",
    "GroupsGroupFullMemberStatus",
    "GroupsGroupFullSection",
    "GroupsGroupIsClosed",
    "GroupsGroupMarketCurrency",
    "GroupsGroupPhotos",
    "GroupsGroupPublicCategoryList",
    "GroupsGroupRole",
    "GroupsGroupSubcategory",
    "GroupsGroupSubject",
    "GroupsGroupSuggestedPrivacy",
    "GroupsGroupTag",
    "GroupsGroupTagColor",
    "GroupsGroupTopics",
    "GroupsGroupType",
    "GroupsGroupVideo",
    "GroupsGroupWall",
    "GroupsGroupWiki",
    "GroupsGroupsArray",
    "GroupsLinksItem",
    "GroupsLiveCovers",
    "GroupsLongPollEvents",
    "GroupsLongPollServer",
    "GroupsLongPollSettings",
    "GroupsMarketInfo",
    "GroupsMarketProperties",
    "GroupsMarketState",
    "GroupsMemberRole",
    "GroupsMemberRolePermission",
    "GroupsMemberRoleStatus",
    "GroupsMemberStatus",
    "GroupsMemberStatusFull",
    "GroupsOnlineStatus",
    "GroupsOnlineStatusType",
    "GroupsOwnerXtrBanInfo",
    "GroupsOwnerXtrBanInfoType",
    "GroupsPhotoSize",
    "GroupsProfileItem",
    "GroupsRoleOptions",
    "GroupsSectionsListItem",
    "GroupsSettingsTwitter",
    "GroupsSettingsTwitterStatus",
    "GroupsSubjectItem",
    "GroupsTokenPermissionSetting",
    "GroupsUserXtrRole",
    "LeadFormsAnswer",
    "LeadFormsAnswerItem",
    "LeadFormsAnswerOneOf",
    "LeadFormsForm",
    "LeadFormsLead",
    "LeadFormsQuestionItem",
    "LeadFormsQuestionItemOption",
    "LeadFormsQuestionItemType",
    "LikesType",
    "LinkTargetObject",
    "MarketCurrency",
    "MarketGlobalSearchFilters",
    "MarketItemOwnerInfo",
    "MarketItemPromotionInfo",
    "MarketMarketAlbum",
    "MarketMarketCategory",
    "MarketMarketCategoryInnerType",
    "MarketMarketCategoryNested",
    "MarketMarketCategoryNestedInnerType",
    "MarketMarketCategoryTree",
    "MarketMarketCategoryTreeView",
    "MarketMarketCategoryTreeViewType",
    "MarketMarketItem",
    "MarketMarketItemAvailability",
    "MarketMarketItemBasic",
    "MarketMarketItemBasicWithGroup",
    "MarketMarketItemFull",
    "MarketOrder",
    "MarketOrderItem",
    "MarketOwnerType",
    "MarketPrice",
    "MarketProperty",
    "MarketPropertyType",
    "MarketPropertyVariant",
    "MarketServicesViewType",
    "MarketUploadPhotoData",
    "MessagesActionOneOf",
    "MessagesAudioMessage",
    "MessagesBaseMessage",
    "MessagesChat",
    "MessagesChatFull",
    "MessagesChatPreview",
    "MessagesChatPushSettings",
    "MessagesChatRestrictions",
    "MessagesChatSettings",
    "MessagesChatSettingsAcl",
    "MessagesChatSettingsPermissions",
    "MessagesChatSettingsPermissionsCall",
    "MessagesChatSettingsPermissionsChangeAdmins",
    "MessagesChatSettingsPermissionsChangeInfo",
    "MessagesChatSettingsPermissionsChangePin",
    "MessagesChatSettingsPermissionsInvite",
    "MessagesChatSettingsPermissionsSeeInviteLink",
    "MessagesChatSettingsPermissionsUseMassMentions",
    "MessagesChatSettingsPhoto",
    "MessagesChatSettingsState",
    "MessagesConversation",
    "MessagesConversationCanWrite",
    "MessagesConversationMember",
    "MessagesConversationPeer",
    "MessagesConversationPeerType",
    "MessagesConversationSortId",
    "MessagesConversationSpecialServiceType",
    "MessagesConversationWithMessage",
    "MessagesDeleteFullResponseItem",
    "MessagesForeignMessage",
    "MessagesForward",
    "MessagesFwdMessages",
    "MessagesGetConversationById",
    "MessagesGetConversationByIdExtended",
    "MessagesGetConversationMembers",
    "MessagesGetInviteLinkByOwnerResponseItem",
    "MessagesGraffiti",
    "MessagesHistoryAttachment",
    "MessagesHistoryMessageAttachment",
    "MessagesHistoryMessageAttachmentType",
    "MessagesKeyboard",
    "MessagesKeyboardButton",
    "MessagesKeyboardButtonActionCallback",
    "MessagesKeyboardButtonActionCallbackType",
    "MessagesKeyboardButtonActionLocation",
    "MessagesKeyboardButtonActionLocationType",
    "MessagesKeyboardButtonActionOpenApp",
    "MessagesKeyboardButtonActionOpenAppType",
    "MessagesKeyboardButtonActionOpenLink",
    "MessagesKeyboardButtonActionOpenLinkType",
    "MessagesKeyboardButtonActionOpenPhoto",
    "MessagesKeyboardButtonActionOpenPhotoType",
    "MessagesKeyboardButtonActionText",
    "MessagesKeyboardButtonActionTextType",
    "MessagesKeyboardButtonActionVkpay",
    "MessagesKeyboardButtonActionVkpayType",
    "MessagesKeyboardButtonColor",
    "MessagesKeyboardButtonPropertyAction",
    "MessagesLastActivity",
    "MessagesLongpollMessages",
    "MessagesLongpollParams",
    "MessagesMessage",
    "MessagesMessageAction",
    "MessagesMessageActionPhoto",
    "MessagesMessageActionStatus",
    "MessagesMessageAttachment",
    "MessagesMessageAttachmentType",
    "MessagesMessageRequestData",
    "MessagesMessagesArray",
    "MessagesOutReadBy",
    "MessagesPinnedMessage",
    "MessagesPushSettings",
    "MessagesReactionAssetItem",
    "MessagesReactionAssetItemLinks",
    "MessagesReactionCounterResponseItem",
    "MessagesReactionCountersResponseItem",
    "MessagesReactionResponseItem",
    "MessagesSendUserIdsResponseItem",
    "MessagesTemplateActionTypeNames",
    "MessagesUserTypeForXtrInvitedBy",
    "MessagesUserXtrInvitedBy",
    "NewsfeedCommentsBase",
    "NewsfeedCommentsFilters",
    "NewsfeedCommentsItem",
    "NewsfeedCommentsItemBase",
    "NewsfeedCommentsItemTypeMarket",
    "NewsfeedCommentsItemTypeNotes",
    "NewsfeedCommentsItemTypePhoto",
    "NewsfeedCommentsItemTypePost",
    "NewsfeedCommentsItemTypeTopic",
    "NewsfeedCommentsItemTypeVideo",
    "NewsfeedIgnoreItemType",
    "NewsfeedItemAudio",
    "NewsfeedItemAudioAudio",
    "NewsfeedItemBase",
    "NewsfeedItemDigest",
    "NewsfeedItemDigestButton",
    "NewsfeedItemDigestButtonStyle",
    "NewsfeedItemDigestFooter",
    "NewsfeedItemDigestFooterStyle",
    "NewsfeedItemDigestFullItem",
    "NewsfeedItemDigestHeader",
    "NewsfeedItemDigestHeaderStyle",
    "NewsfeedItemDigestItem",
    "NewsfeedItemFriend",
    "NewsfeedItemFriendFriends",
    "NewsfeedItemHolidayRecommendationsBlockHeader",
    "NewsfeedItemPhoto",
    "NewsfeedItemPhotoPhotos",
    "NewsfeedItemPhotoTag",
    "NewsfeedItemPhotoTagPhotoTags",
    "NewsfeedItemPromoButton",
    "NewsfeedItemPromoButtonAction",
    "NewsfeedItemPromoButtonImage",
    "NewsfeedItemTopic",
    "NewsfeedItemVideo",
    "NewsfeedItemVideoVideo",
    "NewsfeedItemWallpost",
    "NewsfeedItemWallpostFeedback",
    "NewsfeedItemWallpostFeedbackAnswer",
    "NewsfeedItemWallpostFeedbackType",
    "NewsfeedList",
    "NewsfeedListFull",
    "NewsfeedNewsfeedItem",
    "NewsfeedNewsfeedItemType",
    "NotesNote",
    "NotesNoteComment",
    "NotificationsFeedback",
    "NotificationsNotification",
    "NotificationsNotificationInnerType",
    "NotificationsNotificationItem",
    "NotificationsNotificationItemInnerType",
    "NotificationsReply",
    "NotificationsSendMessageError",
    "NotificationsSendMessageItem",
    "OauthError",
    "OrdersAmount",
    "OrdersAmountItem",
    "OrdersOrder",
    "OrdersOrderStatus",
    "OrdersSubscription",
    "OwnerState",
    "PagesPrivacySettings",
    "PagesWikipage",
    "PagesWikipageFull",
    "PagesWikipageHistory",
    "PhotosImage",
    "PhotosImageType",
    "PhotosPhoto",
    "PhotosPhotoAlbum",
    "PhotosPhotoAlbumFull",
    "PhotosPhotoSizes",
    "PhotosPhotoSizesType",
    "PhotosPhotoTag",
    "PhotosPhotoUpload",
    "PhotosPhotoVerticalAlign",
    "PhotosPhotoXtrTagInfo",
    "PhotosTagsSuggestionItem",
    "PhotosTagsSuggestionItemButton",
    "PhotosTagsSuggestionItemButtonAction",
    "PhotosTagsSuggestionItemButtonStyle",
    "PodcastCover",
    "PodcastExternalData",
    "PollsAnswer",
    "PollsBackground",
    "PollsBackgroundType",
    "PollsFieldsVoters",
    "PollsFriend",
    "PollsPoll",
    "PollsPollAnonymous",
    "PollsPollExtended",
    "PollsVoters",
    "PollsVotersFieldsUsers",
    "PollsVotersUsers",
    "PrettyCardsButtonOneOf",
    "PrettyCardsPrettyCard",
    "PrettyCardsPrettyCardInnerType",
    "PrettyCardsPrettyCardOrError",
    "SearchHint",
    "SearchHintSection",
    "SearchHintType",
    "SecureGiveEventStickerItem",
    "SecureLevel",
    "SecureSetCounterItem",
    "SecureSmsNotification",
    "SecureTokenChecked",
    "SecureTransaction",
    "StatsActivity",
    "StatsCity",
    "StatsCountry",
    "StatsPeriod",
    "StatsPeriodFromOneOf",
    "StatsPeriodToOneOf",
    "StatsReach",
    "StatsSexAge",
    "StatsViews",
    "StatsWallpostStat",
    "StatusStatus",
    "StickersImageSet",
    "StorageValue",
    "StoreProduct",
    "StoreProductIcon",
    "StoreProductType",
    "StoreStickersKeyword",
    "StoreStickersKeywordSticker",
    "StoriesClickableArea",
    "StoriesClickableSticker",
    "StoriesClickableStickerStyle",
    "StoriesClickableStickerSubtype",
    "StoriesClickableStickerType",
    "StoriesClickableStickers",
    "StoriesFeedItem",
    "StoriesFeedItemType",
    "StoriesPromoBlock",
    "StoriesReplies",
    "StoriesStory",
    "StoriesStoryLink",
    "StoriesStoryStats",
    "StoriesStoryStatsStat",
    "StoriesStoryStatsState",
    "StoriesStoryType",
    "StoriesUploadLinkText",
    "StoriesUploadResult",
    "StoriesViewersItem",
    "StreamingStats",
    "StreamingStatsEventType",
    "StreamingStatsPoint",
    "UsersCareer",
    "UsersExports",
    "UsersFields",
    "UsersLastSeen",
    "UsersMilitary",
    "UsersOccupation",
    "UsersOccupationType",
    "UsersOnlineInfo",
    "UsersOnlineInfoStatus",
    "UsersPersonal",
    "UsersRelative",
    "UsersRelativeType",
    "UsersSchool",
    "UsersSubscriptionsItem",
    "UsersUniversity",
    "UsersUser",
    "UsersUserConnections",
    "UsersUserCounters",
    "UsersUserFull",
    "UsersUserMin",
    "UsersUserRelation",
    "UsersUserSettingsXtr",
    "UsersUserType",
    "UsersUserXtrType",
    "UsersUsersArray",
    "UtilsDomainResolved",
    "UtilsDomainResolvedType",
    "UtilsLastShortenedLink",
    "UtilsLinkChecked",
    "UtilsLinkCheckedStatus",
    "UtilsLinkStats",
    "UtilsLinkStatsExtended",
    "UtilsShortLink",
    "UtilsStats",
    "UtilsStatsCity",
    "UtilsStatsCountry",
    "UtilsStatsExtended",
    "UtilsStatsSexAge",
    "VideoEpisode",
    "VideoLiveCategory",
    "VideoLiveInfo",
    "VideoLiveSettings",
    "VideoPlaylistPrivacyCategory",
    "VideoSaveResult",
    "VideoStreamInputParams",
    "VideoVideo",
    "VideoVideoAlbum",
    "VideoVideoAlbumFull",
    "VideoVideoAlbumResponseType",
    "VideoVideoFiles",
    "VideoVideoFull",
    "VideoVideoImage",
    "VideoVideoResponseType",
    "VideoVideoType",
    "WallAppPost",
    "WallAttachedNote",
    "WallCarouselBase",
    "WallCommentAttachment",
    "WallCommentAttachmentType",
    "WallGeo",
    "WallGeoType",
    "WallGetFilter",
    "WallGraffiti",
    "WallPostCopyright",
    "WallPostSource",
    "WallPostSourceType",
    "WallPostType",
    "WallPostedPhoto",
    "WallViews",
    "WallWallComment",
    "WallWallCommentDonut",
    "WallWallCommentDonutPlaceholder",
    "WallWallItem",
    "WallWallpost",
    "WallWallpostAttachment",
    "WallWallpostAttachmentType",
    "WallWallpostCommentsDonut",
    "WallWallpostCommentsDonutPlaceholder",
    "WallWallpostDonut",
    "WallWallpostDonutEditMode",
    "WallWallpostDonutPlaceholder",
    "WallWallpostFull",
    "WallWallpostInnerType",
    "WidgetsCommentMedia",
    "WidgetsCommentMediaType",
    "WidgetsCommentReplies",
    "WidgetsCommentRepliesItem",
    "WidgetsWidgetComment",
    "WidgetsWidgetLikes",
    "WidgetsWidgetPage",
)
