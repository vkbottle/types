from .base_model import BaseObject
from . import link, photos, market, video
from typing import Optional, Union, Any, List
import typing
import enum


class BoolInt(enum.IntEnum):
    """ BoolInt enum """

    no = 0
    yes = 1


class City(BaseObject):
    """VK Object base/City

    id - City ID
    title - City title
    """

    id: Optional[int] = None
    title: Optional[str] = None


class CommentsInfo(BaseObject):
    """VK Object base/CommentsInfo

    can_post - Information whether current user can comment the post
    count - Comments number
    groups_can_post - Information whether groups can comment the post
    """

    can_post: Optional["BoolInt"]
    count: Optional[int] = None
    groups_can_post: Optional[bool] = None


class Country(BaseObject):
    """VK Object base/Country

    id - Country ID
    title - Country title
    """

    id: Optional[int] = None
    title: Optional[str] = None


class CropPhoto(BaseObject):
    """VK Object base/CropPhoto"""

    photo: Optional[photos.Photo] = None
    crop: Optional["CropPhotoCrop"]
    rect: Optional["CropPhotoRect"]


class CropPhotoCrop(BaseObject):
    """VK Object base/CropPhotoCrop

    x - Coordinate X of the left upper corner
    y - Coordinate Y of the left upper corner
    x2 - Coordinate X of the right lower corner
    y2 - Coordinate Y of the right lower corner
    """

    x: Optional[float] = None
    y: Optional[float] = None
    x2: Optional[float] = None
    y2: Optional[float] = None


class CropPhotoRect(BaseObject):
    """VK Object base/CropPhotoRect

    x - Coordinate X of the left upper corner
    y - Coordinate Y of the left upper corner
    x2 - Coordinate X of the right lower corner
    y2 - Coordinate Y of the right lower corner
    """

    x: Optional[float] = None
    y: Optional[float] = None
    x2: Optional[float] = None
    y2: Optional[float] = None


class Error(BaseObject):
    """VK Object base/Error

    error_code - Error code
    error_msg - Error message
    error_text - Localized error message
    """

    error_code: Optional[int] = None
    error_msg: Optional[str] = None
    error_text: Optional[str] = None
    request_params: Optional[List["RequestParam"]]


class Geo(BaseObject):
    """VK Object base/Geo

    showmap - Information whether a map is showed
    type - Place type
    """

    coordinates: Optional["GeoCoordinates"]
    place: Optional["Place"]
    showmap: Optional[int] = None
    type: Optional[str] = None


class GeoCoordinates(BaseObject):
    """VK Object base/GeoCoordinates"""

    latitude: Optional[float] = None
    longitude: Optional[float] = None


class GradientPoint(BaseObject):
    """VK Object base/GradientPoint

    color - Hex color code without #
    position - Point position
    """

    color: Optional[str] = None
    position: Optional[float] = None


class Image(BaseObject):
    """VK Object base/Image

    height - Image height
    url - Image url
    width - Image width
    """

    id: Optional[str] = None
    height: Optional[int] = None
    url: Optional[str] = None
    width: Optional[int] = None


class Likes(BaseObject):
    """VK Object base/Likes

    count - Likes number
    user_likes - Information whether current user likes the photo
    """

    count: Optional[int] = None
    user_likes: Optional["BoolInt"]


class LikesInfo(BaseObject):
    """VK Object base/LikesInfo

    can_like - Information whether current user can like the post
    can_publish - Information whether current user can repost
    count - Likes number
    user_likes - Information whether current uer has liked the post
    """

    can_like: Optional["BoolInt"]
    can_publish: Optional["BoolInt"]
    count: Optional[int] = None
    user_likes: Optional[int] = None


class Link(BaseObject):
    """VK Object base/Link

    caption - Link caption
    description - Link description
    id - Link ID
    preview_page - String ID of the page with article preview
    preview_url - URL of the page with article preview
    title - Link title
    url - Link URL
    is_external - Information whether the current link is external
    video - Video from link
    """

    application: Optional["LinkApplication"]
    button: Optional["LinkButton"]
    caption: Optional[str] = None
    description: Optional[str] = None
    id: Optional[str] = None
    is_favorite: Optional[bool] = None
    photo: Optional[photos.Photo] = None
    preview_page: Optional[str] = None
    preview_url: Optional[str] = None
    product: Optional["LinkProduct"]
    rating: Optional["LinkRating"]
    title: Optional[str] = None
    url: Optional[str] = None
    target_object: Optional[link.TargetObject] = None
    is_external: Optional[bool] = None
    video: Optional[video.Video] = None


class LinkApplication(BaseObject):
    """VK Object base/LinkApplication

    app_id - Application Id
    """

    app_id: Optional[float] = None
    store: Optional["LinkApplicationStore"]


class LinkApplicationStore(BaseObject):
    """VK Object base/LinkApplicationStore

    id - Store Id
    name - Store name
    """

    id: Optional[float] = None
    name: Optional[str] = None


class LinkButton(BaseObject):
    """VK Object base/LinkButton

    action - Button action
    title - Button title
    block_id - Target block id
    section_id - Target section id
    owner_id - Owner id
    icon - Button icon name, e.g. 'phone' or 'gift'
    """

    action: Optional["LinkButtonAction"]
    title: Optional[str] = None
    block_id: Optional[str] = None
    section_id: Optional[str] = None
    owner_id: Optional[int] = None
    icon: Optional[str] = None
    style: Optional["LinkButtonStyle"]


class LinkButtonAction(BaseObject):
    """VK Object base/LinkButtonAction"""

    type: Optional["LinkButtonActionType"]
    url: Optional[str] = None
    consume_reason: Optional[str] = None


class LinkButtonActionType(enum.Enum):
    """ Action type """

    OPEN_URL = "open_url"


class LinkButtonStyle(enum.Enum):
    """ Button style """


class LinkProduct(BaseObject):
    """VK Object base/LinkProduct"""

    price: Optional[market.Price] = None
    merchant: Optional[str] = None
    orders_count: Optional[int] = None


class LinkRating(BaseObject):
    """VK Object base/LinkRating

    reviews_count - Count of reviews
    stars - Count of stars
    """

    reviews_count: Optional[int] = None
    stars: Optional[float] = None


class MessageError(BaseObject):
    """VK Object base/MessageError

    code - Error code
    description - Error message
    """

    code: Optional[int] = None
    description: Optional[str] = None


class Object(BaseObject):
    """VK Object base/Object

    id - Object ID
    title - Object title
    """

    id: Optional[int] = None
    title: Optional[str] = None


class ObjectCount(BaseObject):
    """VK Object base/ObjectCount

    count - Items count
    """

    count: Optional[int] = None


class ObjectWithName(BaseObject):
    """VK Object base/ObjectWithName

    id - Object ID
    name - Object name
    """

    id: Optional[int] = None
    name: Optional[str] = None


class Place(BaseObject):
    """VK Object base/Place"""

    address: Optional[str] = None
    checkins: Optional[int] = None
    city: Optional[str] = None
    country: Optional[str] = None
    created: Optional[int] = None
    icon: Optional[str] = None
    id: Optional[int] = None
    latitude: Optional[float] = None
    longitude: Optional[float] = None
    title: Optional[str] = None
    type: Optional[str] = None


class PropertyExists(enum.IntEnum):
    """ PropertyExists enum """

    property_exists = 1


class RepostsInfo(BaseObject):
    """VK Object base/RepostsInfo

    count - Reposts number
    user_reposted - Information whether current user has reposted the post
    """

    count: Optional[int] = None
    user_reposted: Optional[int] = None


class RequestParam(BaseObject):
    """VK Object base/RequestParam"""

    key: Optional[str] = None
    value: Optional[str] = None


class Sex(enum.IntEnum):
    """ Sex enum """

    unknown = 0
    female = 1
    male = 2


class Sticker(BaseObject):
    """VK Object base/Sticker

    sticker_id - Sticker ID
    product_id - Pack ID
    animation_url - URL of sticker animation script
    animations - Array of sticker animation script objects
    is_allowed - Information whether the sticker is allowed
    """

    sticker_id: Optional[int] = None
    product_id: Optional[int] = None
    images: Optional[List["Image"]]
    images_with_background: Optional[List["Image"]]
    animation_url: Optional[str] = None
    animations: Optional[List["StickerAnimation"]]
    is_allowed: Optional[bool] = None


class StickerAnimation(BaseObject):
    """VK Object base/StickerAnimation

    type - Type of animation script
    url - URL of animation script
    """

    type: Optional[str] = None
    url: Optional[str] = None


class UploadServer(BaseObject):
    """VK Object base/UploadServer"""

    upload_url: Optional[str] = None


class UserGroupFields(enum.Enum):
    """ UserGroupFields enum """

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
    VK_ADMIN_STATUS = "vk_admin_status"


class UserId(BaseObject):
    """VK Object base/UserId

    user_id - User ID
    """

    user_id: Optional[int] = None
