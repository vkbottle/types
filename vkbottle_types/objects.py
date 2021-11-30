import enum
import inspect
import typing
from pydantic import BaseModel


class AccountAccountCounters(BaseModel):
    """VK Object AccountAccountCounters

    app_requests - New app requests number
    events - New events number
    faves - New faves number
    friends - New friends requests number
    friends_recommendations - New friends recommendations number
    friends_suggestions - New friends suggestions number
    gifts - New gifts number
    groups - New groups number
    memories - New memories number
    menu_clips_badge -
    menu_discover_badge -
    messages - New messages number
    notes - New notes number
    notifications - New notifications number
    photos - New photo tags number
    sdk - New sdk number
    """

    app_requests: typing.Optional[int] = None
    events: typing.Optional[int] = None
    faves: typing.Optional[int] = None
    friends: typing.Optional[int] = None
    friends_recommendations: typing.Optional[int] = None
    friends_suggestions: typing.Optional[int] = None
    gifts: typing.Optional[int] = None
    groups: typing.Optional[int] = None
    memories: typing.Optional[int] = None
    menu_clips_badge: typing.Optional[int] = None
    menu_discover_badge: typing.Optional[int] = None
    messages: typing.Optional[int] = None
    notes: typing.Optional[int] = None
    notifications: typing.Optional[int] = None
    photos: typing.Optional[int] = None
    sdk: typing.Optional[int] = None


class AccountInfo(BaseModel):
    """VK Object AccountInfo

    _2fa_required - Two factor authentication is enabled
    country - Country code
    https_required - Information whether HTTPS-only is enabled
    intro - Information whether user has been processed intro
    lang - Language ID
    link_redirects -
    mini_apps_ads_slot_id - Ads slot id for MyTarget
    no_wall_replies - Information whether wall comments should be hidden
    own_posts_default - Information whether only owners posts should be shown
    qr_promotion -
    show_vk_apps_intro -
    subscriptions -
    wishlists_ae_promo_banner_show -
    """

    _2fa_required: typing.Optional["BaseBoolInt"] = None
    country: typing.Optional[str] = None
    https_required: typing.Optional["BaseBoolInt"] = None
    intro: typing.Optional["BaseBoolInt"] = None
    lang: typing.Optional[int] = None
    link_redirects: typing.Optional[typing.Any] = None
    mini_apps_ads_slot_id: typing.Optional[int] = None
    no_wall_replies: typing.Optional["BaseBoolInt"] = None
    own_posts_default: typing.Optional["BaseBoolInt"] = None
    qr_promotion: typing.Optional[int] = None
    show_vk_apps_intro: typing.Optional[bool] = None
    subscriptions: typing.Optional["AccountSubscriptions"] = None
    wishlists_ae_promo_banner_show: typing.Optional["BaseBoolInt"] = None


class AccountNameRequest(BaseModel):
    """VK Object AccountNameRequest

    first_name - First name in request
    id - Request ID needed to cancel the request
    lang - Text to display to user
    last_name - Last name in request
    link_href - href for link in lang field
    link_label - label to display for link in lang field
    status -
    """

    first_name: typing.Optional[str] = None
    id: typing.Optional[int] = None
    lang: typing.Optional[str] = None
    last_name: typing.Optional[str] = None
    link_href: typing.Optional[str] = None
    link_label: typing.Optional[str] = None
    status: typing.Optional["AccountNameRequestStatus"] = None


class AccountNameRequestStatus(enum.Enum):
    """ Request status """

    SUCCESS = "success"
    PROCESSING = "processing"
    DECLINED = "declined"
    WAS_ACCEPTED = "was_accepted"
    WAS_DECLINED = "was_declined"
    DECLINED_WITH_LINK = "declined_with_link"
    RESPONSE = "response"
    RESPONSE_WITH_LINK = "response_with_link"


class LinkType(enum.Enum):
    """ Link type """

    PROFILE = "profile"
    GROUP = "group"
    APP = "app"


class AccountOffer(BaseModel):
    """VK Object AccountOffer

    currency_amount - Currency amount
    description - Offer description
    id - Offer ID
    img - URL of the preview image
    instruction - Instruction how to process the offer
    instruction_html - Instruction how to process the offer (HTML format)
    link_id - Link id
    link_type - Link type
    price - Offer price
    short_description - Offer short description
    tag - Offer tag
    title - Offer title
    """

    currency_amount: typing.Optional[float] = None
    description: typing.Optional[str] = None
    id: typing.Optional[int] = None
    img: typing.Optional[str] = None
    instruction: typing.Optional[str] = None
    instruction_html: typing.Optional[str] = None
    link_id: typing.Optional[int] = None
    link_type: typing.Optional["LinkType"] = None
    price: typing.Optional[int] = None
    short_description: typing.Optional[str] = None
    tag: typing.Optional[str] = None
    title: typing.Optional[str] = None


class AccountPushConversations(BaseModel):
    """VK Object AccountPushConversations

    count - Items count
    items -
    """

    count: typing.Optional[int] = None
    items: typing.Optional[typing.List["AccountPushConversationsItem"]] = None


class AccountPushConversationsItem(BaseModel):
    """VK Object AccountPushConversationsItem

    disabled_mass_mentions - Information whether the mass mentions (like '@all', '@online') are disabled. Can be affected by 'disabled_mentions'
    disabled_mentions - Information whether the mentions are disabled
    disabled_until - Time until that notifications are disabled in seconds
    peer_id - Peer ID
    sound - Information whether the sound are enabled
    """

    disabled_mass_mentions: typing.Optional["BaseBoolInt"] = None
    disabled_mentions: typing.Optional["BaseBoolInt"] = None
    disabled_until: int = None
    peer_id: int = None
    sound: "BaseBoolInt" = None


class AccountPushParams(BaseModel):
    """VK Object AccountPushParams"""

    app_request: typing.Optional[typing.List["AccountPushParamsOnoff"]] = None
    birthday: typing.Optional[typing.List["AccountPushParamsOnoff"]] = None
    chat: typing.Optional[typing.List["AccountPushParamsMode"]] = None
    comment: typing.Optional[typing.List["AccountPushParamsSettings"]] = None
    event_soon: typing.Optional[typing.List["AccountPushParamsOnoff"]] = None
    friend: typing.Optional[typing.List["AccountPushParamsOnoff"]] = None
    friend_accepted: typing.Optional[typing.List["AccountPushParamsOnoff"]] = None
    friend_found: typing.Optional[typing.List["AccountPushParamsOnoff"]] = None
    group_accepted: typing.Optional[typing.List["AccountPushParamsOnoff"]] = None
    group_invite: typing.Optional[typing.List["AccountPushParamsOnoff"]] = None
    like: typing.Optional[typing.List["AccountPushParamsSettings"]] = None
    mention: typing.Optional[typing.List["AccountPushParamsSettings"]] = None
    msg: typing.Optional[typing.List["AccountPushParamsMode"]] = None
    new_post: typing.Optional[typing.List["AccountPushParamsOnoff"]] = None
    reply: typing.Optional[typing.List["AccountPushParamsOnoff"]] = None
    repost: typing.Optional[typing.List["AccountPushParamsSettings"]] = None
    sdk_open: typing.Optional[typing.List["AccountPushParamsOnoff"]] = None
    wall_post: typing.Optional[typing.List["AccountPushParamsOnoff"]] = None
    wall_publish: typing.Optional[typing.List["AccountPushParamsOnoff"]] = None


class AccountPushParamsMode(enum.Enum):
    """ Settings parameters """

    ON = "on"
    OFF = "off"
    NO_SOUND = "no_sound"
    NO_TEXT = "no_text"


class AccountPushParamsOnoff(enum.Enum):
    """ Settings parameters """

    ON = "on"
    OFF = "off"


class AccountPushParamsSettings(enum.Enum):
    """ Settings parameters """

    ON = "on"
    OFF = "off"
    FR_OF_FR = "fr_of_fr"


class AccountPushSettings(BaseModel):
    """VK Object AccountPushSettings

    conversations -
    disabled - Information whether notifications are disabled
    disabled_until - Time until that notifications are disabled in Unixtime
    settings -
    """

    conversations: typing.Optional["AccountPushConversations"] = None
    disabled: typing.Optional["BaseBoolInt"] = None
    disabled_until: typing.Optional[int] = None
    settings: typing.Optional["AccountPushParams"] = None


AccountSubscriptions = typing.List[int]


class UsersUserMin(BaseModel):
    """VK Object UsersUserMin

    can_access_closed -
    deactivated - Returns if a profile is deleted or blocked
    first_name - User first name
    hidden - Returns if a profile is hidden.
    id - User ID
    is_closed -
    last_name - User last name
    """

    can_access_closed: typing.Optional[bool] = None
    deactivated: typing.Optional[str] = None
    first_name: str = None
    hidden: typing.Optional[int] = None
    id: int = None
    is_closed: typing.Optional[bool] = None
    last_name: str = None


class UsersUserSettingsXtr(BaseModel):
    """VK Object UsersUserSettingsXtr

    bdate - User's date of birth
    bdate_visibility - Information whether user's birthdate are hidden
    city -
    connections -
    country -
    first_name - User first name
    home_town - User's hometown
    interests -
    languages -
    last_name - User last name
    maiden_name - User maiden name
    name_request -
    personal -
    phone - User phone number with some hidden digits
    relation - User relationship status
    relation_partner -
    relation_pending - Information whether relation status is pending
    relation_requests -
    screen_name - Domain name of the user's page
    sex - User sex
    status - User status
    status_audio -
    """

    bdate: typing.Optional[str] = None
    bdate_visibility: typing.Optional[int] = None
    city: typing.Optional["BaseCity"] = None
    connections: typing.Optional["UsersUserConnections"] = None
    country: typing.Optional["BaseCountry"] = None
    first_name: typing.Optional[str] = None
    home_town: str = None
    interests: typing.Optional["AccountUserSettingsInterests"] = None
    languages: typing.Optional[typing.List[str]] = None
    last_name: typing.Optional[str] = None
    maiden_name: typing.Optional[str] = None
    name_request: typing.Optional["AccountNameRequest"] = None
    personal: typing.Optional["UsersPersonal"] = None
    phone: typing.Optional[str] = None
    relation: typing.Optional["UsersUserRelation"] = None
    relation_partner: typing.Optional["UsersUserMin"] = None
    relation_pending: typing.Optional["BaseBoolInt"] = None
    relation_requests: typing.Optional[typing.List["UsersUserMin"]] = None
    screen_name: typing.Optional[str] = None
    sex: typing.Optional["BaseSex"] = None
    status: str = None
    status_audio: typing.Optional["AudioAudio"] = None


class AccountUserSettings(UsersUserMin, UsersUserSettingsXtr):
    """VK Object AccountUserSettings

    is_service_account - flag about service account
    photo_200 - URL of square photo of the user with 200 pixels in width
    """

    is_service_account: typing.Optional[bool] = None
    photo_200: typing.Optional[str] = None


class AccountUserSettingsInterest(BaseModel):
    """VK Object AccountUserSettingsInterest"""

    title: str = None
    value: str = None


class AccountUserSettingsInterests(BaseModel):
    """VK Object AccountUserSettingsInterests"""

    about: typing.Optional["AccountUserSettingsInterest"] = None
    activities: typing.Optional["AccountUserSettingsInterest"] = None
    books: typing.Optional["AccountUserSettingsInterest"] = None
    games: typing.Optional["AccountUserSettingsInterest"] = None
    interests: typing.Optional["AccountUserSettingsInterest"] = None
    movies: typing.Optional["AccountUserSettingsInterest"] = None
    music: typing.Optional["AccountUserSettingsInterest"] = None
    quotes: typing.Optional["AccountUserSettingsInterest"] = None
    tv: typing.Optional["AccountUserSettingsInterest"] = None


class AddressesFields(enum.Enum):
    """ AddressesFields enum """

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
    """ Current user's role """

    ADMIN = "admin"
    MANAGER = "manager"
    REPORTS = "reports"


class AdsAccessRolePublic(enum.Enum):
    """ Current user's role """

    MANAGER = "manager"
    REPORTS = "reports"


class AdsAccesses(BaseModel):
    """VK Object AdsAccesses

    client_id - Client ID
    role -
    """

    client_id: typing.Optional[str] = None
    role: typing.Optional["AdsAccessRole"] = None


class AdsAccount(BaseModel):
    """VK Object AdsAccount

    access_role -
    account_id - Account ID
    account_name - Account name
    account_status - Information whether account is active
    account_type -
    can_view_budget - Can user view account budget
    """

    access_role: "AdsAccessRole" = None
    account_id: int = None
    account_name: str = None
    account_status: "BaseBoolInt" = None
    account_type: "AdsAccountType" = None
    can_view_budget: bool = None


class AdsAccountType(enum.Enum):
    """ Account type """

    GENERAL = "general"
    AGENCY = "agency"


class AdsAd(BaseModel):
    """VK Object AdsAd

    ad_format - Ad format
    ad_platform - Ad platform
    all_limit - Total limit
    approved -
    autobidding_max_cost - Max cost of target actions for autobidding, kopecks
    campaign_id - Campaign ID
    category1_id - Category ID
    category2_id - Additional category ID
    cost_type -
    cpa - Cost of an action, kopecks
    cpc - Cost of a click, kopecks
    cpm - Cost of 1000 impressions, kopecks
    disclaimer_medical - Information whether disclaimer is enabled
    disclaimer_specialist - Information whether disclaimer is enabled
    disclaimer_supplements - Information whether disclaimer is enabled
    id - Ad ID
    impressions_limit - Impressions limit
    impressions_limited - Information whether impressions are limited
    name - Ad title
    ocpm - Cost of 1000 impressions optimized, kopecks
    status -
    video - Information whether the ad is a video
    """

    ad_format: int = None
    ad_platform: typing.Optional[typing.Union[int, str]] = None
    all_limit: int = None
    approved: "AdsAdApproved" = None
    autobidding_max_cost: typing.Optional[int] = None
    campaign_id: int = None
    category1_id: typing.Optional[int] = None
    category2_id: typing.Optional[int] = None
    cost_type: "AdsAdCostType" = None
    cpa: typing.Optional[int] = None
    cpc: typing.Optional[int] = None
    cpm: typing.Optional[int] = None
    disclaimer_medical: typing.Optional["BaseBoolInt"] = None
    disclaimer_specialist: typing.Optional["BaseBoolInt"] = None
    disclaimer_supplements: typing.Optional["BaseBoolInt"] = None
    id: int = None
    impressions_limit: typing.Optional[int] = None
    impressions_limited: typing.Optional["BaseBoolInt"] = None
    name: str = None
    ocpm: typing.Optional[int] = None
    status: "AdsAdStatus" = None
    video: typing.Optional["BaseBoolInt"] = None


class AdsAdApproved(enum.IntEnum):
    """ Review status """

    not_moderated = 0
    pending_moderation = 1
    approved = 2
    rejected = 3


class AdsAdCostType(enum.IntEnum):
    """ Cost type """

    per_clicks = 0
    per_impressions = 1
    per_actions = 2
    per_impressions_optimized = 3


class AdsAdLayout(BaseModel):
    """VK Object AdsAdLayout

    ad_format - Ad format
    campaign_id - Campaign ID
    cost_type -
    description - Ad description
    id - Ad ID
    image_src - Image URL
    image_src_2x - URL of the preview image in double size
    link_domain - Domain of advertised object
    link_url - URL of advertised object
    preview_link - link to preview an ad as it is shown on the website
    title - Ad title
    video - Information whether the ad is a video
    """

    ad_format: int = None
    campaign_id: int = None
    cost_type: "AdsAdCostType" = None
    description: str = None
    id: str = None
    image_src: str = None
    image_src_2x: typing.Optional[str] = None
    link_domain: typing.Optional[str] = None
    link_url: str = None
    preview_link: typing.Optional[str] = None
    title: str = None
    video: typing.Optional["BaseBoolInt"] = None


class AdsAdStatus(enum.IntEnum):
    """ Ad atatus """

    stopped = 0
    started = 1
    deleted = 2


class AdsCampaign(BaseModel):
    """VK Object AdsCampaign

    ads_count - Amount of active ads in campaign
    all_limit - Campaign's total limit, rubles
    create_time - Campaign create time, as Unixtime
    day_limit - Campaign's day limit, rubles
    goal_type - Campaign goal type
    id - Campaign ID
    is_cbo_enabled - Shows if Campaign Budget Optimization is on
    name - Campaign title
    start_time - Campaign start time, as Unixtime
    status -
    stop_time - Campaign stop time, as Unixtime
    type -
    update_time - Campaign update time, as Unixtime
    user_goal_type - Campaign user goal type
    views_limit - Limit of views per user per campaign
    """

    ads_count: typing.Optional[int] = None
    all_limit: str = None
    create_time: typing.Optional[int] = None
    day_limit: str = None
    goal_type: typing.Optional[int] = None
    id: int = None
    is_cbo_enabled: typing.Optional[bool] = None
    name: str = None
    start_time: int = None
    status: "AdsCampaignStatus" = None
    stop_time: int = None
    type: "AdsCampaignType" = None
    update_time: typing.Optional[int] = None
    user_goal_type: typing.Optional[int] = None
    views_limit: typing.Optional[int] = None


class AdsCampaignStatus(enum.IntEnum):
    """ Campaign status """

    stopped = 0
    started = 1
    deleted = 2


class AdsCampaignType(enum.Enum):
    """ Campaign type """

    NORMAL = "normal"
    VK_APPS_MANAGED = "vk_apps_managed"
    MOBILE_APPS = "mobile_apps"
    PROMOTED_POSTS = "promoted_posts"
    ADAPTIVE_ADS = "adaptive_ads"
    STORIES = "stories"


class AdsCategory(BaseModel):
    """VK Object AdsCategory

    id - Category ID
    name - Category name
    subcategories -
    """

    id: int = None
    name: str = None
    subcategories: typing.Optional[typing.List["BaseObjectWithName"]] = None


class AdsClient(BaseModel):
    """VK Object AdsClient

    all_limit - Client's total limit, rubles
    day_limit - Client's day limit, rubles
    id - Client ID
    name - Client name
    """

    all_limit: str = None
    day_limit: str = None
    id: int = None
    name: str = None


class AdsCriteria(BaseModel):
    """VK Object AdsCriteria

    age_from - Age from
    age_to - Age to
    apps - Apps IDs
    apps_not - Apps IDs to except
    birthday - Days to birthday
    cities - Cities IDs
    cities_not - Cities IDs to except
    country - Country ID
    districts - Districts IDs
    groups - Communities IDs
    interest_categories - Interests categories IDs
    interests - Interests
    paying - Information whether the user has proceeded VK payments before
    positions - Positions IDs
    religions - Religions IDs
    retargeting_groups - Retargeting groups IDs
    retargeting_groups_not - Retargeting groups IDs to except
    school_from - School graduation year from
    school_to - School graduation year to
    schools - Schools IDs
    sex -
    stations - Stations IDs
    statuses - Relationship statuses
    streets - Streets IDs
    travellers - Travellers only
    uni_from - University graduation year from
    uni_to - University graduation year to
    user_browsers - Browsers
    user_devices - Devices
    user_os - Operating systems
    """

    age_from: typing.Optional[int] = None
    age_to: typing.Optional[int] = None
    apps: typing.Optional[str] = None
    apps_not: typing.Optional[str] = None
    birthday: typing.Optional[int] = None
    cities: typing.Optional[str] = None
    cities_not: typing.Optional[str] = None
    country: typing.Optional[int] = None
    districts: typing.Optional[str] = None
    groups: typing.Optional[str] = None
    interest_categories: typing.Optional[str] = None
    interests: typing.Optional[str] = None
    paying: typing.Optional["BaseBoolInt"] = None
    positions: typing.Optional[str] = None
    religions: typing.Optional[str] = None
    retargeting_groups: typing.Optional[str] = None
    retargeting_groups_not: typing.Optional[str] = None
    school_from: typing.Optional[int] = None
    school_to: typing.Optional[int] = None
    schools: typing.Optional[str] = None
    sex: typing.Optional["AdsCriteriaSex"] = None
    stations: typing.Optional[str] = None
    statuses: typing.Optional[str] = None
    streets: typing.Optional[str] = None
    travellers: typing.Optional["BasePropertyExists"] = None
    uni_from: typing.Optional[int] = None
    uni_to: typing.Optional[int] = None
    user_browsers: typing.Optional[str] = None
    user_devices: typing.Optional[str] = None
    user_os: typing.Optional[str] = None


class AdsCriteriaSex(enum.IntEnum):
    """ Sex """

    any = 0
    male = 1
    female = 2


class AdsDemoStats(BaseModel):
    """VK Object AdsDemoStats

    id - Object ID
    stats -
    type -
    """

    id: typing.Optional[int] = None
    stats: typing.Optional["AdsDemostatsFormat"] = None
    type: typing.Optional["AdsObjectType"] = None


class AdsDemostatsFormat(BaseModel):
    """VK Object AdsDemostatsFormat

    age -
    cities -
    day - Day as YYYY-MM-DD
    month - Month as YYYY-MM
    overall - 1 if period=overall
    sex -
    sex_age -
    """

    age: typing.Optional[typing.List["AdsStatsAge"]] = None
    cities: typing.Optional[typing.List["AdsStatsCities"]] = None
    day: typing.Optional[str] = None
    month: typing.Optional[str] = None
    overall: typing.Optional[int] = None
    sex: typing.Optional[typing.List["AdsStatsSex"]] = None
    sex_age: typing.Optional[typing.List["AdsStatsSexAge"]] = None


class AdsFloodStats(BaseModel):
    """VK Object AdsFloodStats

    left - Requests left
    refresh - Time to refresh in seconds
    """

    left: int = None
    refresh: int = None


class AdsLinkStatus(BaseModel):
    """VK Object AdsLinkStatus

    description - Reject reason
    redirect_url - URL
    status - Link status
    """

    description: str = None
    redirect_url: str = None
    status: str = None


class LookalikeRequestStatus(enum.Enum):
    """ Lookalike request status """

    SEARCH_IN_PROGRESS = "search_in_progress"
    SEARCH_FAILED = "search_failed"
    SEARCH_DONE = "search_done"
    SAVE_IN_PROGRESS = "save_in_progress"
    SAVE_FAILED = "save_failed"
    SAVE_DONE = "save_done"


class LookalikeRequestSourceType(enum.Enum):
    """ Lookalike request source type """

    RETARGETING_GROUP = "retargeting_group"


class AdsLookalikeRequest(BaseModel):
    """VK Object AdsLookalikeRequest

    audience_count - Lookalike request seed audience size
    create_time - Lookalike request create time, as Unixtime
    id - Lookalike request ID
    save_audience_levels -
    scheduled_delete_time - Time by which lookalike request would be deleted, as Unixtime
    source_name - Lookalike request seed name (retargeting group name)
    source_retargeting_group_id - Retargeting group id, which was used as lookalike seed
    source_type - Lookalike request source type
    status - Lookalike request status
    update_time - Lookalike request update time, as Unixtime
    """

    audience_count: typing.Optional[int] = None
    create_time: int = None
    id: int = None
    save_audience_levels: typing.Optional[typing.List["AdsLookalikeRequestSaveAudienceLevel"]] = None
    scheduled_delete_time: typing.Optional[int] = None
    source_name: typing.Optional[str] = None
    source_retargeting_group_id: typing.Optional[int] = None
    source_type: "LookalikeRequestSourceType" = None
    status: "LookalikeRequestStatus" = None
    update_time: int = None


class AdsLookalikeRequestSaveAudienceLevel(BaseModel):
    """VK Object AdsLookalikeRequestSaveAudienceLevel

    audience_count - Saved audience audience size for according level
    level - Save audience level id, which is used in save audience queries
    """

    audience_count: typing.Optional[int] = None
    level: typing.Optional[int] = None


class AdsMusician(BaseModel):
    """VK Object AdsMusician

    avatar - Music artist photo
    id - Targeting music artist ID
    name - Music artist name
    """

    avatar: typing.Optional[str] = None
    id: int = None
    name: str = None


class AdsObjectType(enum.Enum):
    """ Object type """

    AD = "ad"
    CAMPAIGN = "campaign"
    CLIENT = "client"
    OFFICE = "office"


class AdsParagraphs(BaseModel):
    """VK Object AdsParagraphs

    paragraph - Rules paragraph
    """

    paragraph: typing.Optional[str] = None


class AdsPromotedPostReach(BaseModel):
    """VK Object AdsPromotedPostReach

    hide - Hides amount
    id - Object ID from 'ids' parameter
    join_group - Community joins
    links - Link clicks
    reach_subscribers - Subscribers reach
    reach_total - Total reach
    report - Reports amount
    to_group - Community clicks
    unsubscribe - 'Unsubscribe' events amount
    video_views_100p - Video views for 100 percent
    video_views_25p - Video views for 25 percent
    video_views_3s - Video views for 3 seconds
    video_views_50p - Video views for 50 percent
    video_views_75p - Video views for 75 percent
    video_views_start - Video starts
    """

    hide: int = None
    id: int = None
    join_group: int = None
    links: int = None
    reach_subscribers: int = None
    reach_total: int = None
    report: int = None
    to_group: int = None
    unsubscribe: int = None
    video_views_100p: typing.Optional[int] = None
    video_views_25p: typing.Optional[int] = None
    video_views_3s: typing.Optional[int] = None
    video_views_50p: typing.Optional[int] = None
    video_views_75p: typing.Optional[int] = None
    video_views_start: typing.Optional[int] = None


class AdsRejectReason(BaseModel):
    """VK Object AdsRejectReason

    comment - Comment text
    rules -
    """

    comment: typing.Optional[str] = None
    rules: typing.Optional[typing.List["AdsRules"]] = None


class AdsRules(BaseModel):
    """VK Object AdsRules

    paragraphs -
    title - Comment
    """

    paragraphs: typing.Optional[typing.List["AdsParagraphs"]] = None
    title: typing.Optional[str] = None


class AdsStats(BaseModel):
    """VK Object AdsStats

    id - Object ID
    stats -
    type -
    views_times -
    """

    id: typing.Optional[int] = None
    stats: typing.Optional["AdsStatsFormat"] = None
    type: typing.Optional["AdsObjectType"] = None
    views_times: typing.Optional["AdsStatsViewsTimes"] = None


class AdsStatsAge(BaseModel):
    """VK Object AdsStatsAge

    clicks_rate - Clicks rate
    impressions_rate - Impressions rate
    value - Age interval
    """

    clicks_rate: typing.Optional[float] = None
    impressions_rate: typing.Optional[float] = None
    value: typing.Optional[str] = None


class AdsStatsCities(BaseModel):
    """VK Object AdsStatsCities

    clicks_rate - Clicks rate
    impressions_rate - Impressions rate
    name - City name
    value - City ID
    """

    clicks_rate: typing.Optional[float] = None
    impressions_rate: typing.Optional[float] = None
    name: typing.Optional[str] = None
    value: typing.Optional[int] = None


class AdsStatsFormat(BaseModel):
    """VK Object AdsStatsFormat

    clicks - Clicks number
    day - Day as YYYY-MM-DD
    impressions - Impressions number
    join_rate - Events number
    link_external_clicks - External clicks number
    month - Month as YYYY-MM
    overall - 1 if period=overall
    reach - Reach
    spent - Spent funds
    video_clicks_site - Clickthoughs to the advertised site
    video_views - Video views number
    video_views_full - Video views (full video)
    video_views_half - Video views (half of video)
    """

    clicks: typing.Optional[int] = None
    day: typing.Optional[str] = None
    impressions: typing.Optional[int] = None
    join_rate: typing.Optional[int] = None
    link_external_clicks: typing.Optional[int] = None
    month: typing.Optional[str] = None
    overall: typing.Optional[int] = None
    reach: typing.Optional[int] = None
    spent: typing.Optional[int] = None
    video_clicks_site: typing.Optional[int] = None
    video_views: typing.Optional[int] = None
    video_views_full: typing.Optional[int] = None
    video_views_half: typing.Optional[int] = None


class AdsStatsSex(BaseModel):
    """VK Object AdsStatsSex

    clicks_rate - Clicks rate
    impressions_rate - Impressions rate
    value -
    """

    clicks_rate: typing.Optional[float] = None
    impressions_rate: typing.Optional[float] = None
    value: typing.Optional["AdsStatsSexValue"] = None


class AdsStatsSexAge(BaseModel):
    """VK Object AdsStatsSexAge

    clicks_rate - Clicks rate
    impressions_rate - Impressions rate
    value - Sex and age interval
    """

    clicks_rate: typing.Optional[float] = None
    impressions_rate: typing.Optional[float] = None
    value: typing.Optional[str] = None


class AdsStatsSexValue(enum.Enum):
    """ Sex """

    F = "f"
    M = "m"


class AdsStatsViewsTimes(BaseModel):
    """VK Object AdsStatsViewsTimes"""

    views_ads_times_1: typing.Optional[int] = None
    views_ads_times_10: typing.Optional[int] = None
    views_ads_times_11_plus: typing.Optional[int] = None
    views_ads_times_2: typing.Optional[int] = None
    views_ads_times_3: typing.Optional[int] = None
    views_ads_times_4: typing.Optional[int] = None
    views_ads_times_5: typing.Optional[str] = None
    views_ads_times_6: typing.Optional[int] = None
    views_ads_times_7: typing.Optional[int] = None
    views_ads_times_8: typing.Optional[int] = None
    views_ads_times_9: typing.Optional[int] = None


class AdsTargSettings(AdsCriteria):
    """VK Object AdsTargSettings

    campaign_id - Campaign ID
    id - Ad ID
    """

    campaign_id: typing.Optional[int] = None
    id: typing.Optional[int] = None


class AdsTargStats(BaseModel):
    """VK Object AdsTargStats

    audience_count - Audience
    recommended_cpc - Recommended CPC value for 50% reach (old format)
    recommended_cpc_50 - Recommended CPC value for 50% reach
    recommended_cpc_70 - Recommended CPC value for 70% reach
    recommended_cpc_90 - Recommended CPC value for 90% reach
    recommended_cpm - Recommended CPM value for 50% reach (old format)
    recommended_cpm_50 - Recommended CPM value for 50% reach
    recommended_cpm_70 - Recommended CPM value for 70% reach
    recommended_cpm_90 - Recommended CPM value for 90% reach
    """

    audience_count: int = None
    recommended_cpc: typing.Optional[float] = None
    recommended_cpc_50: typing.Optional[float] = None
    recommended_cpc_70: typing.Optional[float] = None
    recommended_cpc_90: typing.Optional[float] = None
    recommended_cpm: typing.Optional[float] = None
    recommended_cpm_50: typing.Optional[float] = None
    recommended_cpm_70: typing.Optional[float] = None
    recommended_cpm_90: typing.Optional[float] = None


class AdsTargSuggestions(BaseModel):
    """VK Object AdsTargSuggestions

    id - Object ID
    name - Object name
    """

    id: typing.Optional[int] = None
    name: typing.Optional[str] = None


class AdsTargSuggestionsCities(BaseModel):
    """VK Object AdsTargSuggestionsCities

    id - Object ID
    name - Object name
    parent - Parent object
    """

    id: typing.Optional[int] = None
    name: typing.Optional[str] = None
    parent: typing.Optional[str] = None


class AdsTargSuggestionsRegions(BaseModel):
    """VK Object AdsTargSuggestionsRegions

    id - Object ID
    name - Object name
    type - Object type
    """

    id: typing.Optional[int] = None
    name: typing.Optional[str] = None
    type: typing.Optional[str] = None


class AdsTargSuggestionsSchools(BaseModel):
    """VK Object AdsTargSuggestionsSchools

    desc - Full school title
    id - School ID
    name - School title
    parent - City name
    type -
    """

    desc: typing.Optional[str] = None
    id: typing.Optional[int] = None
    name: typing.Optional[str] = None
    parent: typing.Optional[str] = None
    type: typing.Optional["AdsTargSuggestionsSchoolsType"] = None


class AdsTargSuggestionsSchoolsType(enum.Enum):
    """ School type """

    SCHOOL = "school"
    UNIVERSITY = "university"
    FACULTY = "faculty"
    CHAIR = "chair"


class AdsTargetGroup(BaseModel):
    """VK Object AdsTargetGroup

    audience_count - Audience
    domain - Site domain
    id - Group ID
    lifetime - Number of days for user to be in group
    name - Group name
    pixel - Pixel code
    """

    audience_count: typing.Optional[int] = None
    domain: typing.Optional[str] = None
    id: typing.Optional[int] = None
    lifetime: typing.Optional[int] = None
    name: typing.Optional[str] = None
    pixel: typing.Optional[str] = None


class AdsUpdateOfficeUsersResult(BaseModel):
    """VK Object AdsUpdateOfficeUsersResult"""

    error: typing.Optional["BaseError"] = None
    is_success: bool = None
    user_id: int = None


class AdsUserSpecification(BaseModel):
    """VK Object AdsUserSpecification"""

    client_ids: typing.Optional[typing.List[int]] = None
    grant_access_to_all_clients: typing.Optional[bool] = None
    role: "AdsAccessRolePublic" = None
    user_id: int = None
    view_budget: typing.Optional[bool] = None


class AdsUserSpecificationCutted(BaseModel):
    """VK Object AdsUserSpecificationCutted"""

    client_id: typing.Optional[int] = None
    role: "AdsAccessRolePublic" = None
    user_id: int = None
    view_budget: typing.Optional[bool] = None


class AdsUsers(BaseModel):
    """VK Object AdsUsers

    accesses -
    user_id - User ID
    """

    accesses: typing.List["AdsAccesses"] = None
    user_id: int = None


class AdswebGetAdCategoriesResponseCategoriesCategory(BaseModel):
    """VK Object AdswebGetAdCategoriesResponseCategoriesCategory"""

    id: int = None
    name: str = None


class AdswebGetAdUnitsResponseAdUnitsAdUnit(BaseModel):
    """VK Object AdswebGetAdUnitsResponseAdUnitsAdUnit"""

    id: int = None
    name: typing.Optional[str] = None
    site_id: int = None


class AdswebGetFraudHistoryResponseEntriesEntry(BaseModel):
    """VK Object AdswebGetFraudHistoryResponseEntriesEntry"""

    day: str = None
    site_id: int = None


class AdswebGetSitesResponseSitesSite(BaseModel):
    """VK Object AdswebGetSitesResponseSitesSite"""

    domains: typing.Optional[str] = None
    id: int = None
    status_moder: typing.Optional[str] = None
    status_user: typing.Optional[str] = None


class AdswebGetStatisticsResponseItemsItem(BaseModel):
    """VK Object AdswebGetStatisticsResponseItemsItem"""

    ad_unit_id: typing.Optional[int] = None
    day_max: typing.Optional[str] = None
    day_min: typing.Optional[str] = None
    days_count: typing.Optional[int] = None
    hour_max: typing.Optional[str] = None
    hour_min: typing.Optional[str] = None
    hours_count: typing.Optional[int] = None
    month_max: typing.Optional[str] = None
    month_min: typing.Optional[str] = None
    months_count: typing.Optional[int] = None
    overall_count: typing.Optional[int] = None
    site_id: typing.Optional[int] = None


class AppWidgetsPhoto(BaseModel):
    """VK Object AppWidgetsPhoto

    id - Image ID
    images -
    """

    id: str = None
    images: typing.List["BaseImage"] = None


class AppWidgetsPhotos(BaseModel):
    """VK Object AppWidgetsPhotos"""

    count: typing.Optional[int] = None
    items: typing.Optional[typing.List["AppWidgetsPhoto"]] = None


class AppsAppMin(BaseModel):
    """VK Object AppsAppMin

    author_owner_id - Application author's ID
    background_loader_color - Hex color code without hash sign
    icon_139 - URL of the app icon with 139 px in width
    icon_150 - URL of the app icon with 150 px in width
    icon_278 - URL of the app icon with 278 px in width
    icon_576 - URL of the app icon with 576 px in width
    icon_75 - URL of the app icon with 75 px in width
    id - Application ID
    is_installed - Is application installed
    loader_icon - SVG data
    title - Application title
    type -
    """

    author_owner_id: typing.Optional[int] = None
    background_loader_color: typing.Optional[str] = None
    icon_139: typing.Optional[str] = None
    icon_150: typing.Optional[str] = None
    icon_278: typing.Optional[str] = None
    icon_576: typing.Optional[str] = None
    icon_75: typing.Optional[str] = None
    id: int = None
    is_installed: typing.Optional[bool] = None
    loader_icon: typing.Optional[str] = None
    title: str = None
    type: "AppsAppType" = None


class AppsApp(AppsAppMin):
    """VK Object AppsApp

    author_url - Application author's URL
    banner_1120 - URL of the app banner with 1120 px in width
    banner_560 - URL of the app banner with 560 px in width
    catalog_position - Catalog position
    description - Application description
    friends -
    genre - Genre name
    genre_id - Genre ID
    icon_16 - URL of the app icon with 16 px in width
    international - Information whether the application is multilanguage
    is_in_catalog - Information whether application is in mobile catalog
    is_new - Is new flag
    leaderboard_type -
    members_count - Members number
    platform_id - Application ID in store
    published_date - Date when the application has been published in Unixtime
    push_enabled - Is push enabled
    screen_name - Screen name
    screen_orientation - Screen orientation
    section - Application section name
    """

    author_url: typing.Optional[str] = None
    banner_1120: typing.Optional[str] = None
    banner_560: typing.Optional[str] = None
    catalog_position: typing.Optional[int] = None
    description: typing.Optional[str] = None
    friends: typing.Optional[typing.List[int]] = None
    genre: typing.Optional[str] = None
    genre_id: typing.Optional[int] = None
    icon_16: typing.Optional[str] = None
    international: typing.Optional[bool] = None
    is_in_catalog: typing.Optional[int] = None
    is_new: typing.Optional["BaseBoolInt"] = None
    leaderboard_type: typing.Optional["AppsAppLeaderboardType"] = None
    members_count: typing.Optional[int] = None
    platform_id: typing.Optional[str] = None
    published_date: typing.Optional[int] = None
    push_enabled: typing.Optional["BaseBoolInt"] = None
    screen_name: typing.Optional[str] = None
    screen_orientation: typing.Optional[int] = None
    section: typing.Optional[str] = None


class AppsAppLeaderboardType(enum.IntEnum):
    """ Leaderboard type """

    not_supported = 0
    levels = 1
    points = 2


class AppsAppType(enum.Enum):
    """ Application type """

    APP = "app"
    GAME = "game"
    SITE = "site"
    STANDALONE = "standalone"
    VK_APP = "vk_app"
    COMMUNITY_APP = "community_app"
    HTML5_GAME = "html5_game"
    MINI_APP = "mini_app"


class AppsCatalogList(BaseModel):
    """VK Object AppsCatalogList

    count - Total number
    items -
    profiles -
    """

    count: int = None
    items: typing.List["AppsApp"] = None
    profiles: typing.Optional[typing.List["UsersUserMin"]] = None


class AppsLeaderboard(BaseModel):
    """VK Object AppsLeaderboard

    level - Level
    points - Points number
    score - Score number
    user_id - User ID
    """

    level: typing.Optional[int] = None
    points: typing.Optional[int] = None
    score: typing.Optional[int] = None
    user_id: int = None


class ScopeName(enum.Enum):
    """ Scope name """

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


class AppsScope(BaseModel):
    """VK Object AppsScope

    name - Scope name
    title - Scope title
    """

    name: "ScopeName" = None
    title: typing.Optional[str] = None


class AudioAudio(BaseModel):
    """VK Object AudioAudio

    access_key - Access key for the audio
    album_id - Album ID
    artist - Artist name
    date - Date when uploaded
    duration - Duration in seconds
    genre_id - Genre ID
    id - Audio ID
    owner_id - Audio owner's ID
    performer - Performer name
    title - Title
    url - URL of mp3 file
    """

    access_key: typing.Optional[str] = None
    album_id: typing.Optional[int] = None
    artist: str = None
    date: typing.Optional[int] = None
    duration: int = None
    genre_id: typing.Optional[int] = None
    id: int = None
    owner_id: int = None
    performer: typing.Optional[str] = None
    title: str = None
    url: typing.Optional[str] = None


class BaseBoolInt(enum.IntEnum):
    """ BaseBoolInt enum """

    no = 0
    yes = 1


class BaseCity(BaseModel):
    """VK Object BaseCity

    id - City ID
    title - City title
    """

    id: int = None
    title: str = None


class BaseCommentsInfo(BaseModel):
    """VK Object BaseCommentsInfo

    can_close -
    can_open -
    can_post - Information whether current user can comment the post
    count - Comments number
    donut -
    groups_can_post - Information whether groups can comment the post
    """

    can_close: typing.Optional["BaseBoolInt"] = None
    can_open: typing.Optional["BaseBoolInt"] = None
    can_post: typing.Optional["BaseBoolInt"] = None
    count: typing.Optional[int] = None
    donut: typing.Optional["WallWallpostCommentsDonut"] = None
    groups_can_post: typing.Optional[bool] = None


class BaseCountry(BaseModel):
    """VK Object BaseCountry

    id - Country ID
    title - Country title
    """

    id: int = None
    title: str = None


class BaseCropPhoto(BaseModel):
    """VK Object BaseCropPhoto"""

    crop: "BaseCropPhotoCrop" = None
    photo: "PhotosPhoto" = None
    rect: "BaseCropPhotoRect" = None


class BaseCropPhotoCrop(BaseModel):
    """VK Object BaseCropPhotoCrop

    x - Coordinate X of the left upper corner
    x2 - Coordinate X of the right lower corner
    y - Coordinate Y of the left upper corner
    y2 - Coordinate Y of the right lower corner
    """

    x: float = None
    x2: float = None
    y: float = None
    y2: float = None


class BaseCropPhotoRect(BaseModel):
    """VK Object BaseCropPhotoRect

    x - Coordinate X of the left upper corner
    x2 - Coordinate X of the right lower corner
    y - Coordinate Y of the left upper corner
    y2 - Coordinate Y of the right lower corner
    """

    x: float = None
    x2: float = None
    y: float = None
    y2: float = None


class BaseError(BaseModel):
    """VK Object BaseError

    error_code - Error code
    error_msg - Error message
    error_subcode - Error subcode
    error_text - Localized error message
    request_params -
    """

    error_code: int = None
    error_msg: typing.Optional[str] = None
    error_subcode: typing.Optional[int] = None
    error_text: typing.Optional[str] = None
    request_params: typing.Optional[typing.List["BaseRequestParam"]] = None


class BaseGeo(BaseModel):
    """VK Object BaseGeo

    coordinates -
    place -
    showmap - Information whether a map is showed
    type - Place type
    """

    coordinates: typing.Optional["BaseGeoCoordinates"] = None
    place: typing.Optional["BasePlace"] = None
    showmap: typing.Optional[int] = None
    type: typing.Optional[str] = None


class BaseGeoCoordinates(BaseModel):
    """VK Object BaseGeoCoordinates"""

    latitude: float = None
    longitude: float = None


class BaseGradientPoint(BaseModel):
    """VK Object BaseGradientPoint

    color - Hex color code without #
    position - Point position
    """

    color: str = None
    position: float = None


class BaseImage(BaseModel):
    """VK Object BaseImage

    height - Image height
    id -
    url - Image url
    width - Image width
    """

    height: int = None
    id: typing.Optional[str] = None
    url: str = None
    width: int = None


class BaseLikes(BaseModel):
    """VK Object BaseLikes

    count - Likes number
    user_likes - Information whether current user likes the photo
    """

    count: typing.Optional[int] = None
    user_likes: typing.Optional["BaseBoolInt"] = None


class BaseLikesInfo(BaseModel):
    """VK Object BaseLikesInfo

    can_like - Information whether current user can like the post
    can_publish - Information whether current user can repost
    count - Likes number
    user_likes - Information whether current uer has liked the post
    """

    can_like: "BaseBoolInt" = None
    can_publish: typing.Optional["BaseBoolInt"] = None
    count: int = None
    user_likes: int = None


class BaseLink(BaseModel):
    """VK Object BaseLink

    application -
    button -
    caption - Link caption
    description - Link description
    id - Link ID
    is_external - Information whether the current link is external
    is_favorite -
    photo -
    preview_page - String ID of the page with article preview
    preview_url - URL of the page with article preview
    product -
    rating -
    target_object -
    title - Link title
    url - Link URL
    video - Video from link
    """

    application: typing.Optional["BaseLinkApplication"] = None
    button: typing.Optional["BaseLinkButton"] = None
    caption: typing.Optional[str] = None
    description: typing.Optional[str] = None
    id: typing.Optional[str] = None
    is_external: typing.Optional[bool] = None
    is_favorite: typing.Optional[bool] = None
    photo: typing.Optional["PhotosPhoto"] = None
    preview_page: typing.Optional[str] = None
    preview_url: typing.Optional[str] = None
    product: typing.Optional["BaseLinkProduct"] = None
    rating: typing.Optional["BaseLinkRating"] = None
    target_object: typing.Optional["LinkTargetObject"] = None
    title: typing.Optional[str] = None
    url: str = None
    video: typing.Optional["VideoVideo"] = None


class BaseLinkApplication(BaseModel):
    """VK Object BaseLinkApplication

    app_id - Application Id
    store -
    """

    app_id: typing.Optional[float] = None
    store: typing.Optional["BaseLinkApplicationStore"] = None


class BaseLinkApplicationStore(BaseModel):
    """VK Object BaseLinkApplicationStore

    id - Store Id
    name - Store name
    """

    id: typing.Optional[float] = None
    name: typing.Optional[str] = None


class BaseLinkButton(BaseModel):
    """VK Object BaseLinkButton

    action - Button action
    album_id - Video album id
    block_id - Target block id
    curator_id - curator id
    icon - Button icon name, e.g. 'phone' or 'gift'
    owner_id - Owner id
    section_id - Target section id
    style -
    title - Button title
    """

    action: typing.Optional["BaseLinkButtonAction"] = None
    album_id: typing.Optional[int] = None
    block_id: typing.Optional[str] = None
    curator_id: typing.Optional[int] = None
    icon: typing.Optional[str] = None
    owner_id: typing.Optional[int] = None
    section_id: typing.Optional[str] = None
    style: typing.Optional["BaseLinkButtonStyle"] = None
    title: typing.Optional[str] = None


class BaseLinkButtonAction(BaseModel):
    """VK Object BaseLinkButtonAction

    consume_reason -
    type -
    url - Action URL
    """

    consume_reason: typing.Optional[str] = None
    type: "BaseLinkButtonActionType" = None
    url: typing.Optional[str] = None


class BaseLinkButtonActionType(enum.Enum):
    """ Action type """

    OPEN_URL = "open_url"


class BaseLinkButtonStyle(enum.Enum):
    """ Button style """

    PRIMARY = "primary"
    SECONDARY = "secondary"


class BaseLinkProduct(BaseModel):
    """VK Object BaseLinkProduct"""

    merchant: typing.Optional[str] = None
    orders_count: typing.Optional[int] = None
    price: "MarketPrice" = None


class BaseLinkProductCategory(BaseModel):
    """VK Object BaseLinkProductCategory"""

    pass


class BaseLinkProductStatus(enum.Enum):
    """ Status representation """

    ACTIVE = "active"
    BLOCKED = "blocked"
    SOLD = "sold"
    DELETED = "deleted"
    ARCHIVED = "archived"


class BaseLinkRating(BaseModel):
    """VK Object BaseLinkRating

    reviews_count - Count of reviews
    stars - Count of stars
    """

    reviews_count: typing.Optional[int] = None
    stars: typing.Optional[float] = None


class BaseMessageError(BaseModel):
    """VK Object BaseMessageError

    code - Error code
    description - Error message
    """

    code: typing.Optional[int] = None
    description: typing.Optional[str] = None


class BaseObject(BaseModel):
    """VK Object BaseObject

    id - Object ID
    title - Object title
    """

    id: int = None
    title: str = None


class BaseObjectCount(BaseModel):
    """VK Object BaseObjectCount

    count - Items count
    """

    count: typing.Optional[int] = None


class BaseObjectWithName(BaseModel):
    """VK Object BaseObjectWithName

    id - Object ID
    name - Object name
    """

    id: int = None
    name: str = None


class BasePlace(BaseModel):
    """VK Object BasePlace

    address - Place address
    checkins - Checkins number
    city - City name
    country - Country name
    created - Date of the place creation in Unixtime
    icon - URL of the place's icon
    id - Place ID
    latitude - Place latitude
    longitude - Place longitude
    title - Place title
    type - Place type
    """

    address: typing.Optional[str] = None
    checkins: typing.Optional[int] = None
    city: typing.Optional[str] = None
    country: typing.Optional[str] = None
    created: typing.Optional[int] = None
    icon: typing.Optional[str] = None
    id: typing.Optional[int] = None
    latitude: typing.Optional[float] = None
    longitude: typing.Optional[float] = None
    title: typing.Optional[str] = None
    type: typing.Optional[str] = None


class BasePropertyExists(enum.IntEnum):
    """ BasePropertyExists enum """

    property_exists = 1


class BaseRepostsInfo(BaseModel):
    """VK Object BaseRepostsInfo

    count - Total reposts counter. Sum of wall and mail reposts counters
    mail_count - Mail reposts counter
    user_reposted - Information whether current user has reposted the post
    wall_count - Wall reposts counter
    """

    count: int = None
    mail_count: typing.Optional[int] = None
    user_reposted: typing.Optional[int] = None
    wall_count: typing.Optional[int] = None


class BaseRequestParam(BaseModel):
    """VK Object BaseRequestParam

    key - Parameter name
    value - Parameter value
    """

    key: typing.Optional[str] = None
    value: typing.Optional[str] = None


class BaseSex(enum.IntEnum):
    """ BaseSex enum """

    unknown = 0
    female = 1
    male = 2


class BaseStickerOld(BaseModel):
    """VK Object BaseStickerOld

    height - Height in px
    id - Sticker ID
    is_allowed - Information whether the sticker is allowed
    photo_128 - URL of the preview image with 128 px in height
    photo_256 - URL of the preview image with 256 px in height
    photo_352 - URL of the preview image with 352 px in height
    photo_512 - URL of the preview image with 512 px in height
    photo_64 - URL of the preview image with 64 px in height
    product_id - Pack ID
    width - Width in px
    """

    height: typing.Optional[int] = None
    id: typing.Optional[int] = None
    is_allowed: typing.Optional[bool] = None
    photo_128: typing.Optional[str] = None
    photo_256: typing.Optional[str] = None
    photo_352: typing.Optional[str] = None
    photo_512: typing.Optional[str] = None
    photo_64: typing.Optional[str] = None
    product_id: typing.Optional[int] = None
    width: typing.Optional[int] = None


class BaseStickerNew(BaseModel):
    """VK Object BaseStickerNew

    animation_url - URL of sticker animation script
    animations - Array of sticker animation script objects
    images -
    images_with_background -
    is_allowed - Information whether the sticker is allowed
    product_id - Pack ID
    sticker_id - Sticker ID
    """

    animation_url: typing.Optional[str] = None
    animations: typing.Optional[typing.List["BaseStickerAnimation"]] = None
    images: typing.Optional[typing.List["BaseImage"]] = None
    images_with_background: typing.Optional[typing.List["BaseImage"]] = None
    is_allowed: typing.Optional[bool] = None
    product_id: typing.Optional[int] = None
    sticker_id: typing.Optional[int] = None


class BaseSticker(BaseStickerOld, BaseStickerNew):
    """VK Object BaseSticker"""

    pass


class AnimationScriptType(enum.Enum):
    """ Type of animation script """

    LIGHT = "light"
    DARK = "dark"


class BaseStickerAnimation(BaseModel):
    """VK Object BaseStickerAnimation

    type - Type of animation script
    url - URL of animation script
    """

    type: typing.Optional["AnimationScriptType"] = None
    url: typing.Optional[str] = None


BaseStickersList = typing.List["BaseStickerNew"]


class BaseUploadServer(BaseModel):
    """VK Object BaseUploadServer

    upload_url - Upload URL
    """

    upload_url: str = None


class BaseUserGroupFields(enum.Enum):
    """ BaseUserGroupFields enum """

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


class BaseUserId(BaseModel):
    """VK Object BaseUserId

    user_id - User ID
    """

    user_id: typing.Optional[int] = None


class BoardDefaultOrder(enum.IntEnum):
    """ Sort type """

    desc_updated = 1
    desc_created = 2
    asc_updated = -1
    asc_created = -2


class BoardTopic(BaseModel):
    """VK Object BoardTopic

    comments - Comments number
    created - Date when the topic has been created in Unixtime
    created_by - Creator ID
    id - Topic ID
    is_closed - Information whether the topic is closed
    is_fixed - Information whether the topic is fixed
    title - Topic title
    updated - Date when the topic has been updated in Unixtime
    updated_by - ID of user who updated the topic
    """

    comments: typing.Optional[int] = None
    created: typing.Optional[int] = None
    created_by: typing.Optional[int] = None
    id: typing.Optional[int] = None
    is_closed: typing.Optional["BaseBoolInt"] = None
    is_fixed: typing.Optional["BaseBoolInt"] = None
    title: typing.Optional[str] = None
    updated: typing.Optional[int] = None
    updated_by: typing.Optional[int] = None


class BoardTopicComment(BaseModel):
    """VK Object BoardTopicComment

    attachments -
    can_edit - Information whether current user can edit the comment
    date - Date when the comment has been added in Unixtime
    from_id - Author ID
    id - Comment ID
    likes -
    real_offset - Real position of the comment
    text - Comment text
    """

    attachments: typing.Optional[typing.List["WallCommentAttachment"]] = None
    can_edit: typing.Optional["BaseBoolInt"] = None
    date: int = None
    from_id: int = None
    id: int = None
    likes: typing.Optional["BaseLikesInfo"] = None
    real_offset: typing.Optional[int] = None
    text: str = None


class BoardTopicPoll(BaseModel):
    """VK Object BoardTopicPoll

    answer_id - Current user's answer ID
    answers -
    created - Date when poll has been created in Unixtime
    is_closed - Information whether the poll is closed
    owner_id - Poll owner's ID
    poll_id - Poll ID
    question - Poll question
    votes - Votes number
    """

    answer_id: int = None
    answers: typing.List["PollsAnswer"] = None
    created: int = None
    is_closed: typing.Optional["BaseBoolInt"] = None
    owner_id: int = None
    poll_id: int = None
    question: str = None
    votes: int = None


class CallbackBase(BaseModel):
    """VK Object CallbackBase

    event_id - Unique event id. If it passed twice or more - you should ignore it.
    group_id -
    secret -
    type -
    """

    event_id: str = None
    group_id: int = None
    secret: typing.Optional[str] = None
    type: "CallbackType" = None


class CallbackBoardPostDelete(BaseModel):
    """VK Object CallbackBoardPostDelete"""

    id: int = None
    topic_id: int = None
    topic_owner_id: int = None


class CallbackConfirmation(CallbackBase):
    """VK Object CallbackConfirmation"""

    type: typing.Optional["CallbackType"] = None


class CallbackDonutMoneyWithdraw(BaseModel):
    """VK Object CallbackDonutMoneyWithdraw"""

    amount: float = None
    amount_without_fee: float = None


class CallbackDonutMoneyWithdrawError(BaseModel):
    """VK Object CallbackDonutMoneyWithdrawError"""

    reason: str = None


class CallbackDonutSubscriptionCancelled(BaseModel):
    """VK Object CallbackDonutSubscriptionCancelled"""

    user_id: typing.Optional[int] = None


class CallbackDonutSubscriptionCreate(BaseModel):
    """VK Object CallbackDonutSubscriptionCreate"""

    amount: int = None
    amount_without_fee: float = None
    user_id: typing.Optional[int] = None


class CallbackDonutSubscriptionExpired(BaseModel):
    """VK Object CallbackDonutSubscriptionExpired"""

    user_id: typing.Optional[int] = None


class CallbackDonutSubscriptionPriceChanged(BaseModel):
    """VK Object CallbackDonutSubscriptionPriceChanged"""

    amount_diff: typing.Optional[float] = None
    amount_diff_without_fee: typing.Optional[float] = None
    amount_new: int = None
    amount_old: int = None
    user_id: typing.Optional[int] = None


class CallbackDonutSubscriptionProlonged(BaseModel):
    """VK Object CallbackDonutSubscriptionProlonged"""

    amount: int = None
    amount_without_fee: float = None
    user_id: typing.Optional[int] = None


class CallbackGroupChangePhoto(BaseModel):
    """VK Object CallbackGroupChangePhoto"""

    photo: "PhotosPhoto" = None
    user_id: int = None


class CallbackGroupChangeSettings(BaseModel):
    """VK Object CallbackGroupChangeSettings"""

    self: "BaseBoolInt" = None
    user_id: int = None


class CallbackGroupJoin(BaseModel):
    """VK Object CallbackGroupJoin"""

    join_type: "CallbackGroupJoinType" = None
    user_id: int = None


class CallbackGroupJoinType(enum.Enum):
    """ CallbackGroupJoinType enum """

    JOIN = "join"
    UNSURE = "unsure"
    ACCEPTED = "accepted"
    APPROVED = "approved"
    REQUEST = "request"


class CallbackGroupLeave(BaseModel):
    """VK Object CallbackGroupLeave"""

    self: typing.Optional["BaseBoolInt"] = None
    user_id: typing.Optional[int] = None


class CallbackGroupMarket(enum.IntEnum):
    """ CallbackGroupMarket enum """

    disabled = 0
    open = 1


class CallbackGroupOfficerRole(enum.IntEnum):
    """ CallbackGroupOfficerRole enum """

    none = 0
    moderator = 1
    editor = 2
    administrator = 3


class CallbackGroupOfficersEdit(BaseModel):
    """VK Object CallbackGroupOfficersEdit"""

    admin_id: int = None
    level_new: "CallbackGroupOfficerRole" = None
    level_old: "CallbackGroupOfficerRole" = None
    user_id: int = None


class CallbackGroupSettingsChanges(BaseModel):
    """VK Object CallbackGroupSettingsChanges"""

    access: typing.Optional["GroupsGroupIsClosed"] = None
    age_limits: typing.Optional["GroupsGroupFullAgeLimits"] = None
    description: typing.Optional[str] = None
    enable_audio: typing.Optional["GroupsGroupAudio"] = None
    enable_market: typing.Optional["CallbackGroupMarket"] = None
    enable_photo: typing.Optional["GroupsGroupPhotos"] = None
    enable_status_default: typing.Optional["GroupsGroupWall"] = None
    enable_video: typing.Optional["GroupsGroupVideo"] = None
    public_category: typing.Optional[int] = None
    public_subcategory: typing.Optional[int] = None
    screen_name: typing.Optional[str] = None
    title: typing.Optional[str] = None
    website: typing.Optional[str] = None


class CallbackLikeAddRemoveObjectType(enum.Enum):
    """ CallbackLikeAddRemoveObjectType enum """

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
    """VK Object CallbackLikeAddRemove"""

    liker_id: int = None
    object_id: int = None
    object_owner_id: int = None
    object_type: "CallbackLikeAddRemoveObjectType" = None
    post_id: int = None
    thread_reply_id: typing.Optional[int] = None


class CallbackMarketComment(BaseModel):
    """VK Object CallbackMarketComment"""

    date: int = None
    from_id: int = None
    id: int = None
    market_owner_id: typing.Optional[int] = None
    photo_id: typing.Optional[int] = None
    text: typing.Optional[str] = None


class CallbackMarketCommentDelete(BaseModel):
    """VK Object CallbackMarketCommentDelete"""

    id: int = None
    item_id: int = None
    owner_id: int = None
    user_id: int = None


class CallbackMessageAllow(CallbackBase):
    """VK Object CallbackMessageAllow"""

    object: typing.Optional["CallbackMessageAllowObject"] = None
    type: typing.Optional["CallbackType"] = None


class CallbackMessageAllowObject(BaseModel):
    """VK Object CallbackMessageAllowObject"""

    key: str = None
    user_id: int = None


class CallbackMessageDeny(BaseModel):
    """VK Object CallbackMessageDeny"""

    user_id: int = None


class CallbackMessageEdit(CallbackBase):
    """VK Object CallbackMessageEdit"""

    object: typing.Optional["MessagesMessage"] = None
    type: typing.Optional["CallbackType"] = None


class CallbackMessageNew(CallbackBase):
    """VK Object CallbackMessageNew"""

    object: typing.Optional["CallbackMessageObject"] = None
    type: typing.Optional["CallbackType"] = None


class CallbackMessageObject(BaseModel):
    """VK Object CallbackMessageObject"""

    client_info: typing.Optional["ClientInfoForBots"] = None
    message: typing.Optional["MessagesMessage"] = None


class CallbackMessageReply(CallbackBase):
    """VK Object CallbackMessageReply"""

    object: typing.Optional["MessagesMessage"] = None
    type: typing.Optional["CallbackType"] = None


class CallbackPhotoComment(BaseModel):
    """VK Object CallbackPhotoComment"""

    date: int = None
    from_id: int = None
    id: int = None
    photo_owner_id: int = None
    text: str = None


class CallbackPhotoCommentDelete(BaseModel):
    """VK Object CallbackPhotoCommentDelete"""

    id: int = None
    owner_id: int = None
    photo_id: int = None
    user_id: int = None


class CallbackPollVoteNew(BaseModel):
    """VK Object CallbackPollVoteNew"""

    option_id: int = None
    owner_id: int = None
    poll_id: int = None
    user_id: int = None


class CallbackQrScan(BaseModel):
    """VK Object CallbackQrScan"""

    data: str = None
    reread: bool = None
    subtype: str = None
    type: str = None
    user_id: int = None


class CallbackType(enum.Enum):
    """ CallbackType enum """

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
    MESSAGE_NEW = "message_new"
    MESSAGE_REPLY = "message_reply"
    MESSAGE_EDIT = "message_edit"
    MESSAGE_ALLOW = "message_allow"
    MESSAGE_DENY = "message_deny"
    MESSAGE_READ = "message_read"
    MESSAGE_TYPING_STATE = "message_typing_state"
    MESSAGES_EDIT = "messages_edit"
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
    """VK Object CallbackUserBlock"""

    admin_id: int = None
    comment: typing.Optional[str] = None
    reason: int = None
    unblock_date: int = None
    user_id: int = None


class CallbackUserUnblock(BaseModel):
    """VK Object CallbackUserUnblock"""

    admin_id: int = None
    by_end_date: int = None
    user_id: int = None


class CallbackVideoComment(BaseModel):
    """VK Object CallbackVideoComment"""

    date: int = None
    from_id: int = None
    id: int = None
    text: str = None
    video_owner_id: int = None


class CallbackVideoCommentDelete(BaseModel):
    """VK Object CallbackVideoCommentDelete"""

    id: int = None
    owner_id: int = None
    user_id: int = None
    video_id: int = None


class CallbackWallCommentDelete(BaseModel):
    """VK Object CallbackWallCommentDelete"""

    id: int = None
    owner_id: int = None
    post_id: int = None
    user_id: int = None


class CallsCall(BaseModel):
    """VK Object CallsCall

    duration - Call duration
    initiator_id - Caller initiator
    participants -
    receiver_id - Caller receiver
    state -
    time - Timestamp for call
    video - Was this call initiated as video call
    """

    duration: typing.Optional[int] = None
    initiator_id: int = None
    participants: typing.Optional["CallsParticipants"] = None
    receiver_id: int = None
    state: "CallsEndState" = None
    time: int = None
    video: typing.Optional[bool] = None


class CallsEndState(enum.Enum):
    """ State in which call ended up """

    CANCELED_BY_INITIATOR = "canceled_by_initiator"
    CANCELED_BY_RECEIVER = "canceled_by_receiver"
    REACHED = "reached"


class CallsParticipants(BaseModel):
    """VK Object CallsParticipants

    count - Participants count
    list -
    """

    count: typing.Optional[int] = None
    list: typing.Optional[typing.List[int]] = None


class ClientInfoForBots(BaseModel):
    """VK Object ClientInfoForBots

    button_actions -
    carousel - client has support carousel
    inline_keyboard - client has support inline keyboard
    keyboard - client has support keyboard
    lang_id - client or user language id
    """

    button_actions: typing.Optional[typing.List["MessagesTemplateActionTypeNames"]] = None
    carousel: typing.Optional[bool] = None
    inline_keyboard: typing.Optional[bool] = None
    keyboard: typing.Optional[bool] = None
    lang_id: typing.Optional[int] = None


class CommentThread(BaseModel):
    """VK Object CommentThread

    can_post - Information whether current user can comment the post
    count - Comments number
    groups_can_post - Information whether groups can comment the post
    items -
    show_reply_button - Information whether recommended to display reply button
    """

    can_post: typing.Optional[bool] = None
    count: int = None
    groups_can_post: typing.Optional[bool] = None
    items: typing.Optional[typing.List["WallWallComment"]] = None
    show_reply_button: typing.Optional[bool] = None


class DatabaseCity(BaseObject):
    """VK Object DatabaseCity

    area - Area title
    important - Information whether the city is included in important cities list
    region - Region title
    """

    area: typing.Optional[str] = None
    important: typing.Optional["BaseBoolInt"] = None
    region: typing.Optional[str] = None


class DatabaseFaculty(BaseModel):
    """VK Object DatabaseFaculty

    id - Faculty ID
    title - Faculty title
    """

    id: typing.Optional[int] = None
    title: typing.Optional[str] = None


class DatabaseRegion(BaseModel):
    """VK Object DatabaseRegion

    id - Region ID
    title - Region title
    """

    id: typing.Optional[int] = None
    title: typing.Optional[str] = None


class DatabaseSchool(BaseModel):
    """VK Object DatabaseSchool

    id - School ID
    title - School title
    """

    id: typing.Optional[int] = None
    title: typing.Optional[str] = None


class DatabaseStation(BaseModel):
    """VK Object DatabaseStation

    city_id - City ID
    color - Hex color code without #
    id - Station ID
    name - Station name
    """

    city_id: typing.Optional[int] = None
    color: typing.Optional[str] = None
    id: int = None
    name: str = None


class DatabaseUniversity(BaseModel):
    """VK Object DatabaseUniversity

    id - University ID
    title - University title
    """

    id: typing.Optional[int] = None
    title: typing.Optional[str] = None


class DocsDoc(BaseModel):
    """VK Object DocsDoc

    access_key - Access key for the document
    date - Date when file has been uploaded in Unixtime
    ext - File extension
    id - Document ID
    is_licensed -
    owner_id - Document owner ID
    preview -
    size - File size in bites
    tags - Document tags
    title - Document title
    type - Document type
    url - File URL
    """

    access_key: typing.Optional[str] = None
    date: int = None
    ext: str = None
    id: int = None
    is_licensed: typing.Optional["BaseBoolInt"] = None
    owner_id: int = None
    preview: typing.Optional["DocsDocPreview"] = None
    size: int = None
    tags: typing.Optional[typing.List[str]] = None
    title: str = None
    type: int = None
    url: typing.Optional[str] = None


class DocsDocAttachmentType(enum.Enum):
    """ Doc attachment type """

    DOC = "doc"
    GRAFFITI = "graffiti"
    AUDIO_MESSAGE = "audio_message"


class DocsDocPreview(BaseModel):
    """VK Object DocsDocPreview"""

    audio_msg: typing.Optional["DocsDocPreviewAudioMsg"] = None
    graffiti: typing.Optional["DocsDocPreviewGraffiti"] = None
    photo: typing.Optional["DocsDocPreviewPhoto"] = None
    video: typing.Optional["DocsDocPreviewVideo"] = None


class DocsDocPreviewAudioMsg(BaseModel):
    """VK Object DocsDocPreviewAudioMsg

    duration - Audio message duration in seconds
    link_mp3 - MP3 file URL
    link_ogg - OGG file URL
    waveform -
    """

    duration: int = None
    link_mp3: str = None
    link_ogg: str = None
    waveform: typing.List[int] = None


class DocsDocPreviewGraffiti(BaseModel):
    """VK Object DocsDocPreviewGraffiti

    height - Graffiti height
    src - Graffiti file URL
    width - Graffiti width
    """

    height: int = None
    src: str = None
    width: int = None


class DocsDocPreviewPhoto(BaseModel):
    """VK Object DocsDocPreviewPhoto"""

    sizes: typing.Optional[typing.List["DocsDocPreviewPhotoSizes"]] = None


class DocsDocPreviewPhotoSizes(BaseModel):
    """VK Object DocsDocPreviewPhotoSizes

    height - Height in px
    src - URL of the image
    type -
    width - Width in px
    """

    height: int = None
    src: str = None
    type: "PhotosPhotoSizesType" = None
    width: int = None


class DocsDocPreviewVideo(BaseModel):
    """VK Object DocsDocPreviewVideo

    file_size - Video file size in bites
    height - Video's height in pixels
    src - Video URL
    width - Video's width in pixels
    """

    file_size: int = None
    height: int = None
    src: str = None
    width: int = None


class DocsDocTypes(BaseModel):
    """VK Object DocsDocTypes

    count - Number of docs
    id - Doc type ID
    name - Doc type title
    """

    count: int = None
    id: int = None
    name: str = None


class DonutDonatorSubscriptionInfoStatus(enum.Enum):
    """ DonutDonatorSubscriptionInfoStatus enum """

    ACTIVE = "active"
    EXPIRING = "expiring"


class DonutDonatorSubscriptionInfo(BaseModel):
    """VK Object DonutDonatorSubscriptionInfo"""

    amount: int = None
    next_payment_date: int = None
    owner_id: int = None
    status: "DonutDonatorSubscriptionInfoStatus" = None


class EventsEventAttach(BaseModel):
    """VK Object EventsEventAttach

    address - address of event
    button_text - text of attach
    friends - array of friends ids
    id - event ID
    is_favorite - is favorite
    member_status - Current user's member status
    text - text of attach
    time - event start time
    """

    address: typing.Optional[str] = None
    button_text: str = None
    friends: typing.List[int] = None
    id: int = None
    is_favorite: bool = None
    member_status: typing.Optional["GroupsGroupFullMemberStatus"] = None
    text: str = None
    time: typing.Optional[int] = None


class FaveBookmark(BaseModel):
    """VK Object FaveBookmark

    added_date - Timestamp, when this item was bookmarked
    link -
    post -
    product -
    seen - Has user seen this item
    tags -
    type - Item type
    video -
    """

    added_date: int = None
    link: typing.Optional["BaseLink"] = None
    post: typing.Optional["WallWallpostFull"] = None
    product: typing.Optional["MarketMarketItem"] = None
    seen: bool = None
    tags: typing.List["FaveTag"] = None
    type: "FaveBookmarkType" = None
    video: typing.Optional["VideoVideo"] = None


class FaveBookmarkType(enum.Enum):
    """ FaveBookmarkType enum """

    POST = "post"
    VIDEO = "video"
    PRODUCT = "product"
    ARTICLE = "article"
    LINK = "link"


class FavePage(BaseModel):
    """VK Object FavePage

    description - Some info about user or group
    group -
    tags -
    type - Item type
    updated_date - Timestamp, when this page was bookmarked
    user -
    """

    description: str = None
    group: typing.Optional["GroupsGroupFull"] = None
    tags: typing.List["FaveTag"] = None
    type: "FavePageType" = None
    updated_date: typing.Optional[int] = None
    user: typing.Optional["UsersUserFull"] = None


class FavePageType(enum.Enum):
    """ FavePageType enum """

    USER = "user"
    GROUP = "group"
    HINTS = "hints"


class FaveTag(BaseModel):
    """VK Object FaveTag

    id - Tag id
    name - Tag name
    """

    id: typing.Optional[int] = None
    name: typing.Optional[str] = None


class FriendsFriendStatus(BaseModel):
    """VK Object FriendsFriendStatus

    friend_status -
    sign - MD5 hash for the result validation
    user_id - User ID
    """

    friend_status: "FriendsFriendStatusStatus" = None
    sign: typing.Optional[str] = None
    user_id: int = None


class FriendsFriendExtendedStatus(FriendsFriendStatus):
    """VK Object FriendsFriendExtendedStatus

    is_request_unread - Is friend request from other user unread
    """

    is_request_unread: typing.Optional[bool] = None


class FriendsFriendStatusStatus(enum.IntEnum):
    """ Friend status with the user """

    not_a_friend = 0
    outcoming_request = 1
    incoming_request = 2
    is_friend = 3


class FriendsFriendsList(BaseModel):
    """VK Object FriendsFriendsList

    id - List ID
    name - List title
    """

    id: int = None
    name: str = None


class FriendsMutualFriend(BaseModel):
    """VK Object FriendsMutualFriend

    common_count - Total mutual friends number
    common_friends -
    id - User ID
    """

    common_count: typing.Optional[int] = None
    common_friends: typing.Optional[typing.List[int]] = None
    id: typing.Optional[int] = None


class FriendsRequests(BaseModel):
    """VK Object FriendsRequests

    _from - ID of the user by whom friend has been suggested
    mutual -
    user_id - User ID
    """

    _from: typing.Optional[str] = None
    mutual: typing.Optional["FriendsRequestsMutual"] = None
    user_id: typing.Optional[int] = None


class FriendsRequestsMutual(BaseModel):
    """VK Object FriendsRequestsMutual

    count - Total mutual friends number
    users -
    """

    count: typing.Optional[int] = None
    users: typing.Optional[typing.List[int]] = None


class FriendsRequestsXtrMessage(BaseModel):
    """VK Object FriendsRequestsXtrMessage

    _from - ID of the user by whom friend has been suggested
    message - Message sent with a request
    mutual -
    user_id - User ID
    """

    _from: typing.Optional[str] = None
    message: typing.Optional[str] = None
    mutual: typing.Optional["FriendsRequestsMutual"] = None
    user_id: typing.Optional[int] = None


class UsersUser(UsersUserMin):
    """VK Object UsersUser

    friend_status -
    mutual -
    online - Information whether the user is online
    online_app - Application ID
    online_info -
    online_mobile - Information whether the user is online in mobile site or application
    photo_100 - URL of square photo of the user with 100 pixels in width
    photo_50 - URL of square photo of the user with 50 pixels in width
    screen_name - Domain name of the user's page
    sex - User sex
    trending - Information whether the user has a "fire" pictogram.
    verified - Information whether the user is verified
    """

    friend_status: typing.Optional["FriendsFriendStatusStatus"] = None
    mutual: typing.Optional["FriendsRequestsMutual"] = None
    online: typing.Optional["BaseBoolInt"] = None
    online_app: typing.Optional[int] = None
    online_info: typing.Optional["UsersOnlineInfo"] = None
    online_mobile: typing.Optional["BaseBoolInt"] = None
    photo_100: typing.Optional[str] = None
    photo_50: typing.Optional[str] = None
    screen_name: typing.Optional[str] = None
    sex: typing.Optional["BaseSex"] = None
    trending: typing.Optional["BaseBoolInt"] = None
    verified: typing.Optional["BaseBoolInt"] = None


class UsersUserFull(UsersUser):
    """VK Object UsersUserFull

    about -
    access_key -
    activities -
    activity - User's status
    bdate - User's date of birth
    blacklisted - Information whether current user is in the requested user's blacklist.
    blacklisted_by_me - Information whether the requested user is in current user's blacklist
    books -
    can_be_invited_group - Information whether current user can be invited to the community
    can_call - Information whether current user can call
    can_call_from_group - Information whether group can call user
    can_post - Information whether current user can post on the user's wall
    can_see_all_posts - Information whether current user can see other users' audio on the wall
    can_see_audio - Information whether current user can see the user's audio
    can_see_gifts - Information whether current user can see the user's gifts
    can_see_wishes - Information whether current user can see the user's wishes
    can_send_friend_request - Information whether current user can send a friend request
    can_subscribe_podcasts - Owner in whitelist or not
    can_subscribe_posts - Can subscribe to wall
    can_upload_doc -
    can_write_private_message - Information whether current user can write private message
    career -
    city -
    clips_count - Number of user's clips
    common_count - Number of common friends with current user
    contact_id - Contact person ID
    contact_name - User contact name
    counters -
    country -
    crop_photo -
    descriptions -
    domain - Domain name of the user's page
    education_form - Education form
    education_status - User's education status
    email -
    exports -
    facebook -
    facebook_name -
    faculty - Faculty ID
    faculty_name - Faculty name
    first_name_abl - User's first name in prepositional case
    first_name_acc - User's first name in accusative case
    first_name_dat - User's first name in dative case
    first_name_gen - User's first name in genitive case
    first_name_ins - User's first name in instrumental case
    first_name_nom - User's first name in nominative case
    followers_count - Number of user's followers
    games -
    graduation - Graduation year
    has_mobile - Information whether the user specified his phone number
    has_photo - Information whether the user has main photo
    has_unseen_stories -
    hash -
    home_phone - User's additional phone number
    home_town - User hometown
    instagram -
    interests -
    is_favorite - Information whether the requested user is in faves of current user
    is_friend - Information whether the user is a friend of current user
    is_hidden_from_feed - Information whether the requested user is hidden from current user's newsfeed
    is_message_request -
    is_no_index - Access to user profile is restricted for search engines
    is_service -
    is_subscribed_podcasts - Information whether current user is subscribed to podcasts
    is_video_live_notifications_blocked -
    language -
    last_name_abl - User's last name in prepositional case
    last_name_acc - User's last name in accusative case
    last_name_dat - User's last name in dative case
    last_name_gen - User's last name in genitive case
    last_name_ins - User's last name in instrumental case
    last_name_nom - User's last name in nominative case
    last_seen -
    lists -
    livejournal -
    maiden_name - User maiden name
    military -
    mobile_phone - User's mobile phone number
    movies -
    music -
    nickname - User nickname
    occupation -
    owner_state -
    personal -
    photo -
    photo_200 - URL of square photo of the user with 200 pixels in width
    photo_200_orig - URL of user's photo with 200 pixels in width
    photo_400 -
    photo_400_orig - URL of user's photo with 400 pixels in width
    photo_big -
    photo_id - ID of the user's main photo
    photo_max - URL of square photo of the user with maximum width
    photo_max_orig - URL of user's photo of maximum size
    photo_max_size -
    photo_medium -
    photo_medium_rec -
    photo_rec -
    quotes -
    relation - User relationship status
    relation_partner -
    relatives -
    schools -
    service_description -
    site - User's website
    skype -
    status - User's status
    status_audio -
    stories_archive_count -
    test -
    timezone - User's timezone
    tv -
    twitter -
    type -
    universities -
    university - University ID
    university_group_id -
    university_name - University name
    video_live -
    video_live_count - Number of user's live streams
    video_live_level - User level in live streams achievements
    wall_comments - Information whether current user can comment wall posts
    wall_default -
    """

    about: typing.Optional[str] = None
    access_key: typing.Optional[str] = None
    activities: typing.Optional[str] = None
    activity: typing.Optional[str] = None
    bdate: typing.Optional[str] = None
    blacklisted: typing.Optional["BaseBoolInt"] = None
    blacklisted_by_me: typing.Optional["BaseBoolInt"] = None
    books: typing.Optional[str] = None
    can_be_invited_group: typing.Optional[bool] = None
    can_call: typing.Optional[bool] = None
    can_call_from_group: typing.Optional[bool] = None
    can_post: typing.Optional["BaseBoolInt"] = None
    can_see_all_posts: typing.Optional["BaseBoolInt"] = None
    can_see_audio: typing.Optional["BaseBoolInt"] = None
    can_see_gifts: typing.Optional["BaseBoolInt"] = None
    can_see_wishes: typing.Optional[bool] = None
    can_send_friend_request: typing.Optional["BaseBoolInt"] = None
    can_subscribe_podcasts: typing.Optional[bool] = None
    can_subscribe_posts: typing.Optional[bool] = None
    can_upload_doc: typing.Optional["BaseBoolInt"] = None
    can_write_private_message: typing.Optional["BaseBoolInt"] = None
    career: typing.Optional[typing.List["UsersCareer"]] = None
    city: typing.Optional["BaseCity"] = None
    clips_count: typing.Optional[int] = None
    common_count: typing.Optional[int] = None
    contact_id: typing.Optional[int] = None
    contact_name: typing.Optional[str] = None
    counters: typing.Optional["UsersUserCounters"] = None
    country: typing.Optional["BaseCountry"] = None
    crop_photo: typing.Optional["BaseCropPhoto"] = None
    descriptions: typing.Optional[typing.List[str]] = None
    domain: typing.Optional[str] = None
    education_form: typing.Optional[str] = None
    education_status: typing.Optional[str] = None
    email: typing.Optional[str] = None
    exports: typing.Optional["UsersExports"] = None
    facebook: typing.Optional[str] = None
    facebook_name: typing.Optional[str] = None
    faculty: typing.Optional[int] = None
    faculty_name: typing.Optional[str] = None
    first_name_abl: typing.Optional[str] = None
    first_name_acc: typing.Optional[str] = None
    first_name_dat: typing.Optional[str] = None
    first_name_gen: typing.Optional[str] = None
    first_name_ins: typing.Optional[str] = None
    first_name_nom: typing.Optional[str] = None
    followers_count: typing.Optional[int] = None
    games: typing.Optional[str] = None
    graduation: typing.Optional[int] = None
    has_mobile: typing.Optional["BaseBoolInt"] = None
    has_photo: typing.Optional["BaseBoolInt"] = None
    has_unseen_stories: typing.Optional[bool] = None
    hash: typing.Optional[str] = None
    home_phone: typing.Optional[str] = None
    home_town: typing.Optional[str] = None
    instagram: typing.Optional[str] = None
    interests: typing.Optional[str] = None
    is_favorite: typing.Optional["BaseBoolInt"] = None
    is_friend: typing.Optional["BaseBoolInt"] = None
    is_hidden_from_feed: typing.Optional["BaseBoolInt"] = None
    is_message_request: typing.Optional[bool] = None
    is_no_index: typing.Optional[bool] = None
    is_service: typing.Optional[bool] = None
    is_subscribed_podcasts: typing.Optional[bool] = None
    is_video_live_notifications_blocked: typing.Optional["BaseBoolInt"] = None
    language: typing.Optional[str] = None
    last_name_abl: typing.Optional[str] = None
    last_name_acc: typing.Optional[str] = None
    last_name_dat: typing.Optional[str] = None
    last_name_gen: typing.Optional[str] = None
    last_name_ins: typing.Optional[str] = None
    last_name_nom: typing.Optional[str] = None
    last_seen: typing.Optional["UsersLastSeen"] = None
    lists: typing.Optional[typing.List[int]] = None
    livejournal: typing.Optional[str] = None
    maiden_name: typing.Optional[str] = None
    military: typing.Optional[typing.List["UsersMilitary"]] = None
    mobile_phone: typing.Optional[str] = None
    movies: typing.Optional[str] = None
    music: typing.Optional[str] = None
    nickname: typing.Optional[str] = None
    occupation: typing.Optional["UsersOccupation"] = None
    owner_state: typing.Optional["OwnerState"] = None
    personal: typing.Optional["UsersPersonal"] = None
    photo: typing.Optional[str] = None
    photo_200: typing.Optional[str] = None
    photo_200_orig: typing.Optional[str] = None
    photo_400: typing.Optional[str] = None
    photo_400_orig: typing.Optional[str] = None
    photo_big: typing.Optional[str] = None
    photo_id: typing.Optional[str] = None
    photo_max: typing.Optional[str] = None
    photo_max_orig: typing.Optional[str] = None
    photo_max_size: typing.Optional["PhotosPhoto"] = None
    photo_medium: typing.Optional["PhotosPhotoFalseable"] = None
    photo_medium_rec: typing.Optional["PhotosPhotoFalseable"] = None
    photo_rec: typing.Optional["PhotosPhotoFalseable"] = None
    quotes: typing.Optional[str] = None
    relation: typing.Optional["UsersUserRelation"] = None
    relation_partner: typing.Optional["UsersUserMin"] = None
    relatives: typing.Optional[typing.List["UsersRelative"]] = None
    schools: typing.Optional[typing.List["UsersSchool"]] = None
    service_description: typing.Optional[str] = None
    site: typing.Optional[str] = None
    skype: typing.Optional[str] = None
    status: typing.Optional[str] = None
    status_audio: typing.Optional["AudioAudio"] = None
    stories_archive_count: typing.Optional[int] = None
    test: typing.Optional["BaseBoolInt"] = None
    timezone: typing.Optional[float] = None
    tv: typing.Optional[str] = None
    twitter: typing.Optional[str] = None
    type: typing.Optional["UsersUserType"] = None
    universities: typing.Optional[typing.List["UsersUniversity"]] = None
    university: typing.Optional[int] = None
    university_group_id: typing.Optional[int] = None
    university_name: typing.Optional[str] = None
    video_live: typing.Optional["VideoLiveInfo"] = None
    video_live_count: typing.Optional[int] = None
    video_live_level: typing.Optional[int] = None
    wall_comments: typing.Optional["BaseBoolInt"] = None
    wall_default: typing.Optional[str] = None


class FriendsUserXtrPhone(UsersUserFull):
    """VK Object FriendsUserXtrPhone

    phone - User phone
    """

    phone: typing.Optional[str] = None


class GiftsGift(BaseModel):
    """VK Object GiftsGift

    date - Date when gist has been sent in Unixtime
    from_id - Gift sender ID
    gift -
    gift_hash - Hash
    id - Gift ID
    message - Comment text
    privacy -
    """

    date: typing.Optional[int] = None
    from_id: typing.Optional[int] = None
    gift: typing.Optional["GiftsLayout"] = None
    gift_hash: typing.Optional[str] = None
    id: typing.Optional[int] = None
    message: typing.Optional[str] = None
    privacy: typing.Optional["GiftsGiftPrivacy"] = None


class GiftsGiftPrivacy(enum.IntEnum):
    """ Gift privacy """

    name_and_message_for_all = 0
    name_for_all = 1
    name_and_message_for_recipient_only = 2


class GiftsLayout(BaseModel):
    """VK Object GiftsLayout

    build_id - ID of the build of constructor gift
    id - Gift ID
    is_stickers_style - Information whether gift represents a stickers style
    keywords - Keywords used for search
    stickers_product_id - ID of the sticker pack, if the gift is representing one
    thumb_256 - URL of the preview image with 256 px in width
    thumb_48 - URL of the preview image with 48 px in width
    thumb_512 - URL of the preview image with 512 px in width
    thumb_96 - URL of the preview image with 96 px in width
    """

    build_id: typing.Optional[str] = None
    id: typing.Optional[int] = None
    is_stickers_style: typing.Optional[bool] = None
    keywords: typing.Optional[str] = None
    stickers_product_id: typing.Optional[int] = None
    thumb_256: typing.Optional[str] = None
    thumb_48: typing.Optional[str] = None
    thumb_512: typing.Optional[str] = None
    thumb_96: typing.Optional[str] = None


class GroupCallInProgress(CallsCall):
    """VK Object GroupCallInProgress"""

    join_link: typing.Optional[str] = None


class GroupsAddress(BaseModel):
    """VK Object GroupsAddress

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
    place_id -
    time_offset - Time offset int minutes from utc time
    timetable - Week timetable for the address
    title - Title of the place (Zinger, etc)
    work_info_status - Status of information about timetable
    """

    additional_address: typing.Optional[str] = None
    address: typing.Optional[str] = None
    city_id: typing.Optional[int] = None
    country_id: typing.Optional[int] = None
    distance: typing.Optional[int] = None
    id: int = None
    latitude: typing.Optional[float] = None
    longitude: typing.Optional[float] = None
    metro_station_id: typing.Optional[int] = None
    phone: typing.Optional[str] = None
    place_id: typing.Optional[int] = None
    time_offset: typing.Optional[int] = None
    timetable: typing.Optional["GroupsAddressTimetable"] = None
    title: typing.Optional[str] = None
    work_info_status: typing.Optional["GroupsAddressWorkInfoStatus"] = None


class GroupsAddressTimetable(BaseModel):
    """VK Object GroupsAddressTimetable

    fri - Timetable for friday
    mon - Timetable for monday
    sat - Timetable for saturday
    sun - Timetable for sunday
    thu - Timetable for thursday
    tue - Timetable for tuesday
    wed - Timetable for wednesday
    """

    fri: typing.Optional["GroupsAddressTimetableDay"] = None
    mon: typing.Optional["GroupsAddressTimetableDay"] = None
    sat: typing.Optional["GroupsAddressTimetableDay"] = None
    sun: typing.Optional["GroupsAddressTimetableDay"] = None
    thu: typing.Optional["GroupsAddressTimetableDay"] = None
    tue: typing.Optional["GroupsAddressTimetableDay"] = None
    wed: typing.Optional["GroupsAddressTimetableDay"] = None


class GroupsAddressTimetableDay(BaseModel):
    """VK Object GroupsAddressTimetableDay

    break_close_time - Close time of the break in minutes
    break_open_time - Start time of the break in minutes
    close_time - Close time in minutes
    open_time - Open time in minutes
    """

    break_close_time: typing.Optional[int] = None
    break_open_time: typing.Optional[int] = None
    close_time: int = None
    open_time: int = None


class GroupsAddressWorkInfoStatus(enum.Enum):
    """ Status of information about timetable """

    NO_INFORMATION = "no_information"
    TEMPORARILY_CLOSED = "temporarily_closed"
    ALWAYS_OPENED = "always_opened"
    TIMETABLE = "timetable"
    FOREVER_CLOSED = "forever_closed"


class GroupsAddressesInfo(BaseModel):
    """VK Object GroupsAddressesInfo

    is_enabled - Information whether addresses is enabled
    main_address_id - Main address id for group
    """

    is_enabled: bool = None
    main_address_id: typing.Optional[int] = None


class GroupsBanInfo(BaseModel):
    """VK Object GroupsBanInfo

    admin_id - Administrator ID
    comment - Comment for a ban
    comment_visible - Show comment for user
    date - Date when user has been added to blacklist in Unixtime
    end_date - Date when user will be removed from blacklist in Unixtime
    is_closed -
    reason -
    """

    admin_id: typing.Optional[int] = None
    comment: typing.Optional[str] = None
    comment_visible: typing.Optional[bool] = None
    date: typing.Optional[int] = None
    end_date: typing.Optional[int] = None
    is_closed: typing.Optional[bool] = None
    reason: typing.Optional["GroupsBanInfoReason"] = None


class GroupsBanInfoReason(enum.IntEnum):
    """ Ban reason """

    other = 0
    spam = 1
    verbal_abuse = 2
    strong_language = 3
    flood = 4


class GroupsOwnerXtrBanInfo(BaseModel):
    """VK Object GroupsOwnerXtrBanInfo

    ban_info -
    group - Information about group if type = group
    profile - Information about group if type = profile
    type -
    """

    ban_info: typing.Optional["GroupsBanInfo"] = None
    group: typing.Optional["GroupsGroup"] = None
    profile: typing.Optional["UsersUser"] = None
    type: typing.Optional["GroupsOwnerXtrBanInfoType"] = None


class GroupsBannedItem(GroupsOwnerXtrBanInfo):
    """VK Object GroupsBannedItem"""

    pass


class GroupsCallbackServerStatus(enum.Enum):
    """ GroupsCallbackServerStatus enum """

    UNCONFIGURED = "unconfigured"
    FAILED = "failed"
    WAIT = "wait"
    OK = "ok"


class GroupsCallbackServer(BaseModel):
    """VK Object GroupsCallbackServer"""

    creator_id: int = None
    id: int = None
    secret_key: str = None
    status: "GroupsCallbackServerStatus" = None
    title: str = None
    url: str = None


class GroupsCallbackSettings(BaseModel):
    """VK Object GroupsCallbackSettings

    api_version - API version used for the events
    events -
    """

    api_version: typing.Optional[str] = None
    events: typing.Optional["GroupsLongPollEvents"] = None


class GroupsContactsItem(BaseModel):
    """VK Object GroupsContactsItem

    desc - Contact description
    email - Contact email
    phone - Contact phone
    user_id - User ID
    """

    desc: typing.Optional[str] = None
    email: typing.Optional[str] = None
    phone: typing.Optional[str] = None
    user_id: typing.Optional[int] = None


class GroupsCountersGroup(BaseModel):
    """VK Object GroupsCountersGroup

    addresses - Addresses number
    albums - Photo albums number
    articles - Articles number
    audio_playlists - Audio playlists number
    audios - Audios number
    clips - Clips number
    clips_followers - Clips followers number
    docs - Docs number
    market - Market items number
    market_services - Market services number
    narratives - Narratives number
    photos - Photos number
    podcasts - Podcasts number
    topics - Topics number
    videos - Videos number
    """

    addresses: typing.Optional[int] = None
    albums: typing.Optional[int] = None
    articles: typing.Optional[int] = None
    audio_playlists: typing.Optional[int] = None
    audios: typing.Optional[int] = None
    clips: typing.Optional[int] = None
    clips_followers: typing.Optional[int] = None
    docs: typing.Optional[int] = None
    market: typing.Optional[int] = None
    market_services: typing.Optional[int] = None
    narratives: typing.Optional[int] = None
    photos: typing.Optional[int] = None
    podcasts: typing.Optional[int] = None
    topics: typing.Optional[int] = None
    videos: typing.Optional[int] = None


class GroupsCover(BaseModel):
    """VK Object GroupsCover

    enabled - Information whether cover is enabled
    images -
    """

    enabled: "BaseBoolInt" = None
    images: typing.Optional[typing.List["BaseImage"]] = None


class GroupsFields(enum.Enum):
    """ GroupsFields enum """

    MARKET = "market"
    MEMBER_STATUS = "member_status"
    IS_FAVORITE = "is_favorite"
    IS_SUBSCRIBED = "is_subscribed"
    IS_SUBSCRIBED_PODCASTS = "is_subscribed_podcasts"
    CAN_SUBSCRIBE_PODCASTS = "can_subscribe_podcasts"
    CITY = "city"
    COUNTRY = "country"
    VERIFIED = "verified"
    DESCRIPTION = "description"
    WIKI_PAGE = "wiki_page"
    MEMBERS_COUNT = "members_count"
    REQUESTS_COUNT = "requests_count"
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
    CROP_PHOTO = "crop_photo"
    ACTIVITY = "activity"
    FIXED_POST = "fixed_post"
    HAS_PHOTO = "has_photo"
    STATUS = "status"
    MAIN_ALBUM_ID = "main_album_id"
    LINKS = "links"
    CONTACTS = "contacts"
    SITE = "site"
    MAIN_SECTION = "main_section"
    SECONDARY_SECTION = "secondary_section"
    WALL = "wall"
    TRENDING = "trending"
    CAN_MESSAGE = "can_message"
    IS_MARKET_CART_ENABLED = "is_market_cart_enabled"
    IS_MESSAGES_BLOCKED = "is_messages_blocked"
    CAN_SEND_NOTIFY = "can_send_notify"
    HAS_GROUP_CHANNEL = "has_group_channel"
    GROUP_CHANNEL = "group_channel"
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
    IS_HIDDEN_FROM_FEED = "is_hidden_from_feed"
    CAN_SUBSCRIBE_POSTS = "can_subscribe_posts"
    WARNING_NOTIFICATION = "warning_notification"
    MSG_PUSH_ALLOWED = "msg_push_allowed"
    STORIES_ARCHIVE_COUNT = "stories_archive_count"
    VIDEO_LIVE_LEVEL = "video_live_level"
    VIDEO_LIVE_COUNT = "video_live_count"
    CLIPS_COUNT = "clips_count"
    HAS_UNSEEN_STORIES = "has_unseen_stories"
    IS_BUSINESS = "is_business"
    TEXTLIVES_COUNT = "textlives_count"


class GroupsFilter(enum.Enum):
    """ GroupsFilter enum """

    ADMIN = "admin"
    EDITOR = "editor"
    MODER = "moder"
    ADVERTISER = "advertiser"
    GROUPS = "groups"
    PUBLICS = "publics"
    EVENTS = "events"
    HAS_ADDRESSES = "has_addresses"


class GroupsGroup(BaseModel):
    """VK Object GroupsGroup

    admin_level -
    deactivated - Information whether community is banned
    est_date - Established date
    finish_date - Finish date in Unixtime format
    id - Community ID
    is_admin - Information whether current user is administrator
    is_advertiser - Information whether current user is advertiser
    is_closed -
    is_member - Information whether current user is member
    is_video_live_notifications_blocked -
    name - Community name
    photo_100 - URL of square photo of the community with 100 pixels in width
    photo_200 - URL of square photo of the community with 200 pixels in width
    photo_200_orig - URL of square photo of the community with 200 pixels in width original
    photo_400 - URL of square photo of the community with 400 pixels in width
    photo_400_orig - URL of square photo of the community with 400 pixels in width original
    photo_50 - URL of square photo of the community with 50 pixels in width
    photo_max - URL of square photo of the community with max pixels in width
    photo_max_orig - URL of square photo of the community with max pixels in width original
    photo_max_size -
    public_date_label - Public date label
    screen_name - Domain of the community page
    start_date - Start date in Unixtime format
    type -
    video_live -
    """

    admin_level: typing.Optional["GroupsGroupAdminLevel"] = None
    deactivated: typing.Optional[str] = None
    est_date: typing.Optional[str] = None
    finish_date: typing.Optional[int] = None
    id: int = None
    is_admin: typing.Optional["BaseBoolInt"] = None
    is_advertiser: typing.Optional["BaseBoolInt"] = None
    is_closed: "GroupsGroupIsClosed" = None
    is_member: typing.Optional["BaseBoolInt"] = None
    is_video_live_notifications_blocked: typing.Optional["BaseBoolInt"] = None
    name: str = None
    photo_100: typing.Optional[str] = None
    photo_200: typing.Optional[str] = None
    photo_200_orig: typing.Optional[str] = None
    photo_400: typing.Optional[str] = None
    photo_400_orig: typing.Optional[str] = None
    photo_50: typing.Optional[str] = None
    photo_max: typing.Optional[str] = None
    photo_max_orig: typing.Optional[str] = None
    photo_max_size: typing.Optional["GroupsPhotoSize"] = None
    public_date_label: typing.Optional[str] = None
    screen_name: str = None
    start_date: typing.Optional[int] = None
    type: typing.Optional["GroupsGroupType"] = None
    video_live: typing.Optional["VideoLiveInfo"] = None


class GroupsGroupAccess(enum.IntEnum):
    """ GroupsGroupAccess enum """

    open = 0
    closed = 1
    private = 2


class GroupsGroupAdminLevel(enum.IntEnum):
    """ Level of current user's credentials as manager """

    moderator = 1
    editor = 2
    administrator = 3


class GroupsGroupAgeLimits(enum.IntEnum):
    """ GroupsGroupAgeLimits enum """

    unlimited = 1
    _16_plus = 2
    _18_plus = 3


class GroupsGroupAttach(BaseModel):
    """VK Object GroupsGroupAttach

    id - group ID
    is_favorite - is favorite
    size - size of group
    status - activity or category of group
    text - text of attach
    """

    id: int = None
    is_favorite: bool = None
    size: int = None
    status: str = None
    text: str = None


class GroupsGroupAudio(enum.IntEnum):
    """ GroupsGroupAudio enum """

    disabled = 0
    open = 1
    limited = 2


class GroupsGroupBanInfo(BaseModel):
    """VK Object GroupsGroupBanInfo

    comment - Ban comment
    end_date - End date of ban in Unixtime
    reason -
    """

    comment: typing.Optional[str] = None
    end_date: typing.Optional[int] = None
    reason: typing.Optional["GroupsBanInfoReason"] = None


class GroupsGroupCategory(BaseModel):
    """VK Object GroupsGroupCategory

    id - Category ID
    name - Category name
    subcategories -
    """

    id: int = None
    name: str = None
    subcategories: typing.Optional[typing.List["BaseObjectWithName"]] = None


class GroupsGroupCategoryFull(BaseModel):
    """VK Object GroupsGroupCategoryFull

    id - Category ID
    name - Category name
    page_count - Pages number
    page_previews -
    subcategories -
    """

    id: int = None
    name: str = None
    page_count: int = None
    page_previews: typing.List["GroupsGroup"] = None
    subcategories: typing.Optional[typing.List["GroupsGroupCategory"]] = None


class GroupsGroupCategoryType(BaseModel):
    """VK Object GroupsGroupCategoryType"""

    id: int = None
    name: str = None


class GroupsGroupDocs(enum.IntEnum):
    """ GroupsGroupDocs enum """

    disabled = 0
    open = 1
    limited = 2


class GroupsGroupFull(GroupsGroup):
    """VK Object GroupsGroupFull

    activity - Type of group, start date of event or category of public page
    addresses - Info about addresses in groups
    age_limits - Information whether age limit
    ban_info - User ban info
    can_create_topic - Information whether current user can create topic
    can_message - Information whether current user can send a message to community
    can_post - Information whether current user can post on community's wall
    can_see_all_posts - Information whether current user can see all posts on community's wall
    can_send_notify - Information whether community can send notifications by phone number to current user
    can_subscribe_podcasts - Owner in whitelist or not
    can_subscribe_posts - Can subscribe to wall
    can_suggest -
    can_upload_doc - Information whether current user can upload doc
    can_upload_story - Information whether current user can upload story
    can_upload_video - Information whether current user can upload video
    city -
    clips_count - Number of community's clips
    contacts -
    counters -
    country -
    cover -
    crop_photo - Данные о точках, по которым вырезаны профильная и миниатюрная фотографии сообщества
    description - Community description
    fixed_post - Fixed post ID
    has_group_channel -
    has_market_app - Information whether community has installed market app
    has_photo - Information whether community has photo
    has_unseen_stories -
    invited_by - Inviter ID
    is_adult - Information whether community is adult
    is_favorite - Information whether community is in faves
    is_hidden_from_feed - Information whether community is hidden from current user's newsfeed
    is_messages_blocked - Information whether community can send a message to current user
    is_subscribed - Information whether current user is subscribed
    is_subscribed_podcasts - Information whether current user is subscribed to podcasts
    links -
    live_covers - Live covers state
    main_album_id - Community's main photo album ID
    main_section -
    market -
    member_status - Current user's member status
    members_count - Community members number
    online_status - Status of replies in community messages
    requests_count - The number of incoming requests to the community
    secondary_section -
    site - Community's website
    status - Community status
    status_audio -
    stories_archive_count -
    trending - Information whether the community has a "fire" pictogram.
    using_vkpay_market_app -
    verified - Information whether community is verified
    video_live_count - Number of community's live streams
    video_live_level - Community level live streams achievements
    wall - Information about wall status in community
    wiki_page - Community's main wiki page title
    """

    activity: typing.Optional[str] = None
    addresses: typing.Optional["GroupsAddressesInfo"] = None
    age_limits: typing.Optional["GroupsGroupFullAgeLimits"] = None
    ban_info: typing.Optional["GroupsGroupBanInfo"] = None
    can_create_topic: typing.Optional["BaseBoolInt"] = None
    can_message: typing.Optional["BaseBoolInt"] = None
    can_post: typing.Optional["BaseBoolInt"] = None
    can_see_all_posts: typing.Optional["BaseBoolInt"] = None
    can_send_notify: typing.Optional["BaseBoolInt"] = None
    can_subscribe_podcasts: typing.Optional[bool] = None
    can_subscribe_posts: typing.Optional[bool] = None
    can_suggest: typing.Optional["BaseBoolInt"] = None
    can_upload_doc: typing.Optional["BaseBoolInt"] = None
    can_upload_story: typing.Optional["BaseBoolInt"] = None
    can_upload_video: typing.Optional["BaseBoolInt"] = None
    city: typing.Optional["BaseObject"] = None
    clips_count: typing.Optional[int] = None
    contacts: typing.Optional[typing.List["GroupsContactsItem"]] = None
    counters: typing.Optional["GroupsCountersGroup"] = None
    country: typing.Optional["BaseCountry"] = None
    cover: typing.Optional["GroupsCover"] = None
    crop_photo: typing.Optional["BaseCropPhoto"] = None
    description: typing.Optional[str] = None
    fixed_post: typing.Optional[int] = None
    has_group_channel: typing.Optional[bool] = None
    has_market_app: typing.Optional[bool] = None
    has_photo: typing.Optional["BaseBoolInt"] = None
    has_unseen_stories: typing.Optional[bool] = None
    invited_by: typing.Optional[int] = None
    is_adult: typing.Optional["BaseBoolInt"] = None
    is_favorite: typing.Optional["BaseBoolInt"] = None
    is_hidden_from_feed: typing.Optional["BaseBoolInt"] = None
    is_messages_blocked: typing.Optional["BaseBoolInt"] = None
    is_subscribed: typing.Optional["BaseBoolInt"] = None
    is_subscribed_podcasts: typing.Optional[bool] = None
    links: typing.Optional[typing.List["GroupsLinksItem"]] = None
    live_covers: typing.Optional["GroupsLiveCovers"] = None
    main_album_id: typing.Optional[int] = None
    main_section: typing.Optional["GroupsGroupFullSection"] = None
    market: typing.Optional["GroupsMarketInfo"] = None
    member_status: typing.Optional["GroupsGroupFullMemberStatus"] = None
    members_count: typing.Optional[int] = None
    online_status: typing.Optional["GroupsOnlineStatus"] = None
    requests_count: typing.Optional[int] = None
    secondary_section: typing.Optional["GroupsGroupFullSection"] = None
    site: typing.Optional[str] = None
    status: typing.Optional[str] = None
    status_audio: typing.Optional["AudioAudio"] = None
    stories_archive_count: typing.Optional[int] = None
    trending: typing.Optional["BaseBoolInt"] = None
    using_vkpay_market_app: typing.Optional[bool] = None
    verified: typing.Optional["BaseBoolInt"] = None
    video_live_count: typing.Optional[int] = None
    video_live_level: typing.Optional[int] = None
    wall: typing.Optional[int] = None
    wiki_page: typing.Optional[str] = None


class GroupsGroupFullAgeLimits(enum.IntEnum):
    """ GroupsGroupFullAgeLimits enum """

    no = 1
    over_16 = 2
    over_18 = 3


class GroupsGroupFullMemberStatus(enum.IntEnum):
    """ GroupsGroupFullMemberStatus enum """

    not_a_member = 0
    member = 1
    not_sure = 2
    declined = 3
    has_sent_a_request = 4
    invited = 5


class GroupsGroupFullSection(enum.IntEnum):
    """ Main section of community """

    absent = 0
    photos = 1
    topics = 2
    audio = 3
    video = 4
    market = 5
    events = 10
    addresses = 35
    articles = 39
    chats = 43
    market_services = 51


class GroupsGroupIsClosed(enum.IntEnum):
    """ Information whether community is closed """

    open = 0
    closed = 1
    private = 2


class GroupsGroupMarketCurrency(enum.IntEnum):
    """ GroupsGroupMarketCurrency enum """

    russian_rubles = 643
    ukrainian_hryvnia = 980
    kazakh_tenge = 398
    euro = 978
    us_dollars = 840


class GroupsGroupPhotos(enum.IntEnum):
    """ GroupsGroupPhotos enum """

    disabled = 0
    open = 1
    limited = 2


class GroupsGroupPublicCategoryList(BaseModel):
    """VK Object GroupsGroupPublicCategoryList"""

    id: typing.Optional[int] = None
    name: typing.Optional[str] = None
    subcategories: typing.Optional[typing.List["GroupsGroupCategoryType"]] = None


class GroupsGroupRole(enum.Enum):
    """ GroupsGroupRole enum """

    MODERATOR = "moderator"
    EDITOR = "editor"
    ADMINISTRATOR = "administrator"
    ADVERTISER = "advertiser"


class GroupsGroupSubject(enum.IntEnum):
    """ GroupsGroupSubject enum """

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


class GroupsGroupSuggestedPrivacy(enum.IntEnum):
    """ GroupsGroupSuggestedPrivacy enum """

    none = 0
    all = 1
    subscribers = 2


class GroupsGroupTagColor(enum.Enum):
    """ GroupsGroupTagColor enum """

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
    """VK Object GroupsGroupTag"""

    color: "GroupsGroupTagColor" = None
    id: int = None
    name: str = None
    uses: typing.Optional[int] = None


class GroupsGroupTopics(enum.IntEnum):
    """ GroupsGroupTopics enum """

    disabled = 0
    open = 1
    limited = 2


class GroupsGroupType(enum.Enum):
    """ Community type """

    GROUP = "group"
    PAGE = "page"
    EVENT = "event"


class GroupsGroupVideo(enum.IntEnum):
    """ GroupsGroupVideo enum """

    disabled = 0
    open = 1
    limited = 2


class GroupsGroupWall(enum.IntEnum):
    """ GroupsGroupWall enum """

    disabled = 0
    open = 1
    limited = 2
    closed = 3


class GroupsGroupWiki(enum.IntEnum):
    """ GroupsGroupWiki enum """

    disabled = 0
    open = 1
    limited = 2


class GroupsGroupsArray(BaseModel):
    """VK Object GroupsGroupsArray

    count - Communities number
    items -
    """

    count: int = None
    items: typing.List[int] = None


class GroupsLinksItem(BaseModel):
    """VK Object GroupsLinksItem

    desc - Link description
    edit_title - Information whether the link title can be edited
    id - Link ID
    image_processing - Information whether the image on processing
    name - Link title
    photo_100 - URL of square image of the link with 100 pixels in width
    photo_50 - URL of square image of the link with 50 pixels in width
    url - Link URL
    """

    desc: typing.Optional[str] = None
    edit_title: typing.Optional["BaseBoolInt"] = None
    id: typing.Optional[int] = None
    image_processing: typing.Optional["BaseBoolInt"] = None
    name: typing.Optional[str] = None
    photo_100: typing.Optional[str] = None
    photo_50: typing.Optional[str] = None
    url: typing.Optional[str] = None


class GroupsLiveCovers(BaseModel):
    """VK Object GroupsLiveCovers

    is_enabled - Information whether live covers is enabled
    is_scalable - Information whether live covers photo scaling is enabled
    story_ids -
    """

    is_enabled: bool = None
    is_scalable: typing.Optional[bool] = None
    story_ids: typing.Optional[typing.List[str]] = None


class GroupsLongPollEvents(BaseModel):
    """VK Object GroupsLongPollEvents"""

    audio_new: "BaseBoolInt" = None
    board_post_delete: "BaseBoolInt" = None
    board_post_edit: "BaseBoolInt" = None
    board_post_new: "BaseBoolInt" = None
    board_post_restore: "BaseBoolInt" = None
    donut_money_withdraw: "BaseBoolInt" = None
    donut_money_withdraw_error: "BaseBoolInt" = None
    donut_subscription_cancelled: "BaseBoolInt" = None
    donut_subscription_create: "BaseBoolInt" = None
    donut_subscription_expired: "BaseBoolInt" = None
    donut_subscription_price_changed: "BaseBoolInt" = None
    donut_subscription_prolonged: "BaseBoolInt" = None
    group_change_photo: "BaseBoolInt" = None
    group_change_settings: "BaseBoolInt" = None
    group_join: "BaseBoolInt" = None
    group_leave: "BaseBoolInt" = None
    group_officers_edit: "BaseBoolInt" = None
    lead_forms_new: typing.Optional["BaseBoolInt"] = None
    market_comment_delete: "BaseBoolInt" = None
    market_comment_edit: "BaseBoolInt" = None
    market_comment_new: "BaseBoolInt" = None
    market_comment_restore: "BaseBoolInt" = None
    market_order_edit: typing.Optional["BaseBoolInt"] = None
    market_order_new: typing.Optional["BaseBoolInt"] = None
    message_allow: "BaseBoolInt" = None
    message_deny: "BaseBoolInt" = None
    message_edit: "BaseBoolInt" = None
    message_new: "BaseBoolInt" = None
    message_read: "BaseBoolInt" = None
    message_reply: "BaseBoolInt" = None
    message_typing_state: "BaseBoolInt" = None
    photo_comment_delete: "BaseBoolInt" = None
    photo_comment_edit: "BaseBoolInt" = None
    photo_comment_new: "BaseBoolInt" = None
    photo_comment_restore: "BaseBoolInt" = None
    photo_new: "BaseBoolInt" = None
    poll_vote_new: "BaseBoolInt" = None
    user_block: "BaseBoolInt" = None
    user_unblock: "BaseBoolInt" = None
    video_comment_delete: "BaseBoolInt" = None
    video_comment_edit: "BaseBoolInt" = None
    video_comment_new: "BaseBoolInt" = None
    video_comment_restore: "BaseBoolInt" = None
    video_new: "BaseBoolInt" = None
    wall_post_new: "BaseBoolInt" = None
    wall_reply_delete: "BaseBoolInt" = None
    wall_reply_edit: "BaseBoolInt" = None
    wall_reply_new: "BaseBoolInt" = None
    wall_reply_restore: "BaseBoolInt" = None
    wall_repost: "BaseBoolInt" = None


class GroupsLongPollServer(BaseModel):
    """VK Object GroupsLongPollServer

    key - Long Poll key
    server - Long Poll server address
    ts - Number of the last event
    """

    key: str = None
    server: str = None
    ts: str = None


class GroupsLongPollSettings(BaseModel):
    """VK Object GroupsLongPollSettings

    api_version - API version used for the events
    events -
    is_enabled - Shows whether Long Poll is enabled
    """

    api_version: typing.Optional[str] = None
    events: "GroupsLongPollEvents" = None
    is_enabled: bool = None


class GroupsMarketInfo(BaseModel):
    """VK Object GroupsMarketInfo

    contact_id - Contact person ID
    currency -
    currency_text - Currency name
    enabled - Information whether the market is enabled
    main_album_id - Main market album ID
    min_order_price -
    price_max - Maximum price
    price_min - Minimum price
    type - Market type
    """

    contact_id: typing.Optional[int] = None
    currency: typing.Optional["MarketCurrency"] = None
    currency_text: typing.Optional[str] = None
    enabled: typing.Optional["BaseBoolInt"] = None
    main_album_id: typing.Optional[int] = None
    min_order_price: typing.Optional["MarketPrice"] = None
    price_max: typing.Optional[str] = None
    price_min: typing.Optional[str] = None
    type: typing.Optional[str] = None


class GroupsMarketState(enum.Enum):
    """ Declares state if market is enabled in group. """

    NONE = "none"
    BASIC = "basic"
    ADVANCED = "advanced"


class GroupsMemberRole(BaseModel):
    """VK Object GroupsMemberRole

    id - User ID
    permissions -
    role -
    """

    id: int = None
    permissions: typing.Optional[typing.List["GroupsMemberRolePermission"]] = None
    role: typing.Optional["GroupsMemberRoleStatus"] = None


class GroupsMemberRolePermission(enum.Enum):
    """ GroupsMemberRolePermission enum """

    ADS = "ads"


class GroupsMemberRoleStatus(enum.Enum):
    """ User's credentials as community admin """

    MODERATOR = "moderator"
    EDITOR = "editor"
    ADMINISTRATOR = "administrator"
    CREATOR = "creator"
    ADVERTISER = "advertiser"


class GroupsMemberStatus(BaseModel):
    """VK Object GroupsMemberStatus

    member - Information whether user is a member of the group
    user_id - User ID
    """

    member: "BaseBoolInt" = None
    user_id: int = None


class GroupsMemberStatusFull(BaseModel):
    """VK Object GroupsMemberStatusFull

    can_invite - Information whether user can be invited
    can_recall - Information whether user's invite to the group can be recalled
    invitation - Information whether user has been invited to the group
    member - Information whether user is a member of the group
    request - Information whether user has send request to the group
    user_id - User ID
    """

    can_invite: typing.Optional["BaseBoolInt"] = None
    can_recall: typing.Optional["BaseBoolInt"] = None
    invitation: typing.Optional["BaseBoolInt"] = None
    member: "BaseBoolInt" = None
    request: typing.Optional["BaseBoolInt"] = None
    user_id: int = None


class GroupsOnlineStatus(BaseModel):
    """VK Object GroupsOnlineStatus

    minutes - Estimated time of answer (for status = answer_mark)
    status -
    """

    minutes: typing.Optional[int] = None
    status: "GroupsOnlineStatusType" = None


class GroupsOnlineStatusType(enum.Enum):
    """ Type of online status of group """

    NONE = "none"
    ONLINE = "online"
    ANSWER_MARK = "answer_mark"


class GroupsOwnerXtrBanInfoType(enum.Enum):
    """ Owner type """

    GROUP = "group"
    PROFILE = "profile"


class GroupsPhotoSize(BaseModel):
    """VK Object GroupsPhotoSize

    height - Image height
    width - Image width
    """

    height: int = None
    width: int = None


class GroupsRoleOptions(enum.Enum):
    """ User's credentials as community admin """

    MODERATOR = "moderator"
    EDITOR = "editor"
    ADMINISTRATOR = "administrator"
    CREATOR = "creator"


GroupsSectionsListItem = typing.List[typing.Union[int, str]]  # (index, title) tuples


class GroupsSettingsTwitterStatus(enum.Enum):
    """ GroupsSettingsTwitterStatus enum """

    LOADING = "loading"
    SYNC = "sync"


class GroupsSettingsTwitter(BaseModel):
    """VK Object GroupsSettingsTwitter"""

    name: typing.Optional[str] = None
    status: "GroupsSettingsTwitterStatus" = None


class GroupsSubjectItem(BaseModel):
    """VK Object GroupsSubjectItem

    id - Subject ID
    name - Subject title
    """

    id: int = None
    name: str = None


class GroupsTokenPermissionSetting(BaseModel):
    """VK Object GroupsTokenPermissionSetting"""

    name: str = None
    setting: int = None


class GroupsUserXtrRole(UsersUserFull):
    """VK Object GroupsUserXtrRole"""

    role: typing.Optional["GroupsRoleOptions"] = None


class LeadFormsAnswer(BaseModel):
    """VK Object LeadFormsAnswer"""

    answer: typing.Union["LeadFormsAnswerItem", typing.List["LeadFormsAnswerItem"]] = None
    key: str = None


class LeadFormsAnswerItem(BaseModel):
    """VK Object LeadFormsAnswerItem"""

    key: typing.Optional[str] = None
    value: str = None


class LeadFormsForm(BaseModel):
    """VK Object LeadFormsForm"""

    active: typing.Optional["BaseBoolInt"] = None
    confirmation: typing.Optional[str] = None
    description: typing.Optional[str] = None
    form_id: int = None
    group_id: int = None
    leads_count: int = None
    name: typing.Optional[str] = None
    notify_admins: typing.Optional[str] = None
    notify_emails: typing.Optional[str] = None
    once_per_user: typing.Optional[int] = None
    photo: typing.Optional[str] = None
    pixel_code: typing.Optional[str] = None
    policy_link_url: typing.Optional[str] = None
    questions: typing.Optional[typing.List["LeadFormsQuestionItem"]] = None
    site_link_url: typing.Optional[str] = None
    title: typing.Optional[str] = None
    url: str = None


class LeadFormsLead(BaseModel):
    """VK Object LeadFormsLead"""

    ad_id: typing.Optional[int] = None
    answers: typing.List["LeadFormsAnswer"] = None
    date: int = None
    lead_id: int = None
    user_id: int = None


class LeadFormsQuestionItemType(enum.Enum):
    """ LeadFormsQuestionItemType enum """

    INPUT = "input"
    TEXTAREA = "textarea"
    RADIO = "radio"
    CHECKBOX = "checkbox"
    SELECT = "select"


class LeadFormsQuestionItem(BaseModel):
    """VK Object LeadFormsQuestionItem

    key -
    label -
    options - Опции выбора для типов radio, checkbox, select
    type -
    """

    key: str = None
    label: typing.Optional[str] = None
    options: typing.Optional[typing.List["LeadFormsQuestionItemOption"]] = None
    type: "LeadFormsQuestionItemType" = None


class LeadFormsQuestionItemOption(BaseModel):
    """VK Object LeadFormsQuestionItemOption"""

    key: typing.Optional[str] = None
    label: str = None


class LikesType(enum.Enum):
    """ LikesType enum """

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


class LinkTargetObject(BaseModel):
    """VK Object LinkTargetObject

    item_id - Item ID
    owner_id - Owner ID
    type - Object type
    """

    item_id: typing.Optional[int] = None
    owner_id: typing.Optional[int] = None
    type: typing.Optional[str] = None


class MarketCurrency(BaseModel):
    """VK Object MarketCurrency

    id - Currency ID
    name - Currency sign
    title - Currency title
    """

    id: int = None
    name: str = None
    title: str = None


class MarketMarketAlbum(BaseModel):
    """VK Object MarketMarketAlbum

    count - Items number
    id - Market album ID
    is_hidden - Is album hidden
    is_main - Is album main for owner
    owner_id - Market album owner's ID
    photo -
    title - Market album title
    updated_time - Date when album has been updated last time in Unixtime
    """

    count: int = None
    id: int = None
    is_hidden: typing.Optional[bool] = None
    is_main: typing.Optional[bool] = None
    owner_id: int = None
    photo: typing.Optional["PhotosPhoto"] = None
    title: str = None
    updated_time: int = None


class MarketMarketCategoryOld(BaseModel):
    """VK Object MarketMarketCategoryOld

    id - Category ID
    name - Category name
    section -
    """

    id: int = None
    name: str = None
    section: "MarketSection" = None


class MarketMarketCategory(MarketMarketCategoryOld):
    """VK Object MarketMarketCategory"""

    pass


class MarketMarketCategoryNested(BaseModel):
    """VK Object MarketMarketCategoryNested

    id - Category ID
    name - Category name
    parent -
    """

    id: int = None
    name: str = None
    parent: typing.Optional["MarketMarketCategoryNested"] = None


class MarketMarketCategoryTree(BaseModel):
    """VK Object MarketMarketCategoryTree

    children -
    id - Category ID
    name - Category name
    """

    children: typing.Optional[typing.List["MarketMarketCategoryTree"]] = None
    id: int = None
    name: str = None


class MarketMarketItem(BaseModel):
    """VK Object MarketMarketItem

    access_key - Access key for the market item
    availability -
    button_title - Title for button for url
    category -
    date - Date when the item has been created in Unixtime
    description - Item description
    external_id -
    id - Item ID
    is_favorite -
    is_main_variant -
    owner_id - Item owner's ID
    price -
    sku -
    thumb_photo - URL of the preview image
    title - Item title
    url - URL to item
    variants_grouping_id -
    """

    access_key: typing.Optional[str] = None
    availability: "MarketMarketItemAvailability" = None
    button_title: typing.Optional[str] = None
    category: "MarketMarketCategory" = None
    date: typing.Optional[int] = None
    description: str = None
    external_id: typing.Optional[str] = None
    id: int = None
    is_favorite: typing.Optional[bool] = None
    is_main_variant: typing.Optional[bool] = None
    owner_id: int = None
    price: "MarketPrice" = None
    sku: typing.Optional[str] = None
    thumb_photo: typing.Optional[str] = None
    title: str = None
    url: typing.Optional[str] = None
    variants_grouping_id: typing.Optional[int] = None


class MarketMarketItemAvailability(enum.IntEnum):
    """ Information whether the item is available """

    available = 0
    removed = 1
    unavailable = 2


class MarketMarketItemFull(MarketMarketItem):
    """VK Object MarketMarketItemFull

    albums_ids -
    can_comment - Information whether current use can comment the item
    can_repost - Information whether current use can repost the item
    cancel_info - Information for cancel and revert order
    likes -
    photos -
    reposts -
    user_agreement_info - User agreement info
    views_count - Views number
    wishlist_item_id - Object identifier in wishlist of viewer
    """

    albums_ids: typing.Optional[typing.List[int]] = None
    can_comment: typing.Optional["BaseBoolInt"] = None
    can_repost: typing.Optional["BaseBoolInt"] = None
    cancel_info: typing.Optional["BaseLink"] = None
    likes: typing.Optional["BaseLikes"] = None
    photos: typing.Optional[typing.List["PhotosPhoto"]] = None
    reposts: typing.Optional["BaseRepostsInfo"] = None
    user_agreement_info: typing.Optional[str] = None
    views_count: typing.Optional[int] = None
    wishlist_item_id: typing.Optional[int] = None


class MarketOrder(BaseModel):
    """VK Object MarketOrder

    address -
    cancel_info - Information for cancel and revert order
    comment -
    date -
    display_order_id -
    group_id -
    id -
    items_count -
    merchant_comment -
    preview_order_items - Several order items for preview
    status -
    total_price -
    track_link -
    track_number -
    user_id -
    weight -
    """

    address: typing.Optional[str] = None
    cancel_info: typing.Optional["BaseLink"] = None
    comment: typing.Optional[str] = None
    date: int = None
    display_order_id: typing.Optional[str] = None
    group_id: int = None
    id: int = None
    items_count: int = None
    merchant_comment: typing.Optional[str] = None
    preview_order_items: typing.Optional[typing.List["MarketOrderItem"]] = None
    status: int = None
    total_price: "MarketPrice" = None
    track_link: typing.Optional[str] = None
    track_number: typing.Optional[str] = None
    user_id: int = None
    weight: typing.Optional[int] = None


class MarketOrderItem(BaseModel):
    """VK Object MarketOrderItem"""

    item: "MarketMarketItem" = None
    item_id: int = None
    owner_id: int = None
    photo: typing.Optional["PhotosPhoto"] = None
    price: "MarketPrice" = None
    quantity: int = None
    title: typing.Optional[str] = None
    variants: typing.Optional[typing.List[str]] = None


class MarketPrice(BaseModel):
    """VK Object MarketPrice

    amount - Amount
    currency -
    discount_rate -
    old_amount -
    old_amount_text - Textual representation of old price
    text - Text
    """

    amount: str = None
    currency: "MarketCurrency" = None
    discount_rate: typing.Optional[int] = None
    old_amount: typing.Optional[str] = None
    old_amount_text: typing.Optional[str] = None
    text: str = None


class MarketSection(BaseModel):
    """VK Object MarketSection

    id - Section ID
    name - Section name
    """

    id: int = None
    name: str = None


class MarketServicesViewType(enum.IntEnum):
    """ Type of view. 1 - cards, 2 - rows """

    cards = 1
    rows = 2


class MessagesAudioMessage(BaseModel):
    """VK Object MessagesAudioMessage

    access_key - Access key for audio message
    duration - Audio message duration in seconds
    id - Audio message ID
    link_mp3 - MP3 file URL
    link_ogg - OGG file URL
    owner_id - Audio message owner ID
    transcript_error -
    waveform -
    """

    access_key: typing.Optional[str] = None
    duration: int = None
    id: int = None
    link_mp3: str = None
    link_ogg: str = None
    owner_id: int = None
    transcript_error: typing.Optional[int] = None
    waveform: typing.List[int] = None


class MessagesChat(BaseModel):
    """VK Object MessagesChat

    admin_id - Chat creator ID
    id - Chat ID
    is_default_photo - If provided photo is default
    is_group_channel - If chat is group channel
    kicked - Shows that user has been kicked from the chat
    left - Shows that user has been left the chat
    members_count - Count members in a chat
    photo_100 - URL of the preview image with 100 px in width
    photo_200 - URL of the preview image with 200 px in width
    photo_50 - URL of the preview image with 50 px in width
    push_settings -
    title - Chat title
    type - Chat type
    users -
    """

    admin_id: int = None
    id: int = None
    is_default_photo: typing.Optional[bool] = None
    is_group_channel: typing.Optional[bool] = None
    kicked: typing.Optional["BaseBoolInt"] = None
    left: typing.Optional["BaseBoolInt"] = None
    members_count: int = None
    photo_100: typing.Optional[str] = None
    photo_200: typing.Optional[str] = None
    photo_50: typing.Optional[str] = None
    push_settings: typing.Optional["MessagesChatPushSettings"] = None
    title: typing.Optional[str] = None
    type: str = None
    users: typing.List[int] = None


class MessagesChatFull(BaseModel):
    """VK Object MessagesChatFull

    admin_id - Chat creator ID
    id - Chat ID
    kicked - Shows that user has been kicked from the chat
    left - Shows that user has been left the chat
    photo_100 - URL of the preview image with 100 px in width
    photo_200 - URL of the preview image with 200 px in width
    photo_50 - URL of the preview image with 50 px in width
    push_settings -
    title - Chat title
    type - Chat type
    users -
    """

    admin_id: int = None
    id: int = None
    kicked: typing.Optional["BaseBoolInt"] = None
    left: typing.Optional["BaseBoolInt"] = None
    photo_100: typing.Optional[str] = None
    photo_200: typing.Optional[str] = None
    photo_50: typing.Optional[str] = None
    push_settings: typing.Optional["MessagesChatPushSettings"] = None
    title: typing.Optional[str] = None
    type: str = None
    users: typing.List["MessagesUserXtrInvitedBy"] = None


class MessagesChatPreview(BaseModel):
    """VK Object MessagesChatPreview"""

    admin_id: typing.Optional[int] = None
    is_member: typing.Optional[bool] = None
    joined: typing.Optional[bool] = None
    local_id: typing.Optional[int] = None
    members: typing.Optional[typing.List[int]] = None
    members_count: typing.Optional[int] = None
    title: typing.Optional[str] = None


class MessagesChatPushSettings(BaseModel):
    """VK Object MessagesChatPushSettings

    disabled_until - Time until that notifications are disabled
    sound - Information whether the sound is on
    """

    disabled_until: typing.Optional[int] = None
    sound: typing.Optional["BaseBoolInt"] = None


class MessagesChatRestrictions(BaseModel):
    """VK Object MessagesChatRestrictions

    admins_promote_users - Only admins can promote users to admins
    only_admins_edit_info - Only admins can change chat info
    only_admins_edit_pin - Only admins can edit pinned message
    only_admins_invite - Only admins can invite users to this chat
    only_admins_kick - Only admins can kick users from this chat
    """

    admins_promote_users: typing.Optional[bool] = None
    only_admins_edit_info: typing.Optional[bool] = None
    only_admins_edit_pin: typing.Optional[bool] = None
    only_admins_invite: typing.Optional[bool] = None
    only_admins_kick: typing.Optional[bool] = None


class MessagesChatSettings(BaseModel):
    """VK Object MessagesChatSettings

    acl -
    active_ids -
    admin_ids - Ids of chat admins
    disappearing_chat_link -
    friends_count -
    is_disappearing -
    is_group_channel -
    is_service -
    members_count -
    owner_id -
    permissions -
    photo -
    pinned_message -
    state -
    theme -
    title - Chat title
    """

    acl: "MessagesChatSettingsAcl" = None
    active_ids: typing.List[int] = None
    admin_ids: typing.Optional[typing.List[int]] = None
    disappearing_chat_link: typing.Optional[str] = None
    friends_count: typing.Optional[int] = None
    is_disappearing: typing.Optional[bool] = None
    is_group_channel: typing.Optional[bool] = None
    is_service: typing.Optional[bool] = None
    members_count: typing.Optional[int] = None
    owner_id: int = None
    permissions: typing.Optional["MessagesChatSettingsPermissions"] = None
    photo: typing.Optional["MessagesChatSettingsPhoto"] = None
    pinned_message: typing.Optional["MessagesPinnedMessage"] = None
    state: "MessagesChatSettingsState" = None
    theme: typing.Optional[str] = None
    title: str = None


class MessagesChatSettingsAcl(BaseModel):
    """VK Object MessagesChatSettingsAcl

    can_call - Can you init group call in the chat
    can_change_info - Can you change photo, description and name
    can_change_invite_link - Can you change invite link for this chat
    can_change_pin - Can you pin/unpin message for this chat
    can_change_service_type - Can you change chat service type
    can_copy_chat - Can you copy chat
    can_invite - Can you invite other peers in chat
    can_moderate - Can you moderate (delete) other users' messages
    can_promote_users - Can you promote simple users to chat admins
    can_see_invite_link - Can you see invite link for this chat
    can_use_mass_mentions - Can you use mass mentions
    """

    can_call: bool = None
    can_change_info: bool = None
    can_change_invite_link: bool = None
    can_change_pin: bool = None
    can_change_service_type: typing.Optional[bool] = None
    can_copy_chat: bool = None
    can_invite: bool = None
    can_moderate: bool = None
    can_promote_users: bool = None
    can_see_invite_link: bool = None
    can_use_mass_mentions: bool = None


class MessagesChatSettingsPermissionsInvite(enum.Enum):
    """ Who can invite users to chat """

    OWNER = "owner"
    OWNER_AND_ADMINS = "owner_and_admins"
    ALL = "all"


class MessagesChatSettingsPermissionsChangeInfo(enum.Enum):
    """ Who can change chat info """

    OWNER = "owner"
    OWNER_AND_ADMINS = "owner_and_admins"
    ALL = "all"


class MessagesChatSettingsPermissionsChangePin(enum.Enum):
    """ Who can change pinned message """

    OWNER = "owner"
    OWNER_AND_ADMINS = "owner_and_admins"
    ALL = "all"


class MessagesChatSettingsPermissionsUseMassMentions(enum.Enum):
    """ Who can use mass mentions """

    OWNER = "owner"
    OWNER_AND_ADMINS = "owner_and_admins"
    ALL = "all"


class MessagesChatSettingsPermissionsSeeInviteLink(enum.Enum):
    """ Who can see invite link """

    OWNER = "owner"
    OWNER_AND_ADMINS = "owner_and_admins"
    ALL = "all"


class WhoCanMakeCalls(enum.Enum):
    """ Who can make calls """

    OWNER = "owner"
    OWNER_AND_ADMINS = "owner_and_admins"
    ALL = "all"


class WhoCanChangeAdmins(enum.Enum):
    """ Who can change admins """

    OWNER = "owner"
    OWNER_AND_ADMINS = "owner_and_admins"


class MessagesChatSettingsPermissions(BaseModel):
    """VK Object MessagesChatSettingsPermissions

    call - Who can make calls
    change_admins - Who can change admins
    change_info - Who can change chat info
    change_pin - Who can change pinned message
    invite - Who can invite users to chat
    see_invite_link - Who can see invite link
    use_mass_mentions - Who can use mass mentions
    """

    call: typing.Optional["WhoCanMakeCalls"] = None
    change_admins: typing.Optional["WhoCanChangeAdmins"] = None
    change_info: typing.Optional["MessagesChatSettingsPermissionsChangeInfo"] = None
    change_pin: typing.Optional["MessagesChatSettingsPermissionsChangePin"] = None
    invite: typing.Optional["MessagesChatSettingsPermissionsInvite"] = None
    see_invite_link: typing.Optional["MessagesChatSettingsPermissionsSeeInviteLink"] = None
    use_mass_mentions: typing.Optional["MessagesChatSettingsPermissionsUseMassMentions"] = None


class MessagesChatSettingsPhoto(BaseModel):
    """VK Object MessagesChatSettingsPhoto

    is_default_call_photo - If provided photo is default call photo
    is_default_photo - If provided photo is default
    photo_100 - URL of the preview image with 100px in width
    photo_200 - URL of the preview image with 200px in width
    photo_50 - URL of the preview image with 50px in width
    """

    is_default_call_photo: typing.Optional[bool] = None
    is_default_photo: typing.Optional[bool] = None
    photo_100: typing.Optional[str] = None
    photo_200: typing.Optional[str] = None
    photo_50: typing.Optional[str] = None


class MessagesChatSettingsState(enum.Enum):
    """ MessagesChatSettingsState enum """

    IN = "in"
    KICKED = "kicked"
    LEFT = "left"


class MessagesConversationSpecialServiceType(enum.Enum):
    """ MessagesConversationSpecialServiceType enum """

    BUSINESS_NOTIFY = "business_notify"


class MessagesConversation(BaseModel):
    """VK Object MessagesConversation

    can_write -
    chat_settings -
    current_keyboard -
    important -
    in_read - Last message user have read
    is_marked_unread - Is this conversation uread
    last_conversation_message_id - Conversation message ID of the last message in conversation
    last_message_id - ID of the last message in conversation
    mentions - Ids of messages with mentions
    message_request_data -
    out_read - Last outcoming message have been read by the opponent
    out_read_by -
    peer -
    push_settings -
    sort_id -
    special_service_type -
    unanswered -
    unread_count - Unread messages number
    """

    can_write: typing.Optional["MessagesConversationCanWrite"] = None
    chat_settings: typing.Optional["MessagesChatSettings"] = None
    current_keyboard: typing.Optional["MessagesKeyboard"] = None
    important: typing.Optional[bool] = None
    in_read: int = None
    is_marked_unread: typing.Optional[bool] = None
    last_conversation_message_id: typing.Optional[int] = None
    last_message_id: int = None
    mentions: typing.Optional[typing.List[int]] = None
    message_request_data: typing.Optional["MessagesMessageRequestData"] = None
    out_read: int = None
    out_read_by: typing.Optional["MessagesOutReadBy"] = None
    peer: "MessagesConversationPeer" = None
    push_settings: typing.Optional["MessagesPushSettings"] = None
    sort_id: typing.Optional["MessagesConversationSortId"] = None
    special_service_type: typing.Optional["MessagesConversationSpecialServiceType"] = None
    unanswered: typing.Optional[bool] = None
    unread_count: typing.Optional[int] = None


class MessagesConversationCanWrite(BaseModel):
    """VK Object MessagesConversationCanWrite"""

    allowed: bool = None
    reason: typing.Optional[int] = None


class MessagesConversationMember(BaseModel):
    """VK Object MessagesConversationMember

    can_kick - Is it possible for user to kick this member
    invited_by -
    is_admin -
    is_message_request -
    is_owner -
    join_date -
    member_id -
    request_date - Message request date
    """

    can_kick: typing.Optional[bool] = None
    invited_by: typing.Optional[int] = None
    is_admin: typing.Optional[bool] = None
    is_message_request: typing.Optional[bool] = None
    is_owner: typing.Optional[bool] = None
    join_date: typing.Optional[int] = None
    member_id: int = None
    request_date: typing.Optional[int] = None


class MessagesConversationPeer(BaseModel):
    """VK Object MessagesConversationPeer"""

    id: int = None
    local_id: typing.Optional[int] = None
    type: "MessagesConversationPeerType" = None


class MessagesConversationPeerType(enum.Enum):
    """ Peer type """

    CHAT = "chat"
    EMAIL = "email"
    USER = "user"
    GROUP = "group"


class MessagesConversationSortId(BaseModel):
    """VK Object MessagesConversationSortId

    major_id - Major id for sorting conversations
    minor_id - Minor id for sorting conversations
    """

    major_id: int = None
    minor_id: int = None


class MessagesConversationWithMessage(BaseModel):
    """VK Object MessagesConversationWithMessage"""

    conversation: "MessagesConversation" = None
    last_message: typing.Optional["MessagesMessage"] = None


class MessagesForeignMessage(BaseModel):
    """VK Object MessagesForeignMessage

    attachments -
    conversation_message_id - Conversation message ID
    date - Date when the message was created
    from_id - Message author's ID
    fwd_messages -
    geo -
    id - Message ID
    payload - Additional data sent along with message for developer convenience
    peer_id - Peer ID
    reply_message -
    text - Message text
    update_time - Date when the message has been updated in Unixtime
    was_listened - Was the audio message inside already listened by you
    """

    attachments: typing.Optional[typing.List["MessagesMessageAttachment"]] = None
    conversation_message_id: typing.Optional[int] = None
    date: int = None
    from_id: int = None
    fwd_messages: typing.Optional[typing.List["MessagesForeignMessage"]] = None
    geo: typing.Optional["BaseGeo"] = None
    id: typing.Optional[int] = None
    payload: typing.Optional[str] = None
    peer_id: typing.Optional[int] = None
    reply_message: typing.Optional["MessagesForeignMessage"] = None
    text: str = None
    update_time: typing.Optional[int] = None
    was_listened: typing.Optional[bool] = None


class MessagesForward(BaseModel):
    """VK Object MessagesForward

    conversation_message_ids -
    is_reply - If you need to reply to a message
    message_ids -
    owner_id - Messages owner_id
    peer_id - Messages peer_id
    """

    conversation_message_ids: typing.Optional[typing.List[int]] = None
    is_reply: typing.Optional[bool] = None
    message_ids: typing.Optional[typing.List[int]] = None
    owner_id: typing.Optional[int] = None
    peer_id: typing.Optional[int] = None


class MessagesGetConversationById(BaseModel):
    """VK Object MessagesGetConversationById

    count - Total number
    items -
    """

    count: int = None
    items: typing.List["MessagesConversation"] = None


class MessagesGetConversationByIdExtended(MessagesGetConversationById):
    """VK Object MessagesGetConversationByIdExtended"""

    groups: typing.Optional[typing.List["GroupsGroupFull"]] = None
    profiles: typing.Optional[typing.List["UsersUserFull"]] = None


class MessagesGetConversationMembers(BaseModel):
    """VK Object MessagesGetConversationMembers

    chat_restrictions -
    count - Chat members count
    groups -
    items -
    profiles -
    """

    chat_restrictions: typing.Optional["MessagesChatRestrictions"] = None
    count: int = None
    groups: typing.Optional[typing.List["GroupsGroupFull"]] = None
    items: typing.List["MessagesConversationMember"] = None
    profiles: typing.Optional[typing.List["UsersUserFull"]] = None


class MessagesGraffiti(BaseModel):
    """VK Object MessagesGraffiti

    access_key - Access key for graffiti
    height - Graffiti height
    id - Graffiti ID
    owner_id - Graffiti owner ID
    url - Graffiti URL
    width - Graffiti width
    """

    access_key: typing.Optional[str] = None
    height: int = None
    id: int = None
    owner_id: int = None
    url: str = None
    width: int = None


class MessagesHistoryAttachment(BaseModel):
    """VK Object MessagesHistoryAttachment

    attachment -
    forward_level - Forward level (optional)
    from_id - Message author's ID
    message_id - Message ID
    """

    attachment: "MessagesHistoryMessageAttachment" = None
    forward_level: typing.Optional[int] = None
    from_id: int = None
    message_id: int = None


class MessagesHistoryMessageAttachment(BaseModel):
    """VK Object MessagesHistoryMessageAttachment"""

    audio: typing.Optional["AudioAudio"] = None
    audio_message: typing.Optional["MessagesAudioMessage"] = None
    doc: typing.Optional["DocsDoc"] = None
    graffiti: typing.Optional["MessagesGraffiti"] = None
    link: typing.Optional["BaseLink"] = None
    market: typing.Optional["BaseLink"] = None
    photo: typing.Optional["PhotosPhoto"] = None
    share: typing.Optional["BaseLink"] = None
    type: "MessagesHistoryMessageAttachmentType" = None
    video: typing.Optional["VideoVideo"] = None
    wall: typing.Optional["BaseLink"] = None


class MessagesHistoryMessageAttachmentType(enum.Enum):
    """ Attachments type """

    PHOTO = "photo"
    VIDEO = "video"
    AUDIO = "audio"
    DOC = "doc"
    LINK = "link"
    MARKET = "market"
    WALL = "wall"
    SHARE = "share"
    GRAFFITI = "graffiti"
    AUDIO_MESSAGE = "audio_message"


class MessagesKeyboard(BaseModel):
    """VK Object MessagesKeyboard

    author_id - Community or bot, which set this keyboard
    buttons -
    inline -
    one_time - Should this keyboard disappear on first use
    """

    author_id: typing.Optional[int] = None
    buttons: typing.List["list"] = None
    inline: typing.Optional[bool] = None
    one_time: bool = None


class ButtonColor(enum.Enum):
    """ Button color """

    DEFAULT = "default"
    POSITIVE = "positive"
    NEGATIVE = "negative"
    PRIMARY = "primary"


class MessagesKeyboardButton(BaseModel):
    """VK Object MessagesKeyboardButton

    action -
    color - Button color
    """

    action: "MessagesKeyboardButtonPropertyAction" = None
    color: typing.Optional["ButtonColor"] = None


class MessagesKeyboardButtonActionCallbackType(enum.Enum):
    """ MessagesKeyboardButtonActionCallbackType enum """

    CALLBACK = "callback"


class MessagesKeyboardButtonActionCallback(BaseModel):
    """VK Object MessagesKeyboardButtonActionCallback

    label - Label for button
    payload - Additional data sent along with message for developer convenience
    type -
    """

    label: str = None
    payload: typing.Optional[str] = None
    type: "MessagesKeyboardButtonActionCallbackType" = None


class MessagesKeyboardButtonActionLocationType(enum.Enum):
    """ MessagesKeyboardButtonActionLocationType enum """

    LOCATION = "location"


class MessagesKeyboardButtonActionLocation(BaseModel):
    """VK Object MessagesKeyboardButtonActionLocation

    payload - Additional data sent along with message for developer convenience
    type -
    """

    payload: typing.Optional[str] = None
    type: "MessagesKeyboardButtonActionLocationType" = None


class MessagesKeyboardButtonActionOpenAppType(enum.Enum):
    """ MessagesKeyboardButtonActionOpenAppType enum """

    OPEN_APP = "open_app"


class MessagesKeyboardButtonActionOpenApp(BaseModel):
    """VK Object MessagesKeyboardButtonActionOpenApp

    app_id - Fragment value in app link like vk.com/app{app_id}_-654321#hash
    hash - Fragment value in app link like vk.com/app123456_-654321#{hash}
    label - Label for button
    owner_id - Fragment value in app link like vk.com/app123456_{owner_id}#hash
    payload - Additional data sent along with message for developer convenience
    type -
    """

    app_id: int = None
    hash: typing.Optional[str] = None
    label: str = None
    owner_id: int = None
    payload: typing.Optional[str] = None
    type: "MessagesKeyboardButtonActionOpenAppType" = None


class MessagesKeyboardButtonActionOpenLinkType(enum.Enum):
    """ MessagesKeyboardButtonActionOpenLinkType enum """

    OPEN_LINK = "open_link"


class MessagesKeyboardButtonActionOpenLink(BaseModel):
    """VK Object MessagesKeyboardButtonActionOpenLink

    label - Label for button
    link - link for button
    payload - Additional data sent along with message for developer convenience
    type -
    """

    label: str = None
    link: str = None
    payload: typing.Optional[str] = None
    type: "MessagesKeyboardButtonActionOpenLinkType" = None


class MessagesKeyboardButtonActionOpenPhotoType(enum.Enum):
    """ MessagesKeyboardButtonActionOpenPhotoType enum """

    OPEN_PHOTO = "open_photo"


class MessagesKeyboardButtonActionOpenPhoto(BaseModel):
    """VK Object MessagesKeyboardButtonActionOpenPhoto"""

    type: "MessagesKeyboardButtonActionOpenPhotoType" = None


class MessagesKeyboardButtonActionTextType(enum.Enum):
    """ MessagesKeyboardButtonActionTextType enum """

    TEXT = "text"


class MessagesKeyboardButtonActionText(BaseModel):
    """VK Object MessagesKeyboardButtonActionText

    label - Label for button
    payload - Additional data sent along with message for developer convenience
    type -
    """

    label: str = None
    payload: typing.Optional[str] = None
    type: "MessagesKeyboardButtonActionTextType" = None


class MessagesKeyboardButtonActionVkpayType(enum.Enum):
    """ MessagesKeyboardButtonActionVkpayType enum """

    VKPAY = "vkpay"


class MessagesKeyboardButtonActionVkpay(BaseModel):
    """VK Object MessagesKeyboardButtonActionVkpay

    hash - Fragment value in app link like vk.com/app123456_-654321#{hash}
    payload - Additional data sent along with message for developer convenience
    type -
    """

    hash: str = None
    payload: typing.Optional[str] = None
    type: "MessagesKeyboardButtonActionVkpayType" = None


class MessagesKeyboardButtonPropertyAction(
    MessagesKeyboardButtonActionLocation,
    MessagesKeyboardButtonActionOpenApp,
    MessagesKeyboardButtonActionOpenLink,
    MessagesKeyboardButtonActionOpenPhoto,
    MessagesKeyboardButtonActionText,
    MessagesKeyboardButtonActionCallback,
    MessagesKeyboardButtonActionVkpay
):
    """VK Object MessagesKeyboardButtonPropertyAction"""

    pass


class MessagesLastActivity(BaseModel):
    """VK Object MessagesLastActivity

    online - Information whether user is online
    time - Time when user was online in Unixtime
    """

    online: "BaseBoolInt" = None
    time: int = None


class MessagesLongpollMessages(BaseModel):
    """VK Object MessagesLongpollMessages

    count - Total number
    items -
    """

    count: typing.Optional[int] = None
    items: typing.Optional[typing.List["MessagesMessage"]] = None


class MessagesLongpollParams(BaseModel):
    """VK Object MessagesLongpollParams

    key - Key
    pts - Persistent timestamp
    server - Server URL
    ts - Timestamp
    """

    key: str = None
    pts: typing.Optional[int] = None
    server: str = None
    ts: int = None


class MessagesMessage(BaseModel):
    """VK Object MessagesMessage

    action -
    admin_author_id - Only for messages from community. Contains user ID of community admin, who sent this message.
    attachments -
    conversation_message_id - Unique auto-incremented number for all messages with this peer
    date - Date when the message has been sent in Unixtime
    deleted - Is it an deleted message
    from_id - Message author's ID
    fwd_messages - Forwarded messages
    geo -
    id - Message ID
    important - Is it an important message
    is_cropped - this message is cropped for bot
    is_hidden -
    is_silent - Is silent message, push without sound
    keyboard -
    members_count - Members number
    out - Information whether the message is outcoming
    payload -
    peer_id - Peer ID
    pinned_at - Date when the message has been pinned in Unixtime
    random_id - ID used for sending messages. It returned only for outgoing messages
    ref -
    ref_source -
    reply_message -
    text - Message text
    update_time - Date when the message has been updated in Unixtime
    was_listened - Was the audio message inside already listened by you
    """

    action: typing.Optional["MessagesMessageAction"] = None
    admin_author_id: typing.Optional[int] = None
    attachments: typing.Optional[typing.List["MessagesMessageAttachment"]] = None
    conversation_message_id: typing.Optional[int] = None
    date: int = None
    deleted: typing.Optional["BaseBoolInt"] = None
    from_id: int = None
    fwd_messages: typing.Optional[typing.List["MessagesForeignMessage"]] = None
    geo: typing.Optional["BaseGeo"] = None
    id: int = None
    important: typing.Optional[bool] = None
    is_cropped: typing.Optional[bool] = None
    is_hidden: typing.Optional[bool] = None
    is_silent: typing.Optional[bool] = None
    keyboard: typing.Optional["MessagesKeyboard"] = None
    members_count: typing.Optional[int] = None
    out: "BaseBoolInt" = None
    payload: typing.Optional[str] = None
    peer_id: int = None
    pinned_at: typing.Optional[int] = None
    random_id: typing.Optional[int] = None
    ref: typing.Optional[str] = None
    ref_source: typing.Optional[str] = None
    reply_message: typing.Optional["MessagesForeignMessage"] = None
    text: str = None
    update_time: typing.Optional[int] = None
    was_listened: typing.Optional[bool] = None

    @property
    def chat_id(self) -> int:
        return self.peer_id - 2_000_000_000

    @property
    def message_id(self) -> int:
        return self.conversation_message_id or self.id

    def get_wall_attachment(self) -> typing.List["WallWallpostFull"]:
        result = [attachment.wall for attachment in self.attachments if attachment.wall]
        return result if result else None

    def get_wall_reply_attachment(self) -> typing.List["WallWallComment"]:
        result = [
            attachment.wall_reply
            for attachment in self.attachments
            if attachment.wall_reply
        ]
        return result if result else None

    def get_photo_attachments(self) -> typing.List["PhotosPhoto"]:
        return [attachment.photo for attachment in self.attachments if attachment.photo]

    def get_video_attachments(self) -> typing.List["VideoVideo"]:
        return [attachment.video for attachment in self.attachments if attachment.video]

    def get_doc_attachments(self) -> typing.List["DocsDoc"]:
        return [attachment.doc for attachment in self.attachments if attachment.doc]

    def get_audio_attachments(self) -> typing.List["AudioAudio"]:
        return [attachment.audio for attachment in self.attachments if attachment.audio]

    def get_message_id(self) -> int:
        return self.id or self.conversation_message_id

    def get_payload_json(
        self,
        throw_error: bool = False,
        unpack_failure: typing.Callable[[str], dict] = lambda payload: payload,
        json: typing.Any = __import__("json"),
    ) -> typing.Union[dict, None]:
        try:
            return json.loads(self.payload)
        except (json.decoder.JSONDecodeError, TypeError) as e:
            if throw_error:
                raise e
        return unpack_failure(self.payload)


class MessagesMessageAction(BaseModel):
    """VK Object MessagesMessageAction

    conversation_message_id - Message ID
    email - Email address for chat_invite_user or chat_kick_user actions
    member_id - User or email peer ID
    message - Message body of related message
    photo -
    text - New chat title for chat_create and chat_title_update actions
    type -
    """

    conversation_message_id: typing.Optional[int] = None
    email: typing.Optional[str] = None
    member_id: typing.Optional[int] = None
    message: typing.Optional[str] = None
    photo: typing.Optional["MessagesMessageActionPhoto"] = None
    text: typing.Optional[str] = None
    type: "MessagesMessageActionStatus" = None
    style: typing.Optional[str] = None


class MessagesMessageActionPhoto(BaseModel):
    """VK Object MessagesMessageActionPhoto

    photo_100 - URL of the preview image with 100px in width
    photo_200 - URL of the preview image with 200px in width
    photo_50 - URL of the preview image with 50px in width
    """

    photo_100: str = None
    photo_200: str = None
    photo_50: str = None


class MessagesMessageActionStatus(enum.Enum):
    """ Action status """

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
    CONVERSATION_STYLE_UPDATE = "conversation_style_update"


class MessagesMessageAttachment(BaseModel):
    """VK Object MessagesMessageAttachment"""

    audio: typing.Optional["AudioAudio"] = None
    audio_message: typing.Optional["MessagesAudioMessage"] = None
    call: typing.Optional["CallsCall"] = None
    doc: typing.Optional["DocsDoc"] = None
    gift: typing.Optional["GiftsLayout"] = None
    graffiti: typing.Optional["MessagesGraffiti"] = None
    group_call_in_progress: typing.Optional["GroupCallInProgress"] = None
    link: typing.Optional["BaseLink"] = None
    market: typing.Optional["MarketMarketItem"] = None
    market_market_album: typing.Optional["MarketMarketAlbum"] = None
    photo: typing.Optional["PhotosPhoto"] = None
    poll: typing.Optional["PollsPoll"] = None
    sticker: typing.Optional["BaseSticker"] = None
    story: typing.Optional["StoriesStory"] = None
    type: "MessagesMessageAttachmentType" = None
    video: typing.Optional["VideoVideo"] = None
    wall: typing.Optional["WallWallpostFull"] = None
    wall_reply: typing.Optional["WallWallComment"] = None


class MessagesMessageAttachmentType(enum.Enum):
    """ Attachment type """

    PHOTO = "photo"
    AUDIO = "audio"
    VIDEO = "video"
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
    STORY = "story"
    GROUP_CALL_IN_PROGRESS = "group_call_in_progress"


class MessagesMessageRequestData(BaseModel):
    """VK Object MessagesMessageRequestData

    inviter_id - Message request sender id
    request_date - Message request date
    status - Status of message request
    """

    inviter_id: typing.Optional[int] = None
    request_date: typing.Optional[int] = None
    status: typing.Optional[str] = None


class MessagesMessagesArray(BaseModel):
    """VK Object MessagesMessagesArray"""

    count: typing.Optional[int] = None
    items: typing.Optional[typing.List["MessagesMessage"]] = None


class MessagesOutReadBy(BaseModel):
    """VK Object MessagesOutReadBy"""

    count: typing.Optional[int] = None
    member_ids: typing.Optional[typing.List[int]] = None


class MessagesPinnedMessage(BaseModel):
    """VK Object MessagesPinnedMessage

    attachments -
    conversation_message_id - Unique auto-incremented number for all messages with this peer
    date - Date when the message has been sent in Unixtime
    from_id - Message author's ID
    fwd_messages - Forwarded messages
    geo -
    id - Message ID
    keyboard -
    peer_id - Peer ID
    reply_message -
    text - Message text
    """

    attachments: typing.Optional[typing.List["MessagesMessageAttachment"]] = None
    conversation_message_id: typing.Optional[int] = None
    date: int = None
    from_id: int = None
    fwd_messages: typing.Optional[typing.List["MessagesForeignMessage"]] = None
    geo: typing.Optional["BaseGeo"] = None
    id: int = None
    keyboard: typing.Optional["MessagesKeyboard"] = None
    peer_id: int = None
    reply_message: typing.Optional["MessagesForeignMessage"] = None
    text: str = None


class MessagesPushSettings(BaseModel):
    """VK Object MessagesPushSettings

    disabled_forever - Information whether push notifications are disabled forever
    disabled_mass_mentions - Information whether the mass mentions (like '@all', '@online') are disabled
    disabled_mentions - Information whether the mentions are disabled
    disabled_until - Time until what notifications are disabled
    no_sound - Information whether the sound is on
    """

    disabled_forever: bool = None
    disabled_mass_mentions: typing.Optional[bool] = None
    disabled_mentions: typing.Optional[bool] = None
    disabled_until: typing.Optional[int] = None
    no_sound: bool = None


class MessagesSendUserIdsResponseItem(BaseModel):
    """VK Object MessagesSendUserIdsResponseItem"""

    conversation_message_id: typing.Optional[int] = None
    error: typing.Optional["BaseMessageError"] = None
    message_id: int = None
    peer_id: int = None


class MessagesTemplateActionTypeNames(enum.Enum):
    """ Template action type names """

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


class UsersUserXtrType(UsersUser):
    """VK Object UsersUserXtrType"""

    type: typing.Optional["UsersUserType"] = None


class MessagesUserXtrInvitedBy(UsersUserXtrType):
    """VK Object MessagesUserXtrInvitedBy

    invited_by - ID of the inviter
    """

    invited_by: typing.Optional[int] = None


class NewsfeedCommentsFilters(enum.Enum):
    """ NewsfeedCommentsFilters enum """

    POST = "post"
    PHOTO = "photo"
    VIDEO = "video"
    TOPIC = "topic"
    NOTE = "note"


class NewsfeedIgnoreItemType(enum.Enum):
    """ NewsfeedIgnoreItemType enum """

    WALL = "wall"
    TAG = "tag"
    PROFILEPHOTO = "profilephoto"
    VIDEO = "video"
    PHOTO = "photo"
    AUDIO = "audio"


class NewsfeedItemBase(BaseModel):
    """VK Object NewsfeedItemBase

    date - Date when item has been added in Unixtime
    source_id - Item source ID
    type -
    """

    date: int = None
    source_id: int = None
    type: "NewsfeedNewsfeedItemType" = None


class NewsfeedItemAudio(NewsfeedItemBase):
    """VK Object NewsfeedItemAudio

    audio -
    post_id - Post ID
    """

    audio: typing.Optional["NewsfeedItemAudioAudio"] = None
    post_id: typing.Optional[int] = None


class NewsfeedItemAudioAudio(BaseModel):
    """VK Object NewsfeedItemAudioAudio

    count - Audios number
    items -
    """

    count: typing.Optional[int] = None
    items: typing.Optional[typing.List["AudioAudio"]] = None


class NewsfeedItemDigest(NewsfeedItemBase):
    """VK Object NewsfeedItemDigest

    feed_id - id of feed in digest
    footer -
    header -
    items -
    main_post_ids -
    template - type of digest
    track_code -
    """

    feed_id: typing.Optional[str] = None
    footer: typing.Optional["NewsfeedItemDigestFooter"] = None
    header: typing.Optional["NewsfeedItemDigestHeader"] = None
    items: typing.Optional[typing.List["NewsfeedItemDigestItem"]] = None
    main_post_ids: typing.Optional[typing.List[str]] = None
    template: typing.Optional[str] = None
    track_code: typing.Optional[str] = None


class NewsfeedItemDigestButtonStyle(enum.Enum):
    """ NewsfeedItemDigestButtonStyle enum """

    PRIMARY = "primary"


class NewsfeedItemDigestButton(BaseModel):
    """VK Object NewsfeedItemDigestButton"""

    style: typing.Optional["NewsfeedItemDigestButtonStyle"] = None
    title: str = None


class NewsfeedItemDigestFooterStyle(enum.Enum):
    """ NewsfeedItemDigestFooterStyle enum """

    TEXT = "text"
    BUTTON = "button"


class NewsfeedItemDigestFooter(BaseModel):
    """VK Object NewsfeedItemDigestFooter

    button -
    style -
    text - text for invite to enable smart feed
    """

    button: typing.Optional["NewsfeedItemDigestButton"] = None
    style: "NewsfeedItemDigestFooterStyle" = None
    text: str = None


class NewsfeedItemDigestFullItemStyle(enum.Enum):
    """ NewsfeedItemDigestFullItemStyle enum """

    DEFAULT = "default"
    INVERSED = "inversed"
    SPOTLIGHT = "spotlight"


class NewsfeedItemDigestFullItem(BaseModel):
    """VK Object NewsfeedItemDigestFullItem"""

    attachment: typing.Optional["WallWallpostAttachment"] = None
    attachment_index: typing.Optional[int] = None
    post: "WallWallpost" = None
    source_name: typing.Optional[str] = None
    style: typing.Optional["NewsfeedItemDigestFullItemStyle"] = None
    text: typing.Optional[str] = None


class NewsfeedItemDigestHeaderStyle(enum.Enum):
    """ NewsfeedItemDigestHeaderStyle enum """

    SINGLELINE = "singleline"
    MULTILINE = "multiline"


class NewsfeedItemDigestHeader(BaseModel):
    """VK Object NewsfeedItemDigestHeader

    button -
    style -
    subtitle - Subtitle of the header, when title have two strings
    title - Title of the header
    """

    button: typing.Optional["NewsfeedItemDigestButton"] = None
    style: "NewsfeedItemDigestHeaderStyle" = None
    subtitle: typing.Optional[str] = None
    title: str = None


class WallWallpost(BaseModel):
    """VK Object WallWallpost

    access_key - Access key to private object
    attachments -
    copyright - Information about the source of the post
    date - Date of publishing in Unixtime
    edited - Date of editing in Unixtime
    from_id - Post author ID
    geo -
    id - Post ID
    is_archived - Is post archived, only for post owners
    is_deleted -
    is_favorite - Information whether the post in favorites list
    likes - Count of likes
    owner_id - Wall owner's ID
    parents_stack - If post type 'reply', contains original parent IDs stack
    post_id - If post type 'reply', contains original post ID
    post_source -
    post_type -
    reposts -
    signer_id - Post signer ID
    text - Post text
    views - Count of views
    """

    access_key: typing.Optional[str] = None
    attachments: typing.Optional[typing.List["WallWallpostAttachment"]] = None
    copyright: typing.Optional["WallPostCopyright"] = None
    date: typing.Optional[int] = None
    edited: typing.Optional[int] = None
    from_id: typing.Optional[int] = None
    geo: typing.Optional["WallGeo"] = None
    id: typing.Optional[int] = None
    is_archived: typing.Optional[bool] = None
    is_deleted: typing.Optional[bool] = None
    is_favorite: typing.Optional[bool] = None
    likes: typing.Optional["BaseLikesInfo"] = None
    owner_id: typing.Optional[int] = None
    parents_stack: typing.Optional[typing.List[int]] = None
    post_id: typing.Optional[int] = None
    post_source: typing.Optional["WallPostSource"] = None
    post_type: typing.Optional["WallPostType"] = None
    reposts: typing.Optional["BaseRepostsInfo"] = None
    signer_id: typing.Optional[int] = None
    text: typing.Optional[str] = None
    views: typing.Optional["WallViews"] = None


class NewsfeedItemDigestItem(WallWallpost):
    """VK Object NewsfeedItemDigestItem"""

    pass


class NewsfeedItemFriend(NewsfeedItemBase):
    """VK Object NewsfeedItemFriend"""

    friends: typing.Optional["NewsfeedItemFriendFriends"] = None


class NewsfeedItemFriendFriends(BaseModel):
    """VK Object NewsfeedItemFriendFriends

    count - Number of friends has been added
    items -
    """

    count: typing.Optional[int] = None
    items: typing.Optional[typing.List["BaseUserId"]] = None


class NewsfeedItemHolidayRecommendationsBlockHeader(BaseModel):
    """VK Object NewsfeedItemHolidayRecommendationsBlockHeader

    action -
    image -
    subtitle - Subtitle of the header
    title - Title of the header
    """

    action: typing.Optional["BaseLinkButtonAction"] = None
    image: typing.Optional[typing.List["BaseImage"]] = None
    subtitle: typing.Optional[str] = None
    title: typing.Optional[str] = None


class WallCarouselBase(BaseModel):
    """VK Object WallCarouselBase

    carousel_offset - Index of current carousel element
    """

    carousel_offset: typing.Optional[int] = None


class NewsfeedItemPhoto(WallCarouselBase, NewsfeedItemBase):
    """VK Object NewsfeedItemPhoto

    photos -
    post_id - Post ID
    """

    photos: typing.Optional["NewsfeedItemPhotoPhotos"] = None
    post_id: typing.Optional[int] = None


class NewsfeedItemPhotoPhotos(BaseModel):
    """VK Object NewsfeedItemPhotoPhotos

    count - Photos number
    items -
    """

    count: typing.Optional[int] = None
    items: typing.Optional[typing.List["NewsfeedNewsfeedPhoto"]] = None


class NewsfeedItemPhotoTag(WallCarouselBase, NewsfeedItemBase):
    """VK Object NewsfeedItemPhotoTag

    photo_tags -
    post_id - Post ID
    """

    photo_tags: typing.Optional["NewsfeedItemPhotoTagPhotoTags"] = None
    post_id: typing.Optional[int] = None


class NewsfeedItemPhotoTagPhotoTags(BaseModel):
    """VK Object NewsfeedItemPhotoTagPhotoTags

    count - Tags number
    items -
    """

    count: typing.Optional[int] = None
    items: typing.Optional[typing.List["NewsfeedNewsfeedPhoto"]] = None


class NewsfeedItemPromoButton(NewsfeedItemBase):
    """VK Object NewsfeedItemPromoButton"""

    action: typing.Optional["NewsfeedItemPromoButtonAction"] = None
    images: typing.Optional[typing.List["NewsfeedItemPromoButtonImage"]] = None
    text: typing.Optional[str] = None
    title: typing.Optional[str] = None
    track_code: typing.Optional[str] = None


class NewsfeedItemPromoButtonAction(BaseModel):
    """VK Object NewsfeedItemPromoButtonAction"""

    target: typing.Optional[str] = None
    type: typing.Optional[str] = None
    url: typing.Optional[str] = None


class NewsfeedItemPromoButtonImage(BaseModel):
    """VK Object NewsfeedItemPromoButtonImage"""

    height: typing.Optional[int] = None
    url: typing.Optional[str] = None
    width: typing.Optional[int] = None


class NewsfeedItemTopic(NewsfeedItemBase):
    """VK Object NewsfeedItemTopic

    comments -
    likes -
    post_id - Topic post ID
    text - Post text
    """

    comments: typing.Optional["BaseCommentsInfo"] = None
    likes: typing.Optional["BaseLikesInfo"] = None
    post_id: typing.Optional[int] = None
    text: typing.Optional[str] = None


class NewsfeedItemVideo(WallCarouselBase, NewsfeedItemBase):
    """VK Object NewsfeedItemVideo"""

    video: typing.Optional["NewsfeedItemVideoVideo"] = None


class NewsfeedItemVideoVideo(BaseModel):
    """VK Object NewsfeedItemVideoVideo

    count - Tags number
    items -
    """

    count: typing.Optional[int] = None
    items: typing.Optional[typing.List["VideoVideo"]] = None


class WallWallpostFull(WallCarouselBase, WallWallpost):
    """VK Object WallWallpostFull

    can_delete - Information whether current user can delete the post
    can_edit - Information whether current user can edit the post
    can_pin - Information whether current user can pin the post
    comments -
    copy_history -
    created_by - Post creator ID (if post still can be edited)
    donut -
    hash - Hash for sharing
    is_pinned - Information whether the post is pinned
    marked_as_ads - Information whether the post is marked as ads
    short_text_rate - Preview length control parameter
    topic_id - Topic ID. Allowed values can be obtained from newsfeed.getPostTopics method
    """

    can_delete: typing.Optional["BaseBoolInt"] = None
    can_edit: typing.Optional["BaseBoolInt"] = None
    can_pin: typing.Optional["BaseBoolInt"] = None
    comments: typing.Optional["BaseCommentsInfo"] = None
    copy_history: typing.Optional[typing.List["WallWallpostFull"]] = None
    created_by: typing.Optional[int] = None
    donut: typing.Optional["WallWallpostDonut"] = None
    hash: typing.Optional[str] = None
    is_pinned: typing.Optional[int] = None
    marked_as_ads: typing.Optional["BaseBoolInt"] = None
    short_text_rate: typing.Optional[float] = None
    topic_id: typing.Optional[int] = None


class NewsfeedItemWallpost(WallWallpostFull):
    """VK Object NewsfeedItemWallpost"""

    feedback: typing.Optional["NewsfeedItemWallpostFeedback"] = None


class NewsfeedItemWallpostFeedback(BaseModel):
    """VK Object NewsfeedItemWallpostFeedback"""

    answers: typing.Optional[typing.List["NewsfeedItemWallpostFeedbackAnswer"]] = None
    gratitude: typing.Optional[str] = None
    question: str = None
    stars_count: typing.Optional[int] = None
    type: "NewsfeedItemWallpostFeedbackType" = None


class NewsfeedItemWallpostFeedbackAnswer(BaseModel):
    """VK Object NewsfeedItemWallpostFeedbackAnswer"""

    id: str = None
    title: str = None


class NewsfeedItemWallpostFeedbackType(enum.Enum):
    """ NewsfeedItemWallpostFeedbackType enum """

    BUTTONS = "buttons"
    STARS = "stars"


class NewsfeedList(BaseModel):
    """VK Object NewsfeedList

    id - List ID
    title - List title
    """

    id: int = None
    title: str = None


class NewsfeedListFull(NewsfeedList):
    """VK Object NewsfeedListFull

    no_reposts - Information whether reposts hiding is enabled
    source_ids -
    """

    no_reposts: typing.Optional["BaseBoolInt"] = None
    source_ids: typing.Optional[typing.List[int]] = None


class NewsfeedNewsfeedItem(
    NewsfeedItemWallpost,
    NewsfeedItemPhoto,
    NewsfeedItemPhotoTag,
    NewsfeedItemFriend,
    NewsfeedItemAudio,
    NewsfeedItemVideo,
    NewsfeedItemTopic,
    NewsfeedItemDigest,
    NewsfeedItemPromoButton
):
    """VK Object NewsfeedNewsfeedItem"""

    pass


class NewsfeedNewsfeedItemType(enum.Enum):
    """ Item type """

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


class PhotosPhoto(BaseModel):
    """VK Object PhotosPhoto

    access_key - Access key for the photo
    album_id - Album ID
    can_comment - Information whether current user can comment the photo
    date - Date when uploaded
    has_tags - Whether photo has attached tag links
    height - Original photo height
    id - Photo ID
    images -
    lat - Latitude
    long - Longitude
    owner_id - Photo owner's ID
    photo_256 - URL of image with 2560 px width
    place -
    post_id - Post ID
    sizes -
    text - Photo caption
    user_id - ID of the user who have uploaded the photo
    width - Original photo width
    """

    access_key: typing.Optional[str] = None
    album_id: int = None
    can_comment: typing.Optional["BaseBoolInt"] = None
    date: int = None
    has_tags: bool = None
    height: typing.Optional[int] = None
    id: int = None
    images: typing.Optional[typing.List["PhotosImage"]] = None
    lat: typing.Optional[float] = None
    long: typing.Optional[float] = None
    owner_id: int = None
    photo_256: typing.Optional[str] = None
    place: typing.Optional[str] = None
    post_id: typing.Optional[int] = None
    sizes: typing.Optional[typing.List["PhotosPhotoSizes"]] = None
    text: typing.Optional[str] = None
    user_id: typing.Optional[int] = None
    width: typing.Optional[int] = None


class NewsfeedNewsfeedPhoto(PhotosPhoto):
    """VK Object NewsfeedNewsfeedPhoto

    can_repost - Information whether current user can repost the photo
    comments -
    likes -
    """

    can_repost: typing.Optional["BaseBoolInt"] = None
    comments: typing.Optional["BaseObjectCount"] = None
    likes: typing.Optional["BaseLikes"] = None


class NotesNote(BaseModel):
    """VK Object NotesNote

    can_comment - Information whether current user can comment the note
    comments - Comments number
    date - Date when the note has been created in Unixtime
    id - Note ID
    owner_id - Note owner's ID
    privacy_comment -
    privacy_view -
    read_comments -
    text - Note text
    text_wiki - Note text in wiki format
    title - Note title
    view_url - URL of the page with note preview
    """

    can_comment: typing.Optional["BaseBoolInt"] = None
    comments: int = None
    date: int = None
    id: int = None
    owner_id: int = None
    privacy_comment: typing.Optional[typing.List[str]] = None
    privacy_view: typing.Optional[typing.List[str]] = None
    read_comments: typing.Optional[int] = None
    text: typing.Optional[str] = None
    text_wiki: typing.Optional[str] = None
    title: str = None
    view_url: str = None


class NotesNoteComment(BaseModel):
    """VK Object NotesNoteComment

    date - Date when the comment has beed added in Unixtime
    id - Comment ID
    message - Comment text
    nid - Note ID
    oid - Note ID
    reply_to - ID of replied comment
    uid - Comment author's ID
    """

    date: int = None
    id: int = None
    message: str = None
    nid: int = None
    oid: int = None
    reply_to: typing.Optional[int] = None
    uid: int = None


class NotificationsFeedback(BaseModel):
    """VK Object NotificationsFeedback

    attachments -
    from_id - Reply author's ID
    geo -
    id - Item ID
    likes -
    text - Reply text
    to_id - Wall owner's ID
    """

    attachments: typing.Optional[typing.List["WallWallpostAttachment"]] = None
    from_id: typing.Optional[int] = None
    geo: typing.Optional["BaseGeo"] = None
    id: typing.Optional[int] = None
    likes: typing.Optional["BaseLikesInfo"] = None
    text: typing.Optional[str] = None
    to_id: typing.Optional[int] = None


class NotificationsNotification(BaseModel):
    """VK Object NotificationsNotification

    date - Date when the event has been occurred
    feedback -
    parent -
    reply -
    type - Notification type
    """

    date: typing.Optional[int] = None
    feedback: typing.Optional["NotificationsFeedback"] = None
    parent: typing.Optional["NotificationsNotification"] = None
    reply: typing.Optional["NotificationsReply"] = None
    type: typing.Optional[str] = None


class NotificationsNotificationItem(NotificationsNotification):
    """VK Object NotificationsNotificationItem"""

    pass


class WallWallpostToId(BaseModel):
    """VK Object WallWallpostToId

    attachments -
    comments -
    copy_owner_id - ID of the source post owner
    copy_post_id - ID of the source post
    date - Date of publishing in Unixtime
    from_id - Post author ID
    geo -
    id - Post ID
    is_favorite - Information whether the post in favorites list
    likes -
    post_id - wall post ID (if comment)
    post_source -
    post_type -
    reposts -
    signer_id - Post signer ID
    text - Post text
    to_id - Wall owner's ID
    """

    attachments: typing.Optional[typing.List["WallWallpostAttachment"]] = None
    comments: typing.Optional["BaseCommentsInfo"] = None
    copy_owner_id: typing.Optional[int] = None
    copy_post_id: typing.Optional[int] = None
    date: typing.Optional[int] = None
    from_id: typing.Optional[int] = None
    geo: typing.Optional["WallGeo"] = None
    id: typing.Optional[int] = None
    is_favorite: typing.Optional[bool] = None
    likes: typing.Optional["BaseLikesInfo"] = None
    post_id: typing.Optional[int] = None
    post_source: typing.Optional["WallPostSource"] = None
    post_type: typing.Optional["WallPostType"] = None
    reposts: typing.Optional["BaseRepostsInfo"] = None
    signer_id: typing.Optional[int] = None
    text: typing.Optional[str] = None
    to_id: typing.Optional[int] = None


class VideoVideo(BaseModel):
    """VK Object VideoVideo

    access_key - Video access key
    added - 1 if video is added to user's albums
    adding_date - Date when the video has been added in Unixtime
    balance - Live donations balance
    can_add - Information whether current user can add the video
    can_add_to_faves - Information whether current user can add the video to favourites
    can_attach_link - Information whether current user can attach action button to the video
    can_comment - Information whether current user can comment the video
    can_edit - Information whether current user can edit the video
    can_like - Information whether current user can like the video
    can_repost - Information whether current user can repost the video
    can_subscribe - Information whether current user can subscribe to author of the video
    comments - Number of comments
    content_restricted - Restriction code
    content_restricted_message - Restriction text
    converting - 1 if  video is being converted
    date - Date when video has been uploaded in Unixtime
    description - Video description
    duration - Video duration in seconds
    first_frame -
    height - Video height
    id - Video ID
    image -
    is_favorite - Whether video is added to bookmarks
    is_private - 1 if video is private
    is_subscribed - 1 if user is subscribed to author of the video
    likes -
    live - 1 if the video is a live stream
    live_notify - Whether current user is subscribed to the upcoming live stream notification (if not subscribed to the author)
    live_start_time - Date in Unixtime when the live stream is scheduled to start by the author
    live_status - Live stream status
    local_views - If video is external, number of views on vk
    owner_id - Video owner ID
    platform - External platform
    player - Video embed URL
    processing - Returns if the video is processing
    repeat - Information whether the video is repeated
    reposts -
    spectators - Number of spectators of the stream
    title - Video title
    track_code -
    type -
    upcoming - 1 if the video is an upcoming stream
    user_id - Id of the user who uploaded the video if it was uploaded to a group by member
    views - Number of views
    width - Video width
    """

    access_key: typing.Optional[str] = None
    added: typing.Optional["BaseBoolInt"] = None
    adding_date: typing.Optional[int] = None
    balance: typing.Optional[int] = None
    can_add: typing.Optional["BaseBoolInt"] = None
    can_add_to_faves: typing.Optional["BaseBoolInt"] = None
    can_attach_link: typing.Optional["BaseBoolInt"] = None
    can_comment: typing.Optional["BaseBoolInt"] = None
    can_edit: typing.Optional["BaseBoolInt"] = None
    can_like: typing.Optional["BaseBoolInt"] = None
    can_repost: typing.Optional["BaseBoolInt"] = None
    can_subscribe: typing.Optional["BaseBoolInt"] = None
    comments: typing.Optional[int] = None
    content_restricted: typing.Optional[int] = None
    content_restricted_message: typing.Optional[str] = None
    converting: typing.Optional["BaseBoolInt"] = None
    date: typing.Optional[int] = None
    description: typing.Optional[str] = None
    duration: typing.Optional[int] = None
    first_frame: typing.Optional[typing.List["VideoVideoImage"]] = None
    height: typing.Optional[int] = None
    id: typing.Optional[int] = None
    image: typing.Optional[typing.List["VideoVideoImage"]] = None
    is_favorite: typing.Optional[bool] = None
    is_private: typing.Optional["BaseBoolInt"] = None
    is_subscribed: typing.Optional["BaseBoolInt"] = None
    likes: typing.Optional["BaseLikes"] = None
    live: typing.Optional["BasePropertyExists"] = None
    live_notify: typing.Optional["BaseBoolInt"] = None
    live_start_time: typing.Optional[int] = None
    live_status: typing.Optional[str] = None
    local_views: typing.Optional[int] = None
    owner_id: typing.Optional[int] = None
    platform: typing.Optional[str] = None
    player: typing.Optional[str] = None
    processing: typing.Optional["BasePropertyExists"] = None
    repeat: typing.Optional["BasePropertyExists"] = None
    reposts: typing.Optional["BaseRepostsInfo"] = None
    spectators: typing.Optional[int] = None
    title: typing.Optional[str] = None
    track_code: typing.Optional[str] = None
    type: typing.Optional[str] = None
    upcoming: typing.Optional["BasePropertyExists"] = None
    user_id: typing.Optional[int] = None
    views: typing.Optional[int] = None
    width: typing.Optional[int] = None


class NotificationsNotificationsComment(BaseModel):
    """VK Object NotificationsNotificationsComment

    date - Date when the comment has been added in Unixtime
    id - Comment ID
    owner_id - Author ID
    photo -
    post -
    text - Comment text
    topic -
    video -
    """

    date: typing.Optional[int] = None
    id: typing.Optional[int] = None
    owner_id: typing.Optional[int] = None
    photo: typing.Optional["PhotosPhoto"] = None
    post: typing.Optional["WallWallpost"] = None
    text: typing.Optional[str] = None
    topic: typing.Optional["BoardTopic"] = None
    video: typing.Optional["VideoVideo"] = None


class NotificationsNotificationParent(
    WallWallpostToId,
    PhotosPhoto,
    BoardTopic,
    VideoVideo,
    NotificationsNotificationsComment
):
    """VK Object NotificationsNotificationParent"""

    pass


class NotificationsReply(BaseModel):
    """VK Object NotificationsReply

    date - Date when the reply has been created in Unixtime
    id - Reply ID
    text - Reply text
    """

    date: typing.Optional[int] = None
    id: typing.Optional[int] = None
    text: typing.Optional[int] = None


class ErrorCode(enum.IntEnum):
    """ Error code """

    notifications_disabled = 1
    flood_control_per_hour = 2
    flood_control_per_day = 3
    app_is_not_installed = 4


class NotificationsSendMessageError(BaseModel):
    """VK Object NotificationsSendMessageError

    code - Error code
    description - Error description
    """

    code: typing.Optional["ErrorCode"] = None
    description: typing.Optional[str] = None


class NotificationsSendMessageItem(BaseModel):
    """VK Object NotificationsSendMessageItem

    error -
    status - Notification status
    user_id - User ID
    """

    error: typing.Optional["NotificationsSendMessageError"] = None
    status: typing.Optional[bool] = None
    user_id: typing.Optional[int] = None


class OauthError(BaseModel):
    """VK Object OauthError

    error - Error type
    error_description - Error description
    redirect_uri - URI for validation
    """

    error: str = None
    error_description: str = None
    redirect_uri: typing.Optional[str] = None


class OrdersAmount(BaseModel):
    """VK Object OrdersAmount

    amounts -
    currency - Currency name
    """

    amounts: typing.Optional[typing.List["OrdersAmountItem"]] = None
    currency: typing.Optional[str] = None


class OrdersAmountItem(BaseModel):
    """VK Object OrdersAmountItem

    amount - Votes amount in user's currency
    description - Amount description
    votes - Votes number
    """

    amount: typing.Optional[float] = None
    description: typing.Optional[str] = None
    votes: typing.Optional[str] = None


class OrderStatus(enum.Enum):
    """ Order status """

    CREATED = "created"
    CHARGED = "charged"
    REFUNDED = "refunded"
    CHARGEABLE = "chargeable"
    CANCELLED = "cancelled"
    DECLINED = "declined"


class OrdersOrder(BaseModel):
    """VK Object OrdersOrder

    amount - Amount
    app_order_id - App order ID
    cancel_transaction_id - Cancel transaction ID
    date - Date of creation in Unixtime
    id - Order ID
    item - Order item
    receiver_id - Receiver ID
    status - Order status
    transaction_id - Transaction ID
    user_id - User ID
    """

    amount: str = None
    app_order_id: str = None
    cancel_transaction_id: typing.Optional[str] = None
    date: str = None
    id: str = None
    item: str = None
    receiver_id: str = None
    status: "OrderStatus" = None
    transaction_id: typing.Optional[str] = None
    user_id: str = None


class OrdersSubscription(BaseModel):
    """VK Object OrdersSubscription

    app_id - Subscription's application id
    application_name - Subscription's application name
    cancel_reason - Cancel reason
    create_time - Date of creation in Unixtime
    expire_time - Subscription expiration time in Unixtime
    id - Subscription ID
    item_id - Subscription order item
    next_bill_time - Date of next bill in Unixtime
    pending_cancel - Pending cancel state
    period - Subscription period
    period_start_time - Date of last period start in Unixtime
    photo_url - Item photo image url
    price - Subscription price
    status - Subscription status
    test_mode - Is test subscription
    title - Subscription name
    trial_expire_time - Date of trial expire in Unixtime
    update_time - Date of last change in Unixtime
    """

    app_id: typing.Optional[int] = None
    application_name: typing.Optional[str] = None
    cancel_reason: typing.Optional[str] = None
    create_time: int = None
    expire_time: typing.Optional[int] = None
    id: int = None
    item_id: str = None
    next_bill_time: typing.Optional[int] = None
    pending_cancel: typing.Optional[bool] = None
    period: int = None
    period_start_time: int = None
    photo_url: typing.Optional[str] = None
    price: int = None
    status: str = None
    test_mode: typing.Optional[bool] = None
    title: typing.Optional[str] = None
    trial_expire_time: typing.Optional[int] = None
    update_time: int = None


class OwnerStateState(enum.IntEnum):
    """ OwnerStateState enum """

    banned = 1
    adult = 2
    hidden = 3
    deleted = 4
    blacklisted = 5


class OwnerState(BaseModel):
    """VK Object OwnerState

    description - wiki text to describe user state
    state -
    """

    description: typing.Optional[str] = None
    state: typing.Optional["OwnerStateState"] = None


class PagesPrivacySettings(enum.IntEnum):
    """ PagesPrivacySettings enum """

    community_managers_only = 0
    community_members_only = 1
    everyone = 2


class PagesWikipage(BaseModel):
    """VK Object PagesWikipage

    creator_id - Page creator ID
    creator_name - Page creator name
    editor_id - Last editor ID
    editor_name - Last editor name
    group_id - Community ID
    id - Page ID
    title - Page title
    views - Views number
    who_can_edit - Edit settings of the page
    who_can_view - View settings of the page
    """

    creator_id: typing.Optional[int] = None
    creator_name: typing.Optional[int] = None
    editor_id: typing.Optional[int] = None
    editor_name: typing.Optional[str] = None
    group_id: int = None
    id: int = None
    title: str = None
    views: int = None
    who_can_edit: "PagesPrivacySettings" = None
    who_can_view: "PagesPrivacySettings" = None


class PagesWikipageFull(BaseModel):
    """VK Object PagesWikipageFull

    created - Date when the page has been created in Unixtime
    creator_id - Page creator ID
    current_user_can_edit - Information whether current user can edit the page
    current_user_can_edit_access - Information whether current user can edit the page access settings
    edited - Date when the page has been edited in Unixtime
    editor_id - Last editor ID
    group_id - Community ID
    html - Page content, HTML
    id - Page ID
    owner_id - Owner ID
    parent - Parent
    parent2 - Parent2
    source - Page content, wiki
    title - Page title
    url - URL
    view_url - URL of the page preview
    views - Views number
    who_can_edit - Edit settings of the page
    who_can_view - View settings of the page
    """

    created: int = None
    creator_id: typing.Optional[int] = None
    current_user_can_edit: typing.Optional["BaseBoolInt"] = None
    current_user_can_edit_access: typing.Optional["BaseBoolInt"] = None
    edited: int = None
    editor_id: typing.Optional[int] = None
    group_id: int = None
    html: typing.Optional[str] = None
    id: int = None
    owner_id: typing.Optional[int] = None
    parent: typing.Optional[str] = None
    parent2: typing.Optional[str] = None
    source: typing.Optional[str] = None
    title: str = None
    url: typing.Optional[str] = None
    view_url: str = None
    views: int = None
    who_can_edit: "PagesPrivacySettings" = None
    who_can_view: "PagesPrivacySettings" = None


class PagesWikipageHistory(BaseModel):
    """VK Object PagesWikipageHistory

    date - Date when the page has been edited in Unixtime
    editor_id - Last editor ID
    editor_name - Last editor name
    id - Version ID
    length - Page size in bytes
    """

    date: int = None
    editor_id: int = None
    editor_name: str = None
    id: int = None
    length: int = None


class PhotosImage(BaseModel):
    """VK Object PhotosImage

    height - Height of the photo in px.
    type -
    url - Photo URL.
    width - Width of the photo in px.
    """

    height: typing.Optional[int] = None
    type: typing.Optional["PhotosImageType"] = None
    url: typing.Optional[str] = None
    width: typing.Optional[int] = None


class PhotosImageType(enum.Enum):
    """ Photo's type. """

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


class PhotosPhotoAlbum(BaseModel):
    """VK Object PhotosPhotoAlbum

    created - Date when the album has been created in Unixtime
    description - Photo album description
    id - Photo album ID
    owner_id - Album owner's ID
    size - Photos number
    thumb -
    title - Photo album title
    updated - Date when the album has been updated last time in Unixtime
    """

    created: int = None
    description: typing.Optional[str] = None
    id: int = None
    owner_id: int = None
    size: int = None
    thumb: typing.Optional["PhotosPhoto"] = None
    title: str = None
    updated: int = None


class PhotosPhotoAlbumFull(BaseModel):
    """VK Object PhotosPhotoAlbumFull

    can_upload - Information whether current user can upload photo to the album
    comments_disabled - Information whether album comments are disabled
    created - Date when the album has been created in Unixtime
    description - Photo album description
    id - Photo album ID
    owner_id - Album owner's ID
    size - Photos number
    sizes -
    thumb_id - Thumb photo ID
    thumb_is_last - Information whether the album thumb is last photo
    thumb_src - URL of the thumb image
    title - Photo album title
    updated - Date when the album has been updated last time in Unixtime
    upload_by_admins_only - Information whether only community administrators can upload photos
    """

    can_upload: typing.Optional["BaseBoolInt"] = None
    comments_disabled: typing.Optional["BaseBoolInt"] = None
    created: int = None
    description: typing.Optional[str] = None
    id: int = None
    owner_id: int = None
    size: int = None
    sizes: typing.Optional[typing.List["PhotosPhotoSizes"]] = None
    thumb_id: typing.Optional[int] = None
    thumb_is_last: typing.Optional["BaseBoolInt"] = None
    thumb_src: typing.Optional[str] = None
    title: str = None
    updated: int = None
    upload_by_admins_only: typing.Optional["BaseBoolInt"] = None


PhotosPhotoFalseable = typing.Union[bool, str]


class PhotosPhotoFull(BaseModel):
    """VK Object PhotosPhotoFull

    access_key - Access key for the photo
    album_id - Album ID
    can_comment - Information whether current user can comment the photo
    comments -
    date - Date when uploaded
    height - Original photo height
    id - Photo ID
    images -
    lat - Latitude
    likes -
    long - Longitude
    owner_id - Photo owner's ID
    post_id - Post ID
    reposts -
    tags -
    text - Photo caption
    user_id - ID of the user who have uploaded the photo
    width - Original photo width
    """

    access_key: typing.Optional[str] = None
    album_id: int = None
    can_comment: typing.Optional["BaseBoolInt"] = None
    comments: typing.Optional["BaseObjectCount"] = None
    date: int = None
    height: typing.Optional[int] = None
    id: int = None
    images: typing.Optional[typing.List["PhotosImage"]] = None
    lat: typing.Optional[float] = None
    likes: typing.Optional["BaseLikes"] = None
    long: typing.Optional[float] = None
    owner_id: int = None
    post_id: typing.Optional[int] = None
    reposts: typing.Optional["BaseRepostsInfo"] = None
    tags: typing.Optional["BaseObjectCount"] = None
    text: typing.Optional[str] = None
    user_id: typing.Optional[int] = None
    width: typing.Optional[int] = None


class PhotosPhotoFullXtrRealOffset(BaseModel):
    """VK Object PhotosPhotoFullXtrRealOffset

    access_key - Access key for the photo
    album_id - Album ID
    can_comment -
    comments -
    date - Date when uploaded
    height - Original photo height
    hidden - Returns if the photo is hidden above the wall
    id - Photo ID
    lat - Latitude
    likes -
    long - Longitude
    owner_id - Photo owner's ID
    photo_1280 - URL of image with 1280 px width
    photo_130 - URL of image with 130 px width
    photo_2560 - URL of image with 2560 px width
    photo_604 - URL of image with 604 px width
    photo_75 - URL of image with 75 px width
    photo_807 - URL of image with 807 px width
    post_id - Post ID
    real_offset - Real position of the photo
    reposts -
    sizes -
    tags -
    text - Photo caption
    user_id - ID of the user who have uploaded the photo
    width - Original photo width
    """

    access_key: typing.Optional[str] = None
    album_id: int = None
    can_comment: typing.Optional["BaseBoolInt"] = None
    comments: typing.Optional["BaseObjectCount"] = None
    date: int = None
    height: typing.Optional[int] = None
    hidden: typing.Optional["BasePropertyExists"] = None
    id: int = None
    lat: typing.Optional[float] = None
    likes: typing.Optional["BaseLikes"] = None
    long: typing.Optional[float] = None
    owner_id: int = None
    photo_1280: typing.Optional[str] = None
    photo_130: typing.Optional[str] = None
    photo_2560: typing.Optional[str] = None
    photo_604: typing.Optional[str] = None
    photo_75: typing.Optional[str] = None
    photo_807: typing.Optional[str] = None
    post_id: typing.Optional[int] = None
    real_offset: typing.Optional[int] = None
    reposts: typing.Optional["BaseObjectCount"] = None
    sizes: typing.Optional[typing.List["PhotosPhotoSizes"]] = None
    tags: typing.Optional["BaseObjectCount"] = None
    text: typing.Optional[str] = None
    user_id: typing.Optional[int] = None
    width: typing.Optional[int] = None


class PhotosPhotoSizes(BaseModel):
    """VK Object PhotosPhotoSizes

    height - Height in px
    src - URL of the image
    type -
    url - URL of the image
    width - Width in px
    """

    height: int = None
    src: typing.Optional[str] = None
    type: "PhotosPhotoSizesType" = None
    url: str = None
    width: int = None


class PhotosPhotoSizesType(enum.Enum):
    """ Size type """

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


class PhotosPhotoTag(BaseModel):
    """VK Object PhotosPhotoTag

    date - Date when tag has been added in Unixtime
    description - Tagged description.
    id - Tag ID
    placer_id - ID of the tag creator
    tagged_name - Tag description
    user_id - Tagged user ID
    viewed - Information whether the tag is reviewed
    x - Coordinate X of the left upper corner
    x2 - Coordinate X of the right lower corner
    y - Coordinate Y of the left upper corner
    y2 - Coordinate Y of the right lower corner
    """

    date: int = None
    description: typing.Optional[str] = None
    id: int = None
    placer_id: int = None
    tagged_name: str = None
    user_id: int = None
    viewed: "BaseBoolInt" = None
    x: float = None
    x2: float = None
    y: float = None
    y2: float = None


class PhotosPhotoUpload(BaseModel):
    """VK Object PhotosPhotoUpload

    album_id - Album ID
    fallback_upload_url - Fallback URL if upload_url returned error
    group_id - Group ID
    upload_url - URL to upload photo
    user_id - User ID
    """

    album_id: int = None
    fallback_upload_url: typing.Optional[str] = None
    group_id: typing.Optional[int] = None
    upload_url: str = None
    user_id: int = None


class PhotosPhotoXtrRealOffset(BaseModel):
    """VK Object PhotosPhotoXtrRealOffset

    access_key - Access key for the photo
    album_id - Album ID
    date - Date when uploaded
    height - Original photo height
    hidden - Returns if the photo is hidden above the wall
    id - Photo ID
    lat - Latitude
    long - Longitude
    owner_id - Photo owner's ID
    photo_1280 - URL of image with 1280 px width
    photo_130 - URL of image with 130 px width
    photo_2560 - URL of image with 2560 px width
    photo_604 - URL of image with 604 px width
    photo_75 - URL of image with 75 px width
    photo_807 - URL of image with 807 px width
    post_id - Post ID
    real_offset - Real position of the photo
    sizes -
    text - Photo caption
    user_id - ID of the user who have uploaded the photo
    width - Original photo width
    """

    access_key: typing.Optional[str] = None
    album_id: int = None
    date: int = None
    height: typing.Optional[int] = None
    hidden: typing.Optional["BasePropertyExists"] = None
    id: int = None
    lat: typing.Optional[float] = None
    long: typing.Optional[float] = None
    owner_id: int = None
    photo_1280: typing.Optional[str] = None
    photo_130: typing.Optional[str] = None
    photo_2560: typing.Optional[str] = None
    photo_604: typing.Optional[str] = None
    photo_75: typing.Optional[str] = None
    photo_807: typing.Optional[str] = None
    post_id: typing.Optional[int] = None
    real_offset: typing.Optional[int] = None
    sizes: typing.Optional[typing.List["PhotosPhotoSizes"]] = None
    text: typing.Optional[str] = None
    user_id: typing.Optional[int] = None
    width: typing.Optional[int] = None


class PhotosPhotoXtrTagInfo(BaseModel):
    """VK Object PhotosPhotoXtrTagInfo

    access_key - Access key for the photo
    album_id - Album ID
    date - Date when uploaded
    height - Original photo height
    id - Photo ID
    lat - Latitude
    long - Longitude
    owner_id - Photo owner's ID
    photo_1280 - URL of image with 1280 px width
    photo_130 - URL of image with 130 px width
    photo_2560 - URL of image with 2560 px width
    photo_604 - URL of image with 604 px width
    photo_75 - URL of image with 75 px width
    photo_807 - URL of image with 807 px width
    placer_id - ID of the tag creator
    post_id - Post ID
    sizes -
    tag_created - Date when tag has been added in Unixtime
    tag_id - Tag ID
    text - Photo caption
    user_id - ID of the user who have uploaded the photo
    width - Original photo width
    """

    access_key: typing.Optional[str] = None
    album_id: int = None
    date: int = None
    height: typing.Optional[int] = None
    id: int = None
    lat: typing.Optional[float] = None
    long: typing.Optional[float] = None
    owner_id: int = None
    photo_1280: typing.Optional[str] = None
    photo_130: typing.Optional[str] = None
    photo_2560: typing.Optional[str] = None
    photo_604: typing.Optional[str] = None
    photo_75: typing.Optional[str] = None
    photo_807: typing.Optional[str] = None
    placer_id: typing.Optional[int] = None
    post_id: typing.Optional[int] = None
    sizes: typing.Optional[typing.List["PhotosPhotoSizes"]] = None
    tag_created: typing.Optional[int] = None
    tag_id: typing.Optional[int] = None
    text: typing.Optional[str] = None
    user_id: typing.Optional[int] = None
    width: typing.Optional[int] = None


class PhotosTagsSuggestionItem(BaseModel):
    """VK Object PhotosTagsSuggestionItem"""

    buttons: typing.Optional[typing.List["PhotosTagsSuggestionItemButton"]] = None
    caption: typing.Optional[str] = None
    photo: typing.Optional["PhotosPhoto"] = None
    tags: typing.Optional[typing.List["PhotosPhotoTag"]] = None
    title: typing.Optional[str] = None
    track_code: typing.Optional[str] = None
    type: typing.Optional[str] = None


class PhotosTagsSuggestionItemButtonAction(enum.Enum):
    """ PhotosTagsSuggestionItemButtonAction enum """

    CONFIRM = "confirm"
    DECLINE = "decline"
    SHOW_TAGS = "show_tags"


class PhotosTagsSuggestionItemButtonStyle(enum.Enum):
    """ PhotosTagsSuggestionItemButtonStyle enum """

    PRIMARY = "primary"
    SECONDARY = "secondary"


class PhotosTagsSuggestionItemButton(BaseModel):
    """VK Object PhotosTagsSuggestionItemButton"""

    action: typing.Optional["PhotosTagsSuggestionItemButtonAction"] = None
    style: typing.Optional["PhotosTagsSuggestionItemButtonStyle"] = None
    title: typing.Optional[str] = None


class PodcastCover(BaseModel):
    """VK Object PodcastCover"""

    sizes: typing.Optional[typing.List["PhotosPhotoSizes"]] = None


class PodcastExternalData(BaseModel):
    """VK Object PodcastExternalData

    cover - Podcast cover
    owner_name - Name of the podcasts owner community
    owner_url - Url of the podcasts owner community
    title - Podcast title
    url - Url of the podcast page
    """

    cover: typing.Optional["PodcastCover"] = None
    owner_name: typing.Optional[str] = None
    owner_url: typing.Optional[str] = None
    title: typing.Optional[str] = None
    url: typing.Optional[str] = None


class PollsAnswer(BaseModel):
    """VK Object PollsAnswer

    id - Answer ID
    rate - Answer rate in percents
    text - Answer text
    votes - Votes number
    """

    id: int = None
    rate: float = None
    text: str = None
    votes: int = None


class PollsBackgroundType(enum.Enum):
    """ PollsBackgroundType enum """

    GRADIENT = "gradient"
    TILE = "tile"


class PollsBackground(BaseModel):
    """VK Object PollsBackground

    angle - Gradient angle with 0 on positive X axis
    color - Hex color code without #
    height - Original height of pattern tile
    id -
    images - Pattern tiles
    name -
    points - Gradient points
    type -
    width - Original with of pattern tile
    """

    angle: typing.Optional[int] = None
    color: typing.Optional[str] = None
    height: typing.Optional[int] = None
    id: typing.Optional[int] = None
    images: typing.Optional[typing.List["BaseImage"]] = None
    name: typing.Optional[str] = None
    points: typing.Optional[typing.List["BaseGradientPoint"]] = None
    type: typing.Optional["PollsBackgroundType"] = None
    width: typing.Optional[int] = None


class PollsFriend(BaseModel):
    """VK Object PollsFriend"""

    id: int = None


class PollsPoll(BaseModel):
    """VK Object PollsPoll

    anonymous -
    answer_id - Current user's answer ID
    answer_ids - Current user's answer IDs
    answers -
    author_id - Poll author's ID
    background -
    can_edit -
    can_report -
    can_share -
    can_vote -
    closed -
    created - Date when poll has been created in Unixtime
    disable_unvote -
    embed_hash -
    end_date -
    friends -
    id - Poll ID
    is_board -
    multiple - Information whether the poll with multiple choices
    owner_id - Poll owner's ID
    photo -
    question - Poll question
    votes - Votes number
    """

    anonymous: typing.Optional["PollsPollAnonymous"] = None
    answer_id: typing.Optional[int] = None
    answer_ids: typing.Optional[typing.List[int]] = None
    answers: typing.List["PollsAnswer"] = None
    author_id: typing.Optional[int] = None
    background: typing.Optional["PollsBackground"] = None
    can_edit: bool = None
    can_report: bool = None
    can_share: bool = None
    can_vote: bool = None
    closed: bool = None
    created: int = None
    disable_unvote: bool = None
    embed_hash: typing.Optional[str] = None
    end_date: int = None
    friends: typing.Optional[typing.List["PollsFriend"]] = None
    id: int = None
    is_board: bool = None
    multiple: bool = None
    owner_id: int = None
    photo: typing.Optional["PollsBackground"] = None
    question: str = None
    votes: int = None


PollsPollAnonymous = typing.Optional[bool]  # Information whether the field is anonymous


class PollsVoters(BaseModel):
    """VK Object PollsVoters

    answer_id - Answer ID
    users -
    """

    answer_id: typing.Optional[int] = None
    users: typing.Optional["PollsVotersUsers"] = None


class PollsVotersUsers(BaseModel):
    """VK Object PollsVotersUsers

    count - Votes number
    items -
    """

    count: typing.Optional[int] = None
    items: typing.Optional[typing.List[int]] = None


class PrettyCardsPrettyCard(BaseModel):
    """VK Object PrettyCardsPrettyCard

    button - Button key
    button_text - Button text in current language
    card_id - Card ID (long int returned as string)
    images -
    link_url - Link URL
    photo - Photo ID (format "<owner_id>_<media_id>")
    price - Price if set (decimal number returned as string)
    price_old - Old price if set (decimal number returned as string)
    title - Title
    """

    button: typing.Optional[str] = None
    button_text: typing.Optional[str] = None
    card_id: str = None
    images: typing.Optional[typing.List["BaseImage"]] = None
    link_url: str = None
    photo: str = None
    price: typing.Optional[str] = None
    price_old: typing.Optional[str] = None
    title: str = None


class SearchHint(BaseModel):
    """VK Object SearchHint

    app -
    description - Object description
    _global - Information whether the object has been found globally
    group -
    link -
    profile -
    section -
    type -
    """

    app: typing.Optional["AppsApp"] = None
    description: str = None
    _global: typing.Optional["BaseBoolInt"] = None
    group: typing.Optional["GroupsGroup"] = None
    link: typing.Optional["BaseLink"] = None
    profile: typing.Optional["UsersUserMin"] = None
    section: typing.Optional["SearchHintSection"] = None
    type: "SearchHintType" = None


class SearchHintSection(enum.Enum):
    """ Section title """

    GROUPS = "groups"
    EVENTS = "events"
    PUBLICS = "publics"
    CORRESPONDENTS = "correspondents"
    PEOPLE = "people"
    FRIENDS = "friends"
    MUTUAL_FRIENDS = "mutual_friends"
    PROMO = "promo"


class SearchHintType(enum.Enum):
    """ Object type """

    GROUP = "group"
    PROFILE = "profile"
    VK_APP = "vk_app"
    APP = "app"
    HTML5_GAME = "html5_game"
    LINK = "link"


class SecureGiveEventStickerItem(BaseModel):
    """VK Object SecureGiveEventStickerItem"""

    status: typing.Optional[str] = None
    user_id: typing.Optional[int] = None


class SecureLevel(BaseModel):
    """VK Object SecureLevel

    level - Level
    uid - User ID
    """

    level: typing.Optional[int] = None
    uid: typing.Optional[int] = None


class SecureSmsNotification(BaseModel):
    """VK Object SecureSmsNotification

    app_id - Application ID
    date - Date when message has been sent in Unixtime
    id - Notification ID
    message - Messsage text
    user_id - User ID
    """

    app_id: typing.Optional[str] = None
    date: typing.Optional[str] = None
    id: typing.Optional[str] = None
    message: typing.Optional[str] = None
    user_id: typing.Optional[str] = None


class SecureTokenChecked(BaseModel):
    """VK Object SecureTokenChecked

    date - Date when access_token has been generated in Unixtime
    expire - Date when access_token will expire in Unixtime
    success - Returns if successfully processed
    user_id - User ID
    """

    date: typing.Optional[int] = None
    expire: typing.Optional[int] = None
    success: typing.Optional[int] = None
    user_id: typing.Optional[int] = None


class SecureTransaction(BaseModel):
    """VK Object SecureTransaction

    date - Transaction date in Unixtime
    id - Transaction ID
    uid_from - From ID
    uid_to - To ID
    votes - Votes number
    """

    date: typing.Optional[int] = None
    id: typing.Optional[int] = None
    uid_from: typing.Optional[int] = None
    uid_to: typing.Optional[int] = None
    votes: typing.Optional[int] = None


class StatsActivity(BaseModel):
    """VK Object StatsActivity

    comments - Comments number
    copies - Reposts number
    hidden - Hidden from news count
    likes - Likes number
    subscribed - New subscribers count
    unsubscribed - Unsubscribed count
    """

    comments: typing.Optional[int] = None
    copies: typing.Optional[int] = None
    hidden: typing.Optional[int] = None
    likes: typing.Optional[int] = None
    subscribed: typing.Optional[int] = None
    unsubscribed: typing.Optional[int] = None


class StatsCity(BaseModel):
    """VK Object StatsCity

    count - Visitors number
    name - City name
    value - City ID
    """

    count: typing.Optional[int] = None
    name: typing.Optional[str] = None
    value: typing.Optional[int] = None


class StatsCountry(BaseModel):
    """VK Object StatsCountry

    code - Country code
    count - Visitors number
    name - Country name
    value - Country ID
    """

    code: typing.Optional[str] = None
    count: typing.Optional[int] = None
    name: typing.Optional[str] = None
    value: typing.Optional[int] = None


class StatsPeriod(BaseModel):
    """VK Object StatsPeriod

    activity -
    period_from - Unix timestamp
    period_to - Unix timestamp
    reach -
    visitors -
    """

    activity: typing.Optional["StatsActivity"] = None
    period_from: typing.Optional[int] = None
    period_to: typing.Optional[int] = None
    reach: typing.Optional["StatsReach"] = None
    visitors: typing.Optional["StatsViews"] = None


class StatsReach(BaseModel):
    """VK Object StatsReach

    age -
    cities -
    countries -
    mobile_reach - Reach count from mobile devices
    reach - Reach count
    reach_subscribers - Subscribers reach count
    sex -
    sex_age -
    """

    age: typing.Optional[typing.List["StatsSexAge"]] = None
    cities: typing.Optional[typing.List["StatsCity"]] = None
    countries: typing.Optional[typing.List["StatsCountry"]] = None
    mobile_reach: typing.Optional[int] = None
    reach: typing.Optional[int] = None
    reach_subscribers: typing.Optional[int] = None
    sex: typing.Optional[typing.List["StatsSexAge"]] = None
    sex_age: typing.Optional[typing.List["StatsSexAge"]] = None


class StatsSexAge(BaseModel):
    """VK Object StatsSexAge

    count - Visitors number
    count_subscribers -
    reach -
    reach_subscribers -
    value - Sex/age value
    """

    count: typing.Optional[int] = None
    count_subscribers: typing.Optional[int] = None
    reach: typing.Optional[int] = None
    reach_subscribers: typing.Optional[int] = None
    value: str = None


class StatsViews(BaseModel):
    """VK Object StatsViews

    age -
    cities -
    countries -
    mobile_views - Number of views from mobile devices
    sex -
    sex_age -
    views - Views number
    visitors - Visitors number
    """

    age: typing.Optional[typing.List["StatsSexAge"]] = None
    cities: typing.Optional[typing.List["StatsCity"]] = None
    countries: typing.Optional[typing.List["StatsCountry"]] = None
    mobile_views: typing.Optional[int] = None
    sex: typing.Optional[typing.List["StatsSexAge"]] = None
    sex_age: typing.Optional[typing.List["StatsSexAge"]] = None
    views: typing.Optional[int] = None
    visitors: typing.Optional[int] = None


class StatsWallpostStat(BaseModel):
    """VK Object StatsWallpostStat

    hide - Hidings number
    join_group - People have joined the group
    links - Link clickthrough
    post_id -
    reach_ads -
    reach_subscribers - Subscribers reach
    reach_subscribers_count -
    reach_total - Total reach
    reach_total_count -
    reach_viral -
    report - Reports number
    sex_age -
    to_group - Clickthrough to community
    unsubscribe - Unsubscribed members
    """

    hide: typing.Optional[int] = None
    join_group: typing.Optional[int] = None
    links: typing.Optional[int] = None
    post_id: typing.Optional[int] = None
    reach_ads: typing.Optional[int] = None
    reach_subscribers: typing.Optional[int] = None
    reach_subscribers_count: typing.Optional[int] = None
    reach_total: typing.Optional[int] = None
    reach_total_count: typing.Optional[int] = None
    reach_viral: typing.Optional[int] = None
    report: typing.Optional[int] = None
    sex_age: typing.Optional[typing.List["StatsSexAge"]] = None
    to_group: typing.Optional[int] = None
    unsubscribe: typing.Optional[int] = None


class StatusStatus(BaseModel):
    """VK Object StatusStatus

    audio -
    text - Status text
    """

    audio: typing.Optional["AudioAudio"] = None
    text: str = None


class StickersImageSet(BaseModel):
    """VK Object StickersImageSet

    base_url - Base URL for images in set
    version - Version number to be appended to the image URL
    """

    base_url: str = None
    version: typing.Optional[int] = None


class StorageValue(BaseModel):
    """VK Object StorageValue"""

    key: str = None
    value: str = None


class ProductType(enum.Enum):
    """ Product type """

    STICKERS = "stickers"


class StoreProduct(BaseModel):
    """VK Object StoreProduct

    active - Information whether the product is active (1 - yes, 0 - no)
    has_animation - Information whether the product is an animated sticker pack (for stickers product type)
    icon - Array of icon images or icon set object of the product (for stickers product type)
    id - Id of the product
    is_new - Information whether sticker product wasn't used after being purchased
    payment_region -
    previews - Array of preview images of the product (for stickers product type)
    promoted - Information whether the product is promoted (1 - yes, 0 - no)
    purchase_date - Date (Unix time) when the product was purchased
    purchased - Information whether the product is purchased (1 - yes, 0 - no)
    stickers -
    style_sticker_ids - Array of style sticker ids (for sticker pack styles)
    subtitle - Subtitle of the product
    title - Title of the product
    type - Product type
    """

    active: typing.Optional["BaseBoolInt"] = None
    has_animation: typing.Optional[bool] = None
    icon: typing.Optional["StoreProductIcon"] = None
    id: int = None
    is_new: typing.Optional[bool] = None
    payment_region: typing.Optional[str] = None
    previews: typing.Optional[typing.List["BaseImage"]] = None
    promoted: typing.Optional["BaseBoolInt"] = None
    purchase_date: typing.Optional[int] = None
    purchased: typing.Optional["BaseBoolInt"] = None
    stickers: typing.Optional["BaseStickersList"] = None
    style_sticker_ids: typing.Optional[typing.List[int]] = None
    subtitle: typing.Optional[str] = None
    title: typing.Optional[str] = None
    type: "ProductType" = None


StoreProductIcon = typing.List["BaseImage"]


class StoreStickersKeyword(BaseModel):
    """VK Object StoreStickersKeyword"""

    promoted_stickers: typing.Optional["StoreStickersKeywordStickers"] = None
    stickers: typing.Optional[typing.List["StoreStickersKeywordSticker"]] = None
    user_stickers: typing.Optional["StoreStickersKeywordStickers"] = None
    words: typing.List[str] = None


class StoreStickersKeywordSticker(BaseModel):
    """VK Object StoreStickersKeywordSticker

    pack_id - Pack id
    sticker_id - Sticker id
    """

    pack_id: int = None
    sticker_id: int = None


StoreStickersKeywordStickers = BaseStickersList


class StoriesClickableArea(BaseModel):
    """VK Object StoriesClickableArea"""

    x: int = None
    y: int = None


class StoriesClickableStickerStyle(enum.Enum):
    """ StoriesClickableStickerStyle enum """

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


class StoriesClickableStickerType(enum.Enum):
    """ StoriesClickableStickerType enum """

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


class StoriesClickableStickerSubtype(enum.Enum):
    """ StoriesClickableStickerSubtype enum """

    MARKET_ITEM = "market_item"
    ALIEXPRESS_PRODUCT = "aliexpress_product"


class StoriesClickableSticker(BaseModel):
    """VK Object StoriesClickableSticker

    app -
    app_context - Additional context for app sticker
    audio -
    audio_start_time -
    clickable_area -
    color - Color, hex format
    has_new_interactions - Whether current user has unread interaction with this app
    hashtag -
    id - Clickable sticker ID
    is_broadcast_notify_allowed - Whether current user allowed broadcast notify from this app
    link_object -
    market_item -
    mention -
    owner_id -
    place_id -
    poll -
    post_id -
    post_owner_id -
    question -
    question_button -
    situational_app_url -
    situational_theme_id -
    sticker_id - Sticker ID
    sticker_pack_id - Sticker pack ID
    story_id -
    style -
    subtype -
    tooltip_text -
    type -
    """

    app: typing.Optional["AppsAppMin"] = None
    app_context: typing.Optional[str] = None
    audio: typing.Optional["AudioAudio"] = None
    audio_start_time: typing.Optional[int] = None
    clickable_area: typing.List["StoriesClickableArea"] = None
    color: typing.Optional[str] = None
    has_new_interactions: typing.Optional[bool] = None
    hashtag: typing.Optional[str] = None
    id: int = None
    is_broadcast_notify_allowed: typing.Optional[bool] = None
    link_object: typing.Optional["BaseLink"] = None
    market_item: typing.Optional["MarketMarketItem"] = None
    mention: typing.Optional[str] = None
    owner_id: typing.Optional[int] = None
    place_id: typing.Optional[int] = None
    poll: typing.Optional["PollsPoll"] = None
    post_id: typing.Optional[int] = None
    post_owner_id: typing.Optional[int] = None
    question: typing.Optional[str] = None
    question_button: typing.Optional[str] = None
    situational_app_url: typing.Optional[str] = None
    situational_theme_id: typing.Optional[int] = None
    sticker_id: typing.Optional[int] = None
    sticker_pack_id: typing.Optional[int] = None
    story_id: typing.Optional[int] = None
    style: typing.Optional["StoriesClickableStickerStyle"] = None
    subtype: typing.Optional["StoriesClickableStickerSubtype"] = None
    tooltip_text: typing.Optional[str] = None
    type: "StoriesClickableStickerType" = None


class StoriesClickableStickers(BaseModel):
    """VK Object StoriesClickableStickers"""

    clickable_stickers: typing.List["StoriesClickableSticker"] = None
    original_height: int = None
    original_width: int = None


class FeedItemType(enum.Enum):
    """ Type of Feed Item """

    PROMO_STORIES = "promo_stories"
    STORIES = "stories"
    LIVE_ACTIVE = "live_active"
    LIVE_FINISHED = "live_finished"
    COMMUNITY_GROUPED_STORIES = "community_grouped_stories"
    APP_GROUPED_STORIES = "app_grouped_stories"
    BIRTHDAY = "birthday"


class StoriesFeedItem(BaseModel):
    """VK Object StoriesFeedItem

    app - App, which stories has been grouped (for type app_grouped_stories)
    birthday_user_id -
    grouped - Grouped stories of various authors (for types community_grouped_stories/app_grouped_stories type)
    has_unseen -
    id -
    name -
    promo_data - Additional data for promo stories (for type promo_stories)
    stories - Author stories
    track_code -
    type - Type of Feed Item
    """

    app: typing.Optional["AppsAppMin"] = None
    birthday_user_id: typing.Optional[int] = None
    grouped: typing.Optional[typing.List["StoriesFeedItem"]] = None
    has_unseen: typing.Optional[bool] = None
    id: typing.Optional[str] = None
    name: typing.Optional[str] = None
    promo_data: typing.Optional["StoriesPromoBlock"] = None
    stories: typing.Optional[typing.List["StoriesStory"]] = None
    track_code: typing.Optional[str] = None
    type: "FeedItemType" = None


class StoriesPromoBlock(BaseModel):
    """VK Object StoriesPromoBlock

    name - Promo story title
    not_animated - Hide animation for promo story
    photo_100 - RL of square photo of the story with 100 pixels in width
    photo_50 - RL of square photo of the story with 50 pixels in width
    """

    name: str = None
    not_animated: bool = None
    photo_100: str = None
    photo_50: str = None


class StoriesReplies(BaseModel):
    """VK Object StoriesReplies

    count - Replies number.
    new - New replies number.
    """

    count: int = None
    new: typing.Optional[int] = None


class StoriesStatLine(BaseModel):
    """VK Object StoriesStatLine"""

    counter: typing.Optional[int] = None
    is_unavailable: typing.Optional[bool] = None
    name: str = None


class StoriesStory(BaseModel):
    """VK Object StoriesStory

    access_key - Access key for private object.
    birthday_wish_user_id -
    can_ask - Information whether story has question sticker and current user can send question to the author
    can_ask_anonymous - Information whether story has question sticker and current user can send anonymous question to the author
    can_comment - Information whether current user can comment the story (0 - no, 1 - yes).
    can_hide - Information whether current user can hide the story (0 - no, 1 - yes).
    can_like - Information whether current user can like the story.
    can_reply - Information whether current user can reply to the story (0 - no, 1 - yes).
    can_see - Information whether current user can see the story (0 - no, 1 - yes).
    can_share - Information whether current user can share the story (0 - no, 1 - yes).
    can_use_in_narrative -
    clickable_stickers -
    date - Date when story has been added in Unixtime.
    expires_at - Story expiration time. Unixtime.
    first_narrative_title -
    id - Story ID.
    is_deleted - Information whether the story is deleted (false - no, true - yes).
    is_expired - Information whether the story is expired (false - no, true - yes).
    link -
    narratives_count -
    owner_id - Story owner's ID.
    parent_story -
    parent_story_access_key - Access key for private object.
    parent_story_id - Parent story ID.
    parent_story_owner_id - Parent story owner's ID.
    photo -
    replies - Replies counters to current story.
    seen - Information whether current user has seen the story or not (0 - no, 1 - yes).
    type -
    video -
    views - Views number.
    """

    access_key: typing.Optional[str] = None
    birthday_wish_user_id: typing.Optional[int] = None
    can_ask: typing.Optional["BaseBoolInt"] = None
    can_ask_anonymous: typing.Optional["BaseBoolInt"] = None
    can_comment: typing.Optional["BaseBoolInt"] = None
    can_hide: typing.Optional["BaseBoolInt"] = None
    can_like: typing.Optional[bool] = None
    can_reply: typing.Optional["BaseBoolInt"] = None
    can_see: typing.Optional["BaseBoolInt"] = None
    can_share: typing.Optional["BaseBoolInt"] = None
    can_use_in_narrative: typing.Optional[bool] = None
    clickable_stickers: typing.Optional["StoriesClickableStickers"] = None
    date: typing.Optional[int] = None
    expires_at: typing.Optional[int] = None
    first_narrative_title: typing.Optional[str] = None
    id: int = None
    is_deleted: typing.Optional[bool] = None
    is_expired: typing.Optional[bool] = None
    link: typing.Optional["StoriesStoryLink"] = None
    narratives_count: typing.Optional[int] = None
    owner_id: int = None
    parent_story: typing.Optional["StoriesStory"] = None
    parent_story_access_key: typing.Optional[str] = None
    parent_story_id: typing.Optional[int] = None
    parent_story_owner_id: typing.Optional[int] = None
    photo: typing.Optional["PhotosPhoto"] = None
    replies: typing.Optional["StoriesReplies"] = None
    seen: typing.Optional["BaseBoolInt"] = None
    type: typing.Optional["StoriesStoryType"] = None
    video: typing.Optional["VideoVideo"] = None
    views: typing.Optional[int] = None


class StoriesStoryLink(BaseModel):
    """VK Object StoriesStoryLink

    text - Link text
    url - Link URL
    """

    text: str = None
    url: str = None


class StoriesStoryStats(BaseModel):
    """VK Object StoriesStoryStats"""

    answer: "StoriesStoryStatsStat" = None
    bans: "StoriesStoryStatsStat" = None
    likes: "StoriesStoryStatsStat" = None
    open_link: "StoriesStoryStatsStat" = None
    replies: "StoriesStoryStatsStat" = None
    shares: "StoriesStoryStatsStat" = None
    subscribers: "StoriesStoryStatsStat" = None
    views: "StoriesStoryStatsStat" = None


class StoriesStoryStatsStat(BaseModel):
    """VK Object StoriesStoryStatsStat

    count - Stat value
    state -
    """

    count: typing.Optional[int] = None
    state: "StoriesStoryStatsState" = None


class StoriesStoryStatsState(enum.Enum):
    """ Statistic state """

    ON = "on"
    OFF = "off"
    HIDDEN = "hidden"


class StoriesStoryType(enum.Enum):
    """ Story type. """

    PHOTO = "photo"
    VIDEO = "video"
    LIVE_ACTIVE = "live_active"
    LIVE_FINISHED = "live_finished"
    BIRTHDAY_INVITE = "birthday_invite"


class StoriesUploadLinkText(enum.Enum):
    """ StoriesUploadLinkText enum """

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


class StoriesViewersItem(BaseModel):
    """VK Object StoriesViewersItem

    is_liked - user has like for this object
    user -
    user_id - user id
    """

    is_liked: bool = None
    user: typing.Optional["UsersUserFull"] = None
    user_id: int = None


class UsersCareer(BaseModel):
    """VK Object UsersCareer

    city_id - City ID
    city_name - City name
    company - Company name
    country_id - Country ID
    _from - From year
    group_id - Community ID
    id - Career ID
    position - Position
    until - Till year
    """

    city_id: typing.Optional[int] = None
    city_name: typing.Optional[str] = None
    company: typing.Optional[str] = None
    country_id: typing.Optional[int] = None
    _from: typing.Optional[int] = None
    group_id: typing.Optional[int] = None
    id: typing.Optional[int] = None
    position: typing.Optional[str] = None
    until: typing.Optional[int] = None


class UsersExports(BaseModel):
    """VK Object UsersExports"""

    facebook: typing.Optional[int] = None
    livejournal: typing.Optional[int] = None
    twitter: typing.Optional[int] = None


class UsersFields(enum.Enum):
    """ UsersFields enum """

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
    IS_FAVORITE = "is_favorite"
    IS_HIDDEN_FROM_FEED = "is_hidden_from_feed"
    TIMEZONE = "timezone"
    SCREEN_NAME = "screen_name"
    MAIDEN_NAME = "maiden_name"
    CROP_PHOTO = "crop_photo"
    IS_FRIEND = "is_friend"
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


class UsersLastSeen(BaseModel):
    """VK Object UsersLastSeen

    platform - Type of the platform that used for the last authorization
    time - Last visit date (in Unix time)
    """

    platform: typing.Optional[int] = None
    time: typing.Optional[int] = None


class UsersMilitary(BaseModel):
    """VK Object UsersMilitary

    country_id - Country ID
    _from - From year
    id - Military ID
    unit - Unit name
    unit_id - Unit ID
    until - Till year
    """

    country_id: int = None
    _from: typing.Optional[int] = None
    id: typing.Optional[int] = None
    unit: str = None
    unit_id: int = None
    until: typing.Optional[int] = None


class UsersOccupation(BaseModel):
    """VK Object UsersOccupation

    id - ID of school, university, company group
    name - Name of occupation
    type - Type of occupation
    """

    id: typing.Optional[int] = None
    name: typing.Optional[str] = None
    type: typing.Optional[str] = None


class UsersOnlineInfoStatus(enum.Enum):
    """ In case user online is not visible, it indicates approximate timeframe of user online """

    RECENTLY = "recently"
    LAST_WEEK = "last_week"
    LAST_MONTH = "last_month"
    LONG_AGO = "long_ago"
    NOT_SHOW = "not_show"


class UsersOnlineInfo(BaseModel):
    """VK Object UsersOnlineInfo

    app_id - Application id from which user is currently online or was last seen online
    is_mobile - Is user online from desktop app or mobile app
    is_online - Whether user is currently online or not
    last_seen - Last time we saw user being active
    status - In case user online is not visible, it indicates approximate timeframe of user online
    visible - Whether you can see real online status of user or not
    """

    app_id: typing.Optional[int] = None
    is_mobile: typing.Optional[bool] = None
    is_online: typing.Optional[bool] = None
    last_seen: typing.Optional[int] = None
    status: typing.Optional["UsersOnlineInfoStatus"] = None
    visible: bool = None


class UsersPersonal(BaseModel):
    """VK Object UsersPersonal

    alcohol - User's views on alcohol
    inspired_by - User's inspired by
    langs -
    life_main - User's personal priority in life
    people_main - User's personal priority in people
    political - User's political views
    religion - User's religion
    religion_id - User's religion id
    smoking - User's views on smoking
    """

    alcohol: typing.Optional[int] = None
    inspired_by: typing.Optional[str] = None
    langs: typing.Optional[typing.List[str]] = None
    life_main: typing.Optional[int] = None
    people_main: typing.Optional[int] = None
    political: typing.Optional[int] = None
    religion: typing.Optional[str] = None
    religion_id: typing.Optional[int] = None
    smoking: typing.Optional[int] = None


class RelativeType(enum.Enum):
    """ Relative type """

    PARENT = "parent"
    CHILD = "child"
    GRANDPARENT = "grandparent"
    GRANDCHILD = "grandchild"
    SIBLING = "sibling"


class UsersRelative(BaseModel):
    """VK Object UsersRelative

    birth_date - Date of child birthday (format dd.mm.yyyy)
    id - Relative ID
    name - Name of relative
    type - Relative type
    """

    birth_date: typing.Optional[str] = None
    id: typing.Optional[int] = None
    name: typing.Optional[str] = None
    type: "RelativeType" = None


class UsersSchool(BaseModel):
    """VK Object UsersSchool

    city - City ID
    _class - School class letter
    country - Country ID
    id - School ID
    name - School name
    speciality -
    type - School type ID
    type_str - School type name
    year_from - Year the user started to study
    year_graduated - Graduation year
    year_to - Year the user finished to study
    """

    city: typing.Optional[int] = None
    _class: typing.Optional[str] = None
    country: typing.Optional[int] = None
    id: typing.Optional[str] = None
    name: typing.Optional[str] = None
    speciality: typing.Optional[str] = None
    type: typing.Optional[int] = None
    type_str: typing.Optional[str] = None
    year_from: typing.Optional[int] = None
    year_graduated: typing.Optional[int] = None
    year_to: typing.Optional[int] = None


class UsersSubscriptionsItem(UsersUserXtrType, GroupsGroupFull):
    """VK Object UsersSubscriptionsItem"""

    pass


class UsersUniversity(BaseModel):
    """VK Object UsersUniversity

    chair - Chair ID
    chair_name - Chair name
    city - City ID
    country - Country ID
    education_form - Education form
    education_status - Education status
    faculty - Faculty ID
    faculty_name - Faculty name
    graduation - Graduation year
    id - University ID
    name - University name
    university_group_id -
    """

    chair: typing.Optional[int] = None
    chair_name: typing.Optional[str] = None
    city: typing.Optional[int] = None
    country: typing.Optional[int] = None
    education_form: typing.Optional[str] = None
    education_status: typing.Optional[str] = None
    faculty: typing.Optional[int] = None
    faculty_name: typing.Optional[str] = None
    graduation: typing.Optional[int] = None
    id: typing.Optional[int] = None
    name: typing.Optional[str] = None
    university_group_id: typing.Optional[int] = None


class UsersUserConnections(BaseModel):
    """VK Object UsersUserConnections

    facebook - User's Facebook account
    facebook_name - User's Facebook name
    instagram - User's Instagram account
    livejournal - User's Livejournal account
    skype - User's Skype nickname
    twitter - User's Twitter account
    """

    facebook: str = None
    facebook_name: typing.Optional[str] = None
    instagram: str = None
    livejournal: typing.Optional[str] = None
    skype: str = None
    twitter: str = None


class UsersUserCounters(BaseModel):
    """VK Object UsersUserCounters

    albums - Albums number
    articles -
    audios - Audios number
    badges - Badges number
    clips -
    clips_followers -
    followers - Followers number
    friends - Friends number
    gifts - Gifts number
    groups - Communities number
    mutual_friends -
    new_photo_tags -
    new_recognition_tags -
    notes - Notes number
    online_friends - Online friends number
    pages - Public pages number
    photos - Photos number
    podcasts -
    posts -
    subscriptions - Subscriptions number
    user_photos - Number of photos with user
    user_videos - Number of videos with user
    videos - Videos number
    wishes -
    """

    albums: typing.Optional[int] = None
    articles: typing.Optional[int] = None
    audios: typing.Optional[int] = None
    badges: typing.Optional[int] = None
    clips: typing.Optional[int] = None
    clips_followers: typing.Optional[int] = None
    followers: typing.Optional[int] = None
    friends: typing.Optional[int] = None
    gifts: typing.Optional[int] = None
    groups: typing.Optional[int] = None
    mutual_friends: typing.Optional[int] = None
    new_photo_tags: typing.Optional[int] = None
    new_recognition_tags: typing.Optional[int] = None
    notes: typing.Optional[int] = None
    online_friends: typing.Optional[int] = None
    pages: typing.Optional[int] = None
    photos: typing.Optional[int] = None
    podcasts: typing.Optional[int] = None
    posts: typing.Optional[int] = None
    subscriptions: typing.Optional[int] = None
    user_photos: typing.Optional[int] = None
    user_videos: typing.Optional[int] = None
    videos: typing.Optional[int] = None
    wishes: typing.Optional[int] = None


class UsersUserRelation(enum.IntEnum):
    """ UsersUserRelation enum """

    not_specified = 0
    single = 1
    in_a_relationship = 2
    engaged = 3
    married = 4
    complicated = 5
    actively_searching = 6
    in_love = 7
    in_a_civil_union = 8


class UsersUserType(enum.Enum):
    """ Object type """

    PROFILE = "profile"


class UsersUsersArray(BaseModel):
    """VK Object UsersUsersArray

    count - Users number
    items -
    """

    count: int = None
    items: typing.List[int] = None


class UtilsDomainResolved(BaseModel):
    """VK Object UtilsDomainResolved

    group_id - Group ID
    object_id - Object ID
    type -
    """

    group_id: typing.Optional[int] = None
    object_id: typing.Optional[int] = None
    type: typing.Optional["UtilsDomainResolvedType"] = None


class UtilsDomainResolvedType(enum.Enum):
    """ Object type """

    USER = "user"
    GROUP = "group"
    APPLICATION = "application"
    PAGE = "page"
    VK_APP = "vk_app"
    COMMUNITY_APPLICATION = "community_application"


class UtilsLastShortenedLink(BaseModel):
    """VK Object UtilsLastShortenedLink

    access_key - Access key for private stats
    key - Link key (characters after vk.cc/)
    short_url - Short link URL
    timestamp - Creation time in Unixtime
    url - Full URL
    views - Total views number
    """

    access_key: typing.Optional[str] = None
    key: typing.Optional[str] = None
    short_url: typing.Optional[str] = None
    timestamp: typing.Optional[int] = None
    url: typing.Optional[str] = None
    views: typing.Optional[int] = None


class UtilsLinkChecked(BaseModel):
    """VK Object UtilsLinkChecked

    link - Link URL
    status -
    """

    link: typing.Optional[str] = None
    status: typing.Optional["UtilsLinkCheckedStatus"] = None


class UtilsLinkCheckedStatus(enum.Enum):
    """ Link status """

    NOT_BANNED = "not_banned"
    BANNED = "banned"
    PROCESSING = "processing"


class UtilsLinkStats(BaseModel):
    """VK Object UtilsLinkStats

    key - Link key (characters after vk.cc/)
    stats -
    """

    key: typing.Optional[str] = None
    stats: typing.Optional[typing.List["UtilsStats"]] = None


class UtilsLinkStatsExtended(BaseModel):
    """VK Object UtilsLinkStatsExtended

    key - Link key (characters after vk.cc/)
    stats -
    """

    key: typing.Optional[str] = None
    stats: typing.Optional[typing.List["UtilsStatsExtended"]] = None


class UtilsShortLink(BaseModel):
    """VK Object UtilsShortLink

    access_key - Access key for private stats
    key - Link key (characters after vk.cc/)
    short_url - Short link URL
    url - Full URL
    """

    access_key: typing.Optional[str] = None
    key: typing.Optional[str] = None
    short_url: typing.Optional[str] = None
    url: typing.Optional[str] = None


class UtilsStats(BaseModel):
    """VK Object UtilsStats

    timestamp - Start time
    views - Total views number
    """

    timestamp: typing.Optional[int] = None
    views: typing.Optional[int] = None


class UtilsStatsCity(BaseModel):
    """VK Object UtilsStatsCity

    city_id - City ID
    views - Views number
    """

    city_id: typing.Optional[int] = None
    views: typing.Optional[int] = None


class UtilsStatsCountry(BaseModel):
    """VK Object UtilsStatsCountry

    country_id - Country ID
    views - Views number
    """

    country_id: typing.Optional[int] = None
    views: typing.Optional[int] = None


class UtilsStatsExtended(BaseModel):
    """VK Object UtilsStatsExtended

    cities -
    countries -
    sex_age -
    timestamp - Start time
    views - Total views number
    """

    cities: typing.Optional[typing.List["UtilsStatsCity"]] = None
    countries: typing.Optional[typing.List["UtilsStatsCountry"]] = None
    sex_age: typing.Optional[typing.List["UtilsStatsSexAge"]] = None
    timestamp: typing.Optional[int] = None
    views: typing.Optional[int] = None


class UtilsStatsSexAge(BaseModel):
    """VK Object UtilsStatsSexAge

    age_range - Age denotation
    female - Views by female users
    male - Views by male users
    """

    age_range: typing.Optional[str] = None
    female: typing.Optional[int] = None
    male: typing.Optional[int] = None


class VideoLiveInfo(BaseModel):
    """VK Object VideoLiveInfo"""

    enabled: "BaseBoolInt" = None
    is_notifications_blocked: typing.Optional["BaseBoolInt"] = None


class VideoLiveSettings(BaseModel):
    """VK Object VideoLiveSettings

    can_rewind - If user car rewind live or not
    is_endless - If live is endless or not
    max_duration - Max possible time for rewind
    """

    can_rewind: typing.Optional["BaseBoolInt"] = None
    is_endless: typing.Optional["BaseBoolInt"] = None
    max_duration: typing.Optional[int] = None


class VideoSaveResult(BaseModel):
    """VK Object VideoSaveResult

    access_key - Video access key
    description - Video description
    owner_id - Video owner ID
    title - Video title
    upload_url - URL for the video uploading
    video_id - Video ID
    """

    access_key: typing.Optional[str] = None
    description: typing.Optional[str] = None
    owner_id: typing.Optional[int] = None
    title: typing.Optional[str] = None
    upload_url: typing.Optional[str] = None
    video_id: typing.Optional[int] = None


class VideoVideoAlbum(BaseModel):
    """VK Object VideoVideoAlbum

    id - Album ID
    owner_id - Album owner's ID
    title - Album title
    """

    id: int = None
    owner_id: int = None
    title: str = None


class VideoVideoAlbumFull(VideoVideoAlbum):
    """VK Object VideoVideoAlbumFull

    count - Total number of videos in album
    image - Album cover image in different sizes
    image_blur - Need blur album thumb or not
    is_system - Information whether album is system
    updated_time - Date when the album has been updated last time in Unixtime
    """

    count: typing.Optional[int] = None
    image: typing.Optional[typing.List["VideoVideoImage"]] = None
    image_blur: typing.Optional["BasePropertyExists"] = None
    is_system: typing.Optional["BasePropertyExists"] = None
    updated_time: typing.Optional[int] = None


class VideoVideoFiles(BaseModel):
    """VK Object VideoVideoFiles

    external - URL of the external player
    flv_320 - URL of the flv file with 320p quality
    mp4_1080 - URL of the mpeg4 file with 1080p quality
    mp4_1440 - URL of the mpeg4 file with 2K quality
    mp4_2160 - URL of the mpeg4 file with 4K quality
    mp4_240 - URL of the mpeg4 file with 240p quality
    mp4_360 - URL of the mpeg4 file with 360p quality
    mp4_480 - URL of the mpeg4 file with 480p quality
    mp4_720 - URL of the mpeg4 file with 720p quality
    """

    external: typing.Optional[str] = None
    flv_320: typing.Optional[str] = None
    mp4_1080: typing.Optional[str] = None
    mp4_1440: typing.Optional[str] = None
    mp4_2160: typing.Optional[str] = None
    mp4_240: typing.Optional[str] = None
    mp4_360: typing.Optional[str] = None
    mp4_480: typing.Optional[str] = None
    mp4_720: typing.Optional[str] = None


class VideoVideoFull(VideoVideo):
    """VK Object VideoVideoFull

    files -
    live_settings - Settings for live stream
    trailer -
    """

    files: typing.Optional["VideoVideoFiles"] = None
    live_settings: typing.Optional["VideoLiveSettings"] = None
    trailer: typing.Optional["VideoVideoFiles"] = None


class VideoVideoImage(BaseImage):
    """VK Object VideoVideoImage"""

    with_padding: typing.Optional["BasePropertyExists"] = None


class WallAppPost(BaseModel):
    """VK Object WallAppPost

    id - Application ID
    name - Application name
    photo_130 - URL of the preview image with 130 px in width
    photo_604 - URL of the preview image with 604 px in width
    """

    id: typing.Optional[int] = None
    name: typing.Optional[str] = None
    photo_130: typing.Optional[str] = None
    photo_604: typing.Optional[str] = None


class WallAttachedNote(BaseModel):
    """VK Object WallAttachedNote

    can_comment -
    comments - Comments number
    date - Date when the note has been created in Unixtime
    id - Note ID
    owner_id - Note owner's ID
    privacy_comment -
    privacy_view -
    read_comments - Read comments number
    text - Note text
    text_wiki - Note wiki text
    title - Note title
    view_url - URL of the page with note preview
    """

    can_comment: typing.Optional[int] = None
    comments: int = None
    date: int = None
    id: int = None
    owner_id: int = None
    privacy_comment: typing.Optional[typing.List[str]] = None
    privacy_view: typing.Optional[typing.List[str]] = None
    read_comments: int = None
    text: typing.Optional[str] = None
    text_wiki: typing.Optional[str] = None
    title: str = None
    view_url: str = None


class WallCommentAttachment(BaseModel):
    """VK Object WallCommentAttachment"""

    audio: typing.Optional["AudioAudio"] = None
    doc: typing.Optional["DocsDoc"] = None
    link: typing.Optional["BaseLink"] = None
    market: typing.Optional["MarketMarketItem"] = None
    market_market_album: typing.Optional["MarketMarketAlbum"] = None
    note: typing.Optional["WallAttachedNote"] = None
    page: typing.Optional["PagesWikipageFull"] = None
    photo: typing.Optional["PhotosPhoto"] = None
    sticker: typing.Optional["BaseSticker"] = None
    type: "WallCommentAttachmentType" = None
    video: typing.Optional["VideoVideo"] = None


class WallCommentAttachmentType(enum.Enum):
    """ Attachment type """

    PHOTO = "photo"
    AUDIO = "audio"
    VIDEO = "video"
    DOC = "doc"
    LINK = "link"
    NOTE = "note"
    PAGE = "page"
    MARKET_MARKET_ALBUM = "market_market_album"
    MARKET = "market"
    STICKER = "sticker"


class PlaceType(enum.Enum):
    """ Place type """

    PLACE = "place"
    POINT = "point"


class WallGeo(BaseModel):
    """VK Object WallGeo

    coordinates - Coordinates as string. <latitude> <longtitude>
    place -
    showmap - Information whether a map is showed
    type - Place type
    """

    coordinates: typing.Optional[str] = None
    place: typing.Optional["BasePlace"] = None
    showmap: typing.Optional[int] = None
    type: typing.Optional["PlaceType"] = None


class WallGetFilter(enum.Enum):
    """ Filter to apply: 'owner' — posts by the wall owner, 'others' — posts by someone else, 'all' — posts by the wall owner and others (default), 'postponed' — timed posts (only available for calls with an 'access_token'), 'suggests' — suggested posts on a community wall """

    OWNER = "owner"
    OTHERS = "others"
    ALL = "all"
    POSTPONED = "postponed"
    SUGGESTS = "suggests"
    ARCHIVED = "archived"
    DONUT = "donut"


class WallGraffiti(BaseModel):
    """VK Object WallGraffiti

    access_key - Access key for graffiti
    height - Graffiti height
    id - Graffiti ID
    owner_id - Graffiti owner's ID
    photo_200 - URL of the preview image with 200 px in width
    photo_586 - URL of the preview image with 586 px in width
    url - Graffiti URL
    width - Graffiti width
    """

    access_key: typing.Optional[str] = None
    height: typing.Optional[int] = None
    id: typing.Optional[int] = None
    owner_id: typing.Optional[int] = None
    photo_200: typing.Optional[str] = None
    photo_586: typing.Optional[str] = None
    url: typing.Optional[str] = None
    width: typing.Optional[int] = None


class WallPostCopyright(BaseModel):
    """VK Object WallPostCopyright"""

    id: typing.Optional[int] = None
    link: str = None
    name: str = None
    type: str = None


class WallPostSource(BaseModel):
    """VK Object WallPostSource

    data - Additional data
    link -
    platform - Platform name
    type -
    url - URL to an external site used to publish the post
    """

    data: typing.Optional[str] = None
    link: typing.Optional["BaseLink"] = None
    platform: typing.Optional[str] = None
    type: typing.Optional["WallPostSourceType"] = None
    url: typing.Optional[str] = None


class WallPostSourceType(enum.Enum):
    """ Type of post source """

    VK = "vk"
    WIDGET = "widget"
    API = "api"
    RSS = "rss"
    SMS = "sms"
    MVK = "mvk"


class WallPostType(enum.Enum):
    """ Post type """

    POST = "post"
    COPY = "copy"
    REPLY = "reply"
    POSTPONE = "postpone"
    SUGGEST = "suggest"
    POST_ADS = "post_ads"
    PHOTO = "photo"
    VIDEO = "video"


class WallPostedPhoto(BaseModel):
    """VK Object WallPostedPhoto

    id - Photo ID
    owner_id - Photo owner's ID
    photo_130 - URL of the preview image with 130 px in width
    photo_604 - URL of the preview image with 604 px in width
    """

    id: typing.Optional[int] = None
    owner_id: typing.Optional[int] = None
    photo_130: typing.Optional[str] = None
    photo_604: typing.Optional[str] = None


class WallViews(BaseModel):
    """VK Object WallViews

    count - Count
    """

    count: typing.Optional[int] = None


class WallWallComment(BaseModel):
    """VK Object WallWallComment

    attachments -
    can_edit -
    date - Date when the comment has been added in Unixtime
    deleted -
    donut -
    from_id - Author ID
    id - Comment ID
    likes -
    owner_id -
    parents_stack -
    photo_id -
    pid - Photo ID
    post_id -
    real_offset - Real position of the comment
    reply_to_comment - Replied comment ID
    reply_to_user - Replied user ID
    text - Comment text
    thread -
    video_id -
    """

    attachments: typing.Optional[typing.List["WallCommentAttachment"]] = None
    can_edit: typing.Optional["BaseBoolInt"] = None
    date: int = None
    deleted: typing.Optional[bool] = None
    donut: typing.Optional["WallWallCommentDonut"] = None
    from_id: int = None
    id: int = None
    likes: typing.Optional["BaseLikesInfo"] = None
    owner_id: typing.Optional[int] = None
    parents_stack: typing.Optional[typing.List[int]] = None
    photo_id: typing.Optional[int] = None
    pid: typing.Optional[int] = None
    post_id: typing.Optional[int] = None
    real_offset: typing.Optional[int] = None
    reply_to_comment: typing.Optional[int] = None
    reply_to_user: typing.Optional[int] = None
    text: str = None
    thread: typing.Optional["CommentThread"] = None
    video_id: typing.Optional[int] = None


class WallWallCommentDonut(BaseModel):
    """VK Object WallWallCommentDonut

    is_don - Means commentator is donator
    placeholder -
    """

    is_don: typing.Optional[bool] = None
    placeholder: typing.Optional["WallWallCommentDonutPlaceholder"] = None


class WallWallCommentDonutPlaceholder(BaseModel):
    """VK Object WallWallCommentDonutPlaceholder"""

    text: str = None


class WallWallpostAttachment(BaseModel):
    """VK Object WallWallpostAttachment

    access_key - Access key for the audio
    album -
    app -
    audio -
    doc -
    event -
    graffiti -
    group -
    link -
    market -
    market_album -
    note -
    page -
    photo -
    poll -
    posted_photo -
    type -
    video -
    """

    access_key: typing.Optional[str] = None
    album: typing.Optional["PhotosPhotoAlbum"] = None
    app: typing.Optional["WallAppPost"] = None
    audio: typing.Optional["AudioAudio"] = None
    doc: typing.Optional["DocsDoc"] = None
    event: typing.Optional["EventsEventAttach"] = None
    graffiti: typing.Optional["WallGraffiti"] = None
    group: typing.Optional["GroupsGroupAttach"] = None
    link: typing.Optional["BaseLink"] = None
    market: typing.Optional["MarketMarketItem"] = None
    market_album: typing.Optional["MarketMarketAlbum"] = None
    note: typing.Optional["NotesNote"] = None
    page: typing.Optional["PagesWikipageFull"] = None
    photo: typing.Optional["PhotosPhoto"] = None
    poll: typing.Optional["PollsPoll"] = None
    posted_photo: typing.Optional["WallPostedPhoto"] = None
    type: "WallWallpostAttachmentType" = None
    video: typing.Optional["VideoVideoFull"] = None


class WallWallpostAttachmentType(enum.Enum):
    """ Attachment type """

    PHOTO = "photo"
    PHOTOS_LIST = "photos_list"
    POSTED_PHOTO = "posted_photo"
    AUDIO = "audio"
    AUDIO_PLAYLIST = "audio_playlist"
    VIDEO = "video"
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
    """VK Object WallWallpostCommentsDonut"""

    placeholder: typing.Optional["WallWallpostCommentsDonutPlaceholder"] = None


class WallWallpostCommentsDonutPlaceholder(BaseModel):
    """VK Object WallWallpostCommentsDonutPlaceholder"""

    text: str = None


class WallWallpostDonutEditMode(enum.Enum):
    """ Says what user can edit in post about donut properties """

    ALL = "all"
    DURATION = "duration"


class WallWallpostDonut(BaseModel):
    """VK Object WallWallpostDonut

    can_publish_free_copy - Says whether group admin can post free copy of this donut post
    edit_mode - Says what user can edit in post about donut properties
    is_donut - Post only for dons
    paid_duration - Value of this field need to pass in wall.post/edit in donut_paid_duration
    placeholder - If placeholder was respond, text and all attachments will be hidden
    """

    can_publish_free_copy: typing.Optional[bool] = None
    edit_mode: typing.Optional["WallWallpostDonutEditMode"] = None
    is_donut: bool = None
    paid_duration: typing.Optional[int] = None
    placeholder: typing.Optional["WallWallpostDonutPlaceholder"] = None


class WallWallpostDonutPlaceholder(BaseModel):
    """VK Object WallWallpostDonutPlaceholder"""

    text: str = None


class WidgetsCommentMedia(BaseModel):
    """VK Object WidgetsCommentMedia

    item_id - Media item ID
    owner_id - Media owner's ID
    thumb_src - URL of the preview image (type=photo only)
    type -
    """

    item_id: typing.Optional[int] = None
    owner_id: typing.Optional[int] = None
    thumb_src: typing.Optional[str] = None
    type: typing.Optional["WidgetsCommentMediaType"] = None


class WidgetsCommentMediaType(enum.Enum):
    """ Media type """

    AUDIO = "audio"
    PHOTO = "photo"
    VIDEO = "video"


class WidgetsCommentReplies(BaseModel):
    """VK Object WidgetsCommentReplies

    can_post - Information whether current user can comment the post
    count - Comments number
    replies -
    """

    can_post: typing.Optional["BaseBoolInt"] = None
    count: typing.Optional[int] = None
    replies: typing.Optional[typing.List["WidgetsCommentRepliesItem"]] = None


class WidgetsCommentRepliesItem(BaseModel):
    """VK Object WidgetsCommentRepliesItem

    cid - Comment ID
    date - Date when the comment has been added in Unixtime
    likes -
    text - Comment text
    uid - User ID
    user -
    """

    cid: typing.Optional[int] = None
    date: typing.Optional[int] = None
    likes: typing.Optional["WidgetsWidgetLikes"] = None
    text: typing.Optional[str] = None
    uid: typing.Optional[int] = None
    user: typing.Optional["UsersUserFull"] = None


class WidgetsWidgetComment(BaseModel):
    """VK Object WidgetsWidgetComment

    attachments -
    can_delete - Information whether current user can delete the comment
    comments -
    date - Date when the comment has been added in Unixtime
    from_id - Comment author ID
    id - Comment ID
    likes -
    media -
    post_source -
    post_type - Post type
    reposts -
    text - Comment text
    to_id - Wall owner
    user -
    """

    attachments: typing.Optional[typing.List["WallCommentAttachment"]] = None
    can_delete: typing.Optional["BaseBoolInt"] = None
    comments: typing.Optional["WidgetsCommentReplies"] = None
    date: int = None
    from_id: int = None
    id: int = None
    likes: typing.Optional["BaseLikesInfo"] = None
    media: typing.Optional["WidgetsCommentMedia"] = None
    post_source: typing.Optional["WallPostSource"] = None
    post_type: int = None
    reposts: typing.Optional["BaseRepostsInfo"] = None
    text: str = None
    to_id: int = None
    user: typing.Optional["UsersUserFull"] = None


class WidgetsWidgetLikes(BaseModel):
    """VK Object WidgetsWidgetLikes

    count - Likes number
    """

    count: typing.Optional[int] = None


class WidgetsWidgetPage(BaseModel):
    """VK Object WidgetsWidgetPage

    comments -
    date - Date when widgets on the page has been initialized firstly in Unixtime
    description - Page description
    id - Page ID
    likes -
    page_id - page_id parameter value
    photo - URL of the preview image
    title - Page title
    url - Page absolute URL
    """

    comments: typing.Optional["BaseObjectCount"] = None
    date: typing.Optional[int] = None
    description: typing.Optional[str] = None
    id: typing.Optional[int] = None
    likes: typing.Optional["BaseObjectCount"] = None
    page_id: typing.Optional[str] = None
    photo: typing.Optional[str] = None
    title: typing.Optional[str] = None
    url: typing.Optional[str] = None


for item in locals().copy().values():
    if inspect.isclass(item) and issubclass(item, BaseModel):
        item.update_forward_refs()
