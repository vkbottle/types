import datetime
import enum

import typing_extensions as typing

from vkbottle_types.base_model import BaseEnumMeta, BaseModel, Field


class BaseBoolInt(int, enum.Enum, metaclass=BaseEnumMeta):
    NO = 0
    YES = 1


class BaseCity(BaseModel):
    """
    Model: `BaseCity`
    """

    id: int = Field()
    """City ID."""

    title: str = Field()
    """City title."""


class BaseCommentsInfo(BaseModel):
    """
    Model: `BaseCommentsInfo`
    """

    can_post: typing.Optional[bool] = Field(
        default=None,
    )
    """Information whether current user can comment the post."""

    can_open: typing.Optional[bool] = Field(
        default=None,
    )
    """Property `BaseCommentsInfo.can_open`."""

    can_close: typing.Optional[bool] = Field(
        default=None,
    )
    """Property `BaseCommentsInfo.can_close`."""

    can_view: typing.Optional[bool] = Field(
        default=None,
    )
    """Information whether current user can view the comments."""

    count: typing.Optional[int] = Field(
        default=None,
    )
    """Comments number."""

    groups_can_post: typing.Optional[bool] = Field(
        default=None,
    )
    """Information whether groups can comment the post."""

    donut: typing.Optional["WallWallpostCommentsDonut"] = Field(
        default=None,
    )
    """Property `BaseCommentsInfo.donut`."""

    list: typing.Optional[typing.List["WallWallComment"]] = Field(
        default=None,
    )
    """Property `BaseCommentsInfo.list`."""


class BaseCountry(BaseModel):
    """
    Model: `BaseCountry`
    """

    id: int = Field()
    """Country ID."""

    title: str = Field()
    """Country title."""


class BaseCropPhoto(BaseModel):
    """
    Model: `BaseCropPhoto`
    """

    photo: "PhotosPhoto" = Field()
    """Property `BaseCropPhoto.photo`."""

    crop: "BaseCropPhotoCrop" = Field()
    """Property `BaseCropPhoto.crop`."""

    rect: "BaseCropPhotoRect" = Field()
    """Property `BaseCropPhoto.rect`."""


class BaseCropPhotoCrop(BaseModel):
    """
    Model: `BaseCropPhotoCrop`
    """

    x: float = Field()
    """Coordinate X of the left upper corner."""

    y: float = Field()
    """Coordinate Y of the left upper corner."""

    x2: float = Field()
    """Coordinate X of the right lower corner."""

    y2: float = Field()
    """Coordinate Y of the right lower corner."""


class BaseCropPhotoRect(BaseModel):
    """
    Model: `BaseCropPhotoRect`
    """

    x: float = Field()
    """Coordinate X of the left upper corner."""

    y: float = Field()
    """Coordinate Y of the left upper corner."""

    x2: float = Field()
    """Coordinate X of the right lower corner."""

    y2: float = Field()
    """Coordinate Y of the right lower corner."""


class BaseErrorInnerType(str, enum.Enum, metaclass=BaseEnumMeta):
    BASE_ERROR = "base_error"


class BaseError(BaseModel):
    """
    Model: `BaseError`
    """

    inner_type: "BaseErrorInnerType" = Field()
    """Property `BaseError.inner_type`."""

    error_code: int = Field()
    """Error code."""

    error_subcode: typing.Optional[int] = Field(
        default=None,
    )
    """Error subcode."""

    error_msg: typing.Optional[str] = Field(
        default=None,
    )
    """Error message."""

    error_text: typing.Optional[str] = Field(
        default=None,
    )
    """Localized error message."""

    request_params: typing.Optional[typing.List["BaseRequestParam"]] = Field(
        default=None,
    )
    """Property `BaseError.request_params`."""


class BaseGeo(BaseModel):
    """
    Model: `BaseGeo`
    """

    coordinates: typing.Optional["BaseGeoCoordinates"] = Field(
        default=None,
    )
    """Property `BaseGeo.coordinates`."""

    place: typing.Optional["BasePlace"] = Field(
        default=None,
    )
    """Property `BaseGeo.place`."""

    showmap: typing.Optional[int] = Field(
        default=None,
    )
    """Information whether a map is showed."""

    type: typing.Optional[str] = Field(
        default=None,
    )
    """Place type."""


class BaseGeoCoordinates(BaseModel):
    """
    Model: `BaseGeoCoordinates`
    """

    latitude: float = Field()
    """Property `BaseGeoCoordinates.latitude`."""

    longitude: float = Field()
    """Property `BaseGeoCoordinates.longitude`."""


class BaseGradientPoint(BaseModel):
    """
    Model: `BaseGradientPoint`
    """

    color: str = Field()
    """Hex color code without #."""

    position: float = Field()
    """Point position."""


class BaseImageTheme(str, enum.Enum, metaclass=BaseEnumMeta):
    LIGHT = "light"
    DARK = "dark"


class BaseImage(BaseModel):
    """
    Model: `BaseImage`
    """

    url: str = Field()
    """Image url."""

    width: int = Field()
    """Image width."""

    height: int = Field()
    """Image height."""

    id: typing.Optional[str] = Field(
        default=None,
    )
    """Property `BaseImage.id`."""

    theme: typing.Optional["BaseImageTheme"] = Field(
        default=None,
    )
    """Property `BaseImage.theme`."""


class BaseLang(str, enum.Enum, metaclass=BaseEnumMeta):
    RU = "ru"
    UA = "ua"
    BE = "be"
    EN = "en"
    ES = "es"
    FI = "fi"
    DE = "de"
    IT = "it"


class BaseLikes(BaseModel):
    """
    Model: `BaseLikes`
    """

    count: typing.Optional[int] = Field(
        default=None,
    )
    """Likes number."""

    user_likes: typing.Optional[bool] = Field(
        default=None,
    )
    """Information whether current user likes the photo."""


class BaseLikesInfo(BaseModel):
    """
    Model: `BaseLikesInfo`
    """

    can_like: bool = Field()
    """Information whether current user can like the post."""

    count: int = Field()
    """Likes number."""

    user_likes: bool = Field()
    """Information whether current uer has liked the post."""

    can_publish: typing.Optional[bool] = Field(
        default=None,
    )
    """Information whether current user can repost."""

    can_like_as_author: typing.Optional[bool] = Field(
        default=None,
    )
    """Whether user can like comment as author."""

    can_like_by_group: typing.Optional[bool] = Field(
        default=None,
    )
    """Whether current owner of the group can like the reply."""

    author_liked: typing.Optional[bool] = Field(
        default=None,
    )
    """Information whether post author liked the reply."""

    group_liked: typing.Optional[bool] = Field(
        default=None,
    )
    """Information whether group liked the reply."""

    repost_disabled: typing.Optional[bool] = Field(
        default=None,
    )
    """Remove repost feature for post."""


class BaseLinkApplication(BaseModel):
    """
    Model: `BaseLinkApplication`
    """

    app_id: typing.Optional[float] = Field(
        default=None,
    )
    """Application Id."""

    store: typing.Optional["BaseLinkApplicationStore"] = Field(
        default=None,
    )
    """Property `BaseLinkApplication.store`."""


class BaseLinkApplicationStore(BaseModel):
    """
    Model: `BaseLinkApplicationStore`
    """

    id: typing.Optional[float] = Field(
        default=None,
    )
    """Store Id."""

    name: typing.Optional[str] = Field(
        default=None,
    )
    """Store name."""


class BaseLinkButton(BaseModel):
    """
    Model: `BaseLinkButton`
    """

    action: typing.Optional["BaseLinkButtonAction"] = Field(
        default=None,
    )
    """Button action."""

    title: typing.Optional[str] = Field(
        default=None,
    )
    """Button title."""

    block_id: typing.Optional[str] = Field(
        default=None,
    )
    """Target block id."""

    section_id: typing.Optional[str] = Field(
        default=None,
    )
    """Target section id."""

    artist_id: typing.Optional[str] = Field(
        default=None,
    )
    """artist id."""

    curator_id: typing.Optional[int] = Field(
        default=None,
    )
    """curator id."""

    album_id: typing.Optional[int] = Field(
        default=None,
    )
    """Video album id."""

    owner_id: typing.Optional[int] = Field(
        default=None,
    )
    """Owner id."""

    icon: typing.Optional[str] = Field(
        default=None,
    )
    """Button icon name, e.g. \'phone\' or \'gift\'."""

    style: typing.Optional["BaseLinkButtonStyle"] = Field(
        default=None,
    )
    """Property `BaseLinkButton.style`."""

    audio_id: typing.Optional[int] = Field(
        default=None,
    )
    """Property `BaseLinkButton.audio_id`."""

    hashtag: typing.Optional[str] = Field(
        default=None,
    )
    """Property `BaseLinkButton.hashtag`."""


class BaseLinkButtonAction(BaseModel):
    """
    Model: `BaseLinkButtonAction`
    """

    type: "BaseLinkButtonActionType" = Field()
    """Property `BaseLinkButtonAction.type`."""

    url: typing.Optional[str] = Field(
        default=None,
    )
    """Action URL."""

    consume_reason: typing.Optional[str] = Field(
        default=None,
    )
    """Property `BaseLinkButtonAction.consume_reason`."""


class BaseLinkButtonActionType(str, enum.Enum, metaclass=BaseEnumMeta):
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


class BaseLinkButtonStyle(str, enum.Enum, metaclass=BaseEnumMeta):
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
    """
    Model: `BaseLinkNoProduct`
    """

    url: str = Field()
    """Link URL."""

    application: typing.Optional["BaseLinkApplication"] = Field(
        default=None,
    )
    """Property `BaseLinkNoProduct.application`."""

    button: typing.Optional["BaseLinkButton"] = Field(
        default=None,
    )
    """Property `BaseLinkNoProduct.button`."""

    caption: typing.Optional[str] = Field(
        default=None,
    )
    """Link caption."""

    description: typing.Optional[str] = Field(
        default=None,
    )
    """Link description."""

    id: typing.Optional[str] = Field(
        default=None,
    )
    """Link ID."""

    is_favorite: typing.Optional[bool] = Field(
        default=None,
    )
    """Property `BaseLinkNoProduct.is_favorite`."""

    photo: typing.Optional["PhotosPhoto"] = Field(
        default=None,
    )
    """Property `BaseLinkNoProduct.photo`."""

    preview_page: typing.Optional[str] = Field(
        default=None,
    )
    """String ID of the page with article preview."""

    preview_url: typing.Optional[str] = Field(
        default=None,
    )
    """URL of the page with article preview."""

    rating: typing.Optional["BaseLinkRating"] = Field(
        default=None,
    )
    """Property `BaseLinkNoProduct.rating`."""

    title: typing.Optional[str] = Field(
        default=None,
    )
    """Link title."""

    target_object: typing.Optional["LinkTargetObject"] = Field(
        default=None,
    )
    """Property `BaseLinkNoProduct.target_object`."""

    is_external: typing.Optional[bool] = Field(
        default=None,
    )
    """Information whether the current link is external."""

    video: typing.Optional["VideoVideoFull"] = Field(
        default=None,
    )
    """Video from link."""


class BaseLinkProductType(str, enum.Enum, metaclass=BaseEnumMeta):
    PRODUCT = "product"


class BaseLinkProduct(BaseModel):
    """
    Model: `BaseLinkProduct`
    """

    price: "MarketPrice" = Field()
    """Property `BaseLinkProduct.price`."""

    merchant: typing.Optional[str] = Field(
        default=None,
    )
    """Property `BaseLinkProduct.merchant`."""

    category: typing.Optional["BaseLinkProductCategory"] = Field(
        default=None,
    )
    """Property `BaseLinkProduct.category`."""

    geo: typing.Optional["BaseGeoCoordinates"] = Field(
        default=None,
    )
    """Property `BaseLinkProduct.geo`."""

    distance: typing.Optional[int] = Field(
        default=None,
    )
    """Property `BaseLinkProduct.distance`."""

    city: typing.Optional[str] = Field(
        default=None,
    )
    """Property `BaseLinkProduct.city`."""

    status: typing.Optional["BaseLinkProductStatus"] = Field(
        default=None,
    )
    """Property `BaseLinkProduct.status`."""

    orders_count: typing.Optional[int] = Field(
        default=None,
    )
    """Property `BaseLinkProduct.orders_count`."""

    type: typing.Optional["BaseLinkProductType"] = Field(
        default=None,
    )
    """Property `BaseLinkProduct.type`."""


class BaseLinkProductCategory(BaseModel):
    """
    Model: `BaseLinkProductCategory`
    """


class BaseLinkProductStatus(str, enum.Enum, metaclass=BaseEnumMeta):
    ACTIVE = "active"
    BLOCKED = "blocked"
    SOLD = "sold"
    DELETED = "deleted"
    ARCHIVED = "archived"


class BaseLinkRatingType(str, enum.Enum, metaclass=BaseEnumMeta):
    RATING = "rating"


class BaseLinkRating(BaseModel):
    """
    Model: `BaseLinkRating`
    """

    reviews_count: typing.Optional[int] = Field(
        default=None,
    )
    """Count of reviews."""

    stars: typing.Optional[float] = Field(
        default=None,
    )
    """Count of stars."""

    type: typing.Optional["BaseLinkRatingType"] = Field(
        default=None,
    )
    """Property `BaseLinkRating.type`."""


class BaseMessageError(BaseModel):
    """
    Model: `BaseMessageError`
    """

    code: typing.Optional[int] = Field(
        default=None,
    )
    """Error code."""

    description: typing.Optional[str] = Field(
        default=None,
    )
    """Error message."""


class BaseNameCase(str, enum.Enum, metaclass=BaseEnumMeta):
    NOM = "Nom"
    GEN = "Gen"
    DAT = "Dat"
    ACC = "Acc"
    INS = "Ins"
    ABL = "Abl"


class BaseObject(BaseModel):
    """
    Model: `BaseObject`
    """

    id: int = Field()
    """Object ID."""

    title: str = Field()
    """Object title."""


class BaseObjectCount(BaseModel):
    """
    Model: `BaseObjectCount`
    """

    count: typing.Optional[int] = Field(
        default=None,
    )
    """Items count."""


class BaseObjectWithName(BaseModel):
    """
    Model: `BaseObjectWithName`
    """

    id: int = Field()
    """Object ID."""

    name: str = Field()
    """Object name."""


class BaseOwnerCover(BaseModel):
    """
    Model: `BaseOwnerCover`
    """

    enabled: bool = Field()
    """Information whether cover is enabled."""

    images: typing.Optional[typing.List["BaseImage"]] = Field(
        default=None,
    )
    """Property `BaseOwnerCover.images`."""

    crop_params: typing.Optional["BaseOwnerCoverCropParams"] = Field(
        default=None,
    )
    """Property `BaseOwnerCover.crop_params`."""

    original_image: typing.Optional["BaseImage"] = Field(
        default=None,
    )
    """Property `BaseOwnerCover.original_image`."""

    photo_id: typing.Optional[int] = Field(
        default=None,
    )
    """Property `BaseOwnerCover.photo_id`."""


class BaseOwnerCoverCropParams(BaseModel):
    """
    Model: `BaseOwnerCoverCropParams`
    """

    x: typing.Optional[int] = Field(
        default=None,
    )
    """Property `BaseOwnerCoverCropParams.x`."""

    y: typing.Optional[int] = Field(
        default=None,
    )
    """Property `BaseOwnerCoverCropParams.y`."""

    width: typing.Optional[int] = Field(
        default=None,
    )
    """Property `BaseOwnerCoverCropParams.width`."""

    height: typing.Optional[int] = Field(
        default=None,
    )
    """Property `BaseOwnerCoverCropParams.height`."""


class BasePlace(BaseModel):
    """
    Model: `BasePlace`
    """

    address: typing.Optional[str] = Field(
        default=None,
    )
    """Place address."""

    checkins: typing.Optional[int] = Field(
        default=None,
    )
    """Checkins number."""

    city: typing.Optional[str] = Field(
        default=None,
    )
    """City name."""

    created: typing.Optional[int] = Field(
        default=None,
    )
    """Date of the place creation in Unixtime."""

    icon: typing.Optional[str] = Field(
        default=None,
    )
    """URL of the place\'s icon."""

    id: typing.Optional[int] = Field(
        default=None,
    )
    """Place ID."""

    latitude: typing.Optional[float] = Field(
        default=None,
    )
    """Place latitude."""

    longitude: typing.Optional[float] = Field(
        default=None,
    )
    """Place longitude."""

    title: typing.Optional[str] = Field(
        default=None,
    )
    """Place title."""

    type: typing.Optional[str] = Field(
        default=None,
    )
    """Place type."""


class BasePropertyExists(int, enum.Enum, metaclass=BaseEnumMeta):
    PROPERTY_EXISTS = 1


class BaseRepostsInfo(BaseModel):
    """
    Count of views
    Model: `BaseRepostsInfo`
    """

    count: int = Field()
    """Total reposts counter. Sum of wall and mail reposts counters."""

    wall_count: typing.Optional[int] = Field(
        default=None,
    )
    """Wall reposts counter."""

    mail_count: typing.Optional[int] = Field(
        default=None,
    )
    """Mail reposts counter."""

    user_reposted: typing.Optional[bool] = Field(
        default=None,
    )
    """Information whether current user has reposted the post."""


class BaseRequestParam(BaseModel):
    """
    Model: `BaseRequestParam`
    """

    key: str = Field()
    """Parameter name."""

    value: str = Field()
    """Parameter value."""


class BaseSex(int, enum.Enum, metaclass=BaseEnumMeta):
    UNKNOWN = 0
    FEMALE = 1
    MALE = 2


class BaseStickerInnerType(str, enum.Enum, metaclass=BaseEnumMeta):
    BASE_STICKER_NEW = "base_sticker_new"


class BaseSticker(BaseModel):
    """
    Model: `BaseSticker`
    """

    inner_type: "BaseStickerInnerType" = Field()
    """Property `BaseSticker.inner_type`."""

    sticker_id: typing.Optional[int] = Field(
        default=None,
    )
    """Sticker ID."""

    product_id: typing.Optional[int] = Field(
        default=None,
    )
    """Pack ID."""

    images: typing.Optional[typing.List["BaseImage"]] = Field(
        default=None,
    )
    """Property `BaseSticker.images`."""

    images_with_background: typing.Optional[typing.List["BaseImage"]] = Field(
        default=None,
    )
    """Property `BaseSticker.images_with_background`."""

    animation_url: typing.Optional[str] = Field(
        default=None,
    )
    """URL of sticker animation script."""

    animations: typing.Optional[typing.List["BaseStickerAnimation"]] = Field(
        default=None,
    )
    """Array of sticker animation script objects."""

    is_allowed: typing.Optional[bool] = Field(
        default=None,
    )
    """Information whether the sticker is allowed."""


class BaseStickerAnimationType(str, enum.Enum, metaclass=BaseEnumMeta):
    LIGHT = "light"
    DARK = "dark"


class BaseStickerAnimation(BaseModel):
    """
    Model: `BaseStickerAnimation`
    """

    type: typing.Optional["BaseStickerAnimationType"] = Field(
        default=None,
    )
    """Type of animation script."""

    url: typing.Optional[str] = Field(
        default=None,
    )
    """URL of animation script."""


class BaseStickerNewInnerType(str, enum.Enum, metaclass=BaseEnumMeta):
    BASE_STICKER_NEW = "base_sticker_new"


class BaseStickerNew(BaseModel):
    """
    Model: `BaseStickerNew`
    """

    inner_type: "BaseStickerNewInnerType" = Field()
    """Property `BaseStickerNew.inner_type`."""

    sticker_id: typing.Optional[int] = Field(
        default=None,
    )
    """Sticker ID."""

    product_id: typing.Optional[int] = Field(
        default=None,
    )
    """Pack ID."""

    images: typing.Optional[typing.List["BaseImage"]] = Field(
        default=None,
    )
    """Property `BaseStickerNew.images`."""

    images_with_background: typing.Optional[typing.List["BaseImage"]] = Field(
        default=None,
    )
    """Property `BaseStickerNew.images_with_background`."""

    animation_url: typing.Optional[str] = Field(
        default=None,
    )
    """URL of sticker animation script."""

    animations: typing.Optional[typing.List["BaseStickerAnimation"]] = Field(
        default=None,
    )
    """Array of sticker animation script objects."""

    is_allowed: typing.Optional[bool] = Field(
        default=None,
    )
    """Information whether the sticker is allowed."""


class BaseUploadServer(BaseModel):
    """
    Model: `BaseUploadServer`
    """

    upload_url: str = Field()
    """Upload URL."""


class BaseUserGroupFields(str, enum.Enum, metaclass=BaseEnumMeta):
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
    """
    Model: `BaseUserId`
    """

    user_id: typing.Optional[int] = Field(
        default=None,
    )
    """User ID."""


class UsersCareer(BaseModel):
    """
    Model: `UsersCareer`
    """

    city_id: typing.Optional[int] = Field(
        default=None,
    )
    """City ID."""

    city_name: typing.Optional[str] = Field(
        default=None,
    )
    """City name."""

    company: typing.Optional[str] = Field(
        default=None,
    )
    """Company name."""

    from_: typing.Optional[int] = Field(
        default=None,
        alias="from",
    )
    """From year."""

    group_id: typing.Optional[int] = Field(
        default=None,
    )
    """Community ID."""

    id: typing.Optional[int] = Field(
        default=None,
    )
    """Career ID."""

    position: typing.Optional[str] = Field(
        default=None,
    )
    """Position."""

    until: typing.Optional[int] = Field(
        default=None,
    )
    """Till year."""


class UsersExports(BaseModel):
    """
    Model: `UsersExports`
    """

    facebook: typing.Optional[int] = Field(
        default=None,
    )
    """Property `UsersExports.facebook`."""

    livejournal: typing.Optional[int] = Field(
        default=None,
    )
    """Property `UsersExports.livejournal`."""

    twitter: typing.Optional[int] = Field(
        default=None,
    )
    """Property `UsersExports.twitter`."""


class UsersFields(str, enum.Enum, metaclass=BaseEnumMeta):
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
    """
    Model: `UsersLastSeen`
    """

    platform: typing.Optional[int] = Field(
        default=None,
    )
    """Type of the platform that used for the last authorization."""

    time: typing.Optional[int] = Field(
        default=None,
    )
    """Last visit date (in Unix time)."""


class UsersMilitary(BaseModel):
    """
    Model: `UsersMilitary`
    """

    unit: str = Field()
    """Unit name."""

    unit_id: int = Field()
    """Unit ID."""

    from_: typing.Optional[int] = Field(
        default=None,
        alias="from",
    )
    """From year."""

    id: typing.Optional[int] = Field(
        default=None,
    )
    """Military ID."""

    until: typing.Optional[int] = Field(
        default=None,
    )
    """Till year."""


class UsersOccupationType(str, enum.Enum, metaclass=BaseEnumMeta):
    SCHOOL = "school"
    UNIVERSITY = "university"
    WORK = "work"


class UsersOccupation(BaseModel):
    """
    Model: `UsersOccupation`
    """

    id: typing.Optional[int] = Field(
        default=None,
    )
    """ID of school, university, company group."""

    name: typing.Optional[str] = Field(
        default=None,
    )
    """Name of occupation."""

    type: typing.Optional["UsersOccupationType"] = Field(
        default=None,
    )
    """Type of occupation."""

    graduate_year: typing.Optional[int] = Field(
        default=None,
    )
    """Property `UsersOccupation.graduate_year`."""

    city_id: typing.Optional[int] = Field(
        default=None,
    )
    """Property `UsersOccupation.city_id`."""


class UsersOnlineInfoStatus(str, enum.Enum, metaclass=BaseEnumMeta):
    RECENTLY = "recently"
    LAST_WEEK = "last_week"
    LAST_MONTH = "last_month"
    LONG_AGO = "long_ago"
    NOT_SHOW = "not_show"


class UsersOnlineInfo(BaseModel):
    """
    Model: `UsersOnlineInfo`
    """

    visible: bool = Field()
    """Whether you can see real online status of user or not."""

    last_seen: typing.Optional[int] = Field(
        default=None,
    )
    """Last time we saw user being active."""

    is_online: typing.Optional[bool] = Field(
        default=None,
    )
    """Whether user is currently online or not."""

    app_id: typing.Optional[int] = Field(
        default=None,
    )
    """Application id from which user is currently online or was last seen online."""

    is_mobile: typing.Optional[bool] = Field(
        default=None,
    )
    """Is user online from desktop app or mobile app."""

    status: typing.Optional["UsersOnlineInfoStatus"] = Field(
        default=None,
    )
    """In case user online is not visible, it indicates approximate timeframe of user online."""


class UsersPersonal(BaseModel):
    """
    Model: `UsersPersonal`
    """

    alcohol: typing.Optional[int] = Field(
        default=None,
    )
    """User\'s views on alcohol."""

    inspired_by: typing.Optional[str] = Field(
        default=None,
    )
    """User\'s inspired by."""

    langs: typing.Optional[typing.List[str]] = Field(
        default=None,
    )
    """Property `UsersPersonal.langs`."""

    langs_full: typing.Optional[typing.List["DatabaseLanguageFull"]] = Field(
        default=None,
    )
    """User\'s languages with full info."""

    life_main: typing.Optional[int] = Field(
        default=None,
    )
    """User\'s personal priority in life."""

    people_main: typing.Optional[int] = Field(
        default=None,
    )
    """User\'s personal priority in people."""

    political: typing.Optional[int] = Field(
        default=None,
    )
    """User\'s political views."""

    religion: typing.Optional[str] = Field(
        default=None,
    )
    """User\'s religion."""

    religion_id: typing.Optional[int] = Field(
        default=None,
    )
    """User\'s religion id."""

    smoking: typing.Optional[int] = Field(
        default=None,
    )
    """User\'s views on smoking."""


class UsersRelativeType(str, enum.Enum, metaclass=BaseEnumMeta):
    PARENT = "parent"
    CHILD = "child"
    GRANDPARENT = "grandparent"
    GRANDCHILD = "grandchild"
    SIBLING = "sibling"


class UsersRelative(BaseModel):
    """
    Model: `UsersRelative`
    """

    type: "UsersRelativeType" = Field()
    """Relative type."""

    birth_date: typing.Optional[str] = Field(
        default=None,
    )
    """Date of child birthday (format dd.mm.yyyy)."""

    id: typing.Optional[int] = Field(
        default=None,
    )
    """Relative ID."""

    name: typing.Optional[str] = Field(
        default=None,
    )
    """Name of relative."""


class UsersSchool(BaseModel):
    """
    Model: `UsersSchool`
    """

    city: typing.Optional[int] = Field(
        default=None,
    )
    """City ID."""

    class_: typing.Optional[str] = Field(
        default=None,
        alias="class",
    )
    """School class letter."""

    class_id: typing.Optional[int] = Field(
        default=None,
    )
    """School class id."""

    id: typing.Optional[str] = Field(
        default=None,
    )
    """School ID."""

    name: typing.Optional[str] = Field(
        default=None,
    )
    """School name."""

    type: typing.Optional[int] = Field(
        default=None,
    )
    """School type ID."""

    type_str: typing.Optional[str] = Field(
        default=None,
    )
    """School type name."""

    year_from: typing.Optional[int] = Field(
        default=None,
    )
    """Year the user started to study."""

    year_graduated: typing.Optional[int] = Field(
        default=None,
    )
    """Graduation year."""

    year_to: typing.Optional[int] = Field(
        default=None,
    )
    """Year the user finished to study."""

    speciality: typing.Optional[str] = Field(
        default=None,
    )
    """Property `UsersSchool.speciality`."""


class UsersSubscriptionsItem(BaseModel):
    """
    Model: `UsersSubscriptionsItem`
    """


class UsersUniversity(BaseModel):
    """
    Model: `UsersUniversity`
    """

    chair: typing.Optional[int] = Field(
        default=None,
    )
    """Chair ID."""

    chair_name: typing.Optional[str] = Field(
        default=None,
    )
    """Chair name."""

    city: typing.Optional[int] = Field(
        default=None,
    )
    """City ID."""

    education_form: typing.Optional[str] = Field(
        default=None,
    )
    """Education form."""

    education_form_id: typing.Optional[int] = Field(
        default=None,
    )
    """Education form id."""

    education_status: typing.Optional[str] = Field(
        default=None,
    )
    """Education status."""

    education_status_id: typing.Optional[int] = Field(
        default=None,
    )
    """Education status id."""

    faculty: typing.Optional[int] = Field(
        default=None,
    )
    """Faculty ID."""

    faculty_name: typing.Optional[str] = Field(
        default=None,
    )
    """Faculty name."""

    graduation: typing.Optional[int] = Field(
        default=None,
    )
    """Graduation year."""

    id: typing.Optional[int] = Field(
        default=None,
    )
    """University ID."""

    name: typing.Optional[str] = Field(
        default=None,
    )
    """University name."""

    university_group_id: typing.Optional[int] = Field(
        default=None,
    )
    """Property `UsersUniversity.university_group_id`."""


class UsersUserConnections(BaseModel):
    """
    Model: `UsersUserConnections`
    """

    skype: str = Field()
    """User\'s Skype nickname."""

    facebook: str = Field()
    """User\'s Facebook account."""

    twitter: str = Field()
    """User\'s Twitter account."""

    instagram: str = Field()
    """User\'s Instagram account."""

    facebook_name: typing.Optional[str] = Field(
        default=None,
    )
    """User\'s Facebook name."""

    livejournal: typing.Optional[str] = Field(
        default=None,
    )
    """User\'s Livejournal account."""


class UsersUserCounters(BaseModel):
    """
    Model: `UsersUserCounters`
    """

    albums: typing.Optional[int] = Field(
        default=None,
    )
    """Albums number."""

    badges: typing.Optional[int] = Field(
        default=None,
    )
    """Badges number."""

    audios: typing.Optional[int] = Field(
        default=None,
    )
    """Audios number."""

    followers: typing.Optional[int] = Field(
        default=None,
    )
    """Followers number."""

    friends: typing.Optional[int] = Field(
        default=None,
    )
    """Friends number."""

    gifts: typing.Optional[int] = Field(
        default=None,
    )
    """Gifts number."""

    groups: typing.Optional[int] = Field(
        default=None,
    )
    """Communities number."""

    notes: typing.Optional[int] = Field(
        default=None,
    )
    """Notes number."""

    online_friends: typing.Optional[int] = Field(
        default=None,
    )
    """Online friends number."""

    pages: typing.Optional[int] = Field(
        default=None,
    )
    """Public pages number."""

    photos: typing.Optional[int] = Field(
        default=None,
    )
    """Photos number."""

    subscriptions: typing.Optional[int] = Field(
        default=None,
    )
    """Subscriptions number."""

    user_photos: typing.Optional[int] = Field(
        default=None,
    )
    """Number of photos with user."""

    user_videos: typing.Optional[int] = Field(
        default=None,
    )
    """Number of videos with user."""

    videos: typing.Optional[int] = Field(
        default=None,
    )
    """Videos number."""

    video_playlists: typing.Optional[int] = Field(
        default=None,
    )
    """Playlists number."""

    new_photo_tags: typing.Optional[int] = Field(
        default=None,
    )
    """Property `UsersUserCounters.new_photo_tags`."""

    new_recognition_tags: typing.Optional[int] = Field(
        default=None,
    )
    """Property `UsersUserCounters.new_recognition_tags`."""

    mutual_friends: typing.Optional[int] = Field(
        default=None,
    )
    """Property `UsersUserCounters.mutual_friends`."""

    friends_followers: typing.Optional[int] = Field(
        default=None,
    )
    """Property `UsersUserCounters.friends_followers`."""

    posts: typing.Optional[int] = Field(
        default=None,
    )
    """Property `UsersUserCounters.posts`."""

    articles: typing.Optional[int] = Field(
        default=None,
    )
    """Property `UsersUserCounters.articles`."""

    wishes: typing.Optional[int] = Field(
        default=None,
    )
    """Property `UsersUserCounters.wishes`."""

    podcasts: typing.Optional[int] = Field(
        default=None,
    )
    """Property `UsersUserCounters.podcasts`."""

    clips: typing.Optional[int] = Field(
        default=None,
    )
    """Property `UsersUserCounters.clips`."""

    clips_followers: typing.Optional[int] = Field(
        default=None,
    )
    """Property `UsersUserCounters.clips_followers`."""

    videos_followers: typing.Optional[int] = Field(
        default=None,
    )
    """Videos followers number."""

    clips_views: typing.Optional[int] = Field(
        default=None,
    )
    """Property `UsersUserCounters.clips_views`."""

    clips_likes: typing.Optional[int] = Field(
        default=None,
    )
    """Property `UsersUserCounters.clips_likes`."""


class UsersUserMin(BaseModel):
    """
    Model: `UsersUserMin`
    """

    id: int = Field()
    """User ID."""

    deactivated: typing.Optional[str] = Field(
        default=None,
    )
    """Returns if a profile is deleted or blocked."""

    first_name: typing.Optional[str] = Field(
        default=None,
    )
    """User first name."""

    hidden: typing.Optional[int] = Field(
        default=None,
    )
    """Returns if a profile is hidden.."""

    last_name: typing.Optional[str] = Field(
        default=None,
    )
    """User last name."""

    can_access_closed: typing.Optional[bool] = Field(
        default=None,
    )
    """Property `UsersUserMin.can_access_closed`."""

    is_closed: typing.Optional[bool] = Field(
        default=None,
    )
    """Property `UsersUserMin.is_closed`."""


class UsersUserRelation(int, enum.Enum, metaclass=BaseEnumMeta):
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
    """
    Model: `UsersUserSettingsXtr`
    """

    home_town: str = Field()
    """User\'s hometown."""

    status: str = Field()
    """User status."""

    connections: typing.Optional["UsersUserConnections"] = Field(
        default=None,
    )
    """Property `UsersUserSettingsXtr.connections`."""

    bdate: typing.Optional[str] = Field(
        default=None,
    )
    """User\'s date of birth."""

    bdate_visibility: typing.Optional[int] = Field(
        default=None,
    )
    """Information whether user\'s birthdate are hidden."""

    city: typing.Optional["BaseCity"] = Field(
        default=None,
    )
    """Property `UsersUserSettingsXtr.city`."""

    first_name: typing.Optional[str] = Field(
        default=None,
    )
    """User first name."""

    last_name: typing.Optional[str] = Field(
        default=None,
    )
    """User last name."""

    maiden_name: typing.Optional[str] = Field(
        default=None,
    )
    """User maiden name."""

    name_request: typing.Optional["AccountNameRequest"] = Field(
        default=None,
    )
    """Property `UsersUserSettingsXtr.name_request`."""

    personal: typing.Optional["UsersPersonal"] = Field(
        default=None,
    )
    """Property `UsersUserSettingsXtr.personal`."""

    phone: typing.Optional[str] = Field(
        default=None,
    )
    """User phone number with some hidden digits."""

    relation: typing.Optional["UsersUserRelation"] = Field(
        default=None,
    )
    """User relationship status."""

    relation_partner: typing.Optional["UsersUserMin"] = Field(
        default=None,
    )
    """Property `UsersUserSettingsXtr.relation_partner`."""

    relation_pending: typing.Optional[bool] = Field(
        default=None,
    )
    """Information whether relation status is pending."""

    relation_requests: typing.Optional[typing.List["UsersUserMin"]] = Field(
        default=None,
    )
    """Property `UsersUserSettingsXtr.relation_requests`."""

    screen_name: typing.Optional[str] = Field(
        default=None,
    )
    """Domain name of the user\'s page."""

    sex: typing.Optional["BaseSex"] = Field(
        default=None,
    )
    """User sex."""

    status_audio: typing.Optional["AudioAudio"] = Field(
        default=None,
    )
    """Property `UsersUserSettingsXtr.status_audio`."""

    interests: typing.Optional["AccountUserSettingsInterests"] = Field(
        default=None,
    )
    """Property `UsersUserSettingsXtr.interests`."""

    languages: typing.Optional[typing.List[str]] = Field(
        default=None,
    )
    """Property `UsersUserSettingsXtr.languages`."""


class UsersUserType(str, enum.Enum, metaclass=BaseEnumMeta):
    PROFILE = "profile"


class UsersUsersArray(BaseModel):
    """
    Model: `UsersUsersArray`
    """

    count: int = Field()
    """Users number."""

    items: typing.List[int] = Field()
    """Property `UsersUsersArray.items`."""


class MessagesActionOneOf(BaseModel):
    """
    Model: `MessagesActionOneOf`
    """

    type: "MessagesMessageActionStatus" = Field()
    """Property `MessagesActionOneOf.type`."""

    conversation_message_id: typing.Optional[int] = Field(
        default=None,
    )
    """Message ID."""

    email: typing.Optional[str] = Field(
        default=None,
    )
    """Email address for chat_invite_user or chat_kick_user actions."""

    member_id: typing.Optional[int] = Field(
        default=None,
    )
    """User or email peer ID."""

    message: typing.Optional[str] = Field(
        default=None,
    )
    """Message body of related message."""

    photo: typing.Optional["MessagesMessageActionPhoto"] = Field(
        default=None,
    )
    """Property `MessagesActionOneOf.photo`."""

    text: typing.Optional[str] = Field(
        default=None,
    )
    """New chat title for chat_create and chat_title_update actions."""


class MessagesAudioMessage(BaseModel):
    """
    Model: `MessagesAudioMessage`
    """

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

    waveform: typing.List[int] = Field()
    """Property `MessagesAudioMessage.waveform`."""

    access_key: typing.Optional[str] = Field(
        default=None,
    )
    """Access key for audio message."""

    transcript_error: typing.Optional[int] = Field(
        default=None,
    )
    """Property `MessagesAudioMessage.transcript_error`."""


class MessagesBaseMessage(BaseModel):
    """
    Model: `MessagesBaseMessage`
    """

    conversation_message_id: int = Field()
    """Unique auto-incremented number for all messages with this peer."""

    date: int = Field()
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

    action: typing.Optional["MessagesActionOneOf"] = Field(
        default=None,
    )
    """Property `MessagesBaseMessage.action`."""

    admin_author_id: typing.Optional[int] = Field(
        default=None,
    )
    """Only for messages from community. Contains user ID of community admin, who sent this message.."""

    attachments: typing.Optional[typing.List["MessagesMessageAttachment"]] = Field(
        default=None,
    )
    """Property `MessagesBaseMessage.attachments`."""

    deleted: typing.Optional[bool] = Field(
        default=None,
    )
    """Is it an deleted message."""

    fwd_messages: typing.Optional["MessagesFwdMessages"] = Field(
        default=None,
    )
    """Property `MessagesBaseMessage.fwd_messages`."""

    geo: typing.Optional["BaseGeo"] = Field(
        default=None,
    )
    """Property `MessagesBaseMessage.geo`."""

    is_cropped: typing.Optional[bool] = Field(
        default=None,
    )
    """this message is cropped for bot."""

    keyboard: typing.Optional["MessagesKeyboard"] = Field(
        default=None,
    )
    """Property `MessagesBaseMessage.keyboard`."""

    payload: typing.Optional[str] = Field(
        default=None,
    )
    """Property `MessagesBaseMessage.payload`."""

    update_time: typing.Optional[int] = Field(
        default=None,
    )
    """Date when the message has been updated in Unixtime."""

    is_silent: typing.Optional[bool] = Field(
        default=None,
    )
    """Is silent message, push without sound."""

    is_unavailable: typing.Optional[bool] = Field(
        default=None,
    )
    """Is message unavailable for some reason, including its id equals 0."""

    random_id: typing.Optional[int] = Field(
        default=None,
    )
    """ID used for sending messages. It returned only for outgoing messages."""

    ref: typing.Optional[str] = Field(
        default=None,
    )
    """Property `MessagesBaseMessage.ref`."""

    ref_source: typing.Optional[str] = Field(
        default=None,
    )
    """Property `MessagesBaseMessage.ref_source`."""


class MessagesChat(BaseModel):
    """
    Model: `MessagesChat`
    """

    admin_id: int = Field()
    """Chat creator ID."""

    id: int = Field()
    """Chat ID."""

    type: str = Field()
    """Chat type."""

    users: typing.List[int] = Field()
    """Property `MessagesChat.users`."""

    members_count: int = Field()
    """Count members in a chat."""

    kicked: typing.Optional[bool] = Field(
        default=None,
    )
    """Shows that user has been kicked from the chat."""

    left: typing.Optional[bool] = Field(
        default=None,
    )
    """Shows that user has been left the chat."""

    photo_100: typing.Optional[str] = Field(
        default=None,
    )
    """URL of the preview image with 100 px in width."""

    photo_200: typing.Optional[str] = Field(
        default=None,
    )
    """URL of the preview image with 200 px in width."""

    photo_50: typing.Optional[str] = Field(
        default=None,
    )
    """URL of the preview image with 50 px in width."""

    push_settings: typing.Optional["MessagesChatPushSettings"] = Field(
        default=None,
    )
    """Property `MessagesChat.push_settings`."""

    title: typing.Optional[str] = Field(
        default=None,
    )
    """Chat title."""

    is_default_photo: typing.Optional[bool] = Field(
        default=None,
    )
    """If provided photo is default."""

    is_group_channel: typing.Optional[bool] = Field(
        default=None,
    )
    """If chat is group channel."""


class MessagesChatFull(BaseModel):
    """
    Model: `MessagesChatFull`
    """

    admin_id: int = Field()
    """Chat creator ID."""

    id: int = Field()
    """Chat ID."""

    type: str = Field()
    """Chat type."""

    users: typing.List["MessagesUserXtrInvitedBy"] = Field()
    """Property `MessagesChatFull.users`."""

    members_count: int = Field()
    """Count members in a chat."""

    kicked: typing.Optional[bool] = Field(
        default=None,
    )
    """Shows that user has been kicked from the chat."""

    left: typing.Optional[bool] = Field(
        default=None,
    )
    """Shows that user has been left the chat."""

    photo_100: typing.Optional[str] = Field(
        default=None,
    )
    """URL of the preview image with 100 px in width."""

    photo_200: typing.Optional[str] = Field(
        default=None,
    )
    """URL of the preview image with 200 px in width."""

    photo_50: typing.Optional[str] = Field(
        default=None,
    )
    """URL of the preview image with 50 px in width."""

    push_settings: typing.Optional["MessagesChatPushSettings"] = Field(
        default=None,
    )
    """Property `MessagesChatFull.push_settings`."""

    title: typing.Optional[str] = Field(
        default=None,
    )
    """Chat title."""

    is_default_photo: typing.Optional[bool] = Field(
        default=None,
    )
    """If provided photo is default."""

    is_group_channel: typing.Optional[bool] = Field(
        default=None,
    )
    """If chat is group channel."""


class MessagesChatPreview(BaseModel):
    """
    Model: `MessagesChatPreview`
    """

    admin_id: int = Field()
    """Property `MessagesChatPreview.admin_id`."""

    members: typing.List[int] = Field()
    """Property `MessagesChatPreview.members`."""

    title: str = Field()
    """Property `MessagesChatPreview.title`."""

    joined: typing.Optional[bool] = Field(
        default=None,
    )
    """Property `MessagesChatPreview.joined`."""

    local_id: typing.Optional[int] = Field(
        default=None,
    )
    """Property `MessagesChatPreview.local_id`."""

    members_count: typing.Optional[int] = Field(
        default=None,
    )
    """Property `MessagesChatPreview.members_count`."""

    is_member: typing.Optional[bool] = Field(
        default=None,
    )
    """Property `MessagesChatPreview.is_member`."""

    photo: typing.Optional["MessagesChatSettingsPhoto"] = Field(
        default=None,
    )
    """Property `MessagesChatPreview.photo`."""

    is_don: typing.Optional[bool] = Field(
        default=None,
    )
    """Property `MessagesChatPreview.is_don`."""

    is_nft: typing.Optional[bool] = Field(
        default=None,
    )
    """Property `MessagesChatPreview.is_nft`."""

    is_group_channel: typing.Optional[bool] = Field(
        default=None,
    )
    """Property `MessagesChatPreview.is_group_channel`."""

    button: typing.Optional["BaseLinkButton"] = Field(
        default=None,
    )
    """Property `MessagesChatPreview.button`."""


class MessagesChatPushSettings(BaseModel):
    """
    Model: `MessagesChatPushSettings`
    """

    disabled_until: typing.Optional[int] = Field(
        default=None,
    )
    """Time until that notifications are disabled."""

    sound: typing.Optional[bool] = Field(
        default=None,
    )
    """Information whether the sound is on."""


class MessagesChatRestrictions(BaseModel):
    """
    Model: `MessagesChatRestrictions`
    """

    admins_promote_users: typing.Optional[bool] = Field(
        default=None,
    )
    """Only admins can promote users to admins."""

    only_admins_edit_info: typing.Optional[bool] = Field(
        default=None,
    )
    """Only admins can change chat info."""

    only_admins_edit_pin: typing.Optional[bool] = Field(
        default=None,
    )
    """Only admins can edit pinned message."""

    only_admins_invite: typing.Optional[bool] = Field(
        default=None,
    )
    """Only admins can invite users to this chat."""

    only_admins_kick: typing.Optional[bool] = Field(
        default=None,
    )
    """Only admins can kick users from this chat."""


class MessagesChatSettings(BaseModel):
    """
    Model: `MessagesChatSettings`
    """

    owner_id: int = Field()
    """Property `MessagesChatSettings.owner_id`."""

    title: str = Field()
    """Chat title."""

    state: "MessagesChatSettingsState" = Field()
    """Property `MessagesChatSettings.state`."""

    acl: "MessagesChatSettingsAcl" = Field()
    """Property `MessagesChatSettings.acl`."""

    members_count: typing.Optional[int] = Field(
        default=None,
    )
    """Property `MessagesChatSettings.members_count`."""

    friends_count: typing.Optional[int] = Field(
        default=None,
    )
    """Property `MessagesChatSettings.friends_count`."""

    pinned_messages_count: typing.Optional[int] = Field(
        default=None,
    )
    """Property `MessagesChatSettings.pinned_messages_count`."""

    pinned_message: typing.Optional["MessagesPinnedMessage"] = Field(
        default=None,
    )
    """Property `MessagesChatSettings.pinned_message`."""

    photo: typing.Optional["MessagesChatSettingsPhoto"] = Field(
        default=None,
    )
    """Property `MessagesChatSettings.photo`."""

    admin_ids: typing.Optional[typing.List[int]] = Field(
        default=None,
    )
    """Ids of chat admins."""

    active_ids: typing.Optional[typing.List[int]] = Field(
        default=None,
    )
    """Property `MessagesChatSettings.active_ids`."""

    is_group_channel: typing.Optional[bool] = Field(
        default=None,
    )
    """Property `MessagesChatSettings.is_group_channel`."""

    permissions: typing.Optional["MessagesChatSettingsPermissions"] = Field(
        default=None,
    )
    """Property `MessagesChatSettings.permissions`."""

    is_disappearing: typing.Optional[bool] = Field(
        default=None,
    )
    """Property `MessagesChatSettings.is_disappearing`."""

    theme: typing.Optional[str] = Field(
        default=None,
    )
    """Property `MessagesChatSettings.theme`."""

    disappearing_chat_link: typing.Optional[str] = Field(
        default=None,
    )
    """Property `MessagesChatSettings.disappearing_chat_link`."""

    is_service: typing.Optional[bool] = Field(
        default=None,
    )
    """Property `MessagesChatSettings.is_service`."""


class MessagesChatSettingsAcl(BaseModel):
    """
    Model: `MessagesChatSettingsAcl`
    """

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

    can_change_service_type: typing.Optional[bool] = Field(
        default=None,
    )
    """Can you change chat service type."""


class MessagesChatSettingsPermissionsInvite(str, enum.Enum, metaclass=BaseEnumMeta):
    OWNER = "owner"
    OWNER_AND_ADMINS = "owner_and_admins"
    ALL = "all"


class MessagesChatSettingsPermissionsChangeInfo(str, enum.Enum, metaclass=BaseEnumMeta):
    OWNER = "owner"
    OWNER_AND_ADMINS = "owner_and_admins"
    ALL = "all"


class MessagesChatSettingsPermissionsChangePin(str, enum.Enum, metaclass=BaseEnumMeta):
    OWNER = "owner"
    OWNER_AND_ADMINS = "owner_and_admins"
    ALL = "all"


class MessagesChatSettingsPermissionsUseMassMentions(str, enum.Enum, metaclass=BaseEnumMeta):
    OWNER = "owner"
    OWNER_AND_ADMINS = "owner_and_admins"
    ALL = "all"


class MessagesChatSettingsPermissionsSeeInviteLink(str, enum.Enum, metaclass=BaseEnumMeta):
    OWNER = "owner"
    OWNER_AND_ADMINS = "owner_and_admins"
    ALL = "all"


class MessagesChatSettingsPermissionsCall(str, enum.Enum, metaclass=BaseEnumMeta):
    OWNER = "owner"
    OWNER_AND_ADMINS = "owner_and_admins"
    ALL = "all"


class MessagesChatSettingsPermissionsChangeAdmins(str, enum.Enum, metaclass=BaseEnumMeta):
    OWNER = "owner"
    OWNER_AND_ADMINS = "owner_and_admins"


class MessagesChatSettingsPermissions(BaseModel):
    """
    Model: `MessagesChatSettingsPermissions`
    """

    invite: typing.Optional["MessagesChatSettingsPermissionsInvite"] = Field(
        default=None,
    )
    """Who can invite users to chat."""

    change_info: typing.Optional["MessagesChatSettingsPermissionsChangeInfo"] = Field(
        default=None,
    )
    """Who can change chat info."""

    change_pin: typing.Optional["MessagesChatSettingsPermissionsChangePin"] = Field(
        default=None,
    )
    """Who can change pinned message."""

    use_mass_mentions: typing.Optional["MessagesChatSettingsPermissionsUseMassMentions"] = Field(
        default=None,
    )
    """Who can use mass mentions."""

    see_invite_link: typing.Optional["MessagesChatSettingsPermissionsSeeInviteLink"] = Field(
        default=None,
    )
    """Who can see invite link."""

    call: typing.Optional["MessagesChatSettingsPermissionsCall"] = Field(
        default=None,
    )
    """Who can make calls."""

    change_admins: typing.Optional["MessagesChatSettingsPermissionsChangeAdmins"] = Field(
        default=None,
    )
    """Who can change admins."""


class MessagesChatSettingsPhoto(BaseModel):
    """
    Model: `MessagesChatSettingsPhoto`
    """

    photo_50: typing.Optional[str] = Field(
        default=None,
    )
    """URL of the preview image with 50px in width."""

    photo_100: typing.Optional[str] = Field(
        default=None,
    )
    """URL of the preview image with 100px in width."""

    photo_200: typing.Optional[str] = Field(
        default=None,
    )
    """URL of the preview image with 200px in width."""

    is_default_photo: typing.Optional[bool] = Field(
        default=None,
    )
    """If provided photo is default."""

    is_default_call_photo: typing.Optional[bool] = Field(
        default=None,
    )
    """If provided photo is default call photo."""


class MessagesChatSettingsState(str, enum.Enum, metaclass=BaseEnumMeta):
    IN = "in"
    KICKED = "kicked"
    LEFT = "left"
    OUT = "out"


class MessagesConversationSpecialServiceType(str, enum.Enum, metaclass=BaseEnumMeta):
    BUSINESS_NOTIFY = "business_notify"


class MessagesConversation(BaseModel):
    """
    Model: `MessagesConversation`
    """

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

    sort_id: typing.Optional["MessagesConversationSortId"] = Field(
        default=None,
    )
    """Property `MessagesConversation.sort_id`."""

    unread_count: typing.Optional[int] = Field(
        default=None,
    )
    """Unread messages number."""

    is_marked_unread: typing.Optional[bool] = Field(
        default=None,
    )
    """Is this conversation unread."""

    out_read_by: typing.Optional["MessagesOutReadBy"] = Field(
        default=None,
    )
    """Property `MessagesConversation.out_read_by`."""

    important: typing.Optional[bool] = Field(
        default=None,
    )
    """Property `MessagesConversation.important`."""

    unanswered: typing.Optional[bool] = Field(
        default=None,
    )
    """Property `MessagesConversation.unanswered`."""

    special_service_type: typing.Optional["MessagesConversationSpecialServiceType"] = Field(
        default=None,
    )
    """Property `MessagesConversation.special_service_type`."""

    message_request_data: typing.Optional["MessagesMessageRequestData"] = Field(
        default=None,
    )
    """Property `MessagesConversation.message_request_data`."""

    mentions: typing.Optional[typing.List[int]] = Field(
        default=None,
    )
    """Ids of messages with mentions."""

    current_keyboard: typing.Optional["MessagesKeyboard"] = Field(
        default=None,
    )
    """Property `MessagesConversation.current_keyboard`."""

    push_settings: typing.Optional["MessagesPushSettings"] = Field(
        default=None,
    )
    """Property `MessagesConversation.push_settings`."""

    can_write: typing.Optional["MessagesConversationCanWrite"] = Field(
        default=None,
    )
    """Property `MessagesConversation.can_write`."""

    chat_settings: typing.Optional["MessagesChatSettings"] = Field(
        default=None,
    )
    """Property `MessagesConversation.chat_settings`."""


class MessagesConversationCanWrite(BaseModel):
    """
    Model: `MessagesConversationCanWrite`
    """

    allowed: bool = Field()
    """Property `MessagesConversationCanWrite.allowed`."""

    reason: typing.Optional[int] = Field(
        default=None,
    )
    """Property `MessagesConversationCanWrite.reason`."""

    until: typing.Optional[int] = Field(
        default=None,
    )
    """Property `MessagesConversationCanWrite.until`."""


class MessagesConversationMember(BaseModel):
    """
    Model: `MessagesConversationMember`
    """

    member_id: int = Field()
    """Property `MessagesConversationMember.member_id`."""

    can_kick: typing.Optional[bool] = Field(
        default=None,
    )
    """Is it possible for user to kick this member."""

    is_restricted_to_write: typing.Optional[bool] = Field(
        default=None,
    )
    """Does this member have write permission."""

    invited_by: typing.Optional[int] = Field(
        default=None,
    )
    """Property `MessagesConversationMember.invited_by`."""

    is_admin: typing.Optional[bool] = Field(
        default=None,
    )
    """Property `MessagesConversationMember.is_admin`."""

    is_owner: typing.Optional[bool] = Field(
        default=None,
    )
    """Property `MessagesConversationMember.is_owner`."""

    is_message_request: typing.Optional[bool] = Field(
        default=None,
    )
    """Property `MessagesConversationMember.is_message_request`."""

    join_date: typing.Optional[int] = Field(
        default=None,
    )
    """Property `MessagesConversationMember.join_date`."""

    request_date: typing.Optional[int] = Field(
        default=None,
    )
    """Message request date."""


class MessagesConversationPeer(BaseModel):
    """
    Model: `MessagesConversationPeer`
    """

    id: int = Field()
    """Property `MessagesConversationPeer.id`."""

    type: "MessagesConversationPeerType" = Field()
    """Property `MessagesConversationPeer.type`."""

    local_id: typing.Optional[int] = Field(
        default=None,
    )
    """Property `MessagesConversationPeer.local_id`."""


class MessagesConversationPeerType(str, enum.Enum, metaclass=BaseEnumMeta):
    CHAT = "chat"
    EMAIL = "email"
    USER = "user"
    GROUP = "group"


class MessagesConversationSortId(BaseModel):
    """
    Model: `MessagesConversationSortId`
    """

    major_id: int = Field()
    """Major id for sorting conversations."""

    minor_id: int = Field()
    """Minor id for sorting conversations."""


class MessagesConversationWithMessage(BaseModel):
    """
    Model: `MessagesConversationWithMessage`
    """

    conversation: "MessagesConversation" = Field()
    """Property `MessagesConversationWithMessage.conversation`."""

    last_message: typing.Optional["MessagesMessage"] = Field(
        default=None,
    )
    """Property `MessagesConversationWithMessage.last_message`."""


class MessagesDeleteFullResponseItem(BaseModel):
    """
    Model: `MessagesDeleteFullResponseItem`
    """

    peer_id: typing.Optional[int] = Field(
        default=None,
    )
    """Property `MessagesDeleteFullResponseItem.peer_id`."""

    message_id: typing.Optional[int] = Field(
        default=None,
    )
    """Property `MessagesDeleteFullResponseItem.message_id`."""

    conversation_message_id: typing.Optional[int] = Field(
        default=None,
    )
    """Property `MessagesDeleteFullResponseItem.conversation_message_id`."""

    response: typing.Optional[bool] = Field(
        default=None,
    )
    """Property `MessagesDeleteFullResponseItem.response`."""

    error: typing.Optional["BaseMessageError"] = Field(
        default=None,
    )
    """Property `MessagesDeleteFullResponseItem.error`."""


class MessagesForeignMessage(BaseModel):
    """
    Model: `MessagesForeignMessage`
    """

    conversation_message_id: int = Field()
    """Conversation message ID."""

    date: int = Field()
    """Date when the message was created."""

    from_id: int = Field()
    """Message author\'s ID."""

    text: str = Field()
    """Message text."""

    attachments: typing.Optional[typing.List["MessagesMessageAttachment"]] = Field(
        default=None,
    )
    """Property `MessagesForeignMessage.attachments`."""

    fwd_messages: typing.Optional[typing.List["MessagesForeignMessage"]] = Field(
        default=None,
    )
    """Property `MessagesForeignMessage.fwd_messages`."""

    geo: typing.Optional["BaseGeo"] = Field(
        default=None,
    )
    """Property `MessagesForeignMessage.geo`."""

    id: typing.Optional[int] = Field(
        default=None,
    )
    """Message ID."""

    peer_id: typing.Optional[int] = Field(
        default=None,
    )
    """Peer ID."""

    reply_message: typing.Optional["MessagesForeignMessage"] = Field(
        default=None,
    )
    """Property `MessagesForeignMessage.reply_message`."""

    update_time: typing.Optional[int] = Field(
        default=None,
    )
    """Date when the message has been updated in Unixtime."""

    was_listened: typing.Optional[bool] = Field(
        default=None,
    )
    """Was the audio message inside already listened by you."""

    payload: typing.Optional[str] = Field(
        default=None,
    )
    """Additional data sent along with message for developer convenience."""


class MessagesForward(BaseModel):
    """
    Model: `MessagesForward`
    """

    owner_id: typing.Optional[int] = Field(
        default=None,
    )
    """Messages owner_id."""

    peer_id: typing.Optional[int] = Field(
        default=None,
    )
    """Messages peer_id."""

    conversation_message_ids: typing.Optional[typing.List[int]] = Field(
        default=None,
    )
    """Property `MessagesForward.conversation_message_ids`."""

    cmids: typing.Optional[typing.List[int]] = Field(
        default=None,
    )
    """Property `MessagesForward.cmids`."""

    message_ids: typing.Optional[typing.List[int]] = Field(
        default=None,
    )
    """Property `MessagesForward.message_ids`."""

    is_reply: typing.Optional[bool] = Field(
        default=None,
    )
    """If you need to reply to a message."""


MessagesFwdMessages: typing.TypeAlias = typing.List[typing.List[MessagesForeignMessage]]


class MessagesGetConversationById(BaseModel):
    """
    Model: `MessagesGetConversationById`
    """

    count: int = Field()
    """Total number."""

    items: typing.List["MessagesConversation"] = Field()
    """Property `MessagesGetConversationById.items`."""


class MessagesGetConversationMembers(BaseModel):
    """
    Model: `MessagesGetConversationMembers`
    """

    items: typing.List["MessagesConversationMember"] = Field()
    """Property `MessagesGetConversationMembers.items`."""

    count: int = Field()
    """Chat members count."""

    chat_restrictions: typing.Optional["MessagesChatRestrictions"] = Field(
        default=None,
    )
    """Property `MessagesGetConversationMembers.chat_restrictions`."""

    profiles: typing.Optional[typing.List["UsersUserFull"]] = Field(
        default=None,
    )
    """Property `MessagesGetConversationMembers.profiles`."""

    groups: typing.Optional[typing.List["GroupsGroupFull"]] = Field(
        default=None,
    )
    """Property `MessagesGetConversationMembers.groups`."""


class MessagesGetInviteLinkByOwnerResponseItem(BaseModel):
    """
    Model: `MessagesGetInviteLinkByOwnerResponseItem`
    """

    owner_id: int = Field()
    """Property `MessagesGetInviteLinkByOwnerResponseItem.owner_id`."""

    link: typing.Optional[str] = Field(
        default=None,
    )
    """Property `MessagesGetInviteLinkByOwnerResponseItem.link`."""

    error: typing.Optional["BaseMessageError"] = Field(
        default=None,
    )
    """Property `MessagesGetInviteLinkByOwnerResponseItem.error`."""


class MessagesGraffiti(BaseModel):
    """
    Model: `MessagesGraffiti`
    """

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

    access_key: typing.Optional[str] = Field(
        default=None,
    )
    """Access key for graffiti."""


class MessagesHistoryAttachment(BaseModel):
    """
    Model: `MessagesHistoryAttachment`
    """

    attachment: "MessagesHistoryMessageAttachment" = Field()
    """Property `MessagesHistoryAttachment.attachment`."""

    date: int = Field()
    """Message sending time."""

    message_id: int = Field()
    """Message ID."""

    cmid: int = Field()
    """Conversation Message ID."""

    from_id: int = Field()
    """Message author\'s ID."""

    message_expire_ttl: typing.Optional[int] = Field(
        default=None,
    )
    """Message Exipire ttl."""

    forward_level: typing.Optional[int] = Field(
        default=None,
    )
    """Forward level (optional)."""

    was_listened: typing.Optional[bool] = Field(
        default=None,
    )
    """Property `MessagesHistoryAttachment.was_listened`."""

    position: typing.Optional[int] = Field(
        default=None,
    )
    """Attachment position in the Message."""


class MessagesHistoryMessageAttachment(BaseModel):
    """
    Model: `MessagesHistoryMessageAttachment`
    """

    type: "MessagesHistoryMessageAttachmentType" = Field()
    """Property `MessagesHistoryMessageAttachment.type`."""

    audio: typing.Optional["AudioAudio"] = Field(
        default=None,
    )
    """Property `MessagesHistoryMessageAttachment.audio`."""

    audio_message: typing.Optional["MessagesAudioMessage"] = Field(
        default=None,
    )
    """Property `MessagesHistoryMessageAttachment.audio_message`."""

    doc: typing.Optional["DocsDoc"] = Field(
        default=None,
    )
    """Property `MessagesHistoryMessageAttachment.doc`."""

    graffiti: typing.Optional["MessagesGraffiti"] = Field(
        default=None,
    )
    """Property `MessagesHistoryMessageAttachment.graffiti`."""

    market: typing.Optional["MarketMarketItem"] = Field(
        default=None,
    )
    """Property `MessagesHistoryMessageAttachment.market`."""

    photo: typing.Optional["PhotosPhoto"] = Field(
        default=None,
    )
    """Property `MessagesHistoryMessageAttachment.photo`."""


class MessagesHistoryMessageAttachmentType(str, enum.Enum, metaclass=BaseEnumMeta):
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
    """
    Model: `MessagesKeyboard`
    """

    one_time: bool = Field()
    """Should this keyboard disappear on first use."""

    buttons: typing.List[typing.List["MessagesKeyboardButton"]] = Field()
    """Property `MessagesKeyboard.buttons`."""

    author_id: typing.Optional[int] = Field(
        default=None,
    )
    """Community or bot, which set this keyboard."""

    inline: typing.Optional[bool] = Field(
        default=None,
    )
    """Property `MessagesKeyboard.inline`."""


class MessagesKeyboardButtonColor(str, enum.Enum, metaclass=BaseEnumMeta):
    DEFAULT = "default"
    POSITIVE = "positive"
    NEGATIVE = "negative"
    PRIMARY = "primary"


class MessagesKeyboardButton(BaseModel):
    """
    Model: `MessagesKeyboardButton`
    """

    action: "MessagesKeyboardButtonPropertyAction" = Field()
    """Property `MessagesKeyboardButton.action`."""

    color: typing.Optional["MessagesKeyboardButtonColor"] = Field(
        default=None,
    )
    """Button color."""


class MessagesKeyboardButtonActionCallbackType(str, enum.Enum, metaclass=BaseEnumMeta):
    CALLBACK = "callback"


class MessagesKeyboardButtonActionCallback(BaseModel):
    """
    Description of the action, that should be performed on button click
    Model: `MessagesKeyboardButtonActionCallback`
    """

    label: str = Field()
    """Label for button."""

    type: "MessagesKeyboardButtonActionCallbackType" = Field()
    """Property `MessagesKeyboardButtonActionCallback.type`."""

    payload: typing.Optional[str] = Field(
        default=None,
    )
    """Additional data sent along with message for developer convenience."""


class MessagesKeyboardButtonActionLocationType(str, enum.Enum, metaclass=BaseEnumMeta):
    LOCATION = "location"


class MessagesKeyboardButtonActionLocation(BaseModel):
    """
    Description of the action, that should be performed on button click
    Model: `MessagesKeyboardButtonActionLocation`
    """

    type: "MessagesKeyboardButtonActionLocationType" = Field()
    """Property `MessagesKeyboardButtonActionLocation.type`."""

    payload: typing.Optional[str] = Field(
        default=None,
    )
    """Additional data sent along with message for developer convenience."""


class MessagesKeyboardButtonActionOpenAppType(str, enum.Enum, metaclass=BaseEnumMeta):
    OPEN_APP = "open_app"


class MessagesKeyboardButtonActionOpenApp(BaseModel):
    """
    Description of the action, that should be performed on button click
    Model: `MessagesKeyboardButtonActionOpenApp`
    """

    app_id: int = Field()
    """Fragment value in app link like vk.ru/app{app_id}_-654321#hash."""

    label: str = Field()
    """Label for button."""

    owner_id: int = Field()
    """Fragment value in app link like vk.ru/app123456_{owner_id}#hash."""

    type: "MessagesKeyboardButtonActionOpenAppType" = Field()
    """Property `MessagesKeyboardButtonActionOpenApp.type`."""

    hash: typing.Optional[str] = Field(
        default=None,
    )
    """Fragment value in app link like vk.ru/app123456_-654321#{hash}."""

    payload: typing.Optional[str] = Field(
        default=None,
    )
    """Additional data sent along with message for developer convenience."""


class MessagesKeyboardButtonActionOpenLinkType(str, enum.Enum, metaclass=BaseEnumMeta):
    OPEN_LINK = "open_link"


class MessagesKeyboardButtonActionOpenLink(BaseModel):
    """
    Description of the action, that should be performed on button click
    Model: `MessagesKeyboardButtonActionOpenLink`
    """

    label: str = Field()
    """Label for button."""

    link: str = Field()
    """link for button."""

    type: "MessagesKeyboardButtonActionOpenLinkType" = Field()
    """Property `MessagesKeyboardButtonActionOpenLink.type`."""

    payload: typing.Optional[str] = Field(
        default=None,
    )
    """Additional data sent along with message for developer convenience."""


class MessagesKeyboardButtonActionOpenPhotoType(str, enum.Enum, metaclass=BaseEnumMeta):
    OPEN_PHOTO = "open_photo"


class MessagesKeyboardButtonActionOpenPhoto(BaseModel):
    """
    Description of the action, that should be performed on button click
    Model: `MessagesKeyboardButtonActionOpenPhoto`
    """

    type: "MessagesKeyboardButtonActionOpenPhotoType" = Field()
    """Property `MessagesKeyboardButtonActionOpenPhoto.type`."""


class MessagesKeyboardButtonActionTextType(str, enum.Enum, metaclass=BaseEnumMeta):
    TEXT = "text"


class MessagesKeyboardButtonActionText(BaseModel):
    """
    Description of the action, that should be performed on button click
    Model: `MessagesKeyboardButtonActionText`
    """

    label: str = Field()
    """Label for button."""

    type: "MessagesKeyboardButtonActionTextType" = Field()
    """Property `MessagesKeyboardButtonActionText.type`."""

    payload: typing.Optional[str] = Field(
        default=None,
    )
    """Additional data sent along with message for developer convenience."""


class MessagesKeyboardButtonActionVkpayType(str, enum.Enum, metaclass=BaseEnumMeta):
    VKPAY = "vkpay"


class MessagesKeyboardButtonActionVkpay(BaseModel):
    """
    Description of the action, that should be performed on button click
    Model: `MessagesKeyboardButtonActionVkpay`
    """

    hash: str = Field()
    """Fragment value in app link like vk.ru/app123456_-654321#{hash}."""

    type: "MessagesKeyboardButtonActionVkpayType" = Field()
    """Property `MessagesKeyboardButtonActionVkpay.type`."""

    payload: typing.Optional[str] = Field(
        default=None,
    )
    """Additional data sent along with message for developer convenience."""


class MessagesKeyboardButtonPropertyAction(BaseModel):
    """
    Model: `MessagesKeyboardButtonPropertyAction`
    """


class MessagesLastActivity(BaseModel):
    """
    Model: `MessagesLastActivity`
    """

    online: bool = Field()
    """Information whether user is online."""

    time: int = Field()
    """Time when user was online in Unixtime."""


class MessagesLongpollMessages(BaseModel):
    """
    Model: `MessagesLongpollMessages`
    """


class MessagesLongpollParams(BaseModel):
    """
    Model: `MessagesLongpollParams`
    """

    server: str = Field()
    """Server URL."""

    key: str = Field()
    """Key."""

    ts: int = Field()
    """Timestamp."""

    pts: typing.Optional[int] = Field(
        default=None,
    )
    """Persistent timestamp."""


class MessagesMessageAction(BaseModel):
    """
    Model: `MessagesMessageAction`
    """

    type: "MessagesMessageActionStatus" = Field()
    """Property `MessagesMessageAction.type`."""

    conversation_message_id: typing.Optional[int] = Field(
        default=None,
    )
    """Message ID."""

    email: typing.Optional[str] = Field(
        default=None,
    )
    """Email address for chat_invite_user or chat_kick_user actions."""

    member_id: typing.Optional[int] = Field(
        default=None,
    )
    """User or email peer ID."""

    message: typing.Optional[str] = Field(
        default=None,
    )
    """Message body of related message."""

    photo: typing.Optional["MessagesMessageActionPhoto"] = Field(
        default=None,
    )
    """Property `MessagesMessageAction.photo`."""

    text: typing.Optional[str] = Field(
        default=None,
    )
    """New chat title for chat_create and chat_title_update actions."""


class MessagesMessageActionPhoto(BaseModel):
    """
    Model: `MessagesMessageActionPhoto`
    """

    photo_50: str = Field()
    """URL of the preview image with 50px in width."""

    photo_100: str = Field()
    """URL of the preview image with 100px in width."""

    photo_200: str = Field()
    """URL of the preview image with 200px in width."""


class MessagesMessageActionStatus(str, enum.Enum, metaclass=BaseEnumMeta):
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
    """
    Model: `MessagesMessageAttachment`
    """

    type: "MessagesMessageAttachmentType" = Field()
    """Property `MessagesMessageAttachment.type`."""

    audio: typing.Optional["AudioAudio"] = Field(
        default=None,
    )
    """Property `MessagesMessageAttachment.audio`."""

    audio_message: typing.Optional["MessagesAudioMessage"] = Field(
        default=None,
    )
    """Property `MessagesMessageAttachment.audio_message`."""

    call: typing.Optional["CallsCall"] = Field(
        default=None,
    )
    """Property `MessagesMessageAttachment.call`."""

    doc: typing.Optional["DocsDoc"] = Field(
        default=None,
    )
    """Property `MessagesMessageAttachment.doc`."""

    gift: typing.Optional["GiftsLayout"] = Field(
        default=None,
    )
    """Property `MessagesMessageAttachment.gift`."""

    graffiti: typing.Optional["MessagesGraffiti"] = Field(
        default=None,
    )
    """Property `MessagesMessageAttachment.graffiti`."""

    market: typing.Optional["MarketMarketItem"] = Field(
        default=None,
    )
    """Property `MessagesMessageAttachment.market`."""

    market_market_album: typing.Optional["MarketMarketAlbum"] = Field(
        default=None,
    )
    """Property `MessagesMessageAttachment.market_market_album`."""

    photo: typing.Optional["PhotosPhoto"] = Field(
        default=None,
    )
    """Property `MessagesMessageAttachment.photo`."""

    sticker: typing.Optional["BaseSticker"] = Field(
        default=None,
    )
    """Property `MessagesMessageAttachment.sticker`."""

    story: typing.Optional["StoriesStory"] = Field(
        default=None,
    )
    """Property `MessagesMessageAttachment.story`."""

    wall_reply: typing.Optional["WallWallComment"] = Field(
        default=None,
    )
    """Property `MessagesMessageAttachment.wall_reply`."""

    poll: typing.Optional["PollsPoll"] = Field(
        default=None,
    )
    """Property `MessagesMessageAttachment.poll`."""


class MessagesMessageAttachmentType(str, enum.Enum, metaclass=BaseEnumMeta):
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
    """
    Model: `MessagesMessageRequestData`
    """

    status: typing.Optional[str] = Field(
        default=None,
    )
    """Status of message request."""

    inviter_id: typing.Optional[int] = Field(
        default=None,
    )
    """Message request sender id."""

    request_date: typing.Optional[int] = Field(
        default=None,
    )
    """Message request date."""


class MessagesMessagesArray(BaseModel):
    """
    Model: `MessagesMessagesArray`
    """

    count: typing.Optional[int] = Field(
        default=None,
    )
    """Property `MessagesMessagesArray.count`."""

    items: typing.Optional[typing.List["MessagesMessage"]] = Field(
        default=None,
    )
    """Property `MessagesMessagesArray.items`."""


class MessagesOutReadBy(BaseModel):
    """
    Model: `MessagesOutReadBy`
    """

    count: typing.Optional[int] = Field(
        default=None,
    )
    """Property `MessagesOutReadBy.count`."""

    member_ids: typing.Optional[typing.List[int]] = Field(
        default=None,
    )
    """Property `MessagesOutReadBy.member_ids`."""


class MessagesPinnedMessage(BaseModel):
    """
    Model: `MessagesPinnedMessage`
    """

    conversation_message_id: int = Field()
    """Unique auto-incremented number for all messages with this peer."""

    id: int = Field()
    """Message ID."""

    date: int = Field()
    """Date when the message has been sent in Unixtime."""

    from_id: int = Field()
    """Message author\'s ID."""

    peer_id: int = Field()
    """Peer ID."""

    text: str = Field()
    """Message text."""

    attachments: typing.Optional[typing.List["MessagesMessageAttachment"]] = Field(
        default=None,
    )
    """Property `MessagesPinnedMessage.attachments`."""

    fwd_messages: typing.Optional[typing.List["MessagesForeignMessage"]] = Field(
        default=None,
    )
    """Forwarded messages."""

    geo: typing.Optional["BaseGeo"] = Field(
        default=None,
    )
    """Property `MessagesPinnedMessage.geo`."""

    reply_message: typing.Optional["MessagesForeignMessage"] = Field(
        default=None,
    )
    """Property `MessagesPinnedMessage.reply_message`."""

    keyboard: typing.Optional["MessagesKeyboard"] = Field(
        default=None,
    )
    """Property `MessagesPinnedMessage.keyboard`."""

    out: typing.Optional[bool] = Field(
        default=None,
    )
    """Information whether the message is outcoming."""

    important: typing.Optional[bool] = Field(
        default=None,
    )
    """Is it an important message."""


class MessagesPushSettings(BaseModel):
    """
    Model: `MessagesPushSettings`
    """

    disabled_forever: bool = Field()
    """Information whether push notifications are disabled forever."""

    no_sound: bool = Field()
    """Information whether the sound is on."""

    disabled_until: typing.Optional[int] = Field(
        default=None,
    )
    """Time until what notifications are disabled."""

    disabled_mentions: typing.Optional[bool] = Field(
        default=None,
    )
    """Information whether the mentions are disabled."""

    disabled_mass_mentions: typing.Optional[bool] = Field(
        default=None,
    )
    """Information whether the mass mentions (like \'@all\', \'@online\') are disabled."""


class MessagesReactionAssetItem(BaseModel):
    """
    Model: `MessagesReactionAssetItem`
    """

    reaction_id: int = Field()
    """Property `MessagesReactionAssetItem.reaction_id`."""

    links: "MessagesReactionAssetItemLinks" = Field()
    """Liks to reactions assets for each asset type."""


class MessagesReactionAssetItemLinks(BaseModel):
    """
    Model: `MessagesReactionAssetItemLinks`
    """

    big_animation: str = Field()
    """Big reaction animation json file."""

    small_animation: str = Field()
    """Small reaction animation json file."""

    static: str = Field()
    """Reaction image file."""


class MessagesReactionCounterResponseItem(BaseModel):
    """
    Model: `MessagesReactionCounterResponseItem`
    """

    reaction_id: int = Field()
    """Property `MessagesReactionCounterResponseItem.reaction_id`."""

    count: int = Field()
    """Property `MessagesReactionCounterResponseItem.count`."""

    user_ids: typing.List[int] = Field()
    """Property `MessagesReactionCounterResponseItem.user_ids`."""


class MessagesReactionCountersResponseItem(BaseModel):
    """
    Model: `MessagesReactionCountersResponseItem`
    """

    cmid: int = Field()
    """Property `MessagesReactionCountersResponseItem.cmid`."""

    counters: typing.List["MessagesReactionCounterResponseItem"] = Field()
    """Property `MessagesReactionCountersResponseItem.counters`."""


class MessagesReactionResponseItem(BaseModel):
    """
    Model: `MessagesReactionResponseItem`
    """

    user_id: int = Field()
    """Property `MessagesReactionResponseItem.user_id`."""

    reaction_id: int = Field()
    """Property `MessagesReactionResponseItem.reaction_id`."""


class MessagesSendUserIdsResponseItem(BaseModel):
    """
    Model: `MessagesSendUserIdsResponseItem`
    """

    peer_id: int = Field()
    """Property `MessagesSendUserIdsResponseItem.peer_id`."""

    message_id: int = Field()
    """Property `MessagesSendUserIdsResponseItem.message_id`."""

    conversation_message_id: int = Field()
    """Property `MessagesSendUserIdsResponseItem.conversation_message_id`."""

    error: typing.Optional["BaseMessageError"] = Field(
        default=None,
    )
    """Property `MessagesSendUserIdsResponseItem.error`."""


class MessagesTemplateActionTypeNames(str, enum.Enum, metaclass=BaseEnumMeta):
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


class MessagesUserTypeForXtrInvitedBy(str, enum.Enum, metaclass=BaseEnumMeta):
    PROFILE = "profile"
    GROUP = "group"


class AccountAccountCounters(BaseModel):
    """
    Model: `AccountAccountCounters`
    """

    app_requests: typing.Optional[int] = Field(
        default=None,
    )
    """New app requests number."""

    events: typing.Optional[int] = Field(
        default=None,
    )
    """New events number."""

    faves: typing.Optional[int] = Field(
        default=None,
    )
    """New faves number."""

    friends: typing.Optional[int] = Field(
        default=None,
    )
    """New friends requests number."""

    friends_recommendations: typing.Optional[int] = Field(
        default=None,
    )
    """New friends recommendations number."""

    gifts: typing.Optional[int] = Field(
        default=None,
    )
    """New gifts number."""

    groups: typing.Optional[int] = Field(
        default=None,
    )
    """New groups number."""

    messages: typing.Optional[int] = Field(
        default=None,
    )
    """New messages number. Will be removed when messages.getCounters is released.."""

    memories: typing.Optional[int] = Field(
        default=None,
    )
    """New memories number."""

    notes: typing.Optional[int] = Field(
        default=None,
    )
    """New notes number."""

    notifications: typing.Optional[int] = Field(
        default=None,
    )
    """New notifications number."""

    photos: typing.Optional[int] = Field(
        default=None,
    )
    """New photo tags number."""


class AccountCountersFilter(str, enum.Enum, metaclass=BaseEnumMeta):
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
    """
    Model: `AccountInfo`
    """

    f__2fa_required: typing.Optional[bool] = Field(
        default=None,
        alias="2fa_required",
    )
    """Two factor authentication is enabled."""

    https_required: typing.Optional[bool] = Field(
        default=None,
    )
    """Information whether HTTPS-only is enabled."""

    intro: typing.Optional[int] = Field(
        default=None,
    )
    """Information whether user has been processed intro."""

    lang: typing.Optional[int] = Field(
        default=None,
    )
    """Language ID."""

    no_wall_replies: typing.Optional[bool] = Field(
        default=None,
    )
    """Information whether wall comments should be hidden."""

    own_posts_default: typing.Optional[bool] = Field(
        default=None,
    )
    """Information whether only owners posts should be shown."""


class AccountNameRequest(BaseModel):
    """
    Model: `AccountNameRequest`
    """

    first_name: typing.Optional[str] = Field(
        default=None,
    )
    """First name in request."""

    id: typing.Optional[int] = Field(
        default=None,
    )
    """Request ID needed to cancel the request."""

    last_name: typing.Optional[str] = Field(
        default=None,
    )
    """Last name in request."""

    status: typing.Optional["AccountNameRequestStatus"] = Field(
        default=None,
    )
    """Property `AccountNameRequest.status`."""

    lang: typing.Optional[str] = Field(
        default=None,
    )
    """Text to display to user."""

    link_href: typing.Optional[str] = Field(
        default=None,
    )
    """href for link in lang field."""

    link_label: typing.Optional[str] = Field(
        default=None,
    )
    """label to display for link in lang field."""


class AccountNameRequestStatus(str, enum.Enum, metaclass=BaseEnumMeta):
    SUCCESS = "success"
    PROCESSING = "processing"
    DECLINED = "declined"
    WAS_ACCEPTED = "was_accepted"
    WAS_DECLINED = "was_declined"
    DECLINED_WITH_LINK = "declined_with_link"
    RESPONSE = "response"
    RESPONSE_WITH_LINK = "response_with_link"


class AccountOfferLinkType(str, enum.Enum, metaclass=BaseEnumMeta):
    PROFILE = "profile"
    GROUP = "group"
    APP = "app"


class AccountOffer(BaseModel):
    """
    Model: `AccountOffer`
    """

    description: typing.Optional[str] = Field(
        default=None,
    )
    """Offer description."""

    id: typing.Optional[int] = Field(
        default=None,
    )
    """Offer ID."""

    img: typing.Optional[str] = Field(
        default=None,
    )
    """URL of the preview image."""

    instruction: typing.Optional[str] = Field(
        default=None,
    )
    """Instruction how to process the offer."""

    instruction_html: typing.Optional[str] = Field(
        default=None,
    )
    """Instruction how to process the offer (HTML format)."""

    price: typing.Optional[int] = Field(
        default=None,
    )
    """Offer price."""

    short_description: typing.Optional[str] = Field(
        default=None,
    )
    """Offer short description."""

    tag: typing.Optional[str] = Field(
        default=None,
    )
    """Offer tag."""

    title: typing.Optional[str] = Field(
        default=None,
    )
    """Offer title."""

    currency_amount: typing.Optional[float] = Field(
        default=None,
    )
    """Currency amount."""

    link_id: typing.Optional[int] = Field(
        default=None,
    )
    """Link id."""

    link_type: typing.Optional["AccountOfferLinkType"] = Field(
        default=None,
    )
    """Link type."""


class AccountPushConversations(BaseModel):
    """
    Model: `AccountPushConversations`
    """

    count: typing.Optional[int] = Field(
        default=None,
    )
    """Items count."""

    items: typing.Optional[typing.List["AccountPushConversationsItem"]] = Field(
        default=None,
    )
    """Property `AccountPushConversations.items`."""


class AccountPushConversationsItem(BaseModel):
    """
    Model: `AccountPushConversationsItem`
    """

    disabled_until: int = Field()
    """Time until that notifications are disabled in seconds."""

    peer_id: int = Field()
    """Peer ID."""

    sound: bool = Field()
    """Information whether the sound are enabled."""

    disabled_mentions: typing.Optional[bool] = Field(
        default=None,
    )
    """Information whether the mentions are disabled."""

    disabled_mass_mentions: typing.Optional[bool] = Field(
        default=None,
    )
    """Information whether the mass mentions (like \'@all\', \'@online\') are disabled. Can be affected by \'disabled_mentions\'."""


class AccountPushParams(BaseModel):
    """
    Model: `AccountPushParams`
    """

    msg: typing.Optional[typing.List["AccountPushParamsMode"]] = Field(
        default=None,
    )
    """Property `AccountPushParams.msg`."""

    chat: typing.Optional[typing.List["AccountPushParamsMode"]] = Field(
        default=None,
    )
    """Property `AccountPushParams.chat`."""

    like: typing.Optional[typing.List["AccountPushParamsSettings"]] = Field(
        default=None,
    )
    """Property `AccountPushParams.like`."""

    repost: typing.Optional[typing.List["AccountPushParamsSettings"]] = Field(
        default=None,
    )
    """Property `AccountPushParams.repost`."""

    comment: typing.Optional[typing.List["AccountPushParamsSettings"]] = Field(
        default=None,
    )
    """Property `AccountPushParams.comment`."""

    mention: typing.Optional[typing.List["AccountPushParamsSettings"]] = Field(
        default=None,
    )
    """Property `AccountPushParams.mention`."""

    reply: typing.Optional[typing.List["AccountPushParamsOnoff"]] = Field(
        default=None,
    )
    """Property `AccountPushParams.reply`."""

    new_post: typing.Optional[typing.List["AccountPushParamsOnoff"]] = Field(
        default=None,
    )
    """Property `AccountPushParams.new_post`."""

    wall_post: typing.Optional[typing.List["AccountPushParamsOnoff"]] = Field(
        default=None,
    )
    """Property `AccountPushParams.wall_post`."""

    wall_publish: typing.Optional[typing.List["AccountPushParamsOnoff"]] = Field(
        default=None,
    )
    """Property `AccountPushParams.wall_publish`."""

    friend: typing.Optional[typing.List["AccountPushParamsOnoff"]] = Field(
        default=None,
    )
    """Property `AccountPushParams.friend`."""

    friend_found: typing.Optional[typing.List["AccountPushParamsOnoff"]] = Field(
        default=None,
    )
    """Property `AccountPushParams.friend_found`."""

    friend_accepted: typing.Optional[typing.List["AccountPushParamsOnoff"]] = Field(
        default=None,
    )
    """Property `AccountPushParams.friend_accepted`."""

    group_invite: typing.Optional[typing.List["AccountPushParamsOnoff"]] = Field(
        default=None,
    )
    """Property `AccountPushParams.group_invite`."""

    group_accepted: typing.Optional[typing.List["AccountPushParamsOnoff"]] = Field(
        default=None,
    )
    """Property `AccountPushParams.group_accepted`."""

    birthday: typing.Optional[typing.List["AccountPushParamsOnoff"]] = Field(
        default=None,
    )
    """Property `AccountPushParams.birthday`."""

    event_soon: typing.Optional[typing.List["AccountPushParamsOnoff"]] = Field(
        default=None,
    )
    """Property `AccountPushParams.event_soon`."""

    app_request: typing.Optional[typing.List["AccountPushParamsOnoff"]] = Field(
        default=None,
    )
    """Property `AccountPushParams.app_request`."""

    sdk_open: typing.Optional[typing.List["AccountPushParamsOnoff"]] = Field(
        default=None,
    )
    """Property `AccountPushParams.sdk_open`."""


class AccountPushParamsMode(str, enum.Enum, metaclass=BaseEnumMeta):
    ON = "on"
    OFF = "off"
    NO_SOUND = "no_sound"
    NO_TEXT = "no_text"


class AccountPushParamsOnoff(str, enum.Enum, metaclass=BaseEnumMeta):
    ON = "on"
    OFF = "off"
    NO_SOUND = "no_sound"


class AccountPushParamsSettings(str, enum.Enum, metaclass=BaseEnumMeta):
    ON = "on"
    OFF = "off"
    FR_OF_FR = "fr_of_fr"
    NO_SOUND = "no_sound"


class AccountPushSettings(BaseModel):
    """
    Model: `AccountPushSettings`
    """

    disabled: typing.Optional[bool] = Field(
        default=None,
    )
    """Information whether notifications are disabled."""

    disabled_until: typing.Optional[int] = Field(
        default=None,
    )
    """Time until that notifications are disabled in Unixtime."""

    settings: typing.Optional["AccountPushParams"] = Field(
        default=None,
    )
    """Property `AccountPushSettings.settings`."""

    conversations: typing.Optional["AccountPushConversations"] = Field(
        default=None,
    )
    """Property `AccountPushSettings.conversations`."""


class AccountUserSettingsInterest(BaseModel):
    """
    Model: `AccountUserSettingsInterest`
    """

    title: str = Field()
    """Property `AccountUserSettingsInterest.title`."""

    value: str = Field()
    """Property `AccountUserSettingsInterest.value`."""


class AccountUserSettingsInterests(BaseModel):
    """
    Model: `AccountUserSettingsInterests`
    """

    activities: typing.Optional["AccountUserSettingsInterest"] = Field(
        default=None,
    )
    """Property `AccountUserSettingsInterests.activities`."""

    interests: typing.Optional["AccountUserSettingsInterest"] = Field(
        default=None,
    )
    """Property `AccountUserSettingsInterests.interests`."""

    music: typing.Optional["AccountUserSettingsInterest"] = Field(
        default=None,
    )
    """Property `AccountUserSettingsInterests.music`."""

    tv: typing.Optional["AccountUserSettingsInterest"] = Field(
        default=None,
    )
    """Property `AccountUserSettingsInterests.tv`."""

    movies: typing.Optional["AccountUserSettingsInterest"] = Field(
        default=None,
    )
    """Property `AccountUserSettingsInterests.movies`."""

    books: typing.Optional["AccountUserSettingsInterest"] = Field(
        default=None,
    )
    """Property `AccountUserSettingsInterests.books`."""

    games: typing.Optional["AccountUserSettingsInterest"] = Field(
        default=None,
    )
    """Property `AccountUserSettingsInterests.games`."""

    quotes: typing.Optional["AccountUserSettingsInterest"] = Field(
        default=None,
    )
    """Property `AccountUserSettingsInterests.quotes`."""

    about: typing.Optional["AccountUserSettingsInterest"] = Field(
        default=None,
    )
    """Property `AccountUserSettingsInterests.about`."""


class AddressFields(str, enum.Enum, metaclass=BaseEnumMeta):
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


class AdsAccessRole(str, enum.Enum, metaclass=BaseEnumMeta):
    ADMIN = "admin"
    MANAGER = "manager"
    REPORTS = "reports"


class AdsAccessRolePublic(str, enum.Enum, metaclass=BaseEnumMeta):
    MANAGER = "manager"
    REPORTS = "reports"


class AdsAccesses(BaseModel):
    """
    Model: `AdsAccesses`
    """

    client_id: typing.Optional[str] = Field(
        default=None,
    )
    """Client ID."""

    role: typing.Optional["AdsAccessRole"] = Field(
        default=None,
    )
    """Property `AdsAccesses.role`."""


class AdsAccount(BaseModel):
    """
    Model: `AdsAccount`
    """

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


class AdsAccountType(str, enum.Enum, metaclass=BaseEnumMeta):
    GENERAL = "general"
    AGENCY = "agency"


class AdsAd(BaseModel):
    """
    Model: `AdsAd`
    """

    ad_format: int = Field()
    """Ad format."""

    ad_platform: typing.Union["int", "str"] = Field()
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

    category1_id: typing.Optional[int] = Field(
        default=None,
    )
    """Category ID."""

    category2_id: typing.Optional[int] = Field(
        default=None,
    )
    """Additional category ID."""

    cpc: typing.Optional[str] = Field(
        default=None,
    )
    """Cost of a click, kopecks."""

    cpm: typing.Optional[str] = Field(
        default=None,
    )
    """Cost of 1000 impressions, kopecks."""

    cpa: typing.Optional[str] = Field(
        default=None,
    )
    """Cost of an action, kopecks."""

    ocpm: typing.Optional[str] = Field(
        default=None,
    )
    """Cost of 1000 impressions optimized, kopecks."""

    autobidding: typing.Optional[bool] = Field(
        default=None,
    )
    """Autobidding."""

    autobidding_max_cost: typing.Optional[str] = Field(
        default=None,
    )
    """Max cost of target actions for autobidding, kopecks."""

    disclaimer_medical: typing.Optional[bool] = Field(
        default=None,
    )
    """Information whether disclaimer is enabled."""

    disclaimer_specialist: typing.Optional[bool] = Field(
        default=None,
    )
    """Information whether disclaimer is enabled."""

    disclaimer_supplements: typing.Optional[bool] = Field(
        default=None,
    )
    """Information whether disclaimer is enabled."""

    disclaimer_credits: typing.Optional[bool] = Field(
        default=None,
    )
    """Information whether disclaimer is enabled."""

    impressions_limit: typing.Optional[int] = Field(
        default=None,
    )
    """Impressions limit."""

    impressions_limit_period: typing.Optional[int] = Field(
        default=None,
    )
    """Impressions limit period."""

    impressions_limited: typing.Optional[bool] = Field(
        default=None,
    )
    """Information whether impressions are limited."""

    video: typing.Optional[bool] = Field(
        default=None,
    )
    """Information whether the ad is a video."""

    day_limit: typing.Optional[str] = Field(
        default=None,
    )
    """Day limit."""

    goal_type: typing.Optional[int] = Field(
        default=None,
    )
    """Goal type."""

    user_goal_type: typing.Optional[int] = Field(
        default=None,
    )
    """User goal type."""

    age_restriction: typing.Optional[int] = Field(
        default=None,
    )
    """Age restriction."""

    conversion_pixel_id: typing.Optional[int] = Field(
        default=None,
    )
    """Conversion pixel id."""

    conversion_event_id: typing.Optional[int] = Field(
        default=None,
    )
    """Conversion event id."""

    create_time: typing.Optional[int] = Field(
        default=None,
    )
    """Create time."""

    update_time: typing.Optional[int] = Field(
        default=None,
    )
    """Update time."""

    start_time: typing.Optional[int] = Field(
        default=None,
    )
    """Start time."""

    stop_time: typing.Optional[int] = Field(
        default=None,
    )
    """Stop time."""

    publisher_platforms_auto: typing.Optional[bool] = Field(
        default=None,
    )
    """Publisher platform auto."""

    publisher_platforms: typing.Optional[str] = Field(
        default=None,
    )
    """Publisher platforms."""

    link_url: typing.Optional[str] = Field(
        default=None,
    )
    """Link url."""

    link_owner_id: typing.Optional[int] = Field(
        default=None,
    )
    """Link owner id."""

    link_id: typing.Optional[int] = Field(
        default=None,
    )
    """Link id."""

    has_campaign_budget_optimization: typing.Optional[bool] = Field(
        default=None,
    )
    """Has campaign budget optimization."""

    events_retargeting_groups: typing.Optional[typing.List["AdsEventsRetargetingGroup"]] = Field(
        default=None,
    )
    """Events retargeting groups."""

    weekly_schedule_hours: typing.Optional[typing.List[str]] = Field(
        default=None,
    )
    """Weekly schedule hours."""

    weekly_schedule_use_holidays: typing.Optional[int] = Field(
        default=None,
    )
    """Weekly schedule use holidays."""

    ad_platform_no_ad_network: typing.Optional[int] = Field(
        default=None,
    )
    """Ad platform no ad network."""

    ad_platform_no_wall: typing.Optional[int] = Field(
        default=None,
    )
    """Ad platform no wall."""

    disclaimer_finance: typing.Optional[int] = Field(
        default=None,
    )
    """Disclaimer finance."""

    disclaimer_finance_name: typing.Optional[str] = Field(
        default=None,
    )
    """Disclaimer finance name."""

    disclaimer_finance_license_no: typing.Optional[str] = Field(
        default=None,
    )
    """Disclaimer finance license no."""

    is_promo: typing.Optional[bool] = Field(
        default=None,
    )
    """is promo."""

    suggested_criteria: typing.Optional[int] = Field(
        default=None,
    )
    """Suggested criteria."""

    link_type: typing.Optional[int] = Field(
        default=None,
    )
    """Link type."""


class AdsAdApproved(int, enum.Enum, metaclass=BaseEnumMeta):
    NOT_MODERATED = 0
    PENDING_MODERATION = 1
    APPROVED = 2
    REJECTED = 3


class AdsAdCostType(int, enum.Enum, metaclass=BaseEnumMeta):
    PER_CLICKS = 0
    PER_IMPRESSIONS = 1
    PER_ACTIONS = 2
    PER_IMPRESSIONS_OPTIMIZED = 3


class AdsAdLayout(BaseModel):
    """
    Model: `AdsAdLayout`
    """

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

    image_src_2x: typing.Optional[str] = Field(
        default=None,
    )
    """URL of the preview image in double size."""

    link_domain: typing.Optional[str] = Field(
        default=None,
    )
    """Domain of advertised object."""

    preview_link: typing.Optional[str] = Field(
        default=None,
    )
    """link to preview an ad as it is shown on the website."""

    video: typing.Optional[bool] = Field(
        default=None,
    )
    """Information whether the ad is a video."""

    social: typing.Optional[bool] = Field(
        default=None,
    )
    """Social."""

    okved: typing.Optional[str] = Field(
        default=None,
    )
    """Okved."""

    age_restriction: typing.Optional[int] = Field(
        default=None,
    )
    """Age restriction."""

    goal_type: typing.Optional[int] = Field(
        default=None,
    )
    """Goal type."""

    link_title: typing.Optional[str] = Field(
        default=None,
    )
    """Link title."""

    link_button: typing.Optional[str] = Field(
        default=None,
    )
    """Link button."""

    repeat_video: typing.Optional[int] = Field(
        default=None,
    )
    """Repeat video."""

    video_src_240: typing.Optional[str] = Field(
        default=None,
    )
    """Video source 240p."""

    video_src_360: typing.Optional[str] = Field(
        default=None,
    )
    """Video source 360p."""

    video_src_480: typing.Optional[str] = Field(
        default=None,
    )
    """Video source 480p."""

    video_src_720: typing.Optional[str] = Field(
        default=None,
    )
    """Video source 720p."""

    video_src_1080: typing.Optional[str] = Field(
        default=None,
    )
    """Video source 1080p."""

    video_src_1440: typing.Optional[str] = Field(
        default=None,
    )
    """Video source 1440p."""

    video_src_2160: typing.Optional[str] = Field(
        default=None,
    )
    """Video source 2160p."""

    video_image_src: typing.Optional[str] = Field(
        default=None,
    )
    """Video image source."""

    video_image_src_2x: typing.Optional[str] = Field(
        default=None,
    )
    """Video image source 2x."""

    video_duration: typing.Optional[int] = Field(
        default=None,
    )
    """Video duration."""

    icon_src: typing.Optional[str] = Field(
        default=None,
    )
    """Icon source."""

    icon_src_2x: typing.Optional[str] = Field(
        default=None,
    )
    """Icon source 2x."""

    post: typing.Optional["AdsPost"] = Field(
        default=None,
    )
    """Property `AdsAdLayout.post`."""

    stories_data: typing.Optional["AdsStories"] = Field(
        default=None,
    )
    """Property `AdsAdLayout.stories_data`."""

    clips_list: typing.Optional[typing.List["AdsClipItem"]] = Field(
        default=None,
    )
    """Property `AdsAdLayout.clips_list`."""


class AdsAdStatus(int, enum.Enum, metaclass=BaseEnumMeta):
    STOPPED = 0
    STARTED = 1
    DELETED = 2


class AdsCampaign(BaseModel):
    """
    Model: `AdsCampaign`
    """

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

    ads_count: typing.Optional[int] = Field(
        default=None,
    )
    """Amount of active ads in campaign."""

    create_time: typing.Optional[int] = Field(
        default=None,
    )
    """Campaign create time, as Unixtime."""

    goal_type: typing.Optional[int] = Field(
        default=None,
    )
    """Campaign goal type."""

    user_goal_type: typing.Optional[int] = Field(
        default=None,
    )
    """Campaign user goal type."""

    is_cbo_enabled: typing.Optional[bool] = Field(
        default=None,
    )
    """Shows if Campaign Budget Optimization is on."""

    update_time: typing.Optional[int] = Field(
        default=None,
    )
    """Campaign update time, as Unixtime."""

    views_limit: typing.Optional[int] = Field(
        default=None,
    )
    """Limit of views per user per campaign."""


class AdsCampaignStatus(int, enum.Enum, metaclass=BaseEnumMeta):
    STOPPED = 0
    STARTED = 1
    DELETED = 2


class AdsCampaignType(str, enum.Enum, metaclass=BaseEnumMeta):
    NORMAL = "normal"
    VK_APPS_MANAGED = "vk_apps_managed"
    MOBILE_APPS = "mobile_apps"
    PROMOTED_POSTS = "promoted_posts"
    ADAPTIVE_ADS = "adaptive_ads"
    STORIES = "stories"


class AdsCategory(BaseModel):
    """
    Model: `AdsCategory`
    """

    id: int = Field()
    """Category ID."""

    name: str = Field()
    """Category name."""

    subcategories: typing.Optional[typing.List["AdsCategory"]] = Field(
        default=None,
    )
    """Property `AdsCategory.subcategories`."""


class AdsClient(BaseModel):
    """
    Model: `AdsClient`
    """

    all_limit: str = Field()
    """Client\'s total limit, rubles."""

    day_limit: str = Field()
    """Client\'s day limit, rubles."""

    id: int = Field()
    """Client ID."""

    name: str = Field()
    """Client name."""

    ord_data: typing.Optional["AdsOrdData"] = Field(
        default=None,
    )
    """Ord data."""


class AdsClipItem(BaseModel):
    """
    Model: `AdsClipItem`
    """

    video_id: typing.Optional[int] = Field(
        default=None,
    )
    """Video id."""

    preview_url: typing.Optional[str] = Field(
        default=None,
    )
    """Preview url."""

    link: typing.Optional["AdsClipItemLink"] = Field(
        default=None,
    )
    """Property `AdsClipItem.link`."""


class AdsClipItemLink(BaseModel):
    """
    Link
    Model: `AdsClipItemLink`
    """

    text: typing.Optional[str] = Field(
        default=None,
    )
    """Text."""

    key: typing.Optional[str] = Field(
        default=None,
    )
    """Key."""

    url: typing.Optional[str] = Field(
        default=None,
    )
    """Url."""


class AdsCreateAdStatus(BaseModel):
    """
    Model: `AdsCreateAdStatus`
    """

    id: int = Field()
    """Ad ID."""

    post_id: typing.Optional[int] = Field(
        default=None,
    )
    """Stealth Post ID."""

    error_code: typing.Optional[int] = Field(
        default=None,
    )
    """Error code."""

    error_desc: typing.Optional[str] = Field(
        default=None,
    )
    """Error description."""


class AdsCreateCampaignStatus(BaseModel):
    """
    Model: `AdsCreateCampaignStatus`
    """

    id: int = Field()
    """Campaign ID."""

    error_code: typing.Optional[int] = Field(
        default=None,
    )
    """Error code."""

    error_desc: typing.Optional[str] = Field(
        default=None,
    )
    """Error description."""


class AdsCreateClientsStatus(BaseModel):
    """
    Model: `AdsCreateClientsStatus`
    """

    id: int = Field()
    """Client ID."""

    error_code: typing.Optional[int] = Field(
        default=None,
    )
    """Error code."""

    error_desc: typing.Optional[str] = Field(
        default=None,
    )
    """Error description."""


class AdsCriteria(BaseModel):
    """
    Model: `AdsCriteria`
    """

    age_from: typing.Optional[str] = Field(
        default=None,
    )
    """Age from."""

    age_to: typing.Optional[str] = Field(
        default=None,
    )
    """Age to."""

    apps: typing.Optional[str] = Field(
        default=None,
    )
    """Apps IDs."""

    apps_not: typing.Optional[str] = Field(
        default=None,
    )
    """Apps IDs to except."""

    birthday: typing.Optional[str] = Field(
        default=None,
    )
    """Days to birthday."""

    cities: typing.Optional[str] = Field(
        default=None,
    )
    """Cities IDs."""

    cities_not: typing.Optional[str] = Field(
        default=None,
    )
    """Cities IDs to except."""

    districts: typing.Optional[str] = Field(
        default=None,
    )
    """Districts IDs."""

    groups: typing.Optional[str] = Field(
        default=None,
    )
    """Communities IDs."""

    interest_categories: typing.Optional[str] = Field(
        default=None,
    )
    """Interests categories IDs."""

    interests: typing.Optional[str] = Field(
        default=None,
    )
    """Interests."""

    paying: typing.Optional[str] = Field(
        default=None,
    )
    """Information whether the user has proceeded VK payments before."""

    positions: typing.Optional[str] = Field(
        default=None,
    )
    """Positions IDs."""

    religions: typing.Optional[str] = Field(
        default=None,
    )
    """Religions IDs."""

    retargeting_groups: typing.Optional[str] = Field(
        default=None,
    )
    """Retargeting groups ids."""

    retargeting_groups_not: typing.Optional[str] = Field(
        default=None,
    )
    """Retargeting groups NOT ids."""

    school_from: typing.Optional[str] = Field(
        default=None,
    )
    """School graduation year from."""

    school_to: typing.Optional[str] = Field(
        default=None,
    )
    """School graduation year to."""

    schools: typing.Optional[str] = Field(
        default=None,
    )
    """Schools IDs."""

    sex: typing.Optional["AdsCriteriaSex"] = Field(
        default=None,
    )
    """Property `AdsCriteria.sex`."""

    stations: typing.Optional[str] = Field(
        default=None,
    )
    """Stations IDs."""

    statuses: typing.Optional[str] = Field(
        default=None,
    )
    """Relationship statuses."""

    streets: typing.Optional[str] = Field(
        default=None,
    )
    """Streets IDs."""

    travellers: typing.Optional[str] = Field(
        default=None,
    )
    """Travellers."""

    ab_test: typing.Optional[str] = Field(
        default=None,
    )
    """AB test."""

    uni_from: typing.Optional[str] = Field(
        default=None,
    )
    """University graduation year from."""

    uni_to: typing.Optional[str] = Field(
        default=None,
    )
    """University graduation year to."""

    user_browsers: typing.Optional[str] = Field(
        default=None,
    )
    """Browsers."""

    user_devices: typing.Optional[str] = Field(
        default=None,
    )
    """Devices."""

    user_os: typing.Optional[str] = Field(
        default=None,
    )
    """Operating systems."""

    suggested_criteria: typing.Optional[str] = Field(
        default=None,
    )
    """Suggested criteria."""

    groups_not: typing.Optional[str] = Field(
        default=None,
    )
    """Group not."""

    price_list_audience_type: typing.Optional[str] = Field(
        default=None,
    )
    """Price list audience type."""

    count: typing.Optional[str] = Field(
        default=None,
    )
    """Count."""

    groups_active_formula: typing.Optional[str] = Field(
        default=None,
    )
    """Group active formula."""

    interest_categories_formula: typing.Optional[str] = Field(
        default=None,
    )
    """Interest categories formula."""

    groups_formula: typing.Optional[str] = Field(
        default=None,
    )
    """Groups formula."""

    groups_active: typing.Optional[str] = Field(
        default=None,
    )
    """Groups active."""

    group_types: typing.Optional[str] = Field(
        default=None,
    )
    """Group types."""

    key_phrases: typing.Optional[str] = Field(
        default=None,
    )
    """Key phrases."""

    key_phrases_days: typing.Optional[str] = Field(
        default=None,
    )
    """Key phrases days."""

    geo_near: typing.Optional[str] = Field(
        default=None,
    )
    """Geo near."""

    geo_point_type: typing.Optional[str] = Field(
        default=None,
    )
    """Geo point type."""

    price_list_id: typing.Optional[str] = Field(
        default=None,
    )
    """Price list id."""

    groups_recommended: typing.Optional[str] = Field(
        default=None,
    )
    """Groups recommended ids."""

    groups_active_recommended: typing.Optional[str] = Field(
        default=None,
    )
    """Groups active recommended ids."""

    music_artists_formula: typing.Optional[str] = Field(
        default=None,
    )
    """Music artists formula."""

    price_list_retargeting_formula: typing.Optional[str] = Field(
        default=None,
    )
    """Price list retargeting formula."""

    tags: typing.Optional[str] = Field(
        default=None,
    )
    """Tags."""

    browsers: typing.Optional[str] = Field(
        default=None,
    )
    """Browsers."""

    mobile_os_min_version: typing.Optional[str] = Field(
        default=None,
    )
    """Mobile os min version."""

    mobile_apps_events_formula: typing.Optional[str] = Field(
        default=None,
    )
    """Mobile apps events formula."""

    mobile_os_max_version: typing.Optional[str] = Field(
        default=None,
    )
    """Mobile os max version."""

    operators: typing.Optional[str] = Field(
        default=None,
    )
    """operators."""

    wifi_only: typing.Optional[str] = Field(
        default=None,
    )
    """wifi_only."""

    mobile_manufacturers: typing.Optional[str] = Field(
        default=None,
    )
    """mobile_manufacturers."""


class AdsCriteriaSex(str, enum.Enum, metaclass=BaseEnumMeta):
    f__0 = "0"
    f__1 = "1"
    f__2 = "2"


class AdsDemoStats(BaseModel):
    """
    Model: `AdsDemoStats`
    """

    id: typing.Optional[int] = Field(
        default=None,
    )
    """Object ID."""

    stats: typing.Optional[typing.List["AdsDemostatsFormat"]] = Field(
        default=None,
    )
    """Property `AdsDemoStats.stats`."""

    type: typing.Optional["AdsObjectType"] = Field(
        default=None,
    )
    """Property `AdsDemoStats.type`."""


class AdsDemographicStatsPeriodItemBase(BaseModel):
    """
    Model: `AdsDemographicStatsPeriodItemBase`
    """

    clicks_rate: typing.Optional[float] = Field(
        default=None,
    )
    """Clicks rate."""

    impressions_rate: typing.Optional[float] = Field(
        default=None,
    )
    """Impressions rate."""


class AdsDemostatsFormat(BaseModel):
    """
    Model: `AdsDemostatsFormat`
    """

    age: typing.Optional[typing.List["AdsStatsAge"]] = Field(
        default=None,
    )
    """Property `AdsDemostatsFormat.age`."""

    cities: typing.Optional[typing.List["AdsStatsCities"]] = Field(
        default=None,
    )
    """Property `AdsDemostatsFormat.cities`."""

    day: typing.Optional[str] = Field(
        default=None,
    )
    """Day as YYYY-MM-DD."""

    day_from: typing.Optional[str] = Field(
        default=None,
    )
    """Property `AdsDemostatsFormat.day_from`."""

    day_to: typing.Optional[str] = Field(
        default=None,
    )
    """Property `AdsDemostatsFormat.day_to`."""

    month: typing.Optional[str] = Field(
        default=None,
    )
    """Month as YYYY-MM."""

    overall: typing.Optional[int] = Field(
        default=None,
    )
    """1 if period=overall."""

    sex: typing.Optional[typing.List["AdsStatsSex"]] = Field(
        default=None,
    )
    """Property `AdsDemostatsFormat.sex`."""

    sex_age: typing.Optional[typing.List["AdsStatsSexAge"]] = Field(
        default=None,
    )
    """Property `AdsDemostatsFormat.sex_age`."""


class AdsEventsRetargetingGroup(BaseModel):
    """
    Model: `AdsEventsRetargetingGroup`
    """

    id: typing.Optional[int] = Field(
        default=None,
    )
    """Property `AdsEventsRetargetingGroup.id`."""

    value: typing.Optional[typing.List[int]] = Field(
        default=None,
    )
    """Property `AdsEventsRetargetingGroup.value`."""


class AdsFloodStats(BaseModel):
    """
    Model: `AdsFloodStats`
    """

    left: int = Field()
    """Requests left."""

    refresh: int = Field()
    """Time to refresh in seconds."""

    stats_by_user: typing.Optional[typing.List["AdsFloodStatsByUserItem"]] = Field(
        default=None,
    )
    """Used requests per user."""


class AdsFloodStatsByUserItem(BaseModel):
    """
    Model: `AdsFloodStatsByUserItem`
    """

    user_id: int = Field()
    """User ID."""

    requests_count: int = Field()
    """Used requests."""


class AdsLinkStatus(BaseModel):
    """
    Model: `AdsLinkStatus`
    """

    status: str = Field()
    """Link status."""

    description: typing.Optional[str] = Field(
        default=None,
    )
    """Reject reason."""

    redirect_url: typing.Optional[str] = Field(
        default=None,
    )
    """URL."""


class AdsLookalikeRequestStatus(str, enum.Enum, metaclass=BaseEnumMeta):
    SEARCH_IN_PROGRESS = "search_in_progress"
    SEARCH_FAILED = "search_failed"
    SEARCH_DONE = "search_done"
    SAVE_IN_PROGRESS = "save_in_progress"
    SAVE_FAILED = "save_failed"
    SAVE_DONE = "save_done"


class AdsLookalikeRequestSourceType(str, enum.Enum, metaclass=BaseEnumMeta):
    RETARGETING_GROUP = "retargeting_group"


class AdsLookalikeRequest(BaseModel):
    """
    Model: `AdsLookalikeRequest`
    """

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

    scheduled_delete_time: typing.Optional[int] = Field(
        default=None,
    )
    """Time by which lookalike request would be deleted, as Unixtime."""

    source_retargeting_group_id: typing.Optional[int] = Field(
        default=None,
    )
    """Retargeting group id, which was used as lookalike seed."""

    source_name: typing.Optional[str] = Field(
        default=None,
    )
    """Lookalike request seed name (retargeting group name)."""

    audience_count: typing.Optional[int] = Field(
        default=None,
    )
    """Lookalike request seed audience size."""

    save_audience_levels: typing.Optional[typing.List["AdsLookalikeRequestSaveAudienceLevel"]] = Field(
        default=None,
    )
    """Property `AdsLookalikeRequest.save_audience_levels`."""


class AdsLookalikeRequestSaveAudienceLevel(BaseModel):
    """
    Model: `AdsLookalikeRequestSaveAudienceLevel`
    """

    level: typing.Optional[int] = Field(
        default=None,
    )
    """Save audience level id, which is used in save audience queries."""

    audience_count: typing.Optional[int] = Field(
        default=None,
    )
    """Saved audience audience size for according level."""


class AdsMobileStatItem(BaseModel):
    """
    Model: `AdsMobileStatItem`
    """

    key: typing.Optional[str] = Field(
        default=None,
    )
    """Property `AdsMobileStatItem.key`."""

    value: typing.Optional[float] = Field(
        default=None,
    )
    """Property `AdsMobileStatItem.value`."""


class AdsMusician(BaseModel):
    """
    Model: `AdsMusician`
    """

    id: int = Field()
    """Targeting music artist ID."""

    original_id: str = Field()
    """Music artist ID as in VKMusic."""

    name: str = Field()
    """Music artist name."""

    avatar: typing.Optional[str] = Field(
        default=None,
    )
    """Music artist photo."""


class AdsObjectType(str, enum.Enum, metaclass=BaseEnumMeta):
    AD = "ad"
    CAMPAIGN = "campaign"
    CLIENT = "client"
    OFFICE = "office"


class AdsOrdClientType(str, enum.Enum, metaclass=BaseEnumMeta):
    PERSON = "person"
    INDIVIDUAL = "individual"
    LEGAL = "legal"
    FOREIGN = "foreign"
    UNKNOWN = "unknown"


class AdsOrdData(BaseModel):
    """
    Model: `AdsOrdData`
    """

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

    inn: typing.Optional[str] = Field(
        default=None,
    )
    """Property `AdsOrdData.inn`."""

    agency_phone: typing.Optional[str] = Field(
        default=None,
    )
    """Property `AdsOrdData.agency_phone`."""

    subagent: typing.Optional["AdsOrdSubagent"] = Field(
        default=None,
    )
    """Property `AdsOrdData.subagent`."""


class AdsOrdSubagent(BaseModel):
    """
    Model: `AdsOrdSubagent`
    """

    type: "AdsOrdClientType" = Field()
    """Property `AdsOrdSubagent.type`."""

    name: str = Field()
    """Property `AdsOrdSubagent.name`."""

    phone: str = Field()
    """Property `AdsOrdSubagent.phone`."""

    inn: typing.Optional[str] = Field(
        default=None,
    )
    """Property `AdsOrdSubagent.inn`."""


class AdsPost(BaseModel):
    """
    Model: `AdsPost`
    """

    id: typing.Optional[int] = Field(
        default=None,
    )
    """Post id."""

    from_id: typing.Optional[int] = Field(
        default=None,
    )
    """From id."""

    owner_id: typing.Optional[int] = Field(
        default=None,
    )
    """Owner id."""

    date: typing.Optional[int] = Field(
        default=None,
    )
    """Date."""

    edited: typing.Optional[int] = Field(
        default=None,
    )
    """Edited date."""

    is_pinned: typing.Optional[int] = Field(
        default=None,
    )
    """Is pinned."""

    marked_as_ads: typing.Optional[int] = Field(
        default=None,
    )
    """Marked as ads."""

    ads_easy_promote: typing.Optional["AdsPostEasyPromote"] = Field(
        default=None,
    )
    """Property `AdsPost.ads_easy_promote`."""

    donut: typing.Optional["AdsPostDonut"] = Field(
        default=None,
    )
    """Property `AdsPost.donut`."""

    comments: typing.Optional["AdsPostComments"] = Field(
        default=None,
    )
    """Property `AdsPost.comments`."""

    copyright: typing.Optional["WallPostCopyright"] = Field(
        default=None,
    )
    """Property `AdsPost.copyright`."""

    short_text_rate: typing.Optional[float] = Field(
        default=None,
    )
    """Short text rate."""

    type: typing.Optional[str] = Field(
        default=None,
    )
    """Type."""

    is_favorite: typing.Optional[bool] = Field(
        default=None,
    )
    """Is favorite."""

    likes: typing.Optional["AdsPostLikes"] = Field(
        default=None,
    )
    """Property `AdsPost.likes`."""

    views: typing.Optional["AdsPostViews"] = Field(
        default=None,
    )
    """Property `AdsPost.views`."""

    post_type: typing.Optional[str] = Field(
        default=None,
    )
    """Post type."""

    reposts: typing.Optional["AdsPostReposts"] = Field(
        default=None,
    )
    """Property `AdsPost.reposts`."""

    text: typing.Optional[str] = Field(
        default=None,
    )
    """Text."""

    is_promoted_post_stealth: typing.Optional[bool] = Field(
        default=None,
    )
    """Is promoted post stealth."""

    hash: typing.Optional[str] = Field(
        default=None,
    )
    """Hash."""

    owner: typing.Optional["AdsPostOwner"] = Field(
        default=None,
    )
    """Property `AdsPost.owner`."""

    attachments: typing.Optional[typing.List["WallWallpostAttachment"]] = Field(
        default=None,
    )
    """Property `AdsPost.attachments`."""

    created_by: typing.Optional[int] = Field(
        default=None,
    )
    """Created by."""

    carousel_offset: typing.Optional[int] = Field(
        default=None,
    )
    """Carousel offset."""

    can_edit: typing.Optional[int] = Field(
        default=None,
    )
    """Can edit."""

    can_delete: typing.Optional[int] = Field(
        default=None,
    )
    """Can delete."""

    can_pin: typing.Optional[int] = Field(
        default=None,
    )
    """Can pin."""


class AdsPostComments(BaseModel):
    """
    Comments
    Model: `AdsPostComments`
    """

    count: typing.Optional[int] = Field(
        default=None,
    )
    """Count."""


class AdsPostDonut(BaseModel):
    """
    Donut
    Model: `AdsPostDonut`
    """

    is_donut: typing.Optional[bool] = Field(
        default=None,
    )
    """Is donut."""


class AdsPostEasyPromote(BaseModel):
    """
    Ads easy promote
    Model: `AdsPostEasyPromote`
    """

    type: typing.Optional[int] = Field(
        default=None,
    )
    """Type."""

    text: typing.Optional[str] = Field(
        default=None,
    )
    """Text."""

    label_text: typing.Optional[str] = Field(
        default=None,
    )
    """Label text."""

    button_text: typing.Optional[str] = Field(
        default=None,
    )
    """Button text."""

    is_ad_not_easy: typing.Optional[bool] = Field(
        default=None,
    )
    """Is ad not easy."""

    ad_id: typing.Optional[int] = Field(
        default=None,
    )
    """Ad id."""

    top_union_id: typing.Optional[int] = Field(
        default=None,
    )
    """Top union id."""


class AdsPostLikes(BaseModel):
    """
    Likes
    Model: `AdsPostLikes`
    """

    can_like: typing.Optional[int] = Field(
        default=None,
    )
    """Can like."""

    count: typing.Optional[int] = Field(
        default=None,
    )
    """Count."""

    user_likes: typing.Optional[int] = Field(
        default=None,
    )
    """User likes."""


class AdsPostOwner(BaseModel):
    """
    Owner
    Model: `AdsPostOwner`
    """

    id: typing.Optional[int] = Field(
        default=None,
    )
    """Owner id."""

    name: typing.Optional[str] = Field(
        default=None,
    )
    """Name."""

    photo: typing.Optional[str] = Field(
        default=None,
    )
    """Photo url."""

    url: typing.Optional[str] = Field(
        default=None,
    )
    """Profile url."""


class AdsPostReposts(BaseModel):
    """
    Reposts
    Model: `AdsPostReposts`
    """

    count: typing.Optional[int] = Field(
        default=None,
    )
    """Count."""

    wall_count: typing.Optional[int] = Field(
        default=None,
    )
    """Wall count."""

    mail_count: typing.Optional[int] = Field(
        default=None,
    )
    """Mail count."""


class AdsPostViews(BaseModel):
    """
    Views
    Model: `AdsPostViews`
    """

    count: typing.Optional[int] = Field(
        default=None,
    )
    """Count."""


class AdsPromotedPostReach(BaseModel):
    """
    Model: `AdsPromotedPostReach`
    """

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

    video_views_100p: typing.Optional[int] = Field(
        default=None,
    )
    """Video views for 100 percent."""

    video_views_25p: typing.Optional[int] = Field(
        default=None,
    )
    """Video views for 25 percent."""

    video_views_3s: typing.Optional[int] = Field(
        default=None,
    )
    """Video views for 3 seconds."""

    video_views_10s: typing.Optional[int] = Field(
        default=None,
    )
    """Video views for 10 seconds."""

    video_views_50p: typing.Optional[int] = Field(
        default=None,
    )
    """Video views for 50 percent."""

    video_views_75p: typing.Optional[int] = Field(
        default=None,
    )
    """Video views for 75 percent."""

    video_views_start: typing.Optional[int] = Field(
        default=None,
    )
    """Video starts."""

    pretty_cards_clicks: typing.Optional[int] = Field(
        default=None,
    )
    """Pretty cards clicks."""


class AdsRejectReason(BaseModel):
    """
    Model: `AdsRejectReason`
    """

    comment: typing.Optional[str] = Field(
        default=None,
    )
    """Comment text."""

    rules: typing.Optional[typing.List["AdsRules"]] = Field(
        default=None,
    )
    """Property `AdsRejectReason.rules`."""


class AdsRules(BaseModel):
    """
    Model: `AdsRules`
    """

    help_url: typing.Optional[typing.Union["str", "bool"]] = Field(
        default=None,
    )
    """Help url."""

    help_label: typing.Optional[str] = Field(
        default=None,
    )
    """Label."""

    content_html: typing.Optional[str] = Field(
        default=None,
    )
    """Content Html."""

    help_chat: typing.Optional[bool] = Field(
        default=None,
    )
    """Help chat."""


class AdsStatisticClickActionType(str, enum.Enum, metaclass=BaseEnumMeta):
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
    """
    Model: `AdsStatisticClickAction`
    """

    type: typing.Optional["AdsStatisticClickActionType"] = Field(
        default=None,
    )
    """Property `AdsStatisticClickAction.type`."""

    url: typing.Optional[str] = Field(
        default=None,
    )
    """Property `AdsStatisticClickAction.url`."""


class AdsStats(BaseModel):
    """
    Model: `AdsStats`
    """

    id: typing.Optional[int] = Field(
        default=None,
    )
    """Object ID."""

    stats: typing.Optional[typing.List["AdsStatsFormat"]] = Field(
        default=None,
    )
    """Property `AdsStats.stats`."""

    type: typing.Optional["AdsObjectType"] = Field(
        default=None,
    )
    """Property `AdsStats.type`."""

    views_times: typing.Optional["AdsStatsViewsTimes"] = Field(
        default=None,
    )
    """Property `AdsStats.views_times`."""


class AdsStatsFormat(BaseModel):
    """
    Model: `AdsStatsFormat`
    """

    clicks: typing.Optional[int] = Field(
        default=None,
    )
    """Clicks number."""

    link_external_clicks: typing.Optional[int] = Field(
        default=None,
    )
    """External clicks number."""

    day: typing.Optional[str] = Field(
        default=None,
    )
    """Day as YYYY-MM-DD."""

    impressions: typing.Optional[int] = Field(
        default=None,
    )
    """Impressions number."""

    join_rate: typing.Optional[int] = Field(
        default=None,
    )
    """Events number."""

    month: typing.Optional[str] = Field(
        default=None,
    )
    """Month as YYYY-MM."""

    year: typing.Optional[int] = Field(
        default=None,
    )
    """Year as YYYY."""

    overall: typing.Optional[int] = Field(
        default=None,
    )
    """1 if period=overall."""

    reach: typing.Optional[int] = Field(
        default=None,
    )
    """Reach ."""

    spent: typing.Optional[str] = Field(
        default=None,
    )
    """Spent funds."""

    video_plays_unique_started: typing.Optional[int] = Field(
        default=None,
    )
    """Video plays unique started count."""

    video_plays_unique_3_seconds: typing.Optional[int] = Field(
        default=None,
    )
    """Video plays unique 3 seconds count."""

    video_plays_unique_10_seconds: typing.Optional[int] = Field(
        default=None,
    )
    """Video plays unique 10 seconds count."""

    video_plays_unique_25_percents: typing.Optional[int] = Field(
        default=None,
    )
    """Video plays unique 25 percents count."""

    video_plays_unique_50_percents: typing.Optional[int] = Field(
        default=None,
    )
    """Video plays unique 50 percents count."""

    video_plays_unique_75_percents: typing.Optional[int] = Field(
        default=None,
    )
    """Video plays unique 75 percents count."""

    video_plays_unique_100_percents: typing.Optional[int] = Field(
        default=None,
    )
    """Video plays unique 100 percents count."""

    effective_cost_per_click: typing.Optional[str] = Field(
        default=None,
    )
    """Effective cost per click."""

    effective_cost_per_mille: typing.Optional[str] = Field(
        default=None,
    )
    """Effective cost per mille."""

    effective_cpf: typing.Optional[str] = Field(
        default=None,
    )
    """Effective cpf."""

    effective_cost_per_message: typing.Optional[str] = Field(
        default=None,
    )
    """Effective cost per message."""

    message_sends: typing.Optional[int] = Field(
        default=None,
    )
    """Message sends count."""

    message_sends_by_any_user: typing.Optional[int] = Field(
        default=None,
    )
    """Message sends by anu user."""

    conversions_external: typing.Optional[int] = Field(
        default=None,
    )
    """Conversions external."""

    conversion_count: typing.Optional[int] = Field(
        default=None,
    )
    """Conversions count."""

    conversion_cr: typing.Optional[str] = Field(
        default=None,
    )
    """Conversions CR."""

    day_from: typing.Optional[str] = Field(
        default=None,
    )
    """Day from."""

    day_to: typing.Optional[str] = Field(
        default=None,
    )
    """Day to."""

    ctr: typing.Optional[str] = Field(
        default=None,
    )
    """Ctr."""

    uniq_views_count: typing.Optional[int] = Field(
        default=None,
    )
    """Unique views count."""

    mobile_app_stat: typing.Optional[typing.List["AdsMobileStatItem"]] = Field(
        default=None,
    )
    """Mobile app stat."""


class AdsStatsSexValue(str, enum.Enum, metaclass=BaseEnumMeta):
    F = "f"
    M = "m"


class AdsStatsViewsTimes(BaseModel):
    """
    Model: `AdsStatsViewsTimes`
    """

    views_ads_times_1: typing.Optional[int] = Field(
        default=None,
    )
    """Property `AdsStatsViewsTimes.views_ads_times_1`."""

    views_ads_times_2: typing.Optional[int] = Field(
        default=None,
    )
    """Property `AdsStatsViewsTimes.views_ads_times_2`."""

    views_ads_times_3: typing.Optional[int] = Field(
        default=None,
    )
    """Property `AdsStatsViewsTimes.views_ads_times_3`."""

    views_ads_times_4: typing.Optional[int] = Field(
        default=None,
    )
    """Property `AdsStatsViewsTimes.views_ads_times_4`."""

    views_ads_times_5: typing.Optional[str] = Field(
        default=None,
    )
    """Property `AdsStatsViewsTimes.views_ads_times_5`."""

    views_ads_times_6: typing.Optional[int] = Field(
        default=None,
    )
    """Property `AdsStatsViewsTimes.views_ads_times_6`."""

    views_ads_times_7: typing.Optional[int] = Field(
        default=None,
    )
    """Property `AdsStatsViewsTimes.views_ads_times_7`."""

    views_ads_times_8: typing.Optional[int] = Field(
        default=None,
    )
    """Property `AdsStatsViewsTimes.views_ads_times_8`."""

    views_ads_times_9: typing.Optional[int] = Field(
        default=None,
    )
    """Property `AdsStatsViewsTimes.views_ads_times_9`."""

    views_ads_times_10: typing.Optional[int] = Field(
        default=None,
    )
    """Property `AdsStatsViewsTimes.views_ads_times_10`."""

    views_ads_times_11_plus: typing.Optional[int] = Field(
        default=None,
    )
    """Property `AdsStatsViewsTimes.views_ads_times_11_plus`."""


class AdsStories(BaseModel):
    """
    Model: `AdsStories`
    """

    stories: typing.Optional[typing.List["AdsStoryItem"]] = Field(
        default=None,
    )
    """Property `AdsStories.stories`."""

    owner: typing.Optional["AdsStoriesOwner"] = Field(
        default=None,
    )
    """Property `AdsStories.owner`."""

    stories_disclaimers_text: typing.Optional[str] = Field(
        default=None,
    )
    """Stories disclaimers text."""


class AdsStoriesOwner(BaseModel):
    """
    Model: `AdsStoriesOwner`
    """

    id: typing.Optional[typing.Union["int", "bool"]] = Field(
        default=None,
    )
    """Owner id."""

    href: typing.Optional[str] = Field(
        default=None,
    )
    """Href."""

    name: typing.Optional[str] = Field(
        default=None,
    )
    """Name."""

    photo: typing.Optional[str] = Field(
        default=None,
    )
    """Photo."""

    verify: typing.Optional[str] = Field(
        default=None,
    )
    """Verify."""

    gender: typing.Optional[str] = Field(
        default=None,
    )
    """Gender."""

    name_get: typing.Optional[str] = Field(
        default=None,
    )
    """Name get."""

    first_name: typing.Optional[str] = Field(
        default=None,
        alias="firstName",
    )
    """First name."""

    first_name_gen: typing.Optional[str] = Field(
        default=None,
    )
    """First name gen."""

    first_name_ins: typing.Optional[str] = Field(
        default=None,
    )
    """First name ins."""

    can_follow: typing.Optional[bool] = Field(
        default=None,
    )
    """Can follow."""


class AdsStoryItem(BaseModel):
    """
    Model: `AdsStoryItem`
    """

    id: typing.Optional[int] = Field(
        default=None,
    )
    """Story id."""

    owner_id: typing.Optional[int] = Field(
        default=None,
    )
    """Owner id."""

    raw_id: typing.Optional[str] = Field(
        default=None,
    )
    """Story raw id."""

    date: typing.Optional[str] = Field(
        default=None,
    )
    """Date."""

    time: typing.Optional[int] = Field(
        default=None,
    )
    """Time."""

    type: typing.Optional[str] = Field(
        default=None,
    )
    """Type."""

    unread: typing.Optional[bool] = Field(
        default=None,
    )
    """Is unread."""

    can_like: typing.Optional[bool] = Field(
        default=None,
        alias="canLike",
    )
    """Can like."""

    can_comment: typing.Optional[bool] = Field(
        default=None,
    )
    """Can comment."""

    can_share: typing.Optional[bool] = Field(
        default=None,
    )
    """Can share."""

    can_remove: typing.Optional[bool] = Field(
        default=None,
    )
    """Can remove."""

    can_manage: typing.Optional[bool] = Field(
        default=None,
    )
    """Can manage."""

    can_ask: typing.Optional[bool] = Field(
        default=None,
    )
    """Can ask."""

    can_ask_anonymous: typing.Optional[bool] = Field(
        default=None,
    )
    """Can ask anonymous."""

    is_profile_question: typing.Optional[bool] = Field(
        default=None,
        alias="isProfileQuestion",
    )
    """Is profile question."""

    stats: typing.Optional["AdsStoryItemStats"] = Field(
        default=None,
    )
    """Property `AdsStoryItem.stats`."""

    link: typing.Optional["AdsStoryItemLink"] = Field(
        default=None,
    )
    """Property `AdsStoryItem.link`."""

    photo_url: typing.Optional[str] = Field(
        default=None,
    )
    """Photo url."""

    preview_url: typing.Optional[str] = Field(
        default=None,
    )
    """Preview url."""

    track_code: typing.Optional[str] = Field(
        default=None,
    )
    """Track code."""

    is_part_of_narrative: typing.Optional[bool] = Field(
        default=None,
        alias="isPartOfNarrative",
    )
    """Is part of narrative."""

    is_ads: typing.Optional[bool] = Field(
        default=None,
        alias="isAds",
    )
    """Is ads."""

    video_url: typing.Optional[str] = Field(
        default=None,
    )
    """Video url."""

    first_frame: typing.Optional[str] = Field(
        default=None,
    )
    """First frame."""

    small_preview: typing.Optional[str] = Field(
        default=None,
    )
    """Small preview."""

    is_liked: typing.Optional[bool] = Field(
        default=None,
        alias="isLiked",
    )
    """Is liked."""


class AdsStoryItemLink(BaseModel):
    """
    Model: `AdsStoryItemLink`
    """

    key: typing.Optional[str] = Field(
        default=None,
    )
    """Key."""

    text: typing.Optional[str] = Field(
        default=None,
    )
    """Text."""

    url: typing.Optional[str] = Field(
        default=None,
    )
    """Url."""

    raw_url: typing.Optional[str] = Field(
        default=None,
    )
    """Raw url."""


class AdsStoryItemStats(BaseModel):
    """
    Model: `AdsStoryItemStats`
    """

    follow: typing.Optional["AdsStoryItemStatsFollow"] = Field(
        default=None,
    )
    """Property `AdsStoryItemStats.follow`."""

    url_view: typing.Optional["AdsStoryItemStatsUrlView"] = Field(
        default=None,
    )
    """Property `AdsStoryItemStats.url_view`."""


class AdsStoryItemStatsFollow(BaseModel):
    """
    Follow event stats
    Model: `AdsStoryItemStatsFollow`
    """

    event_type: typing.Optional[str] = Field(
        default=None,
    )
    """Event type."""

    rhash: typing.Optional[str] = Field(
        default=None,
    )
    """Event hash."""


class AdsStoryItemStatsUrlView(BaseModel):
    """
    Url view event stats
    Model: `AdsStoryItemStatsUrlView`
    """

    event_type: typing.Optional[str] = Field(
        default=None,
    )
    """Event type."""

    rhash: typing.Optional[str] = Field(
        default=None,
    )
    """Event hash."""


class AdsTargStats(BaseModel):
    """
    Model: `AdsTargStats`
    """

    audience_count: int = Field()
    """Audience."""

    recommended_cpc: typing.Optional[str] = Field(
        default=None,
    )
    """Recommended CPC value for 50% reach (old format)."""

    recommended_cpm: typing.Optional[str] = Field(
        default=None,
    )
    """Recommended CPM value for 50% reach (old format)."""

    recommended_cpc_50: typing.Optional[str] = Field(
        default=None,
    )
    """Recommended CPC value for 50% reach."""

    recommended_cpm_50: typing.Optional[str] = Field(
        default=None,
    )
    """Recommended CPM value for 50% reach."""

    recommended_cpc_70: typing.Optional[str] = Field(
        default=None,
    )
    """Recommended CPC value for 70% reach."""

    recommended_cpm_70: typing.Optional[str] = Field(
        default=None,
    )
    """Recommended CPM value for 70% reach."""

    recommended_cpc_90: typing.Optional[str] = Field(
        default=None,
    )
    """Recommended CPC value for 90% reach."""

    recommended_cpm_90: typing.Optional[str] = Field(
        default=None,
    )
    """Recommended CPM value for 90% reach."""

    total_alive_audience: typing.Optional[int] = Field(
        default=None,
    )
    """Total alive audience."""


class AdsTargSuggestions(BaseModel):
    """
    Model: `AdsTargSuggestions`
    """

    id: typing.Optional[int] = Field(
        default=None,
    )
    """Object ID."""

    name: typing.Optional[str] = Field(
        default=None,
    )
    """Object name."""

    type: typing.Optional[str] = Field(
        default=None,
    )
    """Object type."""

    parent: typing.Optional[str] = Field(
        default=None,
    )
    """Parent."""


class AdsTargSuggestionsCities(BaseModel):
    """
    Model: `AdsTargSuggestionsCities`
    """

    id: typing.Optional[int] = Field(
        default=None,
    )
    """Object ID."""

    name: typing.Optional[str] = Field(
        default=None,
    )
    """Object name."""

    parent: typing.Optional[str] = Field(
        default=None,
    )
    """Parent object."""


class AdsTargSuggestionsRegions(BaseModel):
    """
    Model: `AdsTargSuggestionsRegions`
    """

    id: typing.Optional[int] = Field(
        default=None,
    )
    """Object ID."""

    name: typing.Optional[str] = Field(
        default=None,
    )
    """Object name."""

    type: typing.Optional[str] = Field(
        default=None,
    )
    """Object type."""


class AdsTargSuggestionsSchools(BaseModel):
    """
    Model: `AdsTargSuggestionsSchools`
    """

    desc: typing.Optional[str] = Field(
        default=None,
    )
    """Full school title."""

    id: typing.Optional[int] = Field(
        default=None,
    )
    """School ID."""

    name: typing.Optional[str] = Field(
        default=None,
    )
    """School title."""

    parent: typing.Optional[str] = Field(
        default=None,
    )
    """City name."""

    type: typing.Optional["AdsTargSuggestionsSchoolsType"] = Field(
        default=None,
    )
    """Property `AdsTargSuggestionsSchools.type`."""


class AdsTargSuggestionsSchoolsType(str, enum.Enum, metaclass=BaseEnumMeta):
    SCHOOL = "school"
    UNIVERSITY = "university"
    FACULTY = "faculty"
    CHAIR = "chair"


class AdsTargetGroup(BaseModel):
    """
    Model: `AdsTargetGroup`
    """

    id: typing.Optional[int] = Field(
        default=None,
    )
    """Group ID."""

    name: typing.Optional[str] = Field(
        default=None,
    )
    """Group name."""

    is_audience: typing.Optional[bool] = Field(
        default=None,
    )
    """Is audience."""

    is_shared: typing.Optional[bool] = Field(
        default=None,
    )
    """Is shared."""

    file_source: typing.Optional[bool] = Field(
        default=None,
    )
    """File source."""

    api_source: typing.Optional[bool] = Field(
        default=None,
    )
    """API source."""

    lookalike_source: typing.Optional[bool] = Field(
        default=None,
    )
    """File source."""

    audience_count: typing.Optional[int] = Field(
        default=None,
    )
    """Audience."""

    domain: typing.Optional[str] = Field(
        default=None,
    )
    """Site domain."""

    lifetime: typing.Optional[int] = Field(
        default=None,
    )
    """Number of days for user to be in group."""

    pixel: typing.Optional[str] = Field(
        default=None,
    )
    """Pixel code."""

    target_pixel_id: typing.Optional[int] = Field(
        default=None,
    )
    """Target Pixel id."""

    target_pixel_rules: typing.Optional[typing.List["AdsTargetGroupTargetPixelRule"]] = Field(
        default=None,
    )
    """Target Pixel rules."""

    last_updated: typing.Optional[int] = Field(
        default=None,
    )
    """Last updated."""


class AdsTargetGroupTargetPixelRule(BaseModel):
    """
    Model: `AdsTargetGroupTargetPixelRule`
    """

    url_full_match: typing.Optional[str] = Field(
        default=None,
    )
    """Property `AdsTargetGroupTargetPixelRule.url_full_match`."""

    event_full_match: typing.Optional[str] = Field(
        default=None,
    )
    """Property `AdsTargetGroupTargetPixelRule.event_full_match`."""

    url_substrings_match: typing.Optional[typing.List[str]] = Field(
        default=None,
    )
    """Property `AdsTargetGroupTargetPixelRule.url_substrings_match`."""

    event_substrings_match: typing.Optional[typing.List[str]] = Field(
        default=None,
    )
    """Property `AdsTargetGroupTargetPixelRule.event_substrings_match`."""

    url_regex_match: typing.Optional[str] = Field(
        default=None,
    )
    """Property `AdsTargetGroupTargetPixelRule.url_regex_match`."""

    event_regex_match: typing.Optional[str] = Field(
        default=None,
    )
    """Property `AdsTargetGroupTargetPixelRule.event_regex_match`."""


class AdsTargetPixelInfo(BaseModel):
    """
    Model: `AdsTargetPixelInfo`
    """

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
    """
    Model: `AdsUpdateOfficeUsersResult`
    """

    user_id: int = Field()
    """Property `AdsUpdateOfficeUsersResult.user_id`."""

    is_success: bool = Field()
    """Property `AdsUpdateOfficeUsersResult.is_success`."""

    error: typing.Optional["BaseError"] = Field(
        default=None,
    )
    """Property `AdsUpdateOfficeUsersResult.error`."""


class AdsUpdateAdsStatus(BaseModel):
    """
    Model: `AdsUpdateAdsStatus`
    """

    id: int = Field()
    """Ad ID."""

    error_code: typing.Optional[int] = Field(
        default=None,
    )
    """Error code."""

    error_desc: typing.Optional[str] = Field(
        default=None,
    )
    """Error description."""


class AdsUpdateClientsStatus(BaseModel):
    """
    Model: `AdsUpdateClientsStatus`
    """

    id: int = Field()
    """Client ID."""

    error_code: typing.Optional[int] = Field(
        default=None,
    )
    """Error code."""

    error_desc: typing.Optional[str] = Field(
        default=None,
    )
    """Error description."""


class AdsUserSpecification(BaseModel):
    """
    Model: `AdsUserSpecification`
    """

    user_id: int = Field()
    """Property `AdsUserSpecification.user_id`."""

    role: "AdsAccessRolePublic" = Field()
    """Property `AdsUserSpecification.role`."""

    grant_access_to_all_clients: typing.Optional[bool] = Field(
        default=None,
    )
    """Property `AdsUserSpecification.grant_access_to_all_clients`."""

    client_ids: typing.Optional[typing.List[int]] = Field(
        default=None,
    )
    """Property `AdsUserSpecification.client_ids`."""

    view_budget: typing.Optional[bool] = Field(
        default=None,
    )
    """Property `AdsUserSpecification.view_budget`."""


class AdsUserSpecificationCutted(BaseModel):
    """
    Model: `AdsUserSpecificationCutted`
    """

    user_id: int = Field()
    """Property `AdsUserSpecificationCutted.user_id`."""

    role: "AdsAccessRolePublic" = Field()
    """Property `AdsUserSpecificationCutted.role`."""

    client_id: typing.Optional[int] = Field(
        default=None,
    )
    """Property `AdsUserSpecificationCutted.client_id`."""

    view_budget: typing.Optional[bool] = Field(
        default=None,
    )
    """Property `AdsUserSpecificationCutted.view_budget`."""


class AdsUsers(BaseModel):
    """
    Model: `AdsUsers`
    """

    accesses: typing.List["AdsAccesses"] = Field()
    """Property `AdsUsers.accesses`."""

    user_id: int = Field()
    """User ID."""


class AppWidgetsPhoto(BaseModel):
    """
    Model: `AppWidgetsPhoto`
    """

    id: str = Field()
    """Image ID."""

    images: typing.List["BaseImage"] = Field()
    """Property `AppWidgetsPhoto.images`."""


class AppWidgetsPhotos(BaseModel):
    """
    Model: `AppWidgetsPhotos`
    """

    count: typing.Optional[int] = Field(
        default=None,
    )
    """Property `AppWidgetsPhotos.count`."""

    items: typing.Optional[typing.List["AppWidgetsPhoto"]] = Field(
        default=None,
    )
    """Property `AppWidgetsPhotos.items`."""


class AppsAppFields(str, enum.Enum, metaclass=BaseEnumMeta):
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


class AppsAppLeaderboardType(int, enum.Enum, metaclass=BaseEnumMeta):
    NOT_SUPPORTED = 0
    LEVELS = 1
    POINTS = 2


class AppsAppMin(BaseModel):
    """
    Model: `AppsAppMin`
    """

    type: "AppsAppType" = Field()
    """Property `AppsAppMin.type`."""

    id: int = Field()
    """Application ID."""

    title: str = Field()
    """Application title."""

    author_owner_id: typing.Optional[int] = Field(
        default=None,
    )
    """Application author\'s ID."""

    is_installed: typing.Optional[bool] = Field(
        default=None,
    )
    """Is application installed."""

    icon_139: typing.Optional[str] = Field(
        default=None,
    )
    """URL of the app icon with 139 px in width."""

    icon_150: typing.Optional[str] = Field(
        default=None,
    )
    """URL of the app icon with 150 px in width."""

    icon_278: typing.Optional[str] = Field(
        default=None,
    )
    """URL of the app icon with 278 px in width."""

    icon_576: typing.Optional[str] = Field(
        default=None,
    )
    """URL of the app icon with 576 px in width."""

    background_loader_color: typing.Optional[str] = Field(
        default=None,
    )
    """Hex color code without hash sign."""

    loader_icon: typing.Optional[str] = Field(
        default=None,
    )
    """SVG data."""

    icon_75: typing.Optional[str] = Field(
        default=None,
    )
    """URL of the app icon with 75 px in width."""

    screen_orientation: typing.Optional[int] = Field(
        default=None,
    )
    """Screen orientation."""


class AppsAppType(str, enum.Enum, metaclass=BaseEnumMeta):
    APP = "app"
    GAME = "game"
    SITE = "site"
    STANDALONE = "standalone"
    VK_APP = "vk_app"
    COMMUNITY_APP = "community_app"
    HTML5_GAME = "html5_game"
    MINI_APP = "mini_app"


class AppsCatalogList(BaseModel):
    """
    Model: `AppsCatalogList`
    """

    count: int = Field()
    """Total number."""

    items: typing.List["AppsApp"] = Field()
    """Property `AppsCatalogList.items`."""

    profiles: typing.Optional[typing.List["UsersUserMin"]] = Field(
        default=None,
    )
    """Property `AppsCatalogList.profiles`."""


class AppsCustomSnippetButton(str, enum.Enum, metaclass=BaseEnumMeta):
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
    """
    Model: `AppsCustomSnippet`
    """

    vk_ref: typing.Optional[typing.List[typing.Literal["snippet_im", "snippet_post"]]] = Field(
        default=None,
    )
    """Property `AppsCustomSnippet.vk_ref`."""

    group_id: typing.Optional[typing.List[int]] = Field(
        default=None,
    )
    """Property `AppsCustomSnippet.group_id`."""

    hash: typing.Optional[typing.List[str]] = Field(
        default=None,
    )
    """Property `AppsCustomSnippet.hash`."""

    snippet_id: typing.Optional[int] = Field(
        default=None,
    )
    """Property `AppsCustomSnippet.snippet_id`."""

    title: typing.Optional[str] = Field(
        default=None,
    )
    """Property `AppsCustomSnippet.title`."""

    description: typing.Optional[str] = Field(
        default=None,
    )
    """Property `AppsCustomSnippet.description`."""

    expired_at: typing.Optional[int] = Field(
        default=None,
    )
    """Property `AppsCustomSnippet.expired_at`."""

    image_url: typing.Optional[str] = Field(
        default=None,
    )
    """Property `AppsCustomSnippet.image_url`."""

    small_image_url: typing.Optional[str] = Field(
        default=None,
    )
    """Property `AppsCustomSnippet.small_image_url`."""

    button: typing.Optional["AppsCustomSnippetButton"] = Field(
        default=None,
    )
    """Property `AppsCustomSnippet.button`."""


class AppsLeaderboard(BaseModel):
    """
    Model: `AppsLeaderboard`
    """

    user_id: int = Field()
    """User ID."""

    level: typing.Optional[int] = Field(
        default=None,
    )
    """Level."""

    points: typing.Optional[int] = Field(
        default=None,
    )
    """Points number."""

    score: typing.Optional[int] = Field(
        default=None,
    )
    """Score number."""


class AppsScopeName(str, enum.Enum, metaclass=BaseEnumMeta):
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
    """
    Scope description
    Model: `AppsScope`
    """

    name: "AppsScopeName" = Field()
    """Scope name."""

    title: typing.Optional[str] = Field(
        default=None,
    )
    """Scope title."""


class AppsTestingGroup(BaseModel):
    """
    Model: `AppsTestingGroup`
    """

    user_ids: typing.List[int] = Field()
    """Property `AppsTestingGroup.user_ids`."""

    group_id: int = Field()
    """Property `AppsTestingGroup.group_id`."""

    name: typing.Optional[str] = Field(
        default=None,
    )
    """Property `AppsTestingGroup.name`."""

    webview: typing.Optional[str] = Field(
        default=None,
    )
    """Property `AppsTestingGroup.webview`."""

    platforms: typing.Optional[typing.List[typing.Literal["mobile", "web", "mvk"]]] = Field(
        default=None,
    )
    """Property `AppsTestingGroup.platforms`."""


class AudioAudio(BaseModel):
    """
    Model: `AudioAudio`
    """

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

    access_key: typing.Optional[str] = Field(
        default=None,
    )
    """Access key for the audio."""

    url: typing.Optional[str] = Field(
        default=None,
    )
    """URL of mp3 file."""

    stream_duration: typing.Optional[int] = Field(
        default=None,
    )
    """Stream duration in seconds."""

    date: typing.Optional[int] = Field(
        default=None,
    )
    """Date when uploaded."""

    album_id: typing.Optional[int] = Field(
        default=None,
    )
    """Album ID."""

    performer: typing.Optional[str] = Field(
        default=None,
    )
    """Performer name."""

    file_size: typing.Optional[int] = Field(
        default=None,
    )
    """Примерный объем памяти занимаемый аудио на устройстве. Реализовано только для эпизодов подкастов."""


class BoardDefaultOrder(int, enum.Enum, metaclass=BaseEnumMeta):
    DESC_UPDATED = 1
    DESC_CREATED = 2
    ASC_UPDATED = -1
    ASC_CREATED = -2


class BoardTopic(BaseModel):
    """
    Model: `BoardTopic`
    """

    comments: typing.Optional[int] = Field(
        default=None,
    )
    """Comments number."""

    created: typing.Optional[int] = Field(
        default=None,
    )
    """Date when the topic has been created in Unixtime."""

    created_by: typing.Optional[int] = Field(
        default=None,
    )
    """Creator ID."""

    id: typing.Optional[int] = Field(
        default=None,
    )
    """Topic ID."""

    is_closed: typing.Optional[bool] = Field(
        default=None,
    )
    """Information whether the topic is closed."""

    is_fixed: typing.Optional[bool] = Field(
        default=None,
    )
    """Information whether the topic is fixed."""

    title: typing.Optional[str] = Field(
        default=None,
    )
    """Topic title."""

    updated: typing.Optional[int] = Field(
        default=None,
    )
    """Date when the topic has been updated in Unixtime."""

    updated_by: typing.Optional[int] = Field(
        default=None,
    )
    """ID of user who updated the topic."""

    first_comment: typing.Optional[str] = Field(
        default=None,
    )
    """First comment text."""

    last_comment: typing.Optional[str] = Field(
        default=None,
    )
    """Last comment text."""


class BoardTopicComment(BaseModel):
    """
    Model: `BoardTopicComment`
    """

    date: int = Field()
    """Date when the comment has been added in Unixtime."""

    from_id: int = Field()
    """Author ID."""

    id: int = Field()
    """Comment ID."""

    text: str = Field()
    """Comment text."""

    attachments: typing.Optional[typing.List["WallCommentAttachment"]] = Field(
        default=None,
    )
    """Property `BoardTopicComment.attachments`."""

    real_offset: typing.Optional[int] = Field(
        default=None,
    )
    """Real position of the comment."""

    can_edit: typing.Optional[bool] = Field(
        default=None,
    )
    """Information whether current user can edit the comment."""

    likes: typing.Optional["BaseLikesInfo"] = Field(
        default=None,
    )
    """Property `BoardTopicComment.likes`."""


class BugtrackerAddCompanyGroupsMembersError(BaseModel):
    """
    Model: `BugtrackerAddCompanyGroupsMembersError`
    """

    group_id: int = Field()
    """Property `BugtrackerAddCompanyGroupsMembersError.group_id`."""

    user_id: int = Field()
    """Property `BugtrackerAddCompanyGroupsMembersError.user_id`."""


class BugtrackerAttachmentType(str, enum.Enum, metaclass=BaseEnumMeta):
    PHOTO = "photo"
    DOC = "doc"


class BugtrackerAttachment(BaseModel):
    """
    Model: `BugtrackerAttachment`
    """

    type: "BugtrackerAttachmentType" = Field()
    """Property `BugtrackerAttachment.type`."""

    doc: typing.Optional["DocsDoc"] = Field(
        default=None,
    )
    """Property `BugtrackerAttachment.doc`."""

    photo: typing.Optional["PhotosPhoto"] = Field(
        default=None,
    )
    """Property `BugtrackerAttachment.photo`."""


class BugtrackerBugreport(BaseModel):
    """
    Model: `BugtrackerBugreport`
    """

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

    original_id: typing.Optional[int] = Field(
        default=None,
    )
    """Property `BugtrackerBugreport.original_id`."""

    clones_count: typing.Optional[int] = Field(
        default=None,
    )
    """Property `BugtrackerBugreport.clones_count`."""

    description: typing.Optional[str] = Field(
        default=None,
    )
    """Property `BugtrackerBugreport.description`."""

    state_actual: typing.Optional[str] = Field(
        default=None,
    )
    """Property `BugtrackerBugreport.state_actual`."""

    state_supposed: typing.Optional[str] = Field(
        default=None,
    )
    """Property `BugtrackerBugreport.state_supposed`."""

    phone: typing.Optional[str] = Field(
        default=None,
    )
    """Property `BugtrackerBugreport.phone`."""

    comments_count: typing.Optional[int] = Field(
        default=None,
    )
    """Property `BugtrackerBugreport.comments_count`."""

    can_remove: typing.Optional[bool] = Field(
        default=None,
    )
    """Property `BugtrackerBugreport.can_remove`."""

    can_change_status: typing.Optional[bool] = Field(
        default=None,
    )
    """Property `BugtrackerBugreport.can_change_status`."""

    can_bookmark: typing.Optional[bool] = Field(
        default=None,
    )
    """Property `BugtrackerBugreport.can_bookmark`."""

    is_bookmarked: typing.Optional[bool] = Field(
        default=None,
    )
    """Property `BugtrackerBugreport.is_bookmarked`."""

    can_edit: typing.Optional[bool] = Field(
        default=None,
    )
    """Property `BugtrackerBugreport.can_edit`."""

    can_export_to_trackers: typing.Optional[bool] = Field(
        default=None,
    )
    """Property `BugtrackerBugreport.can_export_to_trackers`."""

    can_export_to_csv: typing.Optional[bool] = Field(
        default=None,
    )
    """Property `BugtrackerBugreport.can_export_to_csv`."""

    can_add_moder_comment: typing.Optional[bool] = Field(
        default=None,
    )
    """Property `BugtrackerBugreport.can_add_moder_comment`."""

    can_add_hidden_comment: typing.Optional[bool] = Field(
        default=None,
    )
    """Property `BugtrackerBugreport.can_add_hidden_comment`."""

    can_view_history: typing.Optional[bool] = Field(
        default=None,
    )
    """Property `BugtrackerBugreport.can_view_history`."""

    is_deleted: typing.Optional[bool] = Field(
        default=None,
    )
    """Property `BugtrackerBugreport.is_deleted`."""

    can_restore: typing.Optional[bool] = Field(
        default=None,
    )
    """Property `BugtrackerBugreport.can_restore`."""

    is_vulnerability: typing.Optional[bool] = Field(
        default=None,
    )
    """Property `BugtrackerBugreport.is_vulnerability`."""

    is_severity_by_moderator: typing.Optional[bool] = Field(
        default=None,
    )
    """Property `BugtrackerBugreport.is_severity_by_moderator`."""

    hidden_docs: typing.Optional[bool] = Field(
        default=None,
    )
    """Property `BugtrackerBugreport.hidden_docs`."""

    is_confidential: typing.Optional[bool] = Field(
        default=None,
    )
    """Property `BugtrackerBugreport.is_confidential`."""

    private_comment: typing.Optional[str] = Field(
        default=None,
    )
    """Property `BugtrackerBugreport.private_comment`."""

    can_change_product: typing.Optional[bool] = Field(
        default=None,
    )
    """Property `BugtrackerBugreport.can_change_product`."""

    tournament_score: typing.Optional[int] = Field(
        default=None,
    )
    """Property `BugtrackerBugreport.tournament_score`."""

    moderator_user_id: typing.Optional[int] = Field(
        default=None,
    )
    """Property `BugtrackerBugreport.moderator_user_id`."""

    moderated: typing.Optional[int] = Field(
        default=None,
    )
    """Property `BugtrackerBugreport.moderated`."""

    screen_reader: typing.Optional[int] = Field(
        default=None,
    )
    """Property `BugtrackerBugreport.screen_reader`."""

    status_auto_update_ts: typing.Optional[int] = Field(
        default=None,
    )
    """Property `BugtrackerBugreport.status_auto_update_ts`."""

    status_auto_update_reason: typing.Optional[int] = Field(
        default=None,
    )
    """Property `BugtrackerBugreport.status_auto_update_reason`."""

    product_has_wishes: typing.Optional[bool] = Field(
        default=None,
    )
    """Property `BugtrackerBugreport.product_has_wishes`."""


class BugtrackerBugreportSubscribeState(BaseModel):
    """
    Model: `BugtrackerBugreportSubscribeState`
    """

    can_set_subscribe: bool = Field()
    """Property `BugtrackerBugreportSubscribeState.can_set_subscribe`."""

    is_subscribed: typing.Optional[bool] = Field(
        default=None,
    )
    """Property `BugtrackerBugreportSubscribeState.is_subscribed`."""

    set_subscribe_hash: typing.Optional[str] = Field(
        default=None,
    )
    """Property `BugtrackerBugreportSubscribeState.set_subscribe_hash`."""


class BugtrackerComment(BaseModel):
    """
    Model: `BugtrackerComment`
    """

    bugreport_id: int = Field()
    """Property `BugtrackerComment.bugreport_id`."""

    comment_id: int = Field()
    """Property `BugtrackerComment.comment_id`."""

    created: int = Field()
    """Property `BugtrackerComment.created`."""

    text: str = Field()
    """Property `BugtrackerComment.text`."""

    meta_text: typing.Optional[str] = Field(
        default=None,
    )
    """Property `BugtrackerComment.meta_text`."""

    from_id: typing.Optional[int] = Field(
        default=None,
    )
    """Property `BugtrackerComment.from_id`."""

    author_name: typing.Optional[str] = Field(
        default=None,
    )
    """Property `BugtrackerComment.author_name`."""

    author_photo: typing.Optional[str] = Field(
        default=None,
    )
    """Property `BugtrackerComment.author_photo`."""

    can_edit: typing.Optional[bool] = Field(
        default=None,
    )
    """Property `BugtrackerComment.can_edit`."""

    can_remove: typing.Optional[bool] = Field(
        default=None,
    )
    """Property `BugtrackerComment.can_remove`."""

    is_hidden: typing.Optional[bool] = Field(
        default=None,
    )
    """Property `BugtrackerComment.is_hidden`."""

    attachments: typing.Optional[typing.List["BugtrackerAttachment"]] = Field(
        default=None,
    )
    """Property `BugtrackerComment.attachments`."""

    is_unread: typing.Optional[bool] = Field(
        default=None,
    )
    """Property `BugtrackerComment.is_unread`."""

    author: typing.Optional["BugtrackerCommentAuthor"] = Field(
        default=None,
    )
    """Property `BugtrackerComment.author`."""

    is_attachments_hidden: typing.Optional[bool] = Field(
        default=None,
    )
    """Property `BugtrackerComment.is_attachments_hidden`."""


class BugtrackerCommentAuthor(BaseModel):
    """
    Model: `BugtrackerCommentAuthor`
    """

    author_id: typing.Optional[int] = Field(
        default=None,
    )
    """Property `BugtrackerCommentAuthor.author_id`."""

    name: typing.Optional[str] = Field(
        default=None,
    )
    """Property `BugtrackerCommentAuthor.name`."""

    photo: typing.Optional[str] = Field(
        default=None,
    )
    """Property `BugtrackerCommentAuthor.photo`."""

    moder_name: typing.Optional[str] = Field(
        default=None,
    )
    """Property `BugtrackerCommentAuthor.moder_name`."""

    moder_number: typing.Optional[int] = Field(
        default=None,
    )
    """Property `BugtrackerCommentAuthor.moder_number`."""

    link: typing.Optional[str] = Field(
        default=None,
    )
    """Property `BugtrackerCommentAuthor.link`."""


class BugtrackerCompanyMember(BaseModel):
    """
    Model: `BugtrackerCompanyMember`
    """

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

    groups: typing.Optional[typing.List[int]] = Field(
        default=None,
    )
    """Property `BugtrackerCompanyMember.groups`."""

    products: typing.Optional[typing.List["BugtrackerCompanyMemberProduct"]] = Field(
        default=None,
    )
    """Property `BugtrackerCompanyMember.products`."""


class BugtrackerCompanyMemberProduct(BaseModel):
    """
    Model: `BugtrackerCompanyMemberProduct`
    """

    id: int = Field()
    """Property `BugtrackerCompanyMemberProduct.id`."""

    access: int = Field()
    """Property `BugtrackerCompanyMemberProduct.access`."""

    status: int = Field()
    """Property `BugtrackerCompanyMemberProduct.status`."""

    title: typing.Optional[str] = Field(
        default=None,
    )
    """Property `BugtrackerCompanyMemberProduct.title`."""

    photo_url: typing.Optional[str] = Field(
        default=None,
    )
    """Property `BugtrackerCompanyMemberProduct.photo_url`."""

    licence_status_text: typing.Optional[str] = Field(
        default=None,
    )
    """Property `BugtrackerCompanyMemberProduct.licence_status_text`."""


class CallbackAppPayload(BaseModel):
    """
    Model: `CallbackAppPayload`
    """

    user_id: int = Field()
    """Property `CallbackAppPayload.user_id`."""

    app_id: int = Field()
    """Property `CallbackAppPayload.app_id`."""

    payload: str = Field()
    """Property `CallbackAppPayload.payload`."""


class CallbackAudioNew(BaseModel):
    """
    Model: `CallbackAudioNew`
    """

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

    access_key: typing.Optional[str] = Field(
        default=None,
    )
    """Access key for the audio."""

    url: typing.Optional[str] = Field(
        default=None,
    )
    """URL of mp3 file."""

    stream_duration: typing.Optional[int] = Field(
        default=None,
    )
    """Stream duration in seconds."""

    date: typing.Optional[int] = Field(
        default=None,
    )
    """Date when uploaded."""

    album_id: typing.Optional[int] = Field(
        default=None,
    )
    """Album ID."""

    performer: typing.Optional[str] = Field(
        default=None,
    )
    """Performer name."""

    file_size: typing.Optional[int] = Field(
        default=None,
    )
    """Примерный объем памяти занимаемый аудио на устройстве. Реализовано только для эпизодов подкастов."""


class CallbackBase(BaseModel):
    """
    Model: `CallbackBase`
    """

    type: "CallbackType" = Field()
    """Property `CallbackBase.type`."""

    group_id: int = Field()
    """Property `CallbackBase.group_id`."""

    event_id: str = Field()
    """Unique event id. If it passed twice or more - you should ignore it.."""

    v: str = Field()
    """API object version."""

    secret: typing.Optional[str] = Field(
        default=None,
    )
    """Property `CallbackBase.secret`."""


class CallbackBoardPostDelete(BaseModel):
    """
    Model: `CallbackBoardPostDelete`
    """

    topic_owner_id: int = Field()
    """Property `CallbackBoardPostDelete.topic_owner_id`."""

    topic_id: int = Field()
    """Property `CallbackBoardPostDelete.topic_id`."""

    id: int = Field()
    """Property `CallbackBoardPostDelete.id`."""

    deleter_id: typing.Optional[int] = Field(
        default=None,
    )
    """Property `CallbackBoardPostDelete.deleter_id`."""


class CallbackBoardPostEdit(BaseModel):
    """
    Model: `CallbackBoardPostEdit`
    """

    date: int = Field()
    """Date when the comment has been added in Unixtime."""

    from_id: int = Field()
    """Author ID."""

    id: int = Field()
    """Comment ID."""

    text: str = Field()
    """Comment text."""

    attachments: typing.Optional[typing.List["WallCommentAttachment"]] = Field(
        default=None,
    )
    """Property `CallbackBoardPostEdit.attachments`."""

    real_offset: typing.Optional[int] = Field(
        default=None,
    )
    """Real position of the comment."""

    can_edit: typing.Optional[bool] = Field(
        default=None,
    )
    """Information whether current user can edit the comment."""

    likes: typing.Optional["BaseLikesInfo"] = Field(
        default=None,
    )
    """Property `CallbackBoardPostEdit.likes`."""


class CallbackBoardPostNew(BaseModel):
    """
    Model: `CallbackBoardPostNew`
    """

    date: int = Field()
    """Date when the comment has been added in Unixtime."""

    from_id: int = Field()
    """Author ID."""

    id: int = Field()
    """Comment ID."""

    text: str = Field()
    """Comment text."""

    attachments: typing.Optional[typing.List["WallCommentAttachment"]] = Field(
        default=None,
    )
    """Property `CallbackBoardPostNew.attachments`."""

    real_offset: typing.Optional[int] = Field(
        default=None,
    )
    """Real position of the comment."""

    can_edit: typing.Optional[bool] = Field(
        default=None,
    )
    """Information whether current user can edit the comment."""

    likes: typing.Optional["BaseLikesInfo"] = Field(
        default=None,
    )
    """Property `CallbackBoardPostNew.likes`."""


class CallbackBoardPostRestore(BaseModel):
    """
    Model: `CallbackBoardPostRestore`
    """

    date: int = Field()
    """Date when the comment has been added in Unixtime."""

    from_id: int = Field()
    """Author ID."""

    id: int = Field()
    """Comment ID."""

    text: str = Field()
    """Comment text."""

    attachments: typing.Optional[typing.List["WallCommentAttachment"]] = Field(
        default=None,
    )
    """Property `CallbackBoardPostRestore.attachments`."""

    real_offset: typing.Optional[int] = Field(
        default=None,
    )
    """Real position of the comment."""

    can_edit: typing.Optional[bool] = Field(
        default=None,
    )
    """Information whether current user can edit the comment."""

    likes: typing.Optional["BaseLikesInfo"] = Field(
        default=None,
    )
    """Property `CallbackBoardPostRestore.likes`."""


class CallbackDonutMoneyWithdraw(BaseModel):
    """
    Model: `CallbackDonutMoneyWithdraw`
    """

    amount: float = Field()
    """Property `CallbackDonutMoneyWithdraw.amount`."""

    amount_without_fee: float = Field()
    """Property `CallbackDonutMoneyWithdraw.amount_without_fee`."""


class CallbackDonutMoneyWithdrawError(BaseModel):
    """
    Model: `CallbackDonutMoneyWithdrawError`
    """

    reason: str = Field()
    """Property `CallbackDonutMoneyWithdrawError.reason`."""


class CallbackDonutSubscriptionCancelled(BaseModel):
    """
    Model: `CallbackDonutSubscriptionCancelled`
    """

    user_id: typing.Optional[int] = Field(
        default=None,
    )
    """Property `CallbackDonutSubscriptionCancelled.user_id`."""


class CallbackDonutSubscriptionCreate(BaseModel):
    """
    Model: `CallbackDonutSubscriptionCreate`
    """

    amount: int = Field()
    """Property `CallbackDonutSubscriptionCreate.amount`."""

    amount_without_fee: float = Field()
    """Property `CallbackDonutSubscriptionCreate.amount_without_fee`."""

    user_id: typing.Optional[int] = Field(
        default=None,
    )
    """Property `CallbackDonutSubscriptionCreate.user_id`."""


class CallbackDonutSubscriptionExpired(BaseModel):
    """
    Model: `CallbackDonutSubscriptionExpired`
    """

    user_id: typing.Optional[int] = Field(
        default=None,
    )
    """Property `CallbackDonutSubscriptionExpired.user_id`."""


class CallbackDonutSubscriptionPriceChanged(BaseModel):
    """
    Model: `CallbackDonutSubscriptionPriceChanged`
    """

    amount_old: int = Field()
    """Property `CallbackDonutSubscriptionPriceChanged.amount_old`."""

    amount_new: int = Field()
    """Property `CallbackDonutSubscriptionPriceChanged.amount_new`."""

    user_id: typing.Optional[int] = Field(
        default=None,
    )
    """Property `CallbackDonutSubscriptionPriceChanged.user_id`."""

    amount_diff: typing.Optional[float] = Field(
        default=None,
    )
    """Property `CallbackDonutSubscriptionPriceChanged.amount_diff`."""

    amount_diff_without_fee: typing.Optional[float] = Field(
        default=None,
    )
    """Property `CallbackDonutSubscriptionPriceChanged.amount_diff_without_fee`."""


class CallbackDonutSubscriptionProlonged(BaseModel):
    """
    Model: `CallbackDonutSubscriptionProlonged`
    """

    amount: int = Field()
    """Property `CallbackDonutSubscriptionProlonged.amount`."""

    amount_without_fee: float = Field()
    """Property `CallbackDonutSubscriptionProlonged.amount_without_fee`."""

    user_id: typing.Optional[int] = Field(
        default=None,
    )
    """Property `CallbackDonutSubscriptionProlonged.user_id`."""


CallbackFwdMessages: typing.TypeAlias = typing.List[typing.List["CallbackForeignMessage"]]


class CallbackGroupChangePhoto(BaseModel):
    """
    Model: `CallbackGroupChangePhoto`
    """

    user_id: int = Field()
    """Property `CallbackGroupChangePhoto.user_id`."""

    photo: "PhotosPhoto" = Field()
    """Property `CallbackGroupChangePhoto.photo`."""


class CallbackGroupChangeSettings(BaseModel):
    """
    Model: `CallbackGroupChangeSettings`
    """

    user_id: int = Field()
    """Property `CallbackGroupChangeSettings.user_id`."""

    changes: typing.Optional["CallbackGroupSettingsChanges"] = Field(
        default=None,
    )
    """Property `CallbackGroupChangeSettings.changes`."""


class CallbackGroupJoin(BaseModel):
    """
    Model: `CallbackGroupJoin`
    """

    user_id: int = Field()
    """Property `CallbackGroupJoin.user_id`."""

    join_type: "CallbackGroupJoinType" = Field()
    """Property `CallbackGroupJoin.join_type`."""


class CallbackGroupJoinType(str, enum.Enum, metaclass=BaseEnumMeta):
    JOIN = "join"
    UNSURE = "unsure"
    ACCEPTED = "accepted"
    APPROVED = "approved"
    REQUEST = "request"


class CallbackGroupLeave(BaseModel):
    """
    Model: `CallbackGroupLeave`
    """

    user_id: typing.Optional[int] = Field(
        default=None,
    )
    """Property `CallbackGroupLeave.user_id`."""

    self: typing.Optional[bool] = Field(
        default=None,
    )
    """Property `CallbackGroupLeave.self`."""


class CallbackGroupMarket(int, enum.Enum, metaclass=BaseEnumMeta):
    DISABLED = 0
    OPEN = 1


class CallbackGroupOfficerRole(int, enum.Enum, metaclass=BaseEnumMeta):
    NONE = 0
    MODERATOR = 1
    EDITOR = 2
    ADMINISTRATOR = 3


class CallbackGroupOfficersEdit(BaseModel):
    """
    Model: `CallbackGroupOfficersEdit`
    """

    admin_id: int = Field()
    """Property `CallbackGroupOfficersEdit.admin_id`."""

    user_id: int = Field()
    """Property `CallbackGroupOfficersEdit.user_id`."""

    level_old: "CallbackGroupOfficerRole" = Field()
    """Property `CallbackGroupOfficersEdit.level_old`."""

    level_new: "CallbackGroupOfficerRole" = Field()
    """Property `CallbackGroupOfficersEdit.level_new`."""


class CallbackGroupSettingsChanges(BaseModel):
    """
    Model: `CallbackGroupSettingsChanges`
    """

    title: typing.Optional["CallbackGroupSettingsChangesStringValues"] = Field(
        default=None,
    )
    """Property `CallbackGroupSettingsChanges.title`."""

    screen_name: typing.Optional["CallbackGroupSettingsChangesStringValues"] = Field(
        default=None,
    )
    """Property `CallbackGroupSettingsChanges.screen_name`."""

    event_start_date: typing.Optional["CallbackGroupSettingsChangesIntegerValues"] = Field(
        default=None,
    )
    """Property `CallbackGroupSettingsChanges.event_start_date`."""

    event_finish_date: typing.Optional["CallbackGroupSettingsChangesIntegerValues"] = Field(
        default=None,
    )
    """Property `CallbackGroupSettingsChanges.event_finish_date`."""

    event_group_id: typing.Optional["CallbackGroupSettingsChangesIntegerValues"] = Field(
        default=None,
    )
    """Property `CallbackGroupSettingsChanges.event_group_id`."""

    donations: typing.Optional["CallbackGroupSettingsChangesIntegerValues"] = Field(
        default=None,
    )
    """Property `CallbackGroupSettingsChanges.donations`."""

    wall: typing.Optional["CallbackGroupSettingsChangesIntegerValues"] = Field(
        default=None,
    )
    """Property `CallbackGroupSettingsChanges.wall`."""

    replies: typing.Optional["CallbackGroupSettingsChangesIntegerValues"] = Field(
        default=None,
    )
    """Property `CallbackGroupSettingsChanges.replies`."""

    topics: typing.Optional["CallbackGroupSettingsChangesIntegerValues"] = Field(
        default=None,
    )
    """Property `CallbackGroupSettingsChanges.topics`."""

    photos: typing.Optional["CallbackGroupSettingsChangesIntegerValues"] = Field(
        default=None,
    )
    """Property `CallbackGroupSettingsChanges.photos`."""

    docs: typing.Optional["CallbackGroupSettingsChangesIntegerValues"] = Field(
        default=None,
    )
    """Property `CallbackGroupSettingsChanges.docs`."""

    messages: typing.Optional["CallbackGroupSettingsChangesIntegerValues"] = Field(
        default=None,
    )
    """Property `CallbackGroupSettingsChanges.messages`."""

    market: typing.Optional["CallbackGroupSettingsChangesIntegerValues"] = Field(
        default=None,
    )
    """Property `CallbackGroupSettingsChanges.market`."""

    market_wiki: typing.Optional["CallbackGroupSettingsChangesIntegerValues"] = Field(
        default=None,
    )
    """Property `CallbackGroupSettingsChanges.market_wiki`."""

    board: typing.Optional["CallbackGroupSettingsChangesIntegerValues"] = Field(
        default=None,
    )
    """Property `CallbackGroupSettingsChanges.board`."""

    links: typing.Optional["CallbackGroupSettingsChangesIntegerValues"] = Field(
        default=None,
    )
    """Property `CallbackGroupSettingsChanges.links`."""

    audio: typing.Optional["CallbackGroupSettingsChangesIntegerValues"] = Field(
        default=None,
    )
    """Property `CallbackGroupSettingsChanges.audio`."""

    video: typing.Optional["CallbackGroupSettingsChangesIntegerValues"] = Field(
        default=None,
    )
    """Property `CallbackGroupSettingsChanges.video`."""

    can_post_topics: typing.Optional["CallbackGroupSettingsChangesIntegerValues"] = Field(
        default=None,
    )
    """Property `CallbackGroupSettingsChanges.can_post_topics`."""

    can_post_albums: typing.Optional["CallbackGroupSettingsChangesIntegerValues"] = Field(
        default=None,
    )
    """Property `CallbackGroupSettingsChanges.can_post_albums`."""

    can_post_video: typing.Optional["CallbackGroupSettingsChangesIntegerValues"] = Field(
        default=None,
    )
    """Property `CallbackGroupSettingsChanges.can_post_video`."""

    disable_market_comments: typing.Optional["CallbackGroupSettingsChangesIntegerValues"] = Field(
        default=None,
    )
    """Property `CallbackGroupSettingsChanges.disable_market_comments`."""

    status_default: typing.Optional["CallbackGroupSettingsChangesIntegerValues"] = Field(
        default=None,
    )
    """Property `CallbackGroupSettingsChanges.status_default`."""

    access: typing.Optional["CallbackGroupSettingsChangesIntegerValues"] = Field(
        default=None,
    )
    """Property `CallbackGroupSettingsChanges.access`."""

    email: typing.Optional["CallbackGroupSettingsChangesStringValues"] = Field(
        default=None,
    )
    """Property `CallbackGroupSettingsChanges.email`."""

    country_id: typing.Optional["CallbackGroupSettingsChangesIntegerValues"] = Field(
        default=None,
    )
    """Property `CallbackGroupSettingsChanges.country_id`."""

    city_id: typing.Optional["CallbackGroupSettingsChangesIntegerValues"] = Field(
        default=None,
    )
    """Property `CallbackGroupSettingsChanges.city_id`."""

    address: typing.Optional["CallbackGroupSettingsChangesStringValues"] = Field(
        default=None,
    )
    """Property `CallbackGroupSettingsChanges.address`."""

    description: typing.Optional["CallbackGroupSettingsChangesStringValues"] = Field(
        default=None,
    )
    """Property `CallbackGroupSettingsChanges.description`."""

    website: typing.Optional["CallbackGroupSettingsChangesStringValues"] = Field(
        default=None,
    )
    """Property `CallbackGroupSettingsChanges.website`."""

    phone: typing.Optional["CallbackGroupSettingsChangesStringValues"] = Field(
        default=None,
    )
    """Property `CallbackGroupSettingsChanges.phone`."""

    age_limits: typing.Optional["CallbackGroupSettingsChangesIntegerValues"] = Field(
        default=None,
    )
    """Property `CallbackGroupSettingsChanges.age_limits`."""

    category_v2: typing.Optional["CallbackGroupSettingsChangesIntegerValues"] = Field(
        default=None,
    )
    """Property `CallbackGroupSettingsChanges.category_v2`."""

    public_category: typing.Optional["CallbackGroupSettingsChangesIntegerValues"] = Field(
        default=None,
    )
    """Property `CallbackGroupSettingsChanges.public_category`."""

    public_subcategory: typing.Optional["CallbackGroupSettingsChangesIntegerValues"] = Field(
        default=None,
    )
    """Property `CallbackGroupSettingsChanges.public_subcategory`."""


class CallbackGroupSettingsChangesIntegerValues(BaseModel):
    """
    Model: `CallbackGroupSettingsChangesIntegerValues`
    """

    old_value: typing.Optional[int] = Field(
        default=None,
    )
    """Property `CallbackGroupSettingsChangesIntegerValues.old_value`."""

    new_value: typing.Optional[int] = Field(
        default=None,
    )
    """Property `CallbackGroupSettingsChangesIntegerValues.new_value`."""


class CallbackGroupSettingsChangesStringValues(BaseModel):
    """
    Model: `CallbackGroupSettingsChangesStringValues`
    """

    old_value: typing.Optional[str] = Field(
        default=None,
    )
    """Property `CallbackGroupSettingsChangesStringValues.old_value`."""

    new_value: typing.Optional[str] = Field(
        default=None,
    )
    """Property `CallbackGroupSettingsChangesStringValues.new_value`."""


class CallbackInfoForBots(BaseModel):
    """
    Model: `CallbackInfoForBots`
    """

    button_actions: typing.Optional[typing.List["MessagesTemplateActionTypeNames"]] = Field(
        default=None,
    )
    """Property `CallbackInfoForBots.button_actions`."""

    keyboard: typing.Optional[bool] = Field(
        default=None,
    )
    """client has support keyboard."""

    inline_keyboard: typing.Optional[bool] = Field(
        default=None,
    )
    """client has support inline keyboard."""

    carousel: typing.Optional[bool] = Field(
        default=None,
    )
    """client has support carousel."""

    lang_id: typing.Optional[int] = Field(
        default=None,
    )
    """client or user language id."""


class CallbackLikeAddRemoveObjectType(str, enum.Enum, metaclass=BaseEnumMeta):
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
    """
    Model: `CallbackLikeAddRemove`
    """

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

    thread_reply_id: typing.Optional[int] = Field(
        default=None,
    )
    """Property `CallbackLikeAddRemove.thread_reply_id`."""


class CallbackMarketComment(BaseModel):
    """
    Model: `CallbackMarketComment`
    """

    id: int = Field()
    """Property `CallbackMarketComment.id`."""

    from_id: int = Field()
    """Property `CallbackMarketComment.from_id`."""

    date: int = Field()
    """Property `CallbackMarketComment.date`."""

    text: typing.Optional[str] = Field(
        default=None,
    )
    """Property `CallbackMarketComment.text`."""

    market_owner_id: typing.Optional[int] = Field(
        default=None,
    )
    """Property `CallbackMarketComment.market_owner_id`."""

    photo_id: typing.Optional[int] = Field(
        default=None,
    )
    """Property `CallbackMarketComment.photo_id`."""


class CallbackMarketCommentDelete(BaseModel):
    """
    Model: `CallbackMarketCommentDelete`
    """

    owner_id: int = Field()
    """Property `CallbackMarketCommentDelete.owner_id`."""

    id: int = Field()
    """Property `CallbackMarketCommentDelete.id`."""

    user_id: int = Field()
    """Property `CallbackMarketCommentDelete.user_id`."""

    item_id: int = Field()
    """Property `CallbackMarketCommentDelete.item_id`."""


class CallbackMessageAllow(BaseModel):
    """
    Model: `CallbackMessageAllow`
    """

    user_id: int = Field()
    """Property `CallbackMessageAllow.user_id`."""

    key: str = Field()
    """Property `CallbackMessageAllow.key`."""


class CallbackMessageDeny(BaseModel):
    """
    Model: `CallbackMessageDeny`
    """

    user_id: int = Field()
    """Property `CallbackMessageDeny.user_id`."""


class CallbackMessageEvent(BaseModel):
    """
    Model: `CallbackMessageEvent`
    """

    user_id: int = Field()
    """Property `CallbackMessageEvent.user_id`."""

    peer_id: int = Field()
    """Property `CallbackMessageEvent.peer_id`."""

    event_id: str = Field()
    """Property `CallbackMessageEvent.event_id`."""

    payload: str = Field()
    """Property `CallbackMessageEvent.payload`."""

    conversation_message_id: typing.Optional[int] = Field(
        default=None,
    )
    """Property `CallbackMessageEvent.conversation_message_id`."""


class CallbackMessageNew(BaseModel):
    """
    Model: `CallbackMessageNew`
    """

    client_info: typing.Optional["CallbackInfoForBots"] = Field(
        default=None,
    )
    """Property `CallbackMessageNew.client_info`."""

    message: typing.Optional["CallbackMessage"] = Field(
        default=None,
    )
    """Property `CallbackMessageNew.message`."""


class CallbackMessageObject(BaseModel):
    """
    Model: `CallbackMessageObject`
    """

    client_info: typing.Optional["CallbackInfoForBots"] = Field(
        default=None,
    )
    """Property `CallbackMessageObject.client_info`."""

    message: typing.Optional["CallbackMessage"] = Field(
        default=None,
    )
    """Property `CallbackMessageObject.message`."""


class CallbackMessageReactionEvent(BaseModel):
    """
    Model: `CallbackMessageReactionEvent`
    """

    reacted_id: int = Field()
    """Property `CallbackMessageReactionEvent.reacted_id`."""

    peer_id: int = Field()
    """Property `CallbackMessageReactionEvent.peer_id`."""

    cmid: int = Field()
    """Property `CallbackMessageReactionEvent.cmid`."""

    reaction_id: typing.Optional[int] = Field(
        default=None,
    )
    """Property `CallbackMessageReactionEvent.reaction_id`."""


class CallbackMessageRead(BaseModel):
    """
    Model: `CallbackMessageRead`
    """

    from_id: int = Field()
    """Property `CallbackMessageRead.from_id`."""

    peer_id: int = Field()
    """Property `CallbackMessageRead.peer_id`."""

    read_message_id: int = Field()
    """Property `CallbackMessageRead.read_message_id`."""

    conversation_message_id: int = Field()
    """Property `CallbackMessageRead.conversation_message_id`."""


class CallbackMessageTypingStateState(str, enum.Enum, metaclass=BaseEnumMeta):
    MESSAGE_TYPING_STATE = "message_typing_state"
    f__0 = "0"
    f__1 = "1"
    f__2 = "2"
    f__3 = "3"
    f__4 = "4"
    f__5 = "5"


class CallbackMessageTypingState(BaseModel):
    """
    Model: `CallbackMessageTypingState`
    """

    from_id: int = Field()
    """Property `CallbackMessageTypingState.from_id`."""

    to_id: int = Field()
    """Property `CallbackMessageTypingState.to_id`."""

    state: "CallbackMessageTypingStateState" = Field()
    """Property `CallbackMessageTypingState.state`."""


class CallbackPhotoCommentDelete(BaseModel):
    """
    Model: `CallbackPhotoCommentDelete`
    """

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


class CallbackPhotoNewVerticalAlign(str, enum.Enum, metaclass=BaseEnumMeta):
    TOP = "top"
    MIDDLE = "middle"
    BOTTOM = "bottom"


class CallbackPhotoNew(BaseModel):
    """
    Model: `CallbackPhotoNew`
    """

    album_id: int = Field()
    """Album ID."""

    date: int = Field()
    """Date when uploaded."""

    id: int = Field()
    """Photo ID."""

    owner_id: int = Field()
    """Photo owner\'s ID."""

    has_tags: bool = Field()
    """Whether photo has attached tag links."""

    access_key: typing.Optional[str] = Field(
        default=None,
    )
    """Access key for the photo."""

    height: typing.Optional[int] = Field(
        default=None,
    )
    """Original photo height."""

    images: typing.Optional[typing.List["PhotosImage"]] = Field(
        default=None,
    )
    """Property `CallbackPhotoNew.images`."""

    lat: typing.Optional[float] = Field(
        default=None,
    )
    """Latitude."""

    long: typing.Optional[float] = Field(
        default=None,
    )
    """Longitude."""

    photo_256: typing.Optional[str] = Field(
        default=None,
    )
    """URL of image with 2560 px width."""

    thumb_hash: typing.Optional[str] = Field(
        default=None,
    )
    """Thumb Hash."""

    can_comment: typing.Optional[bool] = Field(
        default=None,
    )
    """Information whether current user can comment the photo."""

    place: typing.Optional[str] = Field(
        default=None,
    )
    """Property `CallbackPhotoNew.place`."""

    post_id: typing.Optional[int] = Field(
        default=None,
    )
    """Post ID."""

    sizes: typing.Optional[typing.List["PhotosPhotoSizes"]] = Field(
        default=None,
    )
    """Property `CallbackPhotoNew.sizes`."""

    square_crop: typing.Optional[str] = Field(
        default=None,
    )
    """Property `CallbackPhotoNew.square_crop`."""

    text: typing.Optional[str] = Field(
        default=None,
    )
    """Photo caption."""

    user_id: typing.Optional[int] = Field(
        default=None,
    )
    """ID of the user who have uploaded the photo."""

    width: typing.Optional[int] = Field(
        default=None,
    )
    """Original photo width."""

    likes: typing.Optional["BaseLikes"] = Field(
        default=None,
    )
    """Property `CallbackPhotoNew.likes`."""

    comments: typing.Optional["BaseObjectCount"] = Field(
        default=None,
    )
    """Property `CallbackPhotoNew.comments`."""

    reposts: typing.Optional["BaseRepostsInfo"] = Field(
        default=None,
    )
    """Property `CallbackPhotoNew.reposts`."""

    tags: typing.Optional["BaseObjectCount"] = Field(
        default=None,
    )
    """Property `CallbackPhotoNew.tags`."""

    hidden: typing.Optional["BasePropertyExists"] = Field(
        default=None,
    )
    """Returns if the photo is hidden above the wall."""

    real_offset: typing.Optional[int] = Field(
        default=None,
    )
    """Real position of the photo."""

    vertical_align: typing.Optional["CallbackPhotoNewVerticalAlign"] = Field(
        default=None,
    )
    """Sets vertical alignment of a photo."""


class CallbackPollVoteNew(BaseModel):
    """
    Model: `CallbackPollVoteNew`
    """

    owner_id: int = Field()
    """Property `CallbackPollVoteNew.owner_id`."""

    poll_id: int = Field()
    """Property `CallbackPollVoteNew.poll_id`."""

    option_id: int = Field()
    """Property `CallbackPollVoteNew.option_id`."""

    user_id: int = Field()
    """Property `CallbackPollVoteNew.user_id`."""


class CallbackType(str, enum.Enum, metaclass=BaseEnumMeta):
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
    """
    Model: `CallbackUserBlock`
    """

    admin_id: int = Field()
    """Property `CallbackUserBlock.admin_id`."""

    user_id: int = Field()
    """Property `CallbackUserBlock.user_id`."""

    unblock_date: int = Field()
    """Property `CallbackUserBlock.unblock_date`."""

    reason: int = Field()
    """Property `CallbackUserBlock.reason`."""

    comment: typing.Optional[str] = Field(
        default=None,
    )
    """Property `CallbackUserBlock.comment`."""


class CallbackUserUnblock(BaseModel):
    """
    Model: `CallbackUserUnblock`
    """

    admin_id: int = Field()
    """Property `CallbackUserUnblock.admin_id`."""

    user_id: int = Field()
    """Property `CallbackUserUnblock.user_id`."""

    by_end_date: int = Field()
    """Property `CallbackUserUnblock.by_end_date`."""


class CallbackVideoCommentDelete(BaseModel):
    """
    Model: `CallbackVideoCommentDelete`
    """

    id: int = Field()
    """Property `CallbackVideoCommentDelete.id`."""

    owner_id: int = Field()
    """Property `CallbackVideoCommentDelete.owner_id`."""

    deleter_id: int = Field()
    """Property `CallbackVideoCommentDelete.deleter_id`."""

    video_id: int = Field()
    """Property `CallbackVideoCommentDelete.video_id`."""


class CallbackVideoNew(BaseModel):
    """
    Model: `CallbackVideoNew`
    """

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

    access_key: typing.Optional[str] = Field(
        default=None,
    )
    """Access key for the audio."""

    url: typing.Optional[str] = Field(
        default=None,
    )
    """URL of mp3 file."""

    stream_duration: typing.Optional[int] = Field(
        default=None,
    )
    """Stream duration in seconds."""

    date: typing.Optional[int] = Field(
        default=None,
    )
    """Date when uploaded."""

    album_id: typing.Optional[int] = Field(
        default=None,
    )
    """Album ID."""

    performer: typing.Optional[str] = Field(
        default=None,
    )
    """Performer name."""

    file_size: typing.Optional[int] = Field(
        default=None,
    )
    """Примерный объем памяти занимаемый аудио на устройстве. Реализовано только для эпизодов подкастов."""


class CallbackVkpayTransaction(BaseModel):
    """
    Model: `CallbackVkpayTransaction`
    """

    amount: int = Field()
    """Property `CallbackVkpayTransaction.amount`."""

    from_id: int = Field()
    """Property `CallbackVkpayTransaction.from_id`."""

    description: str = Field()
    """Property `CallbackVkpayTransaction.description`."""

    date: int = Field()
    """Property `CallbackVkpayTransaction.date`."""

    payload: typing.Optional[str] = Field(
        default=None,
    )
    """Property `CallbackVkpayTransaction.payload`."""


class CallbackWallCommentDelete(BaseModel):
    """
    Model: `CallbackWallCommentDelete`
    """

    owner_id: int = Field()
    """Property `CallbackWallCommentDelete.owner_id`."""

    id: int = Field()
    """Property `CallbackWallCommentDelete.id`."""

    user_id: int = Field()
    """Property `CallbackWallCommentDelete.user_id`."""

    post_id: int = Field()
    """Property `CallbackWallCommentDelete.post_id`."""


class CallbackWallPostNewInnerType(str, enum.Enum, metaclass=BaseEnumMeta):
    WALL_WALLPOST = "wall_wallpost"


class CallbackWallPostNew(BaseModel):
    """
    Model: `CallbackWallPostNew`
    """

    inner_type: "CallbackWallPostNewInnerType" = Field()
    """Property `CallbackWallPostNew.inner_type`."""

    access_key: typing.Optional[str] = Field(
        default=None,
    )
    """Access key to private object."""

    is_deleted: typing.Optional[bool] = Field(
        default=None,
    )
    """Property `CallbackWallPostNew.is_deleted`."""

    deleted_reason: typing.Optional[str] = Field(
        default=None,
    )
    """Property `CallbackWallPostNew.deleted_reason`."""

    deleted_details: typing.Optional[str] = Field(
        default=None,
    )
    """Property `CallbackWallPostNew.deleted_details`."""

    donut_miniapp_url: typing.Optional[str] = Field(
        default=None,
    )
    """Property `CallbackWallPostNew.donut_miniapp_url`."""

    attachments: typing.Optional[typing.List["WallWallpostAttachment"]] = Field(
        default=None,
    )
    """Property `CallbackWallPostNew.attachments`."""

    copyright: typing.Optional["WallPostCopyright"] = Field(
        default=None,
    )
    """Information about the source of the post."""

    date: typing.Optional[int] = Field(
        default=None,
    )
    """Date of publishing in Unixtime."""

    edited: typing.Optional[int] = Field(
        default=None,
    )
    """Date of editing in Unixtime."""

    from_id: typing.Optional[int] = Field(
        default=None,
    )
    """Post author ID."""

    geo: typing.Optional["WallGeo"] = Field(
        default=None,
    )
    """Property `CallbackWallPostNew.geo`."""

    id: typing.Optional[int] = Field(
        default=None,
    )
    """Post ID."""

    is_archived: typing.Optional[bool] = Field(
        default=None,
    )
    """Is post archived, only for post owners."""

    is_favorite: typing.Optional[bool] = Field(
        default=None,
    )
    """Information whether the post in favorites list."""

    likes: typing.Optional["BaseLikesInfo"] = Field(
        default=None,
    )
    """Count of likes."""

    owner_id: typing.Optional[int] = Field(
        default=None,
    )
    """Wall owner\'s ID."""

    post_id: typing.Optional[int] = Field(
        default=None,
    )
    """If post type \'reply\', contains original post ID."""

    parents_stack: typing.Optional[typing.List[int]] = Field(
        default=None,
    )
    """If post type \'reply\', contains original parent IDs stack."""

    post_source: typing.Optional["WallPostSource"] = Field(
        default=None,
    )
    """Property `CallbackWallPostNew.post_source`."""

    post_type: typing.Optional["WallPostType"] = Field(
        default=None,
    )
    """Property `CallbackWallPostNew.post_type`."""

    reposts: typing.Optional["BaseRepostsInfo"] = Field(
        default=None,
    )
    """Property `CallbackWallPostNew.reposts`."""

    signer_id: typing.Optional[int] = Field(
        default=None,
    )
    """Post signer ID."""

    text: typing.Optional[str] = Field(
        default=None,
    )
    """Post text."""

    views: typing.Optional["WallViews"] = Field(
        default=None,
    )
    """Count of views."""


class CallbackWallReplyEdit(BaseModel):
    """
    Model: `CallbackWallReplyEdit`
    """

    id: int = Field()
    """Comment ID."""

    from_id: int = Field()
    """Author ID."""

    date: int = Field()
    """Date when the comment has been added in Unixtime."""

    text: str = Field()
    """Comment text."""

    can_edit: typing.Optional[bool] = Field(
        default=None,
    )
    """Property `CallbackWallReplyEdit.can_edit`."""

    post_id: typing.Optional[int] = Field(
        default=None,
    )
    """Property `CallbackWallReplyEdit.post_id`."""

    owner_id: typing.Optional[int] = Field(
        default=None,
    )
    """Property `CallbackWallReplyEdit.owner_id`."""

    parents_stack: typing.Optional[typing.List[int]] = Field(
        default=None,
    )
    """Property `CallbackWallReplyEdit.parents_stack`."""

    photo_id: typing.Optional[int] = Field(
        default=None,
    )
    """Property `CallbackWallReplyEdit.photo_id`."""

    video_id: typing.Optional[int] = Field(
        default=None,
    )
    """Property `CallbackWallReplyEdit.video_id`."""

    attachments: typing.Optional[typing.List["WallWallpostAttachment"]] = Field(
        default=None,
    )
    """Property `CallbackWallReplyEdit.attachments`."""

    donut: typing.Optional["WallWallCommentDonut"] = Field(
        default=None,
    )
    """Property `CallbackWallReplyEdit.donut`."""

    likes: typing.Optional["BaseLikesInfo"] = Field(
        default=None,
    )
    """Property `CallbackWallReplyEdit.likes`."""

    real_offset: typing.Optional[int] = Field(
        default=None,
    )
    """Real position of the comment."""

    reply_to_user: typing.Optional[int] = Field(
        default=None,
    )
    """Replied user ID."""

    reply_to_comment: typing.Optional[int] = Field(
        default=None,
    )
    """Replied comment ID."""

    thread: typing.Optional["CommentThread"] = Field(
        default=None,
    )
    """Property `CallbackWallReplyEdit.thread`."""

    is_from_post_author: typing.Optional[bool] = Field(
        default=None,
    )
    """Whether post is by author of the post or not."""

    deleted: typing.Optional[bool] = Field(
        default=None,
    )
    """Property `CallbackWallReplyEdit.deleted`."""

    pid: typing.Optional[int] = Field(
        default=None,
    )
    """Photo ID."""


class CallbackWallReplyNew(BaseModel):
    """
    Model: `CallbackWallReplyNew`
    """

    id: int = Field()
    """Comment ID."""

    from_id: int = Field()
    """Author ID."""

    date: int = Field()
    """Date when the comment has been added in Unixtime."""

    text: str = Field()
    """Comment text."""

    can_edit: typing.Optional[bool] = Field(
        default=None,
    )
    """Property `CallbackWallReplyNew.can_edit`."""

    post_id: typing.Optional[int] = Field(
        default=None,
    )
    """Property `CallbackWallReplyNew.post_id`."""

    owner_id: typing.Optional[int] = Field(
        default=None,
    )
    """Property `CallbackWallReplyNew.owner_id`."""

    parents_stack: typing.Optional[typing.List[int]] = Field(
        default=None,
    )
    """Property `CallbackWallReplyNew.parents_stack`."""

    photo_id: typing.Optional[int] = Field(
        default=None,
    )
    """Property `CallbackWallReplyNew.photo_id`."""

    video_id: typing.Optional[int] = Field(
        default=None,
    )
    """Property `CallbackWallReplyNew.video_id`."""

    attachments: typing.Optional[typing.List["WallWallpostAttachment"]] = Field(
        default=None,
    )
    """Property `CallbackWallReplyNew.attachments`."""

    donut: typing.Optional["WallWallCommentDonut"] = Field(
        default=None,
    )
    """Property `CallbackWallReplyNew.donut`."""

    likes: typing.Optional["BaseLikesInfo"] = Field(
        default=None,
    )
    """Property `CallbackWallReplyNew.likes`."""

    real_offset: typing.Optional[int] = Field(
        default=None,
    )
    """Real position of the comment."""

    reply_to_user: typing.Optional[int] = Field(
        default=None,
    )
    """Replied user ID."""

    reply_to_comment: typing.Optional[int] = Field(
        default=None,
    )
    """Replied comment ID."""

    thread: typing.Optional["CommentThread"] = Field(
        default=None,
    )
    """Property `CallbackWallReplyNew.thread`."""

    is_from_post_author: typing.Optional[bool] = Field(
        default=None,
    )
    """Whether post is by author of the post or not."""

    deleted: typing.Optional[bool] = Field(
        default=None,
    )
    """Property `CallbackWallReplyNew.deleted`."""

    pid: typing.Optional[int] = Field(
        default=None,
    )
    """Photo ID."""


class CallbackWallReplyRestore(BaseModel):
    """
    Model: `CallbackWallReplyRestore`
    """

    id: int = Field()
    """Comment ID."""

    from_id: int = Field()
    """Author ID."""

    date: int = Field()
    """Date when the comment has been added in Unixtime."""

    text: str = Field()
    """Comment text."""

    can_edit: typing.Optional[bool] = Field(
        default=None,
    )
    """Property `CallbackWallReplyRestore.can_edit`."""

    post_id: typing.Optional[int] = Field(
        default=None,
    )
    """Property `CallbackWallReplyRestore.post_id`."""

    owner_id: typing.Optional[int] = Field(
        default=None,
    )
    """Property `CallbackWallReplyRestore.owner_id`."""

    parents_stack: typing.Optional[typing.List[int]] = Field(
        default=None,
    )
    """Property `CallbackWallReplyRestore.parents_stack`."""

    photo_id: typing.Optional[int] = Field(
        default=None,
    )
    """Property `CallbackWallReplyRestore.photo_id`."""

    video_id: typing.Optional[int] = Field(
        default=None,
    )
    """Property `CallbackWallReplyRestore.video_id`."""

    attachments: typing.Optional[typing.List["WallWallpostAttachment"]] = Field(
        default=None,
    )
    """Property `CallbackWallReplyRestore.attachments`."""

    donut: typing.Optional["WallWallCommentDonut"] = Field(
        default=None,
    )
    """Property `CallbackWallReplyRestore.donut`."""

    likes: typing.Optional["BaseLikesInfo"] = Field(
        default=None,
    )
    """Property `CallbackWallReplyRestore.likes`."""

    real_offset: typing.Optional[int] = Field(
        default=None,
    )
    """Real position of the comment."""

    reply_to_user: typing.Optional[int] = Field(
        default=None,
    )
    """Replied user ID."""

    reply_to_comment: typing.Optional[int] = Field(
        default=None,
    )
    """Replied comment ID."""

    thread: typing.Optional["CommentThread"] = Field(
        default=None,
    )
    """Property `CallbackWallReplyRestore.thread`."""

    is_from_post_author: typing.Optional[bool] = Field(
        default=None,
    )
    """Whether post is by author of the post or not."""

    deleted: typing.Optional[bool] = Field(
        default=None,
    )
    """Property `CallbackWallReplyRestore.deleted`."""

    pid: typing.Optional[int] = Field(
        default=None,
    )
    """Photo ID."""


class CallbackWallRepostInnerType(str, enum.Enum, metaclass=BaseEnumMeta):
    WALL_WALLPOST = "wall_wallpost"


class CallbackWallRepost(BaseModel):
    """
    Model: `CallbackWallRepost`
    """

    inner_type: "CallbackWallRepostInnerType" = Field()
    """Property `CallbackWallRepost.inner_type`."""

    access_key: typing.Optional[str] = Field(
        default=None,
    )
    """Access key to private object."""

    is_deleted: typing.Optional[bool] = Field(
        default=None,
    )
    """Property `CallbackWallRepost.is_deleted`."""

    deleted_reason: typing.Optional[str] = Field(
        default=None,
    )
    """Property `CallbackWallRepost.deleted_reason`."""

    deleted_details: typing.Optional[str] = Field(
        default=None,
    )
    """Property `CallbackWallRepost.deleted_details`."""

    donut_miniapp_url: typing.Optional[str] = Field(
        default=None,
    )
    """Property `CallbackWallRepost.donut_miniapp_url`."""

    attachments: typing.Optional[typing.List["WallWallpostAttachment"]] = Field(
        default=None,
    )
    """Property `CallbackWallRepost.attachments`."""

    copyright: typing.Optional["WallPostCopyright"] = Field(
        default=None,
    )
    """Information about the source of the post."""

    date: typing.Optional[int] = Field(
        default=None,
    )
    """Date of publishing in Unixtime."""

    edited: typing.Optional[int] = Field(
        default=None,
    )
    """Date of editing in Unixtime."""

    from_id: typing.Optional[int] = Field(
        default=None,
    )
    """Post author ID."""

    geo: typing.Optional["WallGeo"] = Field(
        default=None,
    )
    """Property `CallbackWallRepost.geo`."""

    id: typing.Optional[int] = Field(
        default=None,
    )
    """Post ID."""

    is_archived: typing.Optional[bool] = Field(
        default=None,
    )
    """Is post archived, only for post owners."""

    is_favorite: typing.Optional[bool] = Field(
        default=None,
    )
    """Information whether the post in favorites list."""

    likes: typing.Optional["BaseLikesInfo"] = Field(
        default=None,
    )
    """Count of likes."""

    owner_id: typing.Optional[int] = Field(
        default=None,
    )
    """Wall owner\'s ID."""

    post_id: typing.Optional[int] = Field(
        default=None,
    )
    """If post type \'reply\', contains original post ID."""

    parents_stack: typing.Optional[typing.List[int]] = Field(
        default=None,
    )
    """If post type \'reply\', contains original parent IDs stack."""

    post_source: typing.Optional["WallPostSource"] = Field(
        default=None,
    )
    """Property `CallbackWallRepost.post_source`."""

    post_type: typing.Optional["WallPostType"] = Field(
        default=None,
    )
    """Property `CallbackWallRepost.post_type`."""

    reposts: typing.Optional["BaseRepostsInfo"] = Field(
        default=None,
    )
    """Property `CallbackWallRepost.reposts`."""

    signer_id: typing.Optional[int] = Field(
        default=None,
    )
    """Post signer ID."""

    text: typing.Optional[str] = Field(
        default=None,
    )
    """Post text."""

    views: typing.Optional["WallViews"] = Field(
        default=None,
    )
    """Count of views."""


class CallsCall(BaseModel):
    """
    Model: `CallsCall`
    """

    initiator_id: int = Field()
    """Caller initiator."""

    receiver_id: int = Field()
    """Caller receiver."""

    state: "CallsEndState" = Field()
    """Property `CallsCall.state`."""

    time: int = Field()
    """Timestamp for call."""

    duration: typing.Optional[int] = Field(
        default=None,
    )
    """Call duration."""

    video: typing.Optional[bool] = Field(
        default=None,
    )
    """Was this call initiated as video call."""

    participants: typing.Optional["CallsParticipants"] = Field(
        default=None,
    )
    """Property `CallsCall.participants`."""


class CallsEndState(str, enum.Enum, metaclass=BaseEnumMeta):
    CANCELED_BY_INITIATOR = "canceled_by_initiator"
    CANCELED_BY_RECEIVER = "canceled_by_receiver"
    REACHED = "reached"


class CallsParticipants(BaseModel):
    """
    Model: `CallsParticipants`
    """

    list: typing.Optional[typing.List[int]] = Field(
        default=None,
    )
    """Property `CallsParticipants.list`."""

    count: typing.Optional[int] = Field(
        default=None,
    )
    """Participants count."""


class CallsShortCredentials(BaseModel):
    """
    These credentials may be used to join a call without knowing a VK Join Link
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
    """
    Model: `CommentThread`
    """

    count: int = Field()
    """Comments number."""

    items: typing.Optional[typing.List["WallWallComment"]] = Field(
        default=None,
    )
    """Property `CommentThread.items`."""

    can_post: typing.Optional[bool] = Field(
        default=None,
    )
    """Information whether current user can comment the post."""

    show_reply_button: typing.Optional[bool] = Field(
        default=None,
    )
    """Information whether recommended to display reply button."""

    groups_can_post: typing.Optional[bool] = Field(
        default=None,
    )
    """Information whether groups can comment the post."""

    author_replied: typing.Optional[bool] = Field(
        default=None,
    )
    """Information whether author commented the thread."""


DatabaseCitiesFields: typing.TypeAlias = str


class DatabaseCityById(BaseModel):
    """
    Model: `DatabaseCityById`
    """

    id: int = Field()
    """Object ID."""

    title: str = Field()
    """Object title."""


class DatabaseFaculty(BaseModel):
    """
    Model: `DatabaseFaculty`
    """

    id: typing.Optional[int] = Field(
        default=None,
    )
    """Faculty ID."""

    title: typing.Optional[str] = Field(
        default=None,
    )
    """Faculty title."""


class DatabaseLanguageFull(BaseModel):
    """
    Model: `DatabaseLanguageFull`
    """

    id: int = Field()
    """Language ID."""

    native_name: str = Field()
    """Language native name."""


class DatabaseRegion(BaseModel):
    """
    Model: `DatabaseRegion`
    """

    id: typing.Optional[int] = Field(
        default=None,
    )
    """Region ID."""

    title: typing.Optional[str] = Field(
        default=None,
    )
    """Region title."""


class DatabaseSchool(BaseModel):
    """
    Model: `DatabaseSchool`
    """

    id: typing.Optional[int] = Field(
        default=None,
    )
    """School ID."""

    title: typing.Optional[str] = Field(
        default=None,
    )
    """School title."""


class DatabaseSchoolClass(BaseModel):
    """
    Model: `DatabaseSchoolClass`
    """

    id: int = Field()
    """Object ID."""

    title: str = Field()
    """Object title."""


class DatabaseStation(BaseModel):
    """
    Model: `DatabaseStation`
    """

    id: int = Field()
    """Station ID."""

    name: str = Field()
    """Station name."""

    city_id: typing.Optional[int] = Field(
        default=None,
    )
    """City ID."""

    color: typing.Optional[str] = Field(
        default=None,
    )
    """Hex color code without #."""


class DatabaseUniversity(BaseModel):
    """
    Model: `DatabaseUniversity`
    """

    id: typing.Optional[int] = Field(
        default=None,
    )
    """University ID."""

    title: typing.Optional[str] = Field(
        default=None,
    )
    """University title."""


class DocsDoc(BaseModel):
    """
    Model: `DocsDoc`
    """

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

    date: int = Field()
    """Date when file has been uploaded in Unixtime."""

    type: int = Field()
    """Document type."""

    url: typing.Optional[str] = Field(
        default=None,
    )
    """File URL."""

    preview: typing.Optional["DocsDocPreview"] = Field(
        default=None,
    )
    """Property `DocsDoc.preview`."""

    is_licensed: typing.Optional[bool] = Field(
        default=None,
    )
    """Property `DocsDoc.is_licensed`."""

    access_key: typing.Optional[str] = Field(
        default=None,
    )
    """Access key for the document."""

    tags: typing.Optional[typing.List[str]] = Field(
        default=None,
    )
    """Document tags."""


class DocsDocAttachmentType(str, enum.Enum, metaclass=BaseEnumMeta):
    DOC = "doc"
    GRAFFITI = "graffiti"
    AUDIO_MESSAGE = "audio_message"


class DocsDocPreview(BaseModel):
    """
    Model: `DocsDocPreview`
    """

    audio_msg: typing.Optional["DocsDocPreviewAudioMsg"] = Field(
        default=None,
    )
    """Property `DocsDocPreview.audio_msg`."""

    graffiti: typing.Optional["DocsDocPreviewGraffiti"] = Field(
        default=None,
    )
    """Property `DocsDocPreview.graffiti`."""

    photo: typing.Optional["DocsDocPreviewPhoto"] = Field(
        default=None,
    )
    """Property `DocsDocPreview.photo`."""

    video: typing.Optional["DocsDocPreviewVideo"] = Field(
        default=None,
    )
    """Property `DocsDocPreview.video`."""


class DocsDocPreviewAudioMsg(BaseModel):
    """
    Model: `DocsDocPreviewAudioMsg`
    """

    duration: int = Field()
    """Audio message duration in seconds."""

    link_mp3: str = Field()
    """MP3 file URL."""

    link_ogg: str = Field()
    """OGG file URL."""

    waveform: typing.List[int] = Field()
    """Property `DocsDocPreviewAudioMsg.waveform`."""


class DocsDocPreviewGraffiti(BaseModel):
    """
    Model: `DocsDocPreviewGraffiti`
    """

    src: str = Field()
    """Graffiti file URL."""

    width: int = Field()
    """Graffiti width."""

    height: int = Field()
    """Graffiti height."""


class DocsDocPreviewPhoto(BaseModel):
    """
    Model: `DocsDocPreviewPhoto`
    """

    sizes: typing.Optional[typing.List["DocsDocPreviewPhotoSizes"]] = Field(
        default=None,
    )
    """Property `DocsDocPreviewPhoto.sizes`."""


class DocsDocPreviewPhotoSizes(BaseModel):
    """
    Model: `DocsDocPreviewPhotoSizes`
    """

    src: str = Field()
    """URL of the image."""

    width: int = Field()
    """Width in px."""

    height: int = Field()
    """Height in px."""

    type: "PhotosPhotoSizesType" = Field()
    """Property `DocsDocPreviewPhotoSizes.type`."""


class DocsDocPreviewVideo(BaseModel):
    """
    Model: `DocsDocPreviewVideo`
    """

    src: str = Field()
    """Video URL."""

    width: int = Field()
    """Video\'s width in pixels."""

    height: int = Field()
    """Video\'s height in pixels."""

    file_size: int = Field()
    """Video file size in bites."""


class DocsDocTypes(BaseModel):
    """
    Model: `DocsDocTypes`
    """

    id: int = Field()
    """Doc type ID."""

    name: str = Field()
    """Doc type title."""

    count: int = Field()
    """Number of docs."""


class DonutDonatorSubscriptionInfoStatus(str, enum.Enum, metaclass=BaseEnumMeta):
    ACTIVE = "active"
    EXPIRING = "expiring"


class DonutDonatorSubscriptionInfo(BaseModel):
    """
    Info about user VK Donut subscription
    Model: `DonutDonatorSubscriptionInfo`
    """

    owner_id: int = Field()
    """Property `DonutDonatorSubscriptionInfo.owner_id`."""

    next_payment_date: int = Field()
    """Property `DonutDonatorSubscriptionInfo.next_payment_date`."""

    amount: int = Field()
    """Property `DonutDonatorSubscriptionInfo.amount`."""

    status: "DonutDonatorSubscriptionInfoStatus" = Field()
    """Property `DonutDonatorSubscriptionInfo.status`."""


class EventsEventAttach(BaseModel):
    """
    Model: `EventsEventAttach`
    """

    button_text: str = Field()
    """text of attach."""

    friends: typing.List[int] = Field()
    """array of friends ids."""

    id: int = Field()
    """event ID."""

    is_favorite: bool = Field()
    """is favorite."""

    text: str = Field()
    """text of attach."""

    address: typing.Optional[str] = Field(
        default=None,
    )
    """address of event."""

    member_status: typing.Optional["GroupsGroupFullMemberStatus"] = Field(
        default=None,
    )
    """Current user\'s member status."""

    time: typing.Optional[int] = Field(
        default=None,
    )
    """event start time."""


class FaveBookmark(BaseModel):
    """
    Model: `FaveBookmark`
    """

    added_date: int = Field()
    """Timestamp, when this item was bookmarked."""

    seen: bool = Field()
    """Has user seen this item."""

    tags: typing.List["FaveTag"] = Field()
    """Property `FaveBookmark.tags`."""

    type: "FaveBookmarkType" = Field()
    """Item type."""

    link: typing.Optional["BaseLink"] = Field(
        default=None,
    )
    """Property `FaveBookmark.link`."""

    post: typing.Optional["WallWallpostFull"] = Field(
        default=None,
    )
    """Property `FaveBookmark.post`."""

    product: typing.Optional["MarketMarketItemFull"] = Field(
        default=None,
    )
    """Property `FaveBookmark.product`."""

    video: typing.Optional["VideoVideoFull"] = Field(
        default=None,
    )
    """Property `FaveBookmark.video`."""


class FaveBookmarkType(str, enum.Enum, metaclass=BaseEnumMeta):
    POST = "post"
    VIDEO = "video"
    PRODUCT = "product"
    ARTICLE = "article"
    LINK = "link"
    CLIP = "clip"
    GAME = "game"
    MINI_APP = "mini_app"


class FavePage(BaseModel):
    """
    Model: `FavePage`
    """

    description: str = Field()
    """Some info about user or group."""

    tags: typing.List["FaveTag"] = Field()
    """Property `FavePage.tags`."""

    type: "FavePageType" = Field()
    """Item type."""

    group: typing.Optional["GroupsGroupFull"] = Field(
        default=None,
    )
    """Property `FavePage.group`."""

    updated_date: typing.Optional[int] = Field(
        default=None,
    )
    """Timestamp, when this page was bookmarked."""

    user: typing.Optional["UsersUserFull"] = Field(
        default=None,
    )
    """Property `FavePage.user`."""


class FavePageType(str, enum.Enum, metaclass=BaseEnumMeta):
    USER = "user"
    GROUP = "group"
    HINTS = "hints"


class FaveTag(BaseModel):
    """
    Model: `FaveTag`
    """

    id: typing.Optional[int] = Field(
        default=None,
    )
    """Tag id."""

    name: typing.Optional[str] = Field(
        default=None,
    )
    """Tag name."""


class GiftsGift(BaseModel):
    """
    Model: `GiftsGift`
    """

    date: typing.Optional[int] = Field(
        default=None,
    )
    """Date when gist has been sent in Unixtime."""

    from_id: typing.Optional[int] = Field(
        default=None,
    )
    """Gift sender ID."""

    gift: typing.Optional["GiftsLayout"] = Field(
        default=None,
    )
    """Property `GiftsGift.gift`."""

    gift_hash: typing.Optional[str] = Field(
        default=None,
    )
    """Hash."""

    id: typing.Optional[int] = Field(
        default=None,
    )
    """Gift ID."""

    message: typing.Optional[str] = Field(
        default=None,
    )
    """Comment text."""

    privacy: typing.Optional["GiftsGiftPrivacy"] = Field(
        default=None,
    )
    """Property `GiftsGift.privacy`."""


class GiftsGiftPrivacy(int, enum.Enum, metaclass=BaseEnumMeta):
    NAME_AND_MESSAGE_FOR_ALL = 0
    NAME_FOR_ALL = 1
    NAME_AND_MESSAGE_FOR_RECIPIENT_ONLY = 2


class GiftsLayout(BaseModel):
    """
    Model: `GiftsLayout`
    """

    id: int = Field()
    """Gift ID."""

    thumb_512: typing.Optional[str] = Field(
        default=None,
    )
    """URL of the preview image with 512 px in width."""

    thumb_256: typing.Optional[str] = Field(
        default=None,
    )
    """URL of the preview image with 256 px in width."""

    thumb_48: typing.Optional[str] = Field(
        default=None,
    )
    """URL of the preview image with 48 px in width."""

    thumb_96: typing.Optional[str] = Field(
        default=None,
    )
    """URL of the preview image with 96 px in width."""

    stickers_product_id: typing.Optional[int] = Field(
        default=None,
    )
    """ID of the sticker pack, if the gift is representing one."""

    is_stickers_style: typing.Optional[bool] = Field(
        default=None,
    )
    """Information whether gift represents a stickers style."""

    build_id: typing.Optional[str] = Field(
        default=None,
    )
    """ID of the build of constructor gift."""

    keywords: typing.Optional[str] = Field(
        default=None,
    )
    """Keywords used for search."""


class GroupsAddress(BaseModel):
    """
    Model: `GroupsAddress`
    """

    id: int = Field()
    """Address id."""

    additional_address: typing.Optional[str] = Field(
        default=None,
    )
    """Additional address to the place (6 floor, left door)."""

    address: typing.Optional[str] = Field(
        default=None,
    )
    """String address to the place (Nevsky, 28)."""

    city_id: typing.Optional[int] = Field(
        default=None,
    )
    """City id of address."""

    city: typing.Optional["DatabaseCityById"] = Field(
        default=None,
    )
    """City for address."""

    metro_station: typing.Optional["DatabaseStation"] = Field(
        default=None,
    )
    """Metro for address."""

    country: typing.Optional["BaseCountry"] = Field(
        default=None,
    )
    """Country for address."""

    distance: typing.Optional[int] = Field(
        default=None,
    )
    """Distance from the point."""

    latitude: typing.Optional[float] = Field(
        default=None,
    )
    """Address latitude."""

    longitude: typing.Optional[float] = Field(
        default=None,
    )
    """Address longitude."""

    metro_station_id: typing.Optional[int] = Field(
        default=None,
    )
    """Metro id of address."""

    phone: typing.Optional[str] = Field(
        default=None,
    )
    """Address phone."""

    time_offset: typing.Optional[int] = Field(
        default=None,
    )
    """Time offset int minutes from utc time."""

    timetable: typing.Optional["GroupsAddressTimetable"] = Field(
        default=None,
    )
    """Week timetable for the address."""

    title: typing.Optional[str] = Field(
        default=None,
    )
    """Title of the place (Zinger, etc)."""

    work_info_status: typing.Optional["GroupsAddressWorkInfoStatus"] = Field(
        default=None,
    )
    """Status of information about timetable."""

    place_id: typing.Optional[int] = Field(
        default=None,
    )
    """Property `GroupsAddress.place_id`."""


class GroupsAddressTimetable(BaseModel):
    """
    Timetable for a week
    Model: `GroupsAddressTimetable`
    """

    fri: typing.Optional["GroupsAddressTimetableDay"] = Field(
        default=None,
    )
    """Timetable for friday."""

    mon: typing.Optional["GroupsAddressTimetableDay"] = Field(
        default=None,
    )
    """Timetable for monday."""

    sat: typing.Optional["GroupsAddressTimetableDay"] = Field(
        default=None,
    )
    """Timetable for saturday."""

    sun: typing.Optional["GroupsAddressTimetableDay"] = Field(
        default=None,
    )
    """Timetable for sunday."""

    thu: typing.Optional["GroupsAddressTimetableDay"] = Field(
        default=None,
    )
    """Timetable for thursday."""

    tue: typing.Optional["GroupsAddressTimetableDay"] = Field(
        default=None,
    )
    """Timetable for tuesday."""

    wed: typing.Optional["GroupsAddressTimetableDay"] = Field(
        default=None,
    )
    """Timetable for wednesday."""


class GroupsAddressTimetableDay(BaseModel):
    """
    Timetable for one day
    Model: `GroupsAddressTimetableDay`
    """

    close_time: int = Field()
    """Close time in minutes."""

    open_time: int = Field()
    """Open time in minutes."""

    break_close_time: typing.Optional[int] = Field(
        default=None,
    )
    """Close time of the break in minutes."""

    break_open_time: typing.Optional[int] = Field(
        default=None,
    )
    """Start time of the break in minutes."""


class GroupsAddressWorkInfoStatus(str, enum.Enum, metaclass=BaseEnumMeta):
    NO_INFORMATION = "no_information"
    TEMPORARILY_CLOSED = "temporarily_closed"
    ALWAYS_OPENED = "always_opened"
    TIMETABLE = "timetable"
    FOREVER_CLOSED = "forever_closed"


class GroupsAddressesInfo(BaseModel):
    """
    Model: `GroupsAddressesInfo`
    """

    is_enabled: bool = Field()
    """Information whether addresses is enabled."""

    main_address_id: typing.Optional[int] = Field(
        default=None,
    )
    """Main address id for group."""

    main_address: typing.Optional["GroupsAddress"] = Field(
        default=None,
    )
    """Main address."""

    count: typing.Optional[int] = Field(
        default=None,
    )
    """Count of addresses."""


class GroupsBanInfo(BaseModel):
    """
    Model: `GroupsBanInfo`
    """

    admin_id: typing.Optional[int] = Field(
        default=None,
    )
    """Administrator ID."""

    comment: typing.Optional[str] = Field(
        default=None,
    )
    """Comment for a ban."""

    comment_visible: typing.Optional[bool] = Field(
        default=None,
    )
    """Show comment for user."""

    is_closed: typing.Optional[bool] = Field(
        default=None,
    )
    """Property `GroupsBanInfo.is_closed`."""

    date: typing.Optional[int] = Field(
        default=None,
    )
    """Date when user has been added to blacklist in Unixtime."""

    end_date: typing.Optional[int] = Field(
        default=None,
    )
    """Date when user will be removed from blacklist in Unixtime."""

    reason: typing.Optional["GroupsBanInfoReason"] = Field(
        default=None,
    )
    """Property `GroupsBanInfo.reason`."""


class GroupsBanInfoReason(int, enum.Enum, metaclass=BaseEnumMeta):
    OTHER = 0
    SPAM = 1
    VERBAL_ABUSE = 2
    STRONG_LANGUAGE = 3
    FLOOD = 4


class GroupsCallbackServerStatus(str, enum.Enum, metaclass=BaseEnumMeta):
    UNCONFIGURED = "unconfigured"
    FAILED = "failed"
    WAIT = "wait"
    OK = "ok"


class GroupsCallbackServer(BaseModel):
    """
    Model: `GroupsCallbackServer`
    """

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
    """
    Model: `GroupsCallbackSettings`
    """

    api_version: typing.Optional[str] = Field(
        default=None,
    )
    """API version used for the events."""

    events: typing.Optional["GroupsLongPollEvents"] = Field(
        default=None,
    )
    """Property `GroupsCallbackSettings.events`."""


class GroupsContactsItem(BaseModel):
    """
    Model: `GroupsContactsItem`
    """

    user_id: typing.Optional[int] = Field(
        default=None,
    )
    """User ID."""

    desc: typing.Optional[str] = Field(
        default=None,
    )
    """Contact description."""

    phone: typing.Optional[str] = Field(
        default=None,
    )
    """Contact phone."""

    email: typing.Optional[str] = Field(
        default=None,
    )
    """Contact email."""


class GroupsCountersGroup(BaseModel):
    """
    Model: `GroupsCountersGroup`
    """

    addresses: typing.Optional[int] = Field(
        default=None,
    )
    """Addresses number."""

    albums: typing.Optional[int] = Field(
        default=None,
    )
    """Photo albums number."""

    audios: typing.Optional[int] = Field(
        default=None,
    )
    """Audios number."""

    audio_playlists: typing.Optional[int] = Field(
        default=None,
    )
    """Audio playlists number."""

    docs: typing.Optional[int] = Field(
        default=None,
    )
    """Docs number."""

    market: typing.Optional[int] = Field(
        default=None,
    )
    """Market items number."""

    photos: typing.Optional[int] = Field(
        default=None,
    )
    """Photos number."""

    topics: typing.Optional[int] = Field(
        default=None,
    )
    """Topics number."""

    videos: typing.Optional[int] = Field(
        default=None,
    )
    """Videos number."""

    video_playlists: typing.Optional[int] = Field(
        default=None,
    )
    """Playlists number."""

    market_services: typing.Optional[int] = Field(
        default=None,
    )
    """Market services number."""

    podcasts: typing.Optional[int] = Field(
        default=None,
    )
    """Podcasts number."""

    articles: typing.Optional[int] = Field(
        default=None,
    )
    """Articles number."""

    narratives: typing.Optional[int] = Field(
        default=None,
    )
    """Narratives number."""

    clips: typing.Optional[int] = Field(
        default=None,
    )
    """Clips number."""

    clips_followers: typing.Optional[int] = Field(
        default=None,
    )
    """Clips followers number."""

    videos_followers: typing.Optional[int] = Field(
        default=None,
    )
    """Videos followers number."""

    clips_views: typing.Optional[int] = Field(
        default=None,
    )
    """Clips views number."""

    clips_likes: typing.Optional[int] = Field(
        default=None,
    )
    """Clips likes number."""


class GroupsFields(str, enum.Enum, metaclass=BaseEnumMeta):
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


class GroupsFilter(str, enum.Enum, metaclass=BaseEnumMeta):
    ADMIN = "admin"
    EDITOR = "editor"
    MODER = "moder"
    ADVERTISER = "advertiser"
    GROUPS = "groups"
    PUBLICS = "publics"
    EVENTS = "events"
    HAS_ADDRESSES = "has_addresses"


class GroupsGroup(BaseModel):
    """
    Model: `GroupsGroup`
    """

    id: int = Field()
    """Community ID."""

    name: typing.Optional[str] = Field(
        default=None,
    )
    """Community name."""

    screen_name: typing.Optional[str] = Field(
        default=None,
    )
    """Domain of the community page."""

    is_closed: typing.Optional["GroupsGroupIsClosed"] = Field(
        default=None,
    )
    """Property `GroupsGroup.is_closed`."""

    type: typing.Optional["GroupsGroupType"] = Field(
        default=None,
    )
    """Property `GroupsGroup.type`."""

    is_admin: typing.Optional[bool] = Field(
        default=None,
    )
    """Information whether current user is administrator."""

    admin_level: typing.Optional["GroupsGroupAdminLevel"] = Field(
        default=None,
    )
    """Property `GroupsGroup.admin_level`."""

    is_member: typing.Optional[bool] = Field(
        default=None,
    )
    """Information whether current user is member."""

    is_advertiser: typing.Optional[bool] = Field(
        default=None,
    )
    """Information whether current user is advertiser."""

    start_date: typing.Optional[int] = Field(
        default=None,
    )
    """Start date in Unixtime format."""

    finish_date: typing.Optional[int] = Field(
        default=None,
    )
    """Finish date in Unixtime format."""

    verified: typing.Optional[bool] = Field(
        default=None,
    )
    """Information whether community is verified."""

    deactivated: typing.Optional[str] = Field(
        default=None,
    )
    """Information whether community is banned."""

    photo_50: typing.Optional[str] = Field(
        default=None,
    )
    """URL of square photo of the community with 50 pixels in width."""

    photo_100: typing.Optional[str] = Field(
        default=None,
    )
    """URL of square photo of the community with 100 pixels in width."""

    photo_200: typing.Optional[str] = Field(
        default=None,
    )
    """URL of square photo of the community with 200 pixels in width."""

    photo_200_orig: typing.Optional[str] = Field(
        default=None,
    )
    """URL of square photo of the community with 200 pixels in width original."""

    photo_400: typing.Optional[str] = Field(
        default=None,
    )
    """URL of square photo of the community with 400 pixels in width."""

    photo_400_orig: typing.Optional[str] = Field(
        default=None,
    )
    """URL of square photo of the community with 400 pixels in width original."""

    photo_max: typing.Optional[str] = Field(
        default=None,
    )
    """URL of square photo of the community with max pixels in width."""

    photo_max_orig: typing.Optional[str] = Field(
        default=None,
    )
    """URL of square photo of the community with max pixels in width original."""

    est_date: typing.Optional[str] = Field(
        default=None,
    )
    """Established date."""

    public_date_label: typing.Optional[str] = Field(
        default=None,
    )
    """Public date label."""

    photo_max_size: typing.Optional["GroupsPhotoSize"] = Field(
        default=None,
    )
    """Property `GroupsGroup.photo_max_size`."""

    is_video_live_notifications_blocked: typing.Optional[bool] = Field(
        default=None,
    )
    """Property `GroupsGroup.is_video_live_notifications_blocked`."""

    video_live: typing.Optional["VideoLiveInfo"] = Field(
        default=None,
    )
    """Property `GroupsGroup.video_live`."""


class GroupsGroupAccess(int, enum.Enum, metaclass=BaseEnumMeta):
    OPEN = 0
    CLOSED = 1
    PRIVATE = 2


class GroupsGroupAdminLevel(int, enum.Enum, metaclass=BaseEnumMeta):
    MODERATOR = 1
    EDITOR = 2
    ADMINISTRATOR = 3


class GroupsGroupAgeLimits(int, enum.Enum, metaclass=BaseEnumMeta):
    UNLIMITED = 1
    F__16_PLUS = 2
    F__18_PLUS = 3


class GroupsGroupAttach(BaseModel):
    """
    Model: `GroupsGroupAttach`
    """

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


class GroupsGroupAudio(int, enum.Enum, metaclass=BaseEnumMeta):
    DISABLED = 0
    OPEN = 1
    LIMITED = 2


class GroupsGroupBanInfo(BaseModel):
    """
    Model: `GroupsGroupBanInfo`
    """

    comment: typing.Optional[str] = Field(
        default=None,
    )
    """Ban comment."""

    end_date: typing.Optional[int] = Field(
        default=None,
    )
    """End date of ban in Unixtime."""

    reason: typing.Optional["GroupsBanInfoReason"] = Field(
        default=None,
    )
    """Property `GroupsGroupBanInfo.reason`."""


class GroupsGroupCategory(BaseModel):
    """
    Model: `GroupsGroupCategory`
    """

    id: int = Field()
    """Category ID."""

    name: str = Field()
    """Category name."""

    subcategories: typing.Optional[typing.List["GroupsGroupSubcategory"]] = Field(
        default=None,
    )
    """Property `GroupsGroupCategory.subcategories`."""


class GroupsGroupCategoryFull(BaseModel):
    """
    Model: `GroupsGroupCategoryFull`
    """

    id: int = Field()
    """Category ID."""

    name: str = Field()
    """Category name."""

    page_count: int = Field()
    """Pages number."""

    page_previews: typing.List["GroupsGroup"] = Field()
    """Property `GroupsGroupCategoryFull.page_previews`."""

    subcategories: typing.Optional[typing.List["GroupsGroupCategory"]] = Field(
        default=None,
    )
    """Property `GroupsGroupCategoryFull.subcategories`."""


class GroupsGroupCategoryType(BaseModel):
    """
    Model: `GroupsGroupCategoryType`
    """

    id: int = Field()
    """Property `GroupsGroupCategoryType.id`."""

    name: str = Field()
    """Property `GroupsGroupCategoryType.name`."""


class GroupsGroupDocs(int, enum.Enum, metaclass=BaseEnumMeta):
    DISABLED = 0
    OPEN = 1
    LIMITED = 2


class GroupsGroupFullAgeLimits(int, enum.Enum, metaclass=BaseEnumMeta):
    NO = 1
    OVER_16 = 2
    OVER_18 = 3


class GroupsGroupFullMemberStatus(int, enum.Enum, metaclass=BaseEnumMeta):
    NOT_A_MEMBER = 0
    MEMBER = 1
    NOT_SURE = 2
    DECLINED = 3
    HAS_SENT_A_REQUEST = 4
    INVITED = 5


class GroupsGroupFullSection(int, enum.Enum, metaclass=BaseEnumMeta):
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


class GroupsGroupIsClosed(int, enum.Enum, metaclass=BaseEnumMeta):
    OPEN = 0
    CLOSED = 1
    PRIVATE = 2


class GroupsGroupMarketCurrency(int, enum.Enum, metaclass=BaseEnumMeta):
    RUSSIAN_RUBLES = 643
    UKRAINIAN_HRYVNIA = 980
    KAZAKH_TENGE = 398
    EURO = 978
    US_DOLLARS = 840


class GroupsGroupPhotos(int, enum.Enum, metaclass=BaseEnumMeta):
    DISABLED = 0
    OPEN = 1
    LIMITED = 2


class GroupsGroupPublicCategoryList(BaseModel):
    """
    Model: `GroupsGroupPublicCategoryList`
    """

    id: typing.Optional[int] = Field(
        default=None,
    )
    """Property `GroupsGroupPublicCategoryList.id`."""

    name: typing.Optional[str] = Field(
        default=None,
    )
    """Property `GroupsGroupPublicCategoryList.name`."""

    subcategories: typing.Optional[typing.List["GroupsGroupCategoryType"]] = Field(
        default=None,
    )
    """Property `GroupsGroupPublicCategoryList.subcategories`."""


class GroupsGroupRole(str, enum.Enum, metaclass=BaseEnumMeta):
    MODERATOR = "moderator"
    EDITOR = "editor"
    ADMINISTRATOR = "administrator"
    ADVERTISER = "advertiser"


class GroupsGroupSubcategory(BaseModel):
    """
    Model: `GroupsGroupSubcategory`
    """

    id: int = Field()
    """Object ID."""

    name: str = Field()
    """Object name."""

    genders: typing.Optional[typing.List["BaseObjectWithName"]] = Field(
        default=None,
    )
    """Property `GroupsGroupSubcategory.genders`."""


class GroupsGroupSubject(int, enum.Enum, metaclass=BaseEnumMeta):
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


class GroupsGroupSuggestedPrivacy(int, enum.Enum, metaclass=BaseEnumMeta):
    NONE = 0
    ALL = 1
    SUBSCRIBERS = 2


class GroupsGroupTagColor(str, enum.Enum, metaclass=BaseEnumMeta):
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
    """
    Model: `GroupsGroupTag`
    """

    id: int = Field()
    """Property `GroupsGroupTag.id`."""

    name: str = Field()
    """Property `GroupsGroupTag.name`."""

    color: "GroupsGroupTagColor" = Field()
    """Property `GroupsGroupTag.color`."""

    uses: typing.Optional[int] = Field(
        default=None,
    )
    """Property `GroupsGroupTag.uses`."""


class GroupsGroupTopics(int, enum.Enum, metaclass=BaseEnumMeta):
    DISABLED = 0
    OPEN = 1
    LIMITED = 2


class GroupsGroupType(str, enum.Enum, metaclass=BaseEnumMeta):
    GROUP = "group"
    PAGE = "page"
    EVENT = "event"


class GroupsGroupVideo(int, enum.Enum, metaclass=BaseEnumMeta):
    DISABLED = 0
    OPEN = 1
    LIMITED = 2


class GroupsGroupWall(int, enum.Enum, metaclass=BaseEnumMeta):
    DISABLED = 0
    OPEN = 1
    LIMITED = 2
    CLOSED = 3


class GroupsGroupWiki(int, enum.Enum, metaclass=BaseEnumMeta):
    DISABLED = 0
    OPEN = 1
    LIMITED = 2


class GroupsGroupsArray(BaseModel):
    """
    Model: `GroupsGroupsArray`
    """

    count: int = Field()
    """Communities number."""

    items: typing.List[int] = Field()
    """Property `GroupsGroupsArray.items`."""


class GroupsLinksItem(BaseModel):
    """
    Model: `GroupsLinksItem`
    """

    name: typing.Optional[str] = Field(
        default=None,
    )
    """Link title."""

    desc: typing.Optional[str] = Field(
        default=None,
    )
    """Link description."""

    edit_title: typing.Optional[bool] = Field(
        default=None,
    )
    """Information whether the link title can be edited."""

    id: typing.Optional[int] = Field(
        default=None,
    )
    """Link ID."""

    photo_100: typing.Optional[str] = Field(
        default=None,
    )
    """URL of square image of the link with 100 pixels in width."""

    photo_50: typing.Optional[str] = Field(
        default=None,
    )
    """URL of square image of the link with 50 pixels in width."""

    url: typing.Optional[str] = Field(
        default=None,
    )
    """Link URL."""

    image_processing: typing.Optional[bool] = Field(
        default=None,
    )
    """Information whether the image on processing."""


class GroupsLiveCovers(BaseModel):
    """
    Model: `GroupsLiveCovers`
    """

    is_enabled: bool = Field()
    """Information whether live covers is enabled."""

    is_scalable: typing.Optional[bool] = Field(
        default=None,
    )
    """Information whether live covers photo scaling is enabled."""

    story_ids: typing.Optional[typing.List[str]] = Field(
        default=None,
    )
    """Property `GroupsLiveCovers.story_ids`."""


class GroupsLongPollEvents(BaseModel):
    """
    Model: `GroupsLongPollEvents`
    """

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

    lead_forms_new: typing.Optional[bool] = Field(
        default=None,
    )
    """Property `GroupsLongPollEvents.lead_forms_new`."""

    market_order_new: typing.Optional[bool] = Field(
        default=None,
    )
    """Property `GroupsLongPollEvents.market_order_new`."""

    market_order_edit: typing.Optional[bool] = Field(
        default=None,
    )
    """Property `GroupsLongPollEvents.market_order_edit`."""


class GroupsLongPollServer(BaseModel):
    """
    Model: `GroupsLongPollServer`
    """

    key: str = Field()
    """Long Poll key."""

    server: str = Field()
    """Long Poll server address."""

    ts: str = Field()
    """Number of the last event."""


class GroupsLongPollSettings(BaseModel):
    """
    Model: `GroupsLongPollSettings`
    """

    events: "GroupsLongPollEvents" = Field()
    """Property `GroupsLongPollSettings.events`."""

    is_enabled: bool = Field()
    """Shows whether Long Poll is enabled."""

    api_version: typing.Optional[str] = Field(
        default=None,
    )
    """API version used for the events."""


class GroupsMarketInfo(BaseModel):
    """
    Model: `GroupsMarketInfo`
    """

    type: typing.Optional[str] = Field(
        default=None,
    )
    """Market type."""

    contact_id: typing.Optional[int] = Field(
        default=None,
    )
    """Contact person ID."""

    currency: typing.Optional["MarketCurrency"] = Field(
        default=None,
    )
    """Property `GroupsMarketInfo.currency`."""

    currency_text: typing.Optional[str] = Field(
        default=None,
    )
    """Currency name."""

    enabled: typing.Optional[bool] = Field(
        default=None,
    )
    """Information whether the market is enabled."""

    main_album_id: typing.Optional[int] = Field(
        default=None,
    )
    """Main market album ID."""

    price_max: typing.Optional[str] = Field(
        default=None,
    )
    """Maximum price."""

    price_min: typing.Optional[str] = Field(
        default=None,
    )
    """Minimum price."""

    min_order_price: typing.Optional["MarketPrice"] = Field(
        default=None,
    )
    """Property `GroupsMarketInfo.min_order_price`."""


class GroupsMarketProperties(BaseModel):
    """
    Model: `GroupsMarketProperties`
    """

    market: typing.Optional["GroupsMarketInfo"] = Field(
        default=None,
    )
    """Property `GroupsMarketProperties.market`."""

    has_market_app: typing.Optional[bool] = Field(
        default=None,
    )
    """Information whether community has installed market app."""

    using_vkpay_market_app: typing.Optional[bool] = Field(
        default=None,
    )
    """Property `GroupsMarketProperties.using_vkpay_market_app`."""


class GroupsMarketState(str, enum.Enum, metaclass=BaseEnumMeta):
    NONE = "none"
    BASIC = "basic"
    ADVANCED = "advanced"


class GroupsMemberRole(BaseModel):
    """
    Model: `GroupsMemberRole`
    """

    id: int = Field()
    """User ID."""

    is_call_operator: typing.Optional[bool] = Field(
        default=None,
    )
    """Allow the manager to accept community calls.."""

    permissions: typing.Optional[typing.List["GroupsMemberRolePermission"]] = Field(
        default=None,
    )
    """Property `GroupsMemberRole.permissions`."""

    role: typing.Optional["GroupsMemberRoleStatus"] = Field(
        default=None,
    )
    """Property `GroupsMemberRole.role`."""


class GroupsMemberRolePermission(str, enum.Enum, metaclass=BaseEnumMeta):
    ADS = "ads"


class GroupsMemberRoleStatus(str, enum.Enum, metaclass=BaseEnumMeta):
    MODERATOR = "moderator"
    EDITOR = "editor"
    ADMINISTRATOR = "administrator"
    CREATOR = "creator"
    ADVERTISER = "advertiser"


class GroupsMemberStatus(BaseModel):
    """
    Model: `GroupsMemberStatus`
    """

    member: bool = Field()
    """Information whether user is a member of the group."""

    user_id: int = Field()
    """User ID."""


class GroupsMemberStatusFull(BaseModel):
    """
    Model: `GroupsMemberStatusFull`
    """

    member: bool = Field()
    """Information whether user is a member of the group."""

    user_id: int = Field()
    """User ID."""

    can_invite: typing.Optional[bool] = Field(
        default=None,
    )
    """Information whether user can be invited."""

    can_recall: typing.Optional[bool] = Field(
        default=None,
    )
    """Information whether user\'s invite to the group can be recalled."""

    invitation: typing.Optional[bool] = Field(
        default=None,
    )
    """Information whether user has been invited to the group."""

    request: typing.Optional[bool] = Field(
        default=None,
    )
    """Information whether user has send request to the group."""


class GroupsOnlineStatus(BaseModel):
    """
    Online status of group
    Model: `GroupsOnlineStatus`
    """

    status: "GroupsOnlineStatusType" = Field()
    """Property `GroupsOnlineStatus.status`."""

    minutes: typing.Optional[int] = Field(
        default=None,
    )
    """Estimated time of answer (for status = answer_mark)."""


class GroupsOnlineStatusType(str, enum.Enum, metaclass=BaseEnumMeta):
    NONE = "none"
    ONLINE = "online"
    ANSWER_MARK = "answer_mark"


class GroupsOwnerXtrBanInfoType(str, enum.Enum, metaclass=BaseEnumMeta):
    GROUP = "group"
    PROFILE = "profile"


class GroupsOwnerXtrBanInfo(BaseModel):
    """
    Model: `GroupsOwnerXtrBanInfo`
    """

    ban_info: typing.Optional["GroupsBanInfo"] = Field(
        default=None,
    )
    """Property `GroupsOwnerXtrBanInfo.ban_info`."""

    group: typing.Optional["GroupsGroup"] = Field(
        default=None,
    )
    """Information about group if type = group."""

    profile: typing.Optional["UsersUser"] = Field(
        default=None,
    )
    """Information about group if type = profile."""

    type: typing.Optional["GroupsOwnerXtrBanInfoType"] = Field(
        default=None,
    )
    """Property `GroupsOwnerXtrBanInfo.type`."""


class GroupsPhotoSize(BaseModel):
    """
    Model: `GroupsPhotoSize`
    """

    height: int = Field()
    """Image height."""

    width: int = Field()
    """Image width."""


class GroupsProfileItem(BaseModel):
    """
    Model: `GroupsProfileItem`
    """

    id: int = Field()
    """User id."""

    photo_50: str = Field()
    """Url for user photo."""

    photo_100: str = Field()
    """Url for user photo."""

    first_name: str = Field()
    """User first name."""

    last_name: typing.Optional[str] = Field(
        default=None,
    )
    """User last name."""

    screen_name: typing.Optional[str] = Field(
        default=None,
    )
    """Domain of the user page."""


class GroupsRoleOptions(str, enum.Enum, metaclass=BaseEnumMeta):
    MODERATOR = "moderator"
    EDITOR = "editor"
    ADMINISTRATOR = "administrator"
    CREATOR = "creator"


class GroupsSectionsListItem(BaseModel):
    """
    Model: `GroupsSectionsListItem`
    """

    id: int = Field()
    """Object ID."""

    title: str = Field()
    """Object title."""


class GroupsSettingsTwitterStatus(str, enum.Enum, metaclass=BaseEnumMeta):
    LOADING = "loading"
    SYNC = "sync"


class GroupsSettingsTwitter(BaseModel):
    """
    Model: `GroupsSettingsTwitter`
    """

    status: "GroupsSettingsTwitterStatus" = Field()
    """Property `GroupsSettingsTwitter.status`."""

    name: typing.Optional[str] = Field(
        default=None,
    )
    """Property `GroupsSettingsTwitter.name`."""


class GroupsSubjectItem(BaseModel):
    """
    Model: `GroupsSubjectItem`
    """

    id: int = Field()
    """Subject ID."""

    name: str = Field()
    """Subject title."""


class GroupsTokenPermissionSetting(BaseModel):
    """
    Model: `GroupsTokenPermissionSetting`
    """

    name: str = Field()
    """Property `GroupsTokenPermissionSetting.name`."""

    setting: int = Field()
    """Property `GroupsTokenPermissionSetting.setting`."""


class LeadFormsAnswer(BaseModel):
    """
    Model: `LeadFormsAnswer`
    """

    key: str = Field()
    """Property `LeadFormsAnswer.key`."""

    answer: "LeadFormsAnswerOneOf" = Field()
    """Property `LeadFormsAnswer.answer`."""


class LeadFormsAnswerItem(BaseModel):
    """
    Model: `LeadFormsAnswerItem`
    """

    value: str = Field()
    """Property `LeadFormsAnswerItem.value`."""

    key: typing.Optional[str] = Field(
        default=None,
    )
    """Property `LeadFormsAnswerItem.key`."""


class LeadFormsAnswerOneOf(BaseModel):
    """
    Model: `LeadFormsAnswerOneOf`
    """


class LeadFormsForm(BaseModel):
    """
    Model: `LeadFormsForm`
    """

    form_id: int = Field()
    """Property `LeadFormsForm.form_id`."""

    group_id: int = Field()
    """Property `LeadFormsForm.group_id`."""

    leads_count: int = Field()
    """Property `LeadFormsForm.leads_count`."""

    url: str = Field()
    """Property `LeadFormsForm.url`."""

    photo: typing.Optional[str] = Field(
        default=None,
    )
    """Property `LeadFormsForm.photo`."""

    name: typing.Optional[str] = Field(
        default=None,
    )
    """Property `LeadFormsForm.name`."""

    title: typing.Optional[str] = Field(
        default=None,
    )
    """Property `LeadFormsForm.title`."""

    description: typing.Optional[str] = Field(
        default=None,
    )
    """Property `LeadFormsForm.description`."""

    confirmation: typing.Optional[str] = Field(
        default=None,
    )
    """Property `LeadFormsForm.confirmation`."""

    site_link_url: typing.Optional[str] = Field(
        default=None,
    )
    """Property `LeadFormsForm.site_link_url`."""

    policy_link_url: typing.Optional[str] = Field(
        default=None,
    )
    """Property `LeadFormsForm.policy_link_url`."""

    questions: typing.Optional[typing.List["LeadFormsQuestionItem"]] = Field(
        default=None,
    )
    """Property `LeadFormsForm.questions`."""

    active: typing.Optional[bool] = Field(
        default=None,
    )
    """Property `LeadFormsForm.active`."""

    pixel_code: typing.Optional[str] = Field(
        default=None,
    )
    """Property `LeadFormsForm.pixel_code`."""

    once_per_user: typing.Optional[int] = Field(
        default=None,
    )
    """Property `LeadFormsForm.once_per_user`."""

    notify_admins: typing.Optional[str] = Field(
        default=None,
    )
    """Property `LeadFormsForm.notify_admins`."""

    notify_emails: typing.Optional[str] = Field(
        default=None,
    )
    """Property `LeadFormsForm.notify_emails`."""


class LeadFormsLead(BaseModel):
    """
    Model: `LeadFormsLead`
    """

    lead_id: int = Field()
    """Property `LeadFormsLead.lead_id`."""

    user_id: int = Field()
    """Property `LeadFormsLead.user_id`."""

    date: int = Field()
    """Property `LeadFormsLead.date`."""

    answers: typing.List["LeadFormsAnswer"] = Field()
    """Property `LeadFormsLead.answers`."""

    ad_id: typing.Optional[int] = Field(
        default=None,
    )
    """Property `LeadFormsLead.ad_id`."""


class LeadFormsQuestionItemType(str, enum.Enum, metaclass=BaseEnumMeta):
    INPUT = "input"
    TEXTAREA = "textarea"
    RADIO = "radio"
    CHECKBOX = "checkbox"
    SELECT = "select"


class LeadFormsQuestionItem(BaseModel):
    """
    Model: `LeadFormsQuestionItem`
    """

    key: str = Field()
    """Property `LeadFormsQuestionItem.key`."""

    type: "LeadFormsQuestionItemType" = Field()
    """Property `LeadFormsQuestionItem.type`."""

    label: typing.Optional[str] = Field(
        default=None,
    )
    """Property `LeadFormsQuestionItem.label`."""

    options: typing.Optional[typing.List["LeadFormsQuestionItemOption"]] = Field(
        default=None,
    )
    """Опции выбора для типов radio, checkbox, select."""


class LeadFormsQuestionItemOption(BaseModel):
    """
    Model: `LeadFormsQuestionItemOption`
    """

    label: str = Field()
    """Property `LeadFormsQuestionItemOption.label`."""

    key: typing.Optional[str] = Field(
        default=None,
    )
    """Property `LeadFormsQuestionItemOption.key`."""


class LikesType(str, enum.Enum, metaclass=BaseEnumMeta):
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
    """
    Model: `LinkTargetObject`
    """

    type: typing.Optional[str] = Field(
        default=None,
    )
    """Object type."""

    owner_id: typing.Optional[int] = Field(
        default=None,
    )
    """Owner ID."""

    item_id: typing.Optional[int] = Field(
        default=None,
    )
    """Item ID."""


class MarketCurrency(BaseModel):
    """
    Model: `MarketCurrency`
    """

    id: int = Field()
    """Currency ID."""

    name: str = Field()
    """Currency sign."""

    title: str = Field()
    """Currency title."""


class MarketGlobalSearchFilters(BaseModel):
    """
    Model: `MarketGlobalSearchFilters`
    """

    city: typing.Optional["BaseCity"] = Field(
        default=None,
    )
    """Property `MarketGlobalSearchFilters.city`."""

    country: typing.Optional["BaseCountry"] = Field(
        default=None,
    )
    """Property `MarketGlobalSearchFilters.country`."""


class MarketItemOwnerInfo(BaseModel):
    """
    Information about the group where the item is placed
    Model: `MarketItemOwnerInfo`
    """

    avatar: typing.Optional[typing.List["BaseImage"]] = Field(
        default=None,
    )
    """Avatar of the group."""

    name: typing.Optional[str] = Field(
        default=None,
    )
    """Name of the group."""

    category: typing.Optional[str] = Field(
        default=None,
    )
    """Category of the item or description of the group."""

    category_url: typing.Optional[str] = Field(
        default=None,
    )
    """Link to the section of the group."""

    is_corporated_market: typing.Optional[bool] = Field(
        default=None,
    )
    """Is the group is VK corporated market."""

    market_type: typing.Optional["MarketOwnerType"] = Field(
        default=None,
    )
    """Type of the market group."""


class MarketItemPromotionInfo(BaseModel):
    """
    Information about promotion of the market item
    Model: `MarketItemPromotionInfo`
    """

    is_available: typing.Optional[bool] = Field(
        default=None,
    )
    """Can the item be promoted?."""


class MarketMarketAlbum(BaseModel):
    """
    Model: `MarketMarketAlbum`
    """

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

    is_main: typing.Optional[bool] = Field(
        default=None,
    )
    """Is album main for owner."""

    is_hidden: typing.Optional[bool] = Field(
        default=None,
    )
    """Is album hidden."""

    photo: typing.Optional["PhotosPhoto"] = Field(
        default=None,
    )
    """Property `MarketMarketAlbum.photo`."""

    type: typing.Optional[int] = Field(
        default=None,
    )
    """Type of album."""

    is_blur_enabled: typing.Optional[bool] = Field(
        default=None,
    )
    """Is album needed to be blurred (18+) or not."""


class MarketMarketCategoryInnerType(str, enum.Enum, metaclass=BaseEnumMeta):
    MARKET_MARKET_CATEGORY_NESTED = "market_market_category_nested"


class MarketMarketCategory(BaseModel):
    """
    Model: `MarketMarketCategory`
    """

    inner_type: "MarketMarketCategoryInnerType" = Field()
    """Property `MarketMarketCategory.inner_type`."""

    id: int = Field()
    """Category ID."""

    name: str = Field()
    """Category name."""

    is_v2: typing.Optional[bool] = Field(
        default=None,
    )
    """Is v2 category."""

    parent: typing.Optional["MarketMarketCategoryNested"] = Field(
        default=None,
    )
    """Property `MarketMarketCategory.parent`."""


class MarketMarketCategoryNestedInnerType(str, enum.Enum, metaclass=BaseEnumMeta):
    MARKET_MARKET_CATEGORY_NESTED = "market_market_category_nested"


class MarketMarketCategoryNested(BaseModel):
    """
    Model: `MarketMarketCategoryNested`
    """

    inner_type: "MarketMarketCategoryNestedInnerType" = Field()
    """Property `MarketMarketCategoryNested.inner_type`."""

    id: int = Field()
    """Category ID."""

    name: str = Field()
    """Category name."""

    is_v2: typing.Optional[bool] = Field(
        default=None,
    )
    """Is v2 category."""

    parent: typing.Optional["MarketMarketCategoryNested"] = Field(
        default=None,
    )
    """Property `MarketMarketCategoryNested.parent`."""


class MarketMarketCategoryTree(BaseModel):
    """
    Model: `MarketMarketCategoryTree`
    """

    id: int = Field()
    """Category ID."""

    name: str = Field()
    """Category name."""

    icon_name: typing.Optional[str] = Field(
        default=None,
    )
    """Icon name."""

    children: typing.Optional[typing.List["MarketMarketCategoryTree"]] = Field(
        default=None,
    )
    """Property `MarketMarketCategoryTree.children`."""

    view: typing.Optional["MarketMarketCategoryTreeView"] = Field(
        default=None,
    )
    """Property `MarketMarketCategoryTree.view`."""

    url: typing.Optional[str] = Field(
        default=None,
    )
    """SEO-friendly URL to page with category\'s items."""

    seo_name: typing.Optional[str] = Field(
        default=None,
    )
    """SEO-friendly variant of category\'s name."""

    page_title: typing.Optional[str] = Field(
        default=None,
    )
    """Title for category\'s page. Used for SEO."""

    page_description: typing.Optional[str] = Field(
        default=None,
    )
    """Description for category\'s page. Used for SEO."""


class MarketMarketCategoryTreeViewType(str, enum.Enum, metaclass=BaseEnumMeta):
    TAB_ROOT = "tab_root"


class MarketMarketCategoryTreeView(BaseModel):
    """
    Model: `MarketMarketCategoryTreeView`
    """

    type: typing.Optional["MarketMarketCategoryTreeViewType"] = Field(
        default=None,
    )
    """Property `MarketMarketCategoryTreeView.type`."""

    selected: typing.Optional[bool] = Field(
        default=None,
    )
    """Property `MarketMarketCategoryTreeView.selected`."""

    root_path: typing.Optional[typing.List[str]] = Field(
        default=None,
    )
    """Property `MarketMarketCategoryTreeView.root_path`."""


class MarketMarketItem(BaseModel):
    """
    Model: `MarketMarketItem`
    """

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

    access_key: typing.Optional[str] = Field(
        default=None,
    )
    """Access key for the market item."""

    button_title: typing.Optional[str] = Field(
        default=None,
    )
    """Title for button for url."""

    category_v2: typing.Optional["MarketMarketCategory"] = Field(
        default=None,
    )
    """Property `MarketMarketItem.category_v2`."""

    date: typing.Optional[int] = Field(
        default=None,
    )
    """Date when the item has been created in Unixtime."""

    external_id: typing.Optional[str] = Field(
        default=None,
    )
    """Property `MarketMarketItem.external_id`."""

    is_favorite: typing.Optional[bool] = Field(
        default=None,
    )
    """Property `MarketMarketItem.is_favorite`."""

    is_owner: typing.Optional[bool] = Field(
        default=None,
    )
    """Property `MarketMarketItem.is_owner`."""

    is_adult: typing.Optional[bool] = Field(
        default=None,
    )
    """Property `MarketMarketItem.is_adult`."""

    thumb_photo: typing.Optional[str] = Field(
        default=None,
    )
    """URL of the preview image."""

    url: typing.Optional[str] = Field(
        default=None,
    )
    """URL to item."""

    variants_grouping_id: typing.Optional[int] = Field(
        default=None,
    )
    """Property `MarketMarketItem.variants_grouping_id`."""

    is_main_variant: typing.Optional[bool] = Field(
        default=None,
    )
    """Property `MarketMarketItem.is_main_variant`."""

    sku: typing.Optional[str] = Field(
        default=None,
    )
    """Property `MarketMarketItem.sku`."""

    stock_amount: typing.Optional[int] = Field(
        default=None,
    )
    """Inventory balances."""

    post_id: typing.Optional[int] = Field(
        default=None,
    )
    """Attach for post id."""

    post_owner_id: typing.Optional[int] = Field(
        default=None,
    )
    """Attach for post owner id."""


class MarketMarketItemAvailability(int, enum.Enum, metaclass=BaseEnumMeta):
    AVAILABLE = 0
    REMOVED = 1
    UNAVAILABLE = 2


class MarketMarketItemBasic(BaseModel):
    """
    Model: `MarketMarketItemBasic`
    """

    id: int = Field()
    """Item ID."""

    owner_id: int = Field()
    """Item owner\'s ID."""

    title: str = Field()
    """Item title."""

    price: "MarketPrice" = Field()
    """Property `MarketMarketItemBasic.price`."""

    thumb_photo: typing.Optional[str] = Field(
        default=None,
    )
    """URL of the preview image."""

    is_favorite: typing.Optional[bool] = Field(
        default=None,
    )
    """Property `MarketMarketItemBasic.is_favorite`."""


class MarketOrder(BaseModel):
    """
    Model: `MarketOrder`
    """

    id: int = Field()
    """Property `MarketOrder.id`."""

    group_id: int = Field()
    """Property `MarketOrder.group_id`."""

    user_id: int = Field()
    """Property `MarketOrder.user_id`."""

    date: int = Field()
    """Property `MarketOrder.date`."""

    status: int = Field()
    """Property `MarketOrder.status`."""

    items_count: int = Field()
    """Property `MarketOrder.items_count`."""

    total_price: "MarketPrice" = Field()
    """Property `MarketOrder.total_price`."""

    display_order_id: typing.Optional[str] = Field(
        default=None,
    )
    """Property `MarketOrder.display_order_id`."""

    track_number: typing.Optional[str] = Field(
        default=None,
    )
    """Property `MarketOrder.track_number`."""

    track_link: typing.Optional[str] = Field(
        default=None,
    )
    """Property `MarketOrder.track_link`."""

    comment: typing.Optional[str] = Field(
        default=None,
    )
    """Property `MarketOrder.comment`."""

    address: typing.Optional[str] = Field(
        default=None,
    )
    """Property `MarketOrder.address`."""

    merchant_comment: typing.Optional[str] = Field(
        default=None,
    )
    """Property `MarketOrder.merchant_comment`."""

    weight: typing.Optional[int] = Field(
        default=None,
    )
    """Property `MarketOrder.weight`."""

    discount: typing.Optional["MarketPrice"] = Field(
        default=None,
    )
    """Property `MarketOrder.discount`."""

    preview_order_items: typing.Optional[typing.List["MarketOrderItem"]] = Field(
        default=None,
    )
    """Several order items for preview."""

    cancel_info: typing.Optional["BaseLink"] = Field(
        default=None,
    )
    """Information for cancel and revert order."""

    comment_for_user: typing.Optional[str] = Field(
        default=None,
    )
    """Seller comment for user."""

    is_viewed_by_admin: typing.Optional[bool] = Field(
        default=None,
    )
    """Property `MarketOrder.is_viewed_by_admin`."""

    date_viewed: typing.Optional[int] = Field(
        default=None,
    )
    """Property `MarketOrder.date_viewed`."""

    can_add_review: typing.Optional[bool] = Field(
        default=None,
    )
    """Extended field. Can current viewer add review for at least one item in this order."""


class MarketOrderItem(BaseModel):
    """
    Model: `MarketOrderItem`
    """

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

    title: typing.Optional[str] = Field(
        default=None,
    )
    """Property `MarketOrderItem.title`."""

    photo: typing.Optional["PhotosPhoto"] = Field(
        default=None,
    )
    """Property `MarketOrderItem.photo`."""

    variants: typing.Optional[typing.List[str]] = Field(
        default=None,
    )
    """Property `MarketOrderItem.variants`."""

    can_add_review: typing.Optional[bool] = Field(
        default=None,
    )
    """Extended field. Can current viewer add review for this ordered item."""


class MarketOwnerType(str, enum.Enum, metaclass=BaseEnumMeta):
    BASE = "base"
    PRO = "pro"
    DISABLED = "disabled"


class MarketPrice(BaseModel):
    """
    Model: `MarketPrice`
    """

    amount: str = Field()
    """Amount."""

    currency: "MarketCurrency" = Field()
    """Property `MarketPrice.currency`."""

    text: str = Field()
    """Text."""

    amount_to: typing.Optional[str] = Field(
        default=None,
    )
    """Amount to for price_type=2."""

    price_type: typing.Optional[int] = Field(
        default=None,
    )
    """Property `MarketPrice.price_type`."""

    price_unit: typing.Optional[int] = Field(
        default=None,
    )
    """Property `MarketPrice.price_unit`."""

    discount_rate: typing.Optional[int] = Field(
        default=None,
    )
    """Property `MarketPrice.discount_rate`."""

    old_amount: typing.Optional[str] = Field(
        default=None,
    )
    """Property `MarketPrice.old_amount`."""

    old_amount_text: typing.Optional[str] = Field(
        default=None,
    )
    """Textual representation of old price."""


class MarketPropertyType(str, enum.Enum, metaclass=BaseEnumMeta):
    TEXT = "text"
    COLOR = "color"


class MarketProperty(BaseModel):
    """
    Model: `MarketProperty`
    """

    id: int = Field()
    """Property `MarketProperty.id`."""

    title: str = Field()
    """Property name."""

    variants: typing.List["MarketPropertyVariant"] = Field()
    """Property `MarketProperty.variants`."""

    type: typing.Optional["MarketPropertyType"] = Field(
        default=None,
    )
    """Property type."""


class MarketPropertyVariant(BaseModel):
    """
    Model: `MarketPropertyVariant`
    """

    id: int = Field()
    """Property `MarketPropertyVariant.id`."""

    title: str = Field()
    """Property name."""

    value: typing.Optional[str] = Field(
        default=None,
    )
    """Property value corresponding to property type."""


class MarketServicesViewType(int, enum.Enum, metaclass=BaseEnumMeta):
    CARDS = 1
    ROWS = 2


class MarketUploadPhotoData(BaseModel):
    """
    Model: `MarketUploadPhotoData`
    """

    photo_id: int = Field()
    """Photo ID."""

    photo: typing.Optional["PhotosPhoto"] = Field(
        default=None,
    )
    """Property `MarketUploadPhotoData.photo`."""


class NotesNote(BaseModel):
    """
    Model: `NotesNote`
    """

    comments: int = Field()
    """Comments number."""

    date: int = Field()
    """Date when the note has been created in Unixtime."""

    id: int = Field()
    """Note ID."""

    owner_id: int = Field()
    """Note owner\'s ID."""

    title: str = Field()
    """Note title."""

    view_url: str = Field()
    """URL of the page with note preview."""

    read_comments: typing.Optional[int] = Field(
        default=None,
    )
    """Property `NotesNote.read_comments`."""

    can_comment: typing.Optional[bool] = Field(
        default=None,
    )
    """Information whether current user can comment the note."""

    text: typing.Optional[str] = Field(
        default=None,
    )
    """Note text."""

    text_wiki: typing.Optional[str] = Field(
        default=None,
    )
    """Note text in wiki format."""

    privacy_view: typing.Optional[typing.List[str]] = Field(
        default=None,
    )
    """Property `NotesNote.privacy_view`."""

    privacy_comment: typing.Optional[typing.List[str]] = Field(
        default=None,
    )
    """Property `NotesNote.privacy_comment`."""


class NotesNoteComment(BaseModel):
    """
    Model: `NotesNoteComment`
    """

    date: int = Field()
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

    reply_to: typing.Optional[int] = Field(
        default=None,
    )
    """ID of replied comment ."""


class NotificationsFeedback(BaseModel):
    """
    Model: `NotificationsFeedback`
    """

    attachments: typing.Optional[typing.List["WallWallpostAttachment"]] = Field(
        default=None,
    )
    """Property `NotificationsFeedback.attachments`."""

    from_id: typing.Optional[int] = Field(
        default=None,
    )
    """Reply author\'s ID."""

    geo: typing.Optional["BaseGeo"] = Field(
        default=None,
    )
    """Property `NotificationsFeedback.geo`."""

    id: typing.Optional[int] = Field(
        default=None,
    )
    """Item ID."""

    likes: typing.Optional["BaseLikesInfo"] = Field(
        default=None,
    )
    """Property `NotificationsFeedback.likes`."""

    text: typing.Optional[str] = Field(
        default=None,
    )
    """Reply text."""

    to_id: typing.Optional[int] = Field(
        default=None,
    )
    """Wall owner\'s ID."""


class NotificationsNotificationInnerType(str, enum.Enum, metaclass=BaseEnumMeta):
    NOTIFICATIONS_NOTIFICATION = "notifications_notification"


class NotificationsNotification(BaseModel):
    """
    Model: `NotificationsNotification`
    """

    inner_type: "NotificationsNotificationInnerType" = Field()
    """Property `NotificationsNotification.inner_type`."""

    date: typing.Optional[int] = Field(
        default=None,
    )
    """Date when the event has been occurred."""

    feedback: typing.Optional["NotificationsFeedback"] = Field(
        default=None,
    )
    """Property `NotificationsNotification.feedback`."""

    parent: typing.Optional["NotificationsNotification"] = Field(
        default=None,
    )
    """Property `NotificationsNotification.parent`."""

    reply: typing.Optional["NotificationsReply"] = Field(
        default=None,
    )
    """Property `NotificationsNotification.reply`."""

    type: typing.Optional[str] = Field(
        default=None,
    )
    """Notification type."""


class NotificationsNotificationItemInnerType(str, enum.Enum, metaclass=BaseEnumMeta):
    NOTIFICATIONS_NOTIFICATION = "notifications_notification"


class NotificationsNotificationItem(BaseModel):
    """
    Model: `NotificationsNotificationItem`
    """

    inner_type: "NotificationsNotificationItemInnerType" = Field()
    """Property `NotificationsNotificationItem.inner_type`."""

    date: typing.Optional[int] = Field(
        default=None,
    )
    """Date when the event has been occurred."""

    feedback: typing.Optional["NotificationsFeedback"] = Field(
        default=None,
    )
    """Property `NotificationsNotificationItem.feedback`."""

    parent: typing.Optional["NotificationsNotification"] = Field(
        default=None,
    )
    """Property `NotificationsNotificationItem.parent`."""

    reply: typing.Optional["NotificationsReply"] = Field(
        default=None,
    )
    """Property `NotificationsNotificationItem.reply`."""

    type: typing.Optional[str] = Field(
        default=None,
    )
    """Notification type."""


class NotificationsReply(BaseModel):
    """
    Model: `NotificationsReply`
    """

    date: typing.Optional[int] = Field(
        default=None,
    )
    """Date when the reply has been created in Unixtime."""

    id: typing.Optional[int] = Field(
        default=None,
    )
    """Reply ID."""

    text: typing.Optional[int] = Field(
        default=None,
    )
    """Reply text."""


class NotificationsSendMessageError(BaseModel):
    """
    Model: `NotificationsSendMessageError`
    """

    code: typing.Optional[int] = Field(
        default=None,
    )
    """Error code."""

    description: typing.Optional[str] = Field(
        default=None,
    )
    """Error description."""


class NotificationsSendMessageItem(BaseModel):
    """
    Model: `NotificationsSendMessageItem`
    """

    user_id: typing.Optional[int] = Field(
        default=None,
    )
    """User ID."""

    status: typing.Optional[bool] = Field(
        default=None,
    )
    """Notification status."""

    error: typing.Optional["NotificationsSendMessageError"] = Field(
        default=None,
    )
    """Property `NotificationsSendMessageItem.error`."""


class OauthError(BaseModel):
    """
    Model: `OauthError`
    """

    error: str = Field()
    """Error type."""

    error_description: str = Field()
    """Error description."""

    redirect_uri: typing.Optional[str] = Field(
        default=None,
    )
    """URI for validation."""


class OrdersAmount(BaseModel):
    """
    Model: `OrdersAmount`
    """

    amounts: typing.Optional[typing.List["OrdersAmountItem"]] = Field(
        default=None,
    )
    """Property `OrdersAmount.amounts`."""

    currency: typing.Optional[str] = Field(
        default=None,
    )
    """Currency name."""


class OrdersAmountItem(BaseModel):
    """
    Model: `OrdersAmountItem`
    """

    amount: typing.Optional[float] = Field(
        default=None,
    )
    """Votes amount in user\'s currency."""

    description: typing.Optional[str] = Field(
        default=None,
    )
    """Amount description."""

    votes: typing.Optional[str] = Field(
        default=None,
    )
    """Votes number."""


class OrdersOrderStatus(str, enum.Enum, metaclass=BaseEnumMeta):
    CREATED = "created"
    CHARGED = "charged"
    REFUNDED = "refunded"
    CHARGEABLE = "chargeable"
    CANCELLED = "cancelled"
    DECLINED = "declined"


class OrdersOrder(BaseModel):
    """
    Model: `OrdersOrder`
    """

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

    cancel_transaction_id: typing.Optional[str] = Field(
        default=None,
    )
    """Cancel transaction ID."""

    transaction_id: typing.Optional[str] = Field(
        default=None,
    )
    """Transaction ID."""


class OrdersSubscription(BaseModel):
    """
    Model: `OrdersSubscription`
    """

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

    cancel_reason: typing.Optional[str] = Field(
        default=None,
    )
    """Cancel reason."""

    next_bill_time: typing.Optional[int] = Field(
        default=None,
    )
    """Date of next bill in Unixtime."""

    expire_time: typing.Optional[int] = Field(
        default=None,
    )
    """Subscription expiration time in Unixtime."""

    pending_cancel: typing.Optional[bool] = Field(
        default=None,
    )
    """Pending cancel state."""

    title: typing.Optional[str] = Field(
        default=None,
    )
    """Subscription name."""

    app_id: typing.Optional[int] = Field(
        default=None,
    )
    """Subscription\'s application id."""

    application_name: typing.Optional[str] = Field(
        default=None,
    )
    """Subscription\'s application name."""

    photo_url: typing.Optional[str] = Field(
        default=None,
    )
    """Item photo image url."""

    test_mode: typing.Optional[bool] = Field(
        default=None,
    )
    """Is test subscription."""

    trial_expire_time: typing.Optional[int] = Field(
        default=None,
    )
    """Date of trial expire in Unixtime."""

    is_game: typing.Optional[bool] = Field(
        default=None,
    )
    """Is game (not miniapp) subscription."""


class OwnerState(BaseModel):
    """
    Model: `OwnerState`
    """

    state: typing.Optional[int] = Field(
        default=None,
    )
    """Property `OwnerState.state`."""

    description: typing.Optional[str] = Field(
        default=None,
    )
    """wiki text to describe user state."""


class PagesPrivacySettings(int, enum.Enum, metaclass=BaseEnumMeta):
    COMMUNITY_MANAGERS_ONLY = 0
    COMMUNITY_MEMBERS_ONLY = 1
    EVERYONE = 2


class PagesWikipage(BaseModel):
    """
    Model: `PagesWikipage`
    """

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

    creator_id: typing.Optional[int] = Field(
        default=None,
    )
    """Page creator ID."""

    creator_name: typing.Optional[str] = Field(
        default=None,
    )
    """Page creator name."""

    editor_id: typing.Optional[int] = Field(
        default=None,
    )
    """Last editor ID."""

    editor_name: typing.Optional[str] = Field(
        default=None,
    )
    """Last editor name."""


class PagesWikipageFull(BaseModel):
    """
    Model: `PagesWikipageFull`
    """

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

    creator_id: typing.Optional[int] = Field(
        default=None,
    )
    """Page creator ID."""

    current_user_can_edit: typing.Optional[bool] = Field(
        default=None,
    )
    """Information whether current user can edit the page."""

    current_user_can_edit_access: typing.Optional[bool] = Field(
        default=None,
    )
    """Information whether current user can edit the page access settings."""

    editor_id: typing.Optional[int] = Field(
        default=None,
    )
    """Last editor ID."""

    html: typing.Optional[str] = Field(
        default=None,
    )
    """Page content, HTML."""

    source: typing.Optional[str] = Field(
        default=None,
    )
    """Page content, wiki."""

    url: typing.Optional[str] = Field(
        default=None,
    )
    """URL."""

    parent: typing.Optional[str] = Field(
        default=None,
    )
    """Parent."""

    parent2: typing.Optional[str] = Field(
        default=None,
    )
    """Parent2."""

    owner_id: typing.Optional[int] = Field(
        default=None,
    )
    """Owner ID."""


class PagesWikipageHistory(BaseModel):
    """
    Model: `PagesWikipageHistory`
    """

    id: int = Field()
    """Version ID."""

    length: int = Field()
    """Page size in bytes."""

    date: int = Field()
    """Date when the page has been edited in Unixtime."""

    editor_id: int = Field()
    """Last editor ID."""

    editor_name: str = Field()
    """Last editor name."""


class PhotosImage(BaseModel):
    """
    Model: `PhotosImage`
    """

    height: typing.Optional[int] = Field(
        default=None,
    )
    """Height of the photo in px.."""

    type: typing.Optional["PhotosImageType"] = Field(
        default=None,
    )
    """Property `PhotosImage.type`."""

    url: typing.Optional[str] = Field(
        default=None,
    )
    """Photo URL.."""

    width: typing.Optional[int] = Field(
        default=None,
    )
    """Width of the photo in px.."""


class PhotosImageType(str, enum.Enum, metaclass=BaseEnumMeta):
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


class PhotosPhotoVerticalAlign(str, enum.Enum, metaclass=BaseEnumMeta):
    TOP = "top"
    MIDDLE = "middle"
    BOTTOM = "bottom"


class PhotosPhoto(BaseModel):
    """
    Model: `PhotosPhoto`
    """

    album_id: int = Field()
    """Album ID."""

    date: int = Field()
    """Date when uploaded."""

    id: int = Field()
    """Photo ID."""

    owner_id: int = Field()
    """Photo owner\'s ID."""

    has_tags: bool = Field()
    """Whether photo has attached tag links."""

    access_key: typing.Optional[str] = Field(
        default=None,
    )
    """Access key for the photo."""

    height: typing.Optional[int] = Field(
        default=None,
    )
    """Original photo height."""

    images: typing.Optional[typing.List["PhotosImage"]] = Field(
        default=None,
    )
    """Property `PhotosPhoto.images`."""

    lat: typing.Optional[float] = Field(
        default=None,
    )
    """Latitude."""

    long: typing.Optional[float] = Field(
        default=None,
    )
    """Longitude."""

    photo_256: typing.Optional[str] = Field(
        default=None,
    )
    """URL of image with 2560 px width."""

    thumb_hash: typing.Optional[str] = Field(
        default=None,
    )
    """Thumb Hash."""

    can_comment: typing.Optional[bool] = Field(
        default=None,
    )
    """Information whether current user can comment the photo."""

    place: typing.Optional[str] = Field(
        default=None,
    )
    """Property `PhotosPhoto.place`."""

    post_id: typing.Optional[int] = Field(
        default=None,
    )
    """Post ID."""

    sizes: typing.Optional[typing.List["PhotosPhotoSizes"]] = Field(
        default=None,
    )
    """Property `PhotosPhoto.sizes`."""

    square_crop: typing.Optional[str] = Field(
        default=None,
    )
    """Property `PhotosPhoto.square_crop`."""

    text: typing.Optional[str] = Field(
        default=None,
    )
    """Photo caption."""

    user_id: typing.Optional[int] = Field(
        default=None,
    )
    """ID of the user who have uploaded the photo."""

    width: typing.Optional[int] = Field(
        default=None,
    )
    """Original photo width."""

    likes: typing.Optional["BaseLikes"] = Field(
        default=None,
    )
    """Property `PhotosPhoto.likes`."""

    comments: typing.Optional["BaseObjectCount"] = Field(
        default=None,
    )
    """Property `PhotosPhoto.comments`."""

    reposts: typing.Optional["BaseRepostsInfo"] = Field(
        default=None,
    )
    """Property `PhotosPhoto.reposts`."""

    tags: typing.Optional["BaseObjectCount"] = Field(
        default=None,
    )
    """Property `PhotosPhoto.tags`."""

    hidden: typing.Optional["BasePropertyExists"] = Field(
        default=None,
    )
    """Returns if the photo is hidden above the wall."""

    real_offset: typing.Optional[int] = Field(
        default=None,
    )
    """Real position of the photo."""

    vertical_align: typing.Optional["PhotosPhotoVerticalAlign"] = Field(
        default=None,
    )
    """Sets vertical alignment of a photo."""


class PhotosPhotoAlbum(BaseModel):
    """
    Model: `PhotosPhotoAlbum`
    """

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

    description: typing.Optional[str] = Field(
        default=None,
    )
    """Photo album description."""

    thumb: typing.Optional["PhotosPhoto"] = Field(
        default=None,
    )
    """Property `PhotosPhotoAlbum.thumb`."""


class PhotosPhotoAlbumFull(BaseModel):
    """
    Model: `PhotosPhotoAlbumFull`
    """

    id: int = Field()
    """Photo album ID."""

    owner_id: int = Field()
    """Album owner\'s ID."""

    size: int = Field()
    """Photos number."""

    title: str = Field()
    """Photo album title."""

    can_upload: typing.Optional[bool] = Field(
        default=None,
    )
    """Information whether current user can upload photo to the album."""

    comments_disabled: typing.Optional[bool] = Field(
        default=None,
    )
    """Information whether album comments are disabled."""

    created: typing.Optional[int] = Field(
        default=None,
    )
    """Date when the album has been created in Unixtime, not set for system albums."""

    description: typing.Optional[str] = Field(
        default=None,
    )
    """Photo album description."""

    can_delete: typing.Optional[bool] = Field(
        default=None,
    )
    """album can delete."""

    can_include_to_feed: typing.Optional[bool] = Field(
        default=None,
    )
    """album can be selected to feed."""

    is_locked: typing.Optional[bool] = Field(
        default=None,
    )
    """Need show privacy lock at album."""

    sizes: typing.Optional[typing.List["PhotosPhotoSizes"]] = Field(
        default=None,
    )
    """Property `PhotosPhotoAlbumFull.sizes`."""

    thumb_id: typing.Optional[int] = Field(
        default=None,
    )
    """Thumb photo ID."""

    thumb_is_last: typing.Optional[bool] = Field(
        default=None,
    )
    """Information whether the album thumb is last photo."""

    thumb_src: typing.Optional[str] = Field(
        default=None,
    )
    """URL of the thumb image."""

    updated: typing.Optional[int] = Field(
        default=None,
    )
    """Date when the album has been updated last time in Unixtime, not set for system albums."""

    upload_by_admins_only: typing.Optional[bool] = Field(
        default=None,
    )
    """Information whether only community administrators can upload photos."""


class PhotosPhotoSizes(BaseModel):
    """
    Model: `PhotosPhotoSizes`
    """

    height: int = Field()
    """Height in px."""

    type: "PhotosPhotoSizesType" = Field()
    """Property `PhotosPhotoSizes.type`."""

    width: int = Field()
    """Width in px."""

    url: typing.Optional[str] = Field(
        default=None,
    )
    """URL of the image."""

    src: typing.Optional[str] = Field(
        default=None,
    )
    """URL of the image."""


class PhotosPhotoSizesType(str, enum.Enum, metaclass=BaseEnumMeta):
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
    """
    Model: `PhotosPhotoTag`
    """

    date: int = Field()
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

    description: typing.Optional[str] = Field(
        default=None,
    )
    """Tagged description.."""


class PhotosPhotoUpload(BaseModel):
    """
    Model: `PhotosPhotoUpload`
    """

    album_id: int = Field()
    """Album ID."""

    upload_url: str = Field()
    """URL to upload photo."""

    user_id: int = Field()
    """User ID."""

    fallback_upload_url: typing.Optional[str] = Field(
        default=None,
    )
    """Fallback URL if upload_url returned error."""

    group_id: typing.Optional[int] = Field(
        default=None,
    )
    """Group ID."""


class PhotosPhotoXtrTagInfo(BaseModel):
    """
    Model: `PhotosPhotoXtrTagInfo`
    """

    album_id: int = Field()
    """Album ID."""

    date: int = Field()
    """Date when uploaded."""

    id: int = Field()
    """Photo ID."""

    owner_id: int = Field()
    """Photo owner\'s ID."""

    access_key: typing.Optional[str] = Field(
        default=None,
    )
    """Access key for the photo."""

    height: typing.Optional[int] = Field(
        default=None,
    )
    """Original photo height."""

    lat: typing.Optional[float] = Field(
        default=None,
    )
    """Latitude."""

    long: typing.Optional[float] = Field(
        default=None,
    )
    """Longitude."""

    photo_1280: typing.Optional[str] = Field(
        default=None,
    )
    """URL of image with 1280 px width."""

    photo_130: typing.Optional[str] = Field(
        default=None,
    )
    """URL of image with 130 px width."""

    photo_2560: typing.Optional[str] = Field(
        default=None,
    )
    """URL of image with 2560 px width."""

    photo_604: typing.Optional[str] = Field(
        default=None,
    )
    """URL of image with 604 px width."""

    photo_75: typing.Optional[str] = Field(
        default=None,
    )
    """URL of image with 75 px width."""

    photo_807: typing.Optional[str] = Field(
        default=None,
    )
    """URL of image with 807 px width."""

    placer_id: typing.Optional[int] = Field(
        default=None,
    )
    """ID of the tag creator."""

    post_id: typing.Optional[int] = Field(
        default=None,
    )
    """Post ID."""

    sizes: typing.Optional[typing.List["PhotosPhotoSizes"]] = Field(
        default=None,
    )
    """Property `PhotosPhotoXtrTagInfo.sizes`."""

    tag_created: typing.Optional[int] = Field(
        default=None,
    )
    """Date when tag has been added in Unixtime."""

    tag_id: typing.Optional[int] = Field(
        default=None,
    )
    """Tag ID."""

    text: typing.Optional[str] = Field(
        default=None,
    )
    """Photo caption."""

    user_id: typing.Optional[int] = Field(
        default=None,
    )
    """ID of the user who have uploaded the photo."""

    width: typing.Optional[int] = Field(
        default=None,
    )
    """Original photo width."""

    has_tags: typing.Optional[bool] = Field(
        default=None,
    )
    """Whether photo has attached tag links."""


class PhotosTagsSuggestionItem(BaseModel):
    """
    Model: `PhotosTagsSuggestionItem`
    """

    title: typing.Optional[str] = Field(
        default=None,
    )
    """Property `PhotosTagsSuggestionItem.title`."""

    caption: typing.Optional[str] = Field(
        default=None,
    )
    """Property `PhotosTagsSuggestionItem.caption`."""

    type: typing.Optional[str] = Field(
        default=None,
    )
    """Property `PhotosTagsSuggestionItem.type`."""

    buttons: typing.Optional[typing.List["PhotosTagsSuggestionItemButton"]] = Field(
        default=None,
    )
    """Property `PhotosTagsSuggestionItem.buttons`."""

    photo: typing.Optional["PhotosPhoto"] = Field(
        default=None,
    )
    """Property `PhotosTagsSuggestionItem.photo`."""

    tags: typing.Optional[typing.List["PhotosPhotoTag"]] = Field(
        default=None,
    )
    """Property `PhotosTagsSuggestionItem.tags`."""

    track_code: typing.Optional[str] = Field(
        default=None,
    )
    """Property `PhotosTagsSuggestionItem.track_code`."""


class PhotosTagsSuggestionItemButtonAction(str, enum.Enum, metaclass=BaseEnumMeta):
    CONFIRM = "confirm"
    DECLINE = "decline"
    SHOW_TAGS = "show_tags"


class PhotosTagsSuggestionItemButtonStyle(str, enum.Enum, metaclass=BaseEnumMeta):
    PRIMARY = "primary"
    SECONDARY = "secondary"


class PhotosTagsSuggestionItemButton(BaseModel):
    """
    Model: `PhotosTagsSuggestionItemButton`
    """

    title: typing.Optional[str] = Field(
        default=None,
    )
    """Property `PhotosTagsSuggestionItemButton.title`."""

    action: typing.Optional["PhotosTagsSuggestionItemButtonAction"] = Field(
        default=None,
    )
    """Property `PhotosTagsSuggestionItemButton.action`."""

    style: typing.Optional["PhotosTagsSuggestionItemButtonStyle"] = Field(
        default=None,
    )
    """Property `PhotosTagsSuggestionItemButton.style`."""


class PodcastCover(BaseModel):
    """
    Model: `PodcastCover`
    """

    sizes: typing.Optional[typing.List["PhotosPhotoSizes"]] = Field(
        default=None,
    )
    """Property `PodcastCover.sizes`."""


class PodcastExternalData(BaseModel):
    """
    Model: `PodcastExternalData`
    """

    url: typing.Optional[str] = Field(
        default=None,
    )
    """Url of the podcast page."""

    owner_url: typing.Optional[str] = Field(
        default=None,
    )
    """Url of the podcasts owner community."""

    title: typing.Optional[str] = Field(
        default=None,
    )
    """Podcast title."""

    owner_name: typing.Optional[str] = Field(
        default=None,
    )
    """Name of the podcasts owner community."""

    cover: typing.Optional["PodcastCover"] = Field(
        default=None,
    )
    """Podcast cover."""


class PollsAnswer(BaseModel):
    """
    Model: `PollsAnswer`
    """

    id: int = Field()
    """Answer ID."""

    rate: float = Field()
    """Answer rate in percents."""

    text: str = Field()
    """Answer text."""

    votes: int = Field()
    """Votes number."""


class PollsBackgroundType(str, enum.Enum, metaclass=BaseEnumMeta):
    GRADIENT = "gradient"
    TILE = "tile"
    COLOR = "color"


class PollsBackground(BaseModel):
    """
    Model: `PollsBackground`
    """

    angle: typing.Optional[int] = Field(
        default=None,
    )
    """Gradient angle with 0 on positive X axis."""

    color: typing.Optional[str] = Field(
        default=None,
    )
    """Hex color code without #."""

    height: typing.Optional[int] = Field(
        default=None,
    )
    """Original height of pattern tile."""

    id: typing.Optional[int] = Field(
        default=None,
    )
    """Property `PollsBackground.id`."""

    name: typing.Optional[str] = Field(
        default=None,
    )
    """Property `PollsBackground.name`."""

    images: typing.Optional[typing.List["BaseImage"]] = Field(
        default=None,
    )
    """Pattern tiles."""

    points: typing.Optional[typing.List["BaseGradientPoint"]] = Field(
        default=None,
    )
    """Gradient points."""

    type: typing.Optional["PollsBackgroundType"] = Field(
        default=None,
    )
    """Property `PollsBackground.type`."""

    width: typing.Optional[int] = Field(
        default=None,
    )
    """Original with of pattern tile."""


class PollsFieldsVoters(BaseModel):
    """
    Model: `PollsFieldsVoters`
    """

    answer_id: typing.Optional[int] = Field(
        default=None,
    )
    """Answer ID."""

    users: typing.Optional["PollsVotersFieldsUsers"] = Field(
        default=None,
    )
    """Property `PollsFieldsVoters.users`."""

    answer_offset: typing.Optional[str] = Field(
        default=None,
    )
    """Answer offset."""


class PollsFriend(BaseModel):
    """
    Model: `PollsFriend`
    """

    id: int = Field()
    """Property `PollsFriend.id`."""


class PollsPoll(BaseModel):
    """
    Model: `PollsPoll`
    """

    multiple: bool = Field()
    """Information whether the poll with multiple choices."""

    end_date: int = Field()
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

    answers: typing.List["PollsAnswer"] = Field()
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

    anonymous: typing.Optional["PollsPollAnonymous"] = Field(
        default=None,
    )
    """Property `PollsPoll.anonymous`."""

    friends: typing.Optional[typing.List["PollsFriend"]] = Field(
        default=None,
    )
    """Property `PollsPoll.friends`."""

    answer_id: typing.Optional[int] = Field(
        default=None,
    )
    """Current user\'s answer ID."""

    answer_ids: typing.Optional[typing.List[int]] = Field(
        default=None,
    )
    """Current user\'s answer IDs."""

    embed_hash: typing.Optional[str] = Field(
        default=None,
    )
    """Property `PollsPoll.embed_hash`."""

    photo: typing.Optional["PollsBackground"] = Field(
        default=None,
    )
    """Property `PollsPoll.photo`."""

    author_id: typing.Optional[int] = Field(
        default=None,
    )
    """Poll author\'s ID."""

    background: typing.Optional["PollsBackground"] = Field(
        default=None,
    )
    """Property `PollsPoll.background`."""


PollsPollAnonymous: typing.TypeAlias = bool


class PollsVoters(BaseModel):
    """
    Model: `PollsVoters`
    """

    answer_id: typing.Optional[int] = Field(
        default=None,
    )
    """Answer ID."""

    users: typing.Optional["PollsVotersUsers"] = Field(
        default=None,
    )
    """Property `PollsVoters.users`."""

    answer_offset: typing.Optional[str] = Field(
        default=None,
    )
    """Answer offset."""


class PollsVotersFieldsUsers(BaseModel):
    """
    Model: `PollsVotersFieldsUsers`
    """

    count: typing.Optional[int] = Field(
        default=None,
    )
    """Votes number."""

    items: typing.Optional[typing.List["UsersUserFull"]] = Field(
        default=None,
    )
    """Property `PollsVotersFieldsUsers.items`."""


class PollsVotersUsers(BaseModel):
    """
    Model: `PollsVotersUsers`
    """

    count: typing.Optional[int] = Field(
        default=None,
    )
    """Votes number."""

    items: typing.Optional[typing.List[int]] = Field(
        default=None,
    )
    """Property `PollsVotersUsers.items`."""


class PrettyCardsButtonOneOf(BaseModel):
    """
    Model: `PrettyCardsButtonOneOf`
    """


class PrettyCardsPrettyCardInnerType(str, enum.Enum, metaclass=BaseEnumMeta):
    PRETTYCARDS_PRETTYCARD = "prettyCards_prettyCard"


class PrettyCardsPrettyCard(BaseModel):
    """
    Model: `PrettyCardsPrettyCard`
    """

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

    button: typing.Optional["PrettyCardsButtonOneOf"] = Field(
        default=None,
    )
    """Button key."""

    button_text: typing.Optional[str] = Field(
        default=None,
    )
    """Button text in current language."""

    images: typing.Optional[typing.List["BaseImage"]] = Field(
        default=None,
    )
    """Property `PrettyCardsPrettyCard.images`."""

    price: typing.Optional[str] = Field(
        default=None,
    )
    """Price if set (decimal number returned as string)."""

    price_old: typing.Optional[str] = Field(
        default=None,
    )
    """Old price if set (decimal number returned as string)."""


class PrettyCardsPrettyCardOrError(BaseModel):
    """
    Model: `PrettyCardsPrettyCardOrError`
    """


class SearchHint(BaseModel):
    """
    Model: `SearchHint`
    """

    description: str = Field()
    """Object description."""

    type: "SearchHintType" = Field()
    """Property `SearchHint.type`."""

    app: typing.Optional["AppsApp"] = Field(
        default=None,
    )
    """Property `SearchHint.app`."""

    global_: typing.Optional[bool] = Field(
        default=None,
        alias="global",
    )
    """Information whether the object has been found globally."""

    group: typing.Optional["GroupsGroup"] = Field(
        default=None,
    )
    """Property `SearchHint.group`."""

    profile: typing.Optional["UsersUserMin"] = Field(
        default=None,
    )
    """Property `SearchHint.profile`."""

    section: typing.Optional["SearchHintSection"] = Field(
        default=None,
    )
    """Property `SearchHint.section`."""

    link: typing.Optional["BaseLink"] = Field(
        default=None,
    )
    """Property `SearchHint.link`."""


class SearchHintSection(str, enum.Enum, metaclass=BaseEnumMeta):
    GROUPS = "groups"
    EVENTS = "events"
    PUBLICS = "publics"
    CORRESPONDENTS = "correspondents"
    PEOPLE = "people"
    FRIENDS = "friends"
    MUTUAL_FRIENDS = "mutual_friends"
    PROMO = "promo"


class SearchHintType(str, enum.Enum, metaclass=BaseEnumMeta):
    GROUP = "group"
    PROFILE = "profile"
    VK_APP = "vk_app"
    APP = "app"
    HTML5_GAME = "html5_game"
    LINK = "link"


class SecureGiveEventStickerItem(BaseModel):
    """
    Model: `SecureGiveEventStickerItem`
    """

    user_id: typing.Optional[int] = Field(
        default=None,
    )
    """Property `SecureGiveEventStickerItem.user_id`."""

    status: typing.Optional[str] = Field(
        default=None,
    )
    """Property `SecureGiveEventStickerItem.status`."""


class SecureLevel(BaseModel):
    """
    Model: `SecureLevel`
    """

    level: typing.Optional[int] = Field(
        default=None,
    )
    """Level."""

    uid: typing.Optional[int] = Field(
        default=None,
    )
    """User ID."""


class SecureSetCounterItem(BaseModel):
    """
    Model: `SecureSetCounterItem`
    """

    id: int = Field()
    """User ID."""

    result: bool = Field()
    """Property `SecureSetCounterItem.result`."""


class SecureSmsNotification(BaseModel):
    """
    Model: `SecureSmsNotification`
    """

    app_id: typing.Optional[str] = Field(
        default=None,
    )
    """Application ID."""

    date: typing.Optional[str] = Field(
        default=None,
    )
    """Date when message has been sent in Unixtime."""

    id: typing.Optional[str] = Field(
        default=None,
    )
    """Notification ID."""

    message: typing.Optional[str] = Field(
        default=None,
    )
    """Messsage text."""

    user_id: typing.Optional[str] = Field(
        default=None,
    )
    """User ID."""


class SecureTokenChecked(BaseModel):
    """
    Model: `SecureTokenChecked`
    """

    date: typing.Optional[int] = Field(
        default=None,
    )
    """Date when access_token has been generated in Unixtime."""

    expire: typing.Optional[int] = Field(
        default=None,
    )
    """Date when access_token will expire in Unixtime."""

    success: typing.Optional[int] = Field(
        default=None,
    )
    """Returns if successfully processed."""

    user_id: typing.Optional[int] = Field(
        default=None,
    )
    """User ID."""


class SecureTransaction(BaseModel):
    """
    Model: `SecureTransaction`
    """

    date: typing.Optional[int] = Field(
        default=None,
    )
    """Transaction date in Unixtime."""

    id: typing.Optional[int] = Field(
        default=None,
    )
    """Transaction ID."""

    uid_from: typing.Optional[int] = Field(
        default=None,
    )
    """From ID."""

    uid_to: typing.Optional[int] = Field(
        default=None,
    )
    """To ID."""

    votes: typing.Optional[int] = Field(
        default=None,
    )
    """Votes number."""


class StatsActivity(BaseModel):
    """
    Activity stats
    Model: `StatsActivity`
    """

    comments: typing.Optional[int] = Field(
        default=None,
    )
    """Comments number."""

    copies: typing.Optional[int] = Field(
        default=None,
    )
    """Reposts number."""

    hidden: typing.Optional[int] = Field(
        default=None,
    )
    """Hidden from news count."""

    likes: typing.Optional[int] = Field(
        default=None,
    )
    """Likes number."""

    subscribed: typing.Optional[int] = Field(
        default=None,
    )
    """New subscribers count."""

    unsubscribed: typing.Optional[int] = Field(
        default=None,
    )
    """Unsubscribed count."""


class StatsCity(BaseModel):
    """
    Model: `StatsCity`
    """

    count: typing.Optional[int] = Field(
        default=None,
    )
    """Visitors number."""

    name: typing.Optional[str] = Field(
        default=None,
    )
    """City name."""

    value: typing.Optional[int] = Field(
        default=None,
    )
    """City ID."""


class StatsCountry(BaseModel):
    """
    Model: `StatsCountry`
    """

    code: typing.Optional[str] = Field(
        default=None,
    )
    """Country code."""

    count: typing.Optional[int] = Field(
        default=None,
    )
    """Visitors number."""

    name: typing.Optional[str] = Field(
        default=None,
    )
    """Country name."""

    value: typing.Optional[int] = Field(
        default=None,
    )
    """Country ID."""


class StatsPeriod(BaseModel):
    """
    Model: `StatsPeriod`
    """

    activity: typing.Optional["StatsActivity"] = Field(
        default=None,
    )
    """Property `StatsPeriod.activity`."""

    period_from: typing.Optional["StatsPeriodFromOneOf"] = Field(
        default=None,
    )
    """Property `StatsPeriod.period_from`."""

    period_to: typing.Optional["StatsPeriodToOneOf"] = Field(
        default=None,
    )
    """Property `StatsPeriod.period_to`."""

    reach: typing.Optional["StatsReach"] = Field(
        default=None,
    )
    """Property `StatsPeriod.reach`."""

    visitors: typing.Optional["StatsViews"] = Field(
        default=None,
    )
    """Property `StatsPeriod.visitors`."""


StatsPeriodFromOneOf: typing.TypeAlias = datetime.datetime


StatsPeriodToOneOf: typing.TypeAlias = datetime.datetime


class StatsReach(BaseModel):
    """
    Reach stats
    Model: `StatsReach`
    """

    age: typing.Optional[typing.List["StatsSexAge"]] = Field(
        default=None,
    )
    """Property `StatsReach.age`."""

    cities: typing.Optional[typing.List["StatsCity"]] = Field(
        default=None,
    )
    """Property `StatsReach.cities`."""

    countries: typing.Optional[typing.List["StatsCountry"]] = Field(
        default=None,
    )
    """Property `StatsReach.countries`."""

    mobile_reach: typing.Optional[int] = Field(
        default=None,
    )
    """Reach count from mobile devices."""

    reach: typing.Optional[int] = Field(
        default=None,
    )
    """Reach count."""

    reach_subscribers: typing.Optional[int] = Field(
        default=None,
    )
    """Subscribers reach count."""

    sex: typing.Optional[typing.List["StatsSexAge"]] = Field(
        default=None,
    )
    """Property `StatsReach.sex`."""

    sex_age: typing.Optional[typing.List["StatsSexAge"]] = Field(
        default=None,
    )
    """Property `StatsReach.sex_age`."""


class StatsSexAge(BaseModel):
    """
    Model: `StatsSexAge`
    """

    value: str = Field()
    """Sex/age value."""

    count: typing.Optional[int] = Field(
        default=None,
    )
    """Visitors number."""

    reach: typing.Optional[int] = Field(
        default=None,
    )
    """Property `StatsSexAge.reach`."""

    reach_subscribers: typing.Optional[int] = Field(
        default=None,
    )
    """Property `StatsSexAge.reach_subscribers`."""

    count_subscribers: typing.Optional[int] = Field(
        default=None,
    )
    """Property `StatsSexAge.count_subscribers`."""


class StatsViews(BaseModel):
    """
    Views stats
    Model: `StatsViews`
    """

    age: typing.Optional[typing.List["StatsSexAge"]] = Field(
        default=None,
    )
    """Property `StatsViews.age`."""

    cities: typing.Optional[typing.List["StatsCity"]] = Field(
        default=None,
    )
    """Property `StatsViews.cities`."""

    countries: typing.Optional[typing.List["StatsCountry"]] = Field(
        default=None,
    )
    """Property `StatsViews.countries`."""

    mobile_views: typing.Optional[int] = Field(
        default=None,
    )
    """Number of views from mobile devices."""

    sex: typing.Optional[typing.List["StatsSexAge"]] = Field(
        default=None,
    )
    """Property `StatsViews.sex`."""

    sex_age: typing.Optional[typing.List["StatsSexAge"]] = Field(
        default=None,
    )
    """Property `StatsViews.sex_age`."""

    views: typing.Optional[int] = Field(
        default=None,
    )
    """Views number."""

    visitors: typing.Optional[int] = Field(
        default=None,
    )
    """Visitors number."""


class StatsWallpostStat(BaseModel):
    """
    Model: `StatsWallpostStat`
    """

    post_id: typing.Optional[int] = Field(
        default=None,
    )
    """Property `StatsWallpostStat.post_id`."""

    hide: typing.Optional[int] = Field(
        default=None,
    )
    """Hidings number."""

    join_group: typing.Optional[int] = Field(
        default=None,
    )
    """People have joined the group."""

    links: typing.Optional[int] = Field(
        default=None,
    )
    """Link clickthrough."""

    reach_subscribers: typing.Optional[int] = Field(
        default=None,
    )
    """Subscribers reach."""

    reach_subscribers_count: typing.Optional[int] = Field(
        default=None,
    )
    """Property `StatsWallpostStat.reach_subscribers_count`."""

    reach_total: typing.Optional[int] = Field(
        default=None,
    )
    """Total reach."""

    reach_total_count: typing.Optional[int] = Field(
        default=None,
    )
    """Property `StatsWallpostStat.reach_total_count`."""

    reach_viral: typing.Optional[int] = Field(
        default=None,
    )
    """Property `StatsWallpostStat.reach_viral`."""

    reach_ads: typing.Optional[int] = Field(
        default=None,
    )
    """Property `StatsWallpostStat.reach_ads`."""

    report: typing.Optional[int] = Field(
        default=None,
    )
    """Reports number."""

    to_group: typing.Optional[int] = Field(
        default=None,
    )
    """Clickthrough to community."""

    unsubscribe: typing.Optional[int] = Field(
        default=None,
    )
    """Unsubscribed members."""

    sex_age: typing.Optional[typing.List["StatsSexAge"]] = Field(
        default=None,
    )
    """Property `StatsWallpostStat.sex_age`."""


class StatusStatus(BaseModel):
    """
    Model: `StatusStatus`
    """

    text: str = Field()
    """Status text."""

    audio: typing.Optional["AudioAudio"] = Field(
        default=None,
    )
    """Property `StatusStatus.audio`."""


class StickersImageSet(BaseModel):
    """
    Model: `StickersImageSet`
    """

    base_url: str = Field()
    """Base URL for images in set."""

    version: typing.Optional[int] = Field(
        default=None,
    )
    """Version number to be appended to the image URL."""

    images: typing.Optional[typing.List["BaseImage"]] = Field(
        default=None,
    )
    """Property `StickersImageSet.images`."""


class StorageValue(BaseModel):
    """
    Model: `StorageValue`
    """

    key: str = Field()
    """Property `StorageValue.key`."""

    value: str = Field()
    """Property `StorageValue.value`."""


class StoreProductType(str, enum.Enum, metaclass=BaseEnumMeta):
    STICKERS = "stickers"


class StoreProduct(BaseModel):
    """
    Model: `StoreProduct`
    """

    id: int = Field()
    """Id of the product."""

    type: "StoreProductType" = Field()
    """Product type."""

    is_new: typing.Optional[bool] = Field(
        default=None,
    )
    """Information whether sticker product wasn\'t used after being purchased."""

    copyright: typing.Optional[str] = Field(
        default=None,
    )
    """Product copyright information."""

    base_id: typing.Optional[int] = Field(
        default=None,
    )
    """Id of the base pack (for sticker pack styles)."""

    style_ids: typing.Optional[typing.List[int]] = Field(
        default=None,
    )
    """Array of style ids available for the sticker pack."""

    purchased: typing.Optional[bool] = Field(
        default=None,
    )
    """Information whether the product is purchased (1 - yes, 0 - no)."""

    active: typing.Optional[bool] = Field(
        default=None,
    )
    """Information whether the product is active (1 - yes, 0 - no)."""

    promoted: typing.Optional[bool] = Field(
        default=None,
    )
    """Information whether the product is promoted (1 - yes, 0 - no)."""

    purchase_date: typing.Optional[int] = Field(
        default=None,
    )
    """Date (Unix time) when the product was purchased."""

    title: typing.Optional[str] = Field(
        default=None,
    )
    """Title of the product."""

    stickers: typing.Optional[typing.List["BaseStickerNew"]] = Field(
        default=None,
    )
    """Property `StoreProduct.stickers`."""

    style_sticker_ids: typing.Optional[typing.List[int]] = Field(
        default=None,
    )
    """Array of style sticker ids (for sticker pack styles)."""

    icon: typing.Optional["StoreProductIcon"] = Field(
        default=None,
    )
    """Array of icon images or icon set object of the product (for stickers product type)."""

    previews: typing.Optional[typing.List["BaseImage"]] = Field(
        default=None,
    )
    """Array of preview images of the product (for stickers product type)."""

    has_animation: typing.Optional[bool] = Field(
        default=None,
    )
    """Information whether the product is an animated sticker pack (for stickers product type)."""

    subtitle: typing.Optional[str] = Field(
        default=None,
    )
    """Subtitle of the product."""

    payment_region: typing.Optional[str] = Field(
        default=None,
    )
    """Property `StoreProduct.payment_region`."""

    is_vmoji: typing.Optional[bool] = Field(
        default=None,
    )
    """Information whether sticker pack is a vmoji pack."""

    title_lang_key: typing.Optional[str] = Field(
        default=None,
    )
    """Property `StoreProduct.title_lang_key`."""

    description_lang_key: typing.Optional[str] = Field(
        default=None,
    )
    """Property `StoreProduct.description_lang_key`."""

    url: typing.Optional[str] = Field(
        default=None,
    )
    """Property `StoreProduct.url`."""

    is_popup: typing.Optional[bool] = Field(
        default=None,
    )
    """Information whether the product is a sticker pack with popup stickers (for stickers product type)."""


class StoreProductIcon(BaseModel):
    """
    Model: `StoreProductIcon`
    """

    base_url: str = Field()
    """Base URL for images in set."""

    version: typing.Optional[int] = Field(
        default=None,
    )
    """Version number to be appended to the image URL."""

    images: typing.Optional[typing.List["BaseImage"]] = Field(
        default=None,
    )
    """Property `StoreProductIcon.images`."""


class StoreStickersKeyword(BaseModel):
    """
    Model: `StoreStickersKeyword`
    """

    words: typing.List[str] = Field()
    """Property `StoreStickersKeyword.words`."""

    user_stickers: typing.Optional[typing.List["BaseStickerNew"]] = Field(
        default=None,
    )
    """Property `StoreStickersKeyword.user_stickers`."""

    promoted_stickers: typing.Optional[typing.List["BaseStickerNew"]] = Field(
        default=None,
    )
    """Property `StoreStickersKeyword.promoted_stickers`."""

    stickers: typing.Optional[typing.List["StoreStickersKeywordSticker"]] = Field(
        default=None,
    )
    """Property `StoreStickersKeyword.stickers`."""


class StoreStickersKeywordSticker(BaseModel):
    """
    Model: `StoreStickersKeywordSticker`
    """

    pack_id: int = Field()
    """Pack id."""

    sticker_id: int = Field()
    """Sticker id."""


class StoriesClickableArea(BaseModel):
    """
    Model: `StoriesClickableArea`
    """

    x: int = Field()
    """Property `StoriesClickableArea.x`."""

    y: int = Field()
    """Property `StoriesClickableArea.y`."""


class StoriesClickableStickerType(str, enum.Enum, metaclass=BaseEnumMeta):
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


class StoriesClickableStickerStyle(str, enum.Enum, metaclass=BaseEnumMeta):
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


class StoriesClickableStickerSubtype(str, enum.Enum, metaclass=BaseEnumMeta):
    MARKET_ITEM = "market_item"
    ALIEXPRESS_PRODUCT = "aliexpress_product"


class StoriesClickableSticker(BaseModel):
    """
    Model: `StoriesClickableSticker`
    """

    clickable_area: typing.List["StoriesClickableArea"] = Field()
    """Property `StoriesClickableSticker.clickable_area`."""

    id: int = Field()
    """Clickable sticker ID."""

    type: "StoriesClickableStickerType" = Field()
    """Property `StoriesClickableSticker.type`."""

    hashtag: typing.Optional[str] = Field(
        default=None,
    )
    """Property `StoriesClickableSticker.hashtag`."""

    link_object: typing.Optional["BaseLink"] = Field(
        default=None,
    )
    """Property `StoriesClickableSticker.link_object`."""

    mention: typing.Optional[str] = Field(
        default=None,
    )
    """Property `StoriesClickableSticker.mention`."""

    tooltip_text: typing.Optional[str] = Field(
        default=None,
    )
    """Property `StoriesClickableSticker.tooltip_text`."""

    owner_id: typing.Optional[int] = Field(
        default=None,
    )
    """Property `StoriesClickableSticker.owner_id`."""

    story_id: typing.Optional[int] = Field(
        default=None,
    )
    """Property `StoriesClickableSticker.story_id`."""

    clip_id: typing.Optional[int] = Field(
        default=None,
    )
    """Property `StoriesClickableSticker.clip_id`."""

    video_id: typing.Optional[int] = Field(
        default=None,
    )
    """Property `StoriesClickableSticker.video_id`."""

    question: typing.Optional[str] = Field(
        default=None,
    )
    """Property `StoriesClickableSticker.question`."""

    question_button: typing.Optional[str] = Field(
        default=None,
    )
    """Property `StoriesClickableSticker.question_button`."""

    place_id: typing.Optional[int] = Field(
        default=None,
    )
    """Property `StoriesClickableSticker.place_id`."""

    market_item: typing.Optional["MarketMarketItem"] = Field(
        default=None,
    )
    """Property `StoriesClickableSticker.market_item`."""

    audio: typing.Optional["AudioAudio"] = Field(
        default=None,
    )
    """Property `StoriesClickableSticker.audio`."""

    audio_start_time: typing.Optional[int] = Field(
        default=None,
    )
    """Property `StoriesClickableSticker.audio_start_time`."""

    style: typing.Optional["StoriesClickableStickerStyle"] = Field(
        default=None,
    )
    """Property `StoriesClickableSticker.style`."""

    subtype: typing.Optional["StoriesClickableStickerSubtype"] = Field(
        default=None,
    )
    """Property `StoriesClickableSticker.subtype`."""

    post_owner_id: typing.Optional[int] = Field(
        default=None,
    )
    """Property `StoriesClickableSticker.post_owner_id`."""

    post_id: typing.Optional[int] = Field(
        default=None,
    )
    """Property `StoriesClickableSticker.post_id`."""

    poll: typing.Optional["PollsPoll"] = Field(
        default=None,
    )
    """Property `StoriesClickableSticker.poll`."""

    color: typing.Optional[str] = Field(
        default=None,
    )
    """Color, hex format."""

    sticker_id: typing.Optional[int] = Field(
        default=None,
    )
    """Sticker ID."""

    sticker_pack_id: typing.Optional[int] = Field(
        default=None,
    )
    """Sticker pack ID."""

    app: typing.Optional["AppsAppMin"] = Field(
        default=None,
    )
    """Property `StoriesClickableSticker.app`."""

    app_context: typing.Optional[str] = Field(
        default=None,
    )
    """Additional context for app sticker."""

    has_new_interactions: typing.Optional[bool] = Field(
        default=None,
    )
    """Whether current user has unread interaction with this app."""

    is_broadcast_notify_allowed: typing.Optional[bool] = Field(
        default=None,
    )
    """Whether current user allowed broadcast notify from this app."""

    situational_theme_id: typing.Optional[int] = Field(
        default=None,
    )
    """Property `StoriesClickableSticker.situational_theme_id`."""

    situational_app_url: typing.Optional[str] = Field(
        default=None,
    )
    """Property `StoriesClickableSticker.situational_app_url`."""


class StoriesClickableStickers(BaseModel):
    """
    Model: `StoriesClickableStickers`
    """

    clickable_stickers: typing.List["StoriesClickableSticker"] = Field()
    """Property `StoriesClickableStickers.clickable_stickers`."""

    original_height: int = Field()
    """Property `StoriesClickableStickers.original_height`."""

    original_width: int = Field()
    """Property `StoriesClickableStickers.original_width`."""


class StoriesFeedItemType(str, enum.Enum, metaclass=BaseEnumMeta):
    PROMO_STORIES = "promo_stories"
    STORIES = "stories"
    LIVE_ACTIVE = "live_active"
    LIVE_FINISHED = "live_finished"
    APP_GROUPED_STORIES = "app_grouped_stories"
    DISCOVER = "discover"


class StoriesFeedItem(BaseModel):
    """
    Model: `StoriesFeedItem`
    """

    type: "StoriesFeedItemType" = Field()
    """Type of Feed Item."""

    id: typing.Optional[str] = Field(
        default=None,
    )
    """Property `StoriesFeedItem.id`."""

    owner_id: typing.Optional[int] = Field(
        default=None,
    )
    """Property `StoriesFeedItem.owner_id`."""

    stories: typing.Optional[typing.List["StoriesStory"]] = Field(
        default=None,
    )
    """Author stories."""

    grouped: typing.Optional[typing.List["StoriesFeedItem"]] = Field(
        default=None,
    )
    """Grouped stories of various authors (for types community_grouped_stories/app_grouped_stories type)."""

    app: typing.Optional["AppsAppMin"] = Field(
        default=None,
    )
    """App, which stories has been grouped (for type app_grouped_stories)."""

    promo_data: typing.Optional["StoriesPromoBlock"] = Field(
        default=None,
    )
    """Additional data for promo stories (for type promo_stories)."""

    track_code: typing.Optional[str] = Field(
        default=None,
    )
    """Property `StoriesFeedItem.track_code`."""

    has_unseen: typing.Optional[bool] = Field(
        default=None,
    )
    """Property `StoriesFeedItem.has_unseen`."""

    name: typing.Optional[str] = Field(
        default=None,
    )
    """Property `StoriesFeedItem.name`."""


class StoriesPromoBlock(BaseModel):
    """
    Additional data for promo stories
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
    """
    Model: `StoriesReplies`
    """

    count: int = Field()
    """Replies number.."""

    new: typing.Optional[int] = Field(
        default=None,
    )
    """New replies number.."""


class StoriesStory(BaseModel):
    """
    Model: `StoriesStory`
    """

    id: int = Field()
    """Story ID.."""

    owner_id: int = Field()
    """Story owner\'s ID.."""

    access_key: typing.Optional[str] = Field(
        default=None,
    )
    """Access key for private object.."""

    can_comment: typing.Optional[bool] = Field(
        default=None,
    )
    """Information whether current user can comment the story (0 - no, 1 - yes).."""

    can_reply: typing.Optional[bool] = Field(
        default=None,
    )
    """Information whether current user can reply to the story (0 - no, 1 - yes).."""

    can_see: typing.Optional[bool] = Field(
        default=None,
    )
    """Information whether current user can see the story (0 - no, 1 - yes).."""

    can_like: typing.Optional[bool] = Field(
        default=None,
    )
    """Information whether current user can like the story.."""

    can_share: typing.Optional[bool] = Field(
        default=None,
    )
    """Information whether current user can share the story (0 - no, 1 - yes).."""

    can_hide: typing.Optional[bool] = Field(
        default=None,
    )
    """Information whether current user can hide the story (0 - no, 1 - yes).."""

    date: typing.Optional[int] = Field(
        default=None,
    )
    """Date when story has been added in Unixtime.."""

    expires_at: typing.Optional[int] = Field(
        default=None,
    )
    """Story expiration time. Unixtime.."""

    is_deleted: typing.Optional[bool] = Field(
        default=None,
    )
    """Information whether the story is deleted (false - no, true - yes).."""

    is_expired: typing.Optional[bool] = Field(
        default=None,
    )
    """Information whether the story is expired (false - no, true - yes).."""

    link: typing.Optional["StoriesStoryLink"] = Field(
        default=None,
    )
    """Property `StoriesStory.link`."""

    parent_story: typing.Optional["StoriesStory"] = Field(
        default=None,
    )
    """Property `StoriesStory.parent_story`."""

    parent_story_access_key: typing.Optional[str] = Field(
        default=None,
    )
    """Access key for private object.."""

    parent_story_id: typing.Optional[int] = Field(
        default=None,
    )
    """Parent story ID.."""

    parent_story_owner_id: typing.Optional[int] = Field(
        default=None,
    )
    """Parent story owner\'s ID.."""

    photo: typing.Optional["PhotosPhoto"] = Field(
        default=None,
    )
    """Property `StoriesStory.photo`."""

    blurred_preview: typing.Optional[str] = Field(
        default=None,
    )
    """url with blured preview image.."""

    replies: typing.Optional["StoriesReplies"] = Field(
        default=None,
    )
    """Replies counters to current story.."""

    seen: typing.Optional[bool] = Field(
        default=None,
    )
    """Information whether current user has seen the story or not (0 - no, 1 - yes).."""

    type: typing.Optional["StoriesStoryType"] = Field(
        default=None,
    )
    """Property `StoriesStory.type`."""

    clickable_stickers: typing.Optional["StoriesClickableStickers"] = Field(
        default=None,
    )
    """Property `StoriesStory.clickable_stickers`."""

    video: typing.Optional["VideoVideoFull"] = Field(
        default=None,
    )
    """Property `StoriesStory.video`."""

    views: typing.Optional[int] = Field(
        default=None,
    )
    """Views number.."""

    can_ask: typing.Optional[bool] = Field(
        default=None,
    )
    """Information whether story has question sticker and current user can send question to the author."""

    can_ask_anonymous: typing.Optional[bool] = Field(
        default=None,
    )
    """Information whether story has question sticker and current user can send anonymous question to the author."""

    narratives_count: typing.Optional[int] = Field(
        default=None,
    )
    """Property `StoriesStory.narratives_count`."""

    first_narrative_title: typing.Optional[str] = Field(
        default=None,
    )
    """Property `StoriesStory.first_narrative_title`."""

    first_narrative_id: typing.Optional[int] = Field(
        default=None,
    )
    """Property `StoriesStory.first_narrative_id`."""

    can_use_in_narrative: typing.Optional[bool] = Field(
        default=None,
    )
    """Property `StoriesStory.can_use_in_narrative`."""


class StoriesStoryLink(BaseModel):
    """
    Model: `StoriesStoryLink`
    """

    text: str = Field()
    """Link text."""

    url: str = Field()
    """Link URL."""

    link_url_target: typing.Optional[str] = Field(
        default=None,
    )
    """How to open url."""


class StoriesStoryStats(BaseModel):
    """
    Model: `StoriesStoryStats`
    """

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
    """
    Model: `StoriesStoryStatsStat`
    """

    state: "StoriesStoryStatsState" = Field()
    """Property `StoriesStoryStatsStat.state`."""

    count: typing.Optional[int] = Field(
        default=None,
    )
    """Stat value."""


class StoriesStoryStatsState(str, enum.Enum, metaclass=BaseEnumMeta):
    ON = "on"
    OFF = "off"
    HIDDEN = "hidden"


class StoriesStoryType(str, enum.Enum, metaclass=BaseEnumMeta):
    PHOTO = "photo"
    VIDEO = "video"
    LIVE_ACTIVE = "live_active"
    LIVE_FINISHED = "live_finished"


class StoriesUploadLinkText(str, enum.Enum, metaclass=BaseEnumMeta):
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
    """
    Model: `StoriesUploadResult`
    """

    upload_result: typing.Optional[str] = Field(
        default=None,
    )
    """Property `StoriesUploadResult.upload_result`."""


class StoriesViewersItem(BaseModel):
    """
    Model: `StoriesViewersItem`
    """

    is_liked: bool = Field()
    """user has like for this object."""

    user_id: int = Field()
    """user id."""

    user: typing.Optional["UsersUserFull"] = Field(
        default=None,
    )
    """Property `StoriesViewersItem.user`."""


class StreamingStatsEventType(str, enum.Enum, metaclass=BaseEnumMeta):
    POST = "post"
    COMMENT = "comment"
    SHARE = "share"


class StreamingStats(BaseModel):
    """
    Model: `StreamingStats`
    """

    event_type: "StreamingStatsEventType" = Field()
    """Events type."""

    stats: typing.List["StreamingStatsPoint"] = Field()
    """Statistics."""


class StreamingStatsPoint(BaseModel):
    """
    Model: `StreamingStatsPoint`
    """

    timestamp: int = Field()
    """Property `StreamingStatsPoint.timestamp`."""

    value: int = Field()
    """Property `StreamingStatsPoint.value`."""


class FriendsFriendStatus(BaseModel):
    """
    Model: `FriendsFriendStatus`
    """

    friend_status: "FriendsFriendStatusStatus" = Field()
    """Property `FriendsFriendStatus.friend_status`."""

    user_id: int = Field()
    """User ID."""

    sign: typing.Optional[str] = Field(
        default=None,
    )
    """MD5 hash for the result validation."""


class FriendsFriendStatusStatus(int, enum.Enum, metaclass=BaseEnumMeta):
    NOT_A_FRIEND = 0
    OUTCOMING_REQUEST = 1
    INCOMING_REQUEST = 2
    IS_FRIEND = 3


class FriendsFriendsList(BaseModel):
    """
    Model: `FriendsFriendsList`
    """

    id: int = Field()
    """List ID."""

    name: str = Field()
    """List title."""


class FriendsMutualFriend(BaseModel):
    """
    Model: `FriendsMutualFriend`
    """

    common_count: typing.Optional[int] = Field(
        default=None,
    )
    """Total mutual friends number."""

    common_friends: typing.Optional[typing.List[int]] = Field(
        default=None,
    )
    """Property `FriendsMutualFriend.common_friends`."""

    id: typing.Optional[int] = Field(
        default=None,
    )
    """User ID."""


class FriendsOnlineUsers(BaseModel):
    """
    Model: `FriendsOnlineUsers`
    """

    online: typing.List[int] = Field()
    """Property `FriendsOnlineUsers.online`."""

    total_count: typing.Optional[int] = Field(
        default=None,
    )
    """Total online friends number."""


class FriendsOnlineUsersWithMobile(BaseModel):
    """
    Model: `FriendsOnlineUsersWithMobile`
    """

    online: typing.List[int] = Field()
    """Property `FriendsOnlineUsersWithMobile.online`."""

    online_mobile: typing.List[int] = Field()
    """Property `FriendsOnlineUsersWithMobile.online_mobile`."""

    total_count: typing.Optional[int] = Field(
        default=None,
    )
    """Total online friends number."""


class FriendsRequestsMutual(BaseModel):
    """
    Model: `FriendsRequestsMutual`
    """

    count: typing.Optional[int] = Field(
        default=None,
    )
    """Total mutual friends number."""

    users: typing.Optional[typing.List[int]] = Field(
        default=None,
    )
    """Property `FriendsRequestsMutual.users`."""


class UtilsDomainResolved(BaseModel):
    """
    Model: `UtilsDomainResolved`
    """

    object_id: typing.Optional[int] = Field(
        default=None,
    )
    """Object ID."""

    group_id: typing.Optional[int] = Field(
        default=None,
    )
    """Group ID."""

    type: typing.Optional["UtilsDomainResolvedType"] = Field(
        default=None,
    )
    """Property `UtilsDomainResolved.type`."""


class UtilsDomainResolvedType(str, enum.Enum, metaclass=BaseEnumMeta):
    USER = "user"
    GROUP = "group"
    APPLICATION = "application"
    EVENT = "event"
    PAGE = "page"
    VK_APP = "vk_app"
    COMMUNITY_APPLICATION = "community_application"


class UtilsLastShortenedLink(BaseModel):
    """
    Model: `UtilsLastShortenedLink`
    """

    access_key: typing.Optional[str] = Field(
        default=None,
    )
    """Access key for private stats."""

    key: typing.Optional[str] = Field(
        default=None,
    )
    """Link key (characters after vk.cc/)."""

    short_url: typing.Optional[str] = Field(
        default=None,
    )
    """Short link URL."""

    timestamp: typing.Optional[int] = Field(
        default=None,
    )
    """Creation time in Unixtime."""

    url: typing.Optional[str] = Field(
        default=None,
    )
    """Full URL."""

    views: typing.Optional[int] = Field(
        default=None,
    )
    """Total views number."""


class UtilsLinkChecked(BaseModel):
    """
    Model: `UtilsLinkChecked`
    """

    link: typing.Optional[str] = Field(
        default=None,
    )
    """Link URL."""

    status: typing.Optional["UtilsLinkCheckedStatus"] = Field(
        default=None,
    )
    """Property `UtilsLinkChecked.status`."""


class UtilsLinkCheckedStatus(str, enum.Enum, metaclass=BaseEnumMeta):
    NOT_BANNED = "not_banned"
    BANNED = "banned"
    PROCESSING = "processing"


class UtilsLinkStats(BaseModel):
    """
    Model: `UtilsLinkStats`
    """

    key: typing.Optional[str] = Field(
        default=None,
    )
    """Link key (characters after vk.cc/)."""

    stats: typing.Optional[typing.List["UtilsStats"]] = Field(
        default=None,
    )
    """Property `UtilsLinkStats.stats`."""


class UtilsLinkStatsExtended(BaseModel):
    """
    Model: `UtilsLinkStatsExtended`
    """

    key: typing.Optional[str] = Field(
        default=None,
    )
    """Link key (characters after vk.cc/)."""

    stats: typing.Optional[typing.List["UtilsStatsExtended"]] = Field(
        default=None,
    )
    """Property `UtilsLinkStatsExtended.stats`."""


class UtilsShortLink(BaseModel):
    """
    Model: `UtilsShortLink`
    """

    access_key: typing.Optional[str] = Field(
        default=None,
    )
    """Access key for private stats."""

    key: typing.Optional[str] = Field(
        default=None,
    )
    """Link key (characters after vk.cc/)."""

    short_url: typing.Optional[str] = Field(
        default=None,
    )
    """Short link URL."""

    url: typing.Optional[str] = Field(
        default=None,
    )
    """Full URL."""


class UtilsStats(BaseModel):
    """
    Model: `UtilsStats`
    """

    timestamp: typing.Optional[int] = Field(
        default=None,
    )
    """Start time."""

    views: typing.Optional[int] = Field(
        default=None,
    )
    """Total views number."""


class UtilsStatsCity(BaseModel):
    """
    Model: `UtilsStatsCity`
    """

    city_id: typing.Optional[int] = Field(
        default=None,
    )
    """City ID."""

    views: typing.Optional[int] = Field(
        default=None,
    )
    """Views number."""


class UtilsStatsCountry(BaseModel):
    """
    Model: `UtilsStatsCountry`
    """

    country_id: typing.Optional[int] = Field(
        default=None,
    )
    """Country ID."""

    views: typing.Optional[int] = Field(
        default=None,
    )
    """Views number."""


class UtilsStatsExtended(BaseModel):
    """
    Model: `UtilsStatsExtended`
    """

    cities: typing.Optional[typing.List["UtilsStatsCity"]] = Field(
        default=None,
    )
    """Property `UtilsStatsExtended.cities`."""

    countries: typing.Optional[typing.List["UtilsStatsCountry"]] = Field(
        default=None,
    )
    """Property `UtilsStatsExtended.countries`."""

    sex_age: typing.Optional[typing.List["UtilsStatsSexAge"]] = Field(
        default=None,
    )
    """Property `UtilsStatsExtended.sex_age`."""

    timestamp: typing.Optional[int] = Field(
        default=None,
    )
    """Start time."""

    views: typing.Optional[int] = Field(
        default=None,
    )
    """Total views number."""


class UtilsStatsSexAge(BaseModel):
    """
    Model: `UtilsStatsSexAge`
    """

    age_range: typing.Optional[str] = Field(
        default=None,
    )
    """Age denotation."""

    female: typing.Optional[int] = Field(
        default=None,
    )
    """ Views by female users."""

    male: typing.Optional[int] = Field(
        default=None,
    )
    """ Views by male users."""


class VideoEpisode(BaseModel):
    """
    Model: `VideoEpisode`
    """

    time: typing.Optional[int] = Field(
        default=None,
    )
    """Seconds from start of the video."""

    text: typing.Optional[str] = Field(
        default=None,
    )
    """Description of episode."""


class VideoLiveCategory(BaseModel):
    """
    Model: `VideoLiveCategory`
    """

    id: int = Field()
    """Property `VideoLiveCategory.id`."""

    label: str = Field()
    """Property `VideoLiveCategory.label`."""

    sublist: typing.Optional[typing.List["VideoLiveCategory"]] = Field(
        default=None,
    )
    """Property `VideoLiveCategory.sublist`."""


class VideoLiveInfo(BaseModel):
    """
    Model: `VideoLiveInfo`
    """

    enabled: bool = Field()
    """Property `VideoLiveInfo.enabled`."""

    is_notifications_blocked: typing.Optional[bool] = Field(
        default=None,
    )
    """Property `VideoLiveInfo.is_notifications_blocked`."""


class VideoLiveSettings(BaseModel):
    """
    Video live settings
    Model: `VideoLiveSettings`
    """

    can_rewind: typing.Optional[bool] = Field(
        default=None,
    )
    """If user car rewind live or not."""

    is_endless: typing.Optional[bool] = Field(
        default=None,
    )
    """If live is endless or not."""

    max_duration: typing.Optional[int] = Field(
        default=None,
    )
    """Max possible time for rewind."""

    is_clips_live: typing.Optional[bool] = Field(
        default=None,
    )
    """If live in clips apps."""


class VideoPlaylistPrivacyCategory(str, enum.Enum, metaclass=BaseEnumMeta):
    ALL = "all"
    FRIENDS = "friends"
    FRIENDS_OF_FRIENDS = "friends_of_friends"
    FRIENDS_OF_FRIENDS_ONLY = "friends_of_friends_only"
    ONLY_ME = "only_me"


class VideoSaveResult(BaseModel):
    """
    Model: `VideoSaveResult`
    """

    access_key: typing.Optional[str] = Field(
        default=None,
    )
    """Video access key."""

    description: typing.Optional[str] = Field(
        default=None,
    )
    """Video description."""

    owner_id: typing.Optional[int] = Field(
        default=None,
    )
    """Video owner ID."""

    title: typing.Optional[str] = Field(
        default=None,
    )
    """Video title."""

    upload_url: typing.Optional[str] = Field(
        default=None,
    )
    """URL for the video uploading."""

    video_id: typing.Optional[int] = Field(
        default=None,
    )
    """Video ID."""


class VideoStreamInputParams(BaseModel):
    """
    Model: `VideoStreamInputParams`
    """

    url: typing.Optional[str] = Field(
        default=None,
    )
    """Property `VideoStreamInputParams.url`."""

    key: typing.Optional[str] = Field(
        default=None,
    )
    """Property `VideoStreamInputParams.key`."""

    okmp_url: typing.Optional[str] = Field(
        default=None,
    )
    """Property `VideoStreamInputParams.okmp_url`."""

    webrtc_url: typing.Optional[str] = Field(
        default=None,
    )
    """Property `VideoStreamInputParams.webrtc_url`."""


class VideoVideoResponseType(str, enum.Enum, metaclass=BaseEnumMeta):
    MIN = "min"
    FULL = "full"


class VideoVideoType(str, enum.Enum, metaclass=BaseEnumMeta):
    INTERACTIVE = "interactive"
    VIDEO = "video"
    MUSIC_VIDEO = "music_video"
    MOVIE = "movie"
    LIVE = "live"
    SHORT_VIDEO = "short_video"
    STORY = "story"
    VIDEO_MESSAGE = "video_message"


class VideoVideo(BaseModel):
    """
    Model: `VideoVideo`
    """

    response_type: typing.Optional["VideoVideoResponseType"] = Field(
        default=None,
    )
    """Property `VideoVideo.response_type`."""

    access_key: typing.Optional[str] = Field(
        default=None,
    )
    """Video access key."""

    adding_date: typing.Optional[int] = Field(
        default=None,
    )
    """Date when the video has been added in Unixtime."""

    can_comment: typing.Optional[bool] = Field(
        default=None,
    )
    """Information whether current user can comment the video."""

    can_edit: typing.Optional[bool] = Field(
        default=None,
    )
    """Information whether current user can edit the video."""

    can_delete: typing.Optional[bool] = Field(
        default=None,
    )
    """Information whether current user can delete the video."""

    can_like: typing.Optional[bool] = Field(
        default=None,
    )
    """Information whether current user can like the video."""

    can_repost: typing.Optional[int] = Field(
        default=None,
    )
    """Information whether current user can repost the video."""

    can_subscribe: typing.Optional[bool] = Field(
        default=None,
    )
    """Information whether current user can subscribe to author of the video."""

    can_be_promoted: typing.Optional[bool] = Field(
        default=None,
    )
    """Information whether current user can promote the video."""

    can_add_to_faves: typing.Optional[bool] = Field(
        default=None,
    )
    """Information whether current user can add the video to favourites."""

    can_add: typing.Optional[bool] = Field(
        default=None,
    )
    """Information whether current user can add the video."""

    can_attach_link: typing.Optional[bool] = Field(
        default=None,
    )
    """Information whether current user can attach action button to the video."""

    can_edit_privacy: typing.Optional[bool] = Field(
        default=None,
    )
    """Information whether current user can edit the video privacy."""

    is_private: typing.Optional[bool] = Field(
        default=None,
    )
    """1 if video is private."""

    comments: typing.Optional[int] = Field(
        default=None,
    )
    """Number of comments."""

    date: typing.Optional[int] = Field(
        default=None,
    )
    """Date when video has been uploaded in Unixtime."""

    description: typing.Optional[str] = Field(
        default=None,
    )
    """Video description."""

    duration: typing.Optional[int] = Field(
        default=None,
    )
    """Video duration in seconds."""

    image: typing.Optional[typing.List["VideoVideoImage"]] = Field(
        default=None,
    )
    """Property `VideoVideo.image`."""

    first_frame: typing.Optional[typing.List["VideoVideoImage"]] = Field(
        default=None,
    )
    """Property `VideoVideo.first_frame`."""

    width: typing.Optional[int] = Field(
        default=None,
    )
    """Video width."""

    height: typing.Optional[int] = Field(
        default=None,
    )
    """Video height."""

    id: typing.Optional[int] = Field(
        default=None,
    )
    """Video ID."""

    owner_id: typing.Optional[int] = Field(
        default=None,
    )
    """Video owner ID."""

    user_id: typing.Optional[int] = Field(
        default=None,
    )
    """Id of the user who uploaded the video if it was uploaded to a group by member."""

    title: typing.Optional[str] = Field(
        default=None,
    )
    """Video title."""

    is_favorite: typing.Optional[bool] = Field(
        default=None,
    )
    """Whether video is added to bookmarks."""

    player: typing.Optional[str] = Field(
        default=None,
    )
    """Video embed URL."""

    processing: typing.Optional["BasePropertyExists"] = Field(
        default=None,
    )
    """Returns if the video is processing."""

    converting: typing.Optional[bool] = Field(
        default=None,
    )
    """1 if  video is being converted."""

    added: typing.Optional[bool] = Field(
        default=None,
    )
    """1 if video is added to user\'s albums."""

    is_subscribed: typing.Optional[bool] = Field(
        default=None,
    )
    """1 if user is subscribed to author of the video."""

    track_code: typing.Optional[str] = Field(
        default=None,
    )
    """Property `VideoVideo.track_code`."""

    repeat: typing.Optional["BasePropertyExists"] = Field(
        default=None,
    )
    """Information whether the video is repeated."""

    type: typing.Optional["VideoVideoType"] = Field(
        default=None,
    )
    """Property `VideoVideo.type`."""

    views: typing.Optional[int] = Field(
        default=None,
    )
    """Number of views."""

    local_views: typing.Optional[int] = Field(
        default=None,
    )
    """If video is external, number of views on vk."""

    content_restricted: typing.Optional[int] = Field(
        default=None,
    )
    """Restriction code."""

    content_restricted_message: typing.Optional[str] = Field(
        default=None,
    )
    """Restriction text."""

    balance: typing.Optional[int] = Field(
        default=None,
    )
    """Live donations balance."""

    live: typing.Optional["BasePropertyExists"] = Field(
        default=None,
    )
    """1 if the video is a live stream."""

    upcoming: typing.Optional["BasePropertyExists"] = Field(
        default=None,
    )
    """1 if the video is an upcoming stream."""

    live_start_time: typing.Optional[int] = Field(
        default=None,
    )
    """Date in Unixtime when the live stream is scheduled to start by the author."""

    live_notify: typing.Optional[bool] = Field(
        default=None,
    )
    """Whether current user is subscribed to the upcoming live stream notification (if not subscribed to the author)."""

    spectators: typing.Optional[int] = Field(
        default=None,
    )
    """Number of spectators of the stream."""

    platform: typing.Optional[str] = Field(
        default=None,
    )
    """External platform."""

    likes: typing.Optional["BaseLikes"] = Field(
        default=None,
    )
    """Property `VideoVideo.likes`."""

    reposts: typing.Optional["BaseRepostsInfo"] = Field(
        default=None,
    )
    """Property `VideoVideo.reposts`."""


class VideoVideoAlbumResponseType(str, enum.Enum, metaclass=BaseEnumMeta):
    MIN = "min"
    FULL = "full"


class VideoVideoAlbum(BaseModel):
    """
    Model: `VideoVideoAlbum`
    """

    id: int = Field()
    """Album ID."""

    owner_id: int = Field()
    """Album owner\'s ID."""

    title: str = Field()
    """Album title."""

    track_code: typing.Optional[str] = Field(
        default=None,
    )
    """Album trackcode."""

    response_type: typing.Optional["VideoVideoAlbumResponseType"] = Field(
        default=None,
    )
    """Property `VideoVideoAlbum.response_type`."""


class VideoVideoFiles(BaseModel):
    """
    Model: `VideoVideoFiles`
    """

    external: typing.Optional[str] = Field(
        default=None,
    )
    """URL of the external player."""

    mp4_144: typing.Optional[str] = Field(
        default=None,
    )
    """URL of the mpeg4 file with 144p quality."""

    mp4_240: typing.Optional[str] = Field(
        default=None,
    )
    """URL of the mpeg4 file with 240p quality."""

    mp4_360: typing.Optional[str] = Field(
        default=None,
    )
    """URL of the mpeg4 file with 360p quality."""

    mp4_480: typing.Optional[str] = Field(
        default=None,
    )
    """URL of the mpeg4 file with 480p quality."""

    mp4_720: typing.Optional[str] = Field(
        default=None,
    )
    """URL of the mpeg4 file with 720p quality."""

    mp4_1080: typing.Optional[str] = Field(
        default=None,
    )
    """URL of the mpeg4 file with 1080p quality."""

    mp4_1440: typing.Optional[str] = Field(
        default=None,
    )
    """URL of the mpeg4 file with 2K quality."""

    mp4_2160: typing.Optional[str] = Field(
        default=None,
    )
    """URL of the mpeg4 file with 4K quality."""

    flv_320: typing.Optional[str] = Field(
        default=None,
    )
    """URL of the flv file with 320p quality."""


class WallAppPost(BaseModel):
    """
    Model: `WallAppPost`
    """

    id: typing.Optional[int] = Field(
        default=None,
    )
    """Application ID."""

    name: typing.Optional[str] = Field(
        default=None,
    )
    """Application name."""

    photo_130: typing.Optional[str] = Field(
        default=None,
    )
    """URL of the preview image with 130 px in width."""

    photo_604: typing.Optional[str] = Field(
        default=None,
    )
    """URL of the preview image with 604 px in width."""


class WallAttachedNote(BaseModel):
    """
    Model: `WallAttachedNote`
    """

    comments: int = Field()
    """Comments number."""

    date: int = Field()
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

    text: typing.Optional[str] = Field(
        default=None,
    )
    """Note text."""

    privacy_view: typing.Optional[typing.List[str]] = Field(
        default=None,
    )
    """Property `WallAttachedNote.privacy_view`."""

    privacy_comment: typing.Optional[typing.List[str]] = Field(
        default=None,
    )
    """Property `WallAttachedNote.privacy_comment`."""

    can_comment: typing.Optional[int] = Field(
        default=None,
    )
    """Property `WallAttachedNote.can_comment`."""

    text_wiki: typing.Optional[str] = Field(
        default=None,
    )
    """Note wiki text."""


class WallCarouselBase(BaseModel):
    """
    Model: `WallCarouselBase`
    """

    carousel_offset: typing.Optional[int] = Field(
        default=None,
    )
    """Index of current carousel element."""


class WallCommentAttachment(BaseModel):
    """
    Model: `WallCommentAttachment`
    """

    type: "WallCommentAttachmentType" = Field()
    """Property `WallCommentAttachment.type`."""

    audio: typing.Optional["AudioAudio"] = Field(
        default=None,
    )
    """Property `WallCommentAttachment.audio`."""

    doc: typing.Optional["DocsDoc"] = Field(
        default=None,
    )
    """Property `WallCommentAttachment.doc`."""

    link: typing.Optional["BaseLink"] = Field(
        default=None,
    )
    """Property `WallCommentAttachment.link`."""

    market: typing.Optional["MarketMarketItem"] = Field(
        default=None,
    )
    """Property `WallCommentAttachment.market`."""

    market_market_album: typing.Optional["MarketMarketAlbum"] = Field(
        default=None,
    )
    """Property `WallCommentAttachment.market_market_album`."""

    note: typing.Optional["WallAttachedNote"] = Field(
        default=None,
    )
    """Property `WallCommentAttachment.note`."""

    page: typing.Optional["PagesWikipageFull"] = Field(
        default=None,
    )
    """Property `WallCommentAttachment.page`."""

    photo: typing.Optional["PhotosPhoto"] = Field(
        default=None,
    )
    """Property `WallCommentAttachment.photo`."""

    sticker: typing.Optional["BaseSticker"] = Field(
        default=None,
    )
    """Property `WallCommentAttachment.sticker`."""

    video: typing.Optional["VideoVideo"] = Field(
        default=None,
    )
    """Property `WallCommentAttachment.video`."""

    graffiti: typing.Optional["WallGraffiti"] = Field(
        default=None,
    )
    """Property `WallCommentAttachment.graffiti`."""


class WallCommentAttachmentType(str, enum.Enum, metaclass=BaseEnumMeta):
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


class WallGeoType(str, enum.Enum, metaclass=BaseEnumMeta):
    PLACE = "place"
    POINT = "point"


class WallGeo(BaseModel):
    """
    Model: `WallGeo`
    """

    coordinates: typing.Optional[str] = Field(
        default=None,
    )
    """Coordinates as string. <latitude> <longtitude>."""

    showmap: typing.Optional[int] = Field(
        default=None,
    )
    """Information whether a map is showed."""

    type: typing.Optional["WallGeoType"] = Field(
        default=None,
    )
    """Place type."""


class WallGetFilter(str, enum.Enum, metaclass=BaseEnumMeta):
    OWNER = "owner"
    OTHERS = "others"
    ALL = "all"
    POSTPONED = "postponed"
    SUGGESTS = "suggests"
    ARCHIVED = "archived"
    DONUT = "donut"


class WallGraffiti(BaseModel):
    """
    Model: `WallGraffiti`
    """

    id: typing.Optional[int] = Field(
        default=None,
    )
    """Graffiti ID."""

    owner_id: typing.Optional[int] = Field(
        default=None,
    )
    """Graffiti owner\'s ID."""

    photo_200: typing.Optional[str] = Field(
        default=None,
    )
    """URL of the preview image with 200 px in width."""

    photo_586: typing.Optional[str] = Field(
        default=None,
    )
    """URL of the preview image with 586 px in width."""

    height: typing.Optional[int] = Field(
        default=None,
    )
    """Graffiti height."""

    url: typing.Optional[str] = Field(
        default=None,
    )
    """Graffiti URL."""

    width: typing.Optional[int] = Field(
        default=None,
    )
    """Graffiti width."""

    access_key: typing.Optional[str] = Field(
        default=None,
    )
    """Access key for graffiti."""


class WallPostCopyright(BaseModel):
    """
    Model: `WallPostCopyright`
    """

    link: str = Field()
    """Property `WallPostCopyright.link`."""

    name: str = Field()
    """Property `WallPostCopyright.name`."""

    type: str = Field()
    """Property `WallPostCopyright.type`."""

    id: typing.Optional[int] = Field(
        default=None,
    )
    """Property `WallPostCopyright.id`."""


class WallPostSource(BaseModel):
    """
    Model: `WallPostSource`
    """

    data: typing.Optional[str] = Field(
        default=None,
    )
    """Additional data."""

    platform: typing.Optional[str] = Field(
        default=None,
    )
    """Platform name."""

    type: typing.Optional["WallPostSourceType"] = Field(
        default=None,
    )
    """Property `WallPostSource.type`."""

    url: typing.Optional[str] = Field(
        default=None,
    )
    """URL to an external site used to publish the post."""

    link: typing.Optional["BaseLink"] = Field(
        default=None,
    )
    """Property `WallPostSource.link`."""


class WallPostSourceType(str, enum.Enum, metaclass=BaseEnumMeta):
    VK = "vk"
    WIDGET = "widget"
    API = "api"
    RSS = "rss"
    SMS = "sms"
    MVK = "mvk"


class WallPostType(str, enum.Enum, metaclass=BaseEnumMeta):
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
    """
    Model: `WallPostedPhoto`
    """

    id: typing.Optional[int] = Field(
        default=None,
    )
    """Photo ID."""

    owner_id: typing.Optional[int] = Field(
        default=None,
    )
    """Photo owner\'s ID."""

    photo_130: typing.Optional[str] = Field(
        default=None,
    )
    """URL of the preview image with 130 px in width."""

    photo_604: typing.Optional[str] = Field(
        default=None,
    )
    """URL of the preview image with 604 px in width."""


class WallViews(BaseModel):
    """
    Model: `WallViews`
    """

    count: typing.Optional[int] = Field(
        default=None,
    )
    """Count."""


class WallWallComment(BaseModel):
    """
    Model: `WallWallComment`
    """

    id: int = Field()
    """Comment ID."""

    from_id: int = Field()
    """Author ID."""

    date: int = Field()
    """Date when the comment has been added in Unixtime."""

    text: str = Field()
    """Comment text."""

    can_edit: typing.Optional[bool] = Field(
        default=None,
    )
    """Property `WallWallComment.can_edit`."""

    post_id: typing.Optional[int] = Field(
        default=None,
    )
    """Property `WallWallComment.post_id`."""

    owner_id: typing.Optional[int] = Field(
        default=None,
    )
    """Property `WallWallComment.owner_id`."""

    parents_stack: typing.Optional[typing.List[int]] = Field(
        default=None,
    )
    """Property `WallWallComment.parents_stack`."""

    photo_id: typing.Optional[int] = Field(
        default=None,
    )
    """Property `WallWallComment.photo_id`."""

    video_id: typing.Optional[int] = Field(
        default=None,
    )
    """Property `WallWallComment.video_id`."""

    attachments: typing.Optional[typing.List["WallWallpostAttachment"]] = Field(
        default=None,
    )
    """Property `WallWallComment.attachments`."""

    donut: typing.Optional["WallWallCommentDonut"] = Field(
        default=None,
    )
    """Property `WallWallComment.donut`."""

    likes: typing.Optional["BaseLikesInfo"] = Field(
        default=None,
    )
    """Property `WallWallComment.likes`."""

    real_offset: typing.Optional[int] = Field(
        default=None,
    )
    """Real position of the comment."""

    reply_to_user: typing.Optional[int] = Field(
        default=None,
    )
    """Replied user ID."""

    reply_to_comment: typing.Optional[int] = Field(
        default=None,
    )
    """Replied comment ID."""

    thread: typing.Optional["CommentThread"] = Field(
        default=None,
    )
    """Property `WallWallComment.thread`."""

    is_from_post_author: typing.Optional[bool] = Field(
        default=None,
    )
    """Whether post is by author of the post or not."""

    deleted: typing.Optional[bool] = Field(
        default=None,
    )
    """Property `WallWallComment.deleted`."""

    pid: typing.Optional[int] = Field(
        default=None,
    )
    """Photo ID."""


class WallWallCommentDonut(BaseModel):
    """
    Model: `WallWallCommentDonut`
    """

    is_don: typing.Optional[bool] = Field(
        default=None,
    )
    """Means commentator is donator."""

    placeholder: typing.Optional["WallWallCommentDonutPlaceholder"] = Field(
        default=None,
    )
    """Property `WallWallCommentDonut.placeholder`."""


class WallWallCommentDonutPlaceholder(BaseModel):
    """
    Model: `WallWallCommentDonutPlaceholder`
    """

    text: str = Field()
    """Property `WallWallCommentDonutPlaceholder.text`."""


class WallWallItem(BaseModel):
    """
    Model: `WallWallItem`
    """

    copy_history: typing.Optional[typing.List["WallWallpostFull"]] = Field(
        default=None,
    )
    """Property `WallWallItem.copy_history`."""

    can_edit: typing.Optional[bool] = Field(
        default=None,
    )
    """Information whether current user can edit the post."""

    created_by: typing.Optional[int] = Field(
        default=None,
    )
    """Post creator ID (if post still can be edited)."""

    can_delete: typing.Optional[bool] = Field(
        default=None,
    )
    """Information whether current user can delete the post."""

    can_pin: typing.Optional[bool] = Field(
        default=None,
    )
    """Information whether current user can pin the post."""

    donut: typing.Optional["WallWallpostDonut"] = Field(
        default=None,
    )
    """Property `WallWallItem.donut`."""

    is_pinned: typing.Optional[bool] = Field(
        default=None,
    )
    """Information whether the post is pinned."""

    comments: typing.Optional["BaseCommentsInfo"] = Field(
        default=None,
    )
    """Property `WallWallItem.comments`."""

    marked_as_ads: typing.Optional[bool] = Field(
        default=None,
    )
    """Information whether the post is marked as ads."""

    topic_id: typing.Optional[int] = Field(
        default=None,
    )
    """Topic ID. Allowed values can be obtained from newsfeed.getPostTopics method."""

    short_text_rate: typing.Optional[float] = Field(
        default=None,
    )
    """Preview length control parameter."""

    hash: typing.Optional[str] = Field(
        default=None,
    )
    """Hash for sharing."""

    type: typing.Optional["WallPostType"] = Field(
        default=None,
    )
    """Property `WallWallItem.type`."""

    feedback: typing.Optional["NewsfeedItemWallpostFeedback"] = Field(
        default=None,
    )
    """Property `WallWallItem.feedback`."""

    to_id: typing.Optional[int] = Field(
        default=None,
    )
    """Property `WallWallItem.to_id`."""


class WallWallpostInnerType(str, enum.Enum, metaclass=BaseEnumMeta):
    WALL_WALLPOST = "wall_wallpost"


class WallWallpost(BaseModel):
    """
    Model: `WallWallpost`
    """

    inner_type: "WallWallpostInnerType" = Field()
    """Property `WallWallpost.inner_type`."""

    access_key: typing.Optional[str] = Field(
        default=None,
    )
    """Access key to private object."""

    is_deleted: typing.Optional[bool] = Field(
        default=None,
    )
    """Property `WallWallpost.is_deleted`."""

    deleted_reason: typing.Optional[str] = Field(
        default=None,
    )
    """Property `WallWallpost.deleted_reason`."""

    deleted_details: typing.Optional[str] = Field(
        default=None,
    )
    """Property `WallWallpost.deleted_details`."""

    donut_miniapp_url: typing.Optional[str] = Field(
        default=None,
    )
    """Property `WallWallpost.donut_miniapp_url`."""

    attachments: typing.Optional[typing.List["WallWallpostAttachment"]] = Field(
        default=None,
    )
    """Property `WallWallpost.attachments`."""

    copyright: typing.Optional["WallPostCopyright"] = Field(
        default=None,
    )
    """Information about the source of the post."""

    date: typing.Optional[int] = Field(
        default=None,
    )
    """Date of publishing in Unixtime."""

    edited: typing.Optional[int] = Field(
        default=None,
    )
    """Date of editing in Unixtime."""

    from_id: typing.Optional[int] = Field(
        default=None,
    )
    """Post author ID."""

    geo: typing.Optional["WallGeo"] = Field(
        default=None,
    )
    """Property `WallWallpost.geo`."""

    id: typing.Optional[int] = Field(
        default=None,
    )
    """Post ID."""

    is_archived: typing.Optional[bool] = Field(
        default=None,
    )
    """Is post archived, only for post owners."""

    is_favorite: typing.Optional[bool] = Field(
        default=None,
    )
    """Information whether the post in favorites list."""

    likes: typing.Optional["BaseLikesInfo"] = Field(
        default=None,
    )
    """Count of likes."""

    owner_id: typing.Optional[int] = Field(
        default=None,
    )
    """Wall owner\'s ID."""

    post_id: typing.Optional[int] = Field(
        default=None,
    )
    """If post type \'reply\', contains original post ID."""

    parents_stack: typing.Optional[typing.List[int]] = Field(
        default=None,
    )
    """If post type \'reply\', contains original parent IDs stack."""

    post_source: typing.Optional["WallPostSource"] = Field(
        default=None,
    )
    """Property `WallWallpost.post_source`."""

    post_type: typing.Optional["WallPostType"] = Field(
        default=None,
    )
    """Property `WallWallpost.post_type`."""

    reposts: typing.Optional["BaseRepostsInfo"] = Field(
        default=None,
    )
    """Property `WallWallpost.reposts`."""

    signer_id: typing.Optional[int] = Field(
        default=None,
    )
    """Post signer ID."""

    text: typing.Optional[str] = Field(
        default=None,
    )
    """Post text."""

    views: typing.Optional["WallViews"] = Field(
        default=None,
    )
    """Count of views."""


class WallWallpostAttachment(BaseModel):
    """
    Model: `WallWallpostAttachment`
    """

    type: "WallWallpostAttachmentType" = Field()
    """Property `WallWallpostAttachment.type`."""

    access_key: typing.Optional[str] = Field(
        default=None,
    )
    """Access key for the audio."""

    album: typing.Optional["PhotosPhotoAlbum"] = Field(
        default=None,
    )
    """Property `WallWallpostAttachment.album`."""

    app: typing.Optional["WallAppPost"] = Field(
        default=None,
    )
    """Property `WallWallpostAttachment.app`."""

    audio: typing.Optional["AudioAudio"] = Field(
        default=None,
    )
    """Property `WallWallpostAttachment.audio`."""

    doc: typing.Optional["DocsDoc"] = Field(
        default=None,
    )
    """Property `WallWallpostAttachment.doc`."""

    event: typing.Optional["EventsEventAttach"] = Field(
        default=None,
    )
    """Property `WallWallpostAttachment.event`."""

    group: typing.Optional["GroupsGroupAttach"] = Field(
        default=None,
    )
    """Property `WallWallpostAttachment.group`."""

    graffiti: typing.Optional["WallGraffiti"] = Field(
        default=None,
    )
    """Property `WallWallpostAttachment.graffiti`."""

    link: typing.Optional["BaseLink"] = Field(
        default=None,
    )
    """Property `WallWallpostAttachment.link`."""

    market: typing.Optional["MarketMarketItem"] = Field(
        default=None,
    )
    """Property `WallWallpostAttachment.market`."""

    market_album: typing.Optional["MarketMarketAlbum"] = Field(
        default=None,
    )
    """Property `WallWallpostAttachment.market_album`."""

    note: typing.Optional["NotesNote"] = Field(
        default=None,
    )
    """Property `WallWallpostAttachment.note`."""

    page: typing.Optional["PagesWikipageFull"] = Field(
        default=None,
    )
    """Property `WallWallpostAttachment.page`."""

    photo: typing.Optional["PhotosPhoto"] = Field(
        default=None,
    )
    """Property `WallWallpostAttachment.photo`."""

    poll: typing.Optional["PollsPoll"] = Field(
        default=None,
    )
    """Property `WallWallpostAttachment.poll`."""

    posted_photo: typing.Optional["WallPostedPhoto"] = Field(
        default=None,
    )
    """Property `WallWallpostAttachment.posted_photo`."""

    video: typing.Optional["VideoVideoFull"] = Field(
        default=None,
    )
    """Property `WallWallpostAttachment.video`."""

    clip: typing.Optional["VideoVideoFull"] = Field(
        default=None,
    )
    """Property `WallWallpostAttachment.clip`."""

    video_playlist: typing.Optional["VideoVideoAlbumFull"] = Field(
        default=None,
    )
    """Property `WallWallpostAttachment.video_playlist`."""


class WallWallpostAttachmentType(str, enum.Enum, metaclass=BaseEnumMeta):
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
    """
    Model: `WallWallpostCommentsDonut`
    """

    placeholder: typing.Optional["WallWallpostCommentsDonutPlaceholder"] = Field(
        default=None,
    )
    """Property `WallWallpostCommentsDonut.placeholder`."""


class WallWallpostCommentsDonutPlaceholder(BaseModel):
    """
    Info about paid comments feature
    Model: `WallWallpostCommentsDonutPlaceholder`
    """

    text: str = Field()
    """Property `WallWallpostCommentsDonutPlaceholder.text`."""


class WallWallpostDonutEditMode(str, enum.Enum, metaclass=BaseEnumMeta):
    ALL = "all"
    DURATION = "duration"


class WallWallpostDonut(BaseModel):
    """
    Info about paid wall post
    Model: `WallWallpostDonut`
    """

    is_donut: bool = Field()
    """Post only for dons."""

    paid_duration: typing.Optional[int] = Field(
        default=None,
    )
    """Value of this field need to pass in wall.post/edit in donut_paid_duration."""

    placeholder: typing.Optional["WallWallpostDonutPlaceholder"] = Field(
        default=None,
    )
    """If placeholder was respond, text and all attachments will be hidden."""

    can_publish_free_copy: typing.Optional[bool] = Field(
        default=None,
    )
    """Says whether group admin can post free copy of this donut post."""

    edit_mode: typing.Optional["WallWallpostDonutEditMode"] = Field(
        default=None,
    )
    """Says what user can edit in post about donut properties."""


class WallWallpostDonutPlaceholder(BaseModel):
    """
    Model: `WallWallpostDonutPlaceholder`
    """

    text: str = Field()
    """Property `WallWallpostDonutPlaceholder.text`."""


class NewsfeedCommentsFilters(str, enum.Enum, metaclass=BaseEnumMeta):
    POST = "post"
    PHOTO = "photo"
    VIDEO = "video"
    TOPIC = "topic"
    NOTE = "note"


class NewsfeedCommentsItem(BaseModel):
    """
    Model: `NewsfeedCommentsItem`
    """


class NewsfeedCommentsItemBase(BaseModel):
    """
    Model: `NewsfeedCommentsItemBase`
    """

    type: "NewsfeedNewsfeedItemType" = Field()
    """Property `NewsfeedCommentsItemBase.type`."""

    source_id: typing.Optional[int] = Field(
        default=None,
    )
    """Property `NewsfeedCommentsItemBase.source_id`."""

    date: typing.Optional[int] = Field(
        default=None,
    )
    """Property `NewsfeedCommentsItemBase.date`."""

    post_id: typing.Optional[int] = Field(
        default=None,
    )
    """Property `NewsfeedCommentsItemBase.post_id`."""


class NewsfeedIgnoreItemType(str, enum.Enum, metaclass=BaseEnumMeta):
    WALL = "wall"
    TAG = "tag"
    PROFILEPHOTO = "profilephoto"
    VIDEO = "video"
    PHOTO = "photo"
    AUDIO = "audio"


class NewsfeedItemAudioAudio(BaseModel):
    """
    Model: `NewsfeedItemAudioAudio`
    """

    count: typing.Optional[int] = Field(
        default=None,
    )
    """Audios number."""

    items: typing.Optional[typing.List["AudioAudio"]] = Field(
        default=None,
    )
    """Property `NewsfeedItemAudioAudio.items`."""


class NewsfeedItemBase(BaseModel):
    """
    Model: `NewsfeedItemBase`
    """

    type: "NewsfeedNewsfeedItemType" = Field()
    """Property `NewsfeedItemBase.type`."""

    source_id: int = Field()
    """Item source ID."""

    date: int = Field()
    """Date when item has been added in Unixtime."""

    short_text_rate: typing.Optional[float] = Field(
        default=None,
    )
    """Preview length control parameter."""

    feedback: typing.Optional["NewsfeedItemWallpostFeedback"] = Field(
        default=None,
    )
    """Property `NewsfeedItemBase.feedback`."""


class NewsfeedItemDigestButtonStyle(str, enum.Enum, metaclass=BaseEnumMeta):
    PRIMARY = "primary"


class NewsfeedItemDigestButton(BaseModel):
    """
    Model: `NewsfeedItemDigestButton`
    """

    title: str = Field()
    """Property `NewsfeedItemDigestButton.title`."""

    style: typing.Optional["NewsfeedItemDigestButtonStyle"] = Field(
        default=None,
    )
    """Property `NewsfeedItemDigestButton.style`."""


class NewsfeedItemDigestFooterStyle(str, enum.Enum, metaclass=BaseEnumMeta):
    TEXT = "text"
    BUTTON = "button"


class NewsfeedItemDigestFooter(BaseModel):
    """
    Model: `NewsfeedItemDigestFooter`
    """

    style: "NewsfeedItemDigestFooterStyle" = Field()
    """Property `NewsfeedItemDigestFooter.style`."""

    text: str = Field()
    """text for invite to enable smart feed."""

    button: typing.Optional["NewsfeedItemDigestButton"] = Field(
        default=None,
    )
    """Property `NewsfeedItemDigestFooter.button`."""

    feed_id: typing.Optional[str] = Field(
        default=None,
    )
    """Property `NewsfeedItemDigestFooter.feed_id`."""


class NewsfeedItemDigestHeaderStyle(str, enum.Enum, metaclass=BaseEnumMeta):
    SINGLELINE = "singleline"
    MULTILINE = "multiline"


class NewsfeedItemDigestHeader(BaseModel):
    """
    Model: `NewsfeedItemDigestHeader`
    """

    title: str = Field()
    """Title of the header."""

    style: "NewsfeedItemDigestHeaderStyle" = Field()
    """Property `NewsfeedItemDigestHeader.style`."""

    subtitle: typing.Optional[str] = Field(
        default=None,
    )
    """Subtitle of the header, when title have two strings."""

    badge_text: typing.Optional[str] = Field(
        default=None,
    )
    """Optional field for red badge in Trends feed blocks."""

    button: typing.Optional["NewsfeedItemDigestButton"] = Field(
        default=None,
    )
    """Property `NewsfeedItemDigestHeader.button`."""


class NewsfeedItemDigestItem(BaseModel):
    """
    Model: `NewsfeedItemDigestItem`
    """

    inner_type: str = Field()
    """Property `NewsfeedItemDigestItem.inner_type`."""

    post: "NewsfeedItemWallpost" = Field()
    """Property `NewsfeedItemDigestItem.post`."""

    text: typing.Optional[str] = Field(
        default=None,
    )
    """Property `NewsfeedItemDigestItem.text`."""

    source_name: typing.Optional[str] = Field(
        default=None,
    )
    """Property `NewsfeedItemDigestItem.source_name`."""

    attachment_index: typing.Optional[int] = Field(
        default=None,
    )
    """Property `NewsfeedItemDigestItem.attachment_index`."""

    attachment: typing.Optional["WallWallpostAttachment"] = Field(
        default=None,
    )
    """Property `NewsfeedItemDigestItem.attachment`."""

    style: typing.Optional[str] = Field(
        default=None,
    )
    """Property `NewsfeedItemDigestItem.style`."""

    badge_text: typing.Optional[str] = Field(
        default=None,
    )
    """Optional red badge for posts in digest block."""


class NewsfeedItemFriendFriends(BaseModel):
    """
    Model: `NewsfeedItemFriendFriends`
    """

    count: typing.Optional[int] = Field(
        default=None,
    )
    """Number of friends has been added."""

    items: typing.Optional[typing.List["BaseUserId"]] = Field(
        default=None,
    )
    """Property `NewsfeedItemFriendFriends.items`."""


class NewsfeedItemHolidayRecommendationsBlockHeader(BaseModel):
    """
    Model: `NewsfeedItemHolidayRecommendationsBlockHeader`
    """

    title: typing.Optional[str] = Field(
        default=None,
    )
    """Title of the header."""

    subtitle: typing.Optional[str] = Field(
        default=None,
    )
    """Subtitle of the header."""

    image: typing.Optional[typing.List["BaseImage"]] = Field(
        default=None,
    )
    """Property `NewsfeedItemHolidayRecommendationsBlockHeader.image`."""

    action: typing.Optional["BaseLinkButtonAction"] = Field(
        default=None,
    )
    """Property `NewsfeedItemHolidayRecommendationsBlockHeader.action`."""


class NewsfeedItemPhotoPhotos(BaseModel):
    """
    Model: `NewsfeedItemPhotoPhotos`
    """

    count: typing.Optional[int] = Field(
        default=None,
    )
    """Photos number."""

    items: typing.Optional[typing.List["PhotosPhoto"]] = Field(
        default=None,
    )
    """Property `NewsfeedItemPhotoPhotos.items`."""


class NewsfeedItemPhotoTagPhotoTags(BaseModel):
    """
    Model: `NewsfeedItemPhotoTagPhotoTags`
    """

    count: typing.Optional[int] = Field(
        default=None,
    )
    """Tags number."""

    items: typing.Optional[typing.List["PhotosPhoto"]] = Field(
        default=None,
    )
    """Property `NewsfeedItemPhotoTagPhotoTags.items`."""


class NewsfeedItemPromoButtonAction(BaseModel):
    """
    Model: `NewsfeedItemPromoButtonAction`
    """

    url: typing.Optional[str] = Field(
        default=None,
    )
    """Property `NewsfeedItemPromoButtonAction.url`."""

    type: typing.Optional[str] = Field(
        default=None,
    )
    """Property `NewsfeedItemPromoButtonAction.type`."""

    target: typing.Optional[str] = Field(
        default=None,
    )
    """Property `NewsfeedItemPromoButtonAction.target`."""


class NewsfeedItemPromoButtonImage(BaseModel):
    """
    Model: `NewsfeedItemPromoButtonImage`
    """

    width: typing.Optional[int] = Field(
        default=None,
    )
    """Property `NewsfeedItemPromoButtonImage.width`."""

    height: typing.Optional[int] = Field(
        default=None,
    )
    """Property `NewsfeedItemPromoButtonImage.height`."""

    url: typing.Optional[str] = Field(
        default=None,
    )
    """Property `NewsfeedItemPromoButtonImage.url`."""


class NewsfeedItemVideoVideo(BaseModel):
    """
    Model: `NewsfeedItemVideoVideo`
    """

    count: typing.Optional[int] = Field(
        default=None,
    )
    """Tags number."""

    items: typing.Optional[typing.List["VideoVideoFull"]] = Field(
        default=None,
    )
    """Property `NewsfeedItemVideoVideo.items`."""


class NewsfeedItemWallpostFeedback(BaseModel):
    """
    Model: `NewsfeedItemWallpostFeedback`
    """

    type: "NewsfeedItemWallpostFeedbackType" = Field()
    """Property `NewsfeedItemWallpostFeedback.type`."""

    question: str = Field()
    """Property `NewsfeedItemWallpostFeedback.question`."""

    answers: typing.Optional[typing.List["NewsfeedItemWallpostFeedbackAnswer"]] = Field(
        default=None,
    )
    """Property `NewsfeedItemWallpostFeedback.answers`."""

    stars_count: typing.Optional[int] = Field(
        default=None,
    )
    """Property `NewsfeedItemWallpostFeedback.stars_count`."""

    descriptions: typing.Optional[typing.List[str]] = Field(
        default=None,
    )
    """Property `NewsfeedItemWallpostFeedback.descriptions`."""

    gratitude: typing.Optional[str] = Field(
        default=None,
    )
    """Property `NewsfeedItemWallpostFeedback.gratitude`."""

    track_code: typing.Optional[str] = Field(
        default=None,
    )
    """Property `NewsfeedItemWallpostFeedback.track_code`."""


class NewsfeedItemWallpostFeedbackAnswer(BaseModel):
    """
    Model: `NewsfeedItemWallpostFeedbackAnswer`
    """

    title: str = Field()
    """Property `NewsfeedItemWallpostFeedbackAnswer.title`."""

    id: str = Field()
    """Property `NewsfeedItemWallpostFeedbackAnswer.id`."""


class NewsfeedItemWallpostFeedbackType(str, enum.Enum, metaclass=BaseEnumMeta):
    BUTTONS = "buttons"
    STARS = "stars"


class NewsfeedList(BaseModel):
    """
    Model: `NewsfeedList`
    """

    id: int = Field()
    """List ID."""

    title: str = Field()
    """List title."""


class NewsfeedNewsfeedItem(BaseModel):
    """
    Model: `NewsfeedNewsfeedItem`
    """


class NewsfeedNewsfeedItemType(str, enum.Enum, metaclass=BaseEnumMeta):
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
    """
    Model: `WidgetsCommentMedia`
    """

    item_id: typing.Optional[int] = Field(
        default=None,
    )
    """Media item ID."""

    owner_id: typing.Optional[int] = Field(
        default=None,
    )
    """Media owner\'s ID."""

    thumb_src: typing.Optional[str] = Field(
        default=None,
    )
    """URL of the preview image (type=photo only)."""

    type: typing.Optional["WidgetsCommentMediaType"] = Field(
        default=None,
    )
    """Property `WidgetsCommentMedia.type`."""


class WidgetsCommentMediaType(str, enum.Enum, metaclass=BaseEnumMeta):
    AUDIO = "audio"
    PHOTO = "photo"
    VIDEO = "video"


class WidgetsCommentReplies(BaseModel):
    """
    Model: `WidgetsCommentReplies`
    """

    can_post: typing.Optional[bool] = Field(
        default=None,
    )
    """Information whether current user can comment the post."""

    count: typing.Optional[int] = Field(
        default=None,
    )
    """Comments number."""

    replies: typing.Optional[typing.List["WidgetsCommentRepliesItem"]] = Field(
        default=None,
    )
    """Property `WidgetsCommentReplies.replies`."""

    groups_can_post: typing.Optional[bool] = Field(
        default=None,
    )
    """Information whether groups can comment the post."""

    can_view: typing.Optional[bool] = Field(
        default=None,
    )
    """Information whether current user can view the comments."""


class WidgetsCommentRepliesItem(BaseModel):
    """
    Model: `WidgetsCommentRepliesItem`
    """

    cid: typing.Optional[int] = Field(
        default=None,
    )
    """Comment ID."""

    date: typing.Optional[int] = Field(
        default=None,
    )
    """Date when the comment has been added in Unixtime."""

    likes: typing.Optional["WidgetsWidgetLikes"] = Field(
        default=None,
    )
    """Property `WidgetsCommentRepliesItem.likes`."""

    text: typing.Optional[str] = Field(
        default=None,
    )
    """Comment text."""

    uid: typing.Optional[int] = Field(
        default=None,
    )
    """User ID."""

    user: typing.Optional["UsersUserFull"] = Field(
        default=None,
    )
    """Property `WidgetsCommentRepliesItem.user`."""


class WidgetsWidgetComment(BaseModel):
    """
    Model: `WidgetsWidgetComment`
    """

    date: int = Field()
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

    attachments: typing.Optional[typing.List["WallCommentAttachment"]] = Field(
        default=None,
    )
    """Property `WidgetsWidgetComment.attachments`."""

    owner_id: typing.Optional[int] = Field(
        default=None,
    )
    """Wall owner\'s ID."""

    can_delete: typing.Optional[bool] = Field(
        default=None,
    )
    """Information whether current user can delete the comment."""

    comments: typing.Optional["WidgetsCommentReplies"] = Field(
        default=None,
    )
    """Property `WidgetsWidgetComment.comments`."""

    likes: typing.Optional["BaseLikesInfo"] = Field(
        default=None,
    )
    """Property `WidgetsWidgetComment.likes`."""

    media: typing.Optional["WidgetsCommentMedia"] = Field(
        default=None,
    )
    """Property `WidgetsWidgetComment.media`."""

    post_source: typing.Optional["WallPostSource"] = Field(
        default=None,
    )
    """Property `WidgetsWidgetComment.post_source`."""

    reposts: typing.Optional["BaseRepostsInfo"] = Field(
        default=None,
    )
    """Property `WidgetsWidgetComment.reposts`."""

    user: typing.Optional["UsersUserFull"] = Field(
        default=None,
    )
    """Property `WidgetsWidgetComment.user`."""

    is_favorite: typing.Optional[bool] = Field(
        default=None,
    )
    """Information whether the post in favorites list."""

    short_text_rate: typing.Optional[float] = Field(
        default=None,
    )
    """Preview length control parameter."""


class WidgetsWidgetLikes(BaseModel):
    """
    Model: `WidgetsWidgetLikes`
    """

    count: typing.Optional[int] = Field(
        default=None,
    )
    """Likes number."""


class WidgetsWidgetPage(BaseModel):
    """
    Model: `WidgetsWidgetPage`
    """

    comments: typing.Optional["BaseObjectCount"] = Field(
        default=None,
    )
    """Property `WidgetsWidgetPage.comments`."""

    date: typing.Optional[int] = Field(
        default=None,
    )
    """Date when widgets on the page has been initialized firstly in Unixtime."""

    description: typing.Optional[str] = Field(
        default=None,
    )
    """Page description."""

    id: typing.Optional[int] = Field(
        default=None,
    )
    """Page ID."""

    likes: typing.Optional["BaseObjectCount"] = Field(
        default=None,
    )
    """Property `WidgetsWidgetPage.likes`."""

    page_id: typing.Optional[str] = Field(
        default=None,
    )
    """page_id parameter value."""

    photo: typing.Optional[str] = Field(
        default=None,
    )
    """URL of the preview image."""

    title: typing.Optional[str] = Field(
        default=None,
    )
    """Page title."""

    url: typing.Optional[str] = Field(
        default=None,
    )
    """Page absolute URL."""


class BaseLink(BaseLinkNoProduct):
    """
    Model: `BaseLink`
    """

    text: typing.Optional[str] = Field(
        default=None,
    )
    """Property `BaseLink.text`."""

    product: typing.Optional["BaseLinkProduct"] = Field(
        default=None,
    )
    """Property `BaseLink.product`."""


class UsersUser(UsersUserMin):
    """
    Model: `UsersUser`
    """

    sex: typing.Optional["BaseSex"] = Field(
        default=None,
    )
    """User sex."""

    screen_name: typing.Optional[str] = Field(
        default=None,
    )
    """Domain name of the user\'s page."""

    photo_50: typing.Optional[str] = Field(
        default=None,
    )
    """URL of square photo of the user with 50 pixels in width."""

    photo_100: typing.Optional[str] = Field(
        default=None,
    )
    """URL of square photo of the user with 100 pixels in width."""

    online_info: typing.Optional["UsersOnlineInfo"] = Field(
        default=None,
    )
    """Property `UsersUser.online_info`."""

    online: typing.Optional[bool] = Field(
        default=None,
    )
    """Information whether the user is online."""

    online_mobile: typing.Optional[bool] = Field(
        default=None,
    )
    """Information whether the user is online in mobile site or application."""

    online_app: typing.Optional[int] = Field(
        default=None,
    )
    """Application ID."""

    verified: typing.Optional[bool] = Field(
        default=None,
    )
    """Information whether the user is verified."""

    trending: typing.Optional[bool] = Field(
        default=None,
    )
    """Information whether the user has a \"fire\" pictogram.."""

    friend_status: typing.Optional["FriendsFriendStatusStatus"] = Field(
        default=None,
    )
    """Property `UsersUser.friend_status`."""

    mutual: typing.Optional["FriendsRequestsMutual"] = Field(
        default=None,
    )
    """Property `UsersUser.mutual`."""


class UsersUserFull(UsersUser):
    """
    Model: `UsersUserFull`
    """

    first_name_nom: typing.Optional[str] = Field(
        default=None,
    )
    """User\'s first name in nominative case."""

    first_name_gen: typing.Optional[str] = Field(
        default=None,
    )
    """User\'s first name in genitive case."""

    first_name_dat: typing.Optional[str] = Field(
        default=None,
    )
    """User\'s first name in dative case."""

    first_name_acc: typing.Optional[str] = Field(
        default=None,
    )
    """User\'s first name in accusative case."""

    first_name_ins: typing.Optional[str] = Field(
        default=None,
    )
    """User\'s first name in instrumental case."""

    first_name_abl: typing.Optional[str] = Field(
        default=None,
    )
    """User\'s first name in prepositional case."""

    last_name_nom: typing.Optional[str] = Field(
        default=None,
    )
    """User\'s last name in nominative case."""

    last_name_gen: typing.Optional[str] = Field(
        default=None,
    )
    """User\'s last name in genitive case."""

    last_name_dat: typing.Optional[str] = Field(
        default=None,
    )
    """User\'s last name in dative case."""

    last_name_acc: typing.Optional[str] = Field(
        default=None,
    )
    """User\'s last name in accusative case."""

    last_name_ins: typing.Optional[str] = Field(
        default=None,
    )
    """User\'s last name in instrumental case."""

    last_name_abl: typing.Optional[str] = Field(
        default=None,
    )
    """User\'s last name in prepositional case."""

    nickname: typing.Optional[str] = Field(
        default=None,
    )
    """User nickname."""

    maiden_name: typing.Optional[str] = Field(
        default=None,
    )
    """User maiden name."""

    contact_name: typing.Optional[str] = Field(
        default=None,
    )
    """User contact name."""

    domain: typing.Optional[str] = Field(
        default=None,
    )
    """Domain name of the user\'s page."""

    bdate: typing.Optional[str] = Field(
        default=None,
    )
    """User\'s date of birth."""

    city: typing.Optional["BaseCity"] = Field(
        default=None,
    )
    """Property `UsersUserFull.city`."""

    timezone: typing.Optional[float] = Field(
        default=None,
    )
    """User\'s timezone."""

    owner_state: typing.Optional["OwnerState"] = Field(
        default=None,
    )
    """Property `UsersUserFull.owner_state`."""

    photo_200: typing.Optional[str] = Field(
        default=None,
    )
    """URL of square photo of the user with 200 pixels in width."""

    photo_max: typing.Optional[str] = Field(
        default=None,
    )
    """URL of square photo of the user with maximum width."""

    photo_200_orig: typing.Optional[str] = Field(
        default=None,
    )
    """URL of user\'s photo with 200 pixels in width."""

    photo_400_orig: typing.Optional[str] = Field(
        default=None,
    )
    """URL of user\'s photo with 400 pixels in width."""

    photo_max_orig: typing.Optional[str] = Field(
        default=None,
    )
    """URL of user\'s photo of maximum size."""

    photo_id: typing.Optional[str] = Field(
        default=None,
    )
    """ID of the user\'s main photo."""

    has_photo: typing.Optional[bool] = Field(
        default=None,
    )
    """Information whether the user has main photo."""

    has_mobile: typing.Optional[bool] = Field(
        default=None,
    )
    """Information whether the user specified his phone number."""

    is_friend: typing.Optional[bool] = Field(
        default=None,
    )
    """Information whether the user is a friend of current user."""

    is_best_friend: typing.Optional[bool] = Field(
        default=None,
    )
    """Information whether the user is a best friend of current user."""

    wall_comments: typing.Optional[bool] = Field(
        default=None,
    )
    """Information whether current user can comment wall posts."""

    can_post: typing.Optional[bool] = Field(
        default=None,
    )
    """Information whether current user can post on the user\'s wall."""

    can_see_all_posts: typing.Optional[bool] = Field(
        default=None,
    )
    """Information whether current user can see other users\' audio on the wall."""

    can_see_audio: typing.Optional[bool] = Field(
        default=None,
    )
    """Information whether current user can see the user\'s audio."""

    type: typing.Optional["UsersUserType"] = Field(
        default=None,
    )
    """Property `UsersUserFull.type`."""

    email: typing.Optional[str] = Field(
        default=None,
    )
    """Property `UsersUserFull.email`."""

    skype: typing.Optional[str] = Field(
        default=None,
    )
    """Property `UsersUserFull.skype`."""

    facebook: typing.Optional[str] = Field(
        default=None,
    )
    """Property `UsersUserFull.facebook`."""

    facebook_name: typing.Optional[str] = Field(
        default=None,
    )
    """Property `UsersUserFull.facebook_name`."""

    twitter: typing.Optional[str] = Field(
        default=None,
    )
    """Property `UsersUserFull.twitter`."""

    livejournal: typing.Optional[str] = Field(
        default=None,
    )
    """Property `UsersUserFull.livejournal`."""

    instagram: typing.Optional[str] = Field(
        default=None,
    )
    """Property `UsersUserFull.instagram`."""

    test: typing.Optional[bool] = Field(
        default=None,
    )
    """Property `UsersUserFull.test`."""

    video_live: typing.Optional["VideoLiveInfo"] = Field(
        default=None,
    )
    """Property `UsersUserFull.video_live`."""

    is_video_live_notifications_blocked: typing.Optional[bool] = Field(
        default=None,
    )
    """Property `UsersUserFull.is_video_live_notifications_blocked`."""

    is_service: typing.Optional[bool] = Field(
        default=None,
    )
    """Property `UsersUserFull.is_service`."""

    service_description: typing.Optional[str] = Field(
        default=None,
    )
    """Property `UsersUserFull.service_description`."""

    photo_rec: typing.Optional[typing.Union["str", "bool"]] = Field(
        default=None,
    )
    """Property `UsersUserFull.photo_rec`."""

    photo_medium: typing.Optional[typing.Union["str", "bool"]] = Field(
        default=None,
    )
    """Property `UsersUserFull.photo_medium`."""

    photo_medium_rec: typing.Optional[typing.Union["str", "bool"]] = Field(
        default=None,
    )
    """Property `UsersUserFull.photo_medium_rec`."""

    photo: typing.Optional[str] = Field(
        default=None,
    )
    """Property `UsersUserFull.photo`."""

    photo_big: typing.Optional[str] = Field(
        default=None,
    )
    """Property `UsersUserFull.photo_big`."""

    photo_400: typing.Optional[str] = Field(
        default=None,
    )
    """Property `UsersUserFull.photo_400`."""

    photo_max_size: typing.Optional["PhotosPhoto"] = Field(
        default=None,
    )
    """Property `UsersUserFull.photo_max_size`."""

    language: typing.Optional[str] = Field(
        default=None,
    )
    """Property `UsersUserFull.language`."""

    stories_archive_count: typing.Optional[int] = Field(
        default=None,
    )
    """Property `UsersUserFull.stories_archive_count`."""

    has_unseen_stories: typing.Optional[bool] = Field(
        default=None,
    )
    """Property `UsersUserFull.has_unseen_stories`."""

    wall_default: typing.Optional[str] = Field(
        default=None,
    )
    """Property `UsersUserFull.wall_default`."""

    can_call: typing.Optional[bool] = Field(
        default=None,
    )
    """Information whether current user can call."""

    can_call_from_group: typing.Optional[bool] = Field(
        default=None,
    )
    """Information whether group can call user."""

    can_invite_as_voicerooms_speaker: typing.Optional[bool] = Field(
        default=None,
    )
    """Information whether user/group can invite user as voicerooms speakr."""

    can_see_wishes: typing.Optional[bool] = Field(
        default=None,
    )
    """Information whether current user can see the user\'s wishes."""

    can_see_gifts: typing.Optional[bool] = Field(
        default=None,
    )
    """Information whether current user can see the user\'s gifts."""

    interests: typing.Optional[str] = Field(
        default=None,
    )
    """Property `UsersUserFull.interests`."""

    books: typing.Optional[str] = Field(
        default=None,
    )
    """Property `UsersUserFull.books`."""

    tv: typing.Optional[str] = Field(
        default=None,
    )
    """Property `UsersUserFull.tv`."""

    quotes: typing.Optional[str] = Field(
        default=None,
    )
    """Property `UsersUserFull.quotes`."""

    about: typing.Optional[str] = Field(
        default=None,
    )
    """Property `UsersUserFull.about`."""

    games: typing.Optional[str] = Field(
        default=None,
    )
    """Property `UsersUserFull.games`."""

    movies: typing.Optional[str] = Field(
        default=None,
    )
    """Property `UsersUserFull.movies`."""

    activities: typing.Optional[str] = Field(
        default=None,
    )
    """Property `UsersUserFull.activities`."""

    music: typing.Optional[str] = Field(
        default=None,
    )
    """Property `UsersUserFull.music`."""

    can_write_private_message: typing.Optional[bool] = Field(
        default=None,
    )
    """Information whether current user can write private message."""

    can_send_friend_request: typing.Optional[bool] = Field(
        default=None,
    )
    """Information whether current user can send a friend request."""

    can_be_invited_group: typing.Optional[bool] = Field(
        default=None,
    )
    """Information whether current user can be invited to the community."""

    mobile_phone: typing.Optional[str] = Field(
        default=None,
    )
    """User\'s mobile phone number."""

    home_phone: typing.Optional[str] = Field(
        default=None,
    )
    """User\'s additional phone number."""

    site: typing.Optional[str] = Field(
        default=None,
    )
    """User\'s website."""

    status_audio: typing.Optional["AudioAudio"] = Field(
        default=None,
    )
    """Property `UsersUserFull.status_audio`."""

    status: typing.Optional[str] = Field(
        default=None,
    )
    """User\'s status."""

    activity: typing.Optional[str] = Field(
        default=None,
    )
    """User\'s status."""

    status_app: typing.Optional["AppsAppMin"] = Field(
        default=None,
    )
    """Property `UsersUserFull.status_app`."""

    last_seen: typing.Optional["UsersLastSeen"] = Field(
        default=None,
    )
    """Property `UsersUserFull.last_seen`."""

    exports: typing.Optional["UsersExports"] = Field(
        default=None,
    )
    """Property `UsersUserFull.exports`."""

    crop_photo: typing.Optional["BaseCropPhoto"] = Field(
        default=None,
    )
    """Property `UsersUserFull.crop_photo`."""

    followers_count: typing.Optional[int] = Field(
        default=None,
    )
    """Number of user\'s followers and friends."""

    video_live_level: typing.Optional[int] = Field(
        default=None,
    )
    """User level in live streams achievements."""

    video_live_count: typing.Optional[int] = Field(
        default=None,
    )
    """Number of user\'s live streams."""

    clips_count: typing.Optional[int] = Field(
        default=None,
    )
    """Number of user\'s clips."""

    blacklisted: typing.Optional[bool] = Field(
        default=None,
    )
    """Information whether current user is in the requested user\'s blacklist.."""

    blacklisted_by_me: typing.Optional[bool] = Field(
        default=None,
    )
    """Information whether the requested user is in current user\'s blacklist."""

    is_favorite: typing.Optional[bool] = Field(
        default=None,
    )
    """Information whether the requested user is in faves of current user."""

    is_hidden_from_feed: typing.Optional[bool] = Field(
        default=None,
    )
    """Information whether the requested user is hidden from current user\'s newsfeed."""

    common_count: typing.Optional[int] = Field(
        default=None,
    )
    """Number of common friends with current user."""

    occupation: typing.Optional["UsersOccupation"] = Field(
        default=None,
    )
    """Property `UsersUserFull.occupation`."""

    career: typing.Optional[typing.List["UsersCareer"]] = Field(
        default=None,
    )
    """Property `UsersUserFull.career`."""

    military: typing.Optional[typing.List["UsersMilitary"]] = Field(
        default=None,
    )
    """Property `UsersUserFull.military`."""

    university: typing.Optional[int] = Field(
        default=None,
    )
    """University ID."""

    university_name: typing.Optional[str] = Field(
        default=None,
    )
    """University name."""

    university_group_id: typing.Optional[int] = Field(
        default=None,
    )
    """Property `UsersUserFull.university_group_id`."""

    faculty: typing.Optional[int] = Field(
        default=None,
    )
    """Faculty ID."""

    faculty_name: typing.Optional[str] = Field(
        default=None,
    )
    """Faculty name."""

    graduation: typing.Optional[int] = Field(
        default=None,
    )
    """Graduation year."""

    education_form: typing.Optional[str] = Field(
        default=None,
    )
    """Education form."""

    education_status: typing.Optional[str] = Field(
        default=None,
    )
    """User\'s education status."""

    home_town: typing.Optional[str] = Field(
        default=None,
    )
    """User hometown."""

    relation: typing.Optional["UsersUserRelation"] = Field(
        default=None,
    )
    """User relationship status."""

    relation_partner: typing.Optional["UsersUserMin"] = Field(
        default=None,
    )
    """Property `UsersUserFull.relation_partner`."""

    personal: typing.Optional["UsersPersonal"] = Field(
        default=None,
    )
    """Property `UsersUserFull.personal`."""

    universities: typing.Optional[typing.List["UsersUniversity"]] = Field(
        default=None,
    )
    """Property `UsersUserFull.universities`."""

    schools: typing.Optional[typing.List["UsersSchool"]] = Field(
        default=None,
    )
    """Property `UsersUserFull.schools`."""

    relatives: typing.Optional[typing.List["UsersRelative"]] = Field(
        default=None,
    )
    """Property `UsersUserFull.relatives`."""

    is_subscribed_podcasts: typing.Optional[bool] = Field(
        default=None,
    )
    """Information whether current user is subscribed to podcasts."""

    can_subscribe_podcasts: typing.Optional[bool] = Field(
        default=None,
    )
    """Owner in whitelist or not."""

    can_subscribe_posts: typing.Optional[bool] = Field(
        default=None,
    )
    """Can subscribe to wall."""

    counters: typing.Optional["UsersUserCounters"] = Field(
        default=None,
    )
    """Property `UsersUserFull.counters`."""

    access_key: typing.Optional[str] = Field(
        default=None,
    )
    """Property `UsersUserFull.access_key`."""

    can_upload_doc: typing.Optional[bool] = Field(
        default=None,
    )
    """Property `UsersUserFull.can_upload_doc`."""

    can_ban: typing.Optional[bool] = Field(
        default=None,
    )
    """Information whether the user can be baned (added to black list) by me."""

    hash: typing.Optional[str] = Field(
        default=None,
    )
    """Property `UsersUserFull.hash`."""

    is_no_index: typing.Optional[bool] = Field(
        default=None,
    )
    """Access to user profile is restricted for search engines."""

    contact_id: typing.Optional[int] = Field(
        default=None,
    )
    """Contact person ID."""

    is_message_request: typing.Optional[bool] = Field(
        default=None,
    )
    """Property `UsersUserFull.is_message_request`."""

    descriptions: typing.Optional[typing.List[str]] = Field(
        default=None,
    )
    """Property `UsersUserFull.descriptions`."""

    lists: typing.Optional[typing.List[int]] = Field(
        default=None,
    )
    """Property `UsersUserFull.lists`."""


class UsersUserXtrType(UsersUserFull):
    """
    Model: `UsersUserXtrType`
    """

    type: typing.Optional["UsersUserType"] = Field(
        default=None,
    )
    """Property `UsersUserXtrType.type`."""


class MessagesUserXtrInvitedBy(UsersUserXtrType):
    """
    Model: `MessagesUserXtrInvitedBy`
    """

    invited_by: typing.Optional[int] = Field(
        default=None,
    )
    """ID of the inviter."""

    name: typing.Optional[str] = Field(
        default=None,
    )
    """Name of group."""

    type: typing.Optional["MessagesUserTypeForXtrInvitedBy"] = Field(
        default=None,
    )
    """Property `MessagesUserXtrInvitedBy.type`."""


class MessagesGetConversationByIdExtended(MessagesGetConversationById):
    """
    Model: `MessagesGetConversationByIdExtended`
    """

    profiles: typing.Optional[typing.List["UsersUserFull"]] = Field(
        default=None,
    )
    """Property `MessagesGetConversationByIdExtended.profiles`."""

    groups: typing.Optional[typing.List["GroupsGroupFull"]] = Field(
        default=None,
    )
    """Property `MessagesGetConversationByIdExtended.groups`."""


class MessagesMessage(MessagesBaseMessage):
    """
    Model: `MessagesMessage`
    """

    important: typing.Optional[bool] = Field(
        default=None,
    )
    """Is it an important message."""

    is_hidden: typing.Optional[bool] = Field(
        default=None,
    )
    """Property `MessagesMessage.is_hidden`."""

    members_count: typing.Optional[int] = Field(
        default=None,
    )
    """Members number."""

    reply_message: typing.Optional["MessagesForeignMessage"] = Field(
        default=None,
    )
    """Property `MessagesMessage.reply_message`."""

    reaction_id: typing.Optional[int] = Field(
        default=None,
    )
    """Reaction id set on message."""

    reactions: typing.Optional[typing.List["MessagesReactionCounterResponseItem"]] = Field(
        default=None,
    )
    """Actual reactions counters on this message."""

    last_reaction_id: typing.Optional[int] = Field(
        default=None,
    )
    """Last reaction id set on this message."""

    is_pinned: typing.Optional[bool] = Field(
        default=None,
    )
    """Is message pinned in its conversation."""

    was_listened: typing.Optional[bool] = Field(
        default=None,
    )
    """Was the audio message inside already listened by you."""

    pinned_at: typing.Optional[int] = Field(
        default=None,
    )
    """Date when the message has been pinned in Unixtime."""


class AccountUserSettings(UsersUserMin, UsersUserSettingsXtr):
    """
    Model: `AccountUserSettings`
    """

    photo_200: typing.Optional[str] = Field(
        default=None,
    )
    """URL of square photo of the user with 200 pixels in width."""

    is_service_account: typing.Optional[bool] = Field(
        default=None,
    )
    """flag about service account."""


class AdsStatsAge(AdsDemographicStatsPeriodItemBase):
    """
    Model: `AdsStatsAge`
    """

    value: typing.Optional[str] = Field(
        default=None,
    )
    """Age interval."""


class AdsStatsCities(AdsDemographicStatsPeriodItemBase):
    """
    Model: `AdsStatsCities`
    """

    name: typing.Optional[str] = Field(
        default=None,
    )
    """City name."""

    value: typing.Optional[typing.Union["int", "str"]] = Field(
        default=None,
    )
    """City ID."""


class AdsStatsSex(AdsDemographicStatsPeriodItemBase):
    """
    Model: `AdsStatsSex`
    """

    value: typing.Optional["AdsStatsSexValue"] = Field(
        default=None,
    )
    """Property `AdsStatsSex.value`."""


class AdsStatsSexAge(AdsDemographicStatsPeriodItemBase):
    """
    Model: `AdsStatsSexAge`
    """

    value: typing.Optional[str] = Field(
        default=None,
    )
    """Sex and age interval."""


class AdsTargSettings(AdsCriteria):
    """
    Model: `AdsTargSettings`
    """

    id: typing.Optional[str] = Field(
        default=None,
    )
    """Ad ID."""

    campaign_id: typing.Optional[str] = Field(
        default=None,
    )
    """Campaign ID."""


class AppsApp(AppsAppMin):
    """
    Model: `AppsApp`
    """

    author_url: typing.Optional[str] = Field(
        default=None,
    )
    """Application author\'s URL."""

    banner_1120: typing.Optional[str] = Field(
        default=None,
    )
    """URL of the app banner with 1120 px in width."""

    banner_560: typing.Optional[str] = Field(
        default=None,
    )
    """URL of the app banner with 560 px in width."""

    icon_16: typing.Optional[str] = Field(
        default=None,
    )
    """URL of the app icon with 16 px in width."""

    is_new: typing.Optional[bool] = Field(
        default=None,
    )
    """Is new flag."""

    push_enabled: typing.Optional[bool] = Field(
        default=None,
    )
    """Is push enabled."""

    friends: typing.Optional[typing.List[int]] = Field(
        default=None,
    )
    """Property `AppsApp.friends`."""

    catalog_position: typing.Optional[int] = Field(
        default=None,
    )
    """Catalog position."""

    description: typing.Optional[str] = Field(
        default=None,
    )
    """Application description."""

    genre: typing.Optional[str] = Field(
        default=None,
    )
    """Genre name."""

    genre_id: typing.Optional[int] = Field(
        default=None,
    )
    """Genre ID."""

    international: typing.Optional[bool] = Field(
        default=None,
    )
    """Information whether the application is multilanguage."""

    is_in_catalog: typing.Optional[int] = Field(
        default=None,
    )
    """Information whether application is in mobile catalog."""

    leaderboard_type: typing.Optional["AppsAppLeaderboardType"] = Field(
        default=None,
    )
    """Property `AppsApp.leaderboard_type`."""

    members_count: typing.Optional[int] = Field(
        default=None,
    )
    """Members number."""

    platform_id: typing.Optional[str] = Field(
        default=None,
    )
    """Application ID in store."""

    published_date: typing.Optional[int] = Field(
        default=None,
    )
    """Date when the application has been published in Unixtime."""

    screen_name: typing.Optional[str] = Field(
        default=None,
    )
    """Screen name."""

    section: typing.Optional[str] = Field(
        default=None,
    )
    """Application section name."""


class CallbackForeignMessage(MessagesForeignMessage):
    """
    Model: `CallbackForeignMessage`
    """

    is_cropped: typing.Optional[bool] = Field(
        default=None,
    )
    """Property `CallbackForeignMessage.is_cropped`."""

    fwd_messages: typing.Optional[typing.List["CallbackForeignMessage"]] = Field(
        default=None,
    )
    """Property `CallbackForeignMessage.fwd_messages`."""

    reply_message: typing.Optional["CallbackForeignMessage"] = Field(
        default=None,
    )
    """Property `CallbackForeignMessage.reply_message`."""


class CallbackMessage(MessagesMessage):
    """
    Model: `CallbackMessage`
    """

    influence_score: typing.Optional[float] = Field(
        default=None,
    )
    """Property `CallbackMessage.influence_score`."""

    reply_message: typing.Optional["CallbackForeignMessage"] = Field(
        default=None,
    )
    """Property `CallbackMessage.reply_message`."""

    fwd_messages: typing.Optional["CallbackFwdMessages"] = Field(
        default=None,
    )
    """Property `CallbackMessage.fwd_messages`."""


class CallbackPhotoComment(WallWallComment):
    """
    Model: `CallbackPhotoComment`
    """

    photo_owner_id: int = Field()
    """Property `CallbackPhotoComment.photo_owner_id`."""


class CallbackVideoComment(WallWallComment):
    """
    Model: `CallbackVideoComment`
    """

    video_owner_id: typing.Optional[int] = Field(
        default=None,
    )
    """Property `CallbackVideoComment.video_owner_id`."""


class CallbackConfirmation(CallbackBase):
    """
    Model: `CallbackConfirmation`
    """

    type: typing.Optional[str] = Field(
        default=None,
    )
    """Property `CallbackConfirmation.type`."""


class DatabaseCity(BaseObject):
    """
    Model: `DatabaseCity`
    """

    area: typing.Optional[str] = Field(
        default=None,
    )
    """Area title."""

    region: typing.Optional[str] = Field(
        default=None,
    )
    """Region title."""

    important: typing.Optional[bool] = Field(
        default=None,
    )
    """Information whether the city is included in important cities list."""


class GroupsUserXtrRole(UsersUserFull):
    """
    Model: `GroupsUserXtrRole`
    """

    permissions: typing.Optional[typing.List["GroupsMemberRolePermission"]] = Field(
        default=None,
    )
    """Property `GroupsUserXtrRole.permissions`."""

    role: typing.Optional["GroupsRoleOptions"] = Field(
        default=None,
    )
    """Property `GroupsUserXtrRole.role`."""


class GroupsGroupFull(GroupsGroup, GroupsMarketProperties):
    """
    Model: `GroupsGroupFull`
    """

    member_status: typing.Optional["GroupsGroupFullMemberStatus"] = Field(
        default=None,
    )
    """Current user\'s member status."""

    is_adult: typing.Optional[bool] = Field(
        default=None,
    )
    """Information whether community is adult."""

    is_hidden_from_feed: typing.Optional[bool] = Field(
        default=None,
    )
    """Information whether community is hidden from current user\'s newsfeed."""

    is_favorite: typing.Optional[bool] = Field(
        default=None,
    )
    """Information whether community is in faves."""

    is_subscribed: typing.Optional[bool] = Field(
        default=None,
    )
    """Information whether current user is subscribed."""

    city: typing.Optional["BaseObject"] = Field(
        default=None,
    )
    """Property `GroupsGroupFull.city`."""

    description: typing.Optional[str] = Field(
        default=None,
    )
    """Community description."""

    wiki_page: typing.Optional[str] = Field(
        default=None,
    )
    """Community\'s main wiki page title."""

    members_count: typing.Optional[int] = Field(
        default=None,
    )
    """Community members number."""

    members_count_text: typing.Optional[str] = Field(
        default=None,
    )
    """Info about number of users in group."""

    requests_count: typing.Optional[int] = Field(
        default=None,
    )
    """The number of incoming requests to the community."""

    video_live_level: typing.Optional[int] = Field(
        default=None,
    )
    """Community level live streams achievements."""

    video_live_count: typing.Optional[int] = Field(
        default=None,
    )
    """Number of community\'s live streams."""

    clips_count: typing.Optional[int] = Field(
        default=None,
    )
    """Number of community\'s clips."""

    counters: typing.Optional["GroupsCountersGroup"] = Field(
        default=None,
    )
    """Property `GroupsGroupFull.counters`."""

    textlives_count: typing.Optional[int] = Field(
        default=None,
    )
    """Textlives number."""

    cover: typing.Optional["BaseOwnerCover"] = Field(
        default=None,
    )
    """Property `GroupsGroupFull.cover`."""

    video_cover: typing.Optional["BaseOwnerCover"] = Field(
        default=None,
    )
    """Property `GroupsGroupFull.video_cover`."""

    can_post: typing.Optional[bool] = Field(
        default=None,
    )
    """Information whether current user can post on community\'s wall."""

    can_suggest: typing.Optional[bool] = Field(
        default=None,
    )
    """Property `GroupsGroupFull.can_suggest`."""

    can_upload_story: typing.Optional[bool] = Field(
        default=None,
    )
    """Information whether current user can upload story."""

    can_call_to_community: typing.Optional[bool] = Field(
        default=None,
    )
    """Information whether current user can call to community."""

    can_upload_doc: typing.Optional[bool] = Field(
        default=None,
    )
    """Information whether current user can upload doc."""

    can_upload_video: typing.Optional[bool] = Field(
        default=None,
    )
    """Information whether current user can upload video."""

    can_upload_clip: typing.Optional[bool] = Field(
        default=None,
    )
    """Information whether current user can upload clip."""

    can_see_all_posts: typing.Optional[bool] = Field(
        default=None,
    )
    """Information whether current user can see all posts on community\'s wall."""

    can_create_topic: typing.Optional[bool] = Field(
        default=None,
    )
    """Information whether current user can create topic."""

    activity: typing.Optional[str] = Field(
        default=None,
    )
    """Type of group, start date of event or category of public page."""

    fixed_post: typing.Optional[int] = Field(
        default=None,
    )
    """Fixed post ID."""

    has_photo: typing.Optional[bool] = Field(
        default=None,
    )
    """Information whether community has photo."""

    crop_photo: typing.Optional["BaseCropPhoto"] = Field(
        default=None,
    )
    """Данные о точках, по которым вырезаны профильная и миниатюрная фотографии сообщества."""

    status: typing.Optional[str] = Field(
        default=None,
    )
    """Community status."""

    status_audio: typing.Optional["AudioAudio"] = Field(
        default=None,
    )
    """Property `GroupsGroupFull.status_audio`."""

    main_album_id: typing.Optional[int] = Field(
        default=None,
    )
    """Community\'s main photo album ID."""

    links: typing.Optional[typing.List["GroupsLinksItem"]] = Field(
        default=None,
    )
    """Property `GroupsGroupFull.links`."""

    contacts: typing.Optional[typing.List["GroupsContactsItem"]] = Field(
        default=None,
    )
    """Property `GroupsGroupFull.contacts`."""

    wall: typing.Optional[int] = Field(
        default=None,
    )
    """Information about wall status in community."""

    site: typing.Optional[str] = Field(
        default=None,
    )
    """Community\'s website."""

    main_section: typing.Optional["GroupsGroupFullSection"] = Field(
        default=None,
    )
    """Property `GroupsGroupFull.main_section`."""

    secondary_section: typing.Optional["GroupsGroupFullSection"] = Field(
        default=None,
    )
    """Property `GroupsGroupFull.secondary_section`."""

    trending: typing.Optional[bool] = Field(
        default=None,
    )
    """Information whether the community has a \"fire\" pictogram.."""

    can_message: typing.Optional[bool] = Field(
        default=None,
    )
    """Information whether current user can send a message to community."""

    is_messages_blocked: typing.Optional[bool] = Field(
        default=None,
    )
    """Information whether community can send a message to current user."""

    can_send_notify: typing.Optional[bool] = Field(
        default=None,
    )
    """Information whether community can send notifications by phone number to current user."""

    online_status: typing.Optional["GroupsOnlineStatus"] = Field(
        default=None,
    )
    """Status of replies in community messages."""

    invited_by: typing.Optional[int] = Field(
        default=None,
    )
    """Inviter ID."""

    age_limits: typing.Optional["GroupsGroupFullAgeLimits"] = Field(
        default=None,
    )
    """Information whether age limit."""

    ban_info: typing.Optional["GroupsGroupBanInfo"] = Field(
        default=None,
    )
    """User ban info."""

    has_group_channel: typing.Optional[bool] = Field(
        default=None,
    )
    """Property `GroupsGroupFull.has_group_channel`."""

    addresses: typing.Optional["GroupsAddressesInfo"] = Field(
        default=None,
    )
    """Info about addresses in groups."""

    is_subscribed_podcasts: typing.Optional[bool] = Field(
        default=None,
    )
    """Information whether current user is subscribed to podcasts."""

    can_subscribe_podcasts: typing.Optional[bool] = Field(
        default=None,
    )
    """Owner in whitelist or not."""

    can_subscribe_posts: typing.Optional[bool] = Field(
        default=None,
    )
    """Can subscribe to wall."""

    live_covers: typing.Optional["GroupsLiveCovers"] = Field(
        default=None,
    )
    """Live covers state."""

    stories_archive_count: typing.Optional[int] = Field(
        default=None,
    )
    """Property `GroupsGroupFull.stories_archive_count`."""

    has_unseen_stories: typing.Optional[bool] = Field(
        default=None,
    )
    """Property `GroupsGroupFull.has_unseen_stories`."""

    video_notifications_status: typing.Optional[str] = Field(
        default=None,
    )
    """Information about the status of video notifications for the current user.."""

    videos_count: typing.Optional[int] = Field(
        default=None,
    )
    """Community videos number."""


class MarketMarketItemBasicWithGroup(MarketMarketItemBasic):
    """
    Model: `MarketMarketItemBasicWithGroup`
    """

    is_group_verified: typing.Optional[bool] = Field(
        default=None,
    )
    """Property `MarketMarketItemBasicWithGroup.is_group_verified`."""

    group_name: typing.Optional[str] = Field(
        default=None,
    )
    """Property `MarketMarketItemBasicWithGroup.group_name`."""

    group_link: typing.Optional[str] = Field(
        default=None,
    )
    """Property `MarketMarketItemBasicWithGroup.group_link`."""

    is_owner: typing.Optional[bool] = Field(
        default=None,
    )
    """Property `MarketMarketItemBasicWithGroup.is_owner`."""

    is_adult: typing.Optional[bool] = Field(
        default=None,
    )
    """Property `MarketMarketItemBasicWithGroup.is_adult`."""


class MarketMarketItemFull(MarketMarketItem):
    """
    Model: `MarketMarketItemFull`
    """

    albums_ids: typing.Optional[typing.List[int]] = Field(
        default=None,
    )
    """Property `MarketMarketItemFull.albums_ids`."""

    photos: typing.Optional[typing.List["PhotosPhoto"]] = Field(
        default=None,
    )
    """Property `MarketMarketItemFull.photos`."""

    can_comment: typing.Optional[bool] = Field(
        default=None,
    )
    """Information whether current use can comment the item."""

    show_comments: typing.Optional[bool] = Field(
        default=None,
    )
    """Information about whether to show the comments tab."""

    can_repost: typing.Optional[bool] = Field(
        default=None,
    )
    """Information whether current use can repost the item."""

    likes: typing.Optional["BaseLikes"] = Field(
        default=None,
    )
    """Property `MarketMarketItemFull.likes`."""

    reposts: typing.Optional["BaseRepostsInfo"] = Field(
        default=None,
    )
    """Property `MarketMarketItemFull.reposts`."""

    views_count: typing.Optional[int] = Field(
        default=None,
    )
    """Views number."""

    wishlist_item_id: typing.Optional[int] = Field(
        default=None,
    )
    """Object identifier in wishlist of viewer."""

    rating: typing.Optional[float] = Field(
        default=None,
    )
    """Rating of product."""

    orders_count: typing.Optional[int] = Field(
        default=None,
    )
    """Count of product orders."""

    cancel_info: typing.Optional["BaseLink"] = Field(
        default=None,
    )
    """Information for cancel and revert order."""

    user_agreement_info: typing.Optional[str] = Field(
        default=None,
    )
    """User agreement info."""

    ad_id: typing.Optional[int] = Field(
        default=None,
    )
    """Contains ad ID if it has."""

    owner_info: typing.Optional["MarketItemOwnerInfo"] = Field(
        default=None,
    )
    """Information about the group where the item is placed."""

    can_edit: typing.Optional[bool] = Field(
        default=None,
    )
    """Can the item be updated by current user?."""

    can_delete: typing.Optional[bool] = Field(
        default=None,
    )
    """Can item be deleted by current user?."""

    can_recover: typing.Optional[bool] = Field(
        default=None,
    )
    """Can item be restored by current user?."""

    can_show_convert_to_service: typing.Optional[bool] = Field(
        default=None,
    )
    """Can the item be converted from a product into a service?."""

    promotion: typing.Optional["MarketItemPromotionInfo"] = Field(
        default=None,
    )
    """Information about promotion of the item."""

    vk_pay_discount: typing.Optional[int] = Field(
        default=None,
    )
    """The amount of the discount if VK Pay is used for payment."""


class PollsPollExtended(PollsPoll):
    """
    Model: `PollsPollExtended`
    """

    profiles: typing.Optional[typing.List["UsersUserFull"]] = Field(
        default=None,
    )
    """Property `PollsPollExtended.profiles`."""


class FriendsRequestsXtrMutual(UsersUserFull):
    """
    Model: `FriendsRequestsXtrMutual`
    """

    user_id: int = Field()
    """User ID."""

    id: typing.Optional[int] = Field(
        default=None,
    )
    """User ID."""

    from_: typing.Optional[str] = Field(
        default=None,
        alias="from",
    )
    """ID of the user by whom friend has been suggested."""

    mutual: typing.Optional["FriendsRequestsMutual"] = Field(
        default=None,
    )
    """Property `FriendsRequestsXtrMutual.mutual`."""

    track_code: typing.Optional[str] = Field(
        default=None,
    )
    """Property `FriendsRequestsXtrMutual.track_code`."""

    message: typing.Optional[str] = Field(
        default=None,
    )
    """Message sent with a request."""

    timestamp: typing.Optional[int] = Field(
        default=None,
    )
    """Request timestamp."""

    descriptions: typing.Optional[typing.List[str]] = Field(
        default=None,
    )
    """Property `FriendsRequestsXtrMutual.descriptions`."""


class FriendsFriendExtendedStatus(FriendsFriendStatus):
    """
    Model: `FriendsFriendExtendedStatus`
    """

    is_request_unread: typing.Optional[bool] = Field(
        default=None,
    )
    """Is friend request from other user unread."""


class FriendsRequestsXtrMessage(FriendsRequestsXtrMutual):
    """
    Model: `FriendsRequestsXtrMessage`
    """

    message: typing.Optional[str] = Field(
        default=None,
    )
    """Message sent with a request."""


class VideoVideoImage(BaseImage):
    """
    Model: `VideoVideoImage`
    """

    with_padding: typing.Optional["BasePropertyExists"] = Field(
        default=None,
    )
    """Property `VideoVideoImage.with_padding`."""

    size: typing.Optional[str] = Field(
        default=None,
    )
    """Property `VideoVideoImage.size`."""


class VideoVideoAlbumFull(VideoVideoAlbum):
    """
    Model: `VideoVideoAlbumFull`
    """

    count: int = Field()
    """Total number of videos in album."""

    updated_time: int = Field()
    """Date when the album has been updated last time in Unixtime."""

    image: typing.Optional[typing.List["VideoVideoImage"]] = Field(
        default=None,
    )
    """Album cover image in different sizes."""

    image_blur: typing.Optional["BasePropertyExists"] = Field(
        default=None,
    )
    """Need blur album thumb or not."""

    is_system: typing.Optional["BasePropertyExists"] = Field(
        default=None,
    )
    """Information whether album is system."""

    can_edit: typing.Optional[bool] = Field(
        default=None,
    )
    """Is user can edit playlist."""

    can_delete: typing.Optional[bool] = Field(
        default=None,
    )
    """Is user can delete playlist."""

    can_upload: typing.Optional[bool] = Field(
        default=None,
    )
    """Is user can upload video to playlist."""


class VideoVideoFull(VideoVideo):
    """
    Model: `VideoVideoFull`
    """

    files: typing.Optional["VideoVideoFiles"] = Field(
        default=None,
    )
    """Property `VideoVideoFull.files`."""

    trailer: typing.Optional["VideoVideoFiles"] = Field(
        default=None,
    )
    """Property `VideoVideoFull.trailer`."""

    episodes: typing.Optional[typing.List["VideoEpisode"]] = Field(
        default=None,
    )
    """List of video episodes with timecodes."""

    live_settings: typing.Optional["VideoLiveSettings"] = Field(
        default=None,
    )
    """Settings for live stream."""


class WallWallpostFull(WallCarouselBase, WallWallpost):
    """
    Model: `WallWallpostFull`
    """

    copy_history: typing.Optional[typing.List["WallWallpostFull"]] = Field(
        default=None,
    )
    """Property `WallWallpostFull.copy_history`."""

    can_edit: typing.Optional[bool] = Field(
        default=None,
    )
    """Information whether current user can edit the post."""

    created_by: typing.Optional[int] = Field(
        default=None,
    )
    """Post creator ID (if post still can be edited)."""

    can_delete: typing.Optional[bool] = Field(
        default=None,
    )
    """Information whether current user can delete the post."""

    can_pin: typing.Optional[bool] = Field(
        default=None,
    )
    """Information whether current user can pin the post."""

    donut: typing.Optional["WallWallpostDonut"] = Field(
        default=None,
    )
    """Property `WallWallpostFull.donut`."""

    is_pinned: typing.Optional[bool] = Field(
        default=None,
    )
    """Information whether the post is pinned."""

    comments: typing.Optional["BaseCommentsInfo"] = Field(
        default=None,
    )
    """Property `WallWallpostFull.comments`."""

    marked_as_ads: typing.Optional[bool] = Field(
        default=None,
    )
    """Information whether the post is marked as ads."""

    topic_id: typing.Optional[int] = Field(
        default=None,
    )
    """Topic ID. Allowed values can be obtained from newsfeed.getPostTopics method."""

    short_text_rate: typing.Optional[float] = Field(
        default=None,
    )
    """Preview length control parameter."""

    hash: typing.Optional[str] = Field(
        default=None,
    )
    """Hash for sharing."""

    type: typing.Optional["WallPostType"] = Field(
        default=None,
    )
    """Property `WallWallpostFull.type`."""

    feedback: typing.Optional["NewsfeedItemWallpostFeedback"] = Field(
        default=None,
    )
    """Property `WallWallpostFull.feedback`."""

    to_id: typing.Optional[int] = Field(
        default=None,
    )
    """Property `WallWallpostFull.to_id`."""


class NewsfeedCommentsBase(BaseCommentsInfo):
    """
    Model: `NewsfeedCommentsBase`
    """

    list: typing.Optional[typing.List["WallWallComment"]] = Field(
        default=None,
    )
    """Property `NewsfeedCommentsBase.list`."""


class NewsfeedCommentsItemTypeMarket(MarketMarketItem, NewsfeedCommentsItemBase):
    """
    Model: `NewsfeedCommentsItemTypeMarket`
    """

    comments: typing.Optional["NewsfeedCommentsBase"] = Field(
        default=None,
    )
    """Property `NewsfeedCommentsItemTypeMarket.comments`."""

    likes: typing.Optional["BaseLikes"] = Field(
        default=None,
    )
    """Property `NewsfeedCommentsItemTypeMarket.likes`."""


class NewsfeedCommentsItemTypeNotes(NewsfeedCommentsItemBase):
    """
    Model: `NewsfeedCommentsItemTypeNotes`
    """

    text: typing.Optional[str] = Field(
        default=None,
    )
    """Property `NewsfeedCommentsItemTypeNotes.text`."""

    comments: typing.Optional["NewsfeedCommentsBase"] = Field(
        default=None,
    )
    """Property `NewsfeedCommentsItemTypeNotes.comments`."""

    likes: typing.Optional["BaseLikes"] = Field(
        default=None,
    )
    """Property `NewsfeedCommentsItemTypeNotes.likes`."""


class NewsfeedCommentsItemTypePhoto(PhotosPhoto, NewsfeedCommentsItemBase):
    """
    Model: `NewsfeedCommentsItemTypePhoto`
    """

    comments: typing.Optional["NewsfeedCommentsBase"] = Field(
        default=None,
    )
    """Property `NewsfeedCommentsItemTypePhoto.comments`."""

    likes: typing.Optional["BaseLikes"] = Field(
        default=None,
    )
    """Property `NewsfeedCommentsItemTypePhoto.likes`."""


class NewsfeedCommentsItemTypePost(WallWallpostFull, NewsfeedCommentsItemBase):
    """
    Model: `NewsfeedCommentsItemTypePost`
    """

    from_id: typing.Optional[int] = Field(
        default=None,
    )
    """Property `NewsfeedCommentsItemTypePost.from_id`."""

    comments: typing.Optional["NewsfeedCommentsBase"] = Field(
        default=None,
    )
    """Property `NewsfeedCommentsItemTypePost.comments`."""


class NewsfeedCommentsItemTypeTopic(NewsfeedCommentsItemBase):
    """
    Model: `NewsfeedCommentsItemTypeTopic`
    """

    text: typing.Optional[str] = Field(
        default=None,
    )
    """Property `NewsfeedCommentsItemTypeTopic.text`."""

    comments: typing.Optional["NewsfeedCommentsBase"] = Field(
        default=None,
    )
    """Property `NewsfeedCommentsItemTypeTopic.comments`."""

    likes: typing.Optional["BaseLikes"] = Field(
        default=None,
    )
    """Property `NewsfeedCommentsItemTypeTopic.likes`."""


class NewsfeedCommentsItemTypeVideo(VideoVideo, NewsfeedCommentsItemBase):
    """
    Model: `NewsfeedCommentsItemTypeVideo`
    """

    text: typing.Optional[str] = Field(
        default=None,
    )
    """Property `NewsfeedCommentsItemTypeVideo.text`."""

    comments: typing.Optional["NewsfeedCommentsBase"] = Field(
        default=None,
    )
    """Property `NewsfeedCommentsItemTypeVideo.comments`."""

    likes: typing.Optional["BaseLikes"] = Field(
        default=None,
    )
    """Property `NewsfeedCommentsItemTypeVideo.likes`."""

    type: typing.Optional[str] = Field(
        default=None,
    )
    """Property `NewsfeedCommentsItemTypeVideo.type`."""


class NewsfeedItemAudio(NewsfeedItemBase):
    """
    Model: `NewsfeedItemAudio`
    """

    audio: typing.Optional["NewsfeedItemAudioAudio"] = Field(
        default=None,
    )
    """Property `NewsfeedItemAudio.audio`."""

    post_id: typing.Optional[int] = Field(
        default=None,
    )
    """Post ID."""


class NewsfeedItemDigest(NewsfeedItemBase):
    """
    Model: `NewsfeedItemDigest`
    """

    feed_id: typing.Optional[str] = Field(
        default=None,
    )
    """id of feed in digest."""

    items: typing.Optional[typing.List["NewsfeedItemDigestItem"]] = Field(
        default=None,
    )
    """Property `NewsfeedItemDigest.items`."""

    main_post_ids: typing.Optional[typing.List[str]] = Field(
        default=None,
    )
    """Property `NewsfeedItemDigest.main_post_ids`."""

    template: typing.Optional[str] = Field(
        default=None,
    )
    """type of digest."""

    header: typing.Optional["NewsfeedItemDigestHeader"] = Field(
        default=None,
    )
    """Property `NewsfeedItemDigest.header`."""

    footer: typing.Optional["NewsfeedItemDigestFooter"] = Field(
        default=None,
    )
    """Property `NewsfeedItemDigest.footer`."""


class NewsfeedItemDigestFullItem(NewsfeedItemBase):
    """
    Model: `NewsfeedItemDigestFullItem`
    """

    inner_type: str = Field()
    """Property `NewsfeedItemDigestFullItem.inner_type`."""

    post: "NewsfeedItemWallpost" = Field()
    """Property `NewsfeedItemDigestFullItem.post`."""

    text: typing.Optional[str] = Field(
        default=None,
    )
    """Property `NewsfeedItemDigestFullItem.text`."""

    source_name: typing.Optional[str] = Field(
        default=None,
    )
    """Property `NewsfeedItemDigestFullItem.source_name`."""

    attachment_index: typing.Optional[int] = Field(
        default=None,
    )
    """Property `NewsfeedItemDigestFullItem.attachment_index`."""

    attachment: typing.Optional["WallWallpostAttachment"] = Field(
        default=None,
    )
    """Property `NewsfeedItemDigestFullItem.attachment`."""

    style: typing.Optional[str] = Field(
        default=None,
    )
    """Property `NewsfeedItemDigestFullItem.style`."""

    badge_text: typing.Optional[str] = Field(
        default=None,
    )
    """Optional red badge for posts in digest block."""


class NewsfeedItemFriend(NewsfeedItemBase):
    """
    Model: `NewsfeedItemFriend`
    """

    friends: typing.Optional["NewsfeedItemFriendFriends"] = Field(
        default=None,
    )
    """Property `NewsfeedItemFriend.friends`."""


class NewsfeedItemPhoto(WallCarouselBase, NewsfeedItemBase):
    """
    Model: `NewsfeedItemPhoto`
    """

    photos: typing.Optional["NewsfeedItemPhotoPhotos"] = Field(
        default=None,
    )
    """Property `NewsfeedItemPhoto.photos`."""

    post_id: typing.Optional[int] = Field(
        default=None,
    )
    """Post ID."""


class NewsfeedItemPhotoTag(WallCarouselBase, NewsfeedItemBase):
    """
    Model: `NewsfeedItemPhotoTag`
    """

    photo_tags: typing.Optional["NewsfeedItemPhotoTagPhotoTags"] = Field(
        default=None,
    )
    """Property `NewsfeedItemPhotoTag.photo_tags`."""

    post_id: typing.Optional[int] = Field(
        default=None,
    )
    """Post ID."""


class NewsfeedItemPromoButton(NewsfeedItemBase):
    """
    Model: `NewsfeedItemPromoButton`
    """

    text: typing.Optional[str] = Field(
        default=None,
    )
    """Property `NewsfeedItemPromoButton.text`."""

    title: typing.Optional[str] = Field(
        default=None,
    )
    """Property `NewsfeedItemPromoButton.title`."""

    action: typing.Optional["NewsfeedItemPromoButtonAction"] = Field(
        default=None,
    )
    """Property `NewsfeedItemPromoButton.action`."""

    images: typing.Optional[typing.List["NewsfeedItemPromoButtonImage"]] = Field(
        default=None,
    )
    """Property `NewsfeedItemPromoButton.images`."""


class NewsfeedItemTopic(NewsfeedItemBase):
    """
    Model: `NewsfeedItemTopic`
    """

    post_id: int = Field()
    """Topic post ID."""

    text: str = Field()
    """Post text."""

    comments: typing.Optional["BaseCommentsInfo"] = Field(
        default=None,
    )
    """Property `NewsfeedItemTopic.comments`."""

    likes: typing.Optional["BaseLikesInfo"] = Field(
        default=None,
    )
    """Property `NewsfeedItemTopic.likes`."""


class NewsfeedItemVideo(WallCarouselBase, NewsfeedItemBase):
    """
    Model: `NewsfeedItemVideo`
    """

    video: typing.Optional["NewsfeedItemVideoVideo"] = Field(
        default=None,
    )
    """Property `NewsfeedItemVideo.video`."""

    post_id: typing.Optional[int] = Field(
        default=None,
    )
    """Post ID."""


class NewsfeedItemWallpost(NewsfeedItemBase, WallWallpostFull):
    """
    Model: `NewsfeedItemWallpost`
    """


class NewsfeedListFull(NewsfeedList):
    """
    Model: `NewsfeedListFull`
    """

    no_reposts: typing.Optional[bool] = Field(
        default=None,
    )
    """Information whether reposts hiding is enabled."""

    source_ids: typing.Optional[typing.List[int]] = Field(
        default=None,
    )
    """Property `NewsfeedListFull.source_ids`."""


__all__ = (
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
    "BaseLinkApplication",
    "BaseLinkApplicationStore",
    "BaseLinkButton",
    "BaseLinkButtonAction",
    "BaseLinkButtonActionType",
    "BaseLinkButtonStyle",
    "BaseLinkNoProduct",
    "BaseLinkProduct",
    "BaseLinkProductType",
    "BaseLinkProductCategory",
    "BaseLinkProductStatus",
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
    "BaseStickerInnerType",
    "BaseStickerAnimation",
    "BaseStickerAnimationType",
    "BaseStickerNew",
    "BaseStickerNewInnerType",
    "BaseUploadServer",
    "BaseUserGroupFields",
    "BaseUserId",
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
    "UsersUserConnections",
    "UsersUserCounters",
    "UsersUserMin",
    "UsersUserRelation",
    "UsersUserSettingsXtr",
    "UsersUserType",
    "UsersUsersArray",
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
    "MessagesChatSettingsPermissionsInvite",
    "MessagesChatSettingsPermissionsChangeInfo",
    "MessagesChatSettingsPermissionsChangePin",
    "MessagesChatSettingsPermissionsUseMassMentions",
    "MessagesChatSettingsPermissionsSeeInviteLink",
    "MessagesChatSettingsPermissionsCall",
    "MessagesChatSettingsPermissionsChangeAdmins",
    "MessagesChatSettingsPhoto",
    "MessagesChatSettingsState",
    "MessagesConversation",
    "MessagesConversationSpecialServiceType",
    "MessagesConversationCanWrite",
    "MessagesConversationMember",
    "MessagesConversationPeer",
    "MessagesConversationPeerType",
    "MessagesConversationSortId",
    "MessagesConversationWithMessage",
    "MessagesDeleteFullResponseItem",
    "MessagesForeignMessage",
    "MessagesForward",
    "MessagesFwdMessages",
    "MessagesGetConversationById",
    "MessagesGetConversationMembers",
    "MessagesGetInviteLinkByOwnerResponseItem",
    "MessagesGraffiti",
    "MessagesHistoryAttachment",
    "MessagesHistoryMessageAttachment",
    "MessagesHistoryMessageAttachmentType",
    "MessagesKeyboard",
    "MessagesKeyboardButton",
    "MessagesKeyboardButtonColor",
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
    "MessagesKeyboardButtonPropertyAction",
    "MessagesLastActivity",
    "MessagesLongpollMessages",
    "MessagesLongpollParams",
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
    "AdsLookalikeRequestStatus",
    "AdsLookalikeRequestSourceType",
    "AdsLookalikeRequestSaveAudienceLevel",
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
    "AdsStatsFormat",
    "AdsStatsSexValue",
    "AdsStatsViewsTimes",
    "AdsStories",
    "AdsStoriesOwner",
    "AdsStoryItem",
    "AdsStoryItemLink",
    "AdsStoryItemStats",
    "AdsStoryItemStatsFollow",
    "AdsStoryItemStatsUrlView",
    "AdsTargStats",
    "AdsTargSuggestions",
    "AdsTargSuggestionsCities",
    "AdsTargSuggestionsRegions",
    "AdsTargSuggestionsSchools",
    "AdsTargSuggestionsSchoolsType",
    "AdsTargetGroup",
    "AdsTargetGroupTargetPixelRule",
    "AdsTargetPixelInfo",
    "AdsUpdateOfficeUsersResult",
    "AdsUpdateAdsStatus",
    "AdsUpdateClientsStatus",
    "AdsUserSpecification",
    "AdsUserSpecificationCutted",
    "AdsUsers",
    "AppWidgetsPhoto",
    "AppWidgetsPhotos",
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
    "CallbackDonutMoneyWithdraw",
    "CallbackDonutMoneyWithdrawError",
    "CallbackDonutSubscriptionCancelled",
    "CallbackDonutSubscriptionCreate",
    "CallbackDonutSubscriptionExpired",
    "CallbackDonutSubscriptionPriceChanged",
    "CallbackDonutSubscriptionProlonged",
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
    "CallbackMessageAllow",
    "CallbackMessageDeny",
    "CallbackMessageEvent",
    "CallbackMessageNew",
    "CallbackMessageObject",
    "CallbackMessageReactionEvent",
    "CallbackMessageRead",
    "CallbackMessageTypingState",
    "CallbackMessageTypingStateState",
    "CallbackPhotoCommentDelete",
    "CallbackPhotoNew",
    "CallbackPhotoNewVerticalAlign",
    "CallbackPollVoteNew",
    "CallbackType",
    "CallbackUserBlock",
    "CallbackUserUnblock",
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
    "LeadFormsAnswer",
    "LeadFormsAnswerItem",
    "LeadFormsAnswerOneOf",
    "LeadFormsForm",
    "LeadFormsLead",
    "LeadFormsQuestionItem",
    "LeadFormsQuestionItemType",
    "LeadFormsQuestionItemOption",
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
    "MarketOrder",
    "MarketOrderItem",
    "MarketOwnerType",
    "MarketPrice",
    "MarketProperty",
    "MarketPropertyType",
    "MarketPropertyVariant",
    "MarketServicesViewType",
    "MarketUploadPhotoData",
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
    "PhotosPhotoVerticalAlign",
    "PhotosPhotoAlbum",
    "PhotosPhotoAlbumFull",
    "PhotosPhotoSizes",
    "PhotosPhotoSizesType",
    "PhotosPhotoTag",
    "PhotosPhotoUpload",
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
    "StoreProductType",
    "StoreProductIcon",
    "StoreStickersKeyword",
    "StoreStickersKeywordSticker",
    "StoriesClickableArea",
    "StoriesClickableSticker",
    "StoriesClickableStickerType",
    "StoriesClickableStickerStyle",
    "StoriesClickableStickerSubtype",
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
    "FriendsFriendStatus",
    "FriendsFriendStatusStatus",
    "FriendsFriendsList",
    "FriendsMutualFriend",
    "FriendsOnlineUsers",
    "FriendsOnlineUsersWithMobile",
    "FriendsRequestsMutual",
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
    "VideoVideoResponseType",
    "VideoVideoType",
    "VideoVideoAlbum",
    "VideoVideoAlbumResponseType",
    "VideoVideoFiles",
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
    "WallWallpostInnerType",
    "WallWallpostAttachment",
    "WallWallpostAttachmentType",
    "WallWallpostCommentsDonut",
    "WallWallpostCommentsDonutPlaceholder",
    "WallWallpostDonut",
    "WallWallpostDonutEditMode",
    "WallWallpostDonutPlaceholder",
    "NewsfeedCommentsFilters",
    "NewsfeedCommentsItem",
    "NewsfeedCommentsItemBase",
    "NewsfeedIgnoreItemType",
    "NewsfeedItemAudioAudio",
    "NewsfeedItemBase",
    "NewsfeedItemDigestButton",
    "NewsfeedItemDigestButtonStyle",
    "NewsfeedItemDigestFooter",
    "NewsfeedItemDigestFooterStyle",
    "NewsfeedItemDigestHeader",
    "NewsfeedItemDigestHeaderStyle",
    "NewsfeedItemDigestItem",
    "NewsfeedItemFriendFriends",
    "NewsfeedItemHolidayRecommendationsBlockHeader",
    "NewsfeedItemPhotoPhotos",
    "NewsfeedItemPhotoTagPhotoTags",
    "NewsfeedItemPromoButtonAction",
    "NewsfeedItemPromoButtonImage",
    "NewsfeedItemVideoVideo",
    "NewsfeedItemWallpostFeedback",
    "NewsfeedItemWallpostFeedbackAnswer",
    "NewsfeedItemWallpostFeedbackType",
    "NewsfeedList",
    "NewsfeedNewsfeedItem",
    "NewsfeedNewsfeedItemType",
    "WidgetsCommentMedia",
    "WidgetsCommentMediaType",
    "WidgetsCommentReplies",
    "WidgetsCommentRepliesItem",
    "WidgetsWidgetComment",
    "WidgetsWidgetLikes",
    "WidgetsWidgetPage",
    "BaseLink",
    "UsersUser",
    "UsersUserFull",
    "UsersUserXtrType",
    "MessagesUserXtrInvitedBy",
    "MessagesGetConversationByIdExtended",
    "MessagesMessage",
    "AccountUserSettings",
    "AdsStatsAge",
    "AdsStatsCities",
    "AdsStatsSex",
    "AdsStatsSexAge",
    "AdsTargSettings",
    "AppsApp",
    "CallbackForeignMessage",
    "CallbackMessage",
    "CallbackPhotoComment",
    "CallbackVideoComment",
    "CallbackConfirmation",
    "DatabaseCity",
    "GroupsUserXtrRole",
    "GroupsGroupFull",
    "MarketMarketItemBasicWithGroup",
    "MarketMarketItemFull",
    "PollsPollExtended",
    "FriendsRequestsXtrMutual",
    "FriendsFriendExtendedStatus",
    "FriendsRequestsXtrMessage",
    "VideoVideoImage",
    "VideoVideoAlbumFull",
    "VideoVideoFull",
    "WallWallpostFull",
    "NewsfeedCommentsBase",
    "NewsfeedCommentsItemTypeMarket",
    "NewsfeedCommentsItemTypeNotes",
    "NewsfeedCommentsItemTypePhoto",
    "NewsfeedCommentsItemTypePost",
    "NewsfeedCommentsItemTypeTopic",
    "NewsfeedCommentsItemTypeVideo",
    "NewsfeedItemAudio",
    "NewsfeedItemDigest",
    "NewsfeedItemDigestFullItem",
    "NewsfeedItemFriend",
    "NewsfeedItemPhoto",
    "NewsfeedItemPhotoTag",
    "NewsfeedItemPromoButton",
    "NewsfeedItemTopic",
    "NewsfeedItemVideo",
    "NewsfeedItemWallpost",
    "NewsfeedListFull",
)
