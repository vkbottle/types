from .base_model import BaseObject
from . import market, users, base
from typing import Optional, Union, Any, List
import typing
import enum


class Address(BaseObject):
    """VK Object groups/Address

    additional_address - Additional address to the place (6 floor, left door)
    address - String address to the place (Nevsky, 28)
    city_id - City id of address
    country_id - Country id of address
    distance - Distance from the point
    id - Address id
    latitude - Address latitude
    longitude - Address longitude
    metro_station_id - Metro id of address
    phone - Address phone
    time_offset - Time offset int minutes from utc time
    timetable - Week timetable for the address
    title - Title of the place (Zinger, etc)
    work_info_status - Status of information about timetable
    """

    additional_address: Optional[str] = None
    address: Optional[str] = None
    city_id: Optional[int] = None
    country_id: Optional[int] = None
    distance: Optional[int] = None
    id: Optional[int] = None
    latitude: Optional[float] = None
    longitude: Optional[float] = None
    metro_station_id: Optional[int] = None
    phone: Optional[str] = None
    time_offset: Optional[int] = None
    timetable: Optional["AddressTimetable"] = None
    title: Optional[str] = None
    work_info_status: Optional["AddressWorkInfoStatus"] = None


class AddressTimetable(BaseObject):
    """VK Object groups/AddressTimetable

    fri - Timetable for friday
    mon - Timetable for monday
    sat - Timetable for saturday
    sun - Timetable for sunday
    thu - Timetable for thursday
    tue - Timetable for tuesday
    wed - Timetable for wednesday
    """

    fri: Optional["AddressTimetableDay"] = None
    mon: Optional["AddressTimetableDay"] = None
    sat: Optional["AddressTimetableDay"] = None
    sun: Optional["AddressTimetableDay"] = None
    thu: Optional["AddressTimetableDay"] = None
    tue: Optional["AddressTimetableDay"] = None
    wed: Optional["AddressTimetableDay"] = None


class AddressTimetableDay(BaseObject):
    """VK Object groups/AddressTimetableDay"""

    break_close_time: Optional[int] = None
    break_open_time: Optional[int] = None
    close_time: Optional[int] = None
    open_time: Optional[int] = None


class AddressWorkInfoStatus(enum.Enum):
    """ Status of information about timetable """

    NO_INFORMATION = "no_information"
    TEMPORARILY_CLOSED = "temporarily_closed"
    ALWAYS_OPENED = "always_opened"
    TIMETABLE = "timetable"
    FOREVER_CLOSED = "forever_closed"


class AddressesInfo(BaseObject):
    """VK Object groups/AddressesInfo

    is_enabled - Information whether addresses is enabled
    main_address_id - Main address id for group
    """

    is_enabled: Optional[bool] = None
    main_address_id: Optional[int] = None


class BanInfo(BaseObject):
    """VK Object groups/BanInfo"""

    admin_id: Optional[int] = None
    comment: Optional[str] = None
    comment_visible: Optional[bool] = None
    is_closed: Optional[bool] = None
    date: Optional[int] = None
    end_date: Optional[int] = None
    reason: Optional["BanInfoReason"] = None


class BanInfoReason(enum.IntEnum):
    """ Ban reason """

    other = 0
    spam = 1
    verbal_abuse = 2
    strong_language = 3
    flood = 4


class BannedItem("OwnerXtrBanInfo"):
    """VK Object groups/BannedItem
    #FIXME Comment is undefined"""


class CallbackServer(BaseObject):
    """VK Object groups/CallbackServer"""

    id: Optional[int] = None
    title: Optional[str] = None
    creator_id: Optional[int] = None
    url: Optional[str] = None
    secret_key: Optional[str] = None
    status: Optional[str] = None


class CallbackSettings(BaseObject):
    """VK Object groups/CallbackSettings

    api_version - API version used for the events
    """

    api_version: Optional[str] = None
    events: Optional["LongPollEvents"] = None


class ContactsItem(BaseObject):
    """VK Object groups/ContactsItem

    desc - Contact description
    email - Contact email
    phone - Contact phone
    user_id - User ID
    """

    desc: Optional[str] = None
    email: Optional[str] = None
    phone: Optional[str] = None
    user_id: Optional[int] = None


class CountersGroup(BaseObject):
    """VK Object groups/CountersGroup

    addresses - Addresses number
    albums - Photo albums number
    audios - Audios number
    audio_playlists - Audio playlists number
    docs - Docs number
    market - Market items number
    photos - Photos number
    topics - Topics number
    videos - Videos number
    """

    addresses: Optional[int] = None
    albums: Optional[int] = None
    audios: Optional[int] = None
    audio_playlists: Optional[int] = None
    docs: Optional[int] = None
    market: Optional[int] = None
    photos: Optional[int] = None
    topics: Optional[int] = None
    videos: Optional[int] = None


class Cover(BaseObject):
    """VK Object groups/Cover"""

    enabled: Optional[base.BoolInt] = None
    images: Optional[List[base.Image]] = None


class Fields(enum.Enum):
    """ Fields enum """

    MARKET = "market"
    MEMBER_STATUS = "member_status"
    IS_FAVORITE = "is_favorite"
    IS_SUBSCRIBED = "is_subscribed"
    CITY = "city"
    COUNTRY = "country"
    VERIFIED = "verified"
    DESCRIPTION = "description"
    WIKI_PAGE = "wiki_page"
    MEMBERS_COUNT = "members_count"
    COUNTERS = "counters"
    COVER = "cover"
    CAN_POST = "can_post"
    CAN_SEE_ALL_POSTS = "can_see_all_posts"
    ACTIVITY = "activity"
    FIXED_POST = "fixed_post"
    CAN_CREATE_TOPIC = "can_create_topic"
    CAN_UPLOAD_VIDEO = "can_upload_video"
    HAS_PHOTO = "has_photo"
    STATUS = "status"
    MAIN_ALBUM_ID = "main_album_id"
    LINKS = "links"
    CONTACTS = "contacts"
    SITE = "site"
    MAIN_SECTION = "main_section"
    TRENDING = "trending"
    CAN_MESSAGE = "can_message"
    IS_MARKET_CART_ENABLED = "is_market_cart_enabled"
    IS_MESSAGES_BLOCKED = "is_messages_blocked"
    CAN_SEND_NOTIFY = "can_send_notify"
    ONLINE_STATUS = "online_status"
    START_DATE = "start_date"
    FINISH_DATE = "finish_date"
    AGE_LIMITS = "age_limits"
    BAN_INFO = "ban_info"
    ACTION_BUTTON = "action_button"
    AUTHOR_ID = "author_id"
    PHONE = "phone"
    HAS_MARKET_APP = "has_market_app"
    ADDRESSES = "addresses"
    LIVE_COVERS = "live_covers"
    IS_ADULT = "is_adult"
    CAN_SUBSCRIBE_POSTS = "can_subscribe_posts"
    WARNING_NOTIFICATION = "warning_notification"
    MSG_PUSH_ALLOWED = "msg_push_allowed"
    STORIES_ARCHIVE_COUNT = "stories_archive_count"
    VIDEO_LIVE_LEVEL = "video_live_level"
    VIDEO_LIVE_COUNT = "video_live_count"
    CLIPS_COUNT = "clips_count"


class Filter(enum.Enum):
    """ Filter enum """

    ADMIN = "admin"
    EDITOR = "editor"
    MODER = "moder"
    ADVERTISER = "advertiser"
    GROUPS = "groups"
    PUBLICS = "publics"
    EVENTS = "events"
    HAS_ADDRESSES = "has_addresses"


class Group(BaseObject):
    """VK Object groups/Group"""

    admin_level: Optional["GroupAdminLevel"] = None
    deactivated: Optional[str] = None
    finish_date: Optional[int] = None
    id: Optional[int] = None
    is_admin: Optional[base.BoolInt] = None
    is_advertiser: Optional[base.BoolInt] = None
    is_closed: Optional["GroupIsClosed"] = None
    is_member: Optional[base.BoolInt] = None
    name: Optional[str] = None
    photo_100: Optional[str] = None
    photo_200: Optional[str] = None
    photo_50: Optional[str] = None
    screen_name: Optional[str] = None
    start_date: Optional[int] = None
    type: Optional["GroupType"] = None


class GroupAccess(enum.IntEnum):
    """ GroupAccess enum """

    open = 0
    closed = 1
    private = 2


class GroupAdminLevel(enum.IntEnum):
    """ Level of current user's credentials as manager """

    moderator = 1
    editor = 2
    administrator = 3


class GroupAgeLimits(enum.IntEnum):
    """ GroupAgeLimits enum """

    unlimited = 1
    plus_16 = 2
    plus_18 = 3


class GroupAttach(BaseObject):
    """VK Object groups/GroupAttach"""

    id: Optional[int] = None
    text: Optional[str] = None
    status: Optional[str] = None
    size: Optional[int] = None
    is_favorite: Optional[bool] = None


class GroupAudio(enum.IntEnum):
    """ GroupAudio enum """

    disabled = 0
    open = 1
    limited = 2


class GroupBanInfo(BaseObject):
    """VK Object groups/GroupBanInfo

    comment - Ban comment
    end_date - End date of ban in Unixtime
    """

    comment: Optional[str] = None
    end_date: Optional[int] = None
    reason: Optional["BanInfoReason"] = None


class GroupCategory(BaseObject):
    """VK Object groups/GroupCategory

    id - Category ID
    name - Category name
    """

    id: Optional[int] = None
    name: Optional[str] = None
    subcategories: Optional[List[base.ObjectWithName]] = None


class GroupCategoryFull(BaseObject):
    """VK Object groups/GroupCategoryFull

    id - Category ID
    name - Category name
    page_count - Pages number
    """

    id: Optional[int] = None
    name: Optional[str] = None
    page_count: Optional[int] = None
    page_previews: Optional[List["Group"]] = None
    subcategories: Optional[List["GroupCategory"]] = None


class GroupCategoryType(BaseObject):
    """VK Object groups/GroupCategoryType"""

    id: Optional[int] = None
    name: Optional[str] = None


class GroupDocs(enum.IntEnum):
    """ GroupDocs enum """

    disabled = 0
    open = 1
    limited = 2


class GroupFull(BaseObject):
    """VK Object groups/GroupFull"""


class GroupFullAgeLimits(enum.IntEnum):
    """ GroupFullAgeLimits enum """

    no = 1
    over_16 = 2
    over_18 = 3


class GroupFullMainSection(enum.IntEnum):
    """ Main section of community """

    absent = 0
    photos = 1
    topics = 2
    audio = 3
    video = 4
    market = 5


class GroupFullMemberStatus(enum.IntEnum):
    """ GroupFullMemberStatus enum """

    not_a_member = 0
    member = 1
    not_sure = 2
    declined = 3
    has_sent_a_request = 4
    invited = 5


class GroupIsClosed(enum.IntEnum):
    """ Information whether community is closed """

    open = 0
    closed = 1
    private = 2


class GroupLink(BaseObject):
    """VK Object groups/GroupLink"""

    name: Optional[str] = None
    desc: Optional[str] = None
    edit_title: Optional[base.BoolInt] = None
    id: Optional[int] = None
    image_processing: Optional[base.BoolInt] = None
    url: Optional[str] = None


class GroupMarketCurrency(enum.IntEnum):
    """ GroupMarketCurrency enum """

    russian_rubles = 643
    ukrainian_hryvnia = 980
    kazakh_tenge = 398
    euro = 978
    us_dollars = 840


class GroupPhotos(enum.IntEnum):
    """ GroupPhotos enum """

    disabled = 0
    open = 1
    limited = 2


class GroupPublicCategoryList(BaseObject):
    """VK Object groups/GroupPublicCategoryList"""

    id: Optional[int] = None
    name: Optional[str] = None
    subcategories: Optional[List["GroupCategoryType"]] = None


class GroupRole(enum.Enum):
    """ GroupRole enum """

    MODERATOR = "moderator"
    EDITOR = "editor"
    ADMINISTRATOR = "administrator"
    ADVERTISER = "advertiser"


class GroupSubject(enum.IntEnum):
    """ GroupSubject enum """

    auto = 1
    activity_holidays = 2
    business = 3
    pets = 4
    health = 5
    dating_and_communication = 6
    games = 7
    it = 8
    cinema = 9
    beauty_and_fashion = 10
    cooking = 11
    art_and_culture = 12
    literature = 13
    mobile_services_and_internet = 14
    music = 15
    science_and_technology = 16
    real_estate = 17
    news_and_media = 18
    security = 19
    education = 20
    home_and_renovations = 21
    politics = 22
    food = 23
    industry = 24
    travel = 25
    work = 26
    entertainment = 27
    religion = 28
    family = 29
    sports = 30
    insurance = 31
    television = 32
    goods_and_services = 33
    hobbies = 34
    finance = 35
    photo = 36
    esoterics = 37
    electronics_and_appliances = 38
    erotic = 39
    humor = 40
    society_humanities = 41
    design_and_graphics = 42


class GroupTopics(enum.IntEnum):
    """ GroupTopics enum """

    disabled = 0
    open = 1
    limited = 2


class GroupType(enum.Enum):
    """ Community type """

    GROUP = "group"
    PAGE = "page"
    EVENT = "event"


class GroupVideo(enum.IntEnum):
    """ GroupVideo enum """

    disabled = 0
    open = 1
    limited = 2


class GroupWall(enum.IntEnum):
    """ GroupWall enum """

    disabled = 0
    open = 1
    limited = 2
    closed = 3


class GroupWiki(enum.IntEnum):
    """ GroupWiki enum """

    disabled = 0
    open = 1
    limited = 2


class GroupXtrInvitedBy(BaseObject):
    """VK Object groups/GroupXtrInvitedBy"""

    admin_level: Optional["GroupXtrInvitedByAdminLevel"] = None
    id: Optional[int] = None
    invited_by: Optional[int] = None
    is_admin: Optional[base.BoolInt] = None
    is_advertiser: Optional[base.BoolInt] = None
    is_closed: Optional[base.BoolInt] = None
    is_member: Optional[base.BoolInt] = None
    name: Optional[str] = None
    photo_100: Optional[str] = None
    photo_200: Optional[str] = None
    photo_50: Optional[str] = None
    screen_name: Optional[str] = None
    type: Optional["GroupXtrInvitedByType"] = None


class GroupXtrInvitedByAdminLevel(enum.IntEnum):
    """ Level of current user's credentials as manager """

    moderator = 1
    editor = 2
    administrator = 3


class GroupXtrInvitedByType(enum.Enum):
    """ Community type """

    GROUP = "group"
    PAGE = "page"
    EVENT = "event"


class GroupsArray(BaseObject):
    """VK Object groups/GroupsArray

    count - Communities number
    """

    count: Optional[int] = None
    items: Optional[List[int]] = None


class LinksItem(BaseObject):
    """VK Object groups/LinksItem

    desc - Link description
    edit_title - Information whether the link title can be edited
    id - Link ID
    name - Link title
    photo_100 - URL of square image of the link with 100 pixels in width
    photo_50 - URL of square image of the link with 50 pixels in width
    url - Link URL
    """

    desc: Optional[str] = None
    edit_title: Optional[base.BoolInt] = None
    id: Optional[int] = None
    name: Optional[str] = None
    photo_100: Optional[str] = None
    photo_50: Optional[str] = None
    url: Optional[str] = None


class LiveCovers(BaseObject):
    """VK Object groups/LiveCovers

    is_enabled - Information whether live covers is enabled
    is_scalable - Information whether live covers photo scaling is enabled
    """

    is_enabled: Optional[bool] = None
    is_scalable: Optional[bool] = None
    story_ids: Optional[List[str]] = None


class LongPollEvents(BaseObject):
    """VK Object groups/LongPollEvents"""

    audio_new: Optional[base.BoolInt] = None
    board_post_delete: Optional[base.BoolInt] = None
    board_post_edit: Optional[base.BoolInt] = None
    board_post_new: Optional[base.BoolInt] = None
    board_post_restore: Optional[base.BoolInt] = None
    group_change_photo: Optional[base.BoolInt] = None
    group_change_settings: Optional[base.BoolInt] = None
    group_join: Optional[base.BoolInt] = None
    group_leave: Optional[base.BoolInt] = None
    group_officers_edit: Optional[base.BoolInt] = None
    lead_forms_new: Optional[base.BoolInt] = None
    market_comment_delete: Optional[base.BoolInt] = None
    market_comment_edit: Optional[base.BoolInt] = None
    market_comment_new: Optional[base.BoolInt] = None
    market_comment_restore: Optional[base.BoolInt] = None
    message_allow: Optional[base.BoolInt] = None
    message_deny: Optional[base.BoolInt] = None
    message_new: Optional[base.BoolInt] = None
    message_read: Optional[base.BoolInt] = None
    message_reply: Optional[base.BoolInt] = None
    message_typing_state: Optional[base.BoolInt] = None
    message_edit: Optional[base.BoolInt] = None
    photo_comment_delete: Optional[base.BoolInt] = None
    photo_comment_edit: Optional[base.BoolInt] = None
    photo_comment_new: Optional[base.BoolInt] = None
    photo_comment_restore: Optional[base.BoolInt] = None
    photo_new: Optional[base.BoolInt] = None
    poll_vote_new: Optional[base.BoolInt] = None
    user_block: Optional[base.BoolInt] = None
    user_unblock: Optional[base.BoolInt] = None
    video_comment_delete: Optional[base.BoolInt] = None
    video_comment_edit: Optional[base.BoolInt] = None
    video_comment_new: Optional[base.BoolInt] = None
    video_comment_restore: Optional[base.BoolInt] = None
    video_new: Optional[base.BoolInt] = None
    wall_post_new: Optional[base.BoolInt] = None
    wall_reply_delete: Optional[base.BoolInt] = None
    wall_reply_edit: Optional[base.BoolInt] = None
    wall_reply_new: Optional[base.BoolInt] = None
    wall_reply_restore: Optional[base.BoolInt] = None
    wall_repost: Optional[base.BoolInt] = None


class LongPollServer(BaseObject):
    """VK Object groups/LongPollServer

    key - Long Poll key
    server - Long Poll server address
    ts - Number of the last event
    """

    key: Optional[str] = None
    server: Optional[str] = None
    ts: Optional[str] = None


class LongPollSettings(BaseObject):
    """VK Object groups/LongPollSettings

    api_version - API version used for the events
    is_enabled - Shows whether Long Poll is enabled
    """

    api_version: Optional[str] = None
    events: Optional["LongPollEvents"] = None
    is_enabled: Optional[bool] = None


class MarketInfo(BaseObject):
    """VK Object groups/MarketInfo

    contact_id - Contact person ID
    currency_text - Currency name
    enabled - Information whether the market is enabled
    main_album_id - Main market album ID
    price_max - Maximum price
    price_min - Minimum price
    """

    contact_id: Optional[int] = None
    currency: Optional[market.Currency] = None
    currency_text: Optional[str] = None
    enabled: Optional[base.BoolInt] = None
    main_album_id: Optional[int] = None
    price_max: Optional[str] = None
    price_min: Optional[str] = None


class MemberRole(BaseObject):
    """VK Object groups/MemberRole"""

    id: Optional[int] = None
    permissions: Optional[List["MemberRolePermission"]] = None
    role: Optional["MemberRoleStatus"] = None


class MemberRolePermission(enum.Enum):
    """ MemberRolePermission enum """

    ADS = "ads"


class MemberRoleStatus(enum.Enum):
    """ User's credentials as community admin """

    MODERATOR = "moderator"
    EDITOR = "editor"
    ADMINISTRATOR = "administrator"
    CREATOR = "creator"


class MemberStatus(BaseObject):
    """VK Object groups/MemberStatus

    member - Information whether user is a member of the group
    user_id - User ID
    """

    member: Optional[base.BoolInt] = None
    user_id: Optional[int] = None


class MemberStatusFull(BaseObject):
    """VK Object groups/MemberStatusFull

    can_invite - Information whether user can be invited
    can_recall - Information whether user's invite to the group can be recalled
    invitation - Information whether user has been invited to the group
    member - Information whether user is a member of the group
    request - Information whether user has send request to the group
    user_id - User ID
    """

    can_invite: Optional[base.BoolInt] = None
    can_recall: Optional[base.BoolInt] = None
    invitation: Optional[base.BoolInt] = None
    member: Optional[base.BoolInt] = None
    request: Optional[base.BoolInt] = None
    user_id: Optional[int] = None


class OnlineStatus(BaseObject):
    """VK Object groups/OnlineStatus"""

    minutes: Optional[int] = None
    status: Optional["OnlineStatusType"] = None


class OnlineStatusType(enum.Enum):
    """ Type of online status of group """

    NONE = "none"
    ONLINE = "online"
    ANSWER_MARK = "answer_mark"


class OwnerXtrBanInfo(BaseObject):
    """VK Object groups/OwnerXtrBanInfo"""

    ban_info: Optional["BanInfo"] = None
    group: Optional["Group"] = None
    profile: Optional[users.User] = None
    type: Optional["OwnerXtrBanInfoType"] = None


class OwnerXtrBanInfoType(enum.Enum):
    """ Owner type """

    GROUP = "group"
    PROFILE = "profile"


class RoleOptions(enum.Enum):
    """ User's credentials as community admin """

    MODERATOR = "moderator"
    EDITOR = "editor"
    ADMINISTRATOR = "administrator"
    CREATOR = "creator"


class SettingsTwitter(BaseObject):
    """VK Object groups/SettingsTwitter"""

    status: Optional[str] = None
    name: Optional[str] = None


class SubjectItem(BaseObject):
    """VK Object groups/SubjectItem

    id - Subject ID
    name - Subject title
    """

    id: Optional[int] = None
    name: Optional[str] = None


class TokenPermissionSetting(BaseObject):
    """VK Object groups/TokenPermissionSetting"""

    name: Optional[str] = None
    setting: Optional[int] = None


class UserXtrRole(BaseObject):
    """VK Object groups/UserXtrRole"""
