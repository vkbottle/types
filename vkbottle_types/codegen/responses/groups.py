import typing
from vkbottle_types.responses.base_response import BaseResponse, BaseModel
from vkbottle_types.base_model import Field

from vkbottle_types.objects import (
    GroupsLongPollEvents,
    GroupsMarketInfo,
    GroupsGroupSubcategory,
    GroupsGroupFullSection,
    BaseObjectWithName,
    AudioAudio,
    GroupsAddressesInfo,
    GroupsBanInfo,
    GroupsLiveCovers,
    GroupsAddress,
    BaseCropPhoto,
    DatabaseStation,
    GroupsGroupBanInfo,
    GroupsGroup,
    GroupsGroupIsClosed,
    GroupsGroupCategoryType,
    GroupsGroupAdminLevel,
    GroupsMemberRolePermission,
    GroupsMemberRoleStatus,
    DatabaseCityById,
    GroupsAddressWorkInfoStatus,
    GroupsGroupCategory,
    MarketCurrency,
    GroupsGroupFullMemberStatus,
    GroupsGroupFullAgeLimits,
    GroupsLinksItem,
    MarketPrice,
    GroupsPhotoSize,
    GroupsContactsItem,
    UsersUser,
    BaseBoolInt,
    GroupsOnlineStatusType,
    BaseObject,
    GroupsAddressTimetable,
    GroupsBanInfoReason,
    BaseOwnerCover,
    GroupsCountersGroup,
    GroupsRoleOptions,
    GroupsOnlineStatus,
    BaseCountry,
    VideoLiveInfo,
    GroupsOwnerXtrBanInfoType,
    GroupsGroupType,
    GroupsAddressTimetableDay,
)


class GroupsAddressResponseModel(BaseModel):
    id: int = Field(
        description="Address id",
    )

    additional_address: typing.Optional[str] = Field(
        default=None,
        description="Additional address to the place (6 floor, left door)",
    )

    address: typing.Optional[str] = Field(
        default=None,
        description="String address to the place (Nevsky, 28)",
    )

    city_id: typing.Optional[int] = Field(
        default=None,
        description="City id of address",
    )

    country_id: typing.Optional[int] = Field(
        default=None,
        description="Country id of address",
    )

    city: typing.Optional["DatabaseCityById"] = Field(
        default=None,
        description="City for address",
    )

    metro_station: typing.Optional["DatabaseStation"] = Field(
        default=None,
        description="Metro for address",
    )

    country: typing.Optional["BaseCountry"] = Field(
        default=None,
        description="Country for address",
    )

    distance: typing.Optional[int] = Field(
        default=None,
        description="Distance from the point",
    )

    latitude: typing.Optional[float] = Field(
        default=None,
        description="Address latitude",
    )

    longitude: typing.Optional[float] = Field(
        default=None,
        description="Address longitude",
    )

    metro_station_id: typing.Optional[int] = Field(
        default=None,
        description="Metro id of address",
    )

    phone: typing.Optional[str] = Field(
        default=None,
        description="Address phone",
    )

    time_offset: typing.Optional[int] = Field(
        default=None,
        description="Time offset int minutes from utc time",
    )

    timetable: typing.Optional["GroupsAddressTimetable"] = Field(
        default=None,
        description="Week timetable for the address",
    )

    title: typing.Optional[str] = Field(
        default=None,
        description="Title of the place (Zinger, etc)",
    )

    work_info_status: typing.Optional["GroupsAddressWorkInfoStatus"] = Field(
        default=None,
        description="Status of information about timetable",
    )

    place_id: typing.Optional[int] = Field(
        default=None,
    )


class GroupsAddressResponse(BaseResponse):
    response: "GroupsAddressResponseModel"


class GroupsAddressTimetableResponseModel(BaseModel):
    fri: typing.Optional["GroupsAddressTimetableDay"] = Field(
        default=None,
        description="Timetable for friday",
    )

    mon: typing.Optional["GroupsAddressTimetableDay"] = Field(
        default=None,
        description="Timetable for monday",
    )

    sat: typing.Optional["GroupsAddressTimetableDay"] = Field(
        default=None,
        description="Timetable for saturday",
    )

    sun: typing.Optional["GroupsAddressTimetableDay"] = Field(
        default=None,
        description="Timetable for sunday",
    )

    thu: typing.Optional["GroupsAddressTimetableDay"] = Field(
        default=None,
        description="Timetable for thursday",
    )

    tue: typing.Optional["GroupsAddressTimetableDay"] = Field(
        default=None,
        description="Timetable for tuesday",
    )

    wed: typing.Optional["GroupsAddressTimetableDay"] = Field(
        default=None,
        description="Timetable for wednesday",
    )


class GroupsAddressTimetableResponse(BaseResponse):
    response: "GroupsAddressTimetableResponseModel"


class GroupsAddressTimetableDayResponseModel(BaseModel):
    close_time: int = Field(
        description="Close time in minutes",
    )

    open_time: int = Field(
        description="Open time in minutes",
    )

    break_close_time: typing.Optional[int] = Field(
        default=None,
        description="Close time of the break in minutes",
    )

    break_open_time: typing.Optional[int] = Field(
        default=None,
        description="Start time of the break in minutes",
    )


class GroupsAddressTimetableDayResponse(BaseResponse):
    response: "GroupsAddressTimetableDayResponseModel"


class GroupsAddressWorkInfoStatusResponseModel(enum.Enum):
    NO_INFORMATION = "no_information"

    TEMPORARILY_CLOSED = "temporarily_closed"

    ALWAYS_OPENED = "always_opened"

    TIMETABLE = "timetable"

    FOREVER_CLOSED = "forever_closed"


class GroupsAddressWorkInfoStatusResponse(BaseResponse):
    response: "GroupsAddressWorkInfoStatusResponseModel"


class GroupsAddressesInfoResponseModel(BaseModel):
    is_enabled: bool = Field(
        description="Information whether addresses is enabled",
    )

    main_address_id: typing.Optional[int] = Field(
        default=None,
        description="Main address id for group",
    )

    main_address: typing.Optional["GroupsAddress"] = Field(
        default=None,
        description="Main address",
    )

    count: typing.Optional[int] = Field(
        default=None,
        description="Count of addresses",
    )


class GroupsAddressesInfoResponse(BaseResponse):
    response: "GroupsAddressesInfoResponseModel"


class GroupsBanInfoResponseModel(BaseModel):
    admin_id: typing.Optional[int] = Field(
        default=None,
        description="Administrator ID",
    )

    comment: typing.Optional[str] = Field(
        default=None,
        description="Comment for a ban",
    )

    comment_visible: typing.Optional[bool] = Field(
        default=None,
        description="Show comment for user",
    )

    is_closed: typing.Optional[bool] = Field(
        default=None,
    )

    date: typing.Optional[int] = Field(
        default=None,
        description="Date when user has been added to blacklist in Unixtime",
    )

    end_date: typing.Optional[int] = Field(
        default=None,
        description="Date when user will be removed from blacklist in Unixtime",
    )

    reason: typing.Optional["GroupsBanInfoReason"] = Field(
        default=None,
    )


class GroupsBanInfoResponse(BaseResponse):
    response: "GroupsBanInfoResponseModel"


class GroupsBanInfoReasonResponseModel(enum.IntEnum):
    OTHER = 0

    SPAM = 1

    VERBAL_ABUSE = 2

    STRONG_LANGUAGE = 3

    FLOOD = 4


class GroupsBanInfoReasonResponse(BaseResponse):
    response: "GroupsBanInfoReasonResponseModel"


class GroupsBannedItemResponseModel(BaseModel):
    pass


class GroupsBannedItemResponse(BaseResponse):
    response: "GroupsBannedItemResponseModel"


class GroupsCallbackServerResponseModel(BaseModel):
    id: int = Field()

    title: str = Field()

    creator_id: int = Field()

    url: str = Field()

    secret_key: str = Field()

    status: typing.Literal["unconfigured", "failed", "wait", "ok"] = Field()


class GroupsCallbackServerResponse(BaseResponse):
    response: "GroupsCallbackServerResponseModel"


class GroupsCallbackSettingsResponseModel(BaseModel):
    api_version: typing.Optional[str] = Field(
        default=None,
        description="API version used for the events",
    )

    events: typing.Optional["GroupsLongPollEvents"] = Field(
        default=None,
    )


class GroupsCallbackSettingsResponse(BaseResponse):
    response: "GroupsCallbackSettingsResponseModel"


class GroupsClassifiedsPropertiesResponseModel(BaseModel):
    pass


class GroupsClassifiedsPropertiesResponse(BaseResponse):
    response: "GroupsClassifiedsPropertiesResponseModel"


class GroupsContactsItemResponseModel(BaseModel):
    user_id: typing.Optional[int] = Field(
        default=None,
        description="User ID",
    )

    desc: typing.Optional[str] = Field(
        default=None,
        description="Contact description",
    )

    phone: typing.Optional[str] = Field(
        default=None,
        description="Contact phone",
    )

    email: typing.Optional[str] = Field(
        default=None,
        description="Contact email",
    )


class GroupsContactsItemResponse(BaseResponse):
    response: "GroupsContactsItemResponseModel"


class GroupsCountersGroupResponseModel(BaseModel):
    addresses: typing.Optional[int] = Field(
        default=None,
        description="Addresses number",
    )

    albums: typing.Optional[int] = Field(
        default=None,
        description="Photo albums number",
    )

    audios: typing.Optional[int] = Field(
        default=None,
        description="Audios number",
    )

    audio_playlists: typing.Optional[int] = Field(
        default=None,
        description="Audio playlists number",
    )

    docs: typing.Optional[int] = Field(
        default=None,
        description="Docs number",
    )

    market: typing.Optional[int] = Field(
        default=None,
        description="Market items number",
    )

    photos: typing.Optional[int] = Field(
        default=None,
        description="Photos number",
    )

    topics: typing.Optional[int] = Field(
        default=None,
        description="Topics number",
    )

    videos: typing.Optional[int] = Field(
        default=None,
        description="Videos number",
    )

    video_playlists: typing.Optional[int] = Field(
        default=None,
        description="Playlists number",
    )

    market_services: typing.Optional[int] = Field(
        default=None,
        description="Market services number",
    )

    podcasts: typing.Optional[int] = Field(
        default=None,
        description="Podcasts number",
    )

    articles: typing.Optional[int] = Field(
        default=None,
        description="Articles number",
    )

    narratives: typing.Optional[int] = Field(
        default=None,
        description="Narratives number",
    )

    clips: typing.Optional[int] = Field(
        default=None,
        description="Clips number",
    )

    clips_followers: typing.Optional[int] = Field(
        default=None,
        description="Clips followers number",
    )

    videos_followers: typing.Optional[int] = Field(
        default=None,
        description="Videos followers number",
    )

    clips_views: typing.Optional[int] = Field(
        default=None,
        description="Clips views number",
    )

    clips_likes: typing.Optional[int] = Field(
        default=None,
        description="Clips likes number",
    )


class GroupsCountersGroupResponse(BaseResponse):
    response: "GroupsCountersGroupResponseModel"


class GroupsFieldsResponseModel(enum.Enum):
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

    COUNTRY = "country"

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

    IS_SUBSCRIBED_PODCASTS = "is_subscribed_podcasts"

    CAN_SUBSCRIBE_PODCASTS = "can_subscribe_podcasts"

    CAN_SUBSCRIBE_POSTS = "can_subscribe_posts"

    LIVE_COVERS = "live_covers"

    STORIES_ARCHIVE_COUNT = "stories_archive_count"

    HAS_UNSEEN_STORIES = "has_unseen_stories"

    RATING = "rating"


class GroupsFieldsResponse(BaseResponse):
    response: "GroupsFieldsResponseModel"


class GroupsFilterResponseModel(enum.Enum):
    ADMIN = "admin"

    EDITOR = "editor"

    MODER = "moder"

    ADVERTISER = "advertiser"

    GROUPS = "groups"

    PUBLICS = "publics"

    EVENTS = "events"

    HAS_ADDRESSES = "has_addresses"


class GroupsFilterResponse(BaseResponse):
    response: "GroupsFilterResponseModel"


class GroupsGroupResponseModel(BaseModel):
    id: int = Field(
        description="Community ID",
    )

    name: typing.Optional[str] = Field(
        default=None,
        description="Community name",
    )

    screen_name: typing.Optional[str] = Field(
        default=None,
        description="Domain of the community page",
    )

    is_closed: typing.Optional["GroupsGroupIsClosed"] = Field(
        default=None,
    )

    type: typing.Optional["GroupsGroupType"] = Field(
        default=None,
    )

    is_admin: typing.Optional[bool] = Field(
        default=None,
        description="Information whether current user is administrator",
    )

    admin_level: typing.Optional["GroupsGroupAdminLevel"] = Field(
        default=None,
    )

    is_member: typing.Optional[bool] = Field(
        default=None,
        description="Information whether current user is member",
    )

    is_advertiser: typing.Optional[bool] = Field(
        default=None,
        description="Information whether current user is advertiser",
    )

    start_date: typing.Optional[int] = Field(
        default=None,
        description="Start date in Unixtime format",
    )

    finish_date: typing.Optional[int] = Field(
        default=None,
        description="Finish date in Unixtime format",
    )

    verified: typing.Optional[bool] = Field(
        default=None,
        description="Information whether community is verified",
    )

    deactivated: typing.Optional[str] = Field(
        default=None,
        description="Information whether community is banned",
    )

    photo_50: typing.Optional[str] = Field(
        default=None,
        description="URL of square photo of the community with 50 pixels in width",
    )

    photo_100: typing.Optional[str] = Field(
        default=None,
        description="URL of square photo of the community with 100 pixels in width",
    )

    photo_200: typing.Optional[str] = Field(
        default=None,
        description="URL of square photo of the community with 200 pixels in width",
    )

    photo_200_orig: typing.Optional[str] = Field(
        default=None,
        description="URL of square photo of the community with 200 pixels in width original",
    )

    photo_400: typing.Optional[str] = Field(
        default=None,
        description="URL of square photo of the community with 400 pixels in width",
    )

    photo_400_orig: typing.Optional[str] = Field(
        default=None,
        description="URL of square photo of the community with 400 pixels in width original",
    )

    photo_max: typing.Optional[str] = Field(
        default=None,
        description="URL of square photo of the community with max pixels in width",
    )

    photo_max_orig: typing.Optional[str] = Field(
        default=None,
        description="URL of square photo of the community with max pixels in width original",
    )

    est_date: typing.Optional[str] = Field(
        default=None,
        description="Established date",
    )

    public_date_label: typing.Optional[str] = Field(
        default=None,
        description="Public date label",
    )

    photo_max_size: typing.Optional["GroupsPhotoSize"] = Field(
        default=None,
    )

    is_video_live_notifications_blocked: typing.Optional[bool] = Field(
        default=None,
    )

    video_live: typing.Optional["VideoLiveInfo"] = Field(
        default=None,
    )


class GroupsGroupResponse(BaseResponse):
    response: "GroupsGroupResponseModel"


class GroupsGroupAccessResponseModel(enum.IntEnum):
    OPEN = 0

    CLOSED = 1

    PRIVATE = 2


class GroupsGroupAccessResponse(BaseResponse):
    response: "GroupsGroupAccessResponseModel"


class GroupsGroupAdminLevelResponseModel(enum.IntEnum):
    MODERATOR = 1

    EDITOR = 2

    ADMINISTRATOR = 3


class GroupsGroupAdminLevelResponse(BaseResponse):
    response: "GroupsGroupAdminLevelResponseModel"


class GroupsGroupAgeLimitsResponseModel(enum.IntEnum):
    UNLIMITED = 1

    _16_PLUS = 2

    _18_PLUS = 3


class GroupsGroupAgeLimitsResponse(BaseResponse):
    response: "GroupsGroupAgeLimitsResponseModel"


class GroupsGroupAttachResponseModel(BaseModel):
    id: int = Field(
        description="group ID",
    )

    text: str = Field(
        description="text of attach",
    )

    status: str = Field(
        description="activity or category of group",
    )

    size: int = Field(
        description="size of group",
    )

    is_favorite: bool = Field(
        description="is favorite",
    )


class GroupsGroupAttachResponse(BaseResponse):
    response: "GroupsGroupAttachResponseModel"


class GroupsGroupAudioResponseModel(enum.IntEnum):
    DISABLED = 0

    OPEN = 1

    LIMITED = 2


class GroupsGroupAudioResponse(BaseResponse):
    response: "GroupsGroupAudioResponseModel"


class GroupsGroupBanInfoResponseModel(BaseModel):
    comment: typing.Optional[str] = Field(
        default=None,
        description="Ban comment",
    )

    end_date: typing.Optional[int] = Field(
        default=None,
        description="End date of ban in Unixtime",
    )

    reason: typing.Optional["GroupsBanInfoReason"] = Field(
        default=None,
    )


class GroupsGroupBanInfoResponse(BaseResponse):
    response: "GroupsGroupBanInfoResponseModel"


class GroupsGroupCategoryResponseModel(BaseModel):
    id: int = Field(
        description="Category ID",
    )

    name: str = Field(
        description="Category name",
    )

    subcategories: typing.Optional[typing.List[GroupsGroupSubcategory]] = Field(
        default=None,
    )


class GroupsGroupCategoryResponse(BaseResponse):
    response: "GroupsGroupCategoryResponseModel"


class GroupsGroupCategoryFullResponseModel(BaseModel):
    id: int = Field(
        description="Category ID",
    )

    name: str = Field(
        description="Category name",
    )

    page_count: int = Field(
        description="Pages number",
    )

    page_previews: typing.List[GroupsGroup] = Field()

    subcategories: typing.Optional[typing.List[GroupsGroupCategory]] = Field(
        default=None,
    )


class GroupsGroupCategoryFullResponse(BaseResponse):
    response: "GroupsGroupCategoryFullResponseModel"


class GroupsGroupCategoryTypeResponseModel(BaseModel):
    id: int = Field()

    name: str = Field()


class GroupsGroupCategoryTypeResponse(BaseResponse):
    response: "GroupsGroupCategoryTypeResponseModel"


class GroupsGroupDocsResponseModel(enum.IntEnum):
    DISABLED = 0

    OPEN = 1

    LIMITED = 2


class GroupsGroupDocsResponse(BaseResponse):
    response: "GroupsGroupDocsResponseModel"


class GroupsGroupFullResponseModel(
    GroupsGroup, GroupsMarketProperties, GroupsClassifiedsProperties
):
    member_status: typing.Optional["GroupsGroupFullMemberStatus"] = Field(
        default=None,
        description="Current user's member status",
    )

    is_adult: typing.Optional[bool] = Field(
        default=None,
        description="Information whether community is adult",
    )

    is_hidden_from_feed: typing.Optional[bool] = Field(
        default=None,
        description="Information whether community is hidden from current user's newsfeed",
    )

    is_favorite: typing.Optional[bool] = Field(
        default=None,
        description="Information whether community is in faves",
    )

    is_subscribed: typing.Optional[bool] = Field(
        default=None,
        description="Information whether current user is subscribed",
    )

    city: typing.Optional["BaseObject"] = Field(
        default=None,
    )

    country: typing.Optional["BaseCountry"] = Field(
        default=None,
    )

    description: typing.Optional[str] = Field(
        default=None,
        description="Community description",
    )

    wiki_page: typing.Optional[str] = Field(
        default=None,
        description="Community's main wiki page title",
    )

    members_count: typing.Optional[int] = Field(
        default=None,
        description="Community members number",
    )

    members_count_text: typing.Optional[str] = Field(
        default=None,
        description="Info about number of users in group",
    )

    requests_count: typing.Optional[int] = Field(
        default=None,
        description="The number of incoming requests to the community",
    )

    video_live_level: typing.Optional[int] = Field(
        default=None,
        description="Community level live streams achievements",
    )

    video_live_count: typing.Optional[int] = Field(
        default=None,
        description="Number of community's live streams",
    )

    clips_count: typing.Optional[int] = Field(
        default=None,
        description="Number of community's clips",
    )

    counters: typing.Optional["GroupsCountersGroup"] = Field(
        default=None,
    )

    textlives_count: typing.Optional[int] = Field(
        default=None,
        description="Textlives number",
    )

    cover: typing.Optional["BaseOwnerCover"] = Field(
        default=None,
    )

    can_post: typing.Optional[bool] = Field(
        default=None,
        description="Information whether current user can post on community's wall",
    )

    can_suggest: typing.Optional[bool] = Field(
        default=None,
    )

    can_upload_story: typing.Optional[bool] = Field(
        default=None,
        description="Information whether current user can upload story",
    )

    can_call_to_community: typing.Optional[bool] = Field(
        default=None,
        description="Information whether current user can call to community",
    )

    can_upload_doc: typing.Optional[bool] = Field(
        default=None,
        description="Information whether current user can upload doc",
    )

    can_upload_video: typing.Optional[bool] = Field(
        default=None,
        description="Information whether current user can upload video",
    )

    can_upload_clip: typing.Optional[bool] = Field(
        default=None,
        description="Information whether current user can upload clip",
    )

    can_see_all_posts: typing.Optional[bool] = Field(
        default=None,
        description="Information whether current user can see all posts on community's wall",
    )

    can_create_topic: typing.Optional[bool] = Field(
        default=None,
        description="Information whether current user can create topic",
    )

    activity: typing.Optional[str] = Field(
        default=None,
        description="Type of group, start date of event or category of public page",
    )

    fixed_post: typing.Optional[int] = Field(
        default=None,
        description="Fixed post ID",
    )

    has_photo: typing.Optional[bool] = Field(
        default=None,
        description="Information whether community has photo",
    )

    crop_photo: typing.Optional["BaseCropPhoto"] = Field(
        default=None,
        description="Данные о точках, по которым вырезаны профильная и миниатюрная фотографии сообщества",
    )

    status: typing.Optional[str] = Field(
        default=None,
        description="Community status",
    )

    status_audio: typing.Optional["AudioAudio"] = Field(
        default=None,
    )

    main_album_id: typing.Optional[int] = Field(
        default=None,
        description="Community's main photo album ID",
    )

    links: typing.Optional[typing.List[GroupsLinksItem]] = Field(
        default=None,
    )

    contacts: typing.Optional[typing.List[GroupsContactsItem]] = Field(
        default=None,
    )

    wall: typing.Optional[int] = Field(
        default=None,
        description="Information about wall status in community",
    )

    site: typing.Optional[str] = Field(
        default=None,
        description="Community's website",
    )

    main_section: typing.Optional["GroupsGroupFullSection"] = Field(
        default=None,
    )

    secondary_section: typing.Optional["GroupsGroupFullSection"] = Field(
        default=None,
    )

    trending: typing.Optional[bool] = Field(
        default=None,
        description='Information whether the community has a "fire" pictogram.',
    )

    can_message: typing.Optional[bool] = Field(
        default=None,
        description="Information whether current user can send a message to community",
    )

    is_messages_blocked: typing.Optional[bool] = Field(
        default=None,
        description="Information whether community can send a message to current user",
    )

    can_send_notify: typing.Optional[bool] = Field(
        default=None,
        description="Information whether community can send notifications by phone number to current user",
    )

    online_status: typing.Optional["GroupsOnlineStatus"] = Field(
        default=None,
        description="Status of replies in community messages",
    )

    invited_by: typing.Optional[int] = Field(
        default=None,
        description="Inviter ID",
    )

    age_limits: typing.Optional["GroupsGroupFullAgeLimits"] = Field(
        default=None,
        description="Information whether age limit",
    )

    ban_info: typing.Optional["GroupsGroupBanInfo"] = Field(
        default=None,
        description="User ban info",
    )

    has_group_channel: typing.Optional[bool] = Field(
        default=None,
    )

    addresses: typing.Optional["GroupsAddressesInfo"] = Field(
        default=None,
        description="Info about addresses in groups",
    )

    is_subscribed_podcasts: typing.Optional[bool] = Field(
        default=None,
        description="Information whether current user is subscribed to podcasts",
    )

    can_subscribe_podcasts: typing.Optional[bool] = Field(
        default=None,
        description="Owner in whitelist or not",
    )

    can_subscribe_posts: typing.Optional[bool] = Field(
        default=None,
        description="Can subscribe to wall",
    )

    live_covers: typing.Optional["GroupsLiveCovers"] = Field(
        default=None,
        description="Live covers state",
    )

    stories_archive_count: typing.Optional[int] = Field(
        default=None,
    )

    has_unseen_stories: typing.Optional[bool] = Field(
        default=None,
    )


class GroupsGroupFullResponse(BaseResponse):
    response: "GroupsGroupFullResponseModel"


class GroupsGroupFullAgeLimitsResponseModel(enum.IntEnum):
    NO = 1

    OVER_16 = 2

    OVER_18 = 3


class GroupsGroupFullAgeLimitsResponse(BaseResponse):
    response: "GroupsGroupFullAgeLimitsResponseModel"


class GroupsGroupFullMemberStatusResponseModel(enum.IntEnum):
    NOT_A_MEMBER = 0

    MEMBER = 1

    NOT_SURE = 2

    DECLINED = 3

    HAS_SENT_A_REQUEST = 4

    INVITED = 5


class GroupsGroupFullMemberStatusResponse(BaseResponse):
    response: "GroupsGroupFullMemberStatusResponseModel"


class GroupsGroupFullSectionResponseModel(enum.IntEnum):
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


class GroupsGroupFullSectionResponse(BaseResponse):
    response: "GroupsGroupFullSectionResponseModel"


class GroupsGroupIsClosedResponseModel(enum.IntEnum):
    OPEN = 0

    CLOSED = 1

    PRIVATE = 2


class GroupsGroupIsClosedResponse(BaseResponse):
    response: "GroupsGroupIsClosedResponseModel"


class GroupsGroupMarketCurrencyResponseModel(enum.IntEnum):
    RUSSIAN_RUBLES = 643

    UKRAINIAN_HRYVNIA = 980

    KAZAKH_TENGE = 398

    EURO = 978

    US_DOLLARS = 840


class GroupsGroupMarketCurrencyResponse(BaseResponse):
    response: "GroupsGroupMarketCurrencyResponseModel"


class GroupsGroupPhotosResponseModel(enum.IntEnum):
    DISABLED = 0

    OPEN = 1

    LIMITED = 2


class GroupsGroupPhotosResponse(BaseResponse):
    response: "GroupsGroupPhotosResponseModel"


class GroupsGroupPublicCategoryListResponseModel(BaseModel):
    id: typing.Optional[int] = Field(
        default=None,
    )

    name: typing.Optional[str] = Field(
        default=None,
    )

    subcategories: typing.Optional[typing.List[GroupsGroupCategoryType]] = Field(
        default=None,
    )


class GroupsGroupPublicCategoryListResponse(BaseResponse):
    response: "GroupsGroupPublicCategoryListResponseModel"


class GroupsGroupRoleResponseModel(enum.Enum):
    MODERATOR = "moderator"

    EDITOR = "editor"

    ADMINISTRATOR = "administrator"

    ADVERTISER = "advertiser"


class GroupsGroupRoleResponse(BaseResponse):
    response: "GroupsGroupRoleResponseModel"


class GroupsGroupSubcategoryResponseModel(BaseModel):
    id: int = Field(
        description="Object ID",
    )

    name: str = Field(
        description="Object name",
    )

    genders: typing.Optional[typing.List[BaseObjectWithName]] = Field(
        default=None,
    )


class GroupsGroupSubcategoryResponse(BaseResponse):
    response: "GroupsGroupSubcategoryResponseModel"


class GroupsGroupSubjectResponseModel(enum.IntEnum):
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


class GroupsGroupSubjectResponse(BaseResponse):
    response: "GroupsGroupSubjectResponseModel"


class GroupsGroupSuggestedPrivacyResponseModel(enum.IntEnum):
    NONE = 0

    ALL = 1

    SUBSCRIBERS = 2


class GroupsGroupSuggestedPrivacyResponse(BaseResponse):
    response: "GroupsGroupSuggestedPrivacyResponseModel"


class GroupsGroupTagResponseModel(BaseModel):
    id: int = Field()

    name: str = Field()

    color: typing.Literal[
        "454647",
        "45678f",
        "4bb34b",
        "5181b8",
        "539b9c",
        "5c9ce6",
        "63b9ba",
        "6bc76b",
        "76787a",
        "792ec0",
        "7a6c4f",
        "7ececf",
        "9e8d6b",
        "a162de",
        "aaaeb3",
        "bbaa84",
        "e64646",
        "ff5c5c",
        "ffa000",
        "ffc107",
    ] = Field()

    uses: typing.Optional[int] = Field(
        default=None,
    )


class GroupsGroupTagResponse(BaseResponse):
    response: "GroupsGroupTagResponseModel"


class GroupsGroupTopicsResponseModel(enum.IntEnum):
    DISABLED = 0

    OPEN = 1

    LIMITED = 2


class GroupsGroupTopicsResponse(BaseResponse):
    response: "GroupsGroupTopicsResponseModel"


class GroupsGroupTypeResponseModel(enum.Enum):
    GROUP = "group"

    PAGE = "page"

    EVENT = "event"


class GroupsGroupTypeResponse(BaseResponse):
    response: "GroupsGroupTypeResponseModel"


class GroupsGroupVideoResponseModel(enum.IntEnum):
    DISABLED = 0

    OPEN = 1

    LIMITED = 2


class GroupsGroupVideoResponse(BaseResponse):
    response: "GroupsGroupVideoResponseModel"


class GroupsGroupWallResponseModel(enum.IntEnum):
    DISABLED = 0

    OPEN = 1

    LIMITED = 2

    CLOSED = 3


class GroupsGroupWallResponse(BaseResponse):
    response: "GroupsGroupWallResponseModel"


class GroupsGroupWikiResponseModel(enum.IntEnum):
    DISABLED = 0

    OPEN = 1

    LIMITED = 2


class GroupsGroupWikiResponse(BaseResponse):
    response: "GroupsGroupWikiResponseModel"


class GroupsGroupsArrayResponseModel(BaseModel):
    count: int = Field(
        description="Communities number",
    )

    items: typing.List[int] = Field()


class GroupsGroupsArrayResponse(BaseResponse):
    response: "GroupsGroupsArrayResponseModel"


class GroupsLinksItemResponseModel(BaseModel):
    name: typing.Optional[str] = Field(
        default=None,
        description="Link title",
    )

    desc: typing.Optional[str] = Field(
        default=None,
        description="Link description",
    )

    edit_title: typing.Optional[bool] = Field(
        default=None,
        description="Information whether the link title can be edited",
    )

    id: typing.Optional[int] = Field(
        default=None,
        description="Link ID",
    )

    photo_100: typing.Optional[str] = Field(
        default=None,
        description="URL of square image of the link with 100 pixels in width",
    )

    photo_50: typing.Optional[str] = Field(
        default=None,
        description="URL of square image of the link with 50 pixels in width",
    )

    url: typing.Optional[str] = Field(
        default=None,
        description="Link URL",
    )

    image_processing: typing.Optional[bool] = Field(
        default=None,
        description="Information whether the image on processing",
    )


class GroupsLinksItemResponse(BaseResponse):
    response: "GroupsLinksItemResponseModel"


class GroupsLiveCoversResponseModel(BaseModel):
    is_enabled: bool = Field(
        description="Information whether live covers is enabled",
    )

    is_scalable: typing.Optional[bool] = Field(
        default=None,
        description="Information whether live covers photo scaling is enabled",
    )

    story_ids: typing.Optional[typing.List[str]] = Field(
        default=None,
    )


class GroupsLiveCoversResponse(BaseResponse):
    response: "GroupsLiveCoversResponseModel"


class GroupsLongPollEventsResponseModel(BaseModel):
    audio_new: bool = Field()

    board_post_delete: bool = Field()

    board_post_edit: bool = Field()

    board_post_new: bool = Field()

    board_post_restore: bool = Field()

    group_change_photo: bool = Field()

    group_change_settings: bool = Field()

    group_join: bool = Field()

    group_leave: bool = Field()

    group_officers_edit: bool = Field()

    market_comment_delete: bool = Field()

    market_comment_edit: bool = Field()

    market_comment_new: bool = Field()

    market_comment_restore: bool = Field()

    message_allow: bool = Field()

    message_deny: bool = Field()

    message_new: bool = Field()

    message_read: bool = Field()

    message_reply: bool = Field()

    message_typing_state: bool = Field()

    message_edit: bool = Field()

    photo_comment_delete: bool = Field()

    photo_comment_edit: bool = Field()

    photo_comment_new: bool = Field()

    photo_comment_restore: bool = Field()

    photo_new: bool = Field()

    poll_vote_new: bool = Field()

    user_block: bool = Field()

    user_unblock: bool = Field()

    video_comment_delete: bool = Field()

    video_comment_edit: bool = Field()

    video_comment_new: bool = Field()

    video_comment_restore: bool = Field()

    video_new: bool = Field()

    message_reaction_event: bool = Field()

    wall_post_new: bool = Field()

    wall_reply_delete: bool = Field()

    wall_reply_edit: bool = Field()

    wall_reply_new: bool = Field()

    wall_reply_restore: bool = Field()

    wall_repost: bool = Field()

    donut_subscription_create: bool = Field()

    donut_subscription_prolonged: bool = Field()

    donut_subscription_cancelled: bool = Field()

    donut_subscription_expired: bool = Field()

    donut_subscription_price_changed: bool = Field()

    donut_money_withdraw: bool = Field()

    donut_money_withdraw_error: bool = Field()

    lead_forms_new: typing.Optional[bool] = Field(
        default=None,
    )

    market_order_new: typing.Optional[bool] = Field(
        default=None,
    )

    market_order_edit: typing.Optional[bool] = Field(
        default=None,
    )


class GroupsLongPollEventsResponse(BaseResponse):
    response: "GroupsLongPollEventsResponseModel"


class GroupsLongPollServerResponseModel(BaseModel):
    key: str = Field(
        description="Long Poll key",
    )

    server: str = Field(
        description="Long Poll server address",
    )

    ts: str = Field(
        description="Number of the last event",
    )


class GroupsLongPollServerResponse(BaseResponse):
    response: "GroupsLongPollServerResponseModel"


class GroupsLongPollSettingsResponseModel(BaseModel):
    events: "GroupsLongPollEvents" = Field()

    is_enabled: bool = Field(
        description="Shows whether Long Poll is enabled",
    )

    api_version: typing.Optional[str] = Field(
        default=None,
        description="API version used for the events",
    )


class GroupsLongPollSettingsResponse(BaseResponse):
    response: "GroupsLongPollSettingsResponseModel"


class GroupsMarketInfoResponseModel(BaseModel):
    type: typing.Optional[str] = Field(
        default=None,
        description="Market type",
    )

    contact_id: typing.Optional[int] = Field(
        default=None,
        description="Contact person ID",
    )

    currency: typing.Optional["MarketCurrency"] = Field(
        default=None,
    )

    currency_text: typing.Optional[str] = Field(
        default=None,
        description="Currency name",
    )

    is_show_header_items_link: typing.Optional[bool] = Field(
        default=None,
        description="Shop header items link is enabled",
    )

    enabled: typing.Optional[bool] = Field(
        default=None,
        description="Information whether the market is enabled",
    )

    main_album_id: typing.Optional[int] = Field(
        default=None,
        description="Main market album ID",
    )

    price_max: typing.Optional[str] = Field(
        default=None,
        description="Maximum price",
    )

    price_min: typing.Optional[str] = Field(
        default=None,
        description="Minimum price",
    )

    min_order_price: typing.Optional["MarketPrice"] = Field(
        default=None,
    )


class GroupsMarketInfoResponse(BaseResponse):
    response: "GroupsMarketInfoResponseModel"


class GroupsMarketPropertiesResponseModel(BaseModel):
    market: typing.Optional["GroupsMarketInfo"] = Field(
        default=None,
    )

    has_market_app: typing.Optional[bool] = Field(
        default=None,
        description="Information whether community has installed market app",
    )

    using_vkpay_market_app: typing.Optional[bool] = Field(
        default=None,
    )


class GroupsMarketPropertiesResponse(BaseResponse):
    response: "GroupsMarketPropertiesResponseModel"


class GroupsMarketStateResponseModel(enum.Enum):
    NONE = "none"

    BASIC = "basic"

    ADVANCED = "advanced"


class GroupsMarketStateResponse(BaseResponse):
    response: "GroupsMarketStateResponseModel"


class GroupsMemberRoleResponseModel(BaseModel):
    id: int = Field(
        description="User ID",
    )

    is_call_operator: typing.Optional[bool] = Field(
        default=None,
        description="Allow the manager to accept community calls.",
    )

    permissions: typing.Optional[typing.List[GroupsMemberRolePermission]] = Field(
        default=None,
    )

    role: typing.Optional["GroupsMemberRoleStatus"] = Field(
        default=None,
    )


class GroupsMemberRoleResponse(BaseResponse):
    response: "GroupsMemberRoleResponseModel"


class GroupsMemberRolePermissionResponseModel(enum.Enum):
    ADS = "ads"


class GroupsMemberRolePermissionResponse(BaseResponse):
    response: "GroupsMemberRolePermissionResponseModel"


class GroupsMemberRoleStatusResponseModel(enum.Enum):
    MODERATOR = "moderator"

    EDITOR = "editor"

    ADMINISTRATOR = "administrator"

    CREATOR = "creator"

    ADVERTISER = "advertiser"


class GroupsMemberRoleStatusResponse(BaseResponse):
    response: "GroupsMemberRoleStatusResponseModel"


class GroupsMemberStatusResponseModel(BaseModel):
    member: bool = Field(
        description="Information whether user is a member of the group",
    )

    user_id: int = Field(
        description="User ID",
    )


class GroupsMemberStatusResponse(BaseResponse):
    response: "GroupsMemberStatusResponseModel"


class GroupsMemberStatusFullResponseModel(BaseModel):
    member: bool = Field(
        description="Information whether user is a member of the group",
    )

    user_id: int = Field(
        description="User ID",
    )

    can_invite: typing.Optional[bool] = Field(
        default=None,
        description="Information whether user can be invited",
    )

    can_recall: typing.Optional[bool] = Field(
        default=None,
        description="Information whether user's invite to the group can be recalled",
    )

    invitation: typing.Optional[bool] = Field(
        default=None,
        description="Information whether user has been invited to the group",
    )

    request: typing.Optional[bool] = Field(
        default=None,
        description="Information whether user has send request to the group",
    )


class GroupsMemberStatusFullResponse(BaseResponse):
    response: "GroupsMemberStatusFullResponseModel"


class GroupsOnlineStatusResponseModel(BaseModel):
    status: "GroupsOnlineStatusType" = Field()

    minutes: typing.Optional[int] = Field(
        default=None,
        description="Estimated time of answer (for status = answer_mark)",
    )


class GroupsOnlineStatusResponse(BaseResponse):
    response: "GroupsOnlineStatusResponseModel"


class GroupsOnlineStatusTypeResponseModel(enum.Enum):
    NONE = "none"

    ONLINE = "online"

    ANSWER_MARK = "answer_mark"


class GroupsOnlineStatusTypeResponse(BaseResponse):
    response: "GroupsOnlineStatusTypeResponseModel"


class GroupsOwnerXtrBanInfoResponseModel(BaseModel):
    ban_info: typing.Optional["GroupsBanInfo"] = Field(
        default=None,
    )

    group: typing.Optional["GroupsGroup"] = Field(
        default=None,
        description="Information about group if type = group",
    )

    profile: typing.Optional["UsersUser"] = Field(
        default=None,
        description="Information about group if type = profile",
    )

    type: typing.Optional["GroupsOwnerXtrBanInfoType"] = Field(
        default=None,
    )


class GroupsOwnerXtrBanInfoResponse(BaseResponse):
    response: "GroupsOwnerXtrBanInfoResponseModel"


class GroupsOwnerXtrBanInfoTypeResponseModel(enum.Enum):
    GROUP = "group"

    PROFILE = "profile"


class GroupsOwnerXtrBanInfoTypeResponse(BaseResponse):
    response: "GroupsOwnerXtrBanInfoTypeResponseModel"


class GroupsPhotoSizeResponseModel(BaseModel):
    height: int = Field(
        description="Image height",
    )

    width: int = Field(
        description="Image width",
    )


class GroupsPhotoSizeResponse(BaseResponse):
    response: "GroupsPhotoSizeResponseModel"


class GroupsProfileItemResponseModel(BaseModel):
    id: int = Field(
        description="User id",
    )

    photo_50: str = Field(
        description="Url for user photo",
    )

    photo_100: str = Field(
        description="Url for user photo",
    )

    first_name: str = Field(
        description="User first name",
    )


class GroupsProfileItemResponse(BaseResponse):
    response: "GroupsProfileItemResponseModel"


class GroupsRoleOptionsResponseModel(enum.Enum):
    MODERATOR = "moderator"

    EDITOR = "editor"

    ADMINISTRATOR = "administrator"

    CREATOR = "creator"


class GroupsRoleOptionsResponse(BaseResponse):
    response: "GroupsRoleOptionsResponseModel"


class GroupsSectionsListItemResponseModel(BaseModel):
    pass


class GroupsSectionsListItemResponse(BaseResponse):
    response: "GroupsSectionsListItemResponseModel"


class GroupsSettingsTwitterResponseModel(BaseModel):
    status: typing.Literal["loading", "sync"] = Field()

    name: typing.Optional[str] = Field(
        default=None,
    )


class GroupsSettingsTwitterResponse(BaseResponse):
    response: "GroupsSettingsTwitterResponseModel"


class GroupsSubjectItemResponseModel(BaseModel):
    id: int = Field(
        description="Subject ID",
    )

    name: str = Field(
        description="Subject title",
    )


class GroupsSubjectItemResponse(BaseResponse):
    response: "GroupsSubjectItemResponseModel"


class GroupsTokenPermissionSettingResponseModel(BaseModel):
    name: str = Field()

    setting: int = Field()


class GroupsTokenPermissionSettingResponse(BaseResponse):
    response: "GroupsTokenPermissionSettingResponseModel"


class GroupsUserXtrRoleResponseModel(UsersUserFull):
    permissions: typing.Optional[typing.List[GroupsMemberRolePermission]] = Field(
        default=None,
    )

    role: typing.Optional["GroupsRoleOptions"] = Field(
        default=None,
    )


class GroupsUserXtrRoleResponse(BaseResponse):
    response: "GroupsUserXtrRoleResponseModel"
