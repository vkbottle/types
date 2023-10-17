import typing
import enum
from vkbottle_types.responses.base_response import BaseResponse, BaseModel
from vkbottle_types.base_model import Field

from vkbottle_types.objects import (
    UsersExports,
    BaseCropPhoto,
    FriendsRequestsMutual,
    UsersMilitary,
    UsersUserType,
    UsersUserRelation,
    UsersUserMin,
    PhotosPhotoFalseable,
    VideoLiveInfo,
    BaseCountry,
    UsersUserConnections,
    AppsAppMin,
    FriendsFriendStatusStatus,
    UsersPersonal,
    BaseCity,
    PhotosPhoto,
    UsersOnlineInfo,
    UsersOccupation,
    AccountUserSettingsInterests,
    DatabaseLanguageFull,
    UsersUserCounters,
    UsersUniversity,
    UsersRelative,
    UsersSchool,
    OwnerState,
    BaseSex,
    UsersCareer,
    UsersLastSeen,
    BaseBoolInt,
    AccountNameRequest,
    AudioAudio,
)


class UsersCareerResponseModel(BaseModel):
    city_id: typing.Optional[int] = Field(
        default=None,
        description="City ID",
    )

    city_name: typing.Optional[str] = Field(
        default=None,
        description="City name",
    )

    company: typing.Optional[str] = Field(
        default=None,
        description="Company name",
    )

    country_id: typing.Optional[int] = Field(
        default=None,
        description="Country ID",
    )

    _from: typing.Optional[int] = Field(
        default=None,
        description="From year",
        alias="from",
    )

    group_id: typing.Optional[int] = Field(
        default=None,
        description="Community ID",
    )

    id: typing.Optional[int] = Field(
        default=None,
        description="Career ID",
    )

    position: typing.Optional[str] = Field(
        default=None,
        description="Position",
    )

    until: typing.Optional[int] = Field(
        default=None,
        description="Till year",
    )


class UsersCareerResponse(BaseResponse):
    response: "UsersCareerResponseModel"


class UsersExportsResponseModel(BaseModel):
    facebook: typing.Optional[int] = Field(
        default=None,
    )

    livejournal: typing.Optional[int] = Field(
        default=None,
    )

    twitter: typing.Optional[int] = Field(
        default=None,
    )


class UsersExportsResponse(BaseResponse):
    response: "UsersExportsResponseModel"


class UsersFieldsResponseModel(enum.Enum):
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

    COUNTRY = "country"

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

    IS_ESIA_VERIFIED = "is_esia_verified"

    IS_ESIA_LINKED = "is_esia_linked"

    IS_TINKOFF_LINKED = "is_tinkoff_linked"

    IS_TINKOFF_VERIFIED = "is_tinkoff_verified"

    IS_SBER_VERIFIED = "is_sber_verified"

    OAUTH_LINKED = "oauth_linked"

    OAUTH_VERIFICATION = "oauth_verification"

    IS_SBER_LINKED = "is_sber_linked"


class UsersFieldsResponse(BaseResponse):
    response: "UsersFieldsResponseModel"


class UsersLastSeenResponseModel(BaseModel):
    platform: typing.Optional[int] = Field(
        default=None,
        description="Type of the platform that used for the last authorization",
    )

    time: typing.Optional[int] = Field(
        default=None,
        description="Last visit date (in Unix time)",
    )


class UsersLastSeenResponse(BaseResponse):
    response: "UsersLastSeenResponseModel"


class UsersMilitaryResponseModel(BaseModel):
    country_id: int = Field(
        description="Country ID",
    )

    unit: str = Field(
        description="Unit name",
    )

    unit_id: int = Field(
        description="Unit ID",
    )

    _from: typing.Optional[int] = Field(
        default=None,
        description="From year",
        alias="from",
    )

    id: typing.Optional[int] = Field(
        default=None,
        description="Military ID",
    )

    until: typing.Optional[int] = Field(
        default=None,
        description="Till year",
    )


class UsersMilitaryResponse(BaseResponse):
    response: "UsersMilitaryResponseModel"


class UsersOccupationResponseModel(BaseModel):
    id: typing.Optional[int] = Field(
        default=None,
        description="ID of school, university, company group",
    )

    name: typing.Optional[str] = Field(
        default=None,
        description="Name of occupation",
    )

    type: typing.Optional[typing.Literal["school", "university", "work"]] = Field(
        default=None,
        description="Type of occupation",
    )

    graduate_year: typing.Optional[int] = Field(
        default=None,
    )

    country_id: typing.Optional[int] = Field(
        default=None,
    )

    city_id: typing.Optional[int] = Field(
        default=None,
    )


class UsersOccupationResponse(BaseResponse):
    response: "UsersOccupationResponseModel"


class UsersOnlineInfoResponseModel(BaseModel):
    visible: bool = Field(
        description="Whether you can see real online status of user or not",
    )

    last_seen: typing.Optional[int] = Field(
        default=None,
        description="Last time we saw user being active",
    )

    is_online: typing.Optional[bool] = Field(
        default=None,
        description="Whether user is currently online or not",
    )

    app_id: typing.Optional[int] = Field(
        default=None,
        description="Application id from which user is currently online or was last seen online",
    )

    is_mobile: typing.Optional[bool] = Field(
        default=None,
        description="Is user online from desktop app or mobile app",
    )

    status: typing.Optional[
        typing.Literal["recently", "last_week", "last_month", "long_ago", "not_show"]
    ] = Field(
        default=None,
        description="In case user online is not visible, it indicates approximate timeframe of user online",
    )


class UsersOnlineInfoResponse(BaseResponse):
    response: "UsersOnlineInfoResponseModel"


class UsersPersonalResponseModel(BaseModel):
    alcohol: typing.Optional[int] = Field(
        default=None,
        description="User's views on alcohol",
    )

    inspired_by: typing.Optional[str] = Field(
        default=None,
        description="User's inspired by",
    )

    langs: typing.Optional[typing.List[str]] = Field(
        default=None,
    )

    langs_full: typing.Optional[typing.List[DatabaseLanguageFull]] = Field(
        default=None,
        description="User's languages with full info",
    )

    life_main: typing.Optional[int] = Field(
        default=None,
        description="User's personal priority in life",
    )

    people_main: typing.Optional[int] = Field(
        default=None,
        description="User's personal priority in people",
    )

    political: typing.Optional[int] = Field(
        default=None,
        description="User's political views",
    )

    religion: typing.Optional[str] = Field(
        default=None,
        description="User's religion",
    )

    religion_id: typing.Optional[int] = Field(
        default=None,
        description="User's religion id",
    )

    smoking: typing.Optional[int] = Field(
        default=None,
        description="User's views on smoking",
    )


class UsersPersonalResponse(BaseResponse):
    response: "UsersPersonalResponseModel"


class UsersRelativeResponseModel(BaseModel):
    type: typing.Literal[
        "parent", "child", "grandparent", "grandchild", "sibling"
    ] = Field(
        description="Relative type",
    )

    birth_date: typing.Optional[str] = Field(
        default=None,
        description="Date of child birthday (format dd.mm.yyyy)",
    )

    id: typing.Optional[int] = Field(
        default=None,
        description="Relative ID",
    )

    name: typing.Optional[str] = Field(
        default=None,
        description="Name of relative",
    )


class UsersRelativeResponse(BaseResponse):
    response: "UsersRelativeResponseModel"


class UsersSchoolResponseModel(BaseModel):
    city: typing.Optional[int] = Field(
        default=None,
        description="City ID",
    )

    _class: typing.Optional[str] = Field(
        default=None,
        description="School class letter",
        alias="class",
    )

    class_id: typing.Optional[int] = Field(
        default=None,
        description="School class id",
    )

    country: typing.Optional[int] = Field(
        default=None,
        description="Country ID",
    )

    id: typing.Optional[str] = Field(
        default=None,
        description="School ID",
    )

    name: typing.Optional[str] = Field(
        default=None,
        description="School name",
    )

    type: typing.Optional[int] = Field(
        default=None,
        description="School type ID",
    )

    type_str: typing.Optional[str] = Field(
        default=None,
        description="School type name",
    )

    year_from: typing.Optional[int] = Field(
        default=None,
        description="Year the user started to study",
    )

    year_graduated: typing.Optional[int] = Field(
        default=None,
        description="Graduation year",
    )

    year_to: typing.Optional[int] = Field(
        default=None,
        description="Year the user finished to study",
    )

    speciality: typing.Optional[str] = Field(
        default=None,
    )


class UsersSchoolResponse(BaseResponse):
    response: "UsersSchoolResponseModel"


class UsersSubscriptionsItemResponseModel(BaseModel):
    pass


class UsersSubscriptionsItemResponse(BaseResponse):
    response: "UsersSubscriptionsItemResponseModel"


class UsersUniversityResponseModel(BaseModel):
    chair: typing.Optional[int] = Field(
        default=None,
        description="Chair ID",
    )

    chair_name: typing.Optional[str] = Field(
        default=None,
        description="Chair name",
    )

    city: typing.Optional[int] = Field(
        default=None,
        description="City ID",
    )

    country: typing.Optional[int] = Field(
        default=None,
        description="Country ID",
    )

    education_form: typing.Optional[str] = Field(
        default=None,
        description="Education form",
    )

    education_form_id: typing.Optional[int] = Field(
        default=None,
        description="Education form id",
    )

    education_status: typing.Optional[str] = Field(
        default=None,
        description="Education status",
    )

    education_status_id: typing.Optional[int] = Field(
        default=None,
        description="Education status id",
    )

    faculty: typing.Optional[int] = Field(
        default=None,
        description="Faculty ID",
    )

    faculty_name: typing.Optional[str] = Field(
        default=None,
        description="Faculty name",
    )

    graduation: typing.Optional[int] = Field(
        default=None,
        description="Graduation year",
    )

    id: typing.Optional[int] = Field(
        default=None,
        description="University ID",
    )

    name: typing.Optional[str] = Field(
        default=None,
        description="University name",
    )

    university_group_id: typing.Optional[int] = Field(
        default=None,
    )


class UsersUniversityResponse(BaseResponse):
    response: "UsersUniversityResponseModel"


class UsersUserResponseModel(UsersUserMin):
    sex: typing.Optional["BaseSex"] = Field(
        default=None,
        description="User sex",
    )

    screen_name: typing.Optional[str] = Field(
        default=None,
        description="Domain name of the user's page",
    )

    photo_50: typing.Optional[str] = Field(
        default=None,
        description="URL of square photo of the user with 50 pixels in width",
    )

    photo_100: typing.Optional[str] = Field(
        default=None,
        description="URL of square photo of the user with 100 pixels in width",
    )

    online_info: typing.Optional["UsersOnlineInfo"] = Field(
        default=None,
    )

    online: typing.Optional[bool] = Field(
        default=None,
        description="Information whether the user is online",
    )

    online_mobile: typing.Optional[bool] = Field(
        default=None,
        description="Information whether the user is online in mobile site or application",
    )

    online_app: typing.Optional[int] = Field(
        default=None,
        description="Application ID",
    )

    verified: typing.Optional[bool] = Field(
        default=None,
        description="Information whether the user is verified",
    )

    trending: typing.Optional[bool] = Field(
        default=None,
        description='Information whether the user has a "fire" pictogram.',
    )

    friend_status: typing.Optional["FriendsFriendStatusStatus"] = Field(
        default=None,
    )

    mutual: typing.Optional["FriendsRequestsMutual"] = Field(
        default=None,
    )


class UsersUserResponse(BaseResponse):
    response: "UsersUserResponseModel"


class UsersUserConnectionsResponseModel(BaseModel):
    skype: str = Field(
        description="User's Skype nickname",
    )

    facebook: str = Field(
        description="User's Facebook account",
    )

    twitter: str = Field(
        description="User's Twitter account",
    )

    instagram: str = Field(
        description="User's Instagram account",
    )

    facebook_name: typing.Optional[str] = Field(
        default=None,
        description="User's Facebook name",
    )

    livejournal: typing.Optional[str] = Field(
        default=None,
        description="User's Livejournal account",
    )


class UsersUserConnectionsResponse(BaseResponse):
    response: "UsersUserConnectionsResponseModel"


class UsersUserCountersResponseModel(BaseModel):
    albums: typing.Optional[int] = Field(
        default=None,
        description="Albums number",
    )

    badges: typing.Optional[int] = Field(
        default=None,
        description="Badges number",
    )

    audios: typing.Optional[int] = Field(
        default=None,
        description="Audios number",
    )

    followers: typing.Optional[int] = Field(
        default=None,
        description="Followers number",
    )

    friends: typing.Optional[int] = Field(
        default=None,
        description="Friends number",
    )

    gifts: typing.Optional[int] = Field(
        default=None,
        description="Gifts number",
    )

    groups: typing.Optional[int] = Field(
        default=None,
        description="Communities number",
    )

    notes: typing.Optional[int] = Field(
        default=None,
        description="Notes number",
    )

    online_friends: typing.Optional[int] = Field(
        default=None,
        description="Online friends number",
    )

    pages: typing.Optional[int] = Field(
        default=None,
        description="Public pages number",
    )

    photos: typing.Optional[int] = Field(
        default=None,
        description="Photos number",
    )

    subscriptions: typing.Optional[int] = Field(
        default=None,
        description="Subscriptions number",
    )

    user_photos: typing.Optional[int] = Field(
        default=None,
        description="Number of photos with user",
    )

    user_videos: typing.Optional[int] = Field(
        default=None,
        description="Number of videos with user",
    )

    videos: typing.Optional[int] = Field(
        default=None,
        description="Videos number",
    )

    video_playlists: typing.Optional[int] = Field(
        default=None,
        description="Playlists number",
    )

    new_photo_tags: typing.Optional[int] = Field(
        default=None,
    )

    new_recognition_tags: typing.Optional[int] = Field(
        default=None,
    )

    mutual_friends: typing.Optional[int] = Field(
        default=None,
    )

    friends_followers: typing.Optional[int] = Field(
        default=None,
    )

    posts: typing.Optional[int] = Field(
        default=None,
    )

    articles: typing.Optional[int] = Field(
        default=None,
    )

    wishes: typing.Optional[int] = Field(
        default=None,
    )

    podcasts: typing.Optional[int] = Field(
        default=None,
    )

    clips: typing.Optional[int] = Field(
        default=None,
    )

    clips_followers: typing.Optional[int] = Field(
        default=None,
    )

    videos_followers: typing.Optional[int] = Field(
        default=None,
        description="Videos followers number",
    )

    clips_views: typing.Optional[int] = Field(
        default=None,
    )

    clips_likes: typing.Optional[int] = Field(
        default=None,
    )


class UsersUserCountersResponse(BaseResponse):
    response: "UsersUserCountersResponseModel"


class UsersUserFullResponseModel(UsersUser):
    first_name_nom: typing.Optional[str] = Field(
        default=None,
        description="User's first name in nominative case",
    )

    first_name_gen: typing.Optional[str] = Field(
        default=None,
        description="User's first name in genitive case",
    )

    first_name_dat: typing.Optional[str] = Field(
        default=None,
        description="User's first name in dative case",
    )

    first_name_acc: typing.Optional[str] = Field(
        default=None,
        description="User's first name in accusative case",
    )

    first_name_ins: typing.Optional[str] = Field(
        default=None,
        description="User's first name in instrumental case",
    )

    first_name_abl: typing.Optional[str] = Field(
        default=None,
        description="User's first name in prepositional case",
    )

    last_name_nom: typing.Optional[str] = Field(
        default=None,
        description="User's last name in nominative case",
    )

    last_name_gen: typing.Optional[str] = Field(
        default=None,
        description="User's last name in genitive case",
    )

    last_name_dat: typing.Optional[str] = Field(
        default=None,
        description="User's last name in dative case",
    )

    last_name_acc: typing.Optional[str] = Field(
        default=None,
        description="User's last name in accusative case",
    )

    last_name_ins: typing.Optional[str] = Field(
        default=None,
        description="User's last name in instrumental case",
    )

    last_name_abl: typing.Optional[str] = Field(
        default=None,
        description="User's last name in prepositional case",
    )

    nickname: typing.Optional[str] = Field(
        default=None,
        description="User nickname",
    )

    maiden_name: typing.Optional[str] = Field(
        default=None,
        description="User maiden name",
    )

    contact_name: typing.Optional[str] = Field(
        default=None,
        description="User contact name",
    )

    domain: typing.Optional[str] = Field(
        default=None,
        description="Domain name of the user's page",
    )

    bdate: typing.Optional[str] = Field(
        default=None,
        description="User's date of birth",
    )

    city: typing.Optional["BaseCity"] = Field(
        default=None,
    )

    country: typing.Optional["BaseCountry"] = Field(
        default=None,
    )

    timezone: typing.Optional[float] = Field(
        default=None,
        description="User's timezone",
    )

    owner_state: typing.Optional["OwnerState"] = Field(
        default=None,
    )

    photo_200: typing.Optional[str] = Field(
        default=None,
        description="URL of square photo of the user with 200 pixels in width",
    )

    photo_max: typing.Optional[str] = Field(
        default=None,
        description="URL of square photo of the user with maximum width",
    )

    photo_200_orig: typing.Optional[str] = Field(
        default=None,
        description="URL of user's photo with 200 pixels in width",
    )

    photo_400_orig: typing.Optional[str] = Field(
        default=None,
        description="URL of user's photo with 400 pixels in width",
    )

    photo_max_orig: typing.Optional[str] = Field(
        default=None,
        description="URL of user's photo of maximum size",
    )

    photo_id: typing.Optional[str] = Field(
        default=None,
        description="ID of the user's main photo",
    )

    has_photo: typing.Optional[bool] = Field(
        default=None,
        description="Information whether the user has main photo",
    )

    has_mobile: typing.Optional[bool] = Field(
        default=None,
        description="Information whether the user specified his phone number",
    )

    is_friend: typing.Optional[bool] = Field(
        default=None,
        description="Information whether the user is a friend of current user",
    )

    is_best_friend: typing.Optional[bool] = Field(
        default=None,
        description="Information whether the user is a best friend of current user",
    )

    wall_comments: typing.Optional[bool] = Field(
        default=None,
        description="Information whether current user can comment wall posts",
    )

    can_post: typing.Optional[bool] = Field(
        default=None,
        description="Information whether current user can post on the user's wall",
    )

    can_see_all_posts: typing.Optional[bool] = Field(
        default=None,
        description="Information whether current user can see other users' audio on the wall",
    )

    can_see_audio: typing.Optional[bool] = Field(
        default=None,
        description="Information whether current user can see the user's audio",
    )

    type: typing.Optional["UsersUserType"] = Field(
        default=None,
    )

    email: typing.Optional[str] = Field(
        default=None,
    )

    skype: typing.Optional[str] = Field(
        default=None,
    )

    facebook: typing.Optional[str] = Field(
        default=None,
    )

    facebook_name: typing.Optional[str] = Field(
        default=None,
    )

    twitter: typing.Optional[str] = Field(
        default=None,
    )

    livejournal: typing.Optional[str] = Field(
        default=None,
    )

    instagram: typing.Optional[str] = Field(
        default=None,
    )

    test: typing.Optional[bool] = Field(
        default=None,
    )

    video_live: typing.Optional["VideoLiveInfo"] = Field(
        default=None,
    )

    is_video_live_notifications_blocked: typing.Optional[bool] = Field(
        default=None,
    )

    is_service: typing.Optional[bool] = Field(
        default=None,
    )

    service_description: typing.Optional[str] = Field(
        default=None,
    )

    photo_rec: typing.Optional["PhotosPhotoFalseable"] = Field(
        default=None,
    )

    photo_medium: typing.Optional["PhotosPhotoFalseable"] = Field(
        default=None,
    )

    photo_medium_rec: typing.Optional["PhotosPhotoFalseable"] = Field(
        default=None,
    )

    photo: typing.Optional[str] = Field(
        default=None,
    )

    photo_big: typing.Optional[str] = Field(
        default=None,
    )

    photo_400: typing.Optional[str] = Field(
        default=None,
    )

    photo_max_size: typing.Optional["PhotosPhoto"] = Field(
        default=None,
    )

    language: typing.Optional[str] = Field(
        default=None,
    )

    stories_archive_count: typing.Optional[int] = Field(
        default=None,
    )

    has_unseen_stories: typing.Optional[bool] = Field(
        default=None,
    )

    wall_default: typing.Optional[str] = Field(
        default=None,
    )

    can_call: typing.Optional[bool] = Field(
        default=None,
        description="Information whether current user can call",
    )

    can_call_from_group: typing.Optional[bool] = Field(
        default=None,
        description="Information whether group can call user",
    )

    can_see_wishes: typing.Optional[bool] = Field(
        default=None,
        description="Information whether current user can see the user's wishes",
    )

    can_see_gifts: typing.Optional[bool] = Field(
        default=None,
        description="Information whether current user can see the user's gifts",
    )

    interests: typing.Optional[str] = Field(
        default=None,
    )

    books: typing.Optional[str] = Field(
        default=None,
    )

    tv: typing.Optional[str] = Field(
        default=None,
    )

    quotes: typing.Optional[str] = Field(
        default=None,
    )

    about: typing.Optional[str] = Field(
        default=None,
    )

    games: typing.Optional[str] = Field(
        default=None,
    )

    movies: typing.Optional[str] = Field(
        default=None,
    )

    activities: typing.Optional[str] = Field(
        default=None,
    )

    music: typing.Optional[str] = Field(
        default=None,
    )

    can_write_private_message: typing.Optional[bool] = Field(
        default=None,
        description="Information whether current user can write private message",
    )

    can_send_friend_request: typing.Optional[bool] = Field(
        default=None,
        description="Information whether current user can send a friend request",
    )

    can_be_invited_group: typing.Optional[bool] = Field(
        default=None,
        description="Information whether current user can be invited to the community",
    )

    mobile_phone: typing.Optional[str] = Field(
        default=None,
        description="User's mobile phone number",
    )

    home_phone: typing.Optional[str] = Field(
        default=None,
        description="User's additional phone number",
    )

    site: typing.Optional[str] = Field(
        default=None,
        description="User's website",
    )

    status_audio: typing.Optional["AudioAudio"] = Field(
        default=None,
    )

    status: typing.Optional[str] = Field(
        default=None,
        description="User's status",
    )

    activity: typing.Optional[str] = Field(
        default=None,
        description="User's status",
    )

    status_app: typing.Optional["AppsAppMin"] = Field(
        default=None,
    )

    last_seen: typing.Optional["UsersLastSeen"] = Field(
        default=None,
    )

    exports: typing.Optional["UsersExports"] = Field(
        default=None,
    )

    crop_photo: typing.Optional["BaseCropPhoto"] = Field(
        default=None,
    )

    followers_count: typing.Optional[int] = Field(
        default=None,
        description="Number of user's followers",
    )

    video_live_level: typing.Optional[int] = Field(
        default=None,
        description="User level in live streams achievements",
    )

    video_live_count: typing.Optional[int] = Field(
        default=None,
        description="Number of user's live streams",
    )

    clips_count: typing.Optional[int] = Field(
        default=None,
        description="Number of user's clips",
    )

    blacklisted: typing.Optional[bool] = Field(
        default=None,
        description="Information whether current user is in the requested user's blacklist.",
    )

    blacklisted_by_me: typing.Optional[bool] = Field(
        default=None,
        description="Information whether the requested user is in current user's blacklist",
    )

    is_favorite: typing.Optional[bool] = Field(
        default=None,
        description="Information whether the requested user is in faves of current user",
    )

    is_hidden_from_feed: typing.Optional[bool] = Field(
        default=None,
        description="Information whether the requested user is hidden from current user's newsfeed",
    )

    common_count: typing.Optional[int] = Field(
        default=None,
        description="Number of common friends with current user",
    )

    occupation: typing.Optional["UsersOccupation"] = Field(
        default=None,
    )

    career: typing.Optional[typing.List[UsersCareer]] = Field(
        default=None,
    )

    military: typing.Optional[typing.List[UsersMilitary]] = Field(
        default=None,
    )

    university: typing.Optional[int] = Field(
        default=None,
        description="University ID",
    )

    university_name: typing.Optional[str] = Field(
        default=None,
        description="University name",
    )

    university_group_id: typing.Optional[int] = Field(
        default=None,
    )

    faculty: typing.Optional[int] = Field(
        default=None,
        description="Faculty ID",
    )

    faculty_name: typing.Optional[str] = Field(
        default=None,
        description="Faculty name",
    )

    graduation: typing.Optional[int] = Field(
        default=None,
        description="Graduation year",
    )

    education_form: typing.Optional[str] = Field(
        default=None,
        description="Education form",
    )

    education_status: typing.Optional[str] = Field(
        default=None,
        description="User's education status",
    )

    home_town: typing.Optional[str] = Field(
        default=None,
        description="User hometown",
    )

    relation: typing.Optional["UsersUserRelation"] = Field(
        default=None,
        description="User relationship status",
    )

    relation_partner: typing.Optional["UsersUserMin"] = Field(
        default=None,
    )

    personal: typing.Optional["UsersPersonal"] = Field(
        default=None,
    )

    universities: typing.Optional[typing.List[UsersUniversity]] = Field(
        default=None,
    )

    schools: typing.Optional[typing.List[UsersSchool]] = Field(
        default=None,
    )

    relatives: typing.Optional[typing.List[UsersRelative]] = Field(
        default=None,
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

    counters: typing.Optional["UsersUserCounters"] = Field(
        default=None,
    )

    access_key: typing.Optional[str] = Field(
        default=None,
    )

    can_upload_doc: typing.Optional[bool] = Field(
        default=None,
    )

    can_ban: typing.Optional[bool] = Field(
        default=None,
        description="Information whether the user can be baned (added to black list) by me",
    )

    hash: typing.Optional[str] = Field(
        default=None,
    )

    is_no_index: typing.Optional[bool] = Field(
        default=None,
        description="Access to user profile is restricted for search engines",
    )

    contact_id: typing.Optional[int] = Field(
        default=None,
        description="Contact person ID",
    )

    is_message_request: typing.Optional[bool] = Field(
        default=None,
    )

    descriptions: typing.Optional[typing.List[str]] = Field(
        default=None,
    )

    lists: typing.Optional[typing.List[int]] = Field(
        default=None,
    )


class UsersUserFullResponse(BaseResponse):
    response: "UsersUserFullResponseModel"


class UsersUserMinResponseModel(BaseModel):
    id: int = Field(
        description="User ID",
    )

    deactivated: typing.Optional[str] = Field(
        default=None,
        description="Returns if a profile is deleted or blocked",
    )

    first_name: typing.Optional[str] = Field(
        default=None,
        description="User first name",
    )

    hidden: typing.Optional[int] = Field(
        default=None,
        description="Returns if a profile is hidden.",
    )

    last_name: typing.Optional[str] = Field(
        default=None,
        description="User last name",
    )

    can_access_closed: typing.Optional[bool] = Field(
        default=None,
    )

    is_closed: typing.Optional[bool] = Field(
        default=None,
    )


class UsersUserMinResponse(BaseResponse):
    response: "UsersUserMinResponseModel"


class UsersUserRelationResponseModel(enum.IntEnum):
    NOT_SPECIFIED = 0

    SINGLE = 1

    IN_A_RELATIONSHIP = 2

    ENGAGED = 3

    MARRIED = 4

    COMPLICATED = 5

    ACTIVELY_SEARCHING = 6

    IN_LOVE = 7

    IN_A_CIVIL_UNION = 8


class UsersUserRelationResponse(BaseResponse):
    response: "UsersUserRelationResponseModel"


class UsersUserSettingsXtrResponseModel(BaseModel):
    home_town: str = Field(
        description="User's hometown",
    )

    status: str = Field(
        description="User status",
    )

    connections: typing.Optional["UsersUserConnections"] = Field(
        default=None,
    )

    bdate: typing.Optional[str] = Field(
        default=None,
        description="User's date of birth",
    )

    bdate_visibility: typing.Optional[int] = Field(
        default=None,
        description="Information whether user's birthdate are hidden",
    )

    city: typing.Optional["BaseCity"] = Field(
        default=None,
    )

    country: typing.Optional["BaseCountry"] = Field(
        default=None,
    )

    first_name: typing.Optional[str] = Field(
        default=None,
        description="User first name",
    )

    last_name: typing.Optional[str] = Field(
        default=None,
        description="User last name",
    )

    maiden_name: typing.Optional[str] = Field(
        default=None,
        description="User maiden name",
    )

    name_request: typing.Optional["AccountNameRequest"] = Field(
        default=None,
    )

    personal: typing.Optional["UsersPersonal"] = Field(
        default=None,
    )

    phone: typing.Optional[str] = Field(
        default=None,
        description="User phone number with some hidden digits",
    )

    relation: typing.Optional["UsersUserRelation"] = Field(
        default=None,
        description="User relationship status",
    )

    relation_partner: typing.Optional["UsersUserMin"] = Field(
        default=None,
    )

    relation_pending: typing.Optional[bool] = Field(
        default=None,
        description="Information whether relation status is pending",
    )

    relation_requests: typing.Optional[typing.List[UsersUserMin]] = Field(
        default=None,
    )

    screen_name: typing.Optional[str] = Field(
        default=None,
        description="Domain name of the user's page",
    )

    sex: typing.Optional["BaseSex"] = Field(
        default=None,
        description="User sex",
    )

    status_audio: typing.Optional["AudioAudio"] = Field(
        default=None,
    )

    interests: typing.Optional["AccountUserSettingsInterests"] = Field(
        default=None,
    )

    languages: typing.Optional[typing.List[str]] = Field(
        default=None,
    )


class UsersUserSettingsXtrResponse(BaseResponse):
    response: "UsersUserSettingsXtrResponseModel"


class UsersUserTypeResponseModel(enum.Enum):
    PROFILE = "profile"


class UsersUserTypeResponse(BaseResponse):
    response: "UsersUserTypeResponseModel"


class UsersUserXtrTypeResponseModel(UsersUserFull):
    type: typing.Optional["UsersUserType"] = Field(
        default=None,
    )


class UsersUserXtrTypeResponse(BaseResponse):
    response: "UsersUserXtrTypeResponseModel"


class UsersUsersArrayResponseModel(BaseModel):
    count: int = Field(
        description="Users number",
    )

    items: typing.List[int] = Field()


class UsersUsersArrayResponse(BaseResponse):
    response: "UsersUsersArrayResponseModel"
