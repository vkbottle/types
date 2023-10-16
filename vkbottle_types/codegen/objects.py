import enum
import typing

from vkbottle_types.base_model import BaseModel, Field


class UsersCareer(BaseModel):
    """
    Schema: users_career
    """

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


class UsersExports(BaseModel):
    """
    Schema: users_exports
    """

    facebook: typing.Optional[int] = Field(
        default=None,
    )

    livejournal: typing.Optional[int] = Field(
        default=None,
    )

    twitter: typing.Optional[int] = Field(
        default=None,
    )


class UsersFields(enum.Enum):
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


class UsersLastSeen(BaseModel):
    """
    Schema: users_last_seen
    """

    platform: typing.Optional[int] = Field(
        default=None,
        description="Type of the platform that used for the last authorization",
    )

    time: typing.Optional[int] = Field(
        default=None,
        description="Last visit date (in Unix time)",
    )


class UsersMilitary(BaseModel):
    """
    Schema: users_military
    """

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


class UsersOccupationType(enum.Enum):
    SCHOOL = "school"
    UNIVERSITY = "university"
    WORK = "work"


class UsersOccupation(BaseModel):
    """
    Schema: users_occupation
    """

    id: typing.Optional[int] = Field(
        default=None,
        description="ID of school, university, company group",
    )

    name: typing.Optional[str] = Field(
        default=None,
        description="Name of occupation",
    )

    type: typing.Optional["UsersOccupationType"] = Field(
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


class UsersOnlineInfoStatus(enum.Enum):
    RECENTLY = "recently"
    LAST_WEEK = "last_week"
    LAST_MONTH = "last_month"
    LONG_AGO = "long_ago"
    NOT_SHOW = "not_show"


class UsersOnlineInfo(BaseModel):
    """
    Schema: users_online_info
    """

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

    status: typing.Optional["UsersOnlineInfoStatus"] = Field(
        default=None,
        description="In case user online is not visible, it indicates approximate timeframe of user online",
    )


class UsersPersonal(BaseModel):
    """
    Schema: users_personal
    """

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

    langs_full: typing.Optional[typing.List["DatabaseLanguageFull"]] = Field(
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


class UsersRelativeType(enum.Enum):
    PARENT = "parent"
    CHILD = "child"
    GRANDPARENT = "grandparent"
    GRANDCHILD = "grandchild"
    SIBLING = "sibling"


class UsersRelative(BaseModel):
    """
    Schema: users_relative
    """

    type: "UsersRelativeType" = Field(
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


class UsersSchool(BaseModel):
    """
    Schema: users_school
    """

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


class UsersSubscriptionsItem(BaseModel):
    """
    Schema: users_subscriptions_item
    """


class UsersUniversity(BaseModel):
    """
    Schema: users_university
    """

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


class UsersUserConnections(BaseModel):
    """
    Schema: users_user_connections
    """

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


class UsersUserCounters(BaseModel):
    """
    Schema: users_user_counters
    """

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


class UsersUserMin(BaseModel):
    """
    Schema: users_user_min
    """

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


class UsersUserRelation(enum.IntEnum):
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
    Schema: users_user_settings_xtr
    """

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

    relation_requests: typing.Optional[typing.List["UsersUserMin"]] = Field(
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


class UsersUserType(enum.Enum):
    PROFILE = "profile"


class UsersUsersArray(BaseModel):
    """
    Schema: users_users_array
    """

    count: int = Field(
        description="Users number",
    )

    items: typing.List[int] = Field()


class AccountAccountCounters(BaseModel):
    """
    Schema: account_account_counters
    """

    app_requests: typing.Optional[int] = Field(
        default=None,
        description="New app requests number",
    )

    events: typing.Optional[int] = Field(
        default=None,
        description="New events number",
    )

    faves: typing.Optional[int] = Field(
        default=None,
        description="New faves number",
    )

    friends: typing.Optional[int] = Field(
        default=None,
        description="New friends requests number",
    )

    friends_recommendations: typing.Optional[int] = Field(
        default=None,
        description="New friends recommendations number",
    )

    gifts: typing.Optional[int] = Field(
        default=None,
        description="New gifts number",
    )

    groups: typing.Optional[int] = Field(
        default=None,
        description="New groups number",
    )

    messages: typing.Optional[int] = Field(
        default=None,
        description="New messages number",
    )

    memories: typing.Optional[int] = Field(
        default=None,
        description="New memories number",
    )

    notes: typing.Optional[int] = Field(
        default=None,
        description="New notes number",
    )

    notifications: typing.Optional[int] = Field(
        default=None,
        description="New notifications number",
    )

    photos: typing.Optional[int] = Field(
        default=None,
        description="New photo tags number",
    )


class AccountCountersFilter(enum.Enum):
    APP_REQUESTS = "app_requests"

    EVENTS = "events"

    FRIENDS = "friends"

    FRIENDS_RECOMMENDATIONS = "friends_recommendations"

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
    Schema: account_info
    """

    _2fa_required: typing.Optional[bool] = Field(
        default=None,
        description="Two factor authentication is enabled",
        alias="2fa_required",
    )

    country: typing.Optional[str] = Field(
        default=None,
        description="Country code",
    )

    https_required: typing.Optional[bool] = Field(
        default=None,
        description="Information whether HTTPS-only is enabled",
    )

    intro: typing.Optional[bool] = Field(
        default=None,
        description="Information whether user has been processed intro",
    )

    lang: typing.Optional[int] = Field(
        default=None,
        description="Language ID",
    )

    no_wall_replies: typing.Optional[bool] = Field(
        default=None,
        description="Information whether wall comments should be hidden",
    )

    own_posts_default: typing.Optional[bool] = Field(
        default=None,
        description="Information whether only owners posts should be shown",
    )


class AccountNameRequest(BaseModel):
    """
    Schema: account_name_request
    """

    first_name: typing.Optional[str] = Field(
        default=None,
        description="First name in request",
    )

    id: typing.Optional[int] = Field(
        default=None,
        description="Request ID needed to cancel the request",
    )

    last_name: typing.Optional[str] = Field(
        default=None,
        description="Last name in request",
    )

    status: typing.Optional["AccountNameRequestStatus"] = Field(
        default=None,
    )

    lang: typing.Optional[str] = Field(
        default=None,
        description="Text to display to user",
    )

    link_href: typing.Optional[str] = Field(
        default=None,
        description="href for link in lang field",
    )

    link_label: typing.Optional[str] = Field(
        default=None,
        description="label to display for link in lang field",
    )


class AccountNameRequestStatus(enum.Enum):
    SUCCESS = "success"

    PROCESSING = "processing"

    DECLINED = "declined"

    WAS_ACCEPTED = "was_accepted"

    WAS_DECLINED = "was_declined"

    DECLINED_WITH_LINK = "declined_with_link"

    RESPONSE = "response"

    RESPONSE_WITH_LINK = "response_with_link"


class AccountOfferLinkType(enum.Enum):
    PROFILE = "profile"
    GROUP = "group"
    APP = "app"


class AccountOffer(BaseModel):
    """
    Schema: account_offer
    """

    description: typing.Optional[str] = Field(
        default=None,
        description="Offer description",
    )

    id: typing.Optional[int] = Field(
        default=None,
        description="Offer ID",
    )

    img: typing.Optional[str] = Field(
        default=None,
        description="URL of the preview image",
    )

    instruction: typing.Optional[str] = Field(
        default=None,
        description="Instruction how to process the offer",
    )

    instruction_html: typing.Optional[str] = Field(
        default=None,
        description="Instruction how to process the offer (HTML format)",
    )

    price: typing.Optional[int] = Field(
        default=None,
        description="Offer price",
    )

    short_description: typing.Optional[str] = Field(
        default=None,
        description="Offer short description",
    )

    tag: typing.Optional[str] = Field(
        default=None,
        description="Offer tag",
    )

    title: typing.Optional[str] = Field(
        default=None,
        description="Offer title",
    )

    currency_amount: typing.Optional[float] = Field(
        default=None,
        description="Currency amount",
    )

    link_id: typing.Optional[int] = Field(
        default=None,
        description="Link id",
    )

    link_type: typing.Optional["AccountOfferLinkType"] = Field(
        default=None,
        description="Link type",
    )


class AccountPushConversations(BaseModel):
    """
    Schema: account_push_conversations
    """

    count: typing.Optional[int] = Field(
        default=None,
        description="Items count",
    )

    items: typing.Optional[typing.List["AccountPushConversationsItem"]] = Field(
        default=None,
    )


class AccountPushConversationsItem(BaseModel):
    """
    Schema: account_push_conversations_item
    """

    disabled_until: int = Field(
        description="Time until that notifications are disabled in seconds",
    )

    peer_id: int = Field(
        description="Peer ID",
    )

    sound: bool = Field(
        description="Information whether the sound are enabled",
    )

    disabled_mentions: typing.Optional[bool] = Field(
        default=None,
        description="Information whether the mentions are disabled",
    )

    disabled_mass_mentions: typing.Optional[bool] = Field(
        default=None,
        description="Information whether the mass mentions (like '@all', '@online') are disabled. Can be affected by 'disabled_mentions'",
    )


class AccountPushParams(BaseModel):
    """
    Schema: account_push_params
    """

    msg: typing.Optional[typing.List["AccountPushParamsMode"]] = Field(
        default=None,
    )

    chat: typing.Optional[typing.List["AccountPushParamsMode"]] = Field(
        default=None,
    )

    like: typing.Optional[typing.List["AccountPushParamsSettings"]] = Field(
        default=None,
    )

    repost: typing.Optional[typing.List["AccountPushParamsSettings"]] = Field(
        default=None,
    )

    comment: typing.Optional[typing.List["AccountPushParamsSettings"]] = Field(
        default=None,
    )

    mention: typing.Optional[typing.List["AccountPushParamsSettings"]] = Field(
        default=None,
    )

    reply: typing.Optional[typing.List["AccountPushParamsOnoff"]] = Field(
        default=None,
    )

    new_post: typing.Optional[typing.List["AccountPushParamsOnoff"]] = Field(
        default=None,
    )

    wall_post: typing.Optional[typing.List["AccountPushParamsOnoff"]] = Field(
        default=None,
    )

    wall_publish: typing.Optional[typing.List["AccountPushParamsOnoff"]] = Field(
        default=None,
    )

    friend: typing.Optional[typing.List["AccountPushParamsOnoff"]] = Field(
        default=None,
    )

    friend_found: typing.Optional[typing.List["AccountPushParamsOnoff"]] = Field(
        default=None,
    )

    friend_accepted: typing.Optional[typing.List["AccountPushParamsOnoff"]] = Field(
        default=None,
    )

    group_invite: typing.Optional[typing.List["AccountPushParamsOnoff"]] = Field(
        default=None,
    )

    group_accepted: typing.Optional[typing.List["AccountPushParamsOnoff"]] = Field(
        default=None,
    )

    birthday: typing.Optional[typing.List["AccountPushParamsOnoff"]] = Field(
        default=None,
    )

    event_soon: typing.Optional[typing.List["AccountPushParamsOnoff"]] = Field(
        default=None,
    )

    app_request: typing.Optional[typing.List["AccountPushParamsOnoff"]] = Field(
        default=None,
    )

    sdk_open: typing.Optional[typing.List["AccountPushParamsOnoff"]] = Field(
        default=None,
    )


class AccountPushParamsMode(enum.Enum):
    ON = "on"

    OFF = "off"

    NO_SOUND = "no_sound"

    NO_TEXT = "no_text"


class AccountPushParamsOnoff(enum.Enum):
    ON = "on"

    OFF = "off"


class AccountPushParamsSettings(enum.Enum):
    ON = "on"

    OFF = "off"

    FR_OF_FR = "fr_of_fr"


class AccountPushSettings(BaseModel):
    """
    Schema: account_push_settings
    """

    disabled: typing.Optional[bool] = Field(
        default=None,
        description="Information whether notifications are disabled",
    )

    disabled_until: typing.Optional[int] = Field(
        default=None,
        description="Time until that notifications are disabled in Unixtime",
    )

    settings: typing.Optional["AccountPushParams"] = Field(
        default=None,
    )

    conversations: typing.Optional["AccountPushConversations"] = Field(
        default=None,
    )


class AccountUserSettingsInterest(BaseModel):
    """
    Schema: account_user_settings_interest
    """

    title: str = Field()

    value: str = Field()


class AccountUserSettingsInterests(BaseModel):
    """
    Schema: account_user_settings_interests
    """

    activities: typing.Optional["AccountUserSettingsInterest"] = Field(
        default=None,
    )

    interests: typing.Optional["AccountUserSettingsInterest"] = Field(
        default=None,
    )

    music: typing.Optional["AccountUserSettingsInterest"] = Field(
        default=None,
    )

    tv: typing.Optional["AccountUserSettingsInterest"] = Field(
        default=None,
    )

    movies: typing.Optional["AccountUserSettingsInterest"] = Field(
        default=None,
    )

    books: typing.Optional["AccountUserSettingsInterest"] = Field(
        default=None,
    )

    games: typing.Optional["AccountUserSettingsInterest"] = Field(
        default=None,
    )

    quotes: typing.Optional["AccountUserSettingsInterest"] = Field(
        default=None,
    )

    about: typing.Optional["AccountUserSettingsInterest"] = Field(
        default=None,
    )


class AddressesFields(enum.Enum):
    ID = "id"

    TITLE = "title"

    ADDRESS = "address"

    ADDITIONAL_ADDRESS = "additional_address"

    COUNTRY_ID = "country_id"

    CITY_ID = "city_id"

    METRO_STATION_ID = "metro_station_id"

    LATITUDE = "latitude"

    LONGITUDE = "longitude"

    DISTANCE = "distance"

    WORK_INFO_STATUS = "work_info_status"

    TIMETABLE = "timetable"

    PHONE = "phone"

    TIME_OFFSET = "time_offset"


class AdsAccessRole(enum.Enum):
    ADMIN = "admin"

    MANAGER = "manager"

    REPORTS = "reports"


class AdsAccessRolePublic(enum.Enum):
    MANAGER = "manager"

    REPORTS = "reports"


class AdsAccesses(BaseModel):
    """
    Schema: ads_accesses
    """

    client_id: typing.Optional[str] = Field(
        default=None,
        description="Client ID",
    )

    role: typing.Optional["AdsAccessRole"] = Field(
        default=None,
    )


class AdsAccount(BaseModel):
    """
    Schema: ads_account
    """

    access_role: "AdsAccessRole" = Field()

    account_id: int = Field(
        description="Account ID",
    )

    account_status: bool = Field(
        description="Information whether account is active",
    )

    account_type: "AdsAccountType" = Field()

    account_name: str = Field(
        description="Account name",
    )

    can_view_budget: bool = Field(
        description="Can user view account budget",
    )


class AdsAccountType(enum.Enum):
    GENERAL = "general"

    AGENCY = "agency"


class AdsAd(BaseModel):
    """
    Schema: ads_ad
    """

    ad_format: int = Field(
        description="Ad format",
    )

    ad_platform: typing.Union["int", "str"] = Field(
        description="Ad platform",
    )

    all_limit: str = Field(
        description="Total limit",
    )

    approved: "AdsAdApproved" = Field()

    campaign_id: int = Field(
        description="Campaign ID",
    )

    cost_type: "AdsAdCostType" = Field()

    id: int = Field(
        description="Ad ID",
    )

    name: str = Field(
        description="Ad title",
    )

    status: "AdsAdStatus" = Field()

    category1_id: typing.Optional[int] = Field(
        default=None,
        description="Category ID",
    )

    category2_id: typing.Optional[int] = Field(
        default=None,
        description="Additional category ID",
    )

    cpc: typing.Optional[str] = Field(
        default=None,
        description="Cost of a click, kopecks",
    )

    cpm: typing.Optional[str] = Field(
        default=None,
        description="Cost of 1000 impressions, kopecks",
    )

    cpa: typing.Optional[str] = Field(
        default=None,
        description="Cost of an action, kopecks",
    )

    ocpm: typing.Optional[str] = Field(
        default=None,
        description="Cost of 1000 impressions optimized, kopecks",
    )

    autobidding: typing.Optional[bool] = Field(
        default=None,
        description="Autobidding",
    )

    autobidding_max_cost: typing.Optional[str] = Field(
        default=None,
        description="Max cost of target actions for autobidding, kopecks",
    )

    disclaimer_medical: typing.Optional[bool] = Field(
        default=None,
        description="Information whether disclaimer is enabled",
    )

    disclaimer_specialist: typing.Optional[bool] = Field(
        default=None,
        description="Information whether disclaimer is enabled",
    )

    disclaimer_supplements: typing.Optional[bool] = Field(
        default=None,
        description="Information whether disclaimer is enabled",
    )

    impressions_limit: typing.Optional[int] = Field(
        default=None,
        description="Impressions limit",
    )

    impressions_limit_period: typing.Optional[int] = Field(
        default=None,
        description="Impressions limit period",
    )

    impressions_limited: typing.Optional[bool] = Field(
        default=None,
        description="Information whether impressions are limited",
    )

    video: typing.Optional[bool] = Field(
        default=None,
        description="Information whether the ad is a video",
    )

    day_limit: typing.Optional[str] = Field(
        default=None,
        description="Day limit",
    )

    goal_type: typing.Optional[int] = Field(
        default=None,
        description="Goal type",
    )

    user_goal_type: typing.Optional[int] = Field(
        default=None,
        description="User goal type",
    )

    age_restriction: typing.Optional[int] = Field(
        default=None,
        description="Age restriction",
    )

    conversion_pixel_id: typing.Optional[int] = Field(
        default=None,
        description="Conversion pixel id",
    )

    conversion_event_id: typing.Optional[int] = Field(
        default=None,
        description="Conversion event id",
    )

    create_time: typing.Optional[int] = Field(
        default=None,
        description="Create time",
    )

    update_time: typing.Optional[int] = Field(
        default=None,
        description="Update time",
    )

    start_time: typing.Optional[int] = Field(
        default=None,
        description="Start time",
    )

    stop_time: typing.Optional[int] = Field(
        default=None,
        description="Stop time",
    )

    publisher_platforms_auto: typing.Optional[bool] = Field(
        default=None,
        description="Publisher platform auto",
    )

    publisher_platforms: typing.Optional[str] = Field(
        default=None,
        description="Publisher platforms",
    )

    link_url: typing.Optional[str] = Field(
        default=None,
        description="Link url",
    )

    link_owner_id: typing.Optional[int] = Field(
        default=None,
        description="Link owner id",
    )

    link_id: typing.Optional[int] = Field(
        default=None,
        description="Link id",
    )

    has_campaign_budget_optimization: typing.Optional[bool] = Field(
        default=None,
        description="Has campaign budget optimization",
    )

    events_retargeting_groups: typing.Optional[
        typing.List["AdsEventsRetargetingGroup"]
    ] = Field(
        default=None,
        description="Events retargeting groups",
    )

    weekly_schedule_hours: typing.Optional[typing.List[str]] = Field(
        default=None,
        description="Weekly schedule hours",
    )

    weekly_schedule_use_holidays: typing.Optional[int] = Field(
        default=None,
        description="Weekly schedule use holidays",
    )

    ad_platform_no_ad_network: typing.Optional[int] = Field(
        default=None,
        description="Ad platform no ad network",
    )

    ad_platform_no_wall: typing.Optional[int] = Field(
        default=None,
        description="Ad platform no wall",
    )

    disclaimer_finance: typing.Optional[int] = Field(
        default=None,
        description="Disclaimer finance",
    )

    disclaimer_finance_name: typing.Optional[str] = Field(
        default=None,
        description="Disclaimer finance name",
    )

    disclaimer_finance_license_no: typing.Optional[str] = Field(
        default=None,
        description="Disclaimer finance license no",
    )

    is_promo: typing.Optional[bool] = Field(
        default=None,
        description="is promo",
    )

    suggested_criteria: typing.Optional[int] = Field(
        default=None,
        description="Suggested criteria",
    )


class AdsAdApproved(enum.IntEnum):
    NOT_MODERATED = 0

    PENDING_MODERATION = 1

    APPROVED = 2

    REJECTED = 3


class AdsAdCostType(enum.IntEnum):
    PER_CLICKS = 0

    PER_IMPRESSIONS = 1

    PER_ACTIONS = 2

    PER_IMPRESSIONS_OPTIMIZED = 3


class AdsAdLayout(BaseModel):
    """
    Schema: ads_ad_layout
    """

    ad_format: int = Field(
        description="Ad format",
    )

    campaign_id: int = Field(
        description="Campaign ID",
    )

    cost_type: "AdsAdCostType" = Field()

    description: str = Field(
        description="Ad description",
    )

    id: int = Field(
        description="Ad ID",
    )

    image_src: str = Field(
        description="Image URL",
    )

    link_url: str = Field(
        description="URL of advertised object",
    )

    link_type: int = Field(
        description="Type of advertised object",
    )

    title: str = Field(
        description="Ad title",
    )

    image_src_2x: typing.Optional[str] = Field(
        default=None,
        description="URL of the preview image in double size",
    )

    link_domain: typing.Optional[str] = Field(
        default=None,
        description="Domain of advertised object",
    )

    preview_link: typing.Optional[str] = Field(
        default=None,
        description="link to preview an ad as it is shown on the website",
    )

    video: typing.Optional[bool] = Field(
        default=None,
        description="Information whether the ad is a video",
    )

    social: typing.Optional[bool] = Field(
        default=None,
        description="Social",
    )

    okved: typing.Optional[str] = Field(
        default=None,
        description="Okved",
    )

    age_restriction: typing.Optional[int] = Field(
        default=None,
        description="Age restriction",
    )

    goal_type: typing.Optional[int] = Field(
        default=None,
        description="Goal type",
    )

    link_title: typing.Optional[str] = Field(
        default=None,
        description="Link title",
    )

    link_button: typing.Optional[str] = Field(
        default=None,
        description="Link button",
    )

    repeat_video: typing.Optional[int] = Field(
        default=None,
        description="Repeat video",
    )

    video_src_240: typing.Optional[str] = Field(
        default=None,
        description="Video source 240p",
    )

    video_src_360: typing.Optional[str] = Field(
        default=None,
        description="Video source 360p",
    )

    video_src_480: typing.Optional[str] = Field(
        default=None,
        description="Video source 480p",
    )

    video_src_720: typing.Optional[str] = Field(
        default=None,
        description="Video source 720p",
    )

    video_src_1080: typing.Optional[str] = Field(
        default=None,
        description="Video source 1080p",
    )

    video_image_src: typing.Optional[str] = Field(
        default=None,
        description="Video image source",
    )

    video_image_src_2x: typing.Optional[str] = Field(
        default=None,
        description="Video image source 2x",
    )

    video_duration: typing.Optional[int] = Field(
        default=None,
        description="Video duration",
    )

    icon_src: typing.Optional[str] = Field(
        default=None,
        description="Icon source",
    )

    icon_src_2x: typing.Optional[str] = Field(
        default=None,
        description="Icon source 2x",
    )

    post: typing.Optional["AdsPost"] = Field(
        default=None,
    )

    stories_data: typing.Optional["AdsStories"] = Field(
        default=None,
    )

    clips_list: typing.Optional[typing.List["AdsClipItem"]] = Field(
        default=None,
    )


class AdsAdStatus(enum.IntEnum):
    STOPPED = 0

    STARTED = 1

    DELETED = 2


class AdsCampaign(BaseModel):
    """
    Schema: ads_campaign
    """

    all_limit: str = Field(
        description="Campaign's total limit, rubles",
    )

    day_limit: str = Field(
        description="Campaign's day limit, rubles",
    )

    id: int = Field(
        description="Campaign ID",
    )

    name: str = Field(
        description="Campaign title",
    )

    start_time: int = Field(
        description="Campaign start time, as Unixtime",
    )

    status: "AdsCampaignStatus" = Field()

    stop_time: int = Field(
        description="Campaign stop time, as Unixtime",
    )

    type: "AdsCampaignType" = Field()

    ads_count: typing.Optional[int] = Field(
        default=None,
        description="Amount of active ads in campaign",
    )

    create_time: typing.Optional[int] = Field(
        default=None,
        description="Campaign create time, as Unixtime",
    )

    goal_type: typing.Optional[int] = Field(
        default=None,
        description="Campaign goal type",
    )

    user_goal_type: typing.Optional[int] = Field(
        default=None,
        description="Campaign user goal type",
    )

    is_cbo_enabled: typing.Optional[bool] = Field(
        default=None,
        description="Shows if Campaign Budget Optimization is on",
    )

    update_time: typing.Optional[int] = Field(
        default=None,
        description="Campaign update time, as Unixtime",
    )

    views_limit: typing.Optional[int] = Field(
        default=None,
        description="Limit of views per user per campaign",
    )


class AdsCampaignStatus(enum.IntEnum):
    STOPPED = 0

    STARTED = 1

    DELETED = 2


class AdsCampaignType(enum.Enum):
    NORMAL = "normal"

    VK_APPS_MANAGED = "vk_apps_managed"

    MOBILE_APPS = "mobile_apps"

    PROMOTED_POSTS = "promoted_posts"

    ADAPTIVE_ADS = "adaptive_ads"

    STORIES = "stories"


class AdsCategory(BaseModel):
    """
    Schema: ads_category
    """

    id: int = Field(
        description="Category ID",
    )

    name: str = Field(
        description="Category name",
    )

    subcategories: typing.Optional[typing.List["AdsCategory"]] = Field(
        default=None,
    )


class AdsClient(BaseModel):
    """
    Schema: ads_client
    """

    all_limit: str = Field(
        description="Client's total limit, rubles",
    )

    day_limit: str = Field(
        description="Client's day limit, rubles",
    )

    id: int = Field(
        description="Client ID",
    )

    name: str = Field(
        description="Client name",
    )

    ord_data: typing.Optional["AdsOrdData"] = Field(
        default=None,
        description="Ord data",
    )


class AdsClipItem(BaseModel):
    """
    Schema: ads_clip_item
    """

    video_id: typing.Optional[int] = Field(
        default=None,
        description="Video id",
    )

    preview_url: typing.Optional[str] = Field(
        default=None,
        description="Preview url",
    )

    link: typing.Optional["AdsClipItemLink"] = Field(
        default=None,
    )


class AdsClipItemLink(BaseModel):
    """
    Schema: ads_clip_item_link
    """

    text: typing.Optional[str] = Field(
        default=None,
        description="Text",
    )

    key: typing.Optional[str] = Field(
        default=None,
        description="Key",
    )

    url: typing.Optional[str] = Field(
        default=None,
        description="Url",
    )


class AdsCreateAdStatus(BaseModel):
    """
    Schema: ads_create_ad_status
    """

    id: int = Field(
        description="Ad ID",
    )

    post_id: typing.Optional[int] = Field(
        default=None,
        description="Stealth Post ID",
    )

    error_code: typing.Optional[int] = Field(
        default=None,
        description="Error code",
    )

    error_desc: typing.Optional[str] = Field(
        default=None,
        description="Error description",
    )


class AdsCreateCampaignStatus(BaseModel):
    """
    Schema: ads_create_campaign_status
    """

    id: int = Field(
        description="Campaign ID",
    )

    error_code: typing.Optional[int] = Field(
        default=None,
        description="Error code",
    )

    error_desc: typing.Optional[str] = Field(
        default=None,
        description="Error description",
    )


class AdsCreateClientsStatus(BaseModel):
    """
    Schema: ads_create_clients_status
    """

    id: int = Field(
        description="Client ID",
    )

    error_code: typing.Optional[int] = Field(
        default=None,
        description="Error code",
    )

    error_desc: typing.Optional[str] = Field(
        default=None,
        description="Error description",
    )


class AdsCriteria(BaseModel):
    """
    Schema: ads_criteria
    """

    age_from: typing.Optional[str] = Field(
        default=None,
        description="Age from",
    )

    age_to: typing.Optional[str] = Field(
        default=None,
        description="Age to",
    )

    apps: typing.Optional[str] = Field(
        default=None,
        description="Apps IDs",
    )

    apps_not: typing.Optional[str] = Field(
        default=None,
        description="Apps IDs to except",
    )

    birthday: typing.Optional[str] = Field(
        default=None,
        description="Days to birthday",
    )

    cities: typing.Optional[str] = Field(
        default=None,
        description="Cities IDs",
    )

    cities_not: typing.Optional[str] = Field(
        default=None,
        description="Cities IDs to except",
    )

    country: typing.Optional[str] = Field(
        default=None,
        description="Country ID",
    )

    districts: typing.Optional[str] = Field(
        default=None,
        description="Districts IDs",
    )

    groups: typing.Optional[str] = Field(
        default=None,
        description="Communities IDs",
    )

    interest_categories: typing.Optional[str] = Field(
        default=None,
        description="Interests categories IDs",
    )

    interests: typing.Optional[str] = Field(
        default=None,
        description="Interests",
    )

    paying: typing.Optional[str] = Field(
        default=None,
        description="Information whether the user has proceeded VK payments before",
    )

    positions: typing.Optional[str] = Field(
        default=None,
        description="Positions IDs",
    )

    religions: typing.Optional[str] = Field(
        default=None,
        description="Religions IDs",
    )

    retargeting_groups: typing.Optional[str] = Field(
        default=None,
        description="Retargeting groups ids",
    )

    retargeting_groups_not: typing.Optional[str] = Field(
        default=None,
        description="Retargeting groups NOT ids",
    )

    school_from: typing.Optional[str] = Field(
        default=None,
        description="School graduation year from",
    )

    school_to: typing.Optional[str] = Field(
        default=None,
        description="School graduation year to",
    )

    schools: typing.Optional[str] = Field(
        default=None,
        description="Schools IDs",
    )

    sex: typing.Optional["AdsCriteriaSex"] = Field(
        default=None,
    )

    stations: typing.Optional[str] = Field(
        default=None,
        description="Stations IDs",
    )

    statuses: typing.Optional[str] = Field(
        default=None,
        description="Relationship statuses",
    )

    streets: typing.Optional[str] = Field(
        default=None,
        description="Streets IDs",
    )

    travellers: typing.Optional[str] = Field(
        default=None,
        description="Travellers",
    )

    ab_test: typing.Optional[str] = Field(
        default=None,
        description="AB test",
    )

    uni_from: typing.Optional[str] = Field(
        default=None,
        description="University graduation year from",
    )

    uni_to: typing.Optional[str] = Field(
        default=None,
        description="University graduation year to",
    )

    user_browsers: typing.Optional[str] = Field(
        default=None,
        description="Browsers",
    )

    user_devices: typing.Optional[str] = Field(
        default=None,
        description="Devices",
    )

    user_os: typing.Optional[str] = Field(
        default=None,
        description="Operating systems",
    )

    suggested_criteria: typing.Optional[str] = Field(
        default=None,
        description="Suggested criteria",
    )

    groups_not: typing.Optional[str] = Field(
        default=None,
        description="Group not",
    )

    price_list_audience_type: typing.Optional[str] = Field(
        default=None,
        description="Price list audience type",
    )

    count: typing.Optional[str] = Field(
        default=None,
        description="Count",
    )

    groups_active_formula: typing.Optional[str] = Field(
        default=None,
        description="Group active formula",
    )

    interest_categories_formula: typing.Optional[str] = Field(
        default=None,
        description="Interest categories formula",
    )

    groups_formula: typing.Optional[str] = Field(
        default=None,
        description="Groups formula",
    )

    groups_active: typing.Optional[str] = Field(
        default=None,
        description="Groups active",
    )

    group_types: typing.Optional[str] = Field(
        default=None,
        description="Group types",
    )

    key_phrases: typing.Optional[str] = Field(
        default=None,
        description="Key phrases",
    )

    key_phrases_days: typing.Optional[str] = Field(
        default=None,
        description="Key phrases days",
    )

    geo_near: typing.Optional[str] = Field(
        default=None,
        description="Geo near",
    )

    geo_point_type: typing.Optional[str] = Field(
        default=None,
        description="Geo point type",
    )

    price_list_id: typing.Optional[str] = Field(
        default=None,
        description="Price list id",
    )

    groups_recommended: typing.Optional[str] = Field(
        default=None,
        description="Groups recommended ids",
    )

    groups_active_recommended: typing.Optional[str] = Field(
        default=None,
        description="Groups active recommended ids",
    )

    music_artists_formula: typing.Optional[str] = Field(
        default=None,
        description="Music artists formula",
    )

    price_list_retargeting_formula: typing.Optional[str] = Field(
        default=None,
        description="Price list retargeting formula",
    )

    tags: typing.Optional[str] = Field(
        default=None,
        description="Tags",
    )

    browsers: typing.Optional[str] = Field(
        default=None,
        description="Browsers",
    )

    mobile_os_min_version: typing.Optional[str] = Field(
        default=None,
        description="Mobile os min version",
    )

    mobile_apps_events_formula: typing.Optional[str] = Field(
        default=None,
        description="Mobile apps events formula",
    )

    mobile_os_max_version: typing.Optional[str] = Field(
        default=None,
        description="Mobile os max version",
    )

    operators: typing.Optional[str] = Field(
        default=None,
        description="operators",
    )

    wifi_only: typing.Optional[str] = Field(
        default=None,
        description="wifi_only",
    )

    mobile_manufacturers: typing.Optional[str] = Field(
        default=None,
        description="mobile_manufacturers",
    )


class AdsCriteriaSex(enum.Enum):
    _0 = "0"

    _1 = "1"

    _2 = "2"


class AdsDemoStats(BaseModel):
    """
    Schema: ads_demo_stats
    """

    id: typing.Optional[int] = Field(
        default=None,
        description="Object ID",
    )

    stats: typing.Optional[typing.List["AdsDemostatsFormat"]] = Field(
        default=None,
    )

    type: typing.Optional["AdsObjectType"] = Field(
        default=None,
    )


class AdsDemographicStatsPeriodItemBase(BaseModel):
    """
    Schema: ads_demographic_stats_period_item_base
    """

    clicks_rate: typing.Optional[float] = Field(
        default=None,
        description="Clicks rate",
    )

    impressions_rate: typing.Optional[float] = Field(
        default=None,
        description="Impressions rate",
    )


class AdsDemostatsFormat(BaseModel):
    """
    Schema: ads_demostats_format
    """

    age: typing.Optional[typing.List["AdsStatsAge"]] = Field(
        default=None,
    )

    cities: typing.Optional[typing.List["AdsStatsCities"]] = Field(
        default=None,
    )

    day: typing.Optional[str] = Field(
        default=None,
        description="Day as YYYY-MM-DD",
    )

    day_from: typing.Optional[str] = Field(
        default=None,
    )

    day_to: typing.Optional[str] = Field(
        default=None,
    )

    month: typing.Optional[str] = Field(
        default=None,
        description="Month as YYYY-MM",
    )

    overall: typing.Optional[int] = Field(
        default=None,
        description="1 if period=overall",
    )

    sex: typing.Optional[typing.List["AdsStatsSex"]] = Field(
        default=None,
    )

    sex_age: typing.Optional[typing.List["AdsStatsSexAge"]] = Field(
        default=None,
    )


class AdsEventsRetargetingGroup(BaseModel):
    """
    Schema: ads_events_retargeting_group
    """

    id: typing.Optional[int] = Field(
        default=None,
    )

    value: typing.Optional[typing.List[int]] = Field(
        default=None,
    )


class AdsFloodStats(BaseModel):
    """
    Schema: ads_flood_stats
    """

    left: int = Field(
        description="Requests left",
    )

    refresh: int = Field(
        description="Time to refresh in seconds",
    )

    stats_by_user: typing.Optional[typing.List["AdsFloodStatsByUserItem"]] = Field(
        default=None,
        description="Used requests per user",
    )


class AdsFloodStatsByUserItem(BaseModel):
    """
    Schema: ads_flood_stats_by_user_item
    """

    user_id: int = Field(
        description="User ID",
    )

    requests_count: int = Field(
        description="Used requests",
    )


class AdsLinkStatus(BaseModel):
    """
    Schema: ads_link_status
    """

    status: str = Field(
        description="Link status",
    )

    description: typing.Optional[str] = Field(
        default=None,
        description="Reject reason",
    )

    redirect_url: typing.Optional[str] = Field(
        default=None,
        description="URL",
    )


class AdsLookalikeRequestStatus(enum.Enum):
    SEARCH_IN_PROGRESS = "search_in_progress"
    SEARCH_FAILED = "search_failed"
    SEARCH_DONE = "search_done"
    SAVE_IN_PROGRESS = "save_in_progress"
    SAVE_FAILED = "save_failed"
    SAVE_DONE = "save_done"


class AdsLookalikeRequestSourceType(enum.Enum):
    RETARGETING_GROUP = "retargeting_group"


class AdsLookalikeRequest(BaseModel):
    """
    Schema: ads_lookalike_request
    """

    id: int = Field(
        description="Lookalike request ID",
    )

    create_time: int = Field(
        description="Lookalike request create time, as Unixtime",
    )

    update_time: int = Field(
        description="Lookalike request update time, as Unixtime",
    )

    status: "AdsLookalikeRequestStatus" = Field(
        description="Lookalike request status",
    )

    source_type: "AdsLookalikeRequestSourceType" = Field(
        description="Lookalike request source type",
    )

    scheduled_delete_time: typing.Optional[int] = Field(
        default=None,
        description="Time by which lookalike request would be deleted, as Unixtime",
    )

    source_retargeting_group_id: typing.Optional[int] = Field(
        default=None,
        description="Retargeting group id, which was used as lookalike seed",
    )

    source_name: typing.Optional[str] = Field(
        default=None,
        description="Lookalike request seed name (retargeting group name)",
    )

    audience_count: typing.Optional[int] = Field(
        default=None,
        description="Lookalike request seed audience size",
    )

    save_audience_levels: typing.Optional[
        typing.List["AdsLookalikeRequestSaveAudienceLevel"]
    ] = Field(
        default=None,
    )


class AdsLookalikeRequestSaveAudienceLevel(BaseModel):
    """
    Schema: ads_lookalike_request_save_audience_level
    """

    level: typing.Optional[int] = Field(
        default=None,
        description="Save audience level id, which is used in save audience queries",
    )

    audience_count: typing.Optional[int] = Field(
        default=None,
        description="Saved audience audience size for according level",
    )


class AdsMobileStatItem(BaseModel):
    """
    Schema: ads_mobile_stat_item
    """

    key: typing.Optional[str] = Field(
        default=None,
    )

    value: typing.Optional[float] = Field(
        default=None,
    )


class AdsMusician(BaseModel):
    """
    Schema: ads_musician
    """

    id: int = Field(
        description="Targeting music artist ID",
    )

    name: str = Field(
        description="Music artist name",
    )

    avatar: typing.Optional[str] = Field(
        default=None,
        description="Music artist photo",
    )


class AdsObjectType(enum.Enum):
    AD = "ad"

    CAMPAIGN = "campaign"

    CLIENT = "client"

    OFFICE = "office"


class AdsOrdClientType(enum.Enum):
    PERSON = "person"

    INDIVIDUAL = "individual"

    LEGAL = "legal"

    FOREIGN = "foreign"

    UNKNOWN = "unknown"


class AdsOrdData(BaseModel):
    """
    Schema: ads_ord_data
    """

    client_type: "AdsOrdClientType" = Field()

    client_name: str = Field()

    phone: str = Field()

    contract_number: str = Field()

    contract_date: str = Field()

    contract_type: str = Field()

    contract_object: str = Field()

    with_vat: bool = Field()

    inn: typing.Optional[str] = Field(
        default=None,
    )

    subagent: typing.Optional["AdsOrdSubagent"] = Field(
        default=None,
    )


class AdsOrdSubagent(BaseModel):
    """
    Schema: ads_ord_subagent
    """

    type: "AdsOrdClientType" = Field()

    name: str = Field()

    phone: str = Field()

    inn: typing.Optional[str] = Field(
        default=None,
    )


class AdsPost(BaseModel):
    """
    Schema: ads_post
    """

    id: typing.Optional[int] = Field(
        default=None,
        description="Post id",
    )

    from_id: typing.Optional[int] = Field(
        default=None,
        description="From id",
    )

    owner_id: typing.Optional[int] = Field(
        default=None,
        description="Owner id",
    )

    date: typing.Optional[int] = Field(
        default=None,
        description="Date",
    )

    edited: typing.Optional[int] = Field(
        default=None,
        description="Edited date",
    )

    is_pinned: typing.Optional[int] = Field(
        default=None,
        description="Is pinned",
    )

    marked_as_ads: typing.Optional[int] = Field(
        default=None,
        description="Marked as ads",
    )

    ads_easy_promote: typing.Optional["AdsPostEasyPromote"] = Field(
        default=None,
    )

    donut: typing.Optional["AdsPostDonut"] = Field(
        default=None,
    )

    comments: typing.Optional["AdsPostComments"] = Field(
        default=None,
    )

    short_text_rate: typing.Optional[float] = Field(
        default=None,
        description="Short text rate",
    )

    type: typing.Optional[str] = Field(
        default=None,
        description="Type",
    )

    is_favorite: typing.Optional[bool] = Field(
        default=None,
        description="Is favorite",
    )

    likes: typing.Optional["AdsPostLikes"] = Field(
        default=None,
    )

    views: typing.Optional["AdsPostViews"] = Field(
        default=None,
    )

    post_type: typing.Optional[str] = Field(
        default=None,
        description="Post type",
    )

    reposts: typing.Optional["AdsPostReposts"] = Field(
        default=None,
    )

    text: typing.Optional[str] = Field(
        default=None,
        description="Text",
    )

    is_promoted_post_stealth: typing.Optional[bool] = Field(
        default=None,
        description="Is promoted post stealth",
    )

    hash: typing.Optional[str] = Field(
        default=None,
        description="Hash",
    )

    owner: typing.Optional["AdsPostOwner"] = Field(
        default=None,
    )

    attachments: typing.Optional[typing.List["WallWallpostAttachment"]] = Field(
        default=None,
    )

    created_by: typing.Optional[int] = Field(
        default=None,
        description="Created by",
    )

    carousel_offset: typing.Optional[int] = Field(
        default=None,
        description="Carousel offset",
    )

    can_edit: typing.Optional[int] = Field(
        default=None,
        description="Can edit",
    )

    can_delete: typing.Optional[int] = Field(
        default=None,
        description="Can delete",
    )

    can_pin: typing.Optional[int] = Field(
        default=None,
        description="Can pin",
    )


class AdsPostComments(BaseModel):
    """
    Schema: ads_post_comments
    """

    count: typing.Optional[int] = Field(
        default=None,
        description="Count",
    )


class AdsPostDonut(BaseModel):
    """
    Schema: ads_post_donut
    """

    is_donut: typing.Optional[bool] = Field(
        default=None,
        description="Is donut",
    )


class AdsPostEasyPromote(BaseModel):
    """
    Schema: ads_post_easy_promote
    """

    type: typing.Optional[int] = Field(
        default=None,
        description="Type",
    )

    text: typing.Optional[str] = Field(
        default=None,
        description="Text",
    )

    label_text: typing.Optional[str] = Field(
        default=None,
        description="Label text",
    )

    button_text: typing.Optional[str] = Field(
        default=None,
        description="Button text",
    )

    is_ad_not_easy: typing.Optional[bool] = Field(
        default=None,
        description="Is ad not easy",
    )

    ad_id: typing.Optional[int] = Field(
        default=None,
        description="Ad id",
    )

    top_union_id: typing.Optional[int] = Field(
        default=None,
        description="Top union id",
    )


class AdsPostLikes(BaseModel):
    """
    Schema: ads_post_likes
    """

    can_like: typing.Optional[int] = Field(
        default=None,
        description="Can like",
    )

    count: typing.Optional[int] = Field(
        default=None,
        description="Count",
    )

    user_likes: typing.Optional[int] = Field(
        default=None,
        description="User likes",
    )


class AdsPostOwner(BaseModel):
    """
    Schema: ads_post_owner
    """

    id: typing.Optional[int] = Field(
        default=None,
        description="Owner id",
    )

    name: typing.Optional[str] = Field(
        default=None,
        description="Name",
    )

    photo: typing.Optional[str] = Field(
        default=None,
        description="Photo url",
    )

    url: typing.Optional[str] = Field(
        default=None,
        description="Profile url",
    )


class AdsPostReposts(BaseModel):
    """
    Schema: ads_post_reposts
    """

    count: typing.Optional[int] = Field(
        default=None,
        description="Count",
    )

    wall_count: typing.Optional[int] = Field(
        default=None,
        description="Wall count",
    )

    mail_count: typing.Optional[int] = Field(
        default=None,
        description="Mail count",
    )


class AdsPostViews(BaseModel):
    """
    Schema: ads_post_views
    """

    count: typing.Optional[int] = Field(
        default=None,
        description="Count",
    )


class AdsPromotedPostReach(BaseModel):
    """
    Schema: ads_promoted_post_reach
    """

    hide: int = Field(
        description="Hides amount",
    )

    id: int = Field(
        description="Object ID from 'ids' parameter",
    )

    join_group: int = Field(
        description="Community joins",
    )

    links: int = Field(
        description="Link clicks",
    )

    reach_subscribers: int = Field(
        description="Subscribers reach",
    )

    reach_total: int = Field(
        description="Total reach",
    )

    report: int = Field(
        description="Reports amount",
    )

    to_group: int = Field(
        description="Community clicks",
    )

    unsubscribe: int = Field(
        description="'Unsubscribe' events amount",
    )

    video_views_100p: typing.Optional[int] = Field(
        default=None,
        description="Video views for 100 percent",
    )

    video_views_25p: typing.Optional[int] = Field(
        default=None,
        description="Video views for 25 percent",
    )

    video_views_3s: typing.Optional[int] = Field(
        default=None,
        description="Video views for 3 seconds",
    )

    video_views_10s: typing.Optional[int] = Field(
        default=None,
        description="Video views for 10 seconds",
    )

    video_views_50p: typing.Optional[int] = Field(
        default=None,
        description="Video views for 50 percent",
    )

    video_views_75p: typing.Optional[int] = Field(
        default=None,
        description="Video views for 75 percent",
    )

    video_views_start: typing.Optional[int] = Field(
        default=None,
        description="Video starts",
    )

    pretty_cards_clicks: typing.Optional[int] = Field(
        default=None,
        description="Pretty cards clicks",
    )


class AdsRejectReason(BaseModel):
    """
    Schema: ads_reject_reason
    """

    comment: typing.Optional[str] = Field(
        default=None,
        description="Comment text",
    )

    rules: typing.Optional[typing.List["AdsRules"]] = Field(
        default=None,
    )


class AdsRules(BaseModel):
    """
    Schema: ads_rules
    """

    help_url: typing.Optional["AdsRulesHelpUrl"] = Field(
        default=None,
        description="Help url",
    )

    help_label: typing.Optional[str] = Field(
        default=None,
        description="Label",
    )

    content_html: typing.Optional[str] = Field(
        default=None,
        description="Content Html",
    )

    help_chat: typing.Optional[bool] = Field(
        default=None,
        description="Help chat",
    )


class AdsRulesHelpUrl(BaseModel):
    """
    Schema: ads_rules_help_url
    """


class AdsStatisticClickActionType(enum.Enum):
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
    Schema: ads_statistic_click_action
    """

    type: typing.Optional["AdsStatisticClickActionType"] = Field(
        default=None,
    )

    url: typing.Optional[str] = Field(
        default=None,
    )


class AdsStats(BaseModel):
    """
    Schema: ads_stats
    """

    id: typing.Optional[int] = Field(
        default=None,
        description="Object ID",
    )

    stats: typing.Optional[typing.List["AdsStatsFormat"]] = Field(
        default=None,
    )

    type: typing.Optional["AdsObjectType"] = Field(
        default=None,
    )

    views_times: typing.Optional["AdsStatsViewsTimes"] = Field(
        default=None,
    )


class AdsStatsFormat(BaseModel):
    """
    Schema: ads_stats_format
    """

    clicks: typing.Optional[int] = Field(
        default=None,
        description="Clicks number",
    )

    link_external_clicks: typing.Optional[int] = Field(
        default=None,
        description="External clicks number",
    )

    day: typing.Optional[str] = Field(
        default=None,
        description="Day as YYYY-MM-DD",
    )

    impressions: typing.Optional[int] = Field(
        default=None,
        description="Impressions number",
    )

    join_rate: typing.Optional[int] = Field(
        default=None,
        description="Events number",
    )

    month: typing.Optional[str] = Field(
        default=None,
        description="Month as YYYY-MM",
    )

    year: typing.Optional[int] = Field(
        default=None,
        description="Year as YYYY",
    )

    overall: typing.Optional[int] = Field(
        default=None,
        description="1 if period=overall",
    )

    reach: typing.Optional[int] = Field(
        default=None,
        description="Reach ",
    )

    spent: typing.Optional[str] = Field(
        default=None,
        description="Spent funds",
    )

    video_plays_unique_started: typing.Optional[int] = Field(
        default=None,
        description="Video plays unique started count",
    )

    video_plays_unique_3_seconds: typing.Optional[int] = Field(
        default=None,
        description="Video plays unique 3 seconds count",
    )

    video_plays_unique_10_seconds: typing.Optional[int] = Field(
        default=None,
        description="Video plays unique 10 seconds count",
    )

    video_plays_unique_25_percents: typing.Optional[int] = Field(
        default=None,
        description="Video plays unique 25 percents count",
    )

    video_plays_unique_50_percents: typing.Optional[int] = Field(
        default=None,
        description="Video plays unique 50 percents count",
    )

    video_plays_unique_75_percents: typing.Optional[int] = Field(
        default=None,
        description="Video plays unique 75 percents count",
    )

    video_plays_unique_100_percents: typing.Optional[int] = Field(
        default=None,
        description="Video plays unique 100 percents count",
    )

    effective_cost_per_click: typing.Optional[str] = Field(
        default=None,
        description="Effective cost per click",
    )

    effective_cost_per_mille: typing.Optional[str] = Field(
        default=None,
        description="Effective cost per mille",
    )

    effective_cpf: typing.Optional[str] = Field(
        default=None,
        description="Effective cpf",
    )

    effective_cost_per_message: typing.Optional[str] = Field(
        default=None,
        description="Effective cost per message",
    )

    message_sends: typing.Optional[int] = Field(
        default=None,
        description="Message sends count",
    )

    message_sends_by_any_user: typing.Optional[int] = Field(
        default=None,
        description="Message sends by anu user",
    )

    conversions_external: typing.Optional[int] = Field(
        default=None,
        description="Conversions external",
    )

    conversion_count: typing.Optional[int] = Field(
        default=None,
        description="Conversions count",
    )

    conversion_cr: typing.Optional[str] = Field(
        default=None,
        description="Conversions CR",
    )

    day_from: typing.Optional[str] = Field(
        default=None,
        description="Day from",
    )

    day_to: typing.Optional[str] = Field(
        default=None,
        description="Day to",
    )

    ctr: typing.Optional[str] = Field(
        default=None,
        description="Ctr",
    )

    uniq_views_count: typing.Optional[int] = Field(
        default=None,
        description="Unique views count",
    )

    mobile_app_stat: typing.Optional[typing.List["AdsMobileStatItem"]] = Field(
        default=None,
        description="Mobile app stat",
    )


class AdsStatsSexValue(enum.Enum):
    F = "f"

    M = "m"


class AdsStatsViewsTimes(BaseModel):
    """
    Schema: ads_stats_views_times
    """

    views_ads_times_1: typing.Optional[int] = Field(
        default=None,
    )

    views_ads_times_2: typing.Optional[int] = Field(
        default=None,
    )

    views_ads_times_3: typing.Optional[int] = Field(
        default=None,
    )

    views_ads_times_4: typing.Optional[int] = Field(
        default=None,
    )

    views_ads_times_5: typing.Optional[str] = Field(
        default=None,
    )

    views_ads_times_6: typing.Optional[int] = Field(
        default=None,
    )

    views_ads_times_7: typing.Optional[int] = Field(
        default=None,
    )

    views_ads_times_8: typing.Optional[int] = Field(
        default=None,
    )

    views_ads_times_9: typing.Optional[int] = Field(
        default=None,
    )

    views_ads_times_10: typing.Optional[int] = Field(
        default=None,
    )

    views_ads_times_11_plus: typing.Optional[int] = Field(
        default=None,
    )


class AdsStories(BaseModel):
    """
    Schema: ads_stories
    """

    stories: typing.Optional[typing.List["AdsStoryItem"]] = Field(
        default=None,
    )

    owner: typing.Optional["AdsStoriesOwner"] = Field(
        default=None,
    )

    stories_disclaimers_text: typing.Optional[str] = Field(
        default=None,
        description="Stories disclaimers text",
    )


class AdsStoriesOwner(BaseModel):
    """
    Schema: ads_stories_owner
    """

    id: typing.Optional[int] = Field(
        default=None,
        description="Owner id",
    )

    href: typing.Optional[str] = Field(
        default=None,
        description="Href",
    )

    name: typing.Optional[str] = Field(
        default=None,
        description="Name",
    )

    photo: typing.Optional[str] = Field(
        default=None,
        description="Photo",
    )

    verify: typing.Optional[str] = Field(
        default=None,
        description="Verify",
    )

    gender: typing.Optional[str] = Field(
        default=None,
        description="Gender",
    )

    name_get: typing.Optional[str] = Field(
        default=None,
        description="Name get",
    )

    firstName: typing.Optional[str] = Field(
        default=None,
        description="First name",
    )

    first_name_gen: typing.Optional[str] = Field(
        default=None,
        description="First name gen",
    )

    first_name_ins: typing.Optional[str] = Field(
        default=None,
        description="First name ins",
    )

    can_follow: typing.Optional[bool] = Field(
        default=None,
        description="Can follow",
    )


class AdsStoryItem(BaseModel):
    """
    Schema: ads_story_item
    """

    id: typing.Optional[int] = Field(
        default=None,
        description="Story id",
    )

    owner_id: typing.Optional[int] = Field(
        default=None,
        description="Owner id",
    )

    raw_id: typing.Optional[str] = Field(
        default=None,
        description="Story raw id",
    )

    date: typing.Optional[str] = Field(
        default=None,
        description="Date",
    )

    time: typing.Optional[int] = Field(
        default=None,
        description="Time",
    )

    type: typing.Optional[str] = Field(
        default=None,
        description="Type",
    )

    unread: typing.Optional[bool] = Field(
        default=None,
        description="Is unread",
    )

    canLike: typing.Optional[bool] = Field(
        default=None,
        description="Can like",
    )

    can_comment: typing.Optional[bool] = Field(
        default=None,
        description="Can comment",
    )

    can_share: typing.Optional[bool] = Field(
        default=None,
        description="Can share",
    )

    can_remove: typing.Optional[bool] = Field(
        default=None,
        description="Can remove",
    )

    can_manage: typing.Optional[bool] = Field(
        default=None,
        description="Can manage",
    )

    can_ask: typing.Optional[bool] = Field(
        default=None,
        description="Can ask",
    )

    can_ask_anonymous: typing.Optional[bool] = Field(
        default=None,
        description="Can ask anonymous",
    )

    isProfileQuestion: typing.Optional[bool] = Field(
        default=None,
        description="Is profile question",
    )

    stats: typing.Optional["AdsStoryItemStats"] = Field(
        default=None,
    )

    link: typing.Optional["AdsStoryItemLink"] = Field(
        default=None,
    )

    photo_url: typing.Optional[str] = Field(
        default=None,
        description="Photo url",
    )

    preview_url: typing.Optional[str] = Field(
        default=None,
        description="Preview url",
    )

    track_code: typing.Optional[str] = Field(
        default=None,
        description="Track code",
    )

    isPartOfNarrative: typing.Optional[bool] = Field(
        default=None,
        description="Is part of narrative",
    )

    isAds: typing.Optional[bool] = Field(
        default=None,
        description="Is ads",
    )

    video_url: typing.Optional[str] = Field(
        default=None,
        description="Video url",
    )

    first_frame: typing.Optional[str] = Field(
        default=None,
        description="First frame",
    )

    small_preview: typing.Optional[str] = Field(
        default=None,
        description="Small preview",
    )

    isLiked: typing.Optional[bool] = Field(
        default=None,
        description="Is liked",
    )


class AdsStoryItemLink(BaseModel):
    """
    Schema: ads_story_item_link
    """

    key: typing.Optional[str] = Field(
        default=None,
        description="Key",
    )

    text: typing.Optional[str] = Field(
        default=None,
        description="Text",
    )

    url: typing.Optional[str] = Field(
        default=None,
        description="Url",
    )

    raw_url: typing.Optional[str] = Field(
        default=None,
        description="Raw url",
    )


class AdsStoryItemStats(BaseModel):
    """
    Schema: ads_story_item_stats
    """

    follow: typing.Optional["AdsStoryItemStatsFollow"] = Field(
        default=None,
    )

    url_view: typing.Optional["AdsStoryItemStatsUrlView"] = Field(
        default=None,
    )


class AdsStoryItemStatsFollow(BaseModel):
    """
    Schema: ads_story_item_stats_follow
    """

    event_type: typing.Optional[str] = Field(
        default=None,
        description="Event type",
    )

    rhash: typing.Optional[str] = Field(
        default=None,
        description="Event hash",
    )


class AdsStoryItemStatsUrlView(BaseModel):
    """
    Schema: ads_story_item_stats_url_view
    """

    event_type: typing.Optional[str] = Field(
        default=None,
        description="Event type",
    )

    rhash: typing.Optional[str] = Field(
        default=None,
        description="Event hash",
    )


class AdsTargStats(BaseModel):
    """
    Schema: ads_targ_stats
    """

    audience_count: int = Field(
        description="Audience",
    )

    recommended_cpc: typing.Optional[str] = Field(
        default=None,
        description="Recommended CPC value for 50% reach (old format)",
    )

    recommended_cpm: typing.Optional[str] = Field(
        default=None,
        description="Recommended CPM value for 50% reach (old format)",
    )

    recommended_cpc_50: typing.Optional[str] = Field(
        default=None,
        description="Recommended CPC value for 50% reach",
    )

    recommended_cpm_50: typing.Optional[str] = Field(
        default=None,
        description="Recommended CPM value for 50% reach",
    )

    recommended_cpc_70: typing.Optional[str] = Field(
        default=None,
        description="Recommended CPC value for 70% reach",
    )

    recommended_cpm_70: typing.Optional[str] = Field(
        default=None,
        description="Recommended CPM value for 70% reach",
    )

    recommended_cpc_90: typing.Optional[str] = Field(
        default=None,
        description="Recommended CPC value for 90% reach",
    )

    recommended_cpm_90: typing.Optional[str] = Field(
        default=None,
        description="Recommended CPM value for 90% reach",
    )

    total_alive_audience: typing.Optional[int] = Field(
        default=None,
        description="Total alive audience",
    )


class AdsTargSuggestions(BaseModel):
    """
    Schema: ads_targ_suggestions
    """

    id: typing.Optional[int] = Field(
        default=None,
        description="Object ID",
    )

    name: typing.Optional[str] = Field(
        default=None,
        description="Object name",
    )

    type: typing.Optional[str] = Field(
        default=None,
        description="Object type",
    )

    parent: typing.Optional[str] = Field(
        default=None,
        description="Parent",
    )


class AdsTargSuggestionsCities(BaseModel):
    """
    Schema: ads_targ_suggestions_cities
    """

    id: typing.Optional[int] = Field(
        default=None,
        description="Object ID",
    )

    name: typing.Optional[str] = Field(
        default=None,
        description="Object name",
    )

    parent: typing.Optional[str] = Field(
        default=None,
        description="Parent object",
    )


class AdsTargSuggestionsRegions(BaseModel):
    """
    Schema: ads_targ_suggestions_regions
    """

    id: typing.Optional[int] = Field(
        default=None,
        description="Object ID",
    )

    name: typing.Optional[str] = Field(
        default=None,
        description="Object name",
    )

    type: typing.Optional[str] = Field(
        default=None,
        description="Object type",
    )


class AdsTargSuggestionsSchools(BaseModel):
    """
    Schema: ads_targ_suggestions_schools
    """

    desc: typing.Optional[str] = Field(
        default=None,
        description="Full school title",
    )

    id: typing.Optional[int] = Field(
        default=None,
        description="School ID",
    )

    name: typing.Optional[str] = Field(
        default=None,
        description="School title",
    )

    parent: typing.Optional[str] = Field(
        default=None,
        description="City name",
    )

    type: typing.Optional["AdsTargSuggestionsSchoolsType"] = Field(
        default=None,
    )


class AdsTargSuggestionsSchoolsType(enum.Enum):
    SCHOOL = "school"

    UNIVERSITY = "university"

    FACULTY = "faculty"

    CHAIR = "chair"


class AdsTargetGroup(BaseModel):
    """
    Schema: ads_target_group
    """

    id: typing.Optional[int] = Field(
        default=None,
        description="Group ID",
    )

    name: typing.Optional[str] = Field(
        default=None,
        description="Group name",
    )

    is_audience: typing.Optional[bool] = Field(
        default=None,
        description="Is audience",
    )

    is_shared: typing.Optional[bool] = Field(
        default=None,
        description="Is shared",
    )

    file_source: typing.Optional[bool] = Field(
        default=None,
        description="File source",
    )

    api_source: typing.Optional[bool] = Field(
        default=None,
        description="API source",
    )

    lookalike_source: typing.Optional[bool] = Field(
        default=None,
        description="File source",
    )

    audience_count: typing.Optional[int] = Field(
        default=None,
        description="Audience",
    )

    domain: typing.Optional[str] = Field(
        default=None,
        description="Site domain",
    )

    lifetime: typing.Optional[int] = Field(
        default=None,
        description="Number of days for user to be in group",
    )

    pixel: typing.Optional[str] = Field(
        default=None,
        description="Pixel code",
    )

    target_pixel_id: typing.Optional[int] = Field(
        default=None,
        description="Target Pixel id",
    )

    target_pixel_rules: typing.Optional[
        typing.List["AdsTargetGroupTargetPixelRule"]
    ] = Field(
        default=None,
        description="Target Pixel rules",
    )

    last_updated: typing.Optional[int] = Field(
        default=None,
        description="Last updated",
    )


class AdsTargetGroupTargetPixelRule(BaseModel):
    """
    Schema: ads_target_group_target_pixel_rule
    """

    url_full_match: typing.Optional[str] = Field(
        default=None,
    )

    event_full_match: typing.Optional[str] = Field(
        default=None,
    )

    url_substrings_match: typing.Optional[typing.List[str]] = Field(
        default=None,
    )

    event_substrings_match: typing.Optional[typing.List[str]] = Field(
        default=None,
    )

    url_regex_match: typing.Optional[str] = Field(
        default=None,
    )

    event_regex_match: typing.Optional[str] = Field(
        default=None,
    )


class AdsTargetPixelInfo(BaseModel):
    """
    Schema: ads_target_pixel_info
    """

    target_pixel_id: int = Field()

    name: str = Field()

    domain: str = Field()

    category_id: int = Field()

    last_updated: int = Field()

    pixel: str = Field()


class AdsUpdateOfficeUsersResult(BaseModel):
    """
    Schema: ads_updateOfficeUsers_result
    """

    user_id: int = Field()

    is_success: bool = Field()

    error: typing.Optional["BaseError"] = Field(
        default=None,
    )


class AdsUpdateAdsStatus(BaseModel):
    """
    Schema: ads_update_ads_status
    """

    id: int = Field(
        description="Ad ID",
    )

    error_code: typing.Optional[int] = Field(
        default=None,
        description="Error code",
    )

    error_desc: typing.Optional[str] = Field(
        default=None,
        description="Error description",
    )


class AdsUpdateClientsStatus(BaseModel):
    """
    Schema: ads_update_clients_status
    """

    id: int = Field(
        description="Client ID",
    )

    error_code: typing.Optional[int] = Field(
        default=None,
        description="Error code",
    )

    error_desc: typing.Optional[str] = Field(
        default=None,
        description="Error description",
    )


class AdsUserSpecification(BaseModel):
    """
    Schema: ads_user_specification
    """

    user_id: int = Field()

    role: "AdsAccessRolePublic" = Field()

    grant_access_to_all_clients: typing.Optional[bool] = Field(
        default=None,
    )

    client_ids: typing.Optional[typing.List[int]] = Field(
        default=None,
    )

    view_budget: typing.Optional[bool] = Field(
        default=None,
    )


class AdsUserSpecificationCutted(BaseModel):
    """
    Schema: ads_user_specification_cutted
    """

    user_id: int = Field()

    role: "AdsAccessRolePublic" = Field()

    client_id: typing.Optional[int] = Field(
        default=None,
    )

    view_budget: typing.Optional[bool] = Field(
        default=None,
    )


class AdsUsers(BaseModel):
    """
    Schema: ads_users
    """

    accesses: typing.List["AdsAccesses"] = Field()

    user_id: int = Field(
        description="User ID",
    )


class AdswebGetAdCategoriesResponseCategoriesCategory(BaseModel):
    """
    Schema: adsweb_getAdCategories_response_categories_category
    """

    id: int = Field()

    name: str = Field()


class AdswebGetAdUnitsResponseAdUnitsAdUnit(BaseModel):
    """
    Schema: adsweb_getAdUnits_response_ad_units_ad_unit
    """

    id: int = Field()

    site_id: int = Field()

    name: typing.Optional[str] = Field(
        default=None,
    )


class AdswebGetFraudHistoryResponseEntriesEntry(BaseModel):
    """
    Schema: adsweb_getFraudHistory_response_entries_entry
    """

    site_id: int = Field()

    day: str = Field()


class AdswebGetSitesResponseSitesSite(BaseModel):
    """
    Schema: adsweb_getSites_response_sites_site
    """

    id: int = Field()

    status_user: typing.Optional[str] = Field(
        default=None,
    )

    status_moder: typing.Optional[str] = Field(
        default=None,
    )

    domains: typing.Optional[str] = Field(
        default=None,
    )


class AdswebGetStatisticsResponseItemsItem(BaseModel):
    """
    Schema: adsweb_getStatistics_response_items_item
    """

    site_id: typing.Optional[int] = Field(
        default=None,
    )

    ad_unit_id: typing.Optional[int] = Field(
        default=None,
    )

    overall_count: typing.Optional[int] = Field(
        default=None,
    )

    months_count: typing.Optional[int] = Field(
        default=None,
    )

    month_min: typing.Optional[str] = Field(
        default=None,
    )

    month_max: typing.Optional[str] = Field(
        default=None,
    )

    days_count: typing.Optional[int] = Field(
        default=None,
    )

    day_min: typing.Optional[str] = Field(
        default=None,
    )

    day_max: typing.Optional[str] = Field(
        default=None,
    )

    hours_count: typing.Optional[int] = Field(
        default=None,
    )

    hour_min: typing.Optional[str] = Field(
        default=None,
    )

    hour_max: typing.Optional[str] = Field(
        default=None,
    )


class AppWidgetsPhoto(BaseModel):
    """
    Schema: appWidgets_photo
    """

    id: str = Field(
        description="Image ID",
    )

    images: typing.List["BaseImage"] = Field()


class AppWidgetsPhotos(BaseModel):
    """
    Schema: appWidgets_photos
    """

    count: typing.Optional[int] = Field(
        default=None,
    )

    items: typing.Optional[typing.List["AppWidgetsPhoto"]] = Field(
        default=None,
    )


class AppsAppFields(enum.Enum):
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


class AppsAppLeaderboardType(enum.IntEnum):
    NOT_SUPPORTED = 0

    LEVELS = 1

    POINTS = 2


class AppsAppMin(BaseModel):
    """
    Schema: apps_app_min
    """

    type: "AppsAppType" = Field()

    id: int = Field(
        description="Application ID",
    )

    title: str = Field(
        description="Application title",
    )

    author_owner_id: typing.Optional[int] = Field(
        default=None,
        description="Application author's ID",
    )

    is_installed: typing.Optional[bool] = Field(
        default=None,
        description="Is application installed",
    )

    icon_139: typing.Optional[str] = Field(
        default=None,
        description="URL of the app icon with 139 px in width",
    )

    icon_150: typing.Optional[str] = Field(
        default=None,
        description="URL of the app icon with 150 px in width",
    )

    icon_278: typing.Optional[str] = Field(
        default=None,
        description="URL of the app icon with 278 px in width",
    )

    icon_576: typing.Optional[str] = Field(
        default=None,
        description="URL of the app icon with 576 px in width",
    )

    background_loader_color: typing.Optional[str] = Field(
        default=None,
        description="Hex color code without hash sign",
    )

    loader_icon: typing.Optional[str] = Field(
        default=None,
        description="SVG data",
    )

    icon_75: typing.Optional[str] = Field(
        default=None,
        description="URL of the app icon with 75 px in width",
    )

    screen_orientation: typing.Optional[int] = Field(
        default=None,
        description="Screen orientation",
    )


class AppsAppType(enum.Enum):
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
    Schema: apps_catalog_list
    """

    count: int = Field(
        description="Total number",
    )

    items: typing.List["AppsApp"] = Field()

    profiles: typing.Optional[typing.List["UsersUserMin"]] = Field(
        default=None,
    )


class AppsLeaderboard(BaseModel):
    """
    Schema: apps_leaderboard
    """

    user_id: int = Field(
        description="User ID",
    )

    level: typing.Optional[int] = Field(
        default=None,
        description="Level",
    )

    points: typing.Optional[int] = Field(
        default=None,
        description="Points number",
    )

    score: typing.Optional[int] = Field(
        default=None,
        description="Score number",
    )


class AppsScopeName(enum.Enum):
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
    Schema: apps_scope
    """

    name: "AppsScopeName" = Field(
        description="Scope name",
    )

    title: typing.Optional[str] = Field(
        default=None,
        description="Scope title",
    )


class AppsTestingGroup(BaseModel):
    """
    Schema: apps_testing_group
    """

    user_ids: typing.List[int] = Field()

    group_id: int = Field()

    name: typing.Optional[str] = Field(
        default=None,
    )

    webview: typing.Optional[str] = Field(
        default=None,
    )

    platforms: typing.Optional[typing.List[str]] = Field(
        default=None,
    )


class AudioAudio(BaseModel):
    """
    Schema: audio_audio
    """

    artist: str = Field(
        description="Artist name",
    )

    id: int = Field(
        description="Audio ID",
    )

    owner_id: int = Field(
        description="Audio owner's ID",
    )

    title: str = Field(
        description="Title",
    )

    duration: int = Field(
        description="Duration in seconds",
    )

    access_key: typing.Optional[str] = Field(
        default=None,
        description="Access key for the audio",
    )

    url: typing.Optional[str] = Field(
        default=None,
        description="URL of mp3 file",
    )

    date: typing.Optional[int] = Field(
        default=None,
        description="Date when uploaded",
    )

    album_id: typing.Optional[int] = Field(
        default=None,
        description="Album ID",
    )

    performer: typing.Optional[str] = Field(
        default=None,
        description="Performer name",
    )


class BaseBoolInt(enum.IntEnum):
    NO = 0

    YES = 1


class BaseCity(BaseModel):
    """
    Schema: base_city
    """

    id: int = Field(
        description="City ID",
    )

    title: str = Field(
        description="City title",
    )


class BaseCommentsInfo(BaseModel):
    """
    Schema: base_comments_info
    """

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

    list: typing.Optional[typing.List["WallWallComment"]] = Field(
        default=None,
    )


class BaseCountry(BaseModel):
    """
    Schema: base_country
    """

    id: int = Field(
        description="Country ID",
    )

    title: str = Field(
        description="Country title",
    )


class BaseCropPhoto(BaseModel):
    """
    Schema: base_crop_photo
    """

    photo: "PhotosPhoto" = Field()

    crop: "BaseCropPhotoCrop" = Field()

    rect: "BaseCropPhotoRect" = Field()


class BaseCropPhotoCrop(BaseModel):
    """
    Schema: base_crop_photo_crop
    """

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


class BaseCropPhotoRect(BaseModel):
    """
    Schema: base_crop_photo_rect
    """

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


class BaseError(BaseModel):
    """
    Schema: base_error
    """

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

    request_params: typing.Optional[typing.List["BaseRequestParam"]] = Field(
        default=None,
    )


class BaseGeo(BaseModel):
    """
    Schema: base_geo
    """

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


class BaseGeoCoordinates(BaseModel):
    """
    Schema: base_geo_coordinates
    """

    latitude: float = Field()

    longitude: float = Field()


class BaseGradientPoint(BaseModel):
    """
    Schema: base_gradient_point
    """

    color: str = Field(
        description="Hex color code without #",
    )

    position: float = Field(
        description="Point position",
    )


class BaseImageTheme(enum.Enum):
    LIGHT = "light"
    DARK = "dark"


class BaseImage(BaseModel):
    """
    Schema: base_image
    """

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

    theme: typing.Optional["BaseImageTheme"] = Field(
        default=None,
    )


class BaseLang(enum.Enum):
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
    Schema: base_likes
    """

    count: typing.Optional[int] = Field(
        default=None,
        description="Likes number",
    )

    user_likes: typing.Optional[bool] = Field(
        default=None,
        description="Information whether current user likes the photo",
    )


class BaseLikesInfo(BaseModel):
    """
    Schema: base_likes_info
    """

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


class BaseLinkApplication(BaseModel):
    """
    Schema: base_link_application
    """

    app_id: typing.Optional[float] = Field(
        default=None,
        description="Application Id",
    )

    store: typing.Optional["BaseLinkApplicationStore"] = Field(
        default=None,
    )


class BaseLinkApplicationStore(BaseModel):
    """
    Schema: base_link_application_store
    """

    id: typing.Optional[float] = Field(
        default=None,
        description="Store Id",
    )

    name: typing.Optional[str] = Field(
        default=None,
        description="Store name",
    )


class BaseLinkButton(BaseModel):
    """
    Schema: base_link_button
    """

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


class BaseLinkButtonAction(BaseModel):
    """
    Schema: base_link_button_action
    """

    type: "BaseLinkButtonActionType" = Field()

    url: typing.Optional[str] = Field(
        default=None,
        description="Action URL",
    )

    consume_reason: typing.Optional[str] = Field(
        default=None,
    )


class BaseLinkButtonActionType(enum.Enum):
    OPEN_URL = "open_url"

    MARKET_CLEAR_RECENT_QUERIES = "market_clear_recent_queries"

    CLOSE_WEB_APP = "close_web_app"

    OPEN_SEARCH_TAB = "open_search_tab"

    IMPORT_CONTACTS = "import_contacts"

    ADD_FRIENDS = "add_friends"

    ONBOARDING = "onboarding"


class BaseLinkButtonStyle(enum.Enum):
    PRIMARY = "primary"

    SECONDARY = "secondary"


class BaseLinkNoProduct(BaseModel):
    """
    Schema: base_link_no_product
    """

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


class BaseLinkProductType(enum.Enum):
    PRODUCT = "product"


class BaseLinkProduct(BaseModel):
    """
    Schema: base_link_product
    """

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

    type: typing.Optional["BaseLinkProductType"] = Field(
        default=None,
    )


class BaseLinkProductCategory(BaseModel):
    """
    Schema: base_link_product_category
    """


class BaseLinkProductStatus(enum.Enum):
    ACTIVE = "active"

    BLOCKED = "blocked"

    SOLD = "sold"

    DELETED = "deleted"

    ARCHIVED = "archived"


class BaseLinkRatingType(enum.Enum):
    RATING = "rating"


class BaseLinkRating(BaseModel):
    """
    Schema: base_link_rating
    """

    reviews_count: typing.Optional[int] = Field(
        default=None,
        description="Count of reviews",
    )

    stars: typing.Optional[float] = Field(
        default=None,
        description="Count of stars",
    )

    type: typing.Optional["BaseLinkRatingType"] = Field(
        default=None,
    )


class BaseMessageError(BaseModel):
    """
    Schema: base_message_error
    """

    code: typing.Optional[int] = Field(
        default=None,
        description="Error code",
    )

    description: typing.Optional[str] = Field(
        default=None,
        description="Error message",
    )


class BaseNameCase(enum.Enum):
    NOM = "Nom"

    GEN = "Gen"

    DAT = "Dat"

    ACC = "Acc"

    INS = "Ins"

    ABL = "Abl"


class BaseObject(BaseModel):
    """
    Schema: base_object
    """

    id: int = Field(
        description="Object ID",
    )

    title: str = Field(
        description="Object title",
    )


class BaseObjectCount(BaseModel):
    """
    Schema: base_object_count
    """

    count: typing.Optional[int] = Field(
        default=None,
        description="Items count",
    )


class BaseObjectWithName(BaseModel):
    """
    Schema: base_object_with_name
    """

    id: int = Field(
        description="Object ID",
    )

    name: str = Field(
        description="Object name",
    )


class BaseOwnerCover(BaseModel):
    """
    Schema: base_owner_cover
    """

    enabled: bool = Field(
        description="Information whether cover is enabled",
    )

    images: typing.Optional[typing.List["BaseImage"]] = Field(
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


class BaseOwnerCoverCropParams(BaseModel):
    """
    Schema: base_owner_cover_crop_params
    """

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


class BasePlace(BaseModel):
    """
    Schema: base_place
    """

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


class BasePropertyExists(enum.IntEnum):
    PROPERTY_EXISTS = 1


class BaseRepostsInfo(BaseModel):
    """
    Schema: base_reposts_info
    """

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


class BaseRequestParam(BaseModel):
    """
    Schema: base_request_param
    """

    key: str = Field(
        description="Parameter name",
    )

    value: str = Field(
        description="Parameter value",
    )


class BaseSex(enum.IntEnum):
    UNKNOWN = 0

    FEMALE = 1

    MALE = 2


class BaseSticker(BaseModel):
    """
    Schema: base_sticker
    """


class BaseStickerAnimationType(enum.Enum):
    LIGHT = "light"
    DARK = "dark"


class BaseStickerAnimation(BaseModel):
    """
    Schema: base_sticker_animation
    """

    type: typing.Optional["BaseStickerAnimationType"] = Field(
        default=None,
        description="Type of animation script",
    )

    url: typing.Optional[str] = Field(
        default=None,
        description="URL of animation script",
    )


class BaseStickerNew(BaseModel):
    """
    Schema: base_sticker_new
    """

    sticker_id: typing.Optional[int] = Field(
        default=None,
        description="Sticker ID",
    )

    product_id: typing.Optional[int] = Field(
        default=None,
        description="Pack ID",
    )

    images: typing.Optional[typing.List["BaseImage"]] = Field(
        default=None,
    )

    images_with_background: typing.Optional[typing.List["BaseImage"]] = Field(
        default=None,
    )

    animation_url: typing.Optional[str] = Field(
        default=None,
        description="URL of sticker animation script",
    )

    animations: typing.Optional[typing.List["BaseStickerAnimation"]] = Field(
        default=None,
        description="Array of sticker animation script objects",
    )

    is_allowed: typing.Optional[bool] = Field(
        default=None,
        description="Information whether the sticker is allowed",
    )


class BaseStickerOld(BaseModel):
    """
    Schema: base_sticker_old
    """

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


class BaseStickersList(BaseModel):
    """
    Schema: base_stickers_list
    """


class BaseUploadServer(BaseModel):
    """
    Schema: base_upload_server
    """

    upload_url: str = Field(
        description="Upload URL",
    )


class BaseUserGroupFields(enum.Enum):
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


class BaseUserId(BaseModel):
    """
    Schema: base_user_id
    """

    user_id: typing.Optional[int] = Field(
        default=None,
        description="User ID",
    )


class BoardDefaultOrder(enum.IntEnum):
    DESC_UPDATED = 1

    DESC_CREATED = 2

    ASC_UPDATED = -1

    ASC_CREATED = -2


class BoardTopic(BaseModel):
    """
    Schema: board_topic
    """

    comments: typing.Optional[int] = Field(
        default=None,
        description="Comments number",
    )

    created: typing.Optional[int] = Field(
        default=None,
        description="Date when the topic has been created in Unixtime",
    )

    created_by: typing.Optional[int] = Field(
        default=None,
        description="Creator ID",
    )

    id: typing.Optional[int] = Field(
        default=None,
        description="Topic ID",
    )

    is_closed: typing.Optional[bool] = Field(
        default=None,
        description="Information whether the topic is closed",
    )

    is_fixed: typing.Optional[bool] = Field(
        default=None,
        description="Information whether the topic is fixed",
    )

    title: typing.Optional[str] = Field(
        default=None,
        description="Topic title",
    )

    updated: typing.Optional[int] = Field(
        default=None,
        description="Date when the topic has been updated in Unixtime",
    )

    updated_by: typing.Optional[int] = Field(
        default=None,
        description="ID of user who updated the topic",
    )

    first_comment: typing.Optional[str] = Field(
        default=None,
        description="First comment text",
    )

    last_comment: typing.Optional[str] = Field(
        default=None,
        description="Last comment text",
    )


class BoardTopicComment(BaseModel):
    """
    Schema: board_topic_comment
    """

    date: int = Field(
        description="Date when the comment has been added in Unixtime",
    )

    from_id: int = Field(
        description="Author ID",
    )

    id: int = Field(
        description="Comment ID",
    )

    text: str = Field(
        description="Comment text",
    )

    attachments: typing.Optional[typing.List["WallCommentAttachment"]] = Field(
        default=None,
    )

    real_offset: typing.Optional[int] = Field(
        default=None,
        description="Real position of the comment",
    )

    can_edit: typing.Optional[bool] = Field(
        default=None,
        description="Information whether current user can edit the comment",
    )

    likes: typing.Optional["BaseLikesInfo"] = Field(
        default=None,
    )


class CallbackBase(BaseModel):
    """
    Schema: callback_base
    """

    type: "CallbackType" = Field()

    group_id: int = Field()

    event_id: str = Field(
        description="Unique event id. If it passed twice or more - you should ignore it.",
    )

    v: str = Field(
        description="API object version",
    )

    secret: typing.Optional[str] = Field(
        default=None,
    )


class CallbackBoardPostDelete(BaseModel):
    """
    Schema: callback_board_post_delete
    """

    topic_owner_id: int = Field()

    topic_id: int = Field()

    id: int = Field()


class CallbackDonutMoneyWithdraw(BaseModel):
    """
    Schema: callback_donut_money_withdraw
    """

    amount: float = Field()

    amount_without_fee: float = Field()


class CallbackDonutMoneyWithdrawError(BaseModel):
    """
    Schema: callback_donut_money_withdraw_error
    """

    reason: str = Field()


class CallbackDonutSubscriptionCancelled(BaseModel):
    """
    Schema: callback_donut_subscription_cancelled
    """

    user_id: typing.Optional[int] = Field(
        default=None,
    )


class CallbackDonutSubscriptionCreate(BaseModel):
    """
    Schema: callback_donut_subscription_create
    """

    amount: int = Field()

    amount_without_fee: float = Field()

    user_id: typing.Optional[int] = Field(
        default=None,
    )


class CallbackDonutSubscriptionExpired(BaseModel):
    """
    Schema: callback_donut_subscription_expired
    """

    user_id: typing.Optional[int] = Field(
        default=None,
    )


class CallbackDonutSubscriptionPriceChanged(BaseModel):
    """
    Schema: callback_donut_subscription_price_changed
    """

    amount_old: int = Field()

    amount_new: int = Field()

    user_id: typing.Optional[int] = Field(
        default=None,
    )

    amount_diff: typing.Optional[float] = Field(
        default=None,
    )

    amount_diff_without_fee: typing.Optional[float] = Field(
        default=None,
    )


class CallbackDonutSubscriptionProlonged(BaseModel):
    """
    Schema: callback_donut_subscription_prolonged
    """

    amount: int = Field()

    amount_without_fee: float = Field()

    user_id: typing.Optional[int] = Field(
        default=None,
    )


class CallbackGroupChangePhoto(BaseModel):
    """
    Schema: callback_group_change_photo
    """

    user_id: int = Field()

    photo: "PhotosPhoto" = Field()


class CallbackGroupChangeSettings(BaseModel):
    """
    Schema: callback_group_change_settings
    """

    user_id: int = Field()

    self: bool = Field()


class CallbackGroupJoin(BaseModel):
    """
    Schema: callback_group_join
    """

    user_id: int = Field()

    join_type: "CallbackGroupJoinType" = Field()


class CallbackGroupJoinType(enum.Enum):
    JOIN = "join"

    UNSURE = "unsure"

    ACCEPTED = "accepted"

    APPROVED = "approved"

    REQUEST = "request"


class CallbackGroupLeave(BaseModel):
    """
    Schema: callback_group_leave
    """

    user_id: typing.Optional[int] = Field(
        default=None,
    )

    self: typing.Optional[bool] = Field(
        default=None,
    )


class CallbackGroupMarket(enum.IntEnum):
    DISABLED = 0

    OPEN = 1


class CallbackGroupOfficerRole(enum.IntEnum):
    NONE = 0

    MODERATOR = 1

    EDITOR = 2

    ADMINISTRATOR = 3


class CallbackGroupOfficersEdit(BaseModel):
    """
    Schema: callback_group_officers_edit
    """

    admin_id: int = Field()

    user_id: int = Field()

    level_old: "CallbackGroupOfficerRole" = Field()

    level_new: "CallbackGroupOfficerRole" = Field()


class CallbackGroupSettingsChanges(BaseModel):
    """
    Schema: callback_group_settings_changes
    """

    title: typing.Optional[str] = Field(
        default=None,
    )

    description: typing.Optional[str] = Field(
        default=None,
    )

    access: typing.Optional["GroupsGroupIsClosed"] = Field(
        default=None,
    )

    screen_name: typing.Optional[str] = Field(
        default=None,
    )

    public_category: typing.Optional[int] = Field(
        default=None,
    )

    public_subcategory: typing.Optional[int] = Field(
        default=None,
    )

    age_limits: typing.Optional["GroupsGroupFullAgeLimits"] = Field(
        default=None,
    )

    website: typing.Optional[str] = Field(
        default=None,
    )

    enable_status_default: typing.Optional["GroupsGroupWall"] = Field(
        default=None,
    )

    enable_audio: typing.Optional["GroupsGroupAudio"] = Field(
        default=None,
    )

    enable_video: typing.Optional["GroupsGroupVideo"] = Field(
        default=None,
    )

    enable_photo: typing.Optional["GroupsGroupPhotos"] = Field(
        default=None,
    )

    enable_market: typing.Optional["CallbackGroupMarket"] = Field(
        default=None,
    )


class CallbackLikeAddRemoveObjectType(enum.Enum):
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
    Schema: callback_like_add_remove
    """

    liker_id: int = Field()

    object_type: "CallbackLikeAddRemoveObjectType" = Field()

    object_owner_id: int = Field()

    object_id: int = Field()

    post_id: int = Field()

    thread_reply_id: typing.Optional[int] = Field(
        default=None,
    )


class CallbackMarketComment(BaseModel):
    """
    Schema: callback_market_comment
    """

    id: int = Field()

    from_id: int = Field()

    date: int = Field()

    text: typing.Optional[str] = Field(
        default=None,
    )

    market_owner_id: typing.Optional[int] = Field(
        default=None,
    )

    photo_id: typing.Optional[int] = Field(
        default=None,
    )


class CallbackMarketCommentDelete(BaseModel):
    """
    Schema: callback_market_comment_delete
    """

    owner_id: int = Field()

    id: int = Field()

    user_id: int = Field()

    item_id: int = Field()


class CallbackMessageAllowObject(BaseModel):
    """
    Schema: callback_message_allow_object
    """

    user_id: int = Field()

    key: str = Field()


class CallbackMessageDeny(BaseModel):
    """
    Schema: callback_message_deny
    """

    user_id: int = Field()


class CallbackMessageObject(BaseModel):
    """
    Schema: callback_message_object
    """

    client_info: typing.Optional["ClientInfoForBots"] = Field(
        default=None,
    )

    message: typing.Optional["MessagesMessage"] = Field(
        default=None,
    )


class CallbackPhotoComment(BaseModel):
    """
    Schema: callback_photo_comment
    """

    id: int = Field()

    from_id: int = Field()

    date: int = Field()

    text: str = Field()

    photo_owner_id: int = Field()


class CallbackPhotoCommentDelete(BaseModel):
    """
    Schema: callback_photo_comment_delete
    """

    id: int = Field()

    owner_id: int = Field()

    user_id: int = Field()

    photo_id: int = Field()


class CallbackPollVoteNew(BaseModel):
    """
    Schema: callback_poll_vote_new
    """

    owner_id: int = Field()

    poll_id: int = Field()

    option_id: int = Field()

    user_id: int = Field()


class CallbackType(enum.Enum):
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


class CallbackUserBlock(BaseModel):
    """
    Schema: callback_user_block
    """

    admin_id: int = Field()

    user_id: int = Field()

    unblock_date: int = Field()

    reason: int = Field()

    comment: typing.Optional[str] = Field(
        default=None,
    )


class CallbackUserUnblock(BaseModel):
    """
    Schema: callback_user_unblock
    """

    admin_id: int = Field()

    user_id: int = Field()

    by_end_date: int = Field()


class CallbackVideoComment(BaseModel):
    """
    Schema: callback_video_comment
    """

    id: int = Field()

    from_id: int = Field()

    date: int = Field()

    text: str = Field()

    video_owner_id: int = Field()


class CallbackVideoCommentDelete(BaseModel):
    """
    Schema: callback_video_comment_delete
    """

    id: int = Field()

    owner_id: int = Field()

    user_id: int = Field()

    video_id: int = Field()


class CallbackWallCommentDelete(BaseModel):
    """
    Schema: callback_wall_comment_delete
    """

    owner_id: int = Field()

    id: int = Field()

    user_id: int = Field()

    post_id: int = Field()


class CallsCall(BaseModel):
    """
    Schema: calls_call
    """

    initiator_id: int = Field(
        description="Caller initiator",
    )

    receiver_id: int = Field(
        description="Caller receiver",
    )

    state: "CallsEndState" = Field()

    time: int = Field(
        description="Timestamp for call",
    )

    duration: typing.Optional[int] = Field(
        default=None,
        description="Call duration",
    )

    video: typing.Optional[bool] = Field(
        default=None,
        description="Was this call initiated as video call",
    )

    participants: typing.Optional["CallsParticipants"] = Field(
        default=None,
    )


class CallsEndState(enum.Enum):
    CANCELED_BY_INITIATOR = "canceled_by_initiator"

    CANCELED_BY_RECEIVER = "canceled_by_receiver"

    REACHED = "reached"


class CallsParticipants(BaseModel):
    """
    Schema: calls_participants
    """

    list: typing.Optional[typing.List[int]] = Field(
        default=None,
    )

    count: typing.Optional[int] = Field(
        default=None,
        description="Participants count",
    )


class ClientInfoForBots(BaseModel):
    """
    Schema: client_info_for_bots
    """

    button_actions: typing.Optional[
        typing.List["MessagesTemplateActionTypeNames"]
    ] = Field(
        default=None,
    )

    keyboard: typing.Optional[bool] = Field(
        default=None,
        description="client has support keyboard",
    )

    inline_keyboard: typing.Optional[bool] = Field(
        default=None,
        description="client has support inline keyboard",
    )

    carousel: typing.Optional[bool] = Field(
        default=None,
        description="client has support carousel",
    )

    lang_id: typing.Optional[int] = Field(
        default=None,
        description="client or user language id",
    )


class CommentThread(BaseModel):
    """
    Schema: comment_thread
    """

    count: int = Field(
        description="Comments number",
    )

    items: typing.Optional[typing.List["WallWallComment"]] = Field(
        default=None,
    )

    can_post: typing.Optional[bool] = Field(
        default=None,
        description="Information whether current user can comment the post",
    )

    show_reply_button: typing.Optional[bool] = Field(
        default=None,
        description="Information whether recommended to display reply button",
    )

    groups_can_post: typing.Optional[bool] = Field(
        default=None,
        description="Information whether groups can comment the post",
    )


class DatabaseCityById(BaseModel):
    """
    Schema: database_city_by_id
    """


class DatabaseFaculty(BaseModel):
    """
    Schema: database_faculty
    """

    id: typing.Optional[int] = Field(
        default=None,
        description="Faculty ID",
    )

    title: typing.Optional[str] = Field(
        default=None,
        description="Faculty title",
    )


class DatabaseLanguageFull(BaseModel):
    """
    Schema: database_language_full
    """

    id: int = Field(
        description="Language ID",
    )

    native_name: str = Field(
        description="Language native name",
    )


class DatabaseRegion(BaseModel):
    """
    Schema: database_region
    """

    id: typing.Optional[int] = Field(
        default=None,
        description="Region ID",
    )

    title: typing.Optional[str] = Field(
        default=None,
        description="Region title",
    )


class DatabaseSchool(BaseModel):
    """
    Schema: database_school
    """

    id: typing.Optional[int] = Field(
        default=None,
        description="School ID",
    )

    title: typing.Optional[str] = Field(
        default=None,
        description="School title",
    )


class DatabaseSchoolClass(BaseModel):
    """
    Schema: database_school_class
    """


class DatabaseStation(BaseModel):
    """
    Schema: database_station
    """

    id: int = Field(
        description="Station ID",
    )

    name: str = Field(
        description="Station name",
    )

    city_id: typing.Optional[int] = Field(
        default=None,
        description="City ID",
    )

    color: typing.Optional[str] = Field(
        default=None,
        description="Hex color code without #",
    )


class DatabaseUniversity(BaseModel):
    """
    Schema: database_university
    """

    id: typing.Optional[int] = Field(
        default=None,
        description="University ID",
    )

    title: typing.Optional[str] = Field(
        default=None,
        description="University title",
    )


class DocsDoc(BaseModel):
    """
    Schema: docs_doc
    """

    id: int = Field(
        description="Document ID",
    )

    owner_id: int = Field(
        description="Document owner ID",
    )

    title: str = Field(
        description="Document title",
    )

    size: int = Field(
        description="File size in bites",
    )

    ext: str = Field(
        description="File extension",
    )

    date: int = Field(
        description="Date when file has been uploaded in Unixtime",
    )

    type: int = Field(
        description="Document type",
    )

    url: typing.Optional[str] = Field(
        default=None,
        description="File URL",
    )

    preview: typing.Optional["DocsDocPreview"] = Field(
        default=None,
    )

    is_licensed: typing.Optional[bool] = Field(
        default=None,
    )

    access_key: typing.Optional[str] = Field(
        default=None,
        description="Access key for the document",
    )

    tags: typing.Optional[typing.List[str]] = Field(
        default=None,
        description="Document tags",
    )


class DocsDocAttachmentType(enum.Enum):
    DOC = "doc"

    GRAFFITI = "graffiti"

    AUDIO_MESSAGE = "audio_message"


class DocsDocPreview(BaseModel):
    """
    Schema: docs_doc_preview
    """

    audio_msg: typing.Optional["DocsDocPreviewAudioMsg"] = Field(
        default=None,
    )

    graffiti: typing.Optional["DocsDocPreviewGraffiti"] = Field(
        default=None,
    )

    photo: typing.Optional["DocsDocPreviewPhoto"] = Field(
        default=None,
    )

    video: typing.Optional["DocsDocPreviewVideo"] = Field(
        default=None,
    )


class DocsDocPreviewAudioMsg(BaseModel):
    """
    Schema: docs_doc_preview_audio_msg
    """

    duration: int = Field(
        description="Audio message duration in seconds",
    )

    link_mp3: str = Field(
        description="MP3 file URL",
    )

    link_ogg: str = Field(
        description="OGG file URL",
    )

    waveform: typing.List[int] = Field()


class DocsDocPreviewGraffiti(BaseModel):
    """
    Schema: docs_doc_preview_graffiti
    """

    src: str = Field(
        description="Graffiti file URL",
    )

    width: int = Field(
        description="Graffiti width",
    )

    height: int = Field(
        description="Graffiti height",
    )


class DocsDocPreviewPhoto(BaseModel):
    """
    Schema: docs_doc_preview_photo
    """

    sizes: typing.Optional[typing.List["DocsDocPreviewPhotoSizes"]] = Field(
        default=None,
    )


class DocsDocPreviewPhotoSizes(BaseModel):
    """
    Schema: docs_doc_preview_photo_sizes
    """

    src: str = Field(
        description="URL of the image",
    )

    width: int = Field(
        description="Width in px",
    )

    height: int = Field(
        description="Height in px",
    )

    type: "PhotosPhotoSizesType" = Field()


class DocsDocPreviewVideo(BaseModel):
    """
    Schema: docs_doc_preview_video
    """

    src: str = Field(
        description="Video URL",
    )

    width: int = Field(
        description="Video's width in pixels",
    )

    height: int = Field(
        description="Video's height in pixels",
    )

    file_size: int = Field(
        description="Video file size in bites",
    )


class DocsDocTypes(BaseModel):
    """
    Schema: docs_doc_types
    """

    id: int = Field(
        description="Doc type ID",
    )

    name: str = Field(
        description="Doc type title",
    )

    count: int = Field(
        description="Number of docs",
    )


class DonutDonatorSubscriptionInfoStatus(enum.Enum):
    ACTIVE = "active"
    EXPIRING = "expiring"


class DonutDonatorSubscriptionInfo(BaseModel):
    """
    Schema: donut_donator_subscription_info
    """

    owner_id: int = Field()

    next_payment_date: int = Field()

    amount: int = Field()

    status: "DonutDonatorSubscriptionInfoStatus" = Field()


class EventsEventAttach(BaseModel):
    """
    Schema: events_event_attach
    """

    button_text: str = Field(
        description="text of attach",
    )

    friends: typing.List[int] = Field(
        description="array of friends ids",
    )

    id: int = Field(
        description="event ID",
    )

    is_favorite: bool = Field(
        description="is favorite",
    )

    text: str = Field(
        description="text of attach",
    )

    address: typing.Optional[str] = Field(
        default=None,
        description="address of event",
    )

    member_status: typing.Optional["GroupsGroupFullMemberStatus"] = Field(
        default=None,
        description="Current user's member status",
    )

    time: typing.Optional[int] = Field(
        default=None,
        description="event start time",
    )


class FaveBookmark(BaseModel):
    """
    Schema: fave_bookmark
    """

    added_date: int = Field(
        description="Timestamp, when this item was bookmarked",
    )

    seen: bool = Field(
        description="Has user seen this item",
    )

    tags: typing.List["FaveTag"] = Field()

    type: "FaveBookmarkType" = Field(
        description="Item type",
    )

    link: typing.Optional["BaseLink"] = Field(
        default=None,
    )

    post: typing.Optional["WallWallpostFull"] = Field(
        default=None,
    )

    product: typing.Optional["MarketMarketItem"] = Field(
        default=None,
    )

    video: typing.Optional["VideoVideoFull"] = Field(
        default=None,
    )


class FaveBookmarkType(enum.Enum):
    POST = "post"

    VIDEO = "video"

    PRODUCT = "product"

    ARTICLE = "article"

    LINK = "link"

    CLIP = "clip"


class FavePage(BaseModel):
    """
    Schema: fave_page
    """

    description: str = Field(
        description="Some info about user or group",
    )

    tags: typing.List["FaveTag"] = Field()

    type: "FavePageType" = Field(
        description="Item type",
    )

    group: typing.Optional["GroupsGroupFull"] = Field(
        default=None,
    )

    updated_date: typing.Optional[int] = Field(
        default=None,
        description="Timestamp, when this page was bookmarked",
    )

    user: typing.Optional["UsersUserFull"] = Field(
        default=None,
    )


class FavePageType(enum.Enum):
    USER = "user"

    GROUP = "group"

    HINTS = "hints"


class FaveTag(BaseModel):
    """
    Schema: fave_tag
    """

    id: typing.Optional[int] = Field(
        default=None,
        description="Tag id",
    )

    name: typing.Optional[str] = Field(
        default=None,
        description="Tag name",
    )


class GiftsGift(BaseModel):
    """
    Schema: gifts_gift
    """

    date: typing.Optional[int] = Field(
        default=None,
        description="Date when gist has been sent in Unixtime",
    )

    from_id: typing.Optional[int] = Field(
        default=None,
        description="Gift sender ID",
    )

    gift: typing.Optional["GiftsLayout"] = Field(
        default=None,
    )

    gift_hash: typing.Optional[str] = Field(
        default=None,
        description="Hash",
    )

    id: typing.Optional[int] = Field(
        default=None,
        description="Gift ID",
    )

    message: typing.Optional[str] = Field(
        default=None,
        description="Comment text",
    )

    privacy: typing.Optional["GiftsGiftPrivacy"] = Field(
        default=None,
    )


class GiftsGiftPrivacy(enum.IntEnum):
    NAME_AND_MESSAGE_FOR_ALL = 0

    NAME_FOR_ALL = 1

    NAME_AND_MESSAGE_FOR_RECIPIENT_ONLY = 2


class GiftsLayout(BaseModel):
    """
    Schema: gifts_layout
    """

    id: typing.Optional[int] = Field(
        default=None,
        description="Gift ID",
    )

    thumb_512: typing.Optional[str] = Field(
        default=None,
        description="URL of the preview image with 512 px in width",
    )

    thumb_256: typing.Optional[str] = Field(
        default=None,
        description="URL of the preview image with 256 px in width",
    )

    thumb_48: typing.Optional[str] = Field(
        default=None,
        description="URL of the preview image with 48 px in width",
    )

    thumb_96: typing.Optional[str] = Field(
        default=None,
        description="URL of the preview image with 96 px in width",
    )

    stickers_product_id: typing.Optional[int] = Field(
        default=None,
        description="ID of the sticker pack, if the gift is representing one",
    )

    is_stickers_style: typing.Optional[bool] = Field(
        default=None,
        description="Information whether gift represents a stickers style",
    )

    build_id: typing.Optional[str] = Field(
        default=None,
        description="ID of the build of constructor gift",
    )

    keywords: typing.Optional[str] = Field(
        default=None,
        description="Keywords used for search",
    )


class GroupsAddress(BaseModel):
    """
    Schema: groups_address
    """

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


class GroupsAddressTimetable(BaseModel):
    """
    Schema: groups_address_timetable
    """

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


class GroupsAddressTimetableDay(BaseModel):
    """
    Schema: groups_address_timetable_day
    """

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


class GroupsAddressWorkInfoStatus(enum.Enum):
    NO_INFORMATION = "no_information"

    TEMPORARILY_CLOSED = "temporarily_closed"

    ALWAYS_OPENED = "always_opened"

    TIMETABLE = "timetable"

    FOREVER_CLOSED = "forever_closed"


class GroupsAddressesInfo(BaseModel):
    """
    Schema: groups_addresses_info
    """

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


class GroupsBanInfo(BaseModel):
    """
    Schema: groups_ban_info
    """

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


class GroupsBanInfoReason(enum.IntEnum):
    OTHER = 0

    SPAM = 1

    VERBAL_ABUSE = 2

    STRONG_LANGUAGE = 3

    FLOOD = 4


class GroupsBannedItem(BaseModel):
    """
    Schema: groups_banned_item
    """


class GroupsCallbackServerStatus(enum.Enum):
    UNCONFIGURED = "unconfigured"
    FAILED = "failed"
    WAIT = "wait"
    OK = "ok"


class GroupsCallbackServer(BaseModel):
    """
    Schema: groups_callback_server
    """

    id: int = Field()

    title: str = Field()

    creator_id: int = Field()

    url: str = Field()

    secret_key: str = Field()

    status: "GroupsCallbackServerStatus" = Field()


class GroupsCallbackSettings(BaseModel):
    """
    Schema: groups_callback_settings
    """

    api_version: typing.Optional[str] = Field(
        default=None,
        description="API version used for the events",
    )

    events: typing.Optional["GroupsLongPollEvents"] = Field(
        default=None,
    )


class GroupsClassifiedsProperties(BaseModel):
    """
    Schema: groups_classifieds_properties
    """


class GroupsContactsItem(BaseModel):
    """
    Schema: groups_contacts_item
    """

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


class GroupsCountersGroup(BaseModel):
    """
    Schema: groups_counters_group
    """

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


class GroupsFields(enum.Enum):
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


class GroupsFilter(enum.Enum):
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
    Schema: groups_group
    """

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


class GroupsGroupAccess(enum.IntEnum):
    OPEN = 0

    CLOSED = 1

    PRIVATE = 2


class GroupsGroupAdminLevel(enum.IntEnum):
    MODERATOR = 1

    EDITOR = 2

    ADMINISTRATOR = 3


class GroupsGroupAgeLimits(enum.IntEnum):
    UNLIMITED = 1

    _16_PLUS = 2

    _18_PLUS = 3


class GroupsGroupAttach(BaseModel):
    """
    Schema: groups_group_attach
    """

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


class GroupsGroupAudio(enum.IntEnum):
    DISABLED = 0

    OPEN = 1

    LIMITED = 2


class GroupsGroupBanInfo(BaseModel):
    """
    Schema: groups_group_ban_info
    """

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


class GroupsGroupCategory(BaseModel):
    """
    Schema: groups_group_category
    """

    id: int = Field(
        description="Category ID",
    )

    name: str = Field(
        description="Category name",
    )

    subcategories: typing.Optional[typing.List["GroupsGroupSubcategory"]] = Field(
        default=None,
    )


class GroupsGroupCategoryFull(BaseModel):
    """
    Schema: groups_group_category_full
    """

    id: int = Field(
        description="Category ID",
    )

    name: str = Field(
        description="Category name",
    )

    page_count: int = Field(
        description="Pages number",
    )

    page_previews: typing.List["GroupsGroup"] = Field()

    subcategories: typing.Optional[typing.List["GroupsGroupCategory"]] = Field(
        default=None,
    )


class GroupsGroupCategoryType(BaseModel):
    """
    Schema: groups_group_category_type
    """

    id: int = Field()

    name: str = Field()


class GroupsGroupDocs(enum.IntEnum):
    DISABLED = 0

    OPEN = 1

    LIMITED = 2


class GroupsGroupFullAgeLimits(enum.IntEnum):
    NO = 1

    OVER_16 = 2

    OVER_18 = 3


class GroupsGroupFullMemberStatus(enum.IntEnum):
    NOT_A_MEMBER = 0

    MEMBER = 1

    NOT_SURE = 2

    DECLINED = 3

    HAS_SENT_A_REQUEST = 4

    INVITED = 5


class GroupsGroupFullSection(enum.IntEnum):
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


class GroupsGroupIsClosed(enum.IntEnum):
    OPEN = 0

    CLOSED = 1

    PRIVATE = 2


class GroupsGroupMarketCurrency(enum.IntEnum):
    RUSSIAN_RUBLES = 643

    UKRAINIAN_HRYVNIA = 980

    KAZAKH_TENGE = 398

    EURO = 978

    US_DOLLARS = 840


class GroupsGroupPhotos(enum.IntEnum):
    DISABLED = 0

    OPEN = 1

    LIMITED = 2


class GroupsGroupPublicCategoryList(BaseModel):
    """
    Schema: groups_group_public_category_list
    """

    id: typing.Optional[int] = Field(
        default=None,
    )

    name: typing.Optional[str] = Field(
        default=None,
    )

    subcategories: typing.Optional[typing.List["GroupsGroupCategoryType"]] = Field(
        default=None,
    )


class GroupsGroupRole(enum.Enum):
    MODERATOR = "moderator"

    EDITOR = "editor"

    ADMINISTRATOR = "administrator"

    ADVERTISER = "advertiser"


class GroupsGroupSubcategory(BaseModel):
    """
    Schema: groups_group_subcategory
    """

    id: int = Field(
        description="Object ID",
    )

    name: str = Field(
        description="Object name",
    )

    genders: typing.Optional[typing.List["BaseObjectWithName"]] = Field(
        default=None,
    )


class GroupsGroupSubject(enum.IntEnum):
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


class GroupsGroupSuggestedPrivacy(enum.IntEnum):
    NONE = 0

    ALL = 1

    SUBSCRIBERS = 2


class GroupsGroupTagColor(enum.Enum):
    _454647 = "454647"
    _45678F = "45678f"
    _4BB34B = "4bb34b"
    _5181B8 = "5181b8"
    _539B9C = "539b9c"
    _5C9CE6 = "5c9ce6"
    _63B9BA = "63b9ba"
    _6BC76B = "6bc76b"
    _76787A = "76787a"
    _792EC0 = "792ec0"
    _7A6C4F = "7a6c4f"
    _7ECECF = "7ececf"
    _9E8D6B = "9e8d6b"
    A162DE = "a162de"
    AAAEB3 = "aaaeb3"
    BBAA84 = "bbaa84"
    E64646 = "e64646"
    FF5C5C = "ff5c5c"
    FFA000 = "ffa000"
    FFC107 = "ffc107"


class GroupsGroupTag(BaseModel):
    """
    Schema: groups_group_tag
    """

    id: int = Field()

    name: str = Field()

    color: "GroupsGroupTagColor" = Field()

    uses: typing.Optional[int] = Field(
        default=None,
    )


class GroupsGroupTopics(enum.IntEnum):
    DISABLED = 0

    OPEN = 1

    LIMITED = 2


class GroupsGroupType(enum.Enum):
    GROUP = "group"

    PAGE = "page"

    EVENT = "event"


class GroupsGroupVideo(enum.IntEnum):
    DISABLED = 0

    OPEN = 1

    LIMITED = 2


class GroupsGroupWall(enum.IntEnum):
    DISABLED = 0

    OPEN = 1

    LIMITED = 2

    CLOSED = 3


class GroupsGroupWiki(enum.IntEnum):
    DISABLED = 0

    OPEN = 1

    LIMITED = 2


class GroupsGroupsArray(BaseModel):
    """
    Schema: groups_groups_array
    """

    count: int = Field(
        description="Communities number",
    )

    items: typing.List[int] = Field()


class GroupsLinksItem(BaseModel):
    """
    Schema: groups_links_item
    """

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


class GroupsLiveCovers(BaseModel):
    """
    Schema: groups_live_covers
    """

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


class GroupsLongPollEvents(BaseModel):
    """
    Schema: groups_long_poll_events
    """

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


class GroupsLongPollServer(BaseModel):
    """
    Schema: groups_long_poll_server
    """

    key: str = Field(
        description="Long Poll key",
    )

    server: str = Field(
        description="Long Poll server address",
    )

    ts: str = Field(
        description="Number of the last event",
    )


class GroupsLongPollSettings(BaseModel):
    """
    Schema: groups_long_poll_settings
    """

    events: "GroupsLongPollEvents" = Field()

    is_enabled: bool = Field(
        description="Shows whether Long Poll is enabled",
    )

    api_version: typing.Optional[str] = Field(
        default=None,
        description="API version used for the events",
    )


class GroupsMarketInfo(BaseModel):
    """
    Schema: groups_market_info
    """

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


class GroupsMarketProperties(BaseModel):
    """
    Schema: groups_market_properties
    """

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


class GroupsMarketState(enum.Enum):
    NONE = "none"

    BASIC = "basic"

    ADVANCED = "advanced"


class GroupsMemberRole(BaseModel):
    """
    Schema: groups_member_role
    """

    id: int = Field(
        description="User ID",
    )

    is_call_operator: typing.Optional[bool] = Field(
        default=None,
        description="Allow the manager to accept community calls.",
    )

    permissions: typing.Optional[typing.List["GroupsMemberRolePermission"]] = Field(
        default=None,
    )

    role: typing.Optional["GroupsMemberRoleStatus"] = Field(
        default=None,
    )


class GroupsMemberRolePermission(enum.Enum):
    ADS = "ads"


class GroupsMemberRoleStatus(enum.Enum):
    MODERATOR = "moderator"

    EDITOR = "editor"

    ADMINISTRATOR = "administrator"

    CREATOR = "creator"

    ADVERTISER = "advertiser"


class GroupsMemberStatus(BaseModel):
    """
    Schema: groups_member_status
    """

    member: bool = Field(
        description="Information whether user is a member of the group",
    )

    user_id: int = Field(
        description="User ID",
    )


class GroupsMemberStatusFull(BaseModel):
    """
    Schema: groups_member_status_full
    """

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


class GroupsOnlineStatus(BaseModel):
    """
    Schema: groups_online_status
    """

    status: "GroupsOnlineStatusType" = Field()

    minutes: typing.Optional[int] = Field(
        default=None,
        description="Estimated time of answer (for status = answer_mark)",
    )


class GroupsOnlineStatusType(enum.Enum):
    NONE = "none"

    ONLINE = "online"

    ANSWER_MARK = "answer_mark"


class GroupsOwnerXtrBanInfo(BaseModel):
    """
    Schema: groups_owner_xtr_ban_info
    """

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


class GroupsOwnerXtrBanInfoType(enum.Enum):
    GROUP = "group"

    PROFILE = "profile"


class GroupsPhotoSize(BaseModel):
    """
    Schema: groups_photo_size
    """

    height: int = Field(
        description="Image height",
    )

    width: int = Field(
        description="Image width",
    )


class GroupsProfileItem(BaseModel):
    """
    Schema: groups_profile_item
    """

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


class GroupsRoleOptions(enum.Enum):
    MODERATOR = "moderator"

    EDITOR = "editor"

    ADMINISTRATOR = "administrator"

    CREATOR = "creator"


class GroupsSectionsListItem(BaseModel):
    """
    Schema: groups_sections_list_item
    """


class GroupsSettingsTwitterStatus(enum.Enum):
    LOADING = "loading"
    SYNC = "sync"


class GroupsSettingsTwitter(BaseModel):
    """
    Schema: groups_settings_twitter
    """

    status: "GroupsSettingsTwitterStatus" = Field()

    name: typing.Optional[str] = Field(
        default=None,
    )


class GroupsSubjectItem(BaseModel):
    """
    Schema: groups_subject_item
    """

    id: int = Field(
        description="Subject ID",
    )

    name: str = Field(
        description="Subject title",
    )


class GroupsTokenPermissionSetting(BaseModel):
    """
    Schema: groups_token_permission_setting
    """

    name: str = Field()

    setting: int = Field()


class LeadFormsAnswer(BaseModel):
    """
    Schema: leadForms_answer
    """

    key: str = Field()

    answer: "LeadFormsAnswerOneOf" = Field()


class LeadFormsAnswerItem(BaseModel):
    """
    Schema: leadForms_answer_item
    """

    value: str = Field()

    key: typing.Optional[str] = Field(
        default=None,
    )


class LeadFormsAnswerOneOf(BaseModel):
    """
    Schema: leadForms_answer_one_of
    """


class LeadFormsForm(BaseModel):
    """
    Schema: leadForms_form
    """

    form_id: int = Field()

    group_id: int = Field()

    leads_count: int = Field()

    url: str = Field()

    photo: typing.Optional[str] = Field(
        default=None,
    )

    name: typing.Optional[str] = Field(
        default=None,
    )

    title: typing.Optional[str] = Field(
        default=None,
    )

    description: typing.Optional[str] = Field(
        default=None,
    )

    confirmation: typing.Optional[str] = Field(
        default=None,
    )

    site_link_url: typing.Optional[str] = Field(
        default=None,
    )

    policy_link_url: typing.Optional[str] = Field(
        default=None,
    )

    questions: typing.Optional[typing.List["LeadFormsQuestionItem"]] = Field(
        default=None,
    )

    active: typing.Optional[bool] = Field(
        default=None,
    )

    pixel_code: typing.Optional[str] = Field(
        default=None,
    )

    once_per_user: typing.Optional[int] = Field(
        default=None,
    )

    notify_admins: typing.Optional[str] = Field(
        default=None,
    )

    notify_emails: typing.Optional[str] = Field(
        default=None,
    )


class LeadFormsLead(BaseModel):
    """
    Schema: leadForms_lead
    """

    lead_id: int = Field()

    user_id: int = Field()

    date: int = Field()

    answers: typing.List["LeadFormsAnswer"] = Field()

    ad_id: typing.Optional[int] = Field(
        default=None,
    )


class LeadFormsQuestionItemType(enum.Enum):
    INPUT = "input"
    TEXTAREA = "textarea"
    RADIO = "radio"
    CHECKBOX = "checkbox"
    SELECT = "select"


class LeadFormsQuestionItem(BaseModel):
    """
    Schema: leadForms_question_item
    """

    key: str = Field()

    type: "LeadFormsQuestionItemType" = Field()

    label: typing.Optional[str] = Field(
        default=None,
    )

    options: typing.Optional[typing.List["LeadFormsQuestionItemOption"]] = Field(
        default=None,
        description="Опции выбора для типов radio, checkbox, select",
    )


class LeadFormsQuestionItemOption(BaseModel):
    """
    Schema: leadForms_question_item_option
    """

    label: str = Field()

    key: typing.Optional[str] = Field(
        default=None,
    )


class LikesType(enum.Enum):
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
    Schema: link_target_object
    """

    type: typing.Optional[str] = Field(
        default=None,
        description="Object type",
    )

    owner_id: typing.Optional[int] = Field(
        default=None,
        description="Owner ID",
    )

    item_id: typing.Optional[int] = Field(
        default=None,
        description="Item ID",
    )


class MarketCurrency(BaseModel):
    """
    Schema: market_currency
    """

    id: int = Field(
        description="Currency ID",
    )

    name: str = Field(
        description="Currency sign",
    )

    title: str = Field(
        description="Currency title",
    )


class MarketGlobalSearchFilters(BaseModel):
    """
    Schema: market_global_search_filters
    """

    city: typing.Optional["BaseCity"] = Field(
        default=None,
    )

    country: typing.Optional["BaseCountry"] = Field(
        default=None,
    )


class MarketItemOwnerInfo(BaseModel):
    """
    Schema: market_item_owner_info
    """

    avatar: typing.Optional[typing.List["BaseImage"]] = Field(
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


class MarketItemPromotionInfo(BaseModel):
    """
    Schema: market_item_promotion_info
    """

    is_available: typing.Optional[bool] = Field(
        default=None,
        description="Can the item be promoted?",
    )


class MarketMarketAlbum(BaseModel):
    """
    Schema: market_market_album
    """

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


class MarketMarketCategory(BaseModel):
    """
    Schema: market_market_category
    """


class MarketMarketCategoryNested(BaseModel):
    """
    Schema: market_market_category_nested
    """

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


class MarketMarketCategoryTree(BaseModel):
    """
    Schema: market_market_category_tree
    """

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

    children: typing.Optional[typing.List["MarketMarketCategoryTree"]] = Field(
        default=None,
    )

    view: typing.Optional["MarketMarketCategoryTreeView"] = Field(
        default=None,
    )

    url: typing.Optional[str] = Field(
        default=None,
        description="SEO-friendly URL to page with category's items",
    )


class MarketMarketCategoryTreeViewType(enum.Enum):
    TAB_ROOT = "tab_root"


class MarketMarketCategoryTreeView(BaseModel):
    """
    Schema: market_market_category_tree_view
    """

    type: typing.Optional["MarketMarketCategoryTreeViewType"] = Field(
        default=None,
    )

    selected: typing.Optional[bool] = Field(
        default=None,
    )

    root_path: typing.Optional[typing.List[str]] = Field(
        default=None,
    )


class MarketMarketItem(BaseModel):
    """
    Schema: market_market_item
    """

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


class MarketMarketItemAvailability(enum.IntEnum):
    AVAILABLE = 0

    REMOVED = 1

    UNAVAILABLE = 2


class MarketMarketItemBasic(BaseModel):
    """
    Schema: market_market_item_basic
    """

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


class MarketOrder(BaseModel):
    """
    Schema: market_order
    """

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

    preview_order_items: typing.Optional[typing.List["MarketOrderItem"]] = Field(
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


class MarketOrderItem(BaseModel):
    """
    Schema: market_order_item
    """

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


class MarketOwnerType(enum.Enum):
    BASE = "base"

    PRO = "pro"

    DISABLED = "disabled"


class MarketPrice(BaseModel):
    """
    Schema: market_price
    """

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


class MarketServicesViewType(enum.IntEnum):
    CARDS = 1

    ROWS = 2


class MessagesActionOneOf(BaseModel):
    """
    Schema: messages_action_one_of
    """


class MessagesAudioMessage(BaseModel):
    """
    Schema: messages_audio_message
    """

    duration: int = Field(
        description="Audio message duration in seconds",
    )

    id: int = Field(
        description="Audio message ID",
    )

    link_mp3: str = Field(
        description="MP3 file URL",
    )

    link_ogg: str = Field(
        description="OGG file URL",
    )

    owner_id: int = Field(
        description="Audio message owner ID",
    )

    waveform: typing.List[int] = Field()

    access_key: typing.Optional[str] = Field(
        default=None,
        description="Access key for audio message",
    )

    transcript_error: typing.Optional[int] = Field(
        default=None,
    )


class MessagesChat(BaseModel):
    """
    Schema: messages_chat
    """

    admin_id: int = Field(
        description="Chat creator ID",
    )

    id: int = Field(
        description="Chat ID",
    )

    type: str = Field(
        description="Chat type",
    )

    users: typing.List[int] = Field()

    members_count: int = Field(
        description="Count members in a chat",
    )

    kicked: typing.Optional[bool] = Field(
        default=None,
        description="Shows that user has been kicked from the chat",
    )

    left: typing.Optional[bool] = Field(
        default=None,
        description="Shows that user has been left the chat",
    )

    photo_100: typing.Optional[str] = Field(
        default=None,
        description="URL of the preview image with 100 px in width",
    )

    photo_200: typing.Optional[str] = Field(
        default=None,
        description="URL of the preview image with 200 px in width",
    )

    photo_50: typing.Optional[str] = Field(
        default=None,
        description="URL of the preview image with 50 px in width",
    )

    push_settings: typing.Optional["MessagesChatPushSettings"] = Field(
        default=None,
    )

    title: typing.Optional[str] = Field(
        default=None,
        description="Chat title",
    )

    is_default_photo: typing.Optional[bool] = Field(
        default=None,
        description="If provided photo is default",
    )

    is_group_channel: typing.Optional[bool] = Field(
        default=None,
        description="If chat is group channel",
    )


class MessagesChatFull(BaseModel):
    """
    Schema: messages_chat_full
    """

    admin_id: int = Field(
        description="Chat creator ID",
    )

    id: int = Field(
        description="Chat ID",
    )

    type: str = Field(
        description="Chat type",
    )

    users: typing.List["MessagesUserXtrInvitedBy"] = Field()

    members_count: int = Field(
        description="Count members in a chat",
    )

    kicked: typing.Optional[bool] = Field(
        default=None,
        description="Shows that user has been kicked from the chat",
    )

    left: typing.Optional[bool] = Field(
        default=None,
        description="Shows that user has been left the chat",
    )

    photo_100: typing.Optional[str] = Field(
        default=None,
        description="URL of the preview image with 100 px in width",
    )

    photo_200: typing.Optional[str] = Field(
        default=None,
        description="URL of the preview image with 200 px in width",
    )

    photo_50: typing.Optional[str] = Field(
        default=None,
        description="URL of the preview image with 50 px in width",
    )

    push_settings: typing.Optional["MessagesChatPushSettings"] = Field(
        default=None,
    )

    title: typing.Optional[str] = Field(
        default=None,
        description="Chat title",
    )

    is_default_photo: typing.Optional[bool] = Field(
        default=None,
        description="If provided photo is default",
    )

    is_group_channel: typing.Optional[bool] = Field(
        default=None,
        description="If chat is group channel",
    )


class MessagesChatPreview(BaseModel):
    """
    Schema: messages_chat_preview
    """

    admin_id: typing.Optional[int] = Field(
        default=None,
    )

    joined: typing.Optional[bool] = Field(
        default=None,
    )

    local_id: typing.Optional[int] = Field(
        default=None,
    )

    members: typing.Optional[typing.List[int]] = Field(
        default=None,
    )

    members_count: typing.Optional[int] = Field(
        default=None,
    )

    title: typing.Optional[str] = Field(
        default=None,
    )

    is_member: typing.Optional[bool] = Field(
        default=None,
    )

    photo: typing.Optional["MessagesChatSettingsPhoto"] = Field(
        default=None,
    )

    is_don: typing.Optional[bool] = Field(
        default=None,
    )

    is_nft: typing.Optional[bool] = Field(
        default=None,
    )

    is_group_channel: typing.Optional[bool] = Field(
        default=None,
    )

    button: typing.Optional["BaseLinkButton"] = Field(
        default=None,
    )


class MessagesChatPushSettings(BaseModel):
    """
    Schema: messages_chat_push_settings
    """

    disabled_until: typing.Optional[int] = Field(
        default=None,
        description="Time until that notifications are disabled",
    )

    sound: typing.Optional[bool] = Field(
        default=None,
        description="Information whether the sound is on",
    )


class MessagesChatRestrictions(BaseModel):
    """
    Schema: messages_chat_restrictions
    """

    admins_promote_users: typing.Optional[bool] = Field(
        default=None,
        description="Only admins can promote users to admins",
    )

    only_admins_edit_info: typing.Optional[bool] = Field(
        default=None,
        description="Only admins can change chat info",
    )

    only_admins_edit_pin: typing.Optional[bool] = Field(
        default=None,
        description="Only admins can edit pinned message",
    )

    only_admins_invite: typing.Optional[bool] = Field(
        default=None,
        description="Only admins can invite users to this chat",
    )

    only_admins_kick: typing.Optional[bool] = Field(
        default=None,
        description="Only admins can kick users from this chat",
    )


class MessagesChatSettings(BaseModel):
    """
    Schema: messages_chat_settings
    """

    owner_id: int = Field()

    title: str = Field(
        description="Chat title",
    )

    state: "MessagesChatSettingsState" = Field()

    acl: "MessagesChatSettingsAcl" = Field()

    members_count: typing.Optional[int] = Field(
        default=None,
    )

    friends_count: typing.Optional[int] = Field(
        default=None,
    )

    pinned_message: typing.Optional["MessagesPinnedMessage"] = Field(
        default=None,
    )

    photo: typing.Optional["MessagesChatSettingsPhoto"] = Field(
        default=None,
    )

    admin_ids: typing.Optional[typing.List[int]] = Field(
        default=None,
        description="Ids of chat admins",
    )

    active_ids: typing.Optional[typing.List[int]] = Field(
        default=None,
    )

    is_group_channel: typing.Optional[bool] = Field(
        default=None,
    )

    permissions: typing.Optional["MessagesChatSettingsPermissions"] = Field(
        default=None,
    )

    is_disappearing: typing.Optional[bool] = Field(
        default=None,
    )

    theme: typing.Optional[str] = Field(
        default=None,
    )

    disappearing_chat_link: typing.Optional[str] = Field(
        default=None,
    )

    is_service: typing.Optional[bool] = Field(
        default=None,
    )


class MessagesChatSettingsAcl(BaseModel):
    """
    Schema: messages_chat_settings_acl
    """

    can_change_info: bool = Field(
        description="Can you change photo, description and name",
    )

    can_change_invite_link: bool = Field(
        description="Can you change invite link for this chat",
    )

    can_change_pin: bool = Field(
        description="Can you pin/unpin message for this chat",
    )

    can_invite: bool = Field(
        description="Can you invite other peers in chat",
    )

    can_promote_users: bool = Field(
        description="Can you promote simple users to chat admins",
    )

    can_see_invite_link: bool = Field(
        description="Can you see invite link for this chat",
    )

    can_moderate: bool = Field(
        description="Can you moderate (delete) other users' messages",
    )

    can_copy_chat: bool = Field(
        description="Can you copy chat",
    )

    can_call: bool = Field(
        description="Can you init group call in the chat",
    )

    can_use_mass_mentions: bool = Field(
        description="Can you use mass mentions",
    )

    can_change_service_type: typing.Optional[bool] = Field(
        default=None,
        description="Can you change chat service type",
    )


class MessagesChatSettingsPermissionsInvite(enum.Enum):
    OWNER = "owner"
    OWNER_AND_ADMINS = "owner_and_admins"
    ALL = "all"


class MessagesChatSettingsPermissionsChangeInfo(enum.Enum):
    OWNER = "owner"
    OWNER_AND_ADMINS = "owner_and_admins"
    ALL = "all"


class MessagesChatSettingsPermissionsChangePin(enum.Enum):
    OWNER = "owner"
    OWNER_AND_ADMINS = "owner_and_admins"
    ALL = "all"


class MessagesChatSettingsPermissionsUseMassMentions(enum.Enum):
    OWNER = "owner"
    OWNER_AND_ADMINS = "owner_and_admins"
    ALL = "all"


class MessagesChatSettingsPermissionsSeeInviteLink(enum.Enum):
    OWNER = "owner"
    OWNER_AND_ADMINS = "owner_and_admins"
    ALL = "all"


class MessagesChatSettingsPermissionsCall(enum.Enum):
    OWNER = "owner"
    OWNER_AND_ADMINS = "owner_and_admins"
    ALL = "all"


class MessagesChatSettingsPermissionsChangeAdmins(enum.Enum):
    OWNER = "owner"
    OWNER_AND_ADMINS = "owner_and_admins"


class MessagesChatSettingsPermissions(BaseModel):
    """
    Schema: messages_chat_settings_permissions
    """

    invite: typing.Optional["MessagesChatSettingsPermissionsInvite"] = Field(
        default=None,
        description="Who can invite users to chat",
    )

    change_info: typing.Optional["MessagesChatSettingsPermissionsChangeInfo"] = Field(
        default=None,
        description="Who can change chat info",
    )

    change_pin: typing.Optional["MessagesChatSettingsPermissionsChangePin"] = Field(
        default=None,
        description="Who can change pinned message",
    )

    use_mass_mentions: typing.Optional[
        "MessagesChatSettingsPermissionsUseMassMentions"
    ] = Field(
        default=None,
        description="Who can use mass mentions",
    )

    see_invite_link: typing.Optional[
        "MessagesChatSettingsPermissionsSeeInviteLink"
    ] = Field(
        default=None,
        description="Who can see invite link",
    )

    call: typing.Optional["MessagesChatSettingsPermissionsCall"] = Field(
        default=None,
        description="Who can make calls",
    )

    change_admins: typing.Optional[
        "MessagesChatSettingsPermissionsChangeAdmins"
    ] = Field(
        default=None,
        description="Who can change admins",
    )


class MessagesChatSettingsPhoto(BaseModel):
    """
    Schema: messages_chat_settings_photo
    """

    photo_50: typing.Optional[str] = Field(
        default=None,
        description="URL of the preview image with 50px in width",
    )

    photo_100: typing.Optional[str] = Field(
        default=None,
        description="URL of the preview image with 100px in width",
    )

    photo_200: typing.Optional[str] = Field(
        default=None,
        description="URL of the preview image with 200px in width",
    )

    is_default_photo: typing.Optional[bool] = Field(
        default=None,
        description="If provided photo is default",
    )

    is_default_call_photo: typing.Optional[bool] = Field(
        default=None,
        description="If provided photo is default call photo",
    )


class MessagesChatSettingsState(enum.Enum):
    IN = "in"

    KICKED = "kicked"

    LEFT = "left"

    OUT = "out"


class MessagesConversationSpecialServiceType(enum.Enum):
    BUSINESS_NOTIFY = "business_notify"


class MessagesConversation(BaseModel):
    """
    Schema: messages_conversation
    """

    peer: "MessagesConversationPeer" = Field()

    last_message_id: int = Field(
        description="ID of the last message in conversation",
    )

    in_read: int = Field(
        description="Last message user have read",
    )

    out_read: int = Field(
        description="Last outcoming message have been read by the opponent",
    )

    sort_id: typing.Optional["MessagesConversationSortId"] = Field(
        default=None,
    )

    last_conversation_message_id: typing.Optional[int] = Field(
        default=None,
        description="Conversation message ID of the last message in conversation",
    )

    unread_count: typing.Optional[int] = Field(
        default=None,
        description="Unread messages number",
    )

    is_marked_unread: typing.Optional[bool] = Field(
        default=None,
        description="Is this conversation uread",
    )

    out_read_by: typing.Optional["MessagesOutReadBy"] = Field(
        default=None,
    )

    important: typing.Optional[bool] = Field(
        default=None,
    )

    unanswered: typing.Optional[bool] = Field(
        default=None,
    )

    special_service_type: typing.Optional[
        "MessagesConversationSpecialServiceType"
    ] = Field(
        default=None,
    )

    message_request_data: typing.Optional["MessagesMessageRequestData"] = Field(
        default=None,
    )

    mentions: typing.Optional[typing.List[int]] = Field(
        default=None,
        description="Ids of messages with mentions",
    )

    current_keyboard: typing.Optional["MessagesKeyboard"] = Field(
        default=None,
    )

    push_settings: typing.Optional["MessagesPushSettings"] = Field(
        default=None,
    )

    can_write: typing.Optional["MessagesConversationCanWrite"] = Field(
        default=None,
    )

    chat_settings: typing.Optional["MessagesChatSettings"] = Field(
        default=None,
    )


class MessagesConversationCanWrite(BaseModel):
    """
    Schema: messages_conversation_can_write
    """

    allowed: bool = Field()

    reason: typing.Optional[int] = Field(
        default=None,
    )


class MessagesConversationMember(BaseModel):
    """
    Schema: messages_conversation_member
    """

    member_id: int = Field()

    can_kick: typing.Optional[bool] = Field(
        default=None,
        description="Is it possible for user to kick this member",
    )

    invited_by: typing.Optional[int] = Field(
        default=None,
    )

    is_admin: typing.Optional[bool] = Field(
        default=None,
    )

    is_owner: typing.Optional[bool] = Field(
        default=None,
    )

    is_message_request: typing.Optional[bool] = Field(
        default=None,
    )

    join_date: typing.Optional[int] = Field(
        default=None,
    )

    request_date: typing.Optional[int] = Field(
        default=None,
        description="Message request date",
    )


class MessagesConversationPeer(BaseModel):
    """
    Schema: messages_conversation_peer
    """

    id: int = Field()

    type: "MessagesConversationPeerType" = Field()

    local_id: typing.Optional[int] = Field(
        default=None,
    )


class MessagesConversationPeerType(enum.Enum):
    CHAT = "chat"

    EMAIL = "email"

    USER = "user"

    GROUP = "group"


class MessagesConversationSortId(BaseModel):
    """
    Schema: messages_conversation_sort_id
    """

    major_id: int = Field(
        description="Major id for sorting conversations",
    )

    minor_id: int = Field(
        description="Minor id for sorting conversations",
    )


class MessagesConversationWithMessage(BaseModel):
    """
    Schema: messages_conversation_with_message
    """

    conversation: "MessagesConversation" = Field()

    last_message: typing.Optional["MessagesMessage"] = Field(
        default=None,
    )


class MessagesDeleteFullResponseItem(BaseModel):
    """
    Schema: messages_delete_full_response_item
    """

    peer_id: typing.Optional[int] = Field(
        default=None,
    )

    message_id: typing.Optional[int] = Field(
        default=None,
    )

    conversation_message_id: typing.Optional[int] = Field(
        default=None,
    )

    response: typing.Optional[bool] = Field(
        default=None,
    )

    error: typing.Optional["BaseMessageError"] = Field(
        default=None,
    )


class MessagesForeignMessage(BaseModel):
    """
    Schema: messages_foreign_message
    """

    date: int = Field(
        description="Date when the message was created",
    )

    from_id: int = Field(
        description="Message author's ID",
    )

    text: str = Field(
        description="Message text",
    )

    attachments: typing.Optional[typing.List["MessagesMessageAttachment"]] = Field(
        default=None,
    )

    conversation_message_id: typing.Optional[int] = Field(
        default=None,
        description="Conversation message ID",
    )

    fwd_messages: typing.Optional[typing.List["MessagesForeignMessage"]] = Field(
        default=None,
    )

    geo: typing.Optional["BaseGeo"] = Field(
        default=None,
    )

    id: typing.Optional[int] = Field(
        default=None,
        description="Message ID",
    )

    peer_id: typing.Optional[int] = Field(
        default=None,
        description="Peer ID",
    )

    reply_message: typing.Optional["MessagesForeignMessage"] = Field(
        default=None,
    )

    update_time: typing.Optional[int] = Field(
        default=None,
        description="Date when the message has been updated in Unixtime",
    )

    was_listened: typing.Optional[bool] = Field(
        default=None,
        description="Was the audio message inside already listened by you",
    )

    payload: typing.Optional[str] = Field(
        default=None,
        description="Additional data sent along with message for developer convenience",
    )


class MessagesForward(BaseModel):
    """
    Schema: messages_forward
    """

    owner_id: typing.Optional[int] = Field(
        default=None,
        description="Messages owner_id",
    )

    peer_id: typing.Optional[int] = Field(
        default=None,
        description="Messages peer_id",
    )

    conversation_message_ids: typing.Optional[typing.List[int]] = Field(
        default=None,
    )

    message_ids: typing.Optional[typing.List[int]] = Field(
        default=None,
    )

    is_reply: typing.Optional[bool] = Field(
        default=None,
        description="If you need to reply to a message",
    )


class MessagesFwdMessages(BaseModel):
    """
    Schema: messages_fwd_messages
    """


class MessagesGetConversationById(BaseModel):
    """
    Schema: messages_getConversationById
    """

    count: int = Field(
        description="Total number",
    )

    items: typing.List["MessagesConversation"] = Field()


class MessagesGetConversationMembers(BaseModel):
    """
    Schema: messages_getConversationMembers
    """

    items: typing.List["MessagesConversationMember"] = Field()

    count: int = Field(
        description="Chat members count",
    )

    chat_restrictions: typing.Optional["MessagesChatRestrictions"] = Field(
        default=None,
    )

    profiles: typing.Optional[typing.List["UsersUserFull"]] = Field(
        default=None,
    )

    groups: typing.Optional[typing.List["GroupsGroupFull"]] = Field(
        default=None,
    )


class MessagesGraffiti(BaseModel):
    """
    Schema: messages_graffiti
    """

    id: int = Field(
        description="Graffiti ID",
    )

    owner_id: int = Field(
        description="Graffiti owner ID",
    )

    url: str = Field(
        description="Graffiti URL",
    )

    width: int = Field(
        description="Graffiti width",
    )

    height: int = Field(
        description="Graffiti height",
    )

    access_key: typing.Optional[str] = Field(
        default=None,
        description="Access key for graffiti",
    )


class MessagesHistoryAttachment(BaseModel):
    """
    Schema: messages_history_attachment
    """

    attachment: "MessagesHistoryMessageAttachment" = Field()

    date: int = Field(
        description="Message sending time",
    )

    message_id: int = Field(
        description="Message ID",
    )

    from_id: int = Field(
        description="Message author's ID",
    )

    message_expire_ttl: typing.Optional[int] = Field(
        default=None,
        description="Message Exipire ttl",
    )

    cmid: typing.Optional[int] = Field(
        default=None,
        description="Conversation Message ID",
    )

    forward_level: typing.Optional[int] = Field(
        default=None,
        description="Forward level (optional)",
    )

    was_listened: typing.Optional[bool] = Field(
        default=None,
    )

    position: typing.Optional[int] = Field(
        default=None,
        description="Attachment position in the Message",
    )


class MessagesHistoryMessageAttachment(BaseModel):
    """
    Schema: messages_history_message_attachment
    """

    type: "MessagesHistoryMessageAttachmentType" = Field()

    audio: typing.Optional["AudioAudio"] = Field(
        default=None,
    )

    audio_message: typing.Optional["MessagesAudioMessage"] = Field(
        default=None,
    )

    doc: typing.Optional["DocsDoc"] = Field(
        default=None,
    )

    graffiti: typing.Optional["MessagesGraffiti"] = Field(
        default=None,
    )

    market: typing.Optional["MarketMarketItem"] = Field(
        default=None,
    )

    photo: typing.Optional["PhotosPhoto"] = Field(
        default=None,
    )


class MessagesHistoryMessageAttachmentType(enum.Enum):
    PHOTO = "photo"

    VIDEO = "video"

    AUDIO = "audio"

    DOC = "doc"

    LINK = "link"

    MARKET = "market"

    WALL = "wall"

    SHARE = "share"

    APP_ACTION = "app_action"

    GRAFFITI = "graffiti"

    AUDIO_MESSAGE = "audio_message"


class MessagesKeyboard(BaseModel):
    """
    Schema: messages_keyboard
    """

    one_time: bool = Field(
        description="Should this keyboard disappear on first use",
    )

    buttons: typing.List[typing.List["MessagesKeyboardButton"]] = Field()

    author_id: typing.Optional[int] = Field(
        default=None,
        description="Community or bot, which set this keyboard",
    )

    inline: typing.Optional[bool] = Field(
        default=None,
    )


class MessagesKeyboardButtonColor(enum.Enum):
    DEFAULT = "default"
    POSITIVE = "positive"
    NEGATIVE = "negative"
    PRIMARY = "primary"


class MessagesKeyboardButton(BaseModel):
    """
    Schema: messages_keyboard_button
    """

    action: "MessagesKeyboardButtonPropertyAction" = Field()

    color: typing.Optional["MessagesKeyboardButtonColor"] = Field(
        default=None,
        description="Button color",
    )


class MessagesKeyboardButtonActionCallbackType(enum.Enum):
    CALLBACK = "callback"


class MessagesKeyboardButtonActionCallback(BaseModel):
    """
    Schema: messages_keyboard_button_action_callback
    """

    label: str = Field(
        description="Label for button",
    )

    type: "MessagesKeyboardButtonActionCallbackType" = Field()

    payload: typing.Optional[str] = Field(
        default=None,
        description="Additional data sent along with message for developer convenience",
    )


class MessagesKeyboardButtonActionLocationType(enum.Enum):
    LOCATION = "location"


class MessagesKeyboardButtonActionLocation(BaseModel):
    """
    Schema: messages_keyboard_button_action_location
    """

    type: "MessagesKeyboardButtonActionLocationType" = Field()

    payload: typing.Optional[str] = Field(
        default=None,
        description="Additional data sent along with message for developer convenience",
    )


class MessagesKeyboardButtonActionOpenAppType(enum.Enum):
    OPEN_APP = "open_app"


class MessagesKeyboardButtonActionOpenApp(BaseModel):
    """
    Schema: messages_keyboard_button_action_open_app
    """

    app_id: int = Field(
        description="Fragment value in app link like vk.com/app{app_id}_-654321#hash",
    )

    label: str = Field(
        description="Label for button",
    )

    owner_id: int = Field(
        description="Fragment value in app link like vk.com/app123456_{owner_id}#hash",
    )

    type: "MessagesKeyboardButtonActionOpenAppType" = Field()

    hash: typing.Optional[str] = Field(
        default=None,
        description="Fragment value in app link like vk.com/app123456_-654321#{hash}",
    )

    payload: typing.Optional[str] = Field(
        default=None,
        description="Additional data sent along with message for developer convenience",
    )


class MessagesKeyboardButtonActionOpenLinkType(enum.Enum):
    OPEN_LINK = "open_link"


class MessagesKeyboardButtonActionOpenLink(BaseModel):
    """
    Schema: messages_keyboard_button_action_open_link
    """

    label: str = Field(
        description="Label for button",
    )

    link: str = Field(
        description="link for button",
    )

    type: "MessagesKeyboardButtonActionOpenLinkType" = Field()

    payload: typing.Optional[str] = Field(
        default=None,
        description="Additional data sent along with message for developer convenience",
    )


class MessagesKeyboardButtonActionOpenPhotoType(enum.Enum):
    OPEN_PHOTO = "open_photo"


class MessagesKeyboardButtonActionOpenPhoto(BaseModel):
    """
    Schema: messages_keyboard_button_action_open_photo
    """

    type: "MessagesKeyboardButtonActionOpenPhotoType" = Field()


class MessagesKeyboardButtonActionTextType(enum.Enum):
    TEXT = "text"


class MessagesKeyboardButtonActionText(BaseModel):
    """
    Schema: messages_keyboard_button_action_text
    """

    label: str = Field(
        description="Label for button",
    )

    type: "MessagesKeyboardButtonActionTextType" = Field()

    payload: typing.Optional[str] = Field(
        default=None,
        description="Additional data sent along with message for developer convenience",
    )


class MessagesKeyboardButtonActionVkpayType(enum.Enum):
    VKPAY = "vkpay"


class MessagesKeyboardButtonActionVkpay(BaseModel):
    """
    Schema: messages_keyboard_button_action_vkpay
    """

    hash: str = Field(
        description="Fragment value in app link like vk.com/app123456_-654321#{hash}",
    )

    type: "MessagesKeyboardButtonActionVkpayType" = Field()

    payload: typing.Optional[str] = Field(
        default=None,
        description="Additional data sent along with message for developer convenience",
    )


class MessagesKeyboardButtonPropertyAction(BaseModel):
    """
    Schema: messages_keyboard_button_property_action
    """


class MessagesLastActivity(BaseModel):
    """
    Schema: messages_last_activity
    """

    online: bool = Field(
        description="Information whether user is online",
    )

    time: int = Field(
        description="Time when user was online in Unixtime",
    )


class MessagesLongpollMessages(BaseModel):
    """
    Schema: messages_longpoll_messages
    """

    count: typing.Optional[int] = Field(
        default=None,
        description="Total number",
    )

    items: typing.Optional[typing.List["MessagesMessage"]] = Field(
        default=None,
    )


class MessagesLongpollParams(BaseModel):
    """
    Schema: messages_longpoll_params
    """

    server: str = Field(
        description="Server URL",
    )

    key: str = Field(
        description="Key",
    )

    ts: int = Field(
        description="Timestamp",
    )

    pts: typing.Optional[int] = Field(
        default=None,
        description="Persistent timestamp",
    )


class MessagesMessage(BaseModel):
    """
    Schema: messages_message
    """

    date: int = Field(
        description="Date when the message has been sent in Unixtime",
    )

    from_id: int = Field(
        description="Message author's ID",
    )

    id: int = Field(
        description="Message ID",
    )

    out: bool = Field(
        description="Information whether the message is outcoming",
    )

    peer_id: int = Field(
        description="Peer ID",
    )

    text: str = Field(
        description="Message text",
    )

    action: typing.Optional["MessagesActionOneOf"] = Field(
        default=None,
    )

    admin_author_id: typing.Optional[int] = Field(
        default=None,
        description="Only for messages from community. Contains user ID of community admin, who sent this message.",
    )

    attachments: typing.Optional[typing.List["MessagesMessageAttachment"]] = Field(
        default=None,
    )

    conversation_message_id: typing.Optional[int] = Field(
        default=None,
        description="Unique auto-incremented number for all messages with this peer",
    )

    deleted: typing.Optional[bool] = Field(
        default=None,
        description="Is it an deleted message",
    )

    fwd_messages: typing.Optional["MessagesFwdMessages"] = Field(
        default=None,
    )

    geo: typing.Optional["BaseGeo"] = Field(
        default=None,
    )

    important: typing.Optional[bool] = Field(
        default=None,
        description="Is it an important message",
    )

    is_hidden: typing.Optional[bool] = Field(
        default=None,
    )

    is_cropped: typing.Optional[bool] = Field(
        default=None,
        description="this message is cropped for bot",
    )

    keyboard: typing.Optional["MessagesKeyboard"] = Field(
        default=None,
    )

    members_count: typing.Optional[int] = Field(
        default=None,
        description="Members number",
    )

    payload: typing.Optional[str] = Field(
        default=None,
    )

    random_id: typing.Optional[int] = Field(
        default=None,
        description="ID used for sending messages. It returned only for outgoing messages",
    )

    ref: typing.Optional[str] = Field(
        default=None,
    )

    ref_source: typing.Optional[str] = Field(
        default=None,
    )

    reply_message: typing.Optional["MessagesForeignMessage"] = Field(
        default=None,
    )

    reaction_id: typing.Optional[int] = Field(
        default=None,
        description="Reaction id set on message",
    )

    reactions: typing.Optional[
        typing.List["MessagesReactionCounterResponseItem"]
    ] = Field(
        default=None,
        description="Actual reactions counters on this message",
    )

    last_reaction_id: typing.Optional[int] = Field(
        default=None,
        description="Last reaction id set on this message",
    )

    update_time: typing.Optional[int] = Field(
        default=None,
        description="Date when the message has been updated in Unixtime",
    )

    was_listened: typing.Optional[bool] = Field(
        default=None,
        description="Was the audio message inside already listened by you",
    )

    pinned_at: typing.Optional[int] = Field(
        default=None,
        description="Date when the message has been pinned in Unixtime",
    )

    is_silent: typing.Optional[bool] = Field(
        default=None,
        description="Is silent message, push without sound",
    )


class MessagesMessageAction(BaseModel):
    """
    Schema: messages_message_action
    """

    type: "MessagesMessageActionStatus" = Field()

    conversation_message_id: typing.Optional[int] = Field(
        default=None,
        description="Message ID",
    )

    email: typing.Optional[str] = Field(
        default=None,
        description="Email address for chat_invite_user or chat_kick_user actions",
    )

    member_id: typing.Optional[int] = Field(
        default=None,
        description="User or email peer ID",
    )

    message: typing.Optional[str] = Field(
        default=None,
        description="Message body of related message",
    )

    photo: typing.Optional["MessagesMessageActionPhoto"] = Field(
        default=None,
    )

    text: typing.Optional[str] = Field(
        default=None,
        description="New chat title for chat_create and chat_title_update actions",
    )


class MessagesMessageActionPhoto(BaseModel):
    """
    Schema: messages_message_action_photo
    """

    photo_50: str = Field(
        description="URL of the preview image with 50px in width",
    )

    photo_100: str = Field(
        description="URL of the preview image with 100px in width",
    )

    photo_200: str = Field(
        description="URL of the preview image with 200px in width",
    )


class MessagesMessageActionStatus(enum.Enum):
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
    Schema: messages_message_attachment
    """

    type: "MessagesMessageAttachmentType" = Field()

    audio: typing.Optional["AudioAudio"] = Field(
        default=None,
    )

    audio_message: typing.Optional["MessagesAudioMessage"] = Field(
        default=None,
    )

    call: typing.Optional["CallsCall"] = Field(
        default=None,
    )

    doc: typing.Optional["DocsDoc"] = Field(
        default=None,
    )

    gift: typing.Optional["GiftsLayout"] = Field(
        default=None,
    )

    graffiti: typing.Optional["MessagesGraffiti"] = Field(
        default=None,
    )

    market: typing.Optional["MarketMarketItem"] = Field(
        default=None,
    )

    market_market_album: typing.Optional["MarketMarketAlbum"] = Field(
        default=None,
    )

    photo: typing.Optional["PhotosPhoto"] = Field(
        default=None,
    )

    sticker: typing.Optional["BaseSticker"] = Field(
        default=None,
    )

    story: typing.Optional["StoriesStory"] = Field(
        default=None,
    )

    wall_reply: typing.Optional["WallWallComment"] = Field(
        default=None,
    )

    poll: typing.Optional["PollsPoll"] = Field(
        default=None,
    )


class MessagesMessageAttachmentType(enum.Enum):
    PHOTO = "photo"

    AUDIO = "audio"

    VIDEO = "video"

    VIDEO_PLAYLIST = "video_playlist"

    DOC = "doc"

    LINK = "link"

    MARKET = "market"

    MARKET_ALBUM = "market_album"

    GIFT = "gift"

    STICKER = "sticker"

    WALL = "wall"

    WALL_REPLY = "wall_reply"

    ARTICLE = "article"

    POLL = "poll"

    CALL = "call"

    GRAFFITI = "graffiti"

    AUDIO_MESSAGE = "audio_message"


class MessagesMessageRequestData(BaseModel):
    """
    Schema: messages_message_request_data
    """

    status: typing.Optional[str] = Field(
        default=None,
        description="Status of message request",
    )

    inviter_id: typing.Optional[int] = Field(
        default=None,
        description="Message request sender id",
    )

    request_date: typing.Optional[int] = Field(
        default=None,
        description="Message request date",
    )


class MessagesMessagesArray(BaseModel):
    """
    Schema: messages_messages_array
    """

    count: typing.Optional[int] = Field(
        default=None,
    )

    items: typing.Optional[typing.List["MessagesMessage"]] = Field(
        default=None,
    )


class MessagesOutReadBy(BaseModel):
    """
    Schema: messages_out_read_by
    """

    count: typing.Optional[int] = Field(
        default=None,
    )

    member_ids: typing.Optional[typing.List[int]] = Field(
        default=None,
    )


class MessagesPinnedMessage(BaseModel):
    """
    Schema: messages_pinned_message
    """

    id: int = Field(
        description="Message ID",
    )

    date: int = Field(
        description="Date when the message has been sent in Unixtime",
    )

    from_id: int = Field(
        description="Message author's ID",
    )

    peer_id: int = Field(
        description="Peer ID",
    )

    text: str = Field(
        description="Message text",
    )

    attachments: typing.Optional[typing.List["MessagesMessageAttachment"]] = Field(
        default=None,
    )

    conversation_message_id: typing.Optional[int] = Field(
        default=None,
        description="Unique auto-incremented number for all messages with this peer",
    )

    fwd_messages: typing.Optional[typing.List["MessagesForeignMessage"]] = Field(
        default=None,
        description="Forwarded messages",
    )

    geo: typing.Optional["BaseGeo"] = Field(
        default=None,
    )

    reply_message: typing.Optional["MessagesForeignMessage"] = Field(
        default=None,
    )

    keyboard: typing.Optional["MessagesKeyboard"] = Field(
        default=None,
    )


class MessagesPushSettings(BaseModel):
    """
    Schema: messages_push_settings
    """

    disabled_forever: bool = Field(
        description="Information whether push notifications are disabled forever",
    )

    no_sound: bool = Field(
        description="Information whether the sound is on",
    )

    disabled_until: typing.Optional[int] = Field(
        default=None,
        description="Time until what notifications are disabled",
    )

    disabled_mentions: typing.Optional[bool] = Field(
        default=None,
        description="Information whether the mentions are disabled",
    )

    disabled_mass_mentions: typing.Optional[bool] = Field(
        default=None,
        description="Information whether the mass mentions (like '@all', '@online') are disabled",
    )


class MessagesReactionAssetItem(BaseModel):
    """
    Schema: messages_reaction_asset_item
    """

    reaction_id: int = Field()

    links: "MessagesReactionAssetItemLinks" = Field(
        description="Liks to reactions assets for each asset type",
    )


class MessagesReactionAssetItemLinks(BaseModel):
    """
    Schema: messages_reaction_asset_item_links
    """

    big_animation: str = Field(
        description="Big reaction animation json file",
    )

    small_animation: str = Field(
        description="Small reaction animation json file",
    )

    static: str = Field(
        description="Reaction image file",
    )


class MessagesReactionCounterResponseItem(BaseModel):
    """
    Schema: messages_reaction_counter_response_item
    """

    reaction_id: int = Field()

    count: int = Field()

    user_ids: typing.List[int] = Field()


class MessagesReactionCountersResponseItem(BaseModel):
    """
    Schema: messages_reaction_counters_response_item
    """

    cmid: int = Field()

    counters: typing.List["MessagesReactionCounterResponseItem"] = Field()


class MessagesReactionResponseItem(BaseModel):
    """
    Schema: messages_reaction_response_item
    """

    user_id: int = Field()

    reaction_id: int = Field()


class MessagesSendUserIdsResponseItem(BaseModel):
    """
    Schema: messages_send_user_ids_response_item
    """

    peer_id: int = Field()

    message_id: int = Field()

    conversation_message_id: typing.Optional[int] = Field(
        default=None,
    )

    error: typing.Optional["BaseMessageError"] = Field(
        default=None,
    )


class MessagesTemplateActionTypeNames(enum.Enum):
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


class MessagesUserTypeForXtrInvitedBy(enum.Enum):
    PROFILE = "profile"

    GROUP = "group"


class NotesNote(BaseModel):
    """
    Schema: notes_note
    """

    comments: int = Field(
        description="Comments number",
    )

    date: int = Field(
        description="Date when the note has been created in Unixtime",
    )

    id: int = Field(
        description="Note ID",
    )

    owner_id: int = Field(
        description="Note owner's ID",
    )

    title: str = Field(
        description="Note title",
    )

    view_url: str = Field(
        description="URL of the page with note preview",
    )

    read_comments: typing.Optional[int] = Field(
        default=None,
    )

    can_comment: typing.Optional[bool] = Field(
        default=None,
        description="Information whether current user can comment the note",
    )

    text: typing.Optional[str] = Field(
        default=None,
        description="Note text",
    )

    text_wiki: typing.Optional[str] = Field(
        default=None,
        description="Note text in wiki format",
    )

    privacy_view: typing.Optional[typing.List[str]] = Field(
        default=None,
    )

    privacy_comment: typing.Optional[typing.List[str]] = Field(
        default=None,
    )


class NotesNoteComment(BaseModel):
    """
    Schema: notes_note_comment
    """

    date: int = Field(
        description="Date when the comment has beed added in Unixtime",
    )

    id: int = Field(
        description="Comment ID",
    )

    message: str = Field(
        description="Comment text",
    )

    nid: int = Field(
        description="Note ID",
    )

    oid: int = Field(
        description="Note ID",
    )

    uid: int = Field(
        description="Comment author's ID",
    )

    reply_to: typing.Optional[int] = Field(
        default=None,
        description="ID of replied comment ",
    )


class NotificationsFeedback(BaseModel):
    """
    Schema: notifications_feedback
    """

    attachments: typing.Optional[typing.List["WallWallpostAttachment"]] = Field(
        default=None,
    )

    from_id: typing.Optional[int] = Field(
        default=None,
        description="Reply author's ID",
    )

    geo: typing.Optional["BaseGeo"] = Field(
        default=None,
    )

    id: typing.Optional[int] = Field(
        default=None,
        description="Item ID",
    )

    likes: typing.Optional["BaseLikesInfo"] = Field(
        default=None,
    )

    text: typing.Optional[str] = Field(
        default=None,
        description="Reply text",
    )

    to_id: typing.Optional[int] = Field(
        default=None,
        description="Wall owner's ID",
    )


class NotificationsNotification(BaseModel):
    """
    Schema: notifications_notification
    """

    date: typing.Optional[int] = Field(
        default=None,
        description="Date when the event has been occurred",
    )

    feedback: typing.Optional["NotificationsFeedback"] = Field(
        default=None,
    )

    parent: typing.Optional["NotificationsNotification"] = Field(
        default=None,
    )

    reply: typing.Optional["NotificationsReply"] = Field(
        default=None,
    )

    type: typing.Optional[str] = Field(
        default=None,
        description="Notification type",
    )


class NotificationsNotificationItem(BaseModel):
    """
    Schema: notifications_notification_item
    """


class NotificationsReply(BaseModel):
    """
    Schema: notifications_reply
    """

    date: typing.Optional[int] = Field(
        default=None,
        description="Date when the reply has been created in Unixtime",
    )

    id: typing.Optional[int] = Field(
        default=None,
        description="Reply ID",
    )

    text: typing.Optional[int] = Field(
        default=None,
        description="Reply text",
    )


class NotificationsSendMessageError(BaseModel):
    """
    Schema: notifications_send_message_error
    """

    code: typing.Optional[int] = Field(
        default=None,
        description="Error code",
    )

    description: typing.Optional[str] = Field(
        default=None,
        description="Error description",
    )


class NotificationsSendMessageItem(BaseModel):
    """
    Schema: notifications_send_message_item
    """

    user_id: typing.Optional[int] = Field(
        default=None,
        description="User ID",
    )

    status: typing.Optional[bool] = Field(
        default=None,
        description="Notification status",
    )

    error: typing.Optional["NotificationsSendMessageError"] = Field(
        default=None,
    )


class OauthError(BaseModel):
    """
    Schema: oauth_error
    """

    error: str = Field(
        description="Error type",
    )

    error_description: str = Field(
        description="Error description",
    )

    redirect_uri: typing.Optional[str] = Field(
        default=None,
        description="URI for validation",
    )


class OrdersAmount(BaseModel):
    """
    Schema: orders_amount
    """

    amounts: typing.Optional[typing.List["OrdersAmountItem"]] = Field(
        default=None,
    )

    currency: typing.Optional[str] = Field(
        default=None,
        description="Currency name",
    )


class OrdersAmountItem(BaseModel):
    """
    Schema: orders_amount_item
    """

    amount: typing.Optional[float] = Field(
        default=None,
        description="Votes amount in user's currency",
    )

    description: typing.Optional[str] = Field(
        default=None,
        description="Amount description",
    )

    votes: typing.Optional[str] = Field(
        default=None,
        description="Votes number",
    )


class OrdersOrderStatus(enum.Enum):
    CREATED = "created"
    CHARGED = "charged"
    REFUNDED = "refunded"
    CHARGEABLE = "chargeable"
    CANCELLED = "cancelled"
    DECLINED = "declined"


class OrdersOrder(BaseModel):
    """
    Schema: orders_order
    """

    amount: str = Field(
        description="Amount",
    )

    app_order_id: str = Field(
        description="App order ID",
    )

    date: str = Field(
        description="Date of creation in Unixtime",
    )

    id: str = Field(
        description="Order ID",
    )

    item: str = Field(
        description="Order item",
    )

    receiver_id: str = Field(
        description="Receiver ID",
    )

    status: "OrdersOrderStatus" = Field(
        description="Order status",
    )

    user_id: str = Field(
        description="User ID",
    )

    cancel_transaction_id: typing.Optional[str] = Field(
        default=None,
        description="Cancel transaction ID",
    )

    transaction_id: typing.Optional[str] = Field(
        default=None,
        description="Transaction ID",
    )


class OrdersSubscription(BaseModel):
    """
    Schema: orders_subscription
    """

    create_time: int = Field(
        description="Date of creation in Unixtime",
    )

    id: int = Field(
        description="Subscription ID",
    )

    item_id: str = Field(
        description="Subscription order item",
    )

    period: int = Field(
        description="Subscription period",
    )

    period_start_time: int = Field(
        description="Date of last period start in Unixtime",
    )

    price: int = Field(
        description="Subscription price",
    )

    status: str = Field(
        description="Subscription status",
    )

    update_time: int = Field(
        description="Date of last change in Unixtime",
    )

    cancel_reason: typing.Optional[str] = Field(
        default=None,
        description="Cancel reason",
    )

    next_bill_time: typing.Optional[int] = Field(
        default=None,
        description="Date of next bill in Unixtime",
    )

    expire_time: typing.Optional[int] = Field(
        default=None,
        description="Subscription expiration time in Unixtime",
    )

    pending_cancel: typing.Optional[bool] = Field(
        default=None,
        description="Pending cancel state",
    )

    title: typing.Optional[str] = Field(
        default=None,
        description="Subscription name",
    )

    app_id: typing.Optional[int] = Field(
        default=None,
        description="Subscription's application id",
    )

    application_name: typing.Optional[str] = Field(
        default=None,
        description="Subscription's application name",
    )

    photo_url: typing.Optional[str] = Field(
        default=None,
        description="Item photo image url",
    )

    test_mode: typing.Optional[bool] = Field(
        default=None,
        description="Is test subscription",
    )

    trial_expire_time: typing.Optional[int] = Field(
        default=None,
        description="Date of trial expire in Unixtime",
    )

    is_game: typing.Optional[bool] = Field(
        default=None,
        description="Is game (not miniapp) subscription",
    )


class OwnerState(BaseModel):
    """
    Schema: owner_state
    """

    state: typing.Optional[int] = Field(
        default=None,
    )

    description: typing.Optional[str] = Field(
        default=None,
        description="wiki text to describe user state",
    )


class PagesPrivacySettings(enum.IntEnum):
    COMMUNITY_MANAGERS_ONLY = 0

    COMMUNITY_MEMBERS_ONLY = 1

    EVERYONE = 2


class PagesWikipage(BaseModel):
    """
    Schema: pages_wikipage
    """

    group_id: int = Field(
        description="Community ID",
    )

    id: int = Field(
        description="Page ID",
    )

    title: str = Field(
        description="Page title",
    )

    views: int = Field(
        description="Views number",
    )

    who_can_edit: "PagesPrivacySettings" = Field(
        description="Edit settings of the page",
    )

    who_can_view: "PagesPrivacySettings" = Field(
        description="View settings of the page",
    )

    creator_id: typing.Optional[int] = Field(
        default=None,
        description="Page creator ID",
    )

    creator_name: typing.Optional[str] = Field(
        default=None,
        description="Page creator name",
    )

    editor_id: typing.Optional[int] = Field(
        default=None,
        description="Last editor ID",
    )

    editor_name: typing.Optional[str] = Field(
        default=None,
        description="Last editor name",
    )


class PagesWikipageFull(BaseModel):
    """
    Schema: pages_wikipage_full
    """

    created: int = Field(
        description="Date when the page has been created in Unixtime",
    )

    edited: int = Field(
        description="Date when the page has been edited in Unixtime",
    )

    group_id: int = Field(
        description="Community ID",
    )

    id: int = Field(
        description="Page ID",
    )

    title: str = Field(
        description="Page title",
    )

    view_url: str = Field(
        description="URL of the page preview",
    )

    views: int = Field(
        description="Views number",
    )

    who_can_edit: "PagesPrivacySettings" = Field(
        description="Edit settings of the page",
    )

    who_can_view: "PagesPrivacySettings" = Field(
        description="View settings of the page",
    )

    creator_id: typing.Optional[int] = Field(
        default=None,
        description="Page creator ID",
    )

    current_user_can_edit: typing.Optional[bool] = Field(
        default=None,
        description="Information whether current user can edit the page",
    )

    current_user_can_edit_access: typing.Optional[bool] = Field(
        default=None,
        description="Information whether current user can edit the page access settings",
    )

    editor_id: typing.Optional[int] = Field(
        default=None,
        description="Last editor ID",
    )

    html: typing.Optional[str] = Field(
        default=None,
        description="Page content, HTML",
    )

    source: typing.Optional[str] = Field(
        default=None,
        description="Page content, wiki",
    )

    url: typing.Optional[str] = Field(
        default=None,
        description="URL",
    )

    parent: typing.Optional[str] = Field(
        default=None,
        description="Parent",
    )

    parent2: typing.Optional[str] = Field(
        default=None,
        description="Parent2",
    )

    owner_id: typing.Optional[int] = Field(
        default=None,
        description="Owner ID",
    )


class PagesWikipageHistory(BaseModel):
    """
    Schema: pages_wikipage_history
    """

    id: int = Field(
        description="Version ID",
    )

    length: int = Field(
        description="Page size in bytes",
    )

    date: int = Field(
        description="Date when the page has been edited in Unixtime",
    )

    editor_id: int = Field(
        description="Last editor ID",
    )

    editor_name: str = Field(
        description="Last editor name",
    )


class PhotosImage(BaseModel):
    """
    Schema: photos_image
    """

    height: typing.Optional[int] = Field(
        default=None,
        description="Height of the photo in px.",
    )

    type: typing.Optional["PhotosImageType"] = Field(
        default=None,
    )

    url: typing.Optional[str] = Field(
        default=None,
        description="Photo URL.",
    )

    width: typing.Optional[int] = Field(
        default=None,
        description="Width of the photo in px.",
    )


class PhotosImageType(enum.Enum):
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


class PhotosPhotoVerticalAlign(enum.Enum):
    TOP = "top"
    MIDDLE = "middle"
    BOTTOM = "bottom"


class PhotosPhoto(BaseModel):
    """
    Schema: photos_photo
    """

    album_id: int = Field(
        description="Album ID",
    )

    date: int = Field(
        description="Date when uploaded",
    )

    id: int = Field(
        description="Photo ID",
    )

    owner_id: int = Field(
        description="Photo owner's ID",
    )

    has_tags: bool = Field(
        description="Whether photo has attached tag links",
    )

    access_key: typing.Optional[str] = Field(
        default=None,
        description="Access key for the photo",
    )

    height: typing.Optional[int] = Field(
        default=None,
        description="Original photo height",
    )

    images: typing.Optional[typing.List["PhotosImage"]] = Field(
        default=None,
    )

    lat: typing.Optional[float] = Field(
        default=None,
        description="Latitude",
    )

    long: typing.Optional[float] = Field(
        default=None,
        description="Longitude",
    )

    photo_256: typing.Optional[str] = Field(
        default=None,
        description="URL of image with 2560 px width",
    )

    can_comment: typing.Optional[bool] = Field(
        default=None,
        description="Information whether current user can comment the photo",
    )

    place: typing.Optional[str] = Field(
        default=None,
    )

    post_id: typing.Optional[int] = Field(
        default=None,
        description="Post ID",
    )

    sizes: typing.Optional[typing.List["PhotosPhotoSizes"]] = Field(
        default=None,
    )

    square_crop: typing.Optional[str] = Field(
        default=None,
    )

    text: typing.Optional[str] = Field(
        default=None,
        description="Photo caption",
    )

    user_id: typing.Optional[int] = Field(
        default=None,
        description="ID of the user who have uploaded the photo",
    )

    width: typing.Optional[int] = Field(
        default=None,
        description="Original photo width",
    )

    likes: typing.Optional["BaseLikes"] = Field(
        default=None,
    )

    comments: typing.Optional["BaseObjectCount"] = Field(
        default=None,
    )

    reposts: typing.Optional["BaseRepostsInfo"] = Field(
        default=None,
    )

    tags: typing.Optional["BaseObjectCount"] = Field(
        default=None,
    )

    hidden: typing.Optional["BasePropertyExists"] = Field(
        default=None,
        description="Returns if the photo is hidden above the wall",
    )

    real_offset: typing.Optional[int] = Field(
        default=None,
        description="Real position of the photo",
    )

    vertical_align: typing.Optional["PhotosPhotoVerticalAlign"] = Field(
        default=None,
        description="Sets vertical alignment of a photo",
    )


class PhotosPhotoAlbum(BaseModel):
    """
    Schema: photos_photo_album
    """

    created: int = Field(
        description="Date when the album has been created in Unixtime",
    )

    id: int = Field(
        description="Photo album ID",
    )

    owner_id: int = Field(
        description="Album owner's ID",
    )

    size: int = Field(
        description="Photos number",
    )

    title: str = Field(
        description="Photo album title",
    )

    updated: int = Field(
        description="Date when the album has been updated last time in Unixtime",
    )

    description: typing.Optional[str] = Field(
        default=None,
        description="Photo album description",
    )

    thumb: typing.Optional["PhotosPhoto"] = Field(
        default=None,
    )


class PhotosPhotoAlbumFull(BaseModel):
    """
    Schema: photos_photo_album_full
    """

    id: int = Field(
        description="Photo album ID",
    )

    owner_id: int = Field(
        description="Album owner's ID",
    )

    size: int = Field(
        description="Photos number",
    )

    title: str = Field(
        description="Photo album title",
    )

    can_upload: typing.Optional[bool] = Field(
        default=None,
        description="Information whether current user can upload photo to the album",
    )

    comments_disabled: typing.Optional[bool] = Field(
        default=None,
        description="Information whether album comments are disabled",
    )

    created: typing.Optional[int] = Field(
        default=None,
        description="Date when the album has been created in Unixtime, not set for system albums",
    )

    description: typing.Optional[str] = Field(
        default=None,
        description="Photo album description",
    )

    can_delete: typing.Optional[bool] = Field(
        default=None,
        description="album can delete",
    )

    can_include_to_feed: typing.Optional[bool] = Field(
        default=None,
        description="album can be selected to feed",
    )

    sizes: typing.Optional[typing.List["PhotosPhotoSizes"]] = Field(
        default=None,
    )

    thumb_id: typing.Optional[int] = Field(
        default=None,
        description="Thumb photo ID",
    )

    thumb_is_last: typing.Optional[bool] = Field(
        default=None,
        description="Information whether the album thumb is last photo",
    )

    thumb_src: typing.Optional[str] = Field(
        default=None,
        description="URL of the thumb image",
    )

    updated: typing.Optional[int] = Field(
        default=None,
        description="Date when the album has been updated last time in Unixtime, not set for system albums",
    )

    upload_by_admins_only: typing.Optional[bool] = Field(
        default=None,
        description="Information whether only community administrators can upload photos",
    )


class PhotosPhotoFalseable(BaseModel):
    """
    Schema: photos_photo_falseable
    """


class PhotosPhotoSizes(BaseModel):
    """
    Schema: photos_photo_sizes
    """

    height: int = Field(
        description="Height in px",
    )

    type: "PhotosPhotoSizesType" = Field()

    width: int = Field(
        description="Width in px",
    )

    url: typing.Optional[str] = Field(
        default=None,
        description="URL of the image",
    )

    src: typing.Optional[str] = Field(
        default=None,
        description="URL of the image",
    )


class PhotosPhotoSizesType(enum.Enum):
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


class PhotosPhotoTag(BaseModel):
    """
    Schema: photos_photo_tag
    """

    date: int = Field(
        description="Date when tag has been added in Unixtime",
    )

    id: int = Field(
        description="Tag ID",
    )

    placer_id: int = Field(
        description="ID of the tag creator",
    )

    tagged_name: str = Field(
        description="Tag description",
    )

    user_id: int = Field(
        description="Tagged user ID",
    )

    viewed: bool = Field(
        description="Information whether the tag is reviewed",
    )

    x: float = Field(
        description="Coordinate X of the left upper corner",
    )

    x2: float = Field(
        description="Coordinate X of the right lower corner",
    )

    y: float = Field(
        description="Coordinate Y of the left upper corner",
    )

    y2: float = Field(
        description="Coordinate Y of the right lower corner",
    )

    description: typing.Optional[str] = Field(
        default=None,
        description="Tagged description.",
    )


class PhotosPhotoUpload(BaseModel):
    """
    Schema: photos_photo_upload
    """

    album_id: int = Field(
        description="Album ID",
    )

    upload_url: str = Field(
        description="URL to upload photo",
    )

    user_id: int = Field(
        description="User ID",
    )

    fallback_upload_url: typing.Optional[str] = Field(
        default=None,
        description="Fallback URL if upload_url returned error",
    )

    group_id: typing.Optional[int] = Field(
        default=None,
        description="Group ID",
    )


class PhotosPhotoXtrTagInfo(BaseModel):
    """
    Schema: photos_photo_xtr_tag_info
    """

    album_id: int = Field(
        description="Album ID",
    )

    date: int = Field(
        description="Date when uploaded",
    )

    id: int = Field(
        description="Photo ID",
    )

    owner_id: int = Field(
        description="Photo owner's ID",
    )

    access_key: typing.Optional[str] = Field(
        default=None,
        description="Access key for the photo",
    )

    height: typing.Optional[int] = Field(
        default=None,
        description="Original photo height",
    )

    lat: typing.Optional[float] = Field(
        default=None,
        description="Latitude",
    )

    long: typing.Optional[float] = Field(
        default=None,
        description="Longitude",
    )

    photo_1280: typing.Optional[str] = Field(
        default=None,
        description="URL of image with 1280 px width",
    )

    photo_130: typing.Optional[str] = Field(
        default=None,
        description="URL of image with 130 px width",
    )

    photo_2560: typing.Optional[str] = Field(
        default=None,
        description="URL of image with 2560 px width",
    )

    photo_604: typing.Optional[str] = Field(
        default=None,
        description="URL of image with 604 px width",
    )

    photo_75: typing.Optional[str] = Field(
        default=None,
        description="URL of image with 75 px width",
    )

    photo_807: typing.Optional[str] = Field(
        default=None,
        description="URL of image with 807 px width",
    )

    placer_id: typing.Optional[int] = Field(
        default=None,
        description="ID of the tag creator",
    )

    post_id: typing.Optional[int] = Field(
        default=None,
        description="Post ID",
    )

    sizes: typing.Optional[typing.List["PhotosPhotoSizes"]] = Field(
        default=None,
    )

    tag_created: typing.Optional[int] = Field(
        default=None,
        description="Date when tag has been added in Unixtime",
    )

    tag_id: typing.Optional[int] = Field(
        default=None,
        description="Tag ID",
    )

    text: typing.Optional[str] = Field(
        default=None,
        description="Photo caption",
    )

    user_id: typing.Optional[int] = Field(
        default=None,
        description="ID of the user who have uploaded the photo",
    )

    width: typing.Optional[int] = Field(
        default=None,
        description="Original photo width",
    )

    has_tags: typing.Optional[bool] = Field(
        default=None,
        description="Whether photo has attached tag links",
    )


class PhotosTagsSuggestionItem(BaseModel):
    """
    Schema: photos_tags_suggestion_item
    """

    title: typing.Optional[str] = Field(
        default=None,
    )

    caption: typing.Optional[str] = Field(
        default=None,
    )

    type: typing.Optional[str] = Field(
        default=None,
    )

    buttons: typing.Optional[typing.List["PhotosTagsSuggestionItemButton"]] = Field(
        default=None,
    )

    photo: typing.Optional["PhotosPhoto"] = Field(
        default=None,
    )

    tags: typing.Optional[typing.List["PhotosPhotoTag"]] = Field(
        default=None,
    )

    track_code: typing.Optional[str] = Field(
        default=None,
    )


class PhotosTagsSuggestionItemButtonAction(enum.Enum):
    CONFIRM = "confirm"
    DECLINE = "decline"
    SHOW_TAGS = "show_tags"


class PhotosTagsSuggestionItemButtonStyle(enum.Enum):
    PRIMARY = "primary"
    SECONDARY = "secondary"


class PhotosTagsSuggestionItemButton(BaseModel):
    """
    Schema: photos_tags_suggestion_item_button
    """

    title: typing.Optional[str] = Field(
        default=None,
    )

    action: typing.Optional["PhotosTagsSuggestionItemButtonAction"] = Field(
        default=None,
    )

    style: typing.Optional["PhotosTagsSuggestionItemButtonStyle"] = Field(
        default=None,
    )


class PodcastCover(BaseModel):
    """
    Schema: podcast_cover
    """

    sizes: typing.Optional[typing.List["PhotosPhotoSizes"]] = Field(
        default=None,
    )


class PodcastExternalData(BaseModel):
    """
    Schema: podcast_external_data
    """

    url: typing.Optional[str] = Field(
        default=None,
        description="Url of the podcast page",
    )

    owner_url: typing.Optional[str] = Field(
        default=None,
        description="Url of the podcasts owner community",
    )

    title: typing.Optional[str] = Field(
        default=None,
        description="Podcast title",
    )

    owner_name: typing.Optional[str] = Field(
        default=None,
        description="Name of the podcasts owner community",
    )

    cover: typing.Optional["PodcastCover"] = Field(
        default=None,
        description="Podcast cover",
    )


class PollsAnswer(BaseModel):
    """
    Schema: polls_answer
    """

    id: int = Field(
        description="Answer ID",
    )

    rate: float = Field(
        description="Answer rate in percents",
    )

    text: str = Field(
        description="Answer text",
    )

    votes: int = Field(
        description="Votes number",
    )


class PollsBackgroundType(enum.Enum):
    GRADIENT = "gradient"
    TILE = "tile"


class PollsBackground(BaseModel):
    """
    Schema: polls_background
    """

    angle: typing.Optional[int] = Field(
        default=None,
        description="Gradient angle with 0 on positive X axis",
    )

    color: typing.Optional[str] = Field(
        default=None,
        description="Hex color code without #",
    )

    height: typing.Optional[int] = Field(
        default=None,
        description="Original height of pattern tile",
    )

    id: typing.Optional[int] = Field(
        default=None,
    )

    name: typing.Optional[str] = Field(
        default=None,
    )

    images: typing.Optional[typing.List["BaseImage"]] = Field(
        default=None,
        description="Pattern tiles",
    )

    points: typing.Optional[typing.List["BaseGradientPoint"]] = Field(
        default=None,
        description="Gradient points",
    )

    type: typing.Optional["PollsBackgroundType"] = Field(
        default=None,
    )

    width: typing.Optional[int] = Field(
        default=None,
        description="Original with of pattern tile",
    )


class PollsFieldsVoters(BaseModel):
    """
    Schema: polls_fields_voters
    """

    answer_id: typing.Optional[int] = Field(
        default=None,
        description="Answer ID",
    )

    users: typing.Optional["PollsVotersFieldsUsers"] = Field(
        default=None,
    )

    answer_offset: typing.Optional[str] = Field(
        default=None,
        description="Answer offset",
    )


class PollsFriend(BaseModel):
    """
    Schema: polls_friend
    """

    id: int = Field()


class PollsPoll(BaseModel):
    """
    Schema: polls_poll
    """

    multiple: bool = Field(
        description="Information whether the poll with multiple choices",
    )

    end_date: int = Field()

    closed: bool = Field()

    is_board: bool = Field()

    can_edit: bool = Field()

    can_vote: bool = Field()

    can_report: bool = Field()

    can_share: bool = Field()

    answers: typing.List["PollsAnswer"] = Field()

    created: int = Field(
        description="Date when poll has been created in Unixtime",
    )

    id: int = Field(
        description="Poll ID",
    )

    owner_id: int = Field(
        description="Poll owner's ID",
    )

    question: str = Field(
        description="Poll question",
    )

    votes: int = Field(
        description="Votes number",
    )

    disable_unvote: bool = Field()

    anonymous: typing.Optional["PollsPollAnonymous"] = Field(
        default=None,
    )

    friends: typing.Optional[typing.List["PollsFriend"]] = Field(
        default=None,
    )

    answer_id: typing.Optional[int] = Field(
        default=None,
        description="Current user's answer ID",
    )

    answer_ids: typing.Optional[typing.List[int]] = Field(
        default=None,
        description="Current user's answer IDs",
    )

    embed_hash: typing.Optional[str] = Field(
        default=None,
    )

    photo: typing.Optional["PollsBackground"] = Field(
        default=None,
    )

    author_id: typing.Optional[int] = Field(
        default=None,
        description="Poll author's ID",
    )

    background: typing.Optional["PollsBackground"] = Field(
        default=None,
    )


class PollsPollAnonymous(BaseModel):
    """
    Schema: polls_poll_anonymous
    """


class PollsVoters(BaseModel):
    """
    Schema: polls_voters
    """

    answer_id: typing.Optional[int] = Field(
        default=None,
        description="Answer ID",
    )

    users: typing.Optional["PollsVotersUsers"] = Field(
        default=None,
    )

    answer_offset: typing.Optional[str] = Field(
        default=None,
        description="Answer offset",
    )


class PollsVotersFieldsUsers(BaseModel):
    """
    Schema: polls_voters_fields_users
    """

    count: typing.Optional[int] = Field(
        default=None,
        description="Votes number",
    )

    items: typing.Optional[typing.List["UsersUserFull"]] = Field(
        default=None,
    )


class PollsVotersUsers(BaseModel):
    """
    Schema: polls_voters_users
    """

    count: typing.Optional[int] = Field(
        default=None,
        description="Votes number",
    )

    items: typing.Optional[typing.List[int]] = Field(
        default=None,
    )


class PrettyCardsButtonOneOf(BaseModel):
    """
    Schema: prettyCards_button_one_of
    """


class PrettyCardsPrettyCard(BaseModel):
    """
    Schema: prettyCards_prettyCard
    """

    card_id: str = Field(
        description="Card ID (long int returned as string)",
    )

    link_url: str = Field(
        description="Link URL",
    )

    photo: str = Field(
        description='Photo ID (format "<owner_id>_<media_id>")',
    )

    title: str = Field(
        description="Title",
    )

    button: typing.Optional["PrettyCardsButtonOneOf"] = Field(
        default=None,
        description="Button key",
    )

    button_text: typing.Optional[str] = Field(
        default=None,
        description="Button text in current language",
    )

    images: typing.Optional[typing.List["BaseImage"]] = Field(
        default=None,
    )

    price: typing.Optional[str] = Field(
        default=None,
        description="Price if set (decimal number returned as string)",
    )

    price_old: typing.Optional[str] = Field(
        default=None,
        description="Old price if set (decimal number returned as string)",
    )


class PrettyCardsPrettyCardOrError(BaseModel):
    """
    Schema: prettyCards_prettyCardOrError
    """


class SearchHint(BaseModel):
    """
    Schema: search_hint
    """

    description: str = Field(
        description="Object description",
    )

    type: "SearchHintType" = Field()

    app: typing.Optional["AppsApp"] = Field(
        default=None,
    )

    _global: typing.Optional[bool] = Field(
        default=None,
        description="Information whether the object has been found globally",
        alias="global",
    )

    group: typing.Optional["GroupsGroup"] = Field(
        default=None,
    )

    profile: typing.Optional["UsersUserMin"] = Field(
        default=None,
    )

    section: typing.Optional["SearchHintSection"] = Field(
        default=None,
    )

    link: typing.Optional["BaseLink"] = Field(
        default=None,
    )


class SearchHintSection(enum.Enum):
    GROUPS = "groups"

    EVENTS = "events"

    PUBLICS = "publics"

    CORRESPONDENTS = "correspondents"

    PEOPLE = "people"

    FRIENDS = "friends"

    MUTUAL_FRIENDS = "mutual_friends"

    PROMO = "promo"


class SearchHintType(enum.Enum):
    GROUP = "group"

    PROFILE = "profile"

    VK_APP = "vk_app"

    APP = "app"

    HTML5_GAME = "html5_game"

    LINK = "link"


class SecureGiveEventStickerItem(BaseModel):
    """
    Schema: secure_giveEventSticker_item
    """

    user_id: typing.Optional[int] = Field(
        default=None,
    )

    status: typing.Optional[str] = Field(
        default=None,
    )


class SecureLevel(BaseModel):
    """
    Schema: secure_level
    """

    level: typing.Optional[int] = Field(
        default=None,
        description="Level",
    )

    uid: typing.Optional[int] = Field(
        default=None,
        description="User ID",
    )


class SecureSetCounterItem(BaseModel):
    """
    Schema: secure_setCounter_item
    """

    id: int = Field(
        description="User ID",
    )

    result: bool = Field()


class SecureSmsNotification(BaseModel):
    """
    Schema: secure_sms_notification
    """

    app_id: typing.Optional[str] = Field(
        default=None,
        description="Application ID",
    )

    date: typing.Optional[str] = Field(
        default=None,
        description="Date when message has been sent in Unixtime",
    )

    id: typing.Optional[str] = Field(
        default=None,
        description="Notification ID",
    )

    message: typing.Optional[str] = Field(
        default=None,
        description="Messsage text",
    )

    user_id: typing.Optional[str] = Field(
        default=None,
        description="User ID",
    )


class SecureTokenChecked(BaseModel):
    """
    Schema: secure_token_checked
    """

    date: typing.Optional[int] = Field(
        default=None,
        description="Date when access_token has been generated in Unixtime",
    )

    expire: typing.Optional[int] = Field(
        default=None,
        description="Date when access_token will expire in Unixtime",
    )

    success: typing.Optional[int] = Field(
        default=None,
        description="Returns if successfully processed",
    )

    user_id: typing.Optional[int] = Field(
        default=None,
        description="User ID",
    )


class SecureTransaction(BaseModel):
    """
    Schema: secure_transaction
    """

    date: typing.Optional[int] = Field(
        default=None,
        description="Transaction date in Unixtime",
    )

    id: typing.Optional[int] = Field(
        default=None,
        description="Transaction ID",
    )

    uid_from: typing.Optional[int] = Field(
        default=None,
        description="From ID",
    )

    uid_to: typing.Optional[int] = Field(
        default=None,
        description="To ID",
    )

    votes: typing.Optional[int] = Field(
        default=None,
        description="Votes number",
    )


class StatsActivity(BaseModel):
    """
    Schema: stats_activity
    """

    comments: typing.Optional[int] = Field(
        default=None,
        description="Comments number",
    )

    copies: typing.Optional[int] = Field(
        default=None,
        description="Reposts number",
    )

    hidden: typing.Optional[int] = Field(
        default=None,
        description="Hidden from news count",
    )

    likes: typing.Optional[int] = Field(
        default=None,
        description="Likes number",
    )

    subscribed: typing.Optional[int] = Field(
        default=None,
        description="New subscribers count",
    )

    unsubscribed: typing.Optional[int] = Field(
        default=None,
        description="Unsubscribed count",
    )


class StatsCity(BaseModel):
    """
    Schema: stats_city
    """

    count: typing.Optional[int] = Field(
        default=None,
        description="Visitors number",
    )

    name: typing.Optional[str] = Field(
        default=None,
        description="City name",
    )

    value: typing.Optional[int] = Field(
        default=None,
        description="City ID",
    )


class StatsCountry(BaseModel):
    """
    Schema: stats_country
    """

    code: typing.Optional[str] = Field(
        default=None,
        description="Country code",
    )

    count: typing.Optional[int] = Field(
        default=None,
        description="Visitors number",
    )

    name: typing.Optional[str] = Field(
        default=None,
        description="Country name",
    )

    value: typing.Optional[int] = Field(
        default=None,
        description="Country ID",
    )


class StatsPeriod(BaseModel):
    """
    Schema: stats_period
    """

    activity: typing.Optional["StatsActivity"] = Field(
        default=None,
    )

    period_from: typing.Optional["StatsPeriodFromOneOf"] = Field(
        default=None,
    )

    period_to: typing.Optional["StatsPeriodToOneOf"] = Field(
        default=None,
    )

    reach: typing.Optional["StatsReachOneOf"] = Field(
        default=None,
    )

    visitors: typing.Optional["StatsVisitorsOneOf"] = Field(
        default=None,
    )


class StatsPeriodFromOneOf(BaseModel):
    """
    Schema: stats_period_from_one_of
    """


class StatsPeriodToOneOf(BaseModel):
    """
    Schema: stats_period_to_one_of
    """


class StatsReach(BaseModel):
    """
    Schema: stats_reach
    """

    age: typing.Optional[typing.List["StatsSexAge"]] = Field(
        default=None,
    )

    cities: typing.Optional[typing.List["StatsCity"]] = Field(
        default=None,
    )

    countries: typing.Optional[typing.List["StatsCountry"]] = Field(
        default=None,
    )

    mobile_reach: typing.Optional[int] = Field(
        default=None,
        description="Reach count from mobile devices",
    )

    reach: typing.Optional[int] = Field(
        default=None,
        description="Reach count",
    )

    reach_subscribers: typing.Optional[int] = Field(
        default=None,
        description="Subscribers reach count",
    )

    sex: typing.Optional[typing.List["StatsSexAge"]] = Field(
        default=None,
    )

    sex_age: typing.Optional[typing.List["StatsSexAge"]] = Field(
        default=None,
    )


class StatsReachOneOf(BaseModel):
    """
    Schema: stats_reach_one_of
    """


class StatsSexAge(BaseModel):
    """
    Schema: stats_sex_age
    """

    value: str = Field(
        description="Sex/age value",
    )

    count: typing.Optional[int] = Field(
        default=None,
        description="Visitors number",
    )

    reach: typing.Optional[int] = Field(
        default=None,
    )

    reach_subscribers: typing.Optional[int] = Field(
        default=None,
    )

    count_subscribers: typing.Optional[int] = Field(
        default=None,
    )


class StatsViews(BaseModel):
    """
    Schema: stats_views
    """

    age: typing.Optional[typing.List["StatsSexAge"]] = Field(
        default=None,
    )

    cities: typing.Optional[typing.List["StatsCity"]] = Field(
        default=None,
    )

    countries: typing.Optional[typing.List["StatsCountry"]] = Field(
        default=None,
    )

    mobile_views: typing.Optional[int] = Field(
        default=None,
        description="Number of views from mobile devices",
    )

    sex: typing.Optional[typing.List["StatsSexAge"]] = Field(
        default=None,
    )

    sex_age: typing.Optional[typing.List["StatsSexAge"]] = Field(
        default=None,
    )

    views: typing.Optional[int] = Field(
        default=None,
        description="Views number",
    )

    visitors: typing.Optional[int] = Field(
        default=None,
        description="Visitors number",
    )


class StatsVisitorsOneOf(BaseModel):
    """
    Schema: stats_visitors_one_of
    """


class StatsWallpostStat(BaseModel):
    """
    Schema: stats_wallpost_stat
    """

    post_id: typing.Optional[int] = Field(
        default=None,
    )

    hide: typing.Optional[int] = Field(
        default=None,
        description="Hidings number",
    )

    join_group: typing.Optional[int] = Field(
        default=None,
        description="People have joined the group",
    )

    links: typing.Optional[int] = Field(
        default=None,
        description="Link clickthrough",
    )

    reach_subscribers: typing.Optional[int] = Field(
        default=None,
        description="Subscribers reach",
    )

    reach_subscribers_count: typing.Optional[int] = Field(
        default=None,
    )

    reach_total: typing.Optional[int] = Field(
        default=None,
        description="Total reach",
    )

    reach_total_count: typing.Optional[int] = Field(
        default=None,
    )

    reach_viral: typing.Optional[int] = Field(
        default=None,
    )

    reach_ads: typing.Optional[int] = Field(
        default=None,
    )

    report: typing.Optional[int] = Field(
        default=None,
        description="Reports number",
    )

    to_group: typing.Optional[int] = Field(
        default=None,
        description="Clickthrough to community",
    )

    unsubscribe: typing.Optional[int] = Field(
        default=None,
        description="Unsubscribed members",
    )

    sex_age: typing.Optional[typing.List["StatsSexAge"]] = Field(
        default=None,
    )


class StatusStatus(BaseModel):
    """
    Schema: status_status
    """

    text: str = Field(
        description="Status text",
    )

    audio: typing.Optional["AudioAudio"] = Field(
        default=None,
    )


class StickersImageSet(BaseModel):
    """
    Schema: stickers_image_set
    """

    base_url: str = Field(
        description="Base URL for images in set",
    )

    version: typing.Optional[int] = Field(
        default=None,
        description="Version number to be appended to the image URL",
    )

    images: typing.Optional[typing.List["BaseImage"]] = Field(
        default=None,
    )


class StorageValue(BaseModel):
    """
    Schema: storage_value
    """

    key: str = Field()

    value: str = Field()


class StoreProductType(enum.Enum):
    STICKERS = "stickers"


class StoreProduct(BaseModel):
    """
    Schema: store_product
    """

    id: int = Field(
        description="Id of the product",
    )

    type: "StoreProductType" = Field(
        description="Product type",
    )

    is_new: typing.Optional[bool] = Field(
        default=None,
        description="Information whether sticker product wasn't used after being purchased",
    )

    copyright: typing.Optional[str] = Field(
        default=None,
        description="Product copyright information",
    )

    base_id: typing.Optional[int] = Field(
        default=None,
        description="Id of the base pack (for sticker pack styles)",
    )

    style_ids: typing.Optional[typing.List[int]] = Field(
        default=None,
        description="Array of style ids available for the sticker pack",
    )

    purchased: typing.Optional[bool] = Field(
        default=None,
        description="Information whether the product is purchased (1 - yes, 0 - no)",
    )

    active: typing.Optional[bool] = Field(
        default=None,
        description="Information whether the product is active (1 - yes, 0 - no)",
    )

    promoted: typing.Optional[bool] = Field(
        default=None,
        description="Information whether the product is promoted (1 - yes, 0 - no)",
    )

    purchase_date: typing.Optional[int] = Field(
        default=None,
        description="Date (Unix time) when the product was purchased",
    )

    title: typing.Optional[str] = Field(
        default=None,
        description="Title of the product",
    )

    stickers: typing.Optional["BaseStickersList"] = Field(
        default=None,
    )

    style_sticker_ids: typing.Optional[typing.List[int]] = Field(
        default=None,
        description="Array of style sticker ids (for sticker pack styles)",
    )

    icon: typing.Optional["StoreProductIcon"] = Field(
        default=None,
        description="Array of icon images or icon set object of the product (for stickers product type)",
    )

    previews: typing.Optional[typing.List["BaseImage"]] = Field(
        default=None,
        description="Array of preview images of the product (for stickers product type)",
    )

    has_animation: typing.Optional[bool] = Field(
        default=None,
        description="Information whether the product is an animated sticker pack (for stickers product type)",
    )

    subtitle: typing.Optional[str] = Field(
        default=None,
        description="Subtitle of the product",
    )

    payment_region: typing.Optional[str] = Field(
        default=None,
    )

    is_vmoji: typing.Optional[bool] = Field(
        default=None,
        description="Information whether sticker pack is a vmoji pack",
    )

    title_lang_key: typing.Optional[str] = Field(
        default=None,
    )

    description_lang_key: typing.Optional[str] = Field(
        default=None,
    )

    url: typing.Optional[str] = Field(
        default=None,
    )


class StoreProductIcon(BaseModel):
    """
    Schema: store_product_icon
    """


class StoreStickersKeyword(BaseModel):
    """
    Schema: store_stickers_keyword
    """

    words: typing.List[str] = Field()

    user_stickers: typing.Optional["StoreStickersKeywordStickers"] = Field(
        default=None,
    )

    promoted_stickers: typing.Optional["StoreStickersKeywordStickers"] = Field(
        default=None,
    )

    stickers: typing.Optional[typing.List["StoreStickersKeywordSticker"]] = Field(
        default=None,
    )


class StoreStickersKeywordSticker(BaseModel):
    """
    Schema: store_stickers_keyword_sticker
    """

    pack_id: int = Field(
        description="Pack id",
    )

    sticker_id: int = Field(
        description="Sticker id",
    )


class StoreStickersKeywordStickers(BaseModel):
    """
    Schema: store_stickers_keyword_stickers
    """


class StoriesClickableArea(BaseModel):
    """
    Schema: stories_clickable_area
    """

    x: int = Field()

    y: int = Field()


class StoriesClickableStickerType(enum.Enum):
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


class StoriesClickableStickerStyle(enum.Enum):
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


class StoriesClickableStickerSubtype(enum.Enum):
    MARKET_ITEM = "market_item"
    ALIEXPRESS_PRODUCT = "aliexpress_product"


class StoriesClickableSticker(BaseModel):
    """
    Schema: stories_clickable_sticker
    """

    clickable_area: typing.List["StoriesClickableArea"] = Field()

    id: int = Field(
        description="Clickable sticker ID",
    )

    type: "StoriesClickableStickerType" = Field()

    hashtag: typing.Optional[str] = Field(
        default=None,
    )

    link_object: typing.Optional["BaseLink"] = Field(
        default=None,
    )

    mention: typing.Optional[str] = Field(
        default=None,
    )

    tooltip_text: typing.Optional[str] = Field(
        default=None,
    )

    owner_id: typing.Optional[int] = Field(
        default=None,
    )

    story_id: typing.Optional[int] = Field(
        default=None,
    )

    clip_id: typing.Optional[int] = Field(
        default=None,
    )

    question: typing.Optional[str] = Field(
        default=None,
    )

    question_button: typing.Optional[str] = Field(
        default=None,
    )

    place_id: typing.Optional[int] = Field(
        default=None,
    )

    market_item: typing.Optional["MarketMarketItem"] = Field(
        default=None,
    )

    audio: typing.Optional["AudioAudio"] = Field(
        default=None,
    )

    audio_start_time: typing.Optional[int] = Field(
        default=None,
    )

    style: typing.Optional["StoriesClickableStickerStyle"] = Field(
        default=None,
    )

    subtype: typing.Optional["StoriesClickableStickerSubtype"] = Field(
        default=None,
    )

    post_owner_id: typing.Optional[int] = Field(
        default=None,
    )

    post_id: typing.Optional[int] = Field(
        default=None,
    )

    poll: typing.Optional["PollsPoll"] = Field(
        default=None,
    )

    color: typing.Optional[str] = Field(
        default=None,
        description="Color, hex format",
    )

    sticker_id: typing.Optional[int] = Field(
        default=None,
        description="Sticker ID",
    )

    sticker_pack_id: typing.Optional[int] = Field(
        default=None,
        description="Sticker pack ID",
    )

    app: typing.Optional["AppsAppMin"] = Field(
        default=None,
    )

    app_context: typing.Optional[str] = Field(
        default=None,
        description="Additional context for app sticker",
    )

    has_new_interactions: typing.Optional[bool] = Field(
        default=None,
        description="Whether current user has unread interaction with this app",
    )

    is_broadcast_notify_allowed: typing.Optional[bool] = Field(
        default=None,
        description="Whether current user allowed broadcast notify from this app",
    )

    situational_theme_id: typing.Optional[int] = Field(
        default=None,
    )

    situational_app_url: typing.Optional[str] = Field(
        default=None,
    )


class StoriesClickableStickers(BaseModel):
    """
    Schema: stories_clickable_stickers
    """

    clickable_stickers: typing.List["StoriesClickableSticker"] = Field()

    original_height: int = Field()

    original_width: int = Field()


class StoriesFeedItemType(enum.Enum):
    PROMO_STORIES = "promo_stories"
    STORIES = "stories"
    LIVE_ACTIVE = "live_active"
    LIVE_FINISHED = "live_finished"
    APP_GROUPED_STORIES = "app_grouped_stories"
    DISCOVER = "discover"


class StoriesFeedItem(BaseModel):
    """
    Schema: stories_feed_item
    """

    type: "StoriesFeedItemType" = Field(
        description="Type of Feed Item",
    )

    id: typing.Optional[str] = Field(
        default=None,
    )

    owner_id: typing.Optional[int] = Field(
        default=None,
    )

    stories: typing.Optional[typing.List["StoriesStory"]] = Field(
        default=None,
        description="Author stories",
    )

    grouped: typing.Optional[typing.List["StoriesFeedItem"]] = Field(
        default=None,
        description="Grouped stories of various authors (for types community_grouped_stories/app_grouped_stories type)",
    )

    app: typing.Optional["AppsAppMin"] = Field(
        default=None,
        description="App, which stories has been grouped (for type app_grouped_stories)",
    )

    promo_data: typing.Optional["StoriesPromoBlock"] = Field(
        default=None,
        description="Additional data for promo stories (for type promo_stories)",
    )

    track_code: typing.Optional[str] = Field(
        default=None,
    )

    has_unseen: typing.Optional[bool] = Field(
        default=None,
    )

    name: typing.Optional[str] = Field(
        default=None,
    )


class StoriesPromoBlock(BaseModel):
    """
    Schema: stories_promo_block
    """

    name: str = Field(
        description="Promo story title",
    )

    photo_50: str = Field(
        description="RL of square photo of the story with 50 pixels in width",
    )

    photo_100: str = Field(
        description="RL of square photo of the story with 100 pixels in width",
    )

    not_animated: bool = Field(
        description="Hide animation for promo story",
    )

    is_advice: bool = Field(
        description="Promo story from advice",
    )


class StoriesReplies(BaseModel):
    """
    Schema: stories_replies
    """

    count: int = Field(
        description="Replies number.",
    )

    new: typing.Optional[int] = Field(
        default=None,
        description="New replies number.",
    )


class StoriesStatCategory(BaseModel):
    """
    Schema: stories_stat_category
    """

    header: str = Field()

    lines: typing.List["StoriesStatLine"] = Field()


class StoriesStatLine(BaseModel):
    """
    Schema: stories_stat_line
    """

    name: str = Field()

    counter: typing.Optional[int] = Field(
        default=None,
    )

    is_unavailable: typing.Optional[bool] = Field(
        default=None,
    )


class StoriesStory(BaseModel):
    """
    Schema: stories_story
    """

    id: int = Field(
        description="Story ID.",
    )

    owner_id: int = Field(
        description="Story owner's ID.",
    )

    access_key: typing.Optional[str] = Field(
        default=None,
        description="Access key for private object.",
    )

    can_comment: typing.Optional[bool] = Field(
        default=None,
        description="Information whether current user can comment the story (0 - no, 1 - yes).",
    )

    can_reply: typing.Optional[bool] = Field(
        default=None,
        description="Information whether current user can reply to the story (0 - no, 1 - yes).",
    )

    can_see: typing.Optional[bool] = Field(
        default=None,
        description="Information whether current user can see the story (0 - no, 1 - yes).",
    )

    can_like: typing.Optional[bool] = Field(
        default=None,
        description="Information whether current user can like the story.",
    )

    can_share: typing.Optional[bool] = Field(
        default=None,
        description="Information whether current user can share the story (0 - no, 1 - yes).",
    )

    can_hide: typing.Optional[bool] = Field(
        default=None,
        description="Information whether current user can hide the story (0 - no, 1 - yes).",
    )

    date: typing.Optional[int] = Field(
        default=None,
        description="Date when story has been added in Unixtime.",
    )

    expires_at: typing.Optional[int] = Field(
        default=None,
        description="Story expiration time. Unixtime.",
    )

    is_deleted: typing.Optional[bool] = Field(
        default=None,
        description="Information whether the story is deleted (false - no, true - yes).",
    )

    is_expired: typing.Optional[bool] = Field(
        default=None,
        description="Information whether the story is expired (false - no, true - yes).",
    )

    link: typing.Optional["StoriesStoryLink"] = Field(
        default=None,
    )

    parent_story: typing.Optional["StoriesStory"] = Field(
        default=None,
    )

    parent_story_access_key: typing.Optional[str] = Field(
        default=None,
        description="Access key for private object.",
    )

    parent_story_id: typing.Optional[int] = Field(
        default=None,
        description="Parent story ID.",
    )

    parent_story_owner_id: typing.Optional[int] = Field(
        default=None,
        description="Parent story owner's ID.",
    )

    photo: typing.Optional["PhotosPhoto"] = Field(
        default=None,
    )

    replies: typing.Optional["StoriesReplies"] = Field(
        default=None,
        description="Replies counters to current story.",
    )

    seen: typing.Optional[bool] = Field(
        default=None,
        description="Information whether current user has seen the story or not (0 - no, 1 - yes).",
    )

    type: typing.Optional["StoriesStoryType"] = Field(
        default=None,
    )

    clickable_stickers: typing.Optional["StoriesClickableStickers"] = Field(
        default=None,
    )

    video: typing.Optional["VideoVideoFull"] = Field(
        default=None,
    )

    views: typing.Optional[int] = Field(
        default=None,
        description="Views number.",
    )

    can_ask: typing.Optional[bool] = Field(
        default=None,
        description="Information whether story has question sticker and current user can send question to the author",
    )

    can_ask_anonymous: typing.Optional[bool] = Field(
        default=None,
        description="Information whether story has question sticker and current user can send anonymous question to the author",
    )

    narratives_count: typing.Optional[int] = Field(
        default=None,
    )

    first_narrative_title: typing.Optional[str] = Field(
        default=None,
    )

    can_use_in_narrative: typing.Optional[bool] = Field(
        default=None,
    )


class StoriesStoryLink(BaseModel):
    """
    Schema: stories_story_link
    """

    text: str = Field(
        description="Link text",
    )

    url: str = Field(
        description="Link URL",
    )

    link_url_target: typing.Optional[str] = Field(
        default=None,
        description="How to open url",
    )


class StoriesStoryStats(BaseModel):
    """
    Schema: stories_story_stats
    """

    answer: "StoriesStoryStatsStat" = Field()

    bans: "StoriesStoryStatsStat" = Field()

    open_link: "StoriesStoryStatsStat" = Field()

    replies: "StoriesStoryStatsStat" = Field()

    shares: "StoriesStoryStatsStat" = Field()

    subscribers: "StoriesStoryStatsStat" = Field()

    views: "StoriesStoryStatsStat" = Field()

    likes: "StoriesStoryStatsStat" = Field()


class StoriesStoryStatsStat(BaseModel):
    """
    Schema: stories_story_stats_stat
    """

    state: "StoriesStoryStatsState" = Field()

    count: typing.Optional[int] = Field(
        default=None,
        description="Stat value",
    )


class StoriesStoryStatsState(enum.Enum):
    ON = "on"

    OFF = "off"

    HIDDEN = "hidden"


class StoriesStoryType(enum.Enum):
    PHOTO = "photo"

    VIDEO = "video"

    LIVE_ACTIVE = "live_active"

    LIVE_FINISHED = "live_finished"


class StoriesUploadLinkText(enum.Enum):
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


class StoriesUploadResult(BaseModel):
    """
    Schema: stories_upload_result
    """

    upload_result: typing.Optional[str] = Field(
        default=None,
    )


class StoriesViewersItem(BaseModel):
    """
    Schema: stories_viewers_item
    """

    is_liked: bool = Field(
        description="user has like for this object",
    )

    user_id: int = Field(
        description="user id",
    )

    user: typing.Optional["UsersUserFull"] = Field(
        default=None,
    )


class StreamingStatsEventType(enum.Enum):
    POST = "post"
    COMMENT = "comment"
    SHARE = "share"


class StreamingStats(BaseModel):
    """
    Schema: streaming_stats
    """

    event_type: "StreamingStatsEventType" = Field(
        description="Events type",
    )

    stats: typing.List["StreamingStatsPoint"] = Field(
        description="Statistics",
    )


class StreamingStatsPoint(BaseModel):
    """
    Schema: streaming_stats_point
    """

    timestamp: int = Field()

    value: int = Field()


class FriendsFriendStatus(BaseModel):
    """
    Schema: friends_friend_status
    """

    friend_status: "FriendsFriendStatusStatus" = Field()

    user_id: int = Field(
        description="User ID",
    )

    sign: typing.Optional[str] = Field(
        default=None,
        description="MD5 hash for the result validation",
    )


class FriendsFriendStatusStatus(enum.IntEnum):
    NOT_A_FRIEND = 0

    OUTCOMING_REQUEST = 1

    INCOMING_REQUEST = 2

    IS_FRIEND = 3


class FriendsFriendsList(BaseModel):
    """
    Schema: friends_friends_list
    """

    id: int = Field(
        description="List ID",
    )

    name: str = Field(
        description="List title",
    )


class FriendsMutualFriend(BaseModel):
    """
    Schema: friends_mutual_friend
    """

    common_count: typing.Optional[int] = Field(
        default=None,
        description="Total mutual friends number",
    )

    common_friends: typing.Optional[typing.List[int]] = Field(
        default=None,
    )

    id: typing.Optional[int] = Field(
        default=None,
        description="User ID",
    )


class FriendsRequestsMutual(BaseModel):
    """
    Schema: friends_requests_mutual
    """

    count: typing.Optional[int] = Field(
        default=None,
        description="Total mutual friends number",
    )

    users: typing.Optional[typing.List[int]] = Field(
        default=None,
    )


class UtilsDomainResolved(BaseModel):
    """
    Schema: utils_domain_resolved
    """

    object_id: typing.Optional[int] = Field(
        default=None,
        description="Object ID",
    )

    group_id: typing.Optional[int] = Field(
        default=None,
        description="Group ID",
    )

    type: typing.Optional["UtilsDomainResolvedType"] = Field(
        default=None,
    )


class UtilsDomainResolvedType(enum.Enum):
    USER = "user"

    GROUP = "group"

    APPLICATION = "application"

    PAGE = "page"

    VK_APP = "vk_app"

    COMMUNITY_APPLICATION = "community_application"


class UtilsLastShortenedLink(BaseModel):
    """
    Schema: utils_last_shortened_link
    """

    access_key: typing.Optional[str] = Field(
        default=None,
        description="Access key for private stats",
    )

    key: typing.Optional[str] = Field(
        default=None,
        description="Link key (characters after vk.cc/)",
    )

    short_url: typing.Optional[str] = Field(
        default=None,
        description="Short link URL",
    )

    timestamp: typing.Optional[int] = Field(
        default=None,
        description="Creation time in Unixtime",
    )

    url: typing.Optional[str] = Field(
        default=None,
        description="Full URL",
    )

    views: typing.Optional[int] = Field(
        default=None,
        description="Total views number",
    )


class UtilsLinkChecked(BaseModel):
    """
    Schema: utils_link_checked
    """

    link: typing.Optional[str] = Field(
        default=None,
        description="Link URL",
    )

    status: typing.Optional["UtilsLinkCheckedStatus"] = Field(
        default=None,
    )


class UtilsLinkCheckedStatus(enum.Enum):
    NOT_BANNED = "not_banned"

    BANNED = "banned"

    PROCESSING = "processing"


class UtilsLinkStats(BaseModel):
    """
    Schema: utils_link_stats
    """

    key: typing.Optional[str] = Field(
        default=None,
        description="Link key (characters after vk.cc/)",
    )

    stats: typing.Optional[typing.List["UtilsStats"]] = Field(
        default=None,
    )


class UtilsLinkStatsExtended(BaseModel):
    """
    Schema: utils_link_stats_extended
    """

    key: typing.Optional[str] = Field(
        default=None,
        description="Link key (characters after vk.cc/)",
    )

    stats: typing.Optional[typing.List["UtilsStatsExtended"]] = Field(
        default=None,
    )


class UtilsShortLink(BaseModel):
    """
    Schema: utils_short_link
    """

    access_key: typing.Optional[str] = Field(
        default=None,
        description="Access key for private stats",
    )

    key: typing.Optional[str] = Field(
        default=None,
        description="Link key (characters after vk.cc/)",
    )

    short_url: typing.Optional[str] = Field(
        default=None,
        description="Short link URL",
    )

    url: typing.Optional[str] = Field(
        default=None,
        description="Full URL",
    )


class UtilsStats(BaseModel):
    """
    Schema: utils_stats
    """

    timestamp: typing.Optional[int] = Field(
        default=None,
        description="Start time",
    )

    views: typing.Optional[int] = Field(
        default=None,
        description="Total views number",
    )


class UtilsStatsCity(BaseModel):
    """
    Schema: utils_stats_city
    """

    city_id: typing.Optional[int] = Field(
        default=None,
        description="City ID",
    )

    views: typing.Optional[int] = Field(
        default=None,
        description="Views number",
    )


class UtilsStatsCountry(BaseModel):
    """
    Schema: utils_stats_country
    """

    country_id: typing.Optional[int] = Field(
        default=None,
        description="Country ID",
    )

    views: typing.Optional[int] = Field(
        default=None,
        description="Views number",
    )


class UtilsStatsExtended(BaseModel):
    """
    Schema: utils_stats_extended
    """

    cities: typing.Optional[typing.List["UtilsStatsCity"]] = Field(
        default=None,
    )

    countries: typing.Optional[typing.List["UtilsStatsCountry"]] = Field(
        default=None,
    )

    sex_age: typing.Optional[typing.List["UtilsStatsSexAge"]] = Field(
        default=None,
    )

    timestamp: typing.Optional[int] = Field(
        default=None,
        description="Start time",
    )

    views: typing.Optional[int] = Field(
        default=None,
        description="Total views number",
    )


class UtilsStatsSexAge(BaseModel):
    """
    Schema: utils_stats_sex_age
    """

    age_range: typing.Optional[str] = Field(
        default=None,
        description="Age denotation",
    )

    female: typing.Optional[int] = Field(
        default=None,
        description=" Views by female users",
    )

    male: typing.Optional[int] = Field(
        default=None,
        description=" Views by male users",
    )


class VideoEpisode(BaseModel):
    """
    Schema: video_episode
    """

    time: typing.Optional[int] = Field(
        default=None,
        description="Seconds from start of the video",
    )

    text: typing.Optional[str] = Field(
        default=None,
        description="Description of episode",
    )


class VideoLiveCategory(BaseModel):
    """
    Schema: video_live_category
    """

    id: int = Field()

    label: str = Field()

    sublist: typing.Optional[typing.List["VideoLiveCategory"]] = Field(
        default=None,
    )


class VideoLiveInfo(BaseModel):
    """
    Schema: video_live_info
    """

    enabled: bool = Field()

    is_notifications_blocked: typing.Optional[bool] = Field(
        default=None,
    )


class VideoLiveSettings(BaseModel):
    """
    Schema: video_live_settings
    """

    can_rewind: typing.Optional[bool] = Field(
        default=None,
        description="If user car rewind live or not",
    )

    is_endless: typing.Optional[bool] = Field(
        default=None,
        description="If live is endless or not",
    )

    max_duration: typing.Optional[int] = Field(
        default=None,
        description="Max possible time for rewind",
    )

    is_clips_live: typing.Optional[bool] = Field(
        default=None,
        description="If live in clips apps",
    )


class VideoSaveResult(BaseModel):
    """
    Schema: video_save_result
    """

    access_key: typing.Optional[str] = Field(
        default=None,
        description="Video access key",
    )

    description: typing.Optional[str] = Field(
        default=None,
        description="Video description",
    )

    owner_id: typing.Optional[int] = Field(
        default=None,
        description="Video owner ID",
    )

    title: typing.Optional[str] = Field(
        default=None,
        description="Video title",
    )

    upload_url: typing.Optional[str] = Field(
        default=None,
        description="URL for the video uploading",
    )

    video_id: typing.Optional[int] = Field(
        default=None,
        description="Video ID",
    )


class VideoStreamInputParams(BaseModel):
    """
    Schema: video_stream_input_params
    """

    url: typing.Optional[str] = Field(
        default=None,
    )

    key: typing.Optional[str] = Field(
        default=None,
    )

    okmp_url: typing.Optional[str] = Field(
        default=None,
    )

    webrtc_url: typing.Optional[str] = Field(
        default=None,
    )


class VideoVideoResponseType(enum.Enum):
    MIN = "min"
    FULL = "full"


class VideoVideoType(enum.Enum):
    VIDEO = "video"
    MUSIC_VIDEO = "music_video"
    MOVIE = "movie"
    LIVE = "live"
    SHORT_VIDEO = "short_video"


class VideoVideo(BaseModel):
    """
    Schema: video_video
    """

    response_type: typing.Optional["VideoVideoResponseType"] = Field(
        default=None,
    )

    access_key: typing.Optional[str] = Field(
        default=None,
        description="Video access key",
    )

    adding_date: typing.Optional[int] = Field(
        default=None,
        description="Date when the video has been added in Unixtime",
    )

    can_comment: typing.Optional[bool] = Field(
        default=None,
        description="Information whether current user can comment the video",
    )

    can_edit: typing.Optional[bool] = Field(
        default=None,
        description="Information whether current user can edit the video",
    )

    can_delete: typing.Optional[bool] = Field(
        default=None,
        description="Information whether current user can delete the video",
    )

    can_like: typing.Optional[bool] = Field(
        default=None,
        description="Information whether current user can like the video",
    )

    can_repost: typing.Optional[int] = Field(
        default=None,
        description="Information whether current user can repost the video",
    )

    can_subscribe: typing.Optional[bool] = Field(
        default=None,
        description="Information whether current user can subscribe to author of the video",
    )

    can_add_to_faves: typing.Optional[bool] = Field(
        default=None,
        description="Information whether current user can add the video to favourites",
    )

    can_add: typing.Optional[bool] = Field(
        default=None,
        description="Information whether current user can add the video",
    )

    can_attach_link: typing.Optional[bool] = Field(
        default=None,
        description="Information whether current user can attach action button to the video",
    )

    can_edit_privacy: typing.Optional[bool] = Field(
        default=None,
        description="Information whether current user can edit the video privacy",
    )

    is_private: typing.Optional[bool] = Field(
        default=None,
        description="1 if video is private",
    )

    comments: typing.Optional[int] = Field(
        default=None,
        description="Number of comments",
    )

    date: typing.Optional[int] = Field(
        default=None,
        description="Date when video has been uploaded in Unixtime",
    )

    description: typing.Optional[str] = Field(
        default=None,
        description="Video description",
    )

    duration: typing.Optional[int] = Field(
        default=None,
        description="Video duration in seconds",
    )

    image: typing.Optional[typing.List["VideoVideoImage"]] = Field(
        default=None,
    )

    first_frame: typing.Optional[typing.List["VideoVideoImage"]] = Field(
        default=None,
    )

    width: typing.Optional[int] = Field(
        default=None,
        description="Video width",
    )

    height: typing.Optional[int] = Field(
        default=None,
        description="Video height",
    )

    id: typing.Optional[int] = Field(
        default=None,
        description="Video ID",
    )

    owner_id: typing.Optional[int] = Field(
        default=None,
        description="Video owner ID",
    )

    user_id: typing.Optional[int] = Field(
        default=None,
        description="Id of the user who uploaded the video if it was uploaded to a group by member",
    )

    title: typing.Optional[str] = Field(
        default=None,
        description="Video title",
    )

    is_favorite: typing.Optional[bool] = Field(
        default=None,
        description="Whether video is added to bookmarks",
    )

    player: typing.Optional[str] = Field(
        default=None,
        description="Video embed URL",
    )

    processing: typing.Optional["BasePropertyExists"] = Field(
        default=None,
        description="Returns if the video is processing",
    )

    converting: typing.Optional[bool] = Field(
        default=None,
        description="1 if  video is being converted",
    )

    added: typing.Optional[bool] = Field(
        default=None,
        description="1 if video is added to user's albums",
    )

    is_subscribed: typing.Optional[bool] = Field(
        default=None,
        description="1 if user is subscribed to author of the video",
    )

    track_code: typing.Optional[str] = Field(
        default=None,
    )

    repeat: typing.Optional["BasePropertyExists"] = Field(
        default=None,
        description="Information whether the video is repeated",
    )

    type: typing.Optional["VideoVideoType"] = Field(
        default=None,
    )

    views: typing.Optional[int] = Field(
        default=None,
        description="Number of views",
    )

    local_views: typing.Optional[int] = Field(
        default=None,
        description="If video is external, number of views on vk",
    )

    content_restricted: typing.Optional[int] = Field(
        default=None,
        description="Restriction code",
    )

    content_restricted_message: typing.Optional[str] = Field(
        default=None,
        description="Restriction text",
    )

    balance: typing.Optional[int] = Field(
        default=None,
        description="Live donations balance",
    )

    live: typing.Optional["BasePropertyExists"] = Field(
        default=None,
        description="1 if the video is a live stream",
    )

    upcoming: typing.Optional["BasePropertyExists"] = Field(
        default=None,
        description="1 if the video is an upcoming stream",
    )

    live_start_time: typing.Optional[int] = Field(
        default=None,
        description="Date in Unixtime when the live stream is scheduled to start by the author",
    )

    live_notify: typing.Optional[bool] = Field(
        default=None,
        description="Whether current user is subscribed to the upcoming live stream notification (if not subscribed to the author)",
    )

    spectators: typing.Optional[int] = Field(
        default=None,
        description="Number of spectators of the stream",
    )

    platform: typing.Optional[str] = Field(
        default=None,
        description="External platform",
    )

    likes: typing.Optional["BaseLikes"] = Field(
        default=None,
    )

    reposts: typing.Optional["BaseRepostsInfo"] = Field(
        default=None,
    )


class VideoVideoAlbumResponseType(enum.Enum):
    MIN = "min"
    FULL = "full"


class VideoVideoAlbum(BaseModel):
    """
    Schema: video_video_album
    """

    id: int = Field(
        description="Album ID",
    )

    owner_id: int = Field(
        description="Album owner's ID",
    )

    title: str = Field(
        description="Album title",
    )

    track_code: typing.Optional[str] = Field(
        default=None,
        description="Album trackcode",
    )

    response_type: typing.Optional["VideoVideoAlbumResponseType"] = Field(
        default=None,
    )


class VideoVideoFiles(BaseModel):
    """
    Schema: video_video_files
    """

    external: typing.Optional[str] = Field(
        default=None,
        description="URL of the external player",
    )

    mp4_144: typing.Optional[str] = Field(
        default=None,
        description="URL of the mpeg4 file with 144p quality",
    )

    mp4_240: typing.Optional[str] = Field(
        default=None,
        description="URL of the mpeg4 file with 240p quality",
    )

    mp4_360: typing.Optional[str] = Field(
        default=None,
        description="URL of the mpeg4 file with 360p quality",
    )

    mp4_480: typing.Optional[str] = Field(
        default=None,
        description="URL of the mpeg4 file with 480p quality",
    )

    mp4_720: typing.Optional[str] = Field(
        default=None,
        description="URL of the mpeg4 file with 720p quality",
    )

    mp4_1080: typing.Optional[str] = Field(
        default=None,
        description="URL of the mpeg4 file with 1080p quality",
    )

    mp4_1440: typing.Optional[str] = Field(
        default=None,
        description="URL of the mpeg4 file with 2K quality",
    )

    mp4_2160: typing.Optional[str] = Field(
        default=None,
        description="URL of the mpeg4 file with 4K quality",
    )

    flv_320: typing.Optional[str] = Field(
        default=None,
        description="URL of the flv file with 320p quality",
    )


class WallAppPost(BaseModel):
    """
    Schema: wall_app_post
    """

    id: typing.Optional[int] = Field(
        default=None,
        description="Application ID",
    )

    name: typing.Optional[str] = Field(
        default=None,
        description="Application name",
    )

    photo_130: typing.Optional[str] = Field(
        default=None,
        description="URL of the preview image with 130 px in width",
    )

    photo_604: typing.Optional[str] = Field(
        default=None,
        description="URL of the preview image with 604 px in width",
    )


class WallAttachedNote(BaseModel):
    """
    Schema: wall_attached_note
    """

    comments: int = Field(
        description="Comments number",
    )

    date: int = Field(
        description="Date when the note has been created in Unixtime",
    )

    id: int = Field(
        description="Note ID",
    )

    owner_id: int = Field(
        description="Note owner's ID",
    )

    read_comments: int = Field(
        description="Read comments number",
    )

    title: str = Field(
        description="Note title",
    )

    view_url: str = Field(
        description="URL of the page with note preview",
    )

    text: typing.Optional[str] = Field(
        default=None,
        description="Note text",
    )

    privacy_view: typing.Optional[typing.List[str]] = Field(
        default=None,
    )

    privacy_comment: typing.Optional[typing.List[str]] = Field(
        default=None,
    )

    can_comment: typing.Optional[int] = Field(
        default=None,
    )

    text_wiki: typing.Optional[str] = Field(
        default=None,
        description="Note wiki text",
    )


class WallCarouselBase(BaseModel):
    """
    Schema: wall_carousel_base
    """

    carousel_offset: typing.Optional[int] = Field(
        default=None,
        description="Index of current carousel element",
    )


class WallCommentAttachment(BaseModel):
    """
    Schema: wall_comment_attachment
    """

    type: "WallCommentAttachmentType" = Field()

    audio: typing.Optional["AudioAudio"] = Field(
        default=None,
    )

    doc: typing.Optional["DocsDoc"] = Field(
        default=None,
    )

    link: typing.Optional["BaseLink"] = Field(
        default=None,
    )

    market: typing.Optional["MarketMarketItem"] = Field(
        default=None,
    )

    market_market_album: typing.Optional["MarketMarketAlbum"] = Field(
        default=None,
    )

    note: typing.Optional["WallAttachedNote"] = Field(
        default=None,
    )

    page: typing.Optional["PagesWikipageFull"] = Field(
        default=None,
    )

    photo: typing.Optional["PhotosPhoto"] = Field(
        default=None,
    )

    sticker: typing.Optional["BaseSticker"] = Field(
        default=None,
    )

    video: typing.Optional["VideoVideo"] = Field(
        default=None,
    )

    graffiti: typing.Optional["WallGraffiti"] = Field(
        default=None,
    )


class WallCommentAttachmentType(enum.Enum):
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


class WallGeoType(enum.Enum):
    PLACE = "place"
    POINT = "point"


class WallGeo(BaseModel):
    """
    Schema: wall_geo
    """

    coordinates: typing.Optional[str] = Field(
        default=None,
        description="Coordinates as string. <latitude> <longtitude>",
    )

    showmap: typing.Optional[int] = Field(
        default=None,
        description="Information whether a map is showed",
    )

    type: typing.Optional["WallGeoType"] = Field(
        default=None,
        description="Place type",
    )


class WallGetFilter(enum.Enum):
    OWNER = "owner"

    OTHERS = "others"

    ALL = "all"

    POSTPONED = "postponed"

    SUGGESTS = "suggests"

    ARCHIVED = "archived"

    DONUT = "donut"


class WallGraffiti(BaseModel):
    """
    Schema: wall_graffiti
    """

    id: typing.Optional[int] = Field(
        default=None,
        description="Graffiti ID",
    )

    owner_id: typing.Optional[int] = Field(
        default=None,
        description="Graffiti owner's ID",
    )

    photo_200: typing.Optional[str] = Field(
        default=None,
        description="URL of the preview image with 200 px in width",
    )

    photo_586: typing.Optional[str] = Field(
        default=None,
        description="URL of the preview image with 586 px in width",
    )

    height: typing.Optional[int] = Field(
        default=None,
        description="Graffiti height",
    )

    url: typing.Optional[str] = Field(
        default=None,
        description="Graffiti URL",
    )

    width: typing.Optional[int] = Field(
        default=None,
        description="Graffiti width",
    )

    access_key: typing.Optional[str] = Field(
        default=None,
        description="Access key for graffiti",
    )


class WallPostCopyright(BaseModel):
    """
    Schema: wall_post_copyright
    """

    link: str = Field()

    name: str = Field()

    type: str = Field()

    id: typing.Optional[int] = Field(
        default=None,
    )


class WallPostSource(BaseModel):
    """
    Schema: wall_post_source
    """

    data: typing.Optional[str] = Field(
        default=None,
        description="Additional data",
    )

    platform: typing.Optional[str] = Field(
        default=None,
        description="Platform name",
    )

    type: typing.Optional["WallPostSourceType"] = Field(
        default=None,
    )

    url: typing.Optional[str] = Field(
        default=None,
        description="URL to an external site used to publish the post",
    )

    link: typing.Optional["BaseLink"] = Field(
        default=None,
    )


class WallPostSourceType(enum.Enum):
    VK = "vk"

    WIDGET = "widget"

    API = "api"

    RSS = "rss"

    SMS = "sms"

    MVK = "mvk"


class WallPostType(enum.Enum):
    POST = "post"

    COPY = "copy"

    REPLY = "reply"

    POSTPONE = "postpone"

    SUGGEST = "suggest"

    POST_ADS = "post_ads"

    PHOTO = "photo"

    VIDEO = "video"


class WallPostedPhoto(BaseModel):
    """
    Schema: wall_posted_photo
    """

    id: typing.Optional[int] = Field(
        default=None,
        description="Photo ID",
    )

    owner_id: typing.Optional[int] = Field(
        default=None,
        description="Photo owner's ID",
    )

    photo_130: typing.Optional[str] = Field(
        default=None,
        description="URL of the preview image with 130 px in width",
    )

    photo_604: typing.Optional[str] = Field(
        default=None,
        description="URL of the preview image with 604 px in width",
    )


class WallViews(BaseModel):
    """
    Schema: wall_views
    """

    count: typing.Optional[int] = Field(
        default=None,
        description="Count",
    )


class WallWallComment(BaseModel):
    """
    Schema: wall_wall_comment
    """

    id: int = Field(
        description="Comment ID",
    )

    from_id: int = Field(
        description="Author ID",
    )

    date: int = Field(
        description="Date when the comment has been added in Unixtime",
    )

    text: str = Field(
        description="Comment text",
    )

    can_edit: typing.Optional[bool] = Field(
        default=None,
    )

    post_id: typing.Optional[int] = Field(
        default=None,
    )

    owner_id: typing.Optional[int] = Field(
        default=None,
    )

    parents_stack: typing.Optional[typing.List[int]] = Field(
        default=None,
    )

    photo_id: typing.Optional[int] = Field(
        default=None,
    )

    video_id: typing.Optional[int] = Field(
        default=None,
    )

    attachments: typing.Optional[typing.List["WallWallpostAttachment"]] = Field(
        default=None,
    )

    donut: typing.Optional["WallWallCommentDonut"] = Field(
        default=None,
    )

    likes: typing.Optional["BaseLikesInfo"] = Field(
        default=None,
    )

    real_offset: typing.Optional[int] = Field(
        default=None,
        description="Real position of the comment",
    )

    reply_to_user: typing.Optional[int] = Field(
        default=None,
        description="Replied user ID",
    )

    reply_to_comment: typing.Optional[int] = Field(
        default=None,
        description="Replied comment ID",
    )

    thread: typing.Optional["CommentThread"] = Field(
        default=None,
    )

    deleted: typing.Optional[bool] = Field(
        default=None,
    )

    pid: typing.Optional[int] = Field(
        default=None,
        description="Photo ID",
    )


class WallWallCommentDonut(BaseModel):
    """
    Schema: wall_wall_comment_donut
    """

    is_don: typing.Optional[bool] = Field(
        default=None,
        description="Means commentator is donator",
    )

    placeholder: typing.Optional["WallWallCommentDonutPlaceholder"] = Field(
        default=None,
    )


class WallWallCommentDonutPlaceholder(BaseModel):
    """
    Schema: wall_wall_comment_donut_placeholder
    """

    text: str = Field()


class WallWallItem(BaseModel):
    """
    Schema: wall_wall_item
    """


class WallWallpost(BaseModel):
    """
    Schema: wall_wallpost
    """

    access_key: typing.Optional[str] = Field(
        default=None,
        description="Access key to private object",
    )

    is_deleted: typing.Optional[bool] = Field(
        default=None,
    )

    deleted_reason: typing.Optional[str] = Field(
        default=None,
    )

    deleted_details: typing.Optional[str] = Field(
        default=None,
    )

    attachments: typing.Optional[typing.List["WallWallpostAttachment"]] = Field(
        default=None,
    )

    copyright: typing.Optional["WallPostCopyright"] = Field(
        default=None,
        description="Information about the source of the post",
    )

    date: typing.Optional[int] = Field(
        default=None,
        description="Date of publishing in Unixtime",
    )

    edited: typing.Optional[int] = Field(
        default=None,
        description="Date of editing in Unixtime",
    )

    from_id: typing.Optional[int] = Field(
        default=None,
        description="Post author ID",
    )

    geo: typing.Optional["WallGeo"] = Field(
        default=None,
    )

    id: typing.Optional[int] = Field(
        default=None,
        description="Post ID",
    )

    is_archived: typing.Optional[bool] = Field(
        default=None,
        description="Is post archived, only for post owners",
    )

    is_favorite: typing.Optional[bool] = Field(
        default=None,
        description="Information whether the post in favorites list",
    )

    likes: typing.Optional["BaseLikesInfo"] = Field(
        default=None,
        description="Count of likes",
    )

    owner_id: typing.Optional[int] = Field(
        default=None,
        description="Wall owner's ID",
    )

    post_id: typing.Optional[int] = Field(
        default=None,
        description="If post type 'reply', contains original post ID",
    )

    parents_stack: typing.Optional[typing.List[int]] = Field(
        default=None,
        description="If post type 'reply', contains original parent IDs stack",
    )

    post_source: typing.Optional["WallPostSource"] = Field(
        default=None,
    )

    post_type: typing.Optional["WallPostType"] = Field(
        default=None,
    )

    reposts: typing.Optional["BaseRepostsInfo"] = Field(
        default=None,
    )

    signer_id: typing.Optional[int] = Field(
        default=None,
        description="Post signer ID",
    )

    text: typing.Optional[str] = Field(
        default=None,
        description="Post text",
    )

    views: typing.Optional["WallViews"] = Field(
        default=None,
        description="Count of views",
    )


class WallWallpostAttachment(BaseModel):
    """
    Schema: wall_wallpost_attachment
    """

    type: "WallWallpostAttachmentType" = Field()

    access_key: typing.Optional[str] = Field(
        default=None,
        description="Access key for the audio",
    )

    album: typing.Optional["PhotosPhotoAlbum"] = Field(
        default=None,
    )

    app: typing.Optional["WallAppPost"] = Field(
        default=None,
    )

    audio: typing.Optional["AudioAudio"] = Field(
        default=None,
    )

    doc: typing.Optional["DocsDoc"] = Field(
        default=None,
    )

    event: typing.Optional["EventsEventAttach"] = Field(
        default=None,
    )

    group: typing.Optional["GroupsGroupAttach"] = Field(
        default=None,
    )

    graffiti: typing.Optional["WallGraffiti"] = Field(
        default=None,
    )

    link: typing.Optional["BaseLink"] = Field(
        default=None,
    )

    market: typing.Optional["MarketMarketItem"] = Field(
        default=None,
    )

    market_album: typing.Optional["MarketMarketAlbum"] = Field(
        default=None,
    )

    note: typing.Optional["NotesNote"] = Field(
        default=None,
    )

    page: typing.Optional["PagesWikipageFull"] = Field(
        default=None,
    )

    photo: typing.Optional["PhotosPhoto"] = Field(
        default=None,
    )

    poll: typing.Optional["PollsPoll"] = Field(
        default=None,
    )

    posted_photo: typing.Optional["WallPostedPhoto"] = Field(
        default=None,
    )

    video: typing.Optional["VideoVideoFull"] = Field(
        default=None,
    )

    video_playlist: typing.Optional["VideoVideoAlbumFull"] = Field(
        default=None,
    )


class WallWallpostAttachmentType(enum.Enum):
    PHOTO = "photo"

    PHOTOS_LIST = "photos_list"

    POSTED_PHOTO = "posted_photo"

    AUDIO = "audio"

    AUDIO_PLAYLIST = "audio_playlist"

    VIDEO = "video"

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
    Schema: wall_wallpost_comments_donut
    """

    placeholder: typing.Optional["WallWallpostCommentsDonutPlaceholder"] = Field(
        default=None,
    )


class WallWallpostCommentsDonutPlaceholder(BaseModel):
    """
    Schema: wall_wallpost_comments_donut_placeholder
    """

    text: str = Field()


class WallWallpostDonutEditMode(enum.Enum):
    ALL = "all"
    DURATION = "duration"


class WallWallpostDonut(BaseModel):
    """
    Schema: wall_wallpost_donut
    """

    is_donut: bool = Field(
        description="Post only for dons",
    )

    paid_duration: typing.Optional[int] = Field(
        default=None,
        description="Value of this field need to pass in wall.post/edit in donut_paid_duration",
    )

    placeholder: typing.Optional["WallWallpostDonutPlaceholder"] = Field(
        default=None,
        description="If placeholder was respond, text and all attachments will be hidden",
    )

    can_publish_free_copy: typing.Optional[bool] = Field(
        default=None,
        description="Says whether group admin can post free copy of this donut post",
    )

    edit_mode: typing.Optional["WallWallpostDonutEditMode"] = Field(
        default=None,
        description="Says what user can edit in post about donut properties",
    )


class WallWallpostDonutPlaceholder(BaseModel):
    """
    Schema: wall_wallpost_donut_placeholder
    """

    text: str = Field()


class NewsfeedCommentsFilters(enum.Enum):
    POST = "post"

    PHOTO = "photo"

    VIDEO = "video"

    TOPIC = "topic"

    NOTE = "note"


class NewsfeedCommentsItem(BaseModel):
    """
    Schema: newsfeed_comments_item
    """


class NewsfeedCommentsItemBase(BaseModel):
    """
    Schema: newsfeed_comments_item_base
    """

    type: "NewsfeedNewsfeedItemType" = Field()

    source_id: typing.Optional[int] = Field(
        default=None,
    )

    date: typing.Optional[int] = Field(
        default=None,
    )

    post_id: typing.Optional[int] = Field(
        default=None,
    )


class NewsfeedIgnoreItemType(enum.Enum):
    WALL = "wall"

    TAG = "tag"

    PROFILEPHOTO = "profilephoto"

    VIDEO = "video"

    PHOTO = "photo"

    AUDIO = "audio"


class NewsfeedItemAudioAudio(BaseModel):
    """
    Schema: newsfeed_item_audio_audio
    """

    count: typing.Optional[int] = Field(
        default=None,
        description="Audios number",
    )

    items: typing.Optional[typing.List["AudioAudio"]] = Field(
        default=None,
    )


class NewsfeedItemBase(BaseModel):
    """
    Schema: newsfeed_item_base
    """

    type: "NewsfeedNewsfeedItemType" = Field()

    source_id: int = Field(
        description="Item source ID",
    )

    date: int = Field(
        description="Date when item has been added in Unixtime",
    )

    short_text_rate: typing.Optional[float] = Field(
        default=None,
        description="Preview length control parameter",
    )

    feedback: typing.Optional["NewsfeedItemWallpostFeedback"] = Field(
        default=None,
    )


class NewsfeedItemDigestButtonStyle(enum.Enum):
    PRIMARY = "primary"


class NewsfeedItemDigestButton(BaseModel):
    """
    Schema: newsfeed_item_digest_button
    """

    title: str = Field()

    style: typing.Optional["NewsfeedItemDigestButtonStyle"] = Field(
        default=None,
    )


class NewsfeedItemDigestFooterStyle(enum.Enum):
    TEXT = "text"
    BUTTON = "button"


class NewsfeedItemDigestFooter(BaseModel):
    """
    Schema: newsfeed_item_digest_footer
    """

    style: "NewsfeedItemDigestFooterStyle" = Field()

    text: str = Field(
        description="text for invite to enable smart feed",
    )

    button: typing.Optional["NewsfeedItemDigestButton"] = Field(
        default=None,
    )


class NewsfeedItemDigestHeaderStyle(enum.Enum):
    SINGLELINE = "singleline"
    MULTILINE = "multiline"


class NewsfeedItemDigestHeader(BaseModel):
    """
    Schema: newsfeed_item_digest_header
    """

    title: str = Field(
        description="Title of the header",
    )

    style: "NewsfeedItemDigestHeaderStyle" = Field()

    subtitle: typing.Optional[str] = Field(
        default=None,
        description="Subtitle of the header, when title have two strings",
    )

    badge_text: typing.Optional[str] = Field(
        default=None,
        description="Optional field for red badge in Trends feed blocks",
    )

    button: typing.Optional["NewsfeedItemDigestButton"] = Field(
        default=None,
    )


class NewsfeedItemDigestItem(BaseModel):
    """
    Schema: newsfeed_item_digest_item
    """


class NewsfeedItemFriendFriends(BaseModel):
    """
    Schema: newsfeed_item_friend_friends
    """

    count: typing.Optional[int] = Field(
        default=None,
        description="Number of friends has been added",
    )

    items: typing.Optional[typing.List["BaseUserId"]] = Field(
        default=None,
    )


class NewsfeedItemHolidayRecommendationsBlockHeader(BaseModel):
    """
    Schema: newsfeed_item_holiday_recommendations_block_header
    """

    title: typing.Optional[str] = Field(
        default=None,
        description="Title of the header",
    )

    subtitle: typing.Optional[str] = Field(
        default=None,
        description="Subtitle of the header",
    )

    image: typing.Optional[typing.List["BaseImage"]] = Field(
        default=None,
    )

    action: typing.Optional["BaseLinkButtonAction"] = Field(
        default=None,
    )


class NewsfeedItemPhotoPhotos(BaseModel):
    """
    Schema: newsfeed_item_photo_photos
    """

    count: typing.Optional[int] = Field(
        default=None,
        description="Photos number",
    )

    items: typing.Optional[typing.List["PhotosPhoto"]] = Field(
        default=None,
    )


class NewsfeedItemPhotoTagPhotoTags(BaseModel):
    """
    Schema: newsfeed_item_photo_tag_photo_tags
    """

    count: typing.Optional[int] = Field(
        default=None,
        description="Tags number",
    )

    items: typing.Optional[typing.List["PhotosPhoto"]] = Field(
        default=None,
    )


class NewsfeedItemPromoButtonAction(BaseModel):
    """
    Schema: newsfeed_item_promo_button_action
    """

    url: typing.Optional[str] = Field(
        default=None,
    )

    type: typing.Optional[str] = Field(
        default=None,
    )

    target: typing.Optional[str] = Field(
        default=None,
    )


class NewsfeedItemPromoButtonImage(BaseModel):
    """
    Schema: newsfeed_item_promo_button_image
    """

    width: typing.Optional[int] = Field(
        default=None,
    )

    height: typing.Optional[int] = Field(
        default=None,
    )

    url: typing.Optional[str] = Field(
        default=None,
    )


class NewsfeedItemVideoVideo(BaseModel):
    """
    Schema: newsfeed_item_video_video
    """

    count: typing.Optional[int] = Field(
        default=None,
        description="Tags number",
    )

    items: typing.Optional[typing.List["VideoVideoFull"]] = Field(
        default=None,
    )


class NewsfeedItemWallpostFeedback(BaseModel):
    """
    Schema: newsfeed_item_wallpost_feedback
    """

    type: "NewsfeedItemWallpostFeedbackType" = Field()

    question: str = Field()

    answers: typing.Optional[typing.List["NewsfeedItemWallpostFeedbackAnswer"]] = Field(
        default=None,
    )

    stars_count: typing.Optional[int] = Field(
        default=None,
    )

    descriptions: typing.Optional[typing.List[str]] = Field(
        default=None,
    )

    gratitude: typing.Optional[str] = Field(
        default=None,
    )

    track_code: typing.Optional[str] = Field(
        default=None,
    )


class NewsfeedItemWallpostFeedbackAnswer(BaseModel):
    """
    Schema: newsfeed_item_wallpost_feedback_answer
    """

    title: str = Field()

    id: str = Field()


class NewsfeedItemWallpostFeedbackType(enum.Enum):
    BUTTONS = "buttons"

    STARS = "stars"


class NewsfeedList(BaseModel):
    """
    Schema: newsfeed_list
    """

    id: int = Field(
        description="List ID",
    )

    title: str = Field(
        description="List title",
    )


class NewsfeedNewsfeedItem(BaseModel):
    """
    Schema: newsfeed_newsfeed_item
    """


class NewsfeedNewsfeedItemType(enum.Enum):
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


class WidgetsCommentMedia(BaseModel):
    """
    Schema: widgets_comment_media
    """

    item_id: typing.Optional[int] = Field(
        default=None,
        description="Media item ID",
    )

    owner_id: typing.Optional[int] = Field(
        default=None,
        description="Media owner's ID",
    )

    thumb_src: typing.Optional[str] = Field(
        default=None,
        description="URL of the preview image (type=photo only)",
    )

    type: typing.Optional["WidgetsCommentMediaType"] = Field(
        default=None,
    )


class WidgetsCommentMediaType(enum.Enum):
    AUDIO = "audio"

    PHOTO = "photo"

    VIDEO = "video"


class WidgetsCommentReplies(BaseModel):
    """
    Schema: widgets_comment_replies
    """

    can_post: typing.Optional[bool] = Field(
        default=None,
        description="Information whether current user can comment the post",
    )

    count: typing.Optional[int] = Field(
        default=None,
        description="Comments number",
    )

    replies: typing.Optional[typing.List["WidgetsCommentRepliesItem"]] = Field(
        default=None,
    )

    groups_can_post: typing.Optional[bool] = Field(
        default=None,
        description="Information whether groups can comment the post",
    )

    can_view: typing.Optional[bool] = Field(
        default=None,
        description="Information whether current user can view the comments",
    )


class WidgetsCommentRepliesItem(BaseModel):
    """
    Schema: widgets_comment_replies_item
    """

    cid: typing.Optional[int] = Field(
        default=None,
        description="Comment ID",
    )

    date: typing.Optional[int] = Field(
        default=None,
        description="Date when the comment has been added in Unixtime",
    )

    likes: typing.Optional["WidgetsWidgetLikes"] = Field(
        default=None,
    )

    text: typing.Optional[str] = Field(
        default=None,
        description="Comment text",
    )

    uid: typing.Optional[int] = Field(
        default=None,
        description="User ID",
    )

    user: typing.Optional["UsersUserFull"] = Field(
        default=None,
    )


class WidgetsWidgetComment(BaseModel):
    """
    Schema: widgets_widget_comment
    """

    date: int = Field(
        description="Date when the comment has been added in Unixtime",
    )

    from_id: int = Field(
        description="Comment author ID",
    )

    id: int = Field(
        description="Comment ID",
    )

    post_type: str = Field(
        description="Post type",
    )

    text: str = Field(
        description="Comment text",
    )

    to_id: int = Field(
        description="Wall owner",
    )

    attachments: typing.Optional[typing.List["WallCommentAttachment"]] = Field(
        default=None,
    )

    owner_id: typing.Optional[int] = Field(
        default=None,
        description="Wall owner's ID",
    )

    can_delete: typing.Optional[bool] = Field(
        default=None,
        description="Information whether current user can delete the comment",
    )

    comments: typing.Optional["WidgetsCommentReplies"] = Field(
        default=None,
    )

    likes: typing.Optional["BaseLikesInfo"] = Field(
        default=None,
    )

    media: typing.Optional["WidgetsCommentMedia"] = Field(
        default=None,
    )

    post_source: typing.Optional["WallPostSource"] = Field(
        default=None,
    )

    reposts: typing.Optional["BaseRepostsInfo"] = Field(
        default=None,
    )

    user: typing.Optional["UsersUserFull"] = Field(
        default=None,
    )

    is_favorite: typing.Optional[bool] = Field(
        default=None,
        description="Information whether the post in favorites list",
    )

    short_text_rate: typing.Optional[float] = Field(
        default=None,
        description="Preview length control parameter",
    )


class WidgetsWidgetLikes(BaseModel):
    """
    Schema: widgets_widget_likes
    """

    count: typing.Optional[int] = Field(
        default=None,
        description="Likes number",
    )


class WidgetsWidgetPage(BaseModel):
    """
    Schema: widgets_widget_page
    """

    comments: typing.Optional["BaseObjectCount"] = Field(
        default=None,
    )

    date: typing.Optional[int] = Field(
        default=None,
        description="Date when widgets on the page has been initialized firstly in Unixtime",
    )

    description: typing.Optional[str] = Field(
        default=None,
        description="Page description",
    )

    id: typing.Optional[int] = Field(
        default=None,
        description="Page ID",
    )

    likes: typing.Optional["BaseObjectCount"] = Field(
        default=None,
    )

    page_id: typing.Optional[str] = Field(
        default=None,
        description="page_id parameter value",
    )

    photo: typing.Optional[str] = Field(
        default=None,
        description="URL of the preview image",
    )

    title: typing.Optional[str] = Field(
        default=None,
        description="Page title",
    )

    url: typing.Optional[str] = Field(
        default=None,
        description="Page absolute URL",
    )


class UsersUser(UsersUserMin):
    """
    Schema: users_user
    """

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


class UsersUserFull(UsersUser):
    """
    Schema: users_user_full
    """

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

    career: typing.Optional[typing.List["UsersCareer"]] = Field(
        default=None,
    )

    military: typing.Optional[typing.List["UsersMilitary"]] = Field(
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

    universities: typing.Optional[typing.List["UsersUniversity"]] = Field(
        default=None,
    )

    schools: typing.Optional[typing.List["UsersSchool"]] = Field(
        default=None,
    )

    relatives: typing.Optional[typing.List["UsersRelative"]] = Field(
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


class UsersUserXtrType(UsersUserFull):
    """
    Schema: users_user_xtr_type
    """

    type: typing.Optional["UsersUserType"] = Field(
        default=None,
    )


class AccountUserSettings(UsersUserMin, UsersUserSettingsXtr):
    """
    Schema: account_user_settings
    """

    photo_200: typing.Optional[str] = Field(
        default=None,
        description="URL of square photo of the user with 200 pixels in width",
    )

    is_service_account: typing.Optional[bool] = Field(
        default=None,
        description="flag about service account",
    )


class AdsStatsAge(AdsDemographicStatsPeriodItemBase):
    """
    Schema: ads_stats_age
    """

    value: typing.Optional[str] = Field(
        default=None,
        description="Age interval",
    )


class AdsStatsCities(AdsDemographicStatsPeriodItemBase):
    """
    Schema: ads_stats_cities
    """

    name: typing.Optional[str] = Field(
        default=None,
        description="City name",
    )

    value: typing.Optional[typing.Union["int", "str"]] = Field(
        default=None,
        description="City ID",
    )


class AdsStatsSex(AdsDemographicStatsPeriodItemBase):
    """
    Schema: ads_stats_sex
    """

    value: typing.Optional["AdsStatsSexValue"] = Field(
        default=None,
    )


class AdsStatsSexAge(AdsDemographicStatsPeriodItemBase):
    """
    Schema: ads_stats_sex_age
    """

    value: typing.Optional[str] = Field(
        default=None,
        description="Sex and age interval",
    )


class AdsTargSettings(AdsCriteria):
    """
    Schema: ads_targ_settings
    """

    id: typing.Optional[str] = Field(
        default=None,
        description="Ad ID",
    )

    campaign_id: typing.Optional[str] = Field(
        default=None,
        description="Campaign ID",
    )


class AppsApp(AppsAppMin):
    """
    Schema: apps_app
    """

    author_url: typing.Optional[str] = Field(
        default=None,
        description="Application author's URL",
    )

    banner_1120: typing.Optional[str] = Field(
        default=None,
        description="URL of the app banner with 1120 px in width",
    )

    banner_560: typing.Optional[str] = Field(
        default=None,
        description="URL of the app banner with 560 px in width",
    )

    icon_16: typing.Optional[str] = Field(
        default=None,
        description="URL of the app icon with 16 px in width",
    )

    is_new: typing.Optional[bool] = Field(
        default=None,
        description="Is new flag",
    )

    push_enabled: typing.Optional[bool] = Field(
        default=None,
        description="Is push enabled",
    )

    friends: typing.Optional[typing.List[int]] = Field(
        default=None,
    )

    catalog_position: typing.Optional[int] = Field(
        default=None,
        description="Catalog position",
    )

    description: typing.Optional[str] = Field(
        default=None,
        description="Application description",
    )

    genre: typing.Optional[str] = Field(
        default=None,
        description="Genre name",
    )

    genre_id: typing.Optional[int] = Field(
        default=None,
        description="Genre ID",
    )

    international: typing.Optional[bool] = Field(
        default=None,
        description="Information whether the application is multilanguage",
    )

    is_in_catalog: typing.Optional[int] = Field(
        default=None,
        description="Information whether application is in mobile catalog",
    )

    leaderboard_type: typing.Optional["AppsAppLeaderboardType"] = Field(
        default=None,
    )

    members_count: typing.Optional[int] = Field(
        default=None,
        description="Members number",
    )

    platform_id: typing.Optional[str] = Field(
        default=None,
        description="Application ID in store",
    )

    published_date: typing.Optional[int] = Field(
        default=None,
        description="Date when the application has been published in Unixtime",
    )

    screen_name: typing.Optional[str] = Field(
        default=None,
        description="Screen name",
    )

    section: typing.Optional[str] = Field(
        default=None,
        description="Application section name",
    )


class BaseLink(BaseLinkNoProduct):
    """
    Schema: base_link
    """

    text: typing.Optional[str] = Field(
        default=None,
    )

    product: typing.Optional["BaseLinkProduct"] = Field(
        default=None,
    )


class CallbackConfirmation(CallbackBase):
    """
    Schema: callback_confirmation
    """

    type: typing.Optional[str] = Field(
        default=None,
    )


class CallbackMessageAllow(CallbackBase):
    """
    Schema: callback_message_allow
    """

    object: "CallbackMessageAllowObject" = Field()

    type: typing.Optional[str] = Field(
        default=None,
    )


class CallbackMessageEdit(CallbackBase):
    """
    Schema: callback_message_edit
    """

    object: "MessagesMessage" = Field()

    type: typing.Optional[str] = Field(
        default=None,
    )


class CallbackMessageNew(CallbackBase):
    """
    Schema: callback_message_new
    """

    object: dict = Field()

    type: typing.Optional[str] = Field(
        default=None,
    )


class CallbackMessageReply(CallbackBase):
    """
    Schema: callback_message_reply
    """

    object: "MessagesMessage" = Field()

    type: typing.Optional[str] = Field(
        default=None,
    )


class DatabaseCity(BaseObject):
    """
    Schema: database_city
    """

    area: typing.Optional[str] = Field(
        default=None,
        description="Area title",
    )

    region: typing.Optional[str] = Field(
        default=None,
        description="Region title",
    )

    country: typing.Optional[str] = Field(
        default=None,
        description="Country title",
    )

    important: typing.Optional[bool] = Field(
        default=None,
        description="Information whether the city is included in important cities list",
    )


class GroupsUserXtrRole(UsersUserFull):
    """
    Schema: groups_user_xtr_role
    """

    permissions: typing.Optional[typing.List["GroupsMemberRolePermission"]] = Field(
        default=None,
    )

    role: typing.Optional["GroupsRoleOptions"] = Field(
        default=None,
    )


class GroupsGroupFull(GroupsGroup, GroupsMarketProperties, GroupsClassifiedsProperties):
    """
    Schema: groups_group_full
    """

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

    links: typing.Optional[typing.List["GroupsLinksItem"]] = Field(
        default=None,
    )

    contacts: typing.Optional[typing.List["GroupsContactsItem"]] = Field(
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


class MarketMarketItemBasicWithGroup(MarketMarketItemBasic):
    """
    Schema: market_market_item_basic_with_group
    """

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


class MarketMarketItemFull(MarketMarketItem):
    """
    Schema: market_market_item_full
    """

    albums_ids: typing.Optional[typing.List[int]] = Field(
        default=None,
    )

    photos: typing.Optional[typing.List["PhotosPhoto"]] = Field(
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


class MessagesUserXtrInvitedBy(UsersUserXtrType):
    """
    Schema: messages_user_xtr_invited_by
    """

    invited_by: typing.Optional[int] = Field(
        default=None,
        description="ID of the inviter",
    )

    name: typing.Optional[str] = Field(
        default=None,
        description="Name of group",
    )

    type: typing.Optional["MessagesUserTypeForXtrInvitedBy"] = Field(
        default=None,
    )


class MessagesGetConversationByIdExtended(MessagesGetConversationById):
    """
    Schema: messages_getConversationById_extended
    """

    profiles: typing.Optional[typing.List["UsersUserFull"]] = Field(
        default=None,
    )

    groups: typing.Optional[typing.List["GroupsGroupFull"]] = Field(
        default=None,
    )


class FriendsRequestsXtrMutual(UsersUserFull):
    """
    Schema: friends_requests_xtr_mutual
    """

    user_id: int = Field(
        description="User ID",
    )

    id: typing.Optional[int] = Field(
        default=None,
        description="User ID",
    )

    _from: typing.Optional[str] = Field(
        default=None,
        description="ID of the user by whom friend has been suggested",
        alias="from",
    )

    mutual: typing.Optional["FriendsRequestsMutual"] = Field(
        default=None,
    )

    track_code: typing.Optional[str] = Field(
        default=None,
    )

    message: typing.Optional[str] = Field(
        default=None,
        description="Message sent with a request",
    )

    timestamp: typing.Optional[int] = Field(
        default=None,
        description="Request timestamp",
    )

    descriptions: typing.Optional[typing.List[str]] = Field(
        default=None,
    )


class FriendsUserXtrPhone(UsersUserFull):
    """
    Schema: friends_user_xtr_phone
    """

    phone: typing.Optional[str] = Field(
        default=None,
        description="User phone",
    )


class FriendsFriendExtendedStatus(FriendsFriendStatus):
    """
    Schema: friends_friend_extended_status
    """

    is_request_unread: typing.Optional[bool] = Field(
        default=None,
        description="Is friend request from other user unread",
    )


class FriendsRequestsXtrMessage(FriendsRequestsXtrMutual):
    """
    Schema: friends_requests_xtr_message
    """

    message: typing.Optional[str] = Field(
        default=None,
        description="Message sent with a request",
    )


class VideoVideoImage(BaseImage):
    """
    Schema: video_video_image
    """

    with_padding: typing.Optional["BasePropertyExists"] = Field(
        default=None,
    )


class VideoVideoAlbumFull(VideoVideoAlbum):
    """
    Schema: video_video_album_full
    """

    count: int = Field(
        description="Total number of videos in album",
    )

    updated_time: int = Field(
        description="Date when the album has been updated last time in Unixtime",
    )

    image: typing.Optional[typing.List["VideoVideoImage"]] = Field(
        default=None,
        description="Album cover image in different sizes",
    )

    image_blur: typing.Optional["BasePropertyExists"] = Field(
        default=None,
        description="Need blur album thumb or not",
    )

    is_system: typing.Optional["BasePropertyExists"] = Field(
        default=None,
        description="Information whether album is system",
    )

    can_edit: typing.Optional[bool] = Field(
        default=None,
        description="Is user can edit playlist",
    )

    can_delete: typing.Optional[bool] = Field(
        default=None,
        description="Is user can delete playlist",
    )

    can_upload: typing.Optional[bool] = Field(
        default=None,
        description="Is user can upload video to playlist",
    )


class VideoVideoFull(VideoVideo):
    """
    Schema: video_video_full
    """

    files: typing.Optional["VideoVideoFiles"] = Field(
        default=None,
    )

    trailer: typing.Optional["VideoVideoFiles"] = Field(
        default=None,
    )

    episodes: typing.Optional[typing.List["VideoEpisode"]] = Field(
        default=None,
        description="List of video episodes with timecodes",
    )

    live_settings: typing.Optional["VideoLiveSettings"] = Field(
        default=None,
        description="Settings for live stream",
    )


class WallWallpostFull(WallCarouselBase, WallWallpost):
    """
    Schema: wall_wallpost_full
    """

    copy_history: typing.Optional[typing.List["WallWallpostFull"]] = Field(
        default=None,
    )

    can_edit: typing.Optional[bool] = Field(
        default=None,
        description="Information whether current user can edit the post",
    )

    created_by: typing.Optional[int] = Field(
        default=None,
        description="Post creator ID (if post still can be edited)",
    )

    can_delete: typing.Optional[bool] = Field(
        default=None,
        description="Information whether current user can delete the post",
    )

    can_pin: typing.Optional[bool] = Field(
        default=None,
        description="Information whether current user can pin the post",
    )

    donut: typing.Optional["WallWallpostDonut"] = Field(
        default=None,
    )

    is_pinned: typing.Optional[bool] = Field(
        default=None,
        description="Information whether the post is pinned",
    )

    comments: typing.Optional["BaseCommentsInfo"] = Field(
        default=None,
    )

    marked_as_ads: typing.Optional[bool] = Field(
        default=None,
        description="Information whether the post is marked as ads",
    )

    topic_id: typing.Optional[int] = Field(
        default=None,
        description="Topic ID. Allowed values can be obtained from newsfeed.getPostTopics method",
    )

    short_text_rate: typing.Optional[float] = Field(
        default=None,
        description="Preview length control parameter",
    )

    hash: typing.Optional[str] = Field(
        default=None,
        description="Hash for sharing",
    )

    type: typing.Optional["WallPostType"] = Field(
        default=None,
    )

    feedback: typing.Optional["NewsfeedItemWallpostFeedback"] = Field(
        default=None,
    )

    to_id: typing.Optional[int] = Field(
        default=None,
    )


class NewsfeedCommentsBase(BaseCommentsInfo):
    """
    Schema: newsfeed_comments_base
    """

    list: typing.Optional[typing.List["WallWallComment"]] = Field(
        default=None,
    )


class NewsfeedCommentsItemTypeMarket(MarketMarketItem, NewsfeedCommentsItemBase):
    """
    Schema: newsfeed_comments_item_type_market
    """

    comments: typing.Optional["NewsfeedCommentsBase"] = Field(
        default=None,
    )

    likes: typing.Optional["BaseLikes"] = Field(
        default=None,
    )


class NewsfeedCommentsItemTypeNotes(NewsfeedCommentsItemBase):
    """
    Schema: newsfeed_comments_item_type_notes
    """

    text: typing.Optional[str] = Field(
        default=None,
    )

    comments: typing.Optional["NewsfeedCommentsBase"] = Field(
        default=None,
    )

    likes: typing.Optional["BaseLikes"] = Field(
        default=None,
    )


class NewsfeedCommentsItemTypePhoto(PhotosPhoto, NewsfeedCommentsItemBase):
    """
    Schema: newsfeed_comments_item_type_photo
    """

    comments: typing.Optional["NewsfeedCommentsBase"] = Field(
        default=None,
    )

    likes: typing.Optional["BaseLikes"] = Field(
        default=None,
    )


class NewsfeedCommentsItemTypePost(WallWallpostFull, NewsfeedCommentsItemBase):
    """
    Schema: newsfeed_comments_item_type_post
    """

    from_id: typing.Optional[int] = Field(
        default=None,
    )

    comments: typing.Optional["NewsfeedCommentsBase"] = Field(
        default=None,
    )


class NewsfeedCommentsItemTypeTopic(NewsfeedCommentsItemBase):
    """
    Schema: newsfeed_comments_item_type_topic
    """

    text: typing.Optional[str] = Field(
        default=None,
    )

    comments: typing.Optional["NewsfeedCommentsBase"] = Field(
        default=None,
    )

    likes: typing.Optional["BaseLikes"] = Field(
        default=None,
    )


class NewsfeedCommentsItemTypeVideo(VideoVideo, NewsfeedCommentsItemBase):
    """
    Schema: newsfeed_comments_item_type_video
    """

    text: typing.Optional[str] = Field(
        default=None,
    )

    comments: typing.Optional["NewsfeedCommentsBase"] = Field(
        default=None,
    )

    likes: typing.Optional["BaseLikes"] = Field(
        default=None,
    )

    type: typing.Optional[str] = Field(
        default=None,
    )


class NewsfeedItemAudio(NewsfeedItemBase):
    """
    Schema: newsfeed_item_audio
    """

    audio: typing.Optional["NewsfeedItemAudioAudio"] = Field(
        default=None,
    )

    post_id: typing.Optional[int] = Field(
        default=None,
        description="Post ID",
    )


class NewsfeedItemDigest(NewsfeedItemBase):
    """
    Schema: newsfeed_item_digest
    """

    feed_id: typing.Optional[str] = Field(
        default=None,
        description="id of feed in digest",
    )

    items: typing.Optional[typing.List["NewsfeedItemDigestItem"]] = Field(
        default=None,
    )

    main_post_ids: typing.Optional[typing.List[str]] = Field(
        default=None,
    )

    template: typing.Optional[str] = Field(
        default=None,
        description="type of digest",
    )

    header: typing.Optional["NewsfeedItemDigestHeader"] = Field(
        default=None,
    )

    footer: typing.Optional["NewsfeedItemDigestFooter"] = Field(
        default=None,
    )


class NewsfeedItemDigestFullItem(NewsfeedItemBase):
    """
    Schema: newsfeed_item_digest_full_item
    """

    post: "NewsfeedItemWallpost" = Field()

    text: typing.Optional[str] = Field(
        default=None,
    )

    source_name: typing.Optional[str] = Field(
        default=None,
    )

    attachment_index: typing.Optional[int] = Field(
        default=None,
    )

    attachment: typing.Optional["WallWallpostAttachment"] = Field(
        default=None,
    )

    style: typing.Optional[str] = Field(
        default=None,
    )

    badge_text: typing.Optional[str] = Field(
        default=None,
        description="Optional red badge for posts in digest block",
    )


class NewsfeedItemFriend(NewsfeedItemBase):
    """
    Schema: newsfeed_item_friend
    """

    friends: typing.Optional["NewsfeedItemFriendFriends"] = Field(
        default=None,
    )


class NewsfeedItemPhoto(WallCarouselBase, NewsfeedItemBase):
    """
    Schema: newsfeed_item_photo
    """

    photos: typing.Optional["NewsfeedItemPhotoPhotos"] = Field(
        default=None,
    )

    post_id: typing.Optional[int] = Field(
        default=None,
        description="Post ID",
    )


class NewsfeedItemPhotoTag(WallCarouselBase, NewsfeedItemBase):
    """
    Schema: newsfeed_item_photo_tag
    """

    photo_tags: typing.Optional["NewsfeedItemPhotoTagPhotoTags"] = Field(
        default=None,
    )

    post_id: typing.Optional[int] = Field(
        default=None,
        description="Post ID",
    )


class NewsfeedItemPromoButton(NewsfeedItemBase):
    """
    Schema: newsfeed_item_promo_button
    """

    text: typing.Optional[str] = Field(
        default=None,
    )

    title: typing.Optional[str] = Field(
        default=None,
    )

    action: typing.Optional["NewsfeedItemPromoButtonAction"] = Field(
        default=None,
    )

    images: typing.Optional[typing.List["NewsfeedItemPromoButtonImage"]] = Field(
        default=None,
    )


class NewsfeedItemTopic(NewsfeedItemBase):
    """
    Schema: newsfeed_item_topic
    """

    post_id: int = Field(
        description="Topic post ID",
    )

    text: str = Field(
        description="Post text",
    )

    comments: typing.Optional["BaseCommentsInfo"] = Field(
        default=None,
    )

    likes: typing.Optional["BaseLikesInfo"] = Field(
        default=None,
    )


class NewsfeedItemVideo(WallCarouselBase, NewsfeedItemBase):
    """
    Schema: newsfeed_item_video
    """

    video: typing.Optional["NewsfeedItemVideoVideo"] = Field(
        default=None,
    )

    post_id: typing.Optional[int] = Field(
        default=None,
        description="Post ID",
    )


class NewsfeedItemWallpost(BaseModel):
    """
    Schema: newsfeed_item_wallpost
    """


class NewsfeedListFull(NewsfeedList):
    """
    Schema: newsfeed_list_full
    """

    no_reposts: typing.Optional[bool] = Field(
        default=None,
        description="Information whether reposts hiding is enabled",
    )

    source_ids: typing.Optional[typing.List[int]] = Field(
        default=None,
    )


__all__ = (
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
    "AddressesFields",
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
    "AdsRulesHelpUrl",
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
    "AdswebGetAdCategoriesResponseCategoriesCategory",
    "AdswebGetAdUnitsResponseAdUnitsAdUnit",
    "AdswebGetFraudHistoryResponseEntriesEntry",
    "AdswebGetSitesResponseSitesSite",
    "AdswebGetStatisticsResponseItemsItem",
    "AppWidgetsPhoto",
    "AppWidgetsPhotos",
    "AppsAppFields",
    "AppsAppLeaderboardType",
    "AppsAppMin",
    "AppsAppType",
    "AppsCatalogList",
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
    "BaseStickerAnimation",
    "BaseStickerAnimationType",
    "BaseStickerNew",
    "BaseStickerOld",
    "BaseStickersList",
    "BaseUploadServer",
    "BaseUserGroupFields",
    "BaseUserId",
    "BoardDefaultOrder",
    "BoardTopic",
    "BoardTopicComment",
    "CallbackBase",
    "CallbackBoardPostDelete",
    "CallbackDonutMoneyWithdraw",
    "CallbackDonutMoneyWithdrawError",
    "CallbackDonutSubscriptionCancelled",
    "CallbackDonutSubscriptionCreate",
    "CallbackDonutSubscriptionExpired",
    "CallbackDonutSubscriptionPriceChanged",
    "CallbackDonutSubscriptionProlonged",
    "CallbackGroupChangePhoto",
    "CallbackGroupChangeSettings",
    "CallbackGroupJoin",
    "CallbackGroupJoinType",
    "CallbackGroupLeave",
    "CallbackGroupMarket",
    "CallbackGroupOfficerRole",
    "CallbackGroupOfficersEdit",
    "CallbackGroupSettingsChanges",
    "CallbackLikeAddRemove",
    "CallbackLikeAddRemoveObjectType",
    "CallbackMarketComment",
    "CallbackMarketCommentDelete",
    "CallbackMessageAllowObject",
    "CallbackMessageDeny",
    "CallbackMessageObject",
    "CallbackPhotoComment",
    "CallbackPhotoCommentDelete",
    "CallbackPollVoteNew",
    "CallbackType",
    "CallbackUserBlock",
    "CallbackUserUnblock",
    "CallbackVideoComment",
    "CallbackVideoCommentDelete",
    "CallbackWallCommentDelete",
    "CallsCall",
    "CallsEndState",
    "CallsParticipants",
    "ClientInfoForBots",
    "CommentThread",
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
    "GroupsBannedItem",
    "GroupsCallbackServer",
    "GroupsCallbackServerStatus",
    "GroupsCallbackSettings",
    "GroupsClassifiedsProperties",
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
    "MarketMarketCategoryNested",
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
    "MarketServicesViewType",
    "MessagesActionOneOf",
    "MessagesAudioMessage",
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
    "NotesNote",
    "NotesNoteComment",
    "NotificationsFeedback",
    "NotificationsNotification",
    "NotificationsNotificationItem",
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
    "PhotosPhotoFalseable",
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
    "StatsReachOneOf",
    "StatsSexAge",
    "StatsViews",
    "StatsVisitorsOneOf",
    "StatsWallpostStat",
    "StatusStatus",
    "StickersImageSet",
    "StorageValue",
    "StoreProduct",
    "StoreProductType",
    "StoreProductIcon",
    "StoreStickersKeyword",
    "StoreStickersKeywordSticker",
    "StoreStickersKeywordStickers",
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
    "StoriesStatCategory",
    "StoriesStatLine",
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
    "UsersUser",
    "UsersUserFull",
    "UsersUserXtrType",
    "AccountUserSettings",
    "AdsStatsAge",
    "AdsStatsCities",
    "AdsStatsSex",
    "AdsStatsSexAge",
    "AdsTargSettings",
    "AppsApp",
    "BaseLink",
    "CallbackConfirmation",
    "CallbackMessageAllow",
    "CallbackMessageEdit",
    "CallbackMessageNew",
    "CallbackMessageReply",
    "DatabaseCity",
    "GroupsUserXtrRole",
    "GroupsGroupFull",
    "MarketMarketItemBasicWithGroup",
    "MarketMarketItemFull",
    "MessagesUserXtrInvitedBy",
    "MessagesGetConversationByIdExtended",
    "FriendsRequestsXtrMutual",
    "FriendsUserXtrPhone",
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
