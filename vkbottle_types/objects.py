from typing import Optional, Union, Any, List
import typing
import enum
from pydantic import BaseModel


class BaseObject(BaseModel):
    pass


class AccountAccountCounters(BaseObject):
    """VK Object Account/AccountAccountCounters

    app_requests - New app requests number
    events - New events number
    faves - New faves number
    friends - New friends requests number
    friends_suggestions - New friends suggestions number
    friends_recommendations - New friends recommendations number
    gifts - New gifts number
    groups - New groups number
    menu_discover_badge -
    messages - New messages number
    memories - New memories number
    notes - New notes number
    notifications - New notifications number
    photos - New photo tags number
    sdk - New sdk number
    """

    app_requests: Optional[int] = None
    events: Optional[int] = None
    faves: Optional[int] = None
    friends: Optional[int] = None
    friends_suggestions: Optional[int] = None
    friends_recommendations: Optional[int] = None
    gifts: Optional[int] = None
    groups: Optional[int] = None
    menu_discover_badge: Optional[int] = None
    messages: Optional[int] = None
    memories: Optional[int] = None
    notes: Optional[int] = None
    notifications: Optional[int] = None
    photos: Optional[int] = None
    sdk: Optional[int] = None


class AccountInfo(BaseObject):
    """VK Object Account/AccountInfo

    2fa_required - Two factor authentication is enabled
    country - Country code
    https_required - Information whether HTTPS-only is enabled
    intro - Information whether user has been processed intro
    mini_apps_ads_slot_id - Ads slot id for MyTarget
    lang - Language ID
    no_wall_replies - Information whether wall comments should be hidden
    own_posts_default - Information whether only owners posts should be shown
    """

    wishlists_ae_promo_banner_show: Optional["BaseBoolInt"] = None
    _2fa_required: Optional["BaseBoolInt"] = None
    country: Optional[str] = None
    https_required: Optional["BaseBoolInt"] = None
    intro: Optional["BaseBoolInt"] = None
    show_vk_apps_intro: Optional[bool] = None
    mini_apps_ads_slot_id: Optional[int] = None
    qr_promotion: Optional[int] = None
    link_redirects: Optional[typing.Dict[Any, Any]] = None
    lang: Optional[int] = None
    no_wall_replies: Optional["BaseBoolInt"] = None
    own_posts_default: Optional["BaseBoolInt"] = None
    subscriptions: Optional[List[int]] = None


class AccountNameRequest(BaseObject):
    """VK Object Account/AccountNameRequest"""

    first_name: Optional[str] = None
    id: Optional[int] = None
    last_name: Optional[str] = None
    status: Optional["AccountNameRequestStatus"] = None
    lang: Optional[str] = None
    link_href: Optional[str] = None
    link_label: Optional[str] = None


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


class AccountOffer(BaseObject):
    """VK Object Account/AccountOffer

    description - Offer description
    id - Offer ID
    img - URL of the preview image
    instruction - Instruction how to process the offer
    instruction_html - Instruction how to process the offer (HTML format)
    price - Offer price
    short_description - Offer short description
    tag - Offer tag
    title - Offer title
    currency_amount - Currency amount
    link_id - Link id
    link_type - Link type
    """

    description: Optional[str] = None
    id: Optional[int] = None
    img: Optional[str] = None
    instruction: Optional[str] = None
    instruction_html: Optional[str] = None
    price: Optional[int] = None
    short_description: Optional[str] = None
    tag: Optional[str] = None
    title: Optional[str] = None
    currency_amount: Optional[float] = None
    link_id: Optional[int] = None
    link_type: Optional[str] = None


class AccountPushConversations(BaseObject):
    """VK Object Account/AccountPushConversations

    count - Items count
    """

    count: Optional[int] = None
    items: Optional[List["AccountPushConversationsItem"]] = None


class AccountPushConversationsItem(BaseObject):
    """VK Object Account/AccountPushConversationsItem

    disabled_until - Time until that notifications are disabled in seconds
    peer_id - Peer ID
    sound - Information whether the sound are enabled
    """

    disabled_until: Optional[int] = None
    peer_id: Optional[int] = None
    sound: Optional["BaseBoolInt"] = None


class AccountPushParams(BaseObject):
    """VK Object Account/AccountPushParams"""

    msg: Optional[List["AccountPushParamsMode"]] = None
    chat: Optional[List["AccountPushParamsMode"]] = None
    like: Optional[List["AccountPushParamsSettings"]] = None
    repost: Optional[List["AccountPushParamsSettings"]] = None
    comment: Optional[List["AccountPushParamsSettings"]] = None
    mention: Optional[List["AccountPushParamsSettings"]] = None
    reply: Optional[List["AccountPushParamsOnoff"]] = None
    new_post: Optional[List["AccountPushParamsOnoff"]] = None
    wall_post: Optional[List["AccountPushParamsOnoff"]] = None
    wall_publish: Optional[List["AccountPushParamsOnoff"]] = None
    friend: Optional[List["AccountPushParamsOnoff"]] = None
    friend_found: Optional[List["AccountPushParamsOnoff"]] = None
    friend_accepted: Optional[List["AccountPushParamsOnoff"]] = None
    group_invite: Optional[List["AccountPushParamsOnoff"]] = None
    group_accepted: Optional[List["AccountPushParamsOnoff"]] = None
    birthday: Optional[List["AccountPushParamsOnoff"]] = None
    event_soon: Optional[List["AccountPushParamsOnoff"]] = None
    app_request: Optional[List["AccountPushParamsOnoff"]] = None
    sdk_open: Optional[List["AccountPushParamsOnoff"]] = None


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


class AccountPushSettings(BaseObject):
    """VK Object Account/AccountPushSettings

    disabled - Information whether notifications are disabled
    disabled_until - Time until that notifications are disabled in Unixtime
    """

    disabled: Optional["BaseBoolInt"] = None
    disabled_until: Optional[int] = None
    settings: Optional["AccountPushParams"] = None
    conversations: Optional["AccountPushConversations"] = None


class AccountUserSettingsInterest(BaseObject):
    """VK Object Account/AccountUserSettingsInterest"""

    title: Optional[str] = None
    value: Optional[str] = None


class AccountUserSettingsInterests(BaseObject):
    """VK Object Account/AccountUserSettingsInterests"""

    activities: Optional["AccountUserSettingsInterest"] = None
    interests: Optional["AccountUserSettingsInterest"] = None
    music: Optional["AccountUserSettingsInterest"] = None
    tv: Optional["AccountUserSettingsInterest"] = None
    movies: Optional["AccountUserSettingsInterest"] = None
    books: Optional["AccountUserSettingsInterest"] = None
    games: Optional["AccountUserSettingsInterest"] = None
    quotes: Optional["AccountUserSettingsInterest"] = None
    about: Optional["AccountUserSettingsInterest"] = None


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


class AdsAccesses(BaseObject):
    """VK Object Ads/AdsAccesses

    client_id - Client ID
    """

    client_id: Optional[str] = None
    role: Optional["AdsAccessRole"] = None


class AdsAccount(BaseObject):
    """VK Object Ads/AdsAccount"""

    access_role: Optional["AdsAccessRole"] = None
    account_id: Optional[int] = None
    account_status: Optional["BaseBoolInt"] = None
    account_type: Optional["AdsAccountType"] = None
    account_name: Optional[str] = None


class AdsAccountType(enum.Enum):
    """ Account type """

    GENERAL = "general"
    AGENCY = "agency"


class AdsAd(BaseObject):
    """VK Object Ads/AdsAd"""

    ad_format: Optional[int] = None
    ad_platform: Optional[Union[int, str]] = None
    all_limit: Optional[int] = None
    approved: Optional["AdsAdApproved"] = None
    campaign_id: Optional[int] = None
    category1_id: Optional[int] = None
    category2_id: Optional[int] = None
    cost_type: Optional["AdsAdCostType"] = None
    cpc: Optional[int] = None
    cpm: Optional[int] = None
    cpa: Optional[int] = None
    ocpm: Optional[int] = None
    autobidding_max_cost: Optional[int] = None
    disclaimer_medical: Optional["BaseBoolInt"] = None
    disclaimer_specialist: Optional["BaseBoolInt"] = None
    disclaimer_supplements: Optional["BaseBoolInt"] = None
    id: Optional[int] = None
    impressions_limit: Optional[int] = None
    impressions_limited: Optional["BaseBoolInt"] = None
    name: Optional[str] = None
    status: Optional["AdsAdStatus"] = None
    video: Optional["BaseBoolInt"] = None


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


class AdsAdLayout(BaseObject):
    """VK Object Ads/AdsAdLayout"""

    ad_format: Optional[int] = None
    campaign_id: Optional[int] = None
    cost_type: Optional["AdsAdCostType"] = None
    description: Optional[str] = None
    id: Optional[int] = None
    image_src: Optional[str] = None
    image_src_2x: Optional[str] = None
    link_domain: Optional[str] = None
    link_url: Optional[str] = None
    preview_link: Optional[Union[int, str]] = None
    title: Optional[str] = None
    video: Optional["BaseBoolInt"] = None


class AdsAdStatus(enum.IntEnum):
    """ Ad atatus """

    stopped = 0
    started = 1
    deleted = 2


class AdsCampaign(BaseObject):
    """VK Object Ads/AdsCampaign"""

    all_limit: Optional[str] = None
    day_limit: Optional[str] = None
    id: Optional[int] = None
    name: Optional[str] = None
    start_time: Optional[int] = None
    status: Optional["AdsCampaignStatus"] = None
    stop_time: Optional[int] = None
    type: Optional["AdsCampaignType"] = None


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


class AdsCategory(BaseObject):
    """VK Object Ads/AdsCategory

    id - Category ID
    name - Category name
    """

    id: Optional[int] = None
    name: Optional[str] = None
    subcategories: Optional[List["BaseObjectWithName"]] = None


class AdsClient(BaseObject):
    """VK Object Ads/AdsClient

    all_limit - Client's total limit, rubles
    day_limit - Client's day limit, rubles
    id - Client ID
    name - Client name
    """

    all_limit: Optional[str] = None
    day_limit: Optional[str] = None
    id: Optional[int] = None
    name: Optional[str] = None


class AdsCriteria(BaseObject):
    """VK Object Ads/AdsCriteria"""

    age_from: Optional[int] = None
    age_to: Optional[int] = None
    apps: Optional[str] = None
    apps_not: Optional[str] = None
    birthday: Optional[int] = None
    cities: Optional[str] = None
    cities_not: Optional[str] = None
    country: Optional[int] = None
    districts: Optional[str] = None
    groups: Optional[str] = None
    interest_categories: Optional[str] = None
    interests: Optional[str] = None
    paying: Optional["BaseBoolInt"] = None
    positions: Optional[str] = None
    religions: Optional[str] = None
    retargeting_groups: Optional[str] = None
    retargeting_groups_not: Optional[str] = None
    school_from: Optional[int] = None
    school_to: Optional[int] = None
    schools: Optional[str] = None
    sex: Optional["AdsCriteriaSex"] = None
    stations: Optional[str] = None
    statuses: Optional[str] = None
    streets: Optional[str] = None
    travellers: Optional["BasePropertyExists"] = None
    uni_from: Optional[int] = None
    uni_to: Optional[int] = None
    user_browsers: Optional[str] = None
    user_devices: Optional[str] = None
    user_os: Optional[str] = None


class AdsCriteriaSex(enum.IntEnum):
    """ Sex """

    any = 0
    male = 1
    female = 2


class AdsDemoStats(BaseObject):
    """VK Object Ads/AdsDemoStats

    id - Object ID
    """

    id: Optional[int] = None
    stats: Optional["AdsDemostatsFormat"] = None
    type: Optional["AdsObjectType"] = None


class AdsDemostatsFormat(BaseObject):
    """VK Object Ads/AdsDemostatsFormat

    day - Day as YYYY-MM-DD
    month - Month as YYYY-MM
    overall - 1 if period=overall
    """

    age: Optional[List["AdsStatsAge"]] = None
    cities: Optional[List["AdsStatsCities"]] = None
    day: Optional[str] = None
    month: Optional[str] = None
    overall: Optional[int] = None
    sex: Optional[List["AdsStatsSex"]] = None
    sex_age: Optional[List["AdsStatsSexAge"]] = None


class AdsFloodStats(BaseObject):
    """VK Object Ads/AdsFloodStats

    left - Requests left
    refresh - Time to refresh in seconds
    """

    left: Optional[int] = None
    refresh: Optional[int] = None


class AdsLinkStatus(BaseObject):
    """VK Object Ads/AdsLinkStatus

    description - Reject reason
    redirect_url - URL
    status - Link status
    """

    description: Optional[str] = None
    redirect_url: Optional[str] = None
    status: Optional[str] = None


class AdsLookalikeRequest(BaseObject):
    """VK Object Ads/AdsLookalikeRequest

    id - Lookalike request ID
    create_time - Lookalike request create time, as Unixtime
    update_time - Lookalike request update time, as Unixtime
    scheduled_delete_time - Time by which lookalike request would be deleted, as Unixtime
    status - Lookalike request status
    source_type - Lookalike request source type
    source_retargeting_group_id - Retargeting group id, which was used as lookalike seed
    source_name - Lookalike request seed name (retargeting group name)
    audience_count - Lookalike request seed audience size
    """

    id: Optional[int] = None
    create_time: Optional[int] = None
    update_time: Optional[int] = None
    scheduled_delete_time: Optional[int] = None
    status: Optional[str] = None
    source_type: Optional[str] = None
    source_retargeting_group_id: Optional[int] = None
    source_name: Optional[str] = None
    audience_count: Optional[int] = None
    save_audience_levels: Optional[List["AdsLookalikeRequestSaveAudienceLevel"]] = None


class AdsLookalikeRequestSaveAudienceLevel(BaseObject):
    """VK Object Ads/AdsLookalikeRequestSaveAudienceLevel

    level - Save audience level id, which is used in save audience queries
    audience_count - Saved audience audience size for according level
    """

    level: Optional[int] = None
    audience_count: Optional[int] = None


class AdsMusician(BaseObject):
    """VK Object Ads/AdsMusician"""

    id: Optional[int] = None
    name: Optional[str] = None


class AdsObjectType(enum.Enum):
    """ Object type """

    AD = "ad"
    CAMPAIGN = "campaign"
    CLIENT = "client"
    OFFICE = "office"


class AdsParagraphs(BaseObject):
    """VK Object Ads/AdsParagraphs

    paragraph - Rules paragraph
    """

    paragraph: Optional[str] = None


class AdsPromotedPostReach(BaseObject):
    """VK Object Ads/AdsPromotedPostReach

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

    hide: Optional[int] = None
    id: Optional[int] = None
    join_group: Optional[int] = None
    links: Optional[int] = None
    reach_subscribers: Optional[int] = None
    reach_total: Optional[int] = None
    report: Optional[int] = None
    to_group: Optional[int] = None
    unsubscribe: Optional[int] = None
    video_views_100p: Optional[int] = None
    video_views_25p: Optional[int] = None
    video_views_3s: Optional[int] = None
    video_views_50p: Optional[int] = None
    video_views_75p: Optional[int] = None
    video_views_start: Optional[int] = None


class AdsRejectReason(BaseObject):
    """VK Object Ads/AdsRejectReason

    comment - Comment text
    """

    comment: Optional[str] = None
    rules: Optional[List["AdsRules"]] = None


class AdsRules(BaseObject):
    """VK Object Ads/AdsRules

    title - Comment
    """

    paragraphs: Optional[List["AdsParagraphs"]] = None
    title: Optional[str] = None


class AdsStats(BaseObject):
    """VK Object Ads/AdsStats

    id - Object ID
    """

    id: Optional[int] = None
    stats: Optional["AdsStatsFormat"] = None
    type: Optional["AdsObjectType"] = None
    views_times: Optional["AdsStatsViewsTimes"] = None


class AdsStatsAge(BaseObject):
    """VK Object Ads/AdsStatsAge

    clicks_rate - Clicks rate
    impressions_rate - Impressions rate
    value - Age interval
    """

    clicks_rate: Optional[float] = None
    impressions_rate: Optional[float] = None
    value: Optional[str] = None


class AdsStatsCities(BaseObject):
    """VK Object Ads/AdsStatsCities

    clicks_rate - Clicks rate
    impressions_rate - Impressions rate
    name - City name
    value - City ID
    """

    clicks_rate: Optional[float] = None
    impressions_rate: Optional[float] = None
    name: Optional[str] = None
    value: Optional[int] = None


class AdsStatsFormat(BaseObject):
    """VK Object Ads/AdsStatsFormat

    clicks - Clicks number
    day - Day as YYYY-MM-DD
    impressions - Impressions number
    join_rate - Events number
    month - Month as YYYY-MM
    overall - 1 if period=overall
    reach - Reach
    spent - Spent funds
    video_clicks_site - Clickthoughs to the advertised site
    video_views - Video views number
    video_views_full - Video views (full video)
    video_views_half - Video views (half of video)
    """

    clicks: Optional[int] = None
    day: Optional[str] = None
    impressions: Optional[int] = None
    join_rate: Optional[int] = None
    month: Optional[str] = None
    overall: Optional[int] = None
    reach: Optional[int] = None
    spent: Optional[int] = None
    video_clicks_site: Optional[int] = None
    video_views: Optional[int] = None
    video_views_full: Optional[int] = None
    video_views_half: Optional[int] = None


class AdsStatsSex(BaseObject):
    """VK Object Ads/AdsStatsSex

    clicks_rate - Clicks rate
    impressions_rate - Impressions rate
    """

    clicks_rate: Optional[float] = None
    impressions_rate: Optional[float] = None
    value: Optional["AdsStatsSexValue"] = None


class AdsStatsSexAge(BaseObject):
    """VK Object Ads/AdsStatsSexAge"""

    clicks_rate: Optional[float] = None
    impressions_rate: Optional[float] = None
    value: Optional[str] = None


class AdsStatsSexValue(enum.Enum):
    """ Sex """

    F = "f"
    M = "m"


class AdsStatsViewsTimes(BaseObject):
    """VK Object Ads/AdsStatsViewsTimes"""

    views_ads_times_1: Optional[int] = None
    views_ads_times_2: Optional[int] = None
    views_ads_times_3: Optional[int] = None
    views_ads_times_4: Optional[int] = None
    views_ads_times_5: Optional[str] = None
    views_ads_times_6: Optional[int] = None
    views_ads_times_7: Optional[int] = None
    views_ads_times_8: Optional[int] = None
    views_ads_times_9: Optional[int] = None
    views_ads_times_10: Optional[int] = None
    views_ads_times_11_plus: Optional[int] = None


class AdsTargSettings(AdsCriteria):
    """VK Object Ads/AdsTargSettings

    id - Ad ID
    campaign_id - Campaign ID
    """

    id: Optional[int] = None
    campaign_id: Optional[int] = None


class AdsTargStats(BaseObject):
    """VK Object Ads/AdsTargStats

    audience_count - Audience
    recommended_cpc - Recommended CPC value for 50% reach (old format)
    recommended_cpm - Recommended CPM value for 50% reach (old format)
    recommended_cpc_50 - Recommended CPC value for 50% reach
    recommended_cpm_50 - Recommended CPM value for 50% reach
    recommended_cpc_70 - Recommended CPC value for 70% reach
    recommended_cpm_70 - Recommended CPM value for 70% reach
    recommended_cpc_90 - Recommended CPC value for 90% reach
    recommended_cpm_90 - Recommended CPM value for 90% reach
    """

    audience_count: Optional[int] = None
    recommended_cpc: Optional[float] = None
    recommended_cpm: Optional[float] = None
    recommended_cpc_50: Optional[float] = None
    recommended_cpm_50: Optional[float] = None
    recommended_cpc_70: Optional[float] = None
    recommended_cpm_70: Optional[float] = None
    recommended_cpc_90: Optional[float] = None
    recommended_cpm_90: Optional[float] = None


class AdsTargSuggestions(BaseObject):
    """VK Object Ads/AdsTargSuggestions

    id - Object ID
    name - Object name
    """

    id: Optional[int] = None
    name: Optional[str] = None


class AdsTargSuggestionsCities(BaseObject):
    """VK Object Ads/AdsTargSuggestionsCities

    id - Object ID
    name - Object name
    parent - Parent object
    """

    id: Optional[int] = None
    name: Optional[str] = None
    parent: Optional[str] = None


class AdsTargSuggestionsRegions(BaseObject):
    """VK Object Ads/AdsTargSuggestionsRegions

    id - Object ID
    name - Object name
    type - Object type
    """

    id: Optional[int] = None
    name: Optional[str] = None
    type: Optional[str] = None


class AdsTargSuggestionsSchools(BaseObject):
    """VK Object Ads/AdsTargSuggestionsSchools"""

    desc: Optional[str] = None
    id: Optional[int] = None
    name: Optional[str] = None
    parent: Optional[str] = None
    type: Optional["AdsTargSuggestionsSchoolsType"] = None


class AdsTargSuggestionsSchoolsType(enum.Enum):
    """ School type """

    SCHOOL = "school"
    UNIVERSITY = "university"
    FACULTY = "faculty"
    CHAIR = "chair"


class AdsTargetGroup(BaseObject):
    """VK Object Ads/AdsTargetGroup

    audience_count - Audience
    domain - Site domain
    id - Group ID
    lifetime - Number of days for user to be in group
    name - Group name
    pixel - Pixel code
    """

    audience_count: Optional[int] = None
    domain: Optional[str] = None
    id: Optional[int] = None
    lifetime: Optional[int] = None
    name: Optional[str] = None
    pixel: Optional[str] = None


class AdsUsers(BaseObject):
    """VK Object Ads/AdsUsers

    user_id - User ID
    """

    accesses: Optional[List["AdsAccesses"]] = None
    user_id: Optional[int] = None


class AppsAppLeaderboardType(enum.IntEnum):
    """ Leaderboard type """

    not_supported = 0
    levels = 1
    points = 2


class AppsAppMin(BaseObject):
    """VK Object Apps/AppsAppMin"""

    type: Optional["AppsAppType"] = None
    id: Optional[int] = None
    title: Optional[str] = None
    author_owner_id: Optional[int] = None
    is_installed: Optional[bool] = None
    icon_139: Optional[str] = None
    icon_150: Optional[str] = None
    icon_278: Optional[str] = None
    icon_576: Optional[str] = None
    background_loader_color: Optional[str] = None
    loader_icon: Optional[str] = None
    icon_75: Optional[str] = None


class AppsApp(AppsAppMin):
    """VK Object Apps/AppsApp"""

    author_url: Optional[str] = None
    banner_1120: Optional[str] = None
    banner_560: Optional[str] = None
    icon_16: Optional[str] = None
    is_new: Optional["BaseBoolInt"] = None
    push_enabled: Optional["BaseBoolInt"] = None
    screen_orientation: Optional[int] = None
    friends: Optional[List[int]] = None
    catalog_position: Optional[int] = None
    description: Optional[str] = None
    genre: Optional[str] = None
    genre_id: Optional[int] = None
    international: Optional[bool] = None
    is_in_catalog: Optional[int] = None
    leaderboard_type: Optional["AppsAppLeaderboardType"] = None
    members_count: Optional[int] = None
    platform_id: Optional[str] = None
    published_date: Optional[int] = None
    screen_name: Optional[str] = None
    section: Optional[str] = None


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


class AppsLeaderboard(BaseObject):
    """VK Object Apps/AppsLeaderboard

    level - Level
    points - Points number
    score - Score number
    user_id - User ID
    """

    level: Optional[int] = None
    points: Optional[int] = None
    score: Optional[int] = None
    user_id: Optional[int] = None


class AppsScope(BaseObject):
    """VK Object Apps/AppsScope

    name - Scope name
    title - Scope title
    """

    name: Optional[str] = None
    title: Optional[str] = None


class AudioAudio(BaseObject):
    """VK Object Audio/AudioAudio"""

    artist: Optional[str] = None
    id: Optional[int] = None
    title: Optional[str] = None
    url: Optional[str] = None
    duration: Optional[int] = None
    date: Optional[int] = None
    album_id: Optional[int] = None
    genre_id: Optional[int] = None
    performer: Optional[str] = None


class BaseBoolInt(enum.IntEnum):
    """ BaseBoolInt enum """

    no = 0
    yes = 1


class BaseCity(BaseObject):
    """VK Object Base/BaseCity

    id - City ID
    title - City title
    """

    id: Optional[int] = None
    title: Optional[str] = None


class BaseCommentsInfo(BaseObject):
    """VK Object Base/BaseCommentsInfo

    can_post - Information whether current user can comment the post
    count - Comments number
    groups_can_post - Information whether groups can comment the post
    """

    can_post: Optional["BaseBoolInt"] = None
    count: Optional[int] = None
    groups_can_post: Optional[bool] = None


class BaseCountry(BaseObject):
    """VK Object Base/BaseCountry

    id - Country ID
    title - Country title
    """

    id: Optional[int] = None
    title: Optional[str] = None


class BaseCropPhoto(BaseObject):
    """VK Object Base/BaseCropPhoto"""

    photo: Optional["PhotosPhoto"] = None
    crop: Optional["BaseCropPhotoCrop"] = None
    rect: Optional["BaseCropPhotoRect"] = None


class BaseCropPhotoCrop(BaseObject):
    """VK Object Base/BaseCropPhotoCrop

    x - Coordinate X of the left upper corner
    y - Coordinate Y of the left upper corner
    x2 - Coordinate X of the right lower corner
    y2 - Coordinate Y of the right lower corner
    """

    x: Optional[float] = None
    y: Optional[float] = None
    x2: Optional[float] = None
    y2: Optional[float] = None


class BaseCropPhotoRect(BaseObject):
    """VK Object Base/BaseCropPhotoRect

    x - Coordinate X of the left upper corner
    y - Coordinate Y of the left upper corner
    x2 - Coordinate X of the right lower corner
    y2 - Coordinate Y of the right lower corner
    """

    x: Optional[float] = None
    y: Optional[float] = None
    x2: Optional[float] = None
    y2: Optional[float] = None


class BaseError(BaseObject):
    """VK Object Base/BaseError

    error_code - Error code
    error_msg - Error message
    error_text - Localized error message
    """

    error_code: Optional[int] = None
    error_msg: Optional[str] = None
    error_text: Optional[str] = None
    request_params: Optional[List["BaseRequestParam"]] = None


class BaseGeo(BaseObject):
    """VK Object Base/BaseGeo

    showmap - Information whether a map is showed
    type - Place type
    """

    coordinates: Optional["BaseGeoCoordinates"] = None
    place: Optional["BasePlace"] = None
    showmap: Optional[int] = None
    type: Optional[str] = None


class BaseGeoCoordinates(BaseObject):
    """VK Object Base/BaseGeoCoordinates"""

    latitude: Optional[float] = None
    longitude: Optional[float] = None


class BaseGradientPoint(BaseObject):
    """VK Object Base/BaseGradientPoint

    color - Hex color code without #
    position - Point position
    """

    color: Optional[str] = None
    position: Optional[float] = None


class BaseImage(BaseObject):
    """VK Object Base/BaseImage

    height - Image height
    url - Image url
    width - Image width
    """

    id: Optional[str] = None
    height: Optional[int] = None
    url: Optional[str] = None
    width: Optional[int] = None


class BaseLikes(BaseObject):
    """VK Object Base/BaseLikes

    count - Likes number
    user_likes - Information whether current user likes the photo
    """

    count: Optional[int] = None
    user_likes: Optional["BaseBoolInt"] = None


class BaseLikesInfo(BaseObject):
    """VK Object Base/BaseLikesInfo

    can_like - Information whether current user can like the post
    can_publish - Information whether current user can repost
    count - Likes number
    user_likes - Information whether current uer has liked the post
    """

    can_like: Optional["BaseBoolInt"] = None
    can_publish: Optional["BaseBoolInt"] = None
    count: Optional[int] = None
    user_likes: Optional[int] = None


class BaseLink(BaseObject):
    """VK Object Base/BaseLink

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

    application: Optional["BaseLinkApplication"] = None
    button: Optional["BaseLinkButton"] = None
    caption: Optional[str] = None
    description: Optional[str] = None
    id: Optional[str] = None
    is_favorite: Optional[bool] = None
    photo: Optional["PhotosPhoto"] = None
    preview_page: Optional[str] = None
    preview_url: Optional[str] = None
    product: Optional["BaseLinkProduct"] = None
    rating: Optional["BaseLinkRating"] = None
    title: Optional[str] = None
    url: Optional[str] = None
    target_object: Optional["LinkTargetObject"] = None
    is_external: Optional[bool] = None
    video: Optional["VideoVideo"] = None


class BaseLinkApplication(BaseObject):
    """VK Object Base/BaseLinkApplication

    app_id - Application Id
    """

    app_id: Optional[float] = None
    store: Optional["BaseLinkApplicationStore"] = None


class BaseLinkApplicationStore(BaseObject):
    """VK Object Base/BaseLinkApplicationStore

    id - Store Id
    name - Store name
    """

    id: Optional[float] = None
    name: Optional[str] = None


class BaseLinkButton(BaseObject):
    """VK Object Base/BaseLinkButton

    action - Button action
    title - Button title
    block_id - Target block id
    section_id - Target section id
    owner_id - Owner id
    icon - Button icon name, e.g. 'phone' or 'gift'
    """

    action: Optional["BaseLinkButtonAction"] = None
    title: Optional[str] = None
    block_id: Optional[str] = None
    section_id: Optional[str] = None
    owner_id: Optional[int] = None
    icon: Optional[str] = None
    style: Optional["BaseLinkButtonStyle"] = None


class BaseLinkButtonAction(BaseObject):
    """VK Object Base/BaseLinkButtonAction"""

    type: Optional["BaseLinkButtonActionType"] = None
    url: Optional[str] = None
    consume_reason: Optional[str] = None


class BaseLinkButtonActionType(enum.Enum):
    """ Action type """

    OPEN_URL = "open_url"


class BaseLinkButtonStyle(enum.Enum):
    """ Button style """


class BaseLinkProduct(BaseObject):
    """VK Object Base/BaseLinkProduct"""

    price: Optional["MarketPrice"] = None
    merchant: Optional[str] = None
    orders_count: Optional[int] = None


class BaseLinkRating(BaseObject):
    """VK Object Base/BaseLinkRating

    reviews_count - Count of reviews
    stars - Count of stars
    """

    reviews_count: Optional[int] = None
    stars: Optional[float] = None


class BaseMessageError(BaseObject):
    """VK Object Base/BaseMessageError

    code - Error code
    description - Error message
    """

    code: Optional[int] = None
    description: Optional[str] = None


class BaseObject(BaseObject):
    """VK Object Base/BaseObject

    id - Object ID
    title - Object title
    """

    id: Optional[int] = None
    title: Optional[str] = None


class BaseObjectCount(BaseObject):
    """VK Object Base/BaseObjectCount

    count - Items count
    """

    count: Optional[int] = None


class BaseObjectWithName(BaseObject):
    """VK Object Base/BaseObjectWithName

    id - Object ID
    name - Object name
    """

    id: Optional[int] = None
    name: Optional[str] = None


class BasePlace(BaseObject):
    """VK Object Base/BasePlace"""

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


class BasePropertyExists(enum.IntEnum):
    """ BasePropertyExists enum """

    property_exists = 1


class BaseRepostsInfo(BaseObject):
    """VK Object Base/BaseRepostsInfo

    count - Reposts number
    user_reposted - Information whether current user has reposted the post
    """

    count: Optional[int] = None
    user_reposted: Optional[int] = None


class BaseRequestParam(BaseObject):
    """VK Object Base/BaseRequestParam"""

    key: Optional[str] = None
    value: Optional[str] = None


class BaseSex(enum.IntEnum):
    """ BaseSex enum """

    unknown = 0
    female = 1
    male = 2


class BaseSticker(BaseObject):
    """VK Object Base/BaseSticker

    sticker_id - Sticker ID
    product_id - Pack ID
    animation_url - URL of sticker animation script
    animations - Array of sticker animation script objects
    is_allowed - Information whether the sticker is allowed
    """

    sticker_id: Optional[int] = None
    product_id: Optional[int] = None
    images: Optional[List["BaseImage"]] = None
    images_with_background: Optional[List["BaseImage"]] = None
    animation_url: Optional[str] = None
    animations: Optional[List["BaseStickerAnimation"]] = None
    is_allowed: Optional[bool] = None


class BaseStickerAnimation(BaseObject):
    """VK Object Base/BaseStickerAnimation

    type - Type of animation script
    url - URL of animation script
    """

    type: Optional[str] = None
    url: Optional[str] = None


class BaseUploadServer(BaseObject):
    """VK Object Base/BaseUploadServer"""

    upload_url: Optional[str] = None


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


class BaseUserId(BaseObject):
    """VK Object Base/BaseUserId"""

    user_id: Optional[int] = None


class BoardDefaultOrder(enum.IntEnum):
    """ Sort type """

    desc_updated = 1
    desc_created = 2
    asc_updated = -1
    asc_created = -2


class BoardTopic(BaseObject):
    """VK Object Board/BoardTopic

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

    comments: Optional[int] = None
    created: Optional[int] = None
    created_by: Optional[int] = None
    id: Optional[int] = None
    is_closed: Optional["BaseBoolInt"] = None
    is_fixed: Optional["BaseBoolInt"] = None
    title: Optional[str] = None
    updated: Optional[int] = None
    updated_by: Optional[int] = None


class BoardTopicComment(BaseObject):
    """VK Object Board/BoardTopicComment

    date - Date when the comment has been added in Unixtime
    from_id - Author ID
    id - Comment ID
    real_offset - Real position of the comment
    text - Comment text
    can_edit - Information whether current user can edit the comment
    """

    attachments: Optional[List["WallCommentAttachment"]] = None
    date: Optional[int] = None
    from_id: Optional[int] = None
    id: Optional[int] = None
    real_offset: Optional[int] = None
    text: Optional[str] = None
    can_edit: Optional["BaseBoolInt"] = None
    likes: Optional["BaseLikesInfo"] = None


class BoardTopicPoll(BaseObject):
    """VK Object Board/BoardTopicPoll

    answer_id - Current user's answer ID
    created - Date when poll has been created in Unixtime
    is_closed - Information whether the poll is closed
    owner_id - Poll owner's ID
    poll_id - Poll ID
    question - Poll question
    votes - Votes number
    """

    answer_id: Optional[int] = None
    answers: Optional[List["PollsAnswer"]] = None
    created: Optional[int] = None
    is_closed: Optional["BaseBoolInt"] = None
    owner_id: Optional[int] = None
    poll_id: Optional[int] = None
    question: Optional[str] = None
    votes: Optional[str] = None


class CallbackBoardPostDelete(BaseObject):
    """VK Object Callback/CallbackBoardPostDelete"""

    topic_owner_id: Optional[int] = None
    topic_id: Optional[int] = None
    id: Optional[int] = None


class CallbackConfirmationMessage(BaseObject):
    """VK Object Callback/CallbackConfirmationMessage"""

    type: Optional["CallbackMessageType"] = None
    group_id: Optional[int] = None
    secret: Optional[str] = None


class CallbackGroupChangePhoto(BaseObject):
    """VK Object Callback/CallbackGroupChangePhoto"""

    user_id: Optional[int] = None
    photo: Optional["PhotosPhoto"] = None


class CallbackGroupChangeSettings(BaseObject):
    """VK Object Callback/CallbackGroupChangeSettings"""

    user_id: Optional[int] = None
    self: Optional["BaseBoolInt"] = None


class CallbackGroupJoin(BaseObject):
    """VK Object Callback/CallbackGroupJoin"""

    user_id: Optional[int] = None
    join_type: Optional["CallbackGroupJoinType"] = None


class CallbackGroupJoinType(enum.Enum):
    """ CallbackGroupJoinType enum """

    JOIN = "join"
    UNSURE = "unsure"
    ACCEPTED = "accepted"
    APPROVED = "approved"
    REQUEST = "request"


class CallbackGroupLeave(BaseObject):
    """VK Object Callback/CallbackGroupLeave"""

    user_id: Optional[int] = None
    self: Optional["BaseBoolInt"] = None


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


class CallbackGroupOfficersEdit(BaseObject):
    """VK Object Callback/CallbackGroupOfficersEdit"""

    admin_id: Optional[int] = None
    user_id: Optional[int] = None
    level_old: Optional["CallbackGroupOfficerRole"] = None
    level_new: Optional["CallbackGroupOfficerRole"] = None


class CallbackGroupSettingsChanges(BaseObject):
    """VK Object Callback/CallbackGroupSettingsChanges"""

    title: Optional[str] = None
    description: Optional[str] = None
    access: Optional["GroupsGroupIsClosed"] = None
    screen_name: Optional[str] = None
    public_category: Optional[int] = None
    public_subcategory: Optional[int] = None
    age_limits: Optional["GroupsGroupFullAgeLimits"] = None
    website: Optional[str] = None
    enable_status_default: Optional["GroupsGroupWall"] = None
    enable_audio: Optional["GroupsGroupAudio"] = None
    enable_video: Optional["GroupsGroupVideo"] = None
    enable_photo: Optional["GroupsGroupPhotos"] = None
    enable_market: Optional["CallbackGroupMarket"] = None


class CallbackLikeAddRemove(BaseObject):
    """VK Object Callback/CallbackLikeAddRemove"""

    liker_id: Optional[int] = None
    object_type: Optional[str] = None
    object_owner_id: Optional[int] = None
    object_id: Optional[int] = None
    post_id: Optional[int] = None
    thread_reply_id: Optional[int] = None


class CallbackMarketComment(BaseObject):
    """VK Object Callback/CallbackMarketComment"""

    id: Optional[int] = None
    from_id: Optional[int] = None
    date: Optional[int] = None
    text: Optional[str] = None
    market_owner_od: Optional[int] = None
    photo_id: Optional[int] = None


class CallbackMarketCommentDelete(BaseObject):
    """VK Object Callback/CallbackMarketCommentDelete"""

    owner_id: Optional[int] = None
    id: Optional[int] = None
    user_id: Optional[int] = None
    item_id: Optional[int] = None


class CallbackMessageAllow(BaseObject):
    """VK Object Callback/CallbackMessageAllow"""

    user_id: Optional[int] = None
    key: Optional[str] = None


class CallbackMessageBase(BaseObject):
    """VK Object Callback/CallbackMessageBase"""

    type: Optional["CallbackMessageType"] = None
    object: Optional[typing.Dict[Any, Any]] = None
    group_id: Optional[int] = None


class CallbackMessageDeny(BaseObject):
    """VK Object Callback/CallbackMessageDeny"""

    user_id: Optional[int] = None


class CallbackMessageType(enum.Enum):
    """ CallbackMessageType enum """

    CONFIRMATION = "confirmation"
    GROUP_CHANGE_PHOTO = "group_change_photo"
    GROUP_CHANGE_SETTINGS = "group_change_settings"
    GROUP_OFFICERS_EDIT = "group_officers_edit"
    LEAD_FORMS_NEW = "lead_forms_new"
    MARKET_COMMENT_DELETE = "market_comment_delete"
    MARKET_COMMENT_EDIT = "market_comment_edit"
    MARKET_COMMENT_RESTORE = "market_comment_restore"
    MESSAGE_ALLOW = "message_allow"
    MESSAGE_DENY = "message_deny"
    MESSAGE_READ = "message_read"
    MESSAGE_REPLY = "message_reply"
    MESSAGE_TYPING_STATE = "message_typing_state"
    MESSAGES_EDIT = "messages_edit"
    PHOTO_COMMENT_DELETE = "photo_comment_delete"
    PHOTO_COMMENT_EDIT = "photo_comment_edit"
    PHOTO_COMMENT_RESTORE = "photo_comment_restore"
    POLL_VOTE_NEW = "poll_vote_new"
    USER_BLOCK = "user_block"
    USER_UNBLOCK = "user_unblock"
    VIDEO_COMMENT_DELETE = "video_comment_delete"
    VIDEO_COMMENT_EDIT = "video_comment_edit"
    VIDEO_COMMENT_RESTORE = "video_comment_restore"
    WALL_REPLY_DELETE = "wall_reply_delete"
    WALL_REPLY_RESTORE = "wall_reply_restore"
    WALL_REPOST = "wall_repost"


class CallbackPhotoComment(BaseObject):
    """VK Object Callback/CallbackPhotoComment"""

    id: Optional[int] = None
    from_id: Optional[int] = None
    date: Optional[int] = None
    text: Optional[str] = None
    photo_owner_od: Optional[int] = None


class CallbackPhotoCommentDelete(BaseObject):
    """VK Object Callback/CallbackPhotoCommentDelete"""

    id: Optional[int] = None
    owner_id: Optional[int] = None
    user_id: Optional[int] = None
    photo_id: Optional[int] = None


class CallbackPollVoteNew(BaseObject):
    """VK Object Callback/CallbackPollVoteNew"""

    owner_id: Optional[int] = None
    poll_id: Optional[int] = None
    option_id: Optional[int] = None
    user_id: Optional[int] = None


class CallbackQrScan(BaseObject):
    """VK Object Callback/CallbackQrScan"""

    user_id: Optional[int] = None
    data: Optional[str] = None
    type: Optional[str] = None
    subtype: Optional[str] = None
    reread: Optional[bool] = None


class CallbackUserBlock(BaseObject):
    """VK Object Callback/CallbackUserBlock"""

    admin_id: Optional[int] = None
    user_id: Optional[int] = None
    unblock_date: Optional[int] = None
    reason: Optional[int] = None
    comment: Optional[str] = None


class CallbackUserUnblock(BaseObject):
    """VK Object Callback/CallbackUserUnblock"""

    admin_id: Optional[int] = None
    user_id: Optional[int] = None
    by_end_date: Optional[int] = None


class CallbackVideoComment(BaseObject):
    """VK Object Callback/CallbackVideoComment"""

    id: Optional[int] = None
    from_id: Optional[int] = None
    date: Optional[int] = None
    text: Optional[str] = None
    video_owner_od: Optional[int] = None


class CallbackVideoCommentDelete(BaseObject):
    """VK Object Callback/CallbackVideoCommentDelete"""

    id: Optional[int] = None
    owner_id: Optional[int] = None
    user_id: Optional[int] = None
    video_id: Optional[int] = None


class CallbackWallCommentDelete(BaseObject):
    """VK Object Callback/CallbackWallCommentDelete"""

    owner_id: Optional[int] = None
    id: Optional[int] = None
    user_id: Optional[int] = None
    post_id: Optional[int] = None


class CommentThread(BaseObject):
    """VK Object Comment/CommentThread

    can_post - Information whether current user can comment the post
    count - Comments number
    groups_can_post - Information whether groups can comment the post
    show_reply_button - Information whether recommended to display reply button
    """

    can_post: Optional[bool] = None
    count: Optional[int] = None
    groups_can_post: Optional[bool] = None
    items: Optional[List["WallWallComment"]] = None
    show_reply_button: Optional[bool] = None


class DatabaseCity(BaseObject):
    """VK Object Database/DatabaseCity

    area - Area title
    region - Region title
    important - Information whether the city is included in important cities list
    """

    area: Optional[str] = None
    region: Optional[str] = None
    important: Optional["BaseBoolInt"] = None


class DatabaseFaculty(BaseObject):
    """VK Object Database/DatabaseFaculty

    id - Faculty ID
    title - Faculty title
    """

    id: Optional[int] = None
    title: Optional[str] = None


class DatabaseRegion(BaseObject):
    """VK Object Database/DatabaseRegion

    id - Region ID
    title - Region title
    """

    id: Optional[int] = None
    title: Optional[str] = None


class DatabaseSchool(BaseObject):
    """VK Object Database/DatabaseSchool

    id - School ID
    title - School title
    """

    id: Optional[int] = None
    title: Optional[str] = None


class DatabaseStation(BaseObject):
    """VK Object Database/DatabaseStation

    city_id - City ID
    color - Hex color code without #
    id - Station ID
    name - Station name
    """

    city_id: Optional[int] = None
    color: Optional[str] = None
    id: Optional[int] = None
    name: Optional[str] = None


class DatabaseUniversity(BaseObject):
    """VK Object Database/DatabaseUniversity

    id - University ID
    title - University title
    """

    id: Optional[int] = None
    title: Optional[str] = None


class DocsDoc(BaseObject):
    """VK Object Docs/DocsDoc"""

    id: Optional[int] = None
    owner_id: Optional[int] = None
    title: Optional[str] = None
    size: Optional[int] = None
    ext: Optional[str] = None
    url: Optional[str] = None
    date: Optional[int] = None
    type: Optional[int] = None
    preview: Optional["DocsDocPreview"] = None
    is_licensed: Optional["BaseBoolInt"] = None
    access_key: Optional[str] = None
    tags: Optional[List[str]] = None


class DocsDocAttachmentType(enum.Enum):
    """ Doc attachment type """

    DOC = "doc"
    GRAFFITI = "graffiti"
    AUDIO_MESSAGE = "audio_message"


class DocsDocPreview(BaseObject):
    """VK Object Docs/DocsDocPreview"""

    audio_msg: Optional["DocsDocPreviewAudioMsg"] = None
    graffiti: Optional["DocsDocPreviewGraffiti"] = None
    photo: Optional["DocsDocPreviewPhoto"] = None
    video: Optional["DocsDocPreviewVideo"] = None


class DocsDocPreviewAudioMsg(BaseObject):
    """VK Object Docs/DocsDocPreviewAudioMsg

    duration - Audio message duration in seconds
    link_mp3 - MP3 file URL
    link_ogg - OGG file URL
    """

    duration: Optional[int] = None
    link_mp3: Optional[str] = None
    link_ogg: Optional[str] = None
    waveform: Optional[List[int]] = None


class DocsDocPreviewGraffiti(BaseObject):
    """VK Object Docs/DocsDocPreviewGraffiti

    src - Graffiti file URL
    width - Graffiti width
    height - Graffiti height
    """

    src: Optional[str] = None
    width: Optional[int] = None
    height: Optional[int] = None


class DocsDocPreviewPhoto(BaseObject):
    """VK Object Docs/DocsDocPreviewPhoto"""

    sizes: Optional[List["DocsDocPreviewPhotoSizes"]] = None


class DocsDocPreviewPhotoSizes(BaseObject):
    """VK Object Docs/DocsDocPreviewPhotoSizes

    src - URL of the image
    width - Width in px
    height - Height in px
    """

    src: Optional[str] = None
    width: Optional[int] = None
    height: Optional[int] = None
    type: Optional["PhotosPhotoSizesType"] = None


class DocsDocPreviewVideo(BaseObject):
    """VK Object Docs/DocsDocPreviewVideo

    src - Video URL
    width - Video's width in pixels
    height - Video's height in pixels
    file_size - Video file size in bites
    """

    src: Optional[str] = None
    width: Optional[int] = None
    height: Optional[int] = None
    file_size: Optional[int] = None


class DocsDocTypes(BaseObject):
    """VK Object Docs/DocsDocTypes

    id - Doc type ID
    name - Doc type title
    count - Number of docs
    """

    id: Optional[int] = None
    name: Optional[str] = None
    count: Optional[int] = None


class DocsDocUploadResponse(BaseObject):
    """VK Object Docs/DocsDocUploadResponse

    file - Uploaded file data
    """

    file: Optional[str] = None


class EventsEventAttach(BaseObject):
    """VK Object Events/EventsEventAttach

    address - address of event
    button_text - text of attach
    friends - array of friends ids
    id - event ID
    is_favorite - is favorite
    member_status - Current user's member status
    text - text of attach
    time - event start time
    """

    address: Optional[str] = None
    button_text: Optional[str] = None
    friends: Optional[List[int]] = None
    id: Optional[int] = None
    is_favorite: Optional[bool] = None
    member_status: Optional["GroupsGroupFullMemberStatus"] = None
    text: Optional[str] = None
    time: Optional[int] = None


class FaveBookmark(BaseObject):
    """VK Object Fave/FaveBookmark"""

    added_date: Optional[int] = None
    link: Optional["BaseLink"] = None
    post: Optional["WallWallpostFull"] = None
    product: Optional["MarketMarketItem"] = None
    seen: Optional[bool] = None
    tags: Optional[List["FaveTag"]] = None
    type: Optional["FaveBookmarkType"] = None
    video: Optional["VideoVideo"] = None


class FaveBookmarkType(enum.Enum):
    """ FaveBookmarkType enum """

    POST = "post"
    VIDEO = "video"
    PRODUCT = "product"
    ARTICLE = "article"
    LINK = "link"


class FavePage(BaseObject):
    """VK Object Fave/FavePage"""

    description: Optional[str] = None
    group: Optional["GroupsGroupFull"] = None
    tags: Optional[List["FaveTag"]] = None
    type: Optional["FavePageType"] = None
    updated_date: Optional[int] = None
    user: Optional["UsersUserFull"] = None


class FavePageType(enum.Enum):
    """ FavePageType enum """

    USER = "user"
    GROUP = "group"
    HINTS = "hints"


class FaveTag(BaseObject):
    """VK Object Fave/FaveTag

    id - Tag id
    name - Tag name
    """

    id: Optional[int] = None
    name: Optional[str] = None


class FriendsFriendStatus(BaseObject):
    """VK Object Friends/FriendsFriendStatus"""

    friend_status: Optional["FriendsFriendStatusStatus"] = None
    sign: Optional[str] = None
    user_id: Optional[int] = None


class FriendsFriendExtendedStatus(FriendsFriendStatus):
    """VK Object Friends/FriendsFriendExtendedStatus

    is_request_unread - Is friend request from other user unread
    """

    is_request_unread: Optional[bool] = None


class FriendsFriendStatusStatus(enum.IntEnum):
    """ Friend status with the user """

    not_a_friend = 0
    outcoming_request = 1
    incoming_request = 2
    is_friend = 3


class FriendsFriendsList(BaseObject):
    """VK Object Friends/FriendsFriendsList

    id - List ID
    name - List title
    """

    id: Optional[int] = None
    name: Optional[str] = None


class FriendsMutualFriend(BaseObject):
    """VK Object Friends/FriendsMutualFriend

    common_count - Total mutual friends number
    id - User ID
    """

    common_count: Optional[int] = None
    common_friends: Optional[List[int]] = None
    id: Optional[int] = None


class FriendsRequests(BaseObject):
    """VK Object Friends/FriendsRequests

    from - ID of the user by whom friend has been suggested
    user_id - User ID
    """

    _from: Optional[str] = None
    mutual: Optional["FriendsRequestsMutual"] = None
    user_id: Optional[int] = None


class FriendsRequestsMutual(BaseObject):
    """VK Object Friends/FriendsRequestsMutual

    count - Total mutual friends number
    """

    count: Optional[int] = None
    users: Optional[List[int]] = None


class FriendsRequestsXtrMessage(BaseObject):
    """VK Object Friends/FriendsRequestsXtrMessage

    from - ID of the user by whom friend has been suggested
    message - Message sent with a request
    user_id - User ID
    """

    _from: Optional[str] = None
    message: Optional[str] = None
    mutual: Optional["FriendsRequestsMutual"] = None
    user_id: Optional[int] = None


class GiftsGift(BaseObject):
    """VK Object Gifts/GiftsGift"""

    date: Optional[int] = None
    from_id: Optional[int] = None
    gift: Optional["GiftsLayout"] = None
    gift_hash: Optional[str] = None
    id: Optional[int] = None
    message: Optional[str] = None
    privacy: Optional["GiftsGiftPrivacy"] = None


class GiftsGiftPrivacy(enum.IntEnum):
    """ Gift privacy """

    name_and_message_for_all = 0
    name_for_all = 1
    name_and_message_for_recipient_only = 2


class GiftsLayout(BaseObject):
    """VK Object Gifts/GiftsLayout

    id - Gift ID
    thumb_512 - URL of the preview image with 512 px in width
    thumb_256 - URL of the preview image with 256 px in width
    thumb_48 - URL of the preview image with 48 px in width
    thumb_96 - URL of the preview image with 96 px in width
    stickers_product_id - ID of the sticker pack, if the gift is representing one
    build_id - ID of the build of constructor gift
    keywords - Keywords used for search
    """

    id: Optional[int] = None
    thumb_512: Optional[str] = None
    thumb_256: Optional[str] = None
    thumb_48: Optional[str] = None
    thumb_96: Optional[str] = None
    stickers_product_id: Optional[int] = None
    build_id: Optional[str] = None
    keywords: Optional[str] = None


class GroupsAddress(BaseObject):
    """VK Object Groups/GroupsAddress

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
    timetable: Optional["GroupsAddressTimetable"] = None
    title: Optional[str] = None
    work_info_status: Optional["GroupsAddressWorkInfoStatus"] = None


class GroupsAddressTimetable(BaseObject):
    """VK Object Groups/GroupsAddressTimetable

    fri - Timetable for friday
    mon - Timetable for monday
    sat - Timetable for saturday
    sun - Timetable for sunday
    thu - Timetable for thursday
    tue - Timetable for tuesday
    wed - Timetable for wednesday
    """

    fri: Optional["GroupsAddressTimetableDay"] = None
    mon: Optional["GroupsAddressTimetableDay"] = None
    sat: Optional["GroupsAddressTimetableDay"] = None
    sun: Optional["GroupsAddressTimetableDay"] = None
    thu: Optional["GroupsAddressTimetableDay"] = None
    tue: Optional["GroupsAddressTimetableDay"] = None
    wed: Optional["GroupsAddressTimetableDay"] = None


class GroupsAddressTimetableDay(BaseObject):
    """VK Object Groups/GroupsAddressTimetableDay"""

    break_close_time: Optional[int] = None
    break_open_time: Optional[int] = None
    close_time: Optional[int] = None
    open_time: Optional[int] = None


class GroupsAddressWorkInfoStatus(enum.Enum):
    """ Status of information about timetable """

    NO_INFORMATION = "no_information"
    TEMPORARILY_CLOSED = "temporarily_closed"
    ALWAYS_OPENED = "always_opened"
    TIMETABLE = "timetable"
    FOREVER_CLOSED = "forever_closed"


class GroupsAddressesInfo(BaseObject):
    """VK Object Groups/GroupsAddressesInfo

    is_enabled - Information whether addresses is enabled
    main_address_id - Main address id for group
    """

    is_enabled: Optional[bool] = None
    main_address_id: Optional[int] = None


class GroupsBanInfo(BaseObject):
    """VK Object Groups/GroupsBanInfo"""

    admin_id: Optional[int] = None
    comment: Optional[str] = None
    comment_visible: Optional[bool] = None
    is_closed: Optional[bool] = None
    date: Optional[int] = None
    end_date: Optional[int] = None
    reason: Optional["GroupsBanInfoReason"] = None


class GroupsBanInfoReason(enum.IntEnum):
    """ Ban reason """

    other = 0
    spam = 1
    verbal_abuse = 2
    strong_language = 3
    flood = 4


class GroupsCallbackServer(BaseObject):
    """VK Object Groups/GroupsCallbackServer"""

    id: Optional[int] = None
    title: Optional[str] = None
    creator_id: Optional[int] = None
    url: Optional[str] = None
    secret_key: Optional[str] = None
    status: Optional[str] = None


class GroupsCallbackSettings(BaseObject):
    """VK Object Groups/GroupsCallbackSettings

    api_version - API version used for the events
    """

    api_version: Optional[str] = None
    events: Optional["GroupsLongPollEvents"] = None


class GroupsContactsItem(BaseObject):
    """VK Object Groups/GroupsContactsItem

    desc - Contact description
    email - Contact email
    phone - Contact phone
    user_id - User ID
    """

    desc: Optional[str] = None
    email: Optional[str] = None
    phone: Optional[str] = None
    user_id: Optional[int] = None


class GroupsCountersGroup(BaseObject):
    """VK Object Groups/GroupsCountersGroup

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


class GroupsCover(BaseObject):
    """VK Object Groups/GroupsCover"""

    enabled: Optional["BaseBoolInt"] = None
    images: Optional[List["BaseImage"]] = None


class GroupsFields(enum.Enum):
    """ GroupsFields enum """

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


class GroupsGroup(BaseObject):
    """VK Object Groups/GroupsGroup"""

    admin_level: Optional["GroupsGroupAdminLevel"] = None
    deactivated: Optional[str] = None
    finish_date: Optional[int] = None
    id: Optional[int] = None
    is_admin: Optional["BaseBoolInt"] = None
    is_advertiser: Optional["BaseBoolInt"] = None
    is_closed: Optional["GroupsGroupIsClosed"] = None
    is_member: Optional["BaseBoolInt"] = None
    name: Optional[str] = None
    photo_100: Optional[str] = None
    photo_200: Optional[str] = None
    photo_50: Optional[str] = None
    screen_name: Optional[str] = None
    start_date: Optional[int] = None
    type: Optional["GroupsGroupType"] = None


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
    plus_16 = 2
    plus_18 = 3


class GroupsGroupAttach(BaseObject):
    """VK Object Groups/GroupsGroupAttach"""

    id: Optional[int] = None
    text: Optional[str] = None
    status: Optional[str] = None
    size: Optional[int] = None
    is_favorite: Optional[bool] = None


class GroupsGroupAudio(enum.IntEnum):
    """ GroupsGroupAudio enum """

    disabled = 0
    open = 1
    limited = 2


class GroupsGroupBanInfo(BaseObject):
    """VK Object Groups/GroupsGroupBanInfo

    comment - Ban comment
    end_date - End date of ban in Unixtime
    """

    comment: Optional[str] = None
    end_date: Optional[int] = None
    reason: Optional["GroupsBanInfoReason"] = None


class GroupsGroupCategory(BaseObject):
    """VK Object Groups/GroupsGroupCategory

    id - Category ID
    name - Category name
    """

    id: Optional[int] = None
    name: Optional[str] = None
    subcategories: Optional[List["BaseObjectWithName"]] = None


class GroupsGroupCategoryFull(BaseObject):
    """VK Object Groups/GroupsGroupCategoryFull

    id - Category ID
    name - Category name
    page_count - Pages number
    """

    id: Optional[int] = None
    name: Optional[str] = None
    page_count: Optional[int] = None
    page_previews: Optional[List["GroupsGroup"]] = None
    subcategories: Optional[List["GroupsGroupCategory"]] = None


class GroupsGroupCategoryType(BaseObject):
    """VK Object Groups/GroupsGroupCategoryType"""

    id: Optional[int] = None
    name: Optional[str] = None


class GroupsGroupDocs(enum.IntEnum):
    """ GroupsGroupDocs enum """

    disabled = 0
    open = 1
    limited = 2


class GroupsGroupFull(GroupsGroup):
    """VK Object Groups/GroupsGroupFull"""

    market: Optional["GroupsMarketInfo"] = None
    member_status: Optional["GroupsGroupFullMemberStatus"] = None
    is_adult: Optional["BaseBoolInt"] = None
    is_hidden_from_feed: Optional["BaseBoolInt"] = None
    is_favorite: Optional["BaseBoolInt"] = None
    is_subscribed: Optional["BaseBoolInt"] = None
    city: Optional["BaseObject"] = None
    country: Optional["BaseCountry"] = None
    verified: Optional["BaseBoolInt"] = None
    description: Optional[str] = None
    wiki_page: Optional[str] = None
    members_count: Optional[int] = None
    video_live_level: Optional[int] = None
    video_live_count: Optional[int] = None
    counters: Optional["GroupsCountersGroup"] = None
    cover: Optional["GroupsCover"] = None
    can_post: Optional["BaseBoolInt"] = None
    can_see_all_posts: Optional["BaseBoolInt"] = None
    activity: Optional[str] = None
    fixed_post: Optional[int] = None
    can_create_topic: Optional["BaseBoolInt"] = None
    can_upload_doc: Optional["BaseBoolInt"] = None
    can_upload_story: Optional["BaseBoolInt"] = None
    can_upload_video: Optional["BaseBoolInt"] = None
    has_photo: Optional["BaseBoolInt"] = None
    crop_photo: Optional["BaseCropPhoto"] = None
    status: Optional[str] = None
    main_album_id: Optional[int] = None
    links: Optional[List["GroupsLinksItem"]] = None
    contacts: Optional[List["GroupsContactsItem"]] = None
    wall: Optional[int] = None
    site: Optional[str] = None
    main_section: Optional["GroupsGroupFullMainSection"] = None
    trending: Optional["BaseBoolInt"] = None
    can_message: Optional["BaseBoolInt"] = None
    is_messages_blocked: Optional["BaseBoolInt"] = None
    can_send_notify: Optional["BaseBoolInt"] = None
    online_status: Optional["GroupsOnlineStatus"] = None
    age_limits: Optional["GroupsGroupFullAgeLimits"] = None
    ban_info: Optional["GroupsGroupBanInfo"] = None
    has_market_app: Optional[bool] = None
    addresses: Optional["GroupsAddressesInfo"] = None
    is_subscribed_podcasts: Optional[bool] = None
    can_subscribe_podcasts: Optional[bool] = None
    can_subscribe_posts: Optional[bool] = None
    live_covers: Optional["GroupsLiveCovers"] = None


class GroupsGroupFullAgeLimits(enum.IntEnum):
    """ GroupsGroupFullAgeLimits enum """

    no = 1
    over_16 = 2
    over_18 = 3


class GroupsGroupFullMainSection(enum.IntEnum):
    """ Main section of community """

    absent = 0
    photos = 1
    topics = 2
    audio = 3
    video = 4
    market = 5


class GroupsGroupFullMemberStatus(enum.IntEnum):
    """ GroupsGroupFullMemberStatus enum """

    not_a_member = 0
    member = 1
    not_sure = 2
    declined = 3
    has_sent_a_request = 4
    invited = 5


class GroupsGroupIsClosed(enum.IntEnum):
    """ Information whether community is closed """

    open = 0
    closed = 1
    private = 2


class GroupsGroupLink(BaseObject):
    """VK Object Groups/GroupsGroupLink"""

    name: Optional[str] = None
    desc: Optional[str] = None
    edit_title: Optional["BaseBoolInt"] = None
    id: Optional[int] = None
    image_processing: Optional["BaseBoolInt"] = None
    url: Optional[str] = None


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


class GroupsGroupPublicCategoryList(BaseObject):
    """VK Object Groups/GroupsGroupPublicCategoryList"""

    id: Optional[int] = None
    name: Optional[str] = None
    subcategories: Optional[List["GroupsGroupCategoryType"]] = None


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


class GroupsGroupXtrInvitedBy(BaseObject):
    """VK Object Groups/GroupsGroupXtrInvitedBy"""

    admin_level: Optional["GroupsGroupXtrInvitedByAdminLevel"] = None
    id: Optional[int] = None
    invited_by: Optional[int] = None
    is_admin: Optional["BaseBoolInt"] = None
    is_advertiser: Optional["BaseBoolInt"] = None
    is_closed: Optional["BaseBoolInt"] = None
    is_member: Optional["BaseBoolInt"] = None
    name: Optional[str] = None
    photo_100: Optional[str] = None
    photo_200: Optional[str] = None
    photo_50: Optional[str] = None
    screen_name: Optional[str] = None
    type: Optional["GroupsGroupXtrInvitedByType"] = None


class GroupsGroupXtrInvitedByAdminLevel(enum.IntEnum):
    """ Level of current user's credentials as manager """

    moderator = 1
    editor = 2
    administrator = 3


class GroupsGroupXtrInvitedByType(enum.Enum):
    """ Community type """

    GROUP = "group"
    PAGE = "page"
    EVENT = "event"


class GroupsGroupsArray(BaseObject):
    """VK Object Groups/GroupsGroupsArray

    count - Communities number
    """

    count: Optional[int] = None
    items: Optional[List[int]] = None


class GroupsLinksItem(BaseObject):
    """VK Object Groups/GroupsLinksItem

    desc - Link description
    edit_title - Information whether the link title can be edited
    id - Link ID
    name - Link title
    photo_100 - URL of square image of the link with 100 pixels in width
    photo_50 - URL of square image of the link with 50 pixels in width
    url - Link URL
    """

    desc: Optional[str] = None
    edit_title: Optional["BaseBoolInt"] = None
    id: Optional[int] = None
    name: Optional[str] = None
    photo_100: Optional[str] = None
    photo_50: Optional[str] = None
    url: Optional[str] = None


class GroupsLiveCovers(BaseObject):
    """VK Object Groups/GroupsLiveCovers

    is_enabled - Information whether live covers is enabled
    is_scalable - Information whether live covers photo scaling is enabled
    """

    is_enabled: Optional[bool] = None
    is_scalable: Optional[bool] = None
    story_ids: Optional[List[str]] = None


class GroupsLongPollEvents(BaseObject):
    """VK Object Groups/GroupsLongPollEvents"""

    audio_new: Optional["BaseBoolInt"] = None
    board_post_delete: Optional["BaseBoolInt"] = None
    board_post_edit: Optional["BaseBoolInt"] = None
    board_post_new: Optional["BaseBoolInt"] = None
    board_post_restore: Optional["BaseBoolInt"] = None
    group_change_photo: Optional["BaseBoolInt"] = None
    group_change_settings: Optional["BaseBoolInt"] = None
    group_join: Optional["BaseBoolInt"] = None
    group_leave: Optional["BaseBoolInt"] = None
    group_officers_edit: Optional["BaseBoolInt"] = None
    lead_forms_new: Optional["BaseBoolInt"] = None
    market_comment_delete: Optional["BaseBoolInt"] = None
    market_comment_edit: Optional["BaseBoolInt"] = None
    market_comment_new: Optional["BaseBoolInt"] = None
    market_comment_restore: Optional["BaseBoolInt"] = None
    message_allow: Optional["BaseBoolInt"] = None
    message_deny: Optional["BaseBoolInt"] = None
    message_new: Optional["BaseBoolInt"] = None
    message_read: Optional["BaseBoolInt"] = None
    message_reply: Optional["BaseBoolInt"] = None
    message_typing_state: Optional["BaseBoolInt"] = None
    message_edit: Optional["BaseBoolInt"] = None
    photo_comment_delete: Optional["BaseBoolInt"] = None
    photo_comment_edit: Optional["BaseBoolInt"] = None
    photo_comment_new: Optional["BaseBoolInt"] = None
    photo_comment_restore: Optional["BaseBoolInt"] = None
    photo_new: Optional["BaseBoolInt"] = None
    poll_vote_new: Optional["BaseBoolInt"] = None
    user_block: Optional["BaseBoolInt"] = None
    user_unblock: Optional["BaseBoolInt"] = None
    video_comment_delete: Optional["BaseBoolInt"] = None
    video_comment_edit: Optional["BaseBoolInt"] = None
    video_comment_new: Optional["BaseBoolInt"] = None
    video_comment_restore: Optional["BaseBoolInt"] = None
    video_new: Optional["BaseBoolInt"] = None
    wall_post_new: Optional["BaseBoolInt"] = None
    wall_reply_delete: Optional["BaseBoolInt"] = None
    wall_reply_edit: Optional["BaseBoolInt"] = None
    wall_reply_new: Optional["BaseBoolInt"] = None
    wall_reply_restore: Optional["BaseBoolInt"] = None
    wall_repost: Optional["BaseBoolInt"] = None


class GroupsLongPollServer(BaseObject):
    """VK Object Groups/GroupsLongPollServer

    key - Long Poll key
    server - Long Poll server address
    ts - Number of the last event
    """

    key: Optional[str] = None
    server: Optional[str] = None
    ts: Optional[str] = None


class GroupsLongPollSettings(BaseObject):
    """VK Object Groups/GroupsLongPollSettings

    api_version - API version used for the events
    is_enabled - Shows whether Long Poll is enabled
    """

    api_version: Optional[str] = None
    events: Optional["GroupsLongPollEvents"] = None
    is_enabled: Optional[bool] = None


class GroupsMarketInfo(BaseObject):
    """VK Object Groups/GroupsMarketInfo

    contact_id - Contact person ID
    currency_text - Currency name
    enabled - Information whether the market is enabled
    main_album_id - Main market album ID
    price_max - Maximum price
    price_min - Minimum price
    """

    contact_id: Optional[int] = None
    currency: Optional["MarketCurrency"] = None
    currency_text: Optional[str] = None
    enabled: Optional["BaseBoolInt"] = None
    main_album_id: Optional[int] = None
    price_max: Optional[str] = None
    price_min: Optional[str] = None


class GroupsMemberRole(BaseObject):
    """VK Object Groups/GroupsMemberRole"""

    id: Optional[int] = None
    permissions: Optional[List["GroupsMemberRolePermission"]] = None
    role: Optional["GroupsMemberRoleStatus"] = None


class GroupsMemberRolePermission(enum.Enum):
    """ GroupsMemberRolePermission enum """

    ADS = "ads"


class GroupsMemberRoleStatus(enum.Enum):
    """ User's credentials as community admin """

    MODERATOR = "moderator"
    EDITOR = "editor"
    ADMINISTRATOR = "administrator"
    CREATOR = "creator"


class GroupsMemberStatus(BaseObject):
    """VK Object Groups/GroupsMemberStatus

    member - Information whether user is a member of the group
    user_id - User ID
    """

    member: Optional["BaseBoolInt"] = None
    user_id: Optional[int] = None


class GroupsMemberStatusFull(BaseObject):
    """VK Object Groups/GroupsMemberStatusFull

    can_invite - Information whether user can be invited
    can_recall - Information whether user's invite to the group can be recalled
    invitation - Information whether user has been invited to the group
    member - Information whether user is a member of the group
    request - Information whether user has send request to the group
    user_id - User ID
    """

    can_invite: Optional["BaseBoolInt"] = None
    can_recall: Optional["BaseBoolInt"] = None
    invitation: Optional["BaseBoolInt"] = None
    member: Optional["BaseBoolInt"] = None
    request: Optional["BaseBoolInt"] = None
    user_id: Optional[int] = None


class GroupsOnlineStatus(BaseObject):
    """VK Object Groups/GroupsOnlineStatus"""

    minutes: Optional[int] = None
    status: Optional["GroupsOnlineStatusType"] = None


class GroupsOnlineStatusType(enum.Enum):
    """ Type of online status of group """

    NONE = "none"
    ONLINE = "online"
    ANSWER_MARK = "answer_mark"


class GroupsOwnerXtrBanInfo(BaseObject):
    """VK Object Groups/GroupsOwnerXtrBanInfo"""

    ban_info: Optional["GroupsBanInfo"] = None
    group: Optional["GroupsGroup"] = None
    profile: Optional["UsersUser"] = None
    type: Optional["GroupsOwnerXtrBanInfoType"] = None


class GroupsOwnerXtrBanInfoType(enum.Enum):
    """ Owner type """

    GROUP = "group"
    PROFILE = "profile"


class GroupsRoleOptions(enum.Enum):
    """ User's credentials as community admin """

    MODERATOR = "moderator"
    EDITOR = "editor"
    ADMINISTRATOR = "administrator"
    CREATOR = "creator"


class GroupsSettingsTwitter(BaseObject):
    """VK Object Groups/GroupsSettingsTwitter"""

    status: Optional[str] = None
    name: Optional[str] = None


class GroupsSubjectItem(BaseObject):
    """VK Object Groups/GroupsSubjectItem

    id - Subject ID
    name - Subject title
    """

    id: Optional[int] = None
    name: Optional[str] = None


class GroupsTokenPermissionSetting(BaseObject):
    """VK Object Groups/GroupsTokenPermissionSetting"""

    name: Optional[str] = None
    setting: Optional[int] = None


class LeadsChecked(BaseObject):
    """VK Object Leads/LeadsChecked"""

    reason: Optional[str] = None
    result: Optional["LeadsCheckedResult"] = None
    sid: Optional[str] = None
    start_link: Optional[str] = None


class LeadsCheckedResult(enum.Enum):
    """ Information whether user can start the lead """

    TRUE = "true"
    FALSE = "false"


class LeadsComplete(BaseObject):
    """VK Object Leads/LeadsComplete

    cost - Offer cost
    limit - Offer limit
    spent - Amount of spent votes
    test_mode - Information whether test mode is enabled
    """

    cost: Optional[int] = None
    limit: Optional[int] = None
    spent: Optional[int] = None
    success: Optional[int] = None
    test_mode: Optional["BaseBoolInt"] = None


class LeadsEntry(BaseObject):
    """VK Object Leads/LeadsEntry

    aid - Application ID
    comment - Comment text
    date - Date when the action has been started in Unixtime
    sid - Session string ID
    start_date - Start date in Unixtime (for status=2)
    status - Action type
    test_mode - Information whether test mode is enabled
    uid - User ID
    """

    aid: Optional[int] = None
    comment: Optional[str] = None
    date: Optional[int] = None
    sid: Optional[str] = None
    start_date: Optional[int] = None
    status: Optional[int] = None
    test_mode: Optional["BaseBoolInt"] = None
    uid: Optional[int] = None


class LeadsLead(BaseObject):
    """VK Object Leads/LeadsLead

    completed - Completed offers number
    cost - Offer cost
    impressions - Impressions number
    limit - Lead limit
    spent - Amount of spent votes
    started - Started offers number
    """

    completed: Optional[int] = None
    cost: Optional[int] = None
    days: Optional["LeadsLeadDays"] = None
    impressions: Optional[int] = None
    limit: Optional[int] = None
    spent: Optional[int] = None
    started: Optional[int] = None


class LeadsLeadDays(BaseObject):
    """VK Object Leads/LeadsLeadDays

    completed - Completed offers number
    impressions - Impressions number
    spent - Amount of spent votes
    started - Started offers number
    """

    completed: Optional[int] = None
    impressions: Optional[int] = None
    spent: Optional[int] = None
    started: Optional[int] = None


class LeadsStart(BaseObject):
    """VK Object Leads/LeadsStart"""

    test_mode: Optional["BaseBoolInt"] = None
    vk_sid: Optional[str] = None


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


class LinkTargetObject(BaseObject):
    """VK Object Link/LinkTargetObject

    type - Object type
    owner_id - Owner ID
    item_id - Item ID
    """

    type: Optional[str] = None
    owner_id: Optional[int] = None
    item_id: Optional[int] = None


class MarketCurrency(BaseObject):
    """VK Object Market/MarketCurrency

    id - Currency ID
    name - Currency sign
    """

    id: Optional[int] = None
    name: Optional[str] = None


class MarketMarketAlbum(BaseObject):
    """VK Object Market/MarketMarketAlbum

    count - Items number
    id - Market album ID
    owner_id - Market album owner's ID
    title - Market album title
    updated_time - Date when album has been updated last time in Unixtime
    """

    count: Optional[int] = None
    id: Optional[int] = None
    owner_id: Optional[int] = None
    photo: Optional["PhotosPhoto"] = None
    title: Optional[str] = None
    updated_time: Optional[int] = None


class MarketMarketCategory(BaseObject):
    """VK Object Market/MarketMarketCategory

    id - Category ID
    name - Category name
    """

    id: Optional[int] = None
    name: Optional[str] = None
    section: Optional["MarketSection"] = None


class MarketMarketItem(BaseObject):
    """VK Object Market/MarketMarketItem"""

    access_key: Optional[str] = None
    availability: Optional["MarketMarketItemAvailability"] = None
    button_title: Optional[str] = None
    category: Optional["MarketMarketCategory"] = None
    date: Optional[int] = None
    description: Optional[str] = None
    external_id: Optional[str] = None
    id: Optional[int] = None
    is_favorite: Optional[bool] = None
    owner_id: Optional[int] = None
    price: Optional["MarketPrice"] = None
    thumb_photo: Optional[str] = None
    title: Optional[str] = None
    url: Optional[str] = None
    variants_grouping_id: Optional[int] = None
    is_main_variant: Optional[bool] = None


class MarketMarketItemAvailability(enum.IntEnum):
    """ Information whether the item is available """

    available = 0
    removed = 1
    unavailable = 2


class MarketMarketItemFull(MarketMarketItem):
    """VK Object Market/MarketMarketItemFull

    can_comment - Information whether current use can comment the item
    can_repost - Information whether current use can repost the item
    views_count - Views number
    """

    albums_ids: Optional[List[int]] = None
    photos: Optional[List["PhotosPhoto"]] = None
    can_comment: Optional["BaseBoolInt"] = None
    can_repost: Optional["BaseBoolInt"] = None
    likes: Optional["BaseLikes"] = None
    reposts: Optional["BaseRepostsInfo"] = None
    views_count: Optional[int] = None


class MarketPrice(BaseObject):
    """VK Object Market/MarketPrice

    amount - Amount
    text - Text
    """

    amount: Optional[str] = None
    currency: Optional["MarketCurrency"] = None
    discount_rate: Optional[int] = None
    old_amount: Optional[str] = None
    text: Optional[str] = None


class PropertyValue(BaseObject):
    variant_id: Optional[int] = None
    variant_name: Optional[str] = None
    property_name: Optional[str] = None


class MarketStatus(enum.IntEnum):
    NEW = 0
    AGREE = 1
    PATCH = 2
    DELIVER = 3
    DONE = 4
    CANCELLED = 5
    RETURNED = 6


class MarketDelivery(BaseObject):
    address: Optional[str] = None
    type: Optional[str] = None
    track_number: Optional[str] = None
    track_link: Optional[str] = None
    delivery_point: Optional[dict] = None


class MarketRecipient(BaseObject):
    name: Optional[str] = None
    phone: Optional[str] = None
    display_text: Optional[str] = None


class MarketOrder(BaseObject):
    id: Optional[int] = None
    group_id: Optional[int] = None
    user_id: Optional[int] = None
    date: Optional[int] = None
    variants_grouping_id: Optional[int] = None
    is_main_variant: Optional[int] = None
    property_values: Optional[List[PropertyValue]] = None
    cart_quantity: Optional[int] = None
    status: Optional[MarketStatus] = None
    items_count: Optional[int] = None
    total_price: Optional[MarketPrice] = None
    display_order_id: Optional[str] = None
    comment: Optional[str] = None
    preview_order_items: Optional[List[MarketMarketItemFull]] = None
    delivery: Optional[MarketDelivery] = None
    recipient: Optional[MarketRecipient] = None


class MarketSection(BaseObject):
    """VK Object Market/MarketSection

    id - Section ID
    name - Section name
    """

    id: Optional[int] = None
    name: Optional[str] = None


class MediaRestriction(BaseObject):
    """VK Object Media/MediaRestriction

    always_shown - Need show restriction always or not
    blur - Need blur current video or not
    can_play - Can play video or not
    can_preview - Can preview video or not
    """

    text: Optional[str] = None
    title: Optional[str] = None
    button: Optional["VideoRestrictionButton"] = None
    always_shown: Optional["BaseBoolInt"] = None
    blur: Optional["BaseBoolInt"] = None
    can_play: Optional["BaseBoolInt"] = None
    can_preview: Optional["BaseBoolInt"] = None
    card_icon: Optional[List["BaseImage"]] = None
    list_icon: Optional[List["BaseImage"]] = None


class MessageChatPreview(BaseObject):
    """VK Object Message/MessageChatPreview"""

    admin_id: Optional[int] = None
    joined: Optional[bool] = None
    local_id: Optional[int] = None
    members: Optional[List[int]] = None
    members_count: Optional[int] = None
    title: Optional[str] = None


class MessagesAudioMessage(BaseObject):
    """VK Object Messages/MessagesAudioMessage

    access_key - Access key for audio message
    duration - Audio message duration in seconds
    id - Audio message ID
    link_mp3 - MP3 file URL
    link_ogg - OGG file URL
    owner_id - Audio message owner ID
    """

    access_key: Optional[str] = None
    duration: Optional[int] = None
    id: Optional[int] = None
    link_mp3: Optional[str] = None
    link_ogg: Optional[str] = None
    owner_id: Optional[int] = None
    waveform: Optional[List[int]] = None


class MessagesChat(BaseObject):
    """VK Object Messages/MessagesChat

    admin_id - Chat creator ID
    id - Chat ID
    kicked - Shows that user has been kicked from the chat
    left - Shows that user has been left the chat
    photo_100 - URL of the preview image with 100 px in width
    photo_200 - URL of the preview image with 200 px in width
    photo_50 - URL of the preview image with 50 px in width
    title - Chat title
    type - Chat type
    is_default_photo - If provided photo is default
    """

    admin_id: Optional[int] = None
    id: Optional[int] = None
    kicked: Optional["BaseBoolInt"] = None
    left: Optional["BaseBoolInt"] = None
    photo_100: Optional[str] = None
    photo_200: Optional[str] = None
    photo_50: Optional[str] = None
    push_settings: Optional["MessagesChatPushSettings"] = None
    title: Optional[str] = None
    type: Optional[str] = None
    users: Optional[List[int]] = None
    is_default_photo: Optional[bool] = None


class MessagesChatFull(BaseObject):
    """VK Object Messages/MessagesChatFull

    admin_id - Chat creator ID
    id - Chat ID
    kicked - Shows that user has been kicked from the chat
    left - Shows that user has been left the chat
    photo_100 - URL of the preview image with 100 px in width
    photo_200 - URL of the preview image with 200 px in width
    photo_50 - URL of the preview image with 50 px in width
    title - Chat title
    type - Chat type
    """

    admin_id: Optional[int] = None
    id: Optional[int] = None
    kicked: Optional["BaseBoolInt"] = None
    left: Optional["BaseBoolInt"] = None
    photo_100: Optional[str] = None
    photo_200: Optional[str] = None
    photo_50: Optional[str] = None
    push_settings: Optional["MessagesChatPushSettings"] = None
    title: Optional[str] = None
    type: Optional[str] = None
    users: Optional[List["MessagesUserXtrInvitedBy"]] = None


class MessagesChatPushSettings(BaseObject):
    """VK Object Messages/MessagesChatPushSettings

    disabled_until - Time until that notifications are disabled
    sound - Information whether the sound is on
    """

    disabled_until: Optional[int] = None
    sound: Optional["BaseBoolInt"] = None


class MessagesChatRestrictions(BaseObject):
    """VK Object Messages/MessagesChatRestrictions

    admins_promote_users - Only admins can promote users to admins
    only_admins_edit_info - Only admins can change chat info
    only_admins_edit_pin - Only admins can edit pinned message
    only_admins_invite - Only admins can invite users to this chat
    only_admins_kick - Only admins can kick users from this chat
    """

    admins_promote_users: Optional[bool] = None
    only_admins_edit_info: Optional[bool] = None
    only_admins_edit_pin: Optional[bool] = None
    only_admins_invite: Optional[bool] = None
    only_admins_kick: Optional[bool] = None


class MessagesConversation(BaseObject):
    """VK Object Messages/MessagesConversation

    last_message_id - ID of the last message in conversation
    in_read - Last message user have read
    out_read - Last outcoming message have been read by the opponent
    unread_count - Unread messages number
    is_marked_unread - Is this conversation uread
    mentions - Ids of messages with mentions
    """

    peer: Optional["MessagesConversationPeer"] = None
    last_message_id: Optional[int] = None
    in_read: Optional[int] = None
    out_read: Optional[int] = None
    unread_count: Optional[int] = None
    is_marked_unread: Optional[bool] = None
    important: Optional[bool] = None
    unanswered: Optional[bool] = None
    special_service_type: Optional[str] = None
    message_request_data: Optional["MessagesMessageRequestData"] = None
    mentions: Optional[List[int]] = None
    current_keyboard: Optional["MessagesKeyboard"] = None


class MessagesConversationMember(BaseObject):
    """VK Object Messages/MessagesConversationMember

    can_kick - Is it possible for user to kick this member
    request_date - Message request date
    """

    can_kick: Optional[bool] = None
    invited_by: Optional[int] = None
    is_admin: Optional[bool] = None
    is_owner: Optional[bool] = None
    is_message_request: Optional[bool] = None
    join_date: Optional[int] = None
    request_date: Optional[int] = None
    member_id: Optional[int] = None


class MessagesConversationPeer(BaseObject):
    """VK Object Messages/MessagesConversationPeer"""

    id: Optional[int] = None
    local_id: Optional[int] = None
    type: Optional["MessagesConversationPeerType"] = None


class MessagesConversationPeerType(enum.Enum):
    """ Peer type """

    CHAT = "chat"
    EMAIL = "email"
    USER = "user"
    GROUP = "group"


class MessagesConversationWithMessage(BaseObject):
    """VK Object Messages/MessagesConversationWithMessage"""

    conversation: Optional["MessagesConversation"] = None
    last_message: Optional["MessagesMessage"] = None


class MessagesForeignMessage(BaseObject):
    """VK Object Messages/MessagesForeignMessage

    conversation_message_id - Conversation message ID
    date - Date when the message was created
    from_id - Message author's ID
    id - Message ID
    peer_id - Peer ID
    text - Message text
    update_time - Date when the message has been updated in Unixtime
    was_listened - Was the audio message inside already listened by you
    payload - Additional data sent along with message for developer convenience
    """

    attachments: Optional[List["MessagesMessageAttachment"]] = None
    conversation_message_id: Optional[int] = None
    date: Optional[int] = None
    from_id: Optional[int] = None
    fwd_messages: Optional[List["MessagesForeignMessage"]] = None
    geo: Optional["BaseGeo"] = None
    id: Optional[int] = None
    peer_id: Optional[int] = None
    reply_message: Optional["MessagesForeignMessage"] = None
    text: Optional[str] = None
    update_time: Optional[int] = None
    was_listened: Optional[bool] = None
    payload: Optional[str] = None


class MessagesGraffiti(BaseObject):
    """VK Object Messages/MessagesGraffiti

    access_key - Access key for graffiti
    height - Graffiti height
    id - Graffiti ID
    owner_id - Graffiti owner ID
    url - Graffiti URL
    width - Graffiti width
    """

    access_key: Optional[str] = None
    height: Optional[int] = None
    id: Optional[int] = None
    owner_id: Optional[int] = None
    url: Optional[str] = None
    width: Optional[int] = None


class MessagesHistoryAttachment(BaseObject):
    """VK Object Messages/MessagesHistoryAttachment

    message_id - Message ID
    from_id - Message author's ID
    """

    attachment: Optional["MessagesHistoryMessageAttachment"] = None
    message_id: Optional[int] = None
    from_id: Optional[int] = None


class MessagesHistoryMessageAttachment(BaseObject):
    """VK Object Messages/MessagesHistoryMessageAttachment"""

    audio: Optional["AudioAudio"] = None
    audio_message: Optional["MessagesAudioMessage"] = None
    doc: Optional["DocsDoc"] = None
    graffiti: Optional["MessagesGraffiti"] = None
    link: Optional["BaseLink"] = None
    market: Optional["BaseLink"] = None
    photo: Optional["PhotosPhoto"] = None
    share: Optional["BaseLink"] = None
    type: Optional["MessagesHistoryMessageAttachmentType"] = None
    video: Optional["VideoVideo"] = None
    wall: Optional["BaseLink"] = None


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


class MessagesKeyboard(BaseObject):
    """VK Object Messages/MessagesKeyboard

    author_id - Community or bot, which set this keyboard
    one_time - Should this keyboard disappear on first use
    """

    author_id: Optional[int] = None
    buttons: Optional[List[dict]] = None
    one_time: Optional[bool] = None
    inline: Optional[bool] = None


class MessagesKeyboardButton(BaseObject):
    """VK Object Messages/MessagesKeyboardButton

    color - Button color
    """

    action: Optional["MessagesKeyboardButtonAction"] = None
    color: Optional[str] = None


class MessagesKeyboardButtonAction(BaseObject):
    """VK Object Messages/MessagesKeyboardButtonAction

    app_id - Fragment value in app link like vk.com/app{app_id}_-654321#hash
    hash - Fragment value in app link like vk.com/app123456_-654321#{hash}
    label - Label for button
    link - link for button
    owner_id - Fragment value in app link like vk.com/app123456_{owner_id}#hash
    payload - Additional data sent along with message for developer convenience
    type - Button type
    """

    app_id: Optional[int] = None
    hash: Optional[str] = None
    label: Optional[str] = None
    link: Optional[str] = None
    owner_id: Optional[int] = None
    payload: Optional[str] = None
    type: Optional["MessagesTemplateActionTypeNames"] = None


class MessagesLastActivity(BaseObject):
    """VK Object Messages/MessagesLastActivity

    online - Information whether user is online
    time - Time when user was online in Unixtime
    """

    online: Optional["BaseBoolInt"] = None
    time: Optional[int] = None


class MessagesLongpollMessages(BaseObject):
    """VK Object Messages/MessagesLongpollMessages

    count - Total number
    """

    count: Optional[int] = None
    items: Optional[List["MessagesMessage"]] = None


class MessagesLongpollParams(BaseObject):
    """VK Object Messages/MessagesLongpollParams

    key - Key
    pts - Persistent timestamp
    server - Server URL
    ts - Timestamp
    """

    key: Optional[str] = None
    pts: Optional[int] = None
    server: Optional[str] = None
    ts: Optional[str] = None


class MessagesMessage(BaseObject):
    """VK Object Messages/MessagesMessage

    admin_author_id - Only for messages from community. Contains user ID of community admin, who sent this message.
    conversation_message_id - Unique auto-incremented number for all messages with this peer
    date - Date when the message has been sent in Unixtime
    deleted - Is it an deleted message
    from_id - Message author's ID
    fwd_messages - Forwarded messages
    id - Message ID
    important - Is it an important message
    is_cropped - this message is cropped for bot
    members_count - Members number
    out - Information whether the message is outcoming
    peer_id - Peer ID
    random_id - ID used for sending messages. It returned only for outgoing messages
    text - Message text
    update_time - Date when the message has been updated in Unixtime
    was_listened - Was the audio message inside already listened by you
    pinned_at - Date when the message has been pinned in Unixtime
    """

    action: Optional["MessagesMessageAction"] = None
    admin_author_id: Optional[int] = None
    attachments: Optional[List["MessagesMessageAttachment"]] = None
    conversation_message_id: Optional[int] = None
    date: Optional[int] = None
    deleted: Optional["BaseBoolInt"] = None
    from_id: Optional[int] = None
    fwd_messages: Optional[List["MessagesForeignMessage"]] = None
    geo: Optional["BaseGeo"] = None
    id: Optional[int] = None
    important: Optional[bool] = None
    is_hidden: Optional[bool] = None
    is_cropped: Optional[bool] = None
    keyboard: Optional["MessagesKeyboard"] = None
    members_count: Optional[int] = None
    out: Optional["BaseBoolInt"] = None
    payload: Optional[str] = None
    peer_id: Optional[int] = None
    random_id: Optional[int] = None
    ref: Optional[str] = None
    ref_source: Optional[str] = None
    reply_message: Optional["MessagesForeignMessage"] = None
    text: Optional[str] = None
    update_time: Optional[int] = None
    was_listened: Optional[bool] = None
    pinned_at: Optional[int] = None


class MessagesMessageAction(BaseObject):
    """VK Object Messages/MessagesMessageAction

    conversation_message_id - Message ID
    email - Email address for chat_invite_user or chat_kick_user actions
    member_id - User or email peer ID
    message - Message body of related message
    text - New chat title for chat_create and chat_title_update actions
    """

    conversation_message_id: Optional[int] = None
    email: Optional[str] = None
    member_id: Optional[int] = None
    message: Optional[str] = None
    photo: Optional["MessagesMessageActionPhoto"] = None
    text: Optional[str] = None
    type: Optional["MessagesMessageActionStatus"] = None


class MessagesMessageActionPhoto(BaseObject):
    """VK Object Messages/MessagesMessageActionPhoto"""

    photo_100: Optional[str] = None
    photo_200: Optional[str] = None
    photo_50: Optional[str] = None


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


class MessagesMessageAttachment(BaseObject):
    """VK Object Messages/MessagesMessageAttachment"""

    audio: Optional["AudioAudio"] = None
    audio_message: Optional["MessagesAudioMessage"] = None
    doc: Optional["DocsDoc"] = None
    gift: Optional["GiftsLayout"] = None
    graffiti: Optional["MessagesGraffiti"] = None
    link: Optional["BaseLink"] = None
    market: Optional["MarketMarketItem"] = None
    market_market_album: Optional["MarketMarketAlbum"] = None
    photo: Optional["PhotosPhoto"] = None
    sticker: Optional["BaseSticker"] = None
    story: Optional["StoriesStory"] = None
    type: Optional["MessagesMessageAttachmentType"] = None
    video: Optional["VideoVideo"] = None
    wall: Optional["WallWallpostFull"] = None
    wall_reply: Optional["WallWallComment"] = None


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
    GRAFFITI = "graffiti"
    AUDIO_MESSAGE = "audio_message"


class MessagesMessageRequestData(BaseObject):
    """VK Object Messages/MessagesMessageRequestData

    status - Status of message request
    inviter_id - Message request sender id
    request_date - Message request date
    """

    status: Optional[str] = None
    inviter_id: Optional[int] = None
    request_date: Optional[int] = None


class MessagesPinnedMessage(BaseObject):
    """VK Object Messages/MessagesPinnedMessage"""

    attachments: Optional[List["MessagesMessageAttachment"]] = None
    conversation_message_id: Optional[int] = None
    date: Optional[int] = None
    from_id: Optional[int] = None
    fwd_messages: Optional[List["MessagesForeignMessage"]] = None
    geo: Optional["BaseGeo"] = None
    id: Optional[int] = None
    peer_id: Optional[int] = None
    reply_message: Optional["MessagesForeignMessage"] = None
    text: Optional[str] = None
    keyboard: Optional["MessagesKeyboard"] = None


class MessagesTemplateActionTypeNames(enum.Enum):
    """ Template action type names """

    TEXT = "text"
    START = "start"
    LOCATION = "location"
    VKPAY = "vkpay"
    OPEN_APP = "open_app"
    OPEN_PHOTO = "open_photo"
    OPEN_LINK = "open_link"


class NewsfeedCommentsFilters(enum.Enum):
    """ NewsfeedCommentsFilters enum """

    POST = "post"
    PHOTO = "photo"
    VIDEO = "video"
    TOPIC = "topic"
    NOTE = "note"


class NewsfeedEventActivity(BaseObject):
    """VK Object Newsfeed/NewsfeedEventActivity"""

    address: Optional[str] = None
    button_text: Optional[str] = None
    friends: Optional[List[int]] = None
    member_status: Optional["GroupsGroupFullMemberStatus"] = None
    text: Optional[str] = None
    time: Optional[int] = None


class NewsfeedFilters(enum.Enum):
    """ NewsfeedFilters enum """

    POST = "post"
    PHOTO = "photo"
    PHOTO_TAG = "photo_tag"
    WALL_PHOTO = "wall_photo"
    FRIEND = "friend"
    RECOMMENDED_GROUPS = "recommended_groups"
    NOTE = "note"
    AUDIO = "audio"
    VIDEO = "video"
    AUDIO_PLAYLIST = "audio_playlist"
    CLIP = "clip"


class NewsfeedIgnoreItemType(enum.Enum):
    """ NewsfeedIgnoreItemType enum """

    WALL = "wall"
    TAG = "tag"
    PROFILEPHOTO = "profilephoto"
    VIDEO = "video"
    PHOTO = "photo"
    AUDIO = "audio"


class NewsfeedItemAudioAudio(BaseObject):
    """VK Object Newsfeed/NewsfeedItemAudioAudio

    count - Audios number
    """

    count: Optional[int] = None
    items: Optional[List["AudioAudio"]] = None


class NewsfeedItemBase(BaseObject):
    """VK Object Newsfeed/NewsfeedItemBase

    source_id - Item source ID
    date - Date when item has been added in Unixtime
    """

    type: Optional["NewsfeedNewsfeedItemType"] = None
    source_id: Optional[int] = None
    date: Optional[int] = None


class NewsfeedItemDigest(NewsfeedItemBase):
    """VK Object Newsfeed/NewsfeedItemDigest

    feed_id - id of feed in digest
    template - type of digest
    """

    button_text: Optional[str] = None
    feed_id: Optional[str] = None
    items: Optional[List["WallWallpost"]] = None
    main_post_ids: Optional[List[str]] = None
    template: Optional[str] = None
    title: Optional[str] = None
    track_code: Optional[str] = None


class NewsfeedItemFriend(NewsfeedItemBase):
    """VK Object Newsfeed/NewsfeedItemFriend"""

    friends: Optional["NewsfeedItemFriendFriends"] = None


class NewsfeedItemFriendFriends(BaseObject):
    """VK Object Newsfeed/NewsfeedItemFriendFriends

    count - Number of friends has been added
    """

    count: Optional[int] = None
    items: Optional[List["BaseUserId"]] = None


class NewsfeedItemHolidayRecommendationsBlockHeader(BaseObject):
    """VK Object Newsfeed/NewsfeedItemHolidayRecommendationsBlockHeader

    title - Title of the header
    subtitle - Subtitle of the header
    """

    title: Optional[str] = None
    subtitle: Optional[str] = None
    image: Optional[List["BaseImage"]] = None
    action: Optional["BaseLinkButtonAction"] = None


class NewsfeedItemNote(NewsfeedItemBase):
    """VK Object Newsfeed/NewsfeedItemNote"""

    notes: Optional["NewsfeedItemNoteNotes"] = None


class NewsfeedItemNoteNotes(BaseObject):
    """VK Object Newsfeed/NewsfeedItemNoteNotes

    count - Notes number
    """

    count: Optional[int] = None
    items: Optional[List["NewsfeedNewsfeedNote"]] = None


class NewsfeedItemPhotoPhotos(BaseObject):
    """VK Object Newsfeed/NewsfeedItemPhotoPhotos

    count - Photos number
    """

    count: Optional[int] = None
    items: Optional[List["NewsfeedNewsfeedPhoto"]] = None


class NewsfeedItemPhotoTagPhotoTags(BaseObject):
    """VK Object Newsfeed/NewsfeedItemPhotoTagPhotoTags

    count - Tags number
    """

    count: Optional[int] = None
    items: Optional[List["NewsfeedNewsfeedPhoto"]] = None


class NewsfeedItemPromoButton(NewsfeedItemBase):
    """VK Object Newsfeed/NewsfeedItemPromoButton"""

    text: Optional[str] = None
    title: Optional[str] = None
    action: Optional["NewsfeedItemPromoButtonAction"] = None
    images: Optional[List["NewsfeedItemPromoButtonImage"]] = None
    track_code: Optional[str] = None


class NewsfeedItemPromoButtonAction(BaseObject):
    """VK Object Newsfeed/NewsfeedItemPromoButtonAction"""

    url: Optional[str] = None
    type: Optional[str] = None
    target: Optional[str] = None


class NewsfeedItemPromoButtonImage(BaseObject):
    """VK Object Newsfeed/NewsfeedItemPromoButtonImage"""

    width: Optional[int] = None
    height: Optional[int] = None
    url: Optional[str] = None


class NewsfeedItemTopic(NewsfeedItemBase):
    """VK Object Newsfeed/NewsfeedItemTopic

    post_id - Topic post ID
    text - Post text
    """

    comments: Optional["BaseCommentsInfo"] = None
    likes: Optional["BaseLikesInfo"] = None
    post_id: Optional[int] = None
    text: Optional[str] = None


class NewsfeedItemVideoVideo(BaseObject):
    """VK Object Newsfeed/NewsfeedItemVideoVideo

    count - Tags number
    """

    count: Optional[int] = None
    items: Optional[List["VideoVideo"]] = None


class NewsfeedItemWallpostFeedback(BaseObject):
    """VK Object Newsfeed/NewsfeedItemWallpostFeedback"""

    type: Optional["NewsfeedItemWallpostFeedbackType"] = None
    question: Optional[str] = None
    answers: Optional[List["NewsfeedItemWallpostFeedbackAnswer"]] = None
    stars_count: Optional[int] = None
    gratitude: Optional[str] = None


class NewsfeedItemWallpostFeedbackAnswer(BaseObject):
    """VK Object Newsfeed/NewsfeedItemWallpostFeedbackAnswer"""

    title: Optional[str] = None
    id: Optional[str] = None


class NewsfeedItemWallpostFeedbackType(enum.Enum):
    """ NewsfeedItemWallpostFeedbackType enum """

    BUTTONS = "buttons"
    STARS = "stars"


class NewsfeedItemWallpostType(enum.Enum):
    """ Post type """

    POST = "post"
    COPY = "copy"
    REPLY = "reply"


class NewsfeedList(BaseObject):
    """VK Object Newsfeed/NewsfeedList

    id - List ID
    title - List title
    """

    id: Optional[int] = None
    title: Optional[str] = None


class NewsfeedListFull(NewsfeedList):
    """VK Object Newsfeed/NewsfeedListFull

    no_reposts - Information whether reposts hiding is enabled
    """

    no_reposts: Optional["BaseBoolInt"] = None
    source_ids: Optional[List[int]] = None


class NewsfeedNewsfeedItem(BaseObject):
    """VK Object Newsfeed/NewsfeedNewsfeedItem"""


class NewsfeedNewsfeedItemType(enum.Enum):
    """ Item type """

    POST = "post"
    PHOTO = "photo"
    PHOTO_TAG = "photo_tag"
    WALL_PHOTO = "wall_photo"
    FRIEND = "friend"
    NOTE = "note"
    AUDIO = "audio"
    VIDEO = "video"
    TOPIC = "topic"
    DIGEST = "digest"
    STORIES = "stories"
    TAGS_SUGGESTIONS = "tags_suggestions"


class NewsfeedNewsfeedNote(BaseObject):
    """VK Object Newsfeed/NewsfeedNewsfeedNote

    comments - Comments Number
    id - Note ID
    owner_id - integer
    title - Note title
    """

    comments: Optional[int] = None
    id: Optional[int] = None
    owner_id: Optional[int] = None
    title: Optional[str] = None


class NotesNote(BaseObject):
    """VK Object Notes/NotesNote

    can_comment - Information whether current user can comment the note
    comments - Comments number
    date - Date when the note has been created in Unixtime
    id - Note ID
    owner_id - Note owner's ID
    text - Note text
    text_wiki - Note text in wiki format
    title - Note title
    view_url - URL of the page with note preview
    """

    read_comments: Optional[int] = None
    can_comment: Optional["BaseBoolInt"] = None
    comments: Optional[int] = None
    date: Optional[int] = None
    id: Optional[int] = None
    owner_id: Optional[int] = None
    text: Optional[str] = None
    text_wiki: Optional[str] = None
    title: Optional[str] = None
    view_url: Optional[str] = None


class NotesNoteComment(BaseObject):
    """VK Object Notes/NotesNoteComment

    date - Date when the comment has beed added in Unixtime
    id - Comment ID
    message - Comment text
    nid - Note ID
    oid - Note ID
    reply_to - ID of replied comment
    uid - Comment author's ID
    """

    date: Optional[int] = None
    id: Optional[int] = None
    message: Optional[str] = None
    nid: Optional[int] = None
    oid: Optional[int] = None
    reply_to: Optional[int] = None
    uid: Optional[int] = None


class NotificationsFeedback(BaseObject):
    """VK Object Notifications/NotificationsFeedback

    from_id - Reply author's ID
    id - Item ID
    text - Reply text
    to_id - Wall owner's ID
    """

    attachments: Optional[List["WallWallpostAttachment"]] = None
    from_id: Optional[int] = None
    geo: Optional["BaseGeo"] = None
    id: Optional[int] = None
    likes: Optional["BaseLikesInfo"] = None
    text: Optional[str] = None
    to_id: Optional[int] = None


class NotificationsNotification(BaseObject):
    """VK Object Notifications/NotificationsNotification

    date - Date when the event has been occurred
    type - Notification type
    """

    date: Optional[int] = None
    feedback: Optional["NotificationsFeedback"] = None
    parent: Optional["NotificationsNotificationParent"] = None
    reply: Optional["NotificationsReply"] = None
    type: Optional[str] = None


class NotificationsNotificationItem(BaseObject):
    """VK Object Notifications/NotificationsNotificationItem"""


class NotificationsNotificationsComment(BaseObject):
    """VK Object Notifications/NotificationsNotificationsComment

    date - Date when the comment has been added in Unixtime
    id - Comment ID
    owner_id - Author ID
    text - Comment text
    """

    date: Optional[int] = None
    id: Optional[int] = None
    owner_id: Optional[int] = None
    photo: Optional["PhotosPhoto"] = None
    post: Optional["WallWallpost"] = None
    text: Optional[str] = None
    topic: Optional["BoardTopic"] = None
    video: Optional["VideoVideo"] = None


class NotificationsReply(BaseObject):
    """VK Object Notifications/NotificationsReply

    date - Date when the reply has been created in Unixtime
    id - Reply ID
    text - Reply text
    """

    date: Optional[int] = None
    id: Optional[int] = None
    text: Optional[int] = None


class NotificationsSendMessageError(BaseObject):
    """VK Object Notifications/NotificationsSendMessageError

    code - Error code
    description - Error description
    """

    code: Optional[int] = None
    description: Optional[str] = None


class NotificationsSendMessageItem(BaseObject):
    """VK Object Notifications/NotificationsSendMessageItem

    user_id - User ID
    status - Notification status
    """

    user_id: Optional[int] = None
    status: Optional[bool] = None
    error: Optional["NotificationsSendMessageError"] = None


class OauthError(BaseObject):
    """VK Object Oauth/OauthError

    error - Error type
    error_description - Error description
    redirect_uri - URI for validation
    """

    error: Optional[str] = None
    error_description: Optional[str] = None
    redirect_uri: Optional[str] = None


class OrdersAmount(BaseObject):
    """VK Object Orders/OrdersAmount

    currency - Currency name
    """

    amounts: Optional[List["OrdersAmountItem"]] = None
    currency: Optional[str] = None


class OrdersAmountItem(BaseObject):
    """VK Object Orders/OrdersAmountItem

    amount - Votes amount in user's currency
    description - Amount description
    votes - Votes number
    """

    amount: Optional[int] = None
    description: Optional[str] = None
    votes: Optional[str] = None


class OrdersOrder(BaseObject):
    """VK Object Orders/OrdersOrder

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

    amount: Optional[int] = None
    app_order_id: Optional[int] = None
    cancel_transaction_id: Optional[int] = None
    date: Optional[int] = None
    id: Optional[int] = None
    item: Optional[str] = None
    receiver_id: Optional[int] = None
    status: Optional[str] = None
    transaction_id: Optional[int] = None
    user_id: Optional[int] = None


class OrdersSubscription(BaseObject):
    """VK Object Orders/OrdersSubscription

    cancel_reason - Cancel reason
    create_time - Date of creation in Unixtime
    id - Subscription ID
    item_id - Subscription order item
    next_bill_time - Date of next bill in Unixtime
    pending_cancel - Pending cancel state
    period - Subscription period
    period_start_time - Date of last period start in Unixtime
    price - Subscription price
    status - Subscription status
    test_mode - Is test subscription
    trial_expire_time - Date of trial expire in Unixtime
    update_time - Date of last change in Unixtime
    """

    cancel_reason: Optional[str] = None
    create_time: Optional[int] = None
    id: Optional[int] = None
    item_id: Optional[str] = None
    next_bill_time: Optional[int] = None
    pending_cancel: Optional[bool] = None
    period: Optional[int] = None
    period_start_time: Optional[int] = None
    price: Optional[int] = None
    status: Optional[str] = None
    test_mode: Optional[bool] = None
    trial_expire_time: Optional[int] = None
    update_time: Optional[int] = None


class OwnerState(BaseObject):
    """VK Object Owner/OwnerState"""

    state: Optional[int] = None
    description: Optional[str] = None


class PagesPrivacySettings(enum.IntEnum):
    """ PagesPrivacySettings enum """

    community_managers_only = 0
    community_members_only = 1
    everyone = 2


class PagesWikipage(BaseObject):
    """VK Object Pages/PagesWikipage

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

    creator_id: Optional[int] = None
    creator_name: Optional[int] = None
    editor_id: Optional[int] = None
    editor_name: Optional[str] = None
    group_id: Optional[int] = None
    id: Optional[int] = None
    title: Optional[str] = None
    views: Optional[int] = None
    who_can_edit: Optional["PagesPrivacySettings"] = None
    who_can_view: Optional["PagesPrivacySettings"] = None


class PagesWikipageFull(BaseObject):
    """VK Object Pages/PagesWikipageFull

    created - Date when the page has been created in Unixtime
    creator_id - Page creator ID
    current_user_can_edit - Information whether current user can edit the page
    current_user_can_edit_access - Information whether current user can edit the page access settings
    edited - Date when the page has been edited in Unixtime
    editor_id - Last editor ID
    group_id - Community ID
    html - Page content, HTML
    id - Page ID
    source - Page content, wiki
    title - Page title
    view_url - URL of the page preview
    views - Views number
    who_can_edit - Edit settings of the page
    who_can_view - View settings of the page
    """

    created: Optional[int] = None
    creator_id: Optional[int] = None
    current_user_can_edit: Optional["BaseBoolInt"] = None
    current_user_can_edit_access: Optional["BaseBoolInt"] = None
    edited: Optional[int] = None
    editor_id: Optional[int] = None
    group_id: Optional[int] = None
    html: Optional[str] = None
    id: Optional[int] = None
    source: Optional[str] = None
    title: Optional[str] = None
    view_url: Optional[str] = None
    views: Optional[int] = None
    who_can_edit: Optional["PagesPrivacySettings"] = None
    who_can_view: Optional["PagesPrivacySettings"] = None


class PagesWikipageHistory(BaseObject):
    """VK Object Pages/PagesWikipageHistory

    id - Version ID
    length - Page size in bytes
    date - Date when the page has been edited in Unixtime
    editor_id - Last editor ID
    editor_name - Last editor name
    """

    id: Optional[int] = None
    length: Optional[int] = None
    date: Optional[int] = None
    editor_id: Optional[int] = None
    editor_name: Optional[str] = None


class PhotosCommentXtrPid(BaseObject):
    """VK Object Photos/PhotosCommentXtrPid

    date - Date when the comment has been added in Unixtime
    from_id - Author ID
    id - Comment ID
    pid - Photo ID
    reply_to_comment - Replied comment ID
    reply_to_user - Replied user ID
    text - Comment text
    """

    attachments: Optional[List["WallCommentAttachment"]] = None
    date: Optional[int] = None
    from_id: Optional[int] = None
    id: Optional[int] = None
    likes: Optional["BaseLikesInfo"] = None
    pid: Optional[int] = None
    reply_to_comment: Optional[int] = None
    reply_to_user: Optional[int] = None
    text: Optional[str] = None
    parents_stack: Optional[List[int]] = None
    thread: Optional["CommentThread"] = None


class PhotosImage(BaseObject):
    """VK Object Photos/PhotosImage"""

    height: Optional[int] = None
    type: Optional["PhotosImageType"] = None
    url: Optional[str] = None
    width: Optional[int] = None


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


class PhotosMarketAlbumUploadResponse(BaseObject):
    """VK Object Photos/PhotosMarketAlbumUploadResponse

    gid - Community ID
    hash - Uploading hash
    photo - Uploaded photo data
    server - Upload server number
    """

    gid: Optional[int] = None
    hash: Optional[str] = None
    photo: Optional[str] = None
    server: Optional[int] = None


class PhotosMarketUploadResponse(BaseObject):
    """VK Object Photos/PhotosMarketUploadResponse

    crop_data - Crop data
    crop_hash - Crop hash
    group_id - Community ID
    hash - Uploading hash
    photo - Uploaded photo data
    server - Upload server number
    """

    crop_data: Optional[str] = None
    crop_hash: Optional[str] = None
    group_id: Optional[int] = None
    hash: Optional[str] = None
    photo: Optional[str] = None
    server: Optional[int] = None


class PhotosMessageUploadResponse(BaseObject):
    """VK Object Photos/PhotosMessageUploadResponse

    hash - Uploading hash
    photo - Uploaded photo data
    server - Upload server number
    """

    hash: Optional[str] = None
    photo: Optional[str] = None
    server: Optional[int] = None


class PhotosOwnerUploadResponse(BaseObject):
    """VK Object Photos/PhotosOwnerUploadResponse

    hash - Uploading hash
    photo - Uploaded photo data
    server - Upload server number
    """

    hash: Optional[str] = None
    photo: Optional[str] = None
    server: Optional[int] = None


class PhotosPhoto(BaseObject):
    """VK Object Photos/PhotosPhoto

    access_key - Access key for the photo
    album_id - Album ID
    date - Date when uploaded
    height - Original photo height
    id - Photo ID
    lat - Latitude
    long - Longitude
    owner_id - Photo owner's ID
    photo_256 - URL of image with 2560 px width
    can_comment - Information whether current user can comment the photo
    post_id - Post ID
    text - Photo caption
    user_id - ID of the user who have uploaded the photo
    width - Original photo width
    has_tags - Whether photo has attached tag links
    """

    access_key: Optional[str] = None
    album_id: Optional[int] = None
    date: Optional[int] = None
    height: Optional[int] = None
    id: Optional[int] = None
    images: Optional[List["PhotosImage"]] = None
    lat: Optional[float] = None
    long: Optional[float] = None
    owner_id: Optional[int] = None
    photo_256: Optional[str] = None
    can_comment: Optional["BaseBoolInt"] = None
    place: Optional[str] = None
    post_id: Optional[int] = None
    sizes: Optional[List["PhotosPhotoSizes"]] = None
    text: Optional[str] = None
    user_id: Optional[int] = None
    width: Optional[int] = None
    has_tags: Optional[bool] = None
    restrictions: Optional["MediaRestriction"] = None


class PhotosPhotoAlbum(BaseObject):
    """VK Object Photos/PhotosPhotoAlbum

    created - Date when the album has been created in Unixtime
    description - Photo album description
    id - Photo album ID
    owner_id - Album owner's ID
    size - Photos number
    title - Photo album title
    updated - Date when the album has been updated last time in Unixtime
    """

    created: Optional[int] = None
    description: Optional[str] = None
    id: Optional[int] = None
    owner_id: Optional[int] = None
    size: Optional[int] = None
    thumb: Optional["PhotosPhoto"] = None
    title: Optional[str] = None
    updated: Optional[int] = None


class PhotosPhotoAlbumFull(BaseObject):
    """VK Object Photos/PhotosPhotoAlbumFull

    can_upload - Information whether current user can upload photo to the album
    comments_disabled - Information whether album comments are disabled
    created - Date when the album has been created in Unixtime
    description - Photo album description
    id - Photo album ID
    owner_id - Album owner's ID
    size - Photos number
    thumb_id - Thumb photo ID
    thumb_is_last - Information whether the album thumb is last photo
    thumb_src - URL of the thumb image
    title - Photo album title
    updated - Date when the album has been updated last time in Unixtime
    upload_by_admins_only - Information whether only community administrators can upload photos
    """

    can_upload: Optional["BaseBoolInt"] = None
    comments_disabled: Optional["BaseBoolInt"] = None
    created: Optional[int] = None
    description: Optional[str] = None
    id: Optional[int] = None
    owner_id: Optional[int] = None
    size: Optional[int] = None
    sizes: Optional[List["PhotosPhotoSizes"]] = None
    thumb_id: Optional[int] = None
    thumb_is_last: Optional["BaseBoolInt"] = None
    thumb_src: Optional[str] = None
    title: Optional[str] = None
    updated: Optional[int] = None
    upload_by_admins_only: Optional["BaseBoolInt"] = None


class PhotosPhotoFull(BaseObject):
    """VK Object Photos/PhotosPhotoFull

    access_key - Access key for the photo
    album_id - Album ID
    can_comment - Information whether current user can comment the photo
    date - Date when uploaded
    height - Original photo height
    id - Photo ID
    lat - Latitude
    long - Longitude
    owner_id - Photo owner's ID
    post_id - Post ID
    text - Photo caption
    user_id - ID of the user who have uploaded the photo
    width - Original photo width
    """

    access_key: Optional[str] = None
    album_id: Optional[int] = None
    can_comment: Optional["BaseBoolInt"] = None
    comments: Optional["BaseObjectCount"] = None
    date: Optional[int] = None
    height: Optional[int] = None
    id: Optional[int] = None
    images: Optional[List["PhotosImage"]] = None
    lat: Optional[float] = None
    likes: Optional["BaseLikes"] = None
    long: Optional[float] = None
    owner_id: Optional[int] = None
    post_id: Optional[int] = None
    reposts: Optional["BaseObjectCount"] = None
    tags: Optional["BaseObjectCount"] = None
    text: Optional[str] = None
    user_id: Optional[int] = None
    width: Optional[int] = None


class PhotosPhotoFullXtrRealOffset(BaseObject):
    """VK Object Photos/PhotosPhotoFullXtrRealOffset

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
    text - Photo caption
    user_id - ID of the user who have uploaded the photo
    width - Original photo width
    """

    access_key: Optional[str] = None
    album_id: Optional[int] = None
    can_comment: Optional["BaseBoolInt"] = None
    comments: Optional["BaseObjectCount"] = None
    date: Optional[int] = None
    height: Optional[int] = None
    hidden: Optional["BasePropertyExists"] = None
    id: Optional[int] = None
    lat: Optional[float] = None
    likes: Optional["BaseLikes"] = None
    long: Optional[float] = None
    owner_id: Optional[int] = None
    photo_1280: Optional[str] = None
    photo_130: Optional[str] = None
    photo_2560: Optional[str] = None
    photo_604: Optional[str] = None
    photo_75: Optional[str] = None
    photo_807: Optional[str] = None
    post_id: Optional[int] = None
    real_offset: Optional[int] = None
    reposts: Optional["BaseObjectCount"] = None
    sizes: Optional[List["PhotosPhotoSizes"]] = None
    tags: Optional["BaseObjectCount"] = None
    text: Optional[str] = None
    user_id: Optional[int] = None
    width: Optional[int] = None


class PhotosPhotoSizes(BaseObject):
    """VK Object Photos/PhotosPhotoSizes"""

    height: Optional[int] = None
    url: Optional[str] = None
    src: Optional[str] = None
    type: Optional["PhotosPhotoSizesType"] = None
    width: Optional[int] = None


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


class PhotosPhotoTag(BaseObject):
    """VK Object Photos/PhotosPhotoTag

    date - Date when tag has been added in Unixtime
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

    date: Optional[int] = None
    id: Optional[int] = None
    placer_id: Optional[int] = None
    tagged_name: Optional[str] = None
    user_id: Optional[int] = None
    viewed: Optional["BaseBoolInt"] = None
    x: Optional[float] = None
    x2: Optional[float] = None
    y: Optional[float] = None
    y2: Optional[float] = None


class PhotosPhotoUpload(BaseObject):
    """VK Object Photos/PhotosPhotoUpload

    album_id - Album ID
    upload_url - URL to upload photo
    fallback_upload_url - Fallback URL if upload_url returned error
    user_id - User ID
    group_id - Group ID
    """

    album_id: Optional[int] = None
    upload_url: Optional[str] = None
    fallback_upload_url: Optional[str] = None
    user_id: Optional[int] = None
    group_id: Optional[int] = None


class PhotosPhotoUploadResponse(BaseObject):
    """VK Object Photos/PhotosPhotoUploadResponse

    aid - Album ID
    hash - Uploading hash
    photos_list - Uploaded photos data
    server - Upload server number
    """

    aid: Optional[int] = None
    hash: Optional[str] = None
    photos_list: Optional[str] = None
    server: Optional[int] = None


class PhotosPhotoXtrRealOffset(BaseObject):
    """VK Object Photos/PhotosPhotoXtrRealOffset

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
    text - Photo caption
    user_id - ID of the user who have uploaded the photo
    width - Original photo width
    """

    access_key: Optional[str] = None
    album_id: Optional[int] = None
    date: Optional[int] = None
    height: Optional[int] = None
    hidden: Optional["BasePropertyExists"] = None
    id: Optional[int] = None
    lat: Optional[float] = None
    long: Optional[float] = None
    owner_id: Optional[int] = None
    photo_1280: Optional[str] = None
    photo_130: Optional[str] = None
    photo_2560: Optional[str] = None
    photo_604: Optional[str] = None
    photo_75: Optional[str] = None
    photo_807: Optional[str] = None
    post_id: Optional[int] = None
    real_offset: Optional[int] = None
    sizes: Optional[List["PhotosPhotoSizes"]] = None
    text: Optional[str] = None
    user_id: Optional[int] = None
    width: Optional[int] = None


class PhotosPhotoXtrTagInfo(BaseObject):
    """VK Object Photos/PhotosPhotoXtrTagInfo

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
    tag_created - Date when tag has been added in Unixtime
    tag_id - Tag ID
    text - Photo caption
    user_id - ID of the user who have uploaded the photo
    width - Original photo width
    """

    access_key: Optional[str] = None
    album_id: Optional[int] = None
    date: Optional[int] = None
    height: Optional[int] = None
    id: Optional[int] = None
    lat: Optional[float] = None
    long: Optional[float] = None
    owner_id: Optional[int] = None
    photo_1280: Optional[str] = None
    photo_130: Optional[str] = None
    photo_2560: Optional[str] = None
    photo_604: Optional[str] = None
    photo_75: Optional[str] = None
    photo_807: Optional[str] = None
    placer_id: Optional[int] = None
    post_id: Optional[int] = None
    sizes: Optional[List["PhotosPhotoSizes"]] = None
    tag_created: Optional[int] = None
    tag_id: Optional[int] = None
    text: Optional[str] = None
    user_id: Optional[int] = None
    width: Optional[int] = None


class PhotosTagsSuggestionItem(BaseObject):
    """VK Object Photos/PhotosTagsSuggestionItem"""

    title: Optional[str] = None
    type: Optional[str] = None
    buttons: Optional[List["PhotosTagsSuggestionItemButton"]] = None
    photo: Optional["PhotosPhoto"] = None
    tags: Optional[List["PhotosPhotoTag"]] = None


class PhotosTagsSuggestionItemButton(BaseObject):
    """VK Object Photos/PhotosTagsSuggestionItemButton"""

    title: Optional[str] = None
    action: Optional[str] = None
    style: Optional[str] = None


class PhotosWallUploadResponse(BaseObject):
    """VK Object Photos/PhotosWallUploadResponse

    hash - Uploading hash
    photo - Uploaded photo data
    server - Upload server number
    """

    hash: Optional[str] = None
    photo: Optional[str] = None
    server: Optional[int] = None


class PollsAnswer(BaseObject):
    """VK Object Polls/PollsAnswer

    id - Answer ID
    rate - Answer rate in percents
    text - Answer text
    votes - Votes number
    """

    id: Optional[int] = None
    rate: Optional[float] = None
    text: Optional[str] = None
    votes: Optional[int] = None


class PollsBackground(BaseObject):
    """VK Object Polls/PollsBackground

    angle - Gradient angle with 0 on positive X axis
    color - Hex color code without #
    height - Original height of pattern tile
    images - Pattern tiles
    points - Gradient points
    width - Original with of pattern tile
    """

    angle: Optional[int] = None
    color: Optional[str] = None
    height: Optional[int] = None
    id: Optional[int] = None
    name: Optional[str] = None
    images: Optional[List["BaseImage"]] = None
    points: Optional[List["BaseGradientPoint"]] = None
    type: Optional[str] = None
    width: Optional[int] = None


class PollsFriend(BaseObject):
    """VK Object Polls/PollsFriend"""

    id: Optional[int] = None


class PollsPoll(BaseObject):
    """VK Object Polls/PollsPoll"""

    anonymous: Optional["PollsPollAnonymous"] = None
    friends: Optional[List["PollsFriend"]] = None
    multiple: Optional[bool] = None
    answer_id: Optional[int] = None
    end_date: Optional[int] = None
    answer_ids: Optional[List[int]] = None
    closed: Optional[bool] = None
    is_board: Optional[bool] = None
    can_edit: Optional[bool] = None
    can_vote: Optional[bool] = None
    can_report: Optional[bool] = None
    can_share: Optional[bool] = None
    photo: Optional["PollsBackground"] = None
    answers: Optional[List["PollsAnswer"]] = None
    created: Optional[int] = None
    id: Optional[int] = None
    owner_id: Optional[int] = None
    author_id: Optional[int] = None
    question: Optional[str] = None
    background: Optional["PollsBackground"] = None
    votes: Optional[int] = None
    disable_unvote: Optional[bool] = None


PollsPollAnonymous = Optional[bool]  # Information whether the field is anonymous


class PollsVoters(BaseObject):
    """VK Object Polls/PollsVoters

    answer_id - Answer ID
    """

    answer_id: Optional[int] = None
    users: Optional["PollsVotersUsers"] = None


class PollsVotersUsers(BaseObject):
    """VK Object Polls/PollsVotersUsers

    count - Votes number
    """

    count: Optional[int] = None
    items: Optional[List[int]] = None


class PrettyCardsPrettyCard(BaseObject):
    """VK Object PrettyCards/PrettyCardsPrettyCard

    button - Button key
    button_text - Button text in current language
    card_id - Card ID (long int returned as string)
    link_url - Link URL
    photo - Photo ID (format "<owner_id>_<media_id>")
    price - Price if set (decimal number returned as string)
    price_old - Old price if set (decimal number returned as string)
    title - Title
    """

    button: Optional[str] = None
    button_text: Optional[str] = None
    card_id: Optional[str] = None
    images: Optional[List["BaseImage"]] = None
    link_url: Optional[str] = None
    photo: Optional[str] = None
    price: Optional[str] = None
    price_old: Optional[str] = None
    title: Optional[str] = None


class SearchHint(BaseObject):
    """VK Object Search/SearchHint"""

    app: Optional["AppsApp"] = None
    description: Optional[str] = None
    _global: Optional["BaseBoolInt"] = None
    group: Optional["GroupsGroup"] = None
    profile: Optional["UsersUserMin"] = None
    section: Optional["SearchHintSection"] = None
    type: Optional["SearchHintType"] = None


class SearchHintSection(enum.Enum):
    """ Section title """

    GROUPS = "groups"
    EVENTS = "events"
    PUBLICS = "publics"
    CORRESPONDENTS = "correspondents"
    PEOPLE = "people"
    FRIENDS = "friends"
    MUTUAL_FRIENDS = "mutual_friends"


class SearchHintType(enum.Enum):
    """ Object type """

    GROUP = "group"
    PROFILE = "profile"
    VK_APP = "vk_app"
    APP = "app"
    HTML5_GAME = "html5_game"


class SecureLevel(BaseObject):
    """VK Object Secure/SecureLevel

    level - Level
    uid - User ID
    """

    level: Optional[int] = None
    uid: Optional[int] = None


class SecureSmsNotification(BaseObject):
    """VK Object Secure/SecureSmsNotification

    app_id - Application ID
    date - Date when message has been sent in Unixtime
    id - Notification ID
    message - Messsage text
    user_id - User ID
    """

    app_id: Optional[str] = None
    date: Optional[str] = None
    id: Optional[str] = None
    message: Optional[str] = None
    user_id: Optional[str] = None


class SecureTokenChecked(BaseObject):
    """VK Object Secure/SecureTokenChecked

    date - Date when access_token has been generated in Unixtime
    expire - Date when access_token will expire in Unixtime
    success - Returns if successfully processed
    user_id - User ID
    """

    date: Optional[int] = None
    expire: Optional[int] = None
    success: Optional[int] = None
    user_id: Optional[int] = None


class SecureTransaction(BaseObject):
    """VK Object Secure/SecureTransaction

    date - Transaction date in Unixtime
    id - Transaction ID
    uid_from - From ID
    uid_to - To ID
    votes - Votes number
    """

    date: Optional[int] = None
    id: Optional[int] = None
    uid_from: Optional[int] = None
    uid_to: Optional[int] = None
    votes: Optional[int] = None


class StatsActivity(BaseObject):
    """VK Object Stats/StatsActivity

    comments - Comments number
    copies - Reposts number
    hidden - Hidden from news count
    likes - Likes number
    subscribed - New subscribers count
    unsubscribed - Unsubscribed count
    """

    comments: Optional[int] = None
    copies: Optional[int] = None
    hidden: Optional[int] = None
    likes: Optional[int] = None
    subscribed: Optional[int] = None
    unsubscribed: Optional[int] = None


class StatsCity(BaseObject):
    """VK Object Stats/StatsCity

    count - Visitors number
    name - City name
    value - City ID
    """

    count: Optional[int] = None
    name: Optional[str] = None
    value: Optional[int] = None


class StatsCountry(BaseObject):
    """VK Object Stats/StatsCountry

    code - Country code
    count - Visitors number
    name - Country name
    value - Country ID
    """

    code: Optional[str] = None
    count: Optional[int] = None
    name: Optional[str] = None
    value: Optional[int] = None


class StatsPeriod(BaseObject):
    """VK Object Stats/StatsPeriod

    period_from - Unix timestamp
    period_to - Unix timestamp
    """

    activity: Optional["StatsActivity"] = None
    period_from: Optional[int] = None
    period_to: Optional[int] = None
    reach: Optional["StatsReach"] = None
    visitors: Optional["StatsViews"] = None


class StatsReach(BaseObject):
    """VK Object Stats/StatsReach

    mobile_reach - Reach count from mobile devices
    reach - Reach count
    reach_subscribers - Subscribers reach count
    """

    age: Optional[List["StatsSexAge"]] = None
    cities: Optional[List["StatsCity"]] = None
    countries: Optional[List["StatsCountry"]] = None
    mobile_reach: Optional[int] = None
    reach: Optional[int] = None
    reach_subscribers: Optional[int] = None
    sex: Optional[List["StatsSexAge"]] = None
    sex_age: Optional[List["StatsSexAge"]] = None


class StatsSexAge(BaseObject):
    """VK Object Stats/StatsSexAge

    count - Visitors number
    value - Sex/age value
    """

    count: Optional[int] = None
    value: Optional[str] = None
    reach: Optional[int] = None
    reach_subscribers: Optional[int] = None
    count_subscribers: Optional[int] = None


class StatsViews(BaseObject):
    """VK Object Stats/StatsViews

    mobile_views - Number of views from mobile devices
    views - Views number
    visitors - Visitors number
    """

    age: Optional[List["StatsSexAge"]] = None
    cities: Optional[List["StatsCity"]] = None
    countries: Optional[List["StatsCountry"]] = None
    mobile_views: Optional[int] = None
    sex: Optional[List["StatsSexAge"]] = None
    sex_age: Optional[List["StatsSexAge"]] = None
    views: Optional[int] = None
    visitors: Optional[int] = None


class StatsWallpostStat(BaseObject):
    """VK Object Stats/StatsWallpostStat

    hide - Hidings number
    join_group - People have joined the group
    links - Link clickthrough
    reach_subscribers - Subscribers reach
    reach_total - Total reach
    report - Reports number
    to_group - Clickthrough to community
    unsubscribe - Unsubscribed members
    """

    post_id: Optional[int] = None
    hide: Optional[int] = None
    join_group: Optional[int] = None
    links: Optional[int] = None
    reach_subscribers: Optional[int] = None
    reach_subscribers_count: Optional[int] = None
    reach_total: Optional[int] = None
    reach_total_count: Optional[int] = None
    reach_viral: Optional[int] = None
    reach_ads: Optional[int] = None
    report: Optional[int] = None
    to_group: Optional[int] = None
    unsubscribe: Optional[int] = None
    sex_age: Optional[List["StatsSexAge"]] = None


class StatusStatus(BaseObject):
    """VK Object Status/StatusStatus

    text - Status text
    """

    text: Optional[str] = None
    audio: Optional["AudioAudio"] = None


class StorageValue(BaseObject):
    """VK Object Storage/StorageValue"""

    key: Optional[str] = None
    value: Optional[str] = None


class StoriesClickableArea(BaseObject):
    """VK Object Stories/StoriesClickableArea"""

    x: Optional[int] = None
    y: Optional[int] = None


class StoriesClickableSticker(BaseObject):
    """VK Object Stories/StoriesClickableSticker

    id - Clickable sticker ID
    color - Color, hex format
    sticker_id - Sticker ID
    sticker_pack_id - Sticker pack ID
    app_context - Additional context for app sticker
    has_new_interactions - Whether current user has unread interaction with this app
    is_broadcast_notify_allowed - Whether current user allowed broadcast notify from this app
    """

    clickable_area: Optional[List["StoriesClickableArea"]] = None
    id: Optional[int] = None
    hashtag: Optional[str] = None
    link_object: Optional["BaseLink"] = None
    mention: Optional[str] = None
    tooltip_text: Optional[str] = None
    owner_id: Optional[int] = None
    story_id: Optional[int] = None
    question: Optional[str] = None
    question_button: Optional[str] = None
    place_id: Optional[int] = None
    market_item: Optional["MarketMarketItem"] = None
    audio: Optional["AudioAudio"] = None
    audio_start_time: Optional[int] = None
    style: Optional[str] = None
    type: Optional[str] = None
    subtype: Optional[str] = None
    post_owner_id: Optional[int] = None
    post_id: Optional[int] = None
    poll: Optional["PollsPoll"] = None
    color: Optional[str] = None
    sticker_id: Optional[int] = None
    sticker_pack_id: Optional[int] = None
    app: Optional["AppsAppMin"] = None
    app_context: Optional[str] = None
    has_new_interactions: Optional[bool] = None
    is_broadcast_notify_allowed: Optional[bool] = None


class StoriesClickableStickers(BaseObject):
    """VK Object Stories/StoriesClickableStickers"""

    clickable_stickers: Optional[List["StoriesClickableSticker"]] = None
    original_height: Optional[int] = None
    original_width: Optional[int] = None


class StoriesFeedItem(BaseObject):
    """VK Object Stories/StoriesFeedItem

    type - Type of Feed Item
    stories - Author stories
    grouped - Grouped stories of various authors (for types community_grouped_stories/app_grouped_stories type)
    app - App, which stories has been grouped (for type app_grouped_stories)
    promo_data - Additional data for promo stories (for type promo_stories)
    """

    type: Optional[str] = None
    stories: Optional[List["StoriesStory"]] = None
    grouped: Optional[List["StoriesFeedItem"]] = None
    app: Optional["AppsAppMin"] = None
    promo_data: Optional["StoriesPromoBlock"] = None


class StoriesPromoBlock(BaseObject):
    """VK Object Stories/StoriesPromoBlock

    name - Promo story title
    photo_50 - RL of square photo of the story with 50 pixels in width
    photo_100 - RL of square photo of the story with 100 pixels in width
    not_animated - Hide animation for promo story
    """

    name: Optional[str] = None
    photo_50: Optional[str] = None
    photo_100: Optional[str] = None
    not_animated: Optional[bool] = None


class StoriesReplies(BaseObject):
    """VK Object Stories/StoriesReplies

    count - Replies number.
    new - New replies number.
    """

    count: Optional[int] = None
    new: Optional[int] = None


class StoriesStatLine(BaseObject):
    """VK Object Stories/StoriesStatLine"""

    name: Optional[str] = None
    counter: Optional[int] = None
    is_unavailable: Optional[bool] = None


class StoriesStory(BaseObject):
    """VK Object Stories/StoriesStory

    access_key - Access key for private object.
    can_comment - Information whether current user can comment the story (0 - no, 1 - yes).
    can_reply - Information whether current user can reply to the story (0 - no, 1 - yes).
    can_see - Information whether current user can see the story (0 - no, 1 - yes).
    can_like - Information whether current user can like the story.
    can_share - Information whether current user can share the story (0 - no, 1 - yes).
    can_hide - Information whether current user can hide the story (0 - no, 1 - yes).
    date - Date when story has been added in Unixtime.
    expires_at - Story expiration time. Unixtime.
    id - Story ID.
    is_deleted - Information whether the story is deleted (false - no, true - yes).
    is_expired - Information whether the story is expired (false - no, true - yes).
    owner_id - Story owner's ID.
    parent_story_access_key - Access key for private object.
    parent_story_id - Parent story ID.
    parent_story_owner_id - Parent story owner's ID.
    replies - Replies counters to current story.
    seen - Information whether current user has seen the story or not (0 - no, 1 - yes).
    views - Views number.
    can_ask - Information whether story has question sticker and current user can send question to the author
    can_ask_anonymous - Information whether story has question sticker and current user can send anonymous question to the author
    """

    access_key: Optional[str] = None
    can_comment: Optional["BaseBoolInt"] = None
    can_reply: Optional["BaseBoolInt"] = None
    can_see: Optional["BaseBoolInt"] = None
    can_like: Optional[bool] = None
    can_share: Optional["BaseBoolInt"] = None
    can_hide: Optional["BaseBoolInt"] = None
    date: Optional[int] = None
    expires_at: Optional[int] = None
    id: Optional[int] = None
    is_deleted: Optional[bool] = None
    is_expired: Optional[bool] = None
    link: Optional["StoriesStoryLink"] = None
    owner_id: Optional[int] = None
    parent_story: Optional["StoriesStory"] = None
    parent_story_access_key: Optional[str] = None
    parent_story_id: Optional[int] = None
    parent_story_owner_id: Optional[int] = None
    photo: Optional["PhotosPhoto"] = None
    replies: Optional["StoriesReplies"] = None
    seen: Optional["BaseBoolInt"] = None
    type: Optional["StoriesStoryType"] = None
    clickable_stickers: Optional["StoriesClickableStickers"] = None
    video: Optional["VideoVideo"] = None
    views: Optional[int] = None
    can_ask: Optional["BaseBoolInt"] = None
    can_ask_anonymous: Optional["BaseBoolInt"] = None
    narratives_count: Optional[int] = None
    first_narrative_title: Optional[str] = None
    birthday_wish_user_id: Optional[int] = None


class StoriesStoryLink(BaseObject):
    """VK Object Stories/StoriesStoryLink

    text - Link text
    url - Link URL
    """

    text: Optional[str] = None
    url: Optional[str] = None


class StoriesStoryStats(BaseObject):
    """VK Object Stories/StoriesStoryStats"""

    answer: Optional["StoriesStoryStatsStat"] = None
    bans: Optional["StoriesStoryStatsStat"] = None
    open_link: Optional["StoriesStoryStatsStat"] = None
    replies: Optional["StoriesStoryStatsStat"] = None
    shares: Optional["StoriesStoryStatsStat"] = None
    subscribers: Optional["StoriesStoryStatsStat"] = None
    views: Optional["StoriesStoryStatsStat"] = None
    likes: Optional["StoriesStoryStatsStat"] = None


class StoriesStoryStatsStat(BaseObject):
    """VK Object Stories/StoriesStoryStatsStat"""

    count: Optional[int] = None
    state: Optional["StoriesStoryStatsState"] = None


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


class StoriesViewersItem(BaseObject):
    """VK Object Stories/StoriesViewersItem

    is_liked - user has like for this object
    user_id - user id
    """

    is_liked: Optional[bool] = None
    user_id: Optional[int] = None
    user: Optional["UsersUserFull"] = None


class UsersCareer(BaseObject):
    """VK Object Users/UsersCareer

    city_id - City ID
    company - Company name
    country_id - Country ID
    from - From year
    group_id - Community ID
    id - Career ID
    position - Position
    until - Till year
    """

    city_id: Optional[int] = None
    company: Optional[str] = None
    country_id: Optional[int] = None
    _from: Optional[int] = None
    group_id: Optional[int] = None
    id: Optional[int] = None
    position: Optional[str] = None
    until: Optional[int] = None


class UsersExports(BaseObject):
    """VK Object Users/UsersExports"""

    facebook: Optional[int] = None
    livejournal: Optional[int] = None
    twitter: Optional[int] = None


class UsersFields(enum.Enum):
    """ UsersFields enum """

    PHOTO_ID = "photo_id"
    VERIFIED = "verified"
    SEX = "sex"
    BDATE = "bdate"
    CITY = "city"
    COUNTRY = "country"
    HOME_TOWN = "home_town"
    HAS_PHOTO = "has_photo"
    PHOTO_50 = "photo_50"
    PHOTO_100 = "photo_100"
    PHOTO_200_ORIG = "photo_200_orig"
    PHOTO_200 = "photo_200"
    PHOTO_400_ORIG = "photo_400_orig"
    PHOTO_MAX = "photo_max"
    PHOTO_MAX_ORIG = "photo_max_orig"
    ONLINE = "online"
    LISTS = "lists"
    DOMAIN = "domain"
    HAS_MOBILE = "has_mobile"
    CONTACTS = "contacts"
    SITE = "site"
    EDUCATION = "education"
    UNIVERSITIES = "universities"
    SCHOOLS = "schools"
    STATUS = "status"
    LAST_SEEN = "last_seen"
    FOLLOWERS_COUNT = "followers_count"
    COUNTERS = "counters"
    COMMON_COUNT = "common_count"
    OCCUPATION = "occupation"
    NICKNAME = "nickname"
    RELATIVES = "relatives"
    RELATION = "relation"
    PERSONAL = "personal"
    CONNECTIONS = "connections"
    EXPORTS = "exports"
    WALL_COMMENTS = "wall_comments"
    ACTIVITIES = "activities"
    INTERESTS = "interests"
    MUSIC = "music"
    MOVIES = "movies"
    TV = "tv"
    BOOKS = "books"
    GAMES = "games"
    ABOUT = "about"
    QUOTES = "quotes"
    CAN_POST = "can_post"
    CAN_SEE_ALL_POSTS = "can_see_all_posts"
    CAN_SEE_AUDIO = "can_see_audio"
    CAN_WRITE_PRIVATE_MESSAGE = "can_write_private_message"
    CAN_SEND_FRIEND_REQUEST = "can_send_friend_request"
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
    VIDEO_LIVE_LEVEL = "video_live_level"
    VIDEO_LIVE_COUNT = "video_live_count"
    CLIPS_COUNT = "clips_count"


class UsersLastSeen(BaseObject):
    """VK Object Users/UsersLastSeen

    platform - Type of the platform that used for the last authorization
    time - Last visit date (in Unix time)
    """

    platform: Optional[int] = None
    time: Optional[int] = None


class UsersMilitary(BaseObject):
    """VK Object Users/UsersMilitary

    country_id - Country ID
    from - From year
    id - Military ID
    unit - Unit name
    unit_id - Unit ID
    until - Till year
    """

    country_id: Optional[int] = None
    _from: Optional[int] = None
    id: Optional[int] = None
    unit: Optional[str] = None
    unit_id: Optional[int] = None
    until: Optional[int] = None


class UsersOccupation(BaseObject):
    """VK Object Users/UsersOccupation

    id - ID of school, university, company group
    name - Name of occupation
    type - Type of occupation
    """

    id: Optional[int] = None
    name: Optional[str] = None
    type: Optional[str] = None


class UsersOnlineInfo(BaseObject):
    """VK Object Users/UsersOnlineInfo

    visible - Whether you can see real online status of user or not
    last_seen - Last time we saw user being active
    is_online - Whether user is currently online or not
    app_id - Application id from which user is currently online or was last seen online
    is_mobile - Is user online from desktop app or mobile app
    status - In case user online is not visible, it indicates approximate timeframe of user online
    """

    visible: Optional[bool] = None
    last_seen: Optional[int] = None
    is_online: Optional[bool] = None
    app_id: Optional[int] = None
    is_mobile: Optional[bool] = None
    status: Optional[str] = None


class UsersPersonal(BaseObject):
    """VK Object Users/UsersPersonal

    alcohol - User's views on alcohol
    inspired_by - User's inspired by
    life_main - User's personal priority in life
    people_main - User's personal priority in people
    political - User's political views
    religion - User's religion
    religion_id - User's religion id
    smoking - User's views on smoking
    """

    alcohol: Optional[int] = None
    inspired_by: Optional[str] = None
    langs: Optional[List[str]] = None
    life_main: Optional[int] = None
    people_main: Optional[int] = None
    political: Optional[int] = None
    religion: Optional[str] = None
    religion_id: Optional[int] = None
    smoking: Optional[int] = None


class UsersRelative(BaseObject):
    """VK Object Users/UsersRelative

    birth_date - Date of child birthday (format dd.mm.yyyy)
    id - Relative ID
    name - Name of relative
    type - Relative type
    """

    birth_date: Optional[str] = None
    id: Optional[int] = None
    name: Optional[str] = None
    type: Optional[str] = None


class UsersSchool(BaseObject):
    """VK Object Users/UsersSchool

    city - City ID
    class - School class letter
    country - Country ID
    id - School ID
    name - School name
    type - School type ID
    type_str - School type name
    year_from - Year the user started to study
    year_graduated - Graduation year
    year_to - Year the user finished to study
    """

    city: Optional[int] = None
    _class: Optional[str] = None
    country: Optional[int] = None
    id: Optional[str] = None
    name: Optional[str] = None
    type: Optional[int] = None
    type_str: Optional[str] = None
    year_from: Optional[int] = None
    year_graduated: Optional[int] = None
    year_to: Optional[int] = None


class UsersSubscriptionsItem(BaseObject):
    """VK Object Users/UsersSubscriptionsItem"""


class UsersUniversity(BaseObject):
    """VK Object Users/UsersUniversity

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
    """

    chair: Optional[int] = None
    chair_name: Optional[str] = None
    city: Optional[int] = None
    country: Optional[int] = None
    education_form: Optional[str] = None
    education_status: Optional[str] = None
    faculty: Optional[int] = None
    faculty_name: Optional[str] = None
    graduation: Optional[int] = None
    id: Optional[int] = None
    name: Optional[str] = None


class UsersUserConnections(BaseObject):
    """VK Object Users/UsersUserConnections

    skype - User's Skype nickname
    facebook - User's Facebook account
    facebook_name - User's Facebook name
    twitter - User's Twitter account
    livejournal - User's Livejournal account
    instagram - User's Instagram account
    """

    skype: Optional[str] = None
    facebook: Optional[str] = None
    facebook_name: Optional[str] = None
    twitter: Optional[str] = None
    livejournal: Optional[str] = None
    instagram: Optional[str] = None


class UsersUserCounters(BaseObject):
    """VK Object Users/UsersUserCounters

    albums - Albums number
    audios - Audios number
    followers - Followers number
    friends - Friends number
    gifts - Gifts number
    groups - Communities number
    notes - Notes number
    online_friends - Online friends number
    pages - Public pages number
    photos - Photos number
    subscriptions - Subscriptions number
    user_photos - Number of photos with user
    user_videos - Number of videos with user
    videos - Videos number
    """

    albums: Optional[int] = None
    audios: Optional[int] = None
    followers: Optional[int] = None
    friends: Optional[int] = None
    gifts: Optional[int] = None
    groups: Optional[int] = None
    notes: Optional[int] = None
    online_friends: Optional[int] = None
    pages: Optional[int] = None
    photos: Optional[int] = None
    subscriptions: Optional[int] = None
    user_photos: Optional[int] = None
    user_videos: Optional[int] = None
    videos: Optional[int] = None


class UsersUserMin(BaseObject):
    """VK Object Users/UsersUserMin"""

    deactivated: Optional[str] = None
    first_name: Optional[str] = None
    hidden: Optional[int] = None
    id: Optional[int] = None
    last_name: Optional[str] = None
    can_access_closed: Optional[bool] = None
    is_closed: Optional[bool] = None


class UsersUser(UsersUserMin):
    """VK Object Users/UsersUser

    sex - User sex
    screen_name - Domain name of the user's page
    photo_50 - URL of square photo of the user with 50 pixels in width
    photo_100 - URL of square photo of the user with 100 pixels in width
    online - Information whether the user is online
    online_mobile - Information whether the user is online in mobile site or application
    online_app - Application ID
    verified - Information whether the user is verified
    trending - Information whether the user has a "fire" pictogram.
    """

    sex: Optional["BaseSex"] = None
    screen_name: Optional[str] = None
    photo_50: Optional[str] = None
    photo_100: Optional[str] = None
    online_info: Optional["UsersOnlineInfo"] = None
    online: Optional["BaseBoolInt"] = None
    online_mobile: Optional["BaseBoolInt"] = None
    online_app: Optional[int] = None
    verified: Optional["BaseBoolInt"] = None
    trending: Optional["BaseBoolInt"] = None
    friend_status: Optional["FriendsFriendStatusStatus"] = None
    mutual: Optional["FriendsRequestsMutual"] = None


class UsersUserFull(UsersUser):
    """VK Object Users/UsersUserFull

    first_name_nom - User's first name in nominative case
    first_name_gen - User's first name in genitive case
    first_name_dat - User's first name in dative case
    first_name_acc - User's first name in accusative case
    first_name_ins - User's first name in instrumental case
    first_name_abl - User's first name in prepositional case
    last_name_nom - User's last name in nominative case
    last_name_gen - User's last name in genitive case
    last_name_dat - User's last name in dative case
    last_name_acc - User's last name in accusative case
    last_name_ins - User's last name in instrumental case
    last_name_abl - User's last name in prepositional case
    nickname - User nickname
    maiden_name - User maiden name
    domain - Domain name of the user's page
    bdate - User's date of birth
    timezone - User's timezone
    photo_200 - URL of square photo of the user with 200 pixels in width
    photo_max - URL of square photo of the user with maximum width
    photo_200_orig - URL of user's photo with 200 pixels in width
    photo_400_orig - URL of user's photo with 400 pixels in width
    photo_max_orig - URL of user's photo of maximum size
    photo_id - ID of the user's main photo
    has_photo - Information whether the user has main photo
    has_mobile - Information whether the user specified his phone number
    is_friend - Information whether the user is a friend of current user
    wall_comments - Information whether current user can comment wall posts
    can_post - Information whether current user can post on the user's wall
    can_see_all_posts - Information whether current user can see other users' audio on the wall
    can_see_audio - Information whether current user can see the user's audio
    can_write_private_message - Information whether current user can write private message
    can_send_friend_request - Information whether current user can send a friend request
    can_be_invited_group - Information whether current user can be invited to the community
    mobile_phone - User's mobile phone number
    home_phone - User's additional phone number
    site - User's website
    status - User's status
    activity - User's status
    followers_count - Number of user's followers
    video_live_level - User level in live streams achievements
    video_live_count - Number of user's live streams
    blacklisted - Information whether current user is in the requested user's blacklist.
    blacklisted_by_me - Information whether the requested user is in current user's blacklist
    is_favorite - Information whether the requested user is in faves of current user
    is_hidden_from_feed - Information whether the requested user is hidden from current user's newsfeed
    common_count - Number of common friends with current user
    university - University ID
    university_name - University name
    faculty - Faculty ID
    faculty_name - Faculty name
    graduation - Graduation year
    education_form - Education form
    education_status - User's education status
    home_town - User hometown
    relation - User relationship status
    is_subscribed_podcasts - Information whether current user is subscribed to podcasts
    can_subscribe_podcasts - Owner in whitelist or not
    can_subscribe_posts - Can subscribe to wall
    """

    first_name_nom: Optional[str] = None
    first_name_gen: Optional[str] = None
    first_name_dat: Optional[str] = None
    first_name_acc: Optional[str] = None
    first_name_ins: Optional[str] = None
    first_name_abl: Optional[str] = None
    last_name_nom: Optional[str] = None
    last_name_gen: Optional[str] = None
    last_name_dat: Optional[str] = None
    last_name_acc: Optional[str] = None
    last_name_ins: Optional[str] = None
    last_name_abl: Optional[str] = None
    nickname: Optional[str] = None
    maiden_name: Optional[str] = None
    domain: Optional[str] = None
    bdate: Optional[str] = None
    city: Optional["BaseObject"] = None
    country: Optional["BaseCountry"] = None
    timezone: Optional[int] = None
    owner_state: Optional["OwnerState"] = None
    photo_200: Optional[str] = None
    photo_max: Optional[str] = None
    photo_200_orig: Optional[str] = None
    photo_400_orig: Optional[str] = None
    photo_max_orig: Optional[str] = None
    photo_id: Optional[str] = None
    has_photo: Optional["BaseBoolInt"] = None
    has_mobile: Optional["BaseBoolInt"] = None
    is_friend: Optional["BaseBoolInt"] = None
    wall_comments: Optional["BaseBoolInt"] = None
    can_post: Optional["BaseBoolInt"] = None
    can_see_all_posts: Optional["BaseBoolInt"] = None
    can_see_audio: Optional["BaseBoolInt"] = None
    can_write_private_message: Optional["BaseBoolInt"] = None
    can_send_friend_request: Optional["BaseBoolInt"] = None
    can_be_invited_group: Optional[bool] = None
    mobile_phone: Optional[str] = None
    home_phone: Optional[str] = None
    site: Optional[str] = None
    status_audio: Optional["AudioAudio"] = None
    status: Optional[str] = None
    activity: Optional[str] = None
    last_seen: Optional["UsersLastSeen"] = None
    exports: Optional["UsersExports"] = None
    crop_photo: Optional["BaseCropPhoto"] = None
    followers_count: Optional[int] = None
    video_live_level: Optional[int] = None
    video_live_count: Optional[int] = None
    blacklisted: Optional["BaseBoolInt"] = None
    blacklisted_by_me: Optional["BaseBoolInt"] = None
    is_favorite: Optional["BaseBoolInt"] = None
    is_hidden_from_feed: Optional["BaseBoolInt"] = None
    common_count: Optional[int] = None
    occupation: Optional["UsersOccupation"] = None
    career: Optional[List["UsersCareer"]] = None
    military: Optional[List["UsersMilitary"]] = None
    university: Optional[int] = None
    university_name: Optional[str] = None
    faculty: Optional[int] = None
    faculty_name: Optional[str] = None
    graduation: Optional[int] = None
    education_form: Optional[str] = None
    education_status: Optional[str] = None
    home_town: Optional[str] = None
    relation: Optional["UsersUserRelation"] = None
    relation_partner: Optional["UsersUserMin"] = None
    personal: Optional["UsersPersonal"] = None
    universities: Optional[List["UsersUniversity"]] = None
    schools: Optional[List["UsersSchool"]] = None
    relatives: Optional[List["UsersRelative"]] = None
    is_subscribed_podcasts: Optional[bool] = None
    can_subscribe_podcasts: Optional[bool] = None
    can_subscribe_posts: Optional[bool] = None


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


class UsersUserSettingsXtr(BaseObject):
    """VK Object Users/UsersUserSettingsXtr"""

    connections: Optional["UsersUserConnections"] = None
    bdate: Optional[str] = None
    bdate_visibility: Optional[int] = None
    city: Optional["BaseCity"] = None
    country: Optional["BaseCountry"] = None
    first_name: Optional[str] = None
    home_town: Optional[str] = None
    last_name: Optional[str] = None
    maiden_name: Optional[str] = None
    name_request: Optional["AccountNameRequest"] = None
    personal: Optional["UsersPersonal"] = None
    phone: Optional[str] = None
    relation: Optional["UsersUserRelation"] = None
    relation_partner: Optional["UsersUserMin"] = None
    relation_pending: Optional["BaseBoolInt"] = None
    relation_requests: Optional[List["UsersUserMin"]] = None
    screen_name: Optional[str] = None
    sex: Optional["BaseSex"] = None
    status: Optional[str] = None
    status_audio: Optional["AudioAudio"] = None
    interests: Optional["AccountUserSettingsInterests"] = None
    languages: Optional[List[str]] = None


class UsersUserType(enum.Enum):
    """ Object type """

    PROFILE = "profile"


class UsersUserXtrCounters(UsersUserFull):
    """VK Object Users/UsersUserXtrCounters"""

    counters: Optional["UsersUserCounters"] = None


class UsersUserXtrType(UsersUser):
    """VK Object Users/UsersUserXtrType"""

    type: Optional["UsersUserType"] = None


class UsersUsersArray(BaseObject):
    """VK Object Users/UsersUsersArray

    count - Users number
    """

    count: Optional[int] = None
    items: Optional[List[int]] = None


class UtilsDomainResolved(BaseObject):
    """VK Object Utils/UtilsDomainResolved"""

    object_id: Optional[int] = None
    group_id: Optional[int] = None
    type: Optional["UtilsDomainResolvedType"] = None


class UtilsDomainResolvedType(enum.Enum):
    """ Object type """

    USER = "user"
    GROUP = "group"
    APPLICATION = "application"
    PAGE = "page"


class UtilsLastShortenedLink(BaseObject):
    """VK Object Utils/UtilsLastShortenedLink

    access_key - Access key for private stats
    key - Link key (characters after vk.cc/)
    short_url - Short link URL
    timestamp - Creation time in Unixtime
    url - Full URL
    views - Total views number
    """

    access_key: Optional[str] = None
    key: Optional[str] = None
    short_url: Optional[str] = None
    timestamp: Optional[int] = None
    url: Optional[str] = None
    views: Optional[int] = None


class UtilsLinkChecked(BaseObject):
    """VK Object Utils/UtilsLinkChecked"""

    link: Optional[str] = None
    status: Optional["UtilsLinkCheckedStatus"] = None


class UtilsLinkCheckedStatus(enum.Enum):
    """ Link status """

    NOT_BANNED = "not_banned"
    BANNED = "banned"
    PROCESSING = "processing"


class UsersBlockReason(enum.IntEnum):
    OTHER = 0
    SPAM = 1
    VERBAL_ABUSE = 2
    STRONG_LANGUAGE = 3
    IRRELEVANT_MESSAGES = 4


class UtilsLinkStats(BaseObject):
    """VK Object Utils/UtilsLinkStats

    key - Link key (characters after vk.cc/)
    """

    key: Optional[str] = None
    stats: Optional[List["UtilsStats"]] = None


class UtilsLinkStatsExtended(BaseObject):
    """VK Object Utils/UtilsLinkStatsExtended

    key - Link key (characters after vk.cc/)
    """

    key: Optional[str] = None
    stats: Optional[List["UtilsStatsExtended"]] = None


class UtilsShortLink(BaseObject):
    """VK Object Utils/UtilsShortLink

    access_key - Access key for private stats
    key - Link key (characters after vk.cc/)
    short_url - Short link URL
    url - Full URL
    """

    access_key: Optional[str] = None
    key: Optional[str] = None
    short_url: Optional[str] = None
    url: Optional[str] = None


class UtilsStats(BaseObject):
    """VK Object Utils/UtilsStats

    timestamp - Start time
    views - Total views number
    """

    timestamp: Optional[int] = None
    views: Optional[int] = None


class UtilsStatsCity(BaseObject):
    """VK Object Utils/UtilsStatsCity

    city_id - City ID
    views - Views number
    """

    city_id: Optional[int] = None
    views: Optional[int] = None


class UtilsStatsCountry(BaseObject):
    """VK Object Utils/UtilsStatsCountry

    country_id - Country ID
    views - Views number
    """

    country_id: Optional[int] = None
    views: Optional[int] = None


class UtilsStatsExtended(BaseObject):
    """VK Object Utils/UtilsStatsExtended

    timestamp - Start time
    views - Total views number
    """

    cities: Optional[List["UtilsStatsCity"]] = None
    countries: Optional[List["UtilsStatsCountry"]] = None
    sex_age: Optional[List["UtilsStatsSexAge"]] = None
    timestamp: Optional[int] = None
    views: Optional[int] = None


class UtilsStatsSexAge(BaseObject):
    """VK Object Utils/UtilsStatsSexAge

    age_range - Age denotation
    female -  Views by female users
    male -  Views by male users
    """

    age_range: Optional[str] = None
    female: Optional[int] = None
    male: Optional[int] = None


class VideoLiveSettings(BaseObject):
    """VK Object Video/VideoLiveSettings

    can_rewind - If user car rewind live or not
    is_endless - If live is endless or not
    max_duration - Max possible time for rewind
    """

    can_rewind: Optional["BaseBoolInt"] = None
    is_endless: Optional["BaseBoolInt"] = None
    max_duration: Optional[int] = None


class VideoRestrictionButton(BaseObject):
    """VK Object Video/VideoRestrictionButton"""

    action: Optional[str] = None
    title: Optional[str] = None


class VideoSaveResult(BaseObject):
    """VK Object Video/VideoSaveResult

    access_key - Video access key
    description - Video description
    owner_id - Video owner ID
    title - Video title
    upload_url - URL for the video uploading
    video_id - Video ID
    """

    access_key: Optional[str] = None
    description: Optional[str] = None
    owner_id: Optional[int] = None
    title: Optional[str] = None
    upload_url: Optional[str] = None
    video_id: Optional[int] = None


class VideoVideo(BaseObject):
    """VK Object Video/VideoVideo

    access_key - Video access key
    adding_date - Date when the video has been added in Unixtime
    can_comment - Information whether current user can comment the video
    can_edit - Information whether current user can edit the video
    can_like - Information whether current user can like the video
    can_repost - Information whether current user can repost the video
    can_subscribe - Information whether current user can subscribe to author of the video
    can_add_to_faves - Information whether current user can add the video to favourites
    can_add - Information whether current user can add the video
    can_attach_link - Information whether current user can attach action button to the video
    is_private - 1 if video is private
    comments - Number of comments
    date - Date when video has been uploaded in Unixtime
    description - Video description
    duration - Video duration in seconds
    width - Video width
    height - Video height
    id - Video ID
    owner_id - Video owner ID
    user_id - Id of the user who uploaded the video if it was uploaded to a group by member
    title - Video title
    is_favorite - Whether video is added to bookmarks
    player - Video embed URL
    processing - Returns if the video is processing
    converting - 1 if  video is being converted
    added - 1 if video is added to user's albums
    is_subscribed - 1 if user is subscribed to author of the video
    repeat - Information whether the video is repeated
    views - Number of views
    local_views - If video is external, number of views on vk
    content_restricted - Restriction code
    content_restricted_message - Restriction text
    balance - Live donations balance
    live_status - Live stream status
    live - 1 if the video is a live stream
    upcoming - 1 if the video is an upcoming stream
    spectators - Number of spectators of the stream
    platform - External platform
    """

    access_key: Optional[str] = None
    adding_date: Optional[int] = None
    can_comment: Optional["BaseBoolInt"] = None
    can_edit: Optional["BaseBoolInt"] = None
    can_like: Optional["BaseBoolInt"] = None
    can_repost: Optional["BaseBoolInt"] = None
    can_subscribe: Optional["BaseBoolInt"] = None
    can_add_to_faves: Optional["BaseBoolInt"] = None
    can_add: Optional["BaseBoolInt"] = None
    can_attach_link: Optional["BaseBoolInt"] = None
    is_private: Optional["BaseBoolInt"] = None
    comments: Optional[int] = None
    date: Optional[int] = None
    description: Optional[str] = None
    duration: Optional[int] = None
    image: Optional[List["VideoVideoImage"]] = None
    first_frame: Optional[List["VideoVideoImage"]] = None
    width: Optional[int] = None
    height: Optional[int] = None
    id: Optional[int] = None
    owner_id: Optional[int] = None
    user_id: Optional[int] = None
    title: Optional[str] = None
    is_favorite: Optional[bool] = None
    player: Optional[str] = None
    processing: Optional["BasePropertyExists"] = None
    converting: Optional["BaseBoolInt"] = None
    restriction: Optional["MediaRestriction"] = None
    added: Optional["BaseBoolInt"] = None
    is_subscribed: Optional["BaseBoolInt"] = None
    track_code: Optional[str] = None
    repeat: Optional["BasePropertyExists"] = None
    type: Optional[str] = None
    views: Optional[int] = None
    local_views: Optional[int] = None
    content_restricted: Optional[int] = None
    content_restricted_message: Optional[str] = None
    balance: Optional[int] = None
    live_status: Optional[str] = None
    live: Optional["BasePropertyExists"] = None
    upcoming: Optional["BasePropertyExists"] = None
    spectators: Optional[int] = None
    platform: Optional[str] = None
    likes: Optional["BaseLikes"] = None
    reposts: Optional["BaseRepostsInfo"] = None


class VideoVideoAlbumFull(BaseObject):
    """VK Object Video/VideoVideoAlbumFull

    count - Total number of videos in album
    id - Album ID
    image - Album cover image in different sizes
    image_blur - Need blur album thumb or not
    is_system - Information whether album is system
    owner_id - Album owner's ID
    title - Album title
    updated_time - Date when the album has been updated last time in Unixtime
    """

    count: Optional[int] = None
    id: Optional[int] = None
    image: Optional[List["VideoVideoImage"]] = None
    image_blur: Optional["BasePropertyExists"] = None
    is_system: Optional["BasePropertyExists"] = None
    owner_id: Optional[int] = None
    title: Optional[str] = None
    updated_time: Optional[int] = None


class VideoVideoFiles(BaseObject):
    """VK Object Video/VideoVideoFiles

    external - URL of the external player
    mp4_240 - URL of the mpeg4 file with 240p quality
    mp4_360 - URL of the mpeg4 file with 360p quality
    mp4_480 - URL of the mpeg4 file with 480p quality
    mp4_720 - URL of the mpeg4 file with 720p quality
    mp4_1080 - URL of the mpeg4 file with 1080p quality
    flv_320 - URL of the flv file with 320p quality
    """

    external: Optional[str] = None
    mp4_240: Optional[str] = None
    mp4_360: Optional[str] = None
    mp4_480: Optional[str] = None
    mp4_720: Optional[str] = None
    mp4_1080: Optional[str] = None
    flv_320: Optional[str] = None


class VideoVideoFull(VideoVideo):
    """VK Object Video/VideoVideoFull

    live_settings - Settings for live stream
    """

    files: Optional["VideoVideoFiles"] = None
    live_settings: Optional["VideoLiveSettings"] = None


class VideoVideoImage(BaseImage):
    """VK Object Video/VideoVideoImage"""

    with_padding: Optional["BasePropertyExists"] = None


class WallAppPost(BaseObject):
    """VK Object Wall/WallAppPost

    id - Application ID
    name - Application name
    photo_130 - URL of the preview image with 130 px in width
    photo_604 - URL of the preview image with 604 px in width
    """

    id: Optional[int] = None
    name: Optional[str] = None
    photo_130: Optional[str] = None
    photo_604: Optional[str] = None


class WallAttachedNote(BaseObject):
    """VK Object Wall/WallAttachedNote

    comments - Comments number
    date - Date when the note has been created in Unixtime
    id - Note ID
    owner_id - Note owner's ID
    read_comments - Read comments number
    title - Note title
    view_url - URL of the page with note preview
    """

    comments: Optional[int] = None
    date: Optional[int] = None
    id: Optional[int] = None
    owner_id: Optional[int] = None
    read_comments: Optional[int] = None
    title: Optional[str] = None
    view_url: Optional[str] = None


class WallCarouselBase(BaseObject):
    """VK Object Wall/WallCarouselBase

    carousel_offset - Index of current carousel element
    """

    carousel_offset: Optional[int] = None


class WallCommentAttachment(BaseObject):
    """VK Object Wall/WallCommentAttachment"""

    audio: Optional["AudioAudio"] = None
    doc: Optional["DocsDoc"] = None
    link: Optional["BaseLink"] = None
    market: Optional["MarketMarketItem"] = None
    market_market_album: Optional["MarketMarketAlbum"] = None
    note: Optional["WallAttachedNote"] = None
    page: Optional["PagesWikipageFull"] = None
    photo: Optional["PhotosPhoto"] = None
    sticker: Optional["BaseSticker"] = None
    type: Optional["WallCommentAttachmentType"] = None
    video: Optional["VideoVideo"] = None


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


class WallGeo(BaseObject):
    """VK Object Wall/WallGeo

    coordinates - Coordinates as string. <latitude> <longtitude>
    showmap - Information whether a map is showed
    type - Place type
    """

    coordinates: Optional[str] = None
    place: Optional["BasePlace"] = None
    showmap: Optional[int] = None
    type: Optional[str] = None


class WallGraffiti(BaseObject):
    """VK Object Wall/WallGraffiti

    id - Graffiti ID
    owner_id - Graffiti owner's ID
    photo_200 - URL of the preview image with 200 px in width
    photo_586 - URL of the preview image with 586 px in width
    """

    id: Optional[int] = None
    owner_id: Optional[int] = None
    photo_200: Optional[str] = None
    photo_586: Optional[str] = None


class WallPostCopyright(BaseObject):
    """VK Object Wall/WallPostCopyright"""

    id: Optional[int] = None
    link: Optional[str] = None
    name: Optional[str] = None
    type: Optional[str] = None


class WallPostSource(BaseObject):
    """VK Object Wall/WallPostSource"""

    data: Optional[str] = None
    platform: Optional[str] = None
    type: Optional["WallPostSourceType"] = None
    url: Optional[str] = None


class WallPostSourceType(enum.Enum):
    """ Type of post source """

    VK = "vk"
    WIDGET = "widget"
    API = "api"
    RSS = "rss"
    SMS = "sms"


class WallPostType(enum.Enum):
    """ Post type """

    POST = "post"
    COPY = "copy"
    REPLY = "reply"
    POSTPONE = "postpone"
    SUGGEST = "suggest"


class WallPostedPhoto(BaseObject):
    """VK Object Wall/WallPostedPhoto

    id - Photo ID
    owner_id - Photo owner's ID
    photo_130 - URL of the preview image with 130 px in width
    photo_604 - URL of the preview image with 604 px in width
    """

    id: Optional[int] = None
    owner_id: Optional[int] = None
    photo_130: Optional[str] = None
    photo_604: Optional[str] = None


class WallViews(BaseObject):
    """VK Object Wall/WallViews

    count - Count
    """

    count: Optional[int] = None


class WallWallComment(BaseObject):
    """VK Object Wall/WallWallComment

    date - Date when the comment has been added in Unixtime
    from_id - Author ID
    id - Comment ID
    real_offset - Real position of the comment
    reply_to_comment - Replied comment ID
    reply_to_user - Replied user ID
    text - Comment text
    """

    attachments: Optional[List["WallCommentAttachment"]] = None
    date: Optional[int] = None
    from_id: Optional[int] = None
    id: Optional[int] = None
    likes: Optional["BaseLikesInfo"] = None
    real_offset: Optional[int] = None
    reply_to_comment: Optional[int] = None
    reply_to_user: Optional[int] = None
    text: Optional[str] = None
    thread: Optional["CommentThread"] = None
    post_id: Optional[int] = None
    owner_id: Optional[int] = None
    parents_stack: Optional[List[int]] = None
    deleted: Optional[bool] = None


class WallWallpost(BaseObject):
    """VK Object Wall/WallWallpost

    access_key - Access key to private object
    copyright - Information about the source of the post
    date - Date of publishing in Unixtime
    edited - Date of editing in Unixtime
    from_id - Post author ID
    id - Post ID
    is_archived - Is post archived, only for post owners
    is_favorite - Information whether the post in favorites list
    likes - Count of likes
    owner_id - Wall owner's ID
    reposts - Count of views
    signer_id - Post signer ID
    text - Post text
    views - Count of views
    """

    access_key: Optional[str] = None
    attachments: Optional[List["WallWallpostAttachment"]] = None
    copyright: Optional["WallPostCopyright"] = None
    date: Optional[int] = None
    edited: Optional[int] = None
    from_id: Optional[int] = None
    geo: Optional["WallGeo"] = None
    id: Optional[int] = None
    is_archived: Optional[bool] = None
    is_favorite: Optional[bool] = None
    likes: Optional["BaseLikesInfo"] = None
    owner_id: Optional[int] = None
    post_source: Optional["WallPostSource"] = None
    post_type: Optional["WallPostType"] = None
    reposts: Optional["BaseRepostsInfo"] = None
    signer_id: Optional[int] = None
    text: Optional[str] = None
    views: Optional["WallViews"] = None


class WallWallpostAttachment(BaseObject):
    """VK Object Wall/WallWallpostAttachment"""

    access_key: Optional[str] = None
    album: Optional["PhotosPhotoAlbum"] = None
    app: Optional["WallAppPost"] = None
    audio: Optional["AudioAudio"] = None
    doc: Optional["DocsDoc"] = None
    event: Optional["EventsEventAttach"] = None
    group: Optional["GroupsGroupAttach"] = None
    graffiti: Optional["WallGraffiti"] = None
    link: Optional["BaseLink"] = None
    market: Optional["MarketMarketItem"] = None
    market_album: Optional["MarketMarketAlbum"] = None
    note: Optional["WallAttachedNote"] = None
    page: Optional["PagesWikipageFull"] = None
    photo: Optional["PhotosPhoto"] = None
    photos_list: Optional[List[str]] = None
    poll: Optional["PollsPoll"] = None
    posted_photo: Optional["WallPostedPhoto"] = None
    type: Optional["WallWallpostAttachmentType"] = None
    video: Optional["VideoVideo"] = None


class WallWallpostAttachmentType(enum.Enum):
    """ Attachment type """

    PHOTO = "photo"
    POSTED_PHOTO = "posted_photo"
    AUDIO = "audio"
    VIDEO = "video"
    DOC = "doc"
    LINK = "link"
    GRAFFITI = "graffiti"
    NOTE = "note"
    APP = "app"
    POLL = "poll"
    PAGE = "page"
    ALBUM = "album"
    PHOTOS_LIST = "photos_list"
    MARKET_MARKET_ALBUM = "market_market_album"
    MARKET = "market"
    EVENT = "event"


class WallWallpostFull(WallCarouselBase, WallWallpost):
    """VK Object Wall/WallWallpostFull

    can_edit - Information whether current user can edit the post
    created_by - Post creator ID (if post still can be edited)
    can_delete - Information whether current user can delete the post
    can_pin - Information whether current user can pin the post
    is_pinned - Information whether the post is pinned
    marked_as_ads - Information whether the post is marked as ads
    short_text_rate - Preview length control parameter
    """

    copy_history: Optional[List["WallWallpost"]] = None
    can_edit: Optional["BaseBoolInt"] = None
    created_by: Optional[int] = None
    can_delete: Optional["BaseBoolInt"] = None
    can_pin: Optional["BaseBoolInt"] = None
    is_pinned: Optional[int] = None
    comments: Optional["BaseCommentsInfo"] = None
    marked_as_ads: Optional["BaseBoolInt"] = None
    short_text_rate: Optional[float] = None


class WallWallpostToId(BaseObject):
    """VK Object Wall/WallWallpostToId

    copy_owner_id - ID of the source post owner
    copy_post_id - ID of the source post
    date - Date of publishing in Unixtime
    from_id - Post author ID
    id - Post ID
    is_favorite - Information whether the post in favorites list
    post_id - wall post ID (if comment)
    signer_id - Post signer ID
    text - Post text
    to_id - Wall owner's ID
    """

    attachments: Optional[List["WallWallpostAttachment"]] = None
    comments: Optional["BaseCommentsInfo"] = None
    copy_owner_id: Optional[int] = None
    copy_post_id: Optional[int] = None
    date: Optional[int] = None
    from_id: Optional[int] = None
    geo: Optional["WallGeo"] = None
    id: Optional[int] = None
    is_favorite: Optional[bool] = None
    likes: Optional["BaseLikesInfo"] = None
    post_id: Optional[int] = None
    post_source: Optional["WallPostSource"] = None
    post_type: Optional["WallPostType"] = None
    reposts: Optional["BaseRepostsInfo"] = None
    signer_id: Optional[int] = None
    text: Optional[str] = None
    to_id: Optional[int] = None


class WidgetsCommentMedia(BaseObject):
    """VK Object Widgets/WidgetsCommentMedia"""

    item_id: Optional[int] = None
    owner_id: Optional[int] = None
    thumb_src: Optional[str] = None
    type: Optional["WidgetsCommentMediaType"] = None


class WidgetsCommentMediaType(enum.Enum):
    """ Media type """

    AUDIO = "audio"
    PHOTO = "photo"
    VIDEO = "video"


class WidgetsCommentReplies(BaseObject):
    """VK Object Widgets/WidgetsCommentReplies

    can_post - Information whether current user can comment the post
    count - Comments number
    """

    can_post: Optional["BaseBoolInt"] = None
    count: Optional[int] = None
    replies: Optional[List["WidgetsCommentRepliesItem"]] = None


class WidgetsCommentRepliesItem(BaseObject):
    """VK Object Widgets/WidgetsCommentRepliesItem

    cid - Comment ID
    date - Date when the comment has been added in Unixtime
    text - Comment text
    uid - User ID
    """

    cid: Optional[int] = None
    date: Optional[int] = None
    likes: Optional["WidgetsWidgetLikes"] = None
    text: Optional[str] = None
    uid: Optional[int] = None
    user: Optional["UsersUserFull"] = None


class WidgetsWidgetComment(BaseObject):
    """VK Object Widgets/WidgetsWidgetComment

    can_delete - Information whether current user can delete the comment
    date - Date when the comment has been added in Unixtime
    from_id - Comment author ID
    id - Comment ID
    post_type - Post type
    text - Comment text
    to_id - Wall owner
    """

    attachments: Optional[List["WallCommentAttachment"]] = None
    can_delete: Optional["BaseBoolInt"] = None
    comments: Optional["WidgetsCommentReplies"] = None
    date: Optional[int] = None
    from_id: Optional[int] = None
    id: Optional[int] = None
    likes: Optional["BaseLikesInfo"] = None
    media: Optional["WidgetsCommentMedia"] = None
    post_source: Optional["WallPostSource"] = None
    post_type: Optional[int] = None
    reposts: Optional["BaseRepostsInfo"] = None
    text: Optional[str] = None
    to_id: Optional[int] = None
    user: Optional["UsersUserFull"] = None


class WidgetsWidgetLikes(BaseObject):
    """VK Object Widgets/WidgetsWidgetLikes

    count - Likes number
    """

    count: Optional[int] = None


class WidgetsWidgetPage(BaseObject):
    """VK Object Widgets/WidgetsWidgetPage

    date - Date when widgets on the page has been initialized firstly in Unixtime
    description - Page description
    id - Page ID
    page_id - page_id parameter value
    photo - URL of the preview image
    title - Page title
    url - Page absolute URL
    """

    comments: Optional["BaseObjectCount"] = None
    date: Optional[int] = None
    description: Optional[str] = None
    id: Optional[int] = None
    likes: Optional["BaseObjectCount"] = None
    page_id: Optional[str] = None
    photo: Optional[str] = None
    title: Optional[str] = None
    url: Optional[str] = None


class AccountUserSettings(UsersUserMin, UsersUserSettingsXtr):
    """VK Object Account/AccountUserSettings

    photo_200 - URL of square photo of the user with 200 pixels in width
    is_service_account - flag about service account
    """

    photo_200: Optional[str] = None
    is_service_account: Optional[bool] = None


class FriendsUserXtrPhone(UsersUserFull):
    """VK Object Friends/FriendsUserXtrPhone

    phone - User phone
    """

    phone: Optional[str] = None


class MessagesUserXtrInvitedBy(UsersUserXtrType):
    """VK Object Messages/MessagesUserXtrInvitedBy"""

    invited_by: Optional[int] = None


class FriendsUserXtrLists(UsersUserFull):
    """VK Object Friends/FriendsUserXtrLists"""

    lists: Optional[List[int]] = None


class GroupsUserXtrRole(UsersUserFull):
    """VK Object Groups/GroupsUserXtrRole"""

    role: Optional["GroupsRoleOptions"] = None


class NotificationsNotificationParent(
    WallWallpostToId,
    PhotosPhoto,
    BoardTopic,
    VideoVideo,
    NotificationsNotificationsComment,
):
    """VK Object Notifications/NotificationsNotificationParent"""


class NewsfeedNewsfeedPhoto(PhotosPhoto):
    """VK Object Newsfeed/NewsfeedNewsfeedPhoto

    can_repost - Information whether current user can repost the photo
    """

    likes: Optional["BaseLikes"] = None
    comments: Optional["BaseObjectCount"] = None
    can_repost: Optional["BaseBoolInt"] = None


class NewsfeedItemWallpost(WallCarouselBase, NewsfeedItemBase):
    """VK Object Newsfeed/NewsfeedItemWallpost

    is_favorite - Information whether the post in favorites list
    marked_as_ads - Information whether the post is marked as ads
    post_id - Post ID
    signer_id - Post signer ID
    text - Post text
    views - Count of views
    short_text_rate - Preview length control parameter
    """

    activity: Optional["NewsfeedEventActivity"] = None
    attachments: Optional[List["WallWallpostAttachment"]] = None
    comments: Optional["BaseCommentsInfo"] = None
    copy_history: Optional[List["WallWallpost"]] = None
    feedback: Optional["NewsfeedItemWallpostFeedback"] = None
    geo: Optional["BaseGeo"] = None
    is_favorite: Optional[bool] = None
    likes: Optional["BaseLikesInfo"] = None
    marked_as_ads: Optional["BaseBoolInt"] = None
    post_id: Optional[int] = None
    post_source: Optional["WallPostSource"] = None
    post_type: Optional["NewsfeedItemWallpostType"] = None
    reposts: Optional["BaseRepostsInfo"] = None
    signer_id: Optional[int] = None
    text: Optional[str] = None
    views: Optional["WallViews"] = None
    short_text_rate: Optional[float] = None


class NewsfeedItemVideo(WallCarouselBase, NewsfeedItemBase):
    """VK Object Newsfeed/NewsfeedItemVideo"""

    video: Optional["NewsfeedItemVideoVideo"] = None


class NewsfeedItemPhotoTag(WallCarouselBase, NewsfeedItemBase):
    """VK Object Newsfeed/NewsfeedItemPhotoTag

    post_id - Post ID
    """

    photo_tags: Optional["NewsfeedItemPhotoTagPhotoTags"] = None
    post_id: Optional[int] = None


class NewsfeedItemPhoto(WallCarouselBase, NewsfeedItemBase):
    """VK Object Newsfeed/NewsfeedItemPhoto

    post_id - Post ID
    """

    photos: Optional["NewsfeedItemPhotoPhotos"] = None
    post_id: Optional[int] = None


class NewsfeedItemAudio(NewsfeedItemBase):
    """VK Object Newsfeed/NewsfeedItemAudio

    post_id - Post ID
    """

    audio: Optional["NewsfeedItemAudioAudio"] = None
    post_id: Optional[int] = None


class GroupsBannedItem(GroupsOwnerXtrBanInfo):
    """VK Object Groups/GroupsBannedItem
    #FIXME Comment is undefined
    """


class ClientInfoButtonActions(enum.Enum):
    TEXT = "text"
    VKPAY = "vkpay"
    OPEN_APP = "open_app"
    LOCATION = "location"
    OPEN_LINK = "open_link"
    OPEN_PHOTO = "open_photo"
    CALLBACK = "callback"


class MessagesClientInfo(BaseObject):
    button_actions: Optional[List[ClientInfoButtonActions]] = None
    keyboard: Optional[bool] = None
    inline_keyboard: Optional[bool] = None
    carousel: Optional[bool] = None
    lang_id: Optional[int] = None


class ObjectType(enum.Enum):
    VIDEO = "video"
    PHOTO = "photo"
    COMMENT = "comment"
    NOTE = "note"
    TOPIC_COMMENT = "topic_comment"
    PHOTO_COMMENT = "photo_comment"
    VIDEO_COMMENT = "video_comment"
    MARKET = "market"
    MARKET_COMMENT = "market_comment"


AccountAccountCounters.update_forward_refs()
AccountInfo.update_forward_refs()
AccountNameRequest.update_forward_refs()
AccountOffer.update_forward_refs()
AccountPushConversations.update_forward_refs()
AccountPushConversationsItem.update_forward_refs()
AccountPushParams.update_forward_refs()
AccountPushSettings.update_forward_refs()
AccountUserSettingsInterest.update_forward_refs()
AccountUserSettingsInterests.update_forward_refs()
AdsAccesses.update_forward_refs()
AdsAccount.update_forward_refs()
AdsAd.update_forward_refs()
AdsAdLayout.update_forward_refs()
AdsCampaign.update_forward_refs()
AdsCategory.update_forward_refs()
AdsClient.update_forward_refs()
AdsCriteria.update_forward_refs()
AdsDemoStats.update_forward_refs()
AdsDemostatsFormat.update_forward_refs()
AdsFloodStats.update_forward_refs()
AdsLinkStatus.update_forward_refs()
AdsLookalikeRequest.update_forward_refs()
AdsLookalikeRequestSaveAudienceLevel.update_forward_refs()
AdsMusician.update_forward_refs()
AdsParagraphs.update_forward_refs()
AdsPromotedPostReach.update_forward_refs()
AdsRejectReason.update_forward_refs()
AdsRules.update_forward_refs()
AdsStats.update_forward_refs()
AdsStatsAge.update_forward_refs()
AdsStatsCities.update_forward_refs()
AdsStatsFormat.update_forward_refs()
AdsStatsSex.update_forward_refs()
AdsStatsSexAge.update_forward_refs()
AdsStatsViewsTimes.update_forward_refs()
AdsTargStats.update_forward_refs()
AdsTargSuggestions.update_forward_refs()
AdsTargSuggestionsCities.update_forward_refs()
AdsTargSuggestionsRegions.update_forward_refs()
AdsTargSuggestionsSchools.update_forward_refs()
AdsTargetGroup.update_forward_refs()
AdsUsers.update_forward_refs()
AppsAppMin.update_forward_refs()
AppsLeaderboard.update_forward_refs()
AppsScope.update_forward_refs()
AudioAudio.update_forward_refs()
BaseCity.update_forward_refs()
BaseCommentsInfo.update_forward_refs()
BaseCountry.update_forward_refs()
BaseCropPhoto.update_forward_refs()
BaseCropPhotoCrop.update_forward_refs()
BaseCropPhotoRect.update_forward_refs()
BaseError.update_forward_refs()
BaseGeo.update_forward_refs()
BaseGeoCoordinates.update_forward_refs()
BaseGradientPoint.update_forward_refs()
BaseImage.update_forward_refs()
BaseLikes.update_forward_refs()
BaseLikesInfo.update_forward_refs()
BaseLink.update_forward_refs()
BaseLinkApplication.update_forward_refs()
BaseLinkApplicationStore.update_forward_refs()
BaseLinkButton.update_forward_refs()
BaseLinkButtonAction.update_forward_refs()
BaseLinkProduct.update_forward_refs()
BaseLinkRating.update_forward_refs()
BaseMessageError.update_forward_refs()
BaseObject.update_forward_refs()
BaseObjectCount.update_forward_refs()
BaseObjectWithName.update_forward_refs()
BasePlace.update_forward_refs()
BaseRepostsInfo.update_forward_refs()
BaseRequestParam.update_forward_refs()
BaseSticker.update_forward_refs()
BaseStickerAnimation.update_forward_refs()
BaseUploadServer.update_forward_refs()
BaseUserId.update_forward_refs()
BoardTopic.update_forward_refs()
BoardTopicComment.update_forward_refs()
BoardTopicPoll.update_forward_refs()
CallbackBoardPostDelete.update_forward_refs()
CallbackConfirmationMessage.update_forward_refs()
CallbackGroupChangePhoto.update_forward_refs()
CallbackGroupChangeSettings.update_forward_refs()
CallbackGroupJoin.update_forward_refs()
CallbackGroupLeave.update_forward_refs()
CallbackGroupOfficersEdit.update_forward_refs()
CallbackGroupSettingsChanges.update_forward_refs()
CallbackLikeAddRemove.update_forward_refs()
CallbackMarketComment.update_forward_refs()
CallbackMarketCommentDelete.update_forward_refs()
CallbackMessageAllow.update_forward_refs()
CallbackMessageBase.update_forward_refs()
CallbackMessageDeny.update_forward_refs()
CallbackPhotoComment.update_forward_refs()
CallbackPhotoCommentDelete.update_forward_refs()
CallbackPollVoteNew.update_forward_refs()
CallbackQrScan.update_forward_refs()
CallbackUserBlock.update_forward_refs()
CallbackUserUnblock.update_forward_refs()
CallbackVideoComment.update_forward_refs()
CallbackVideoCommentDelete.update_forward_refs()
CallbackWallCommentDelete.update_forward_refs()
CommentThread.update_forward_refs()
DatabaseCity.update_forward_refs()
DatabaseFaculty.update_forward_refs()
DatabaseRegion.update_forward_refs()
DatabaseSchool.update_forward_refs()
DatabaseStation.update_forward_refs()
DatabaseUniversity.update_forward_refs()
DocsDoc.update_forward_refs()
DocsDocPreview.update_forward_refs()
DocsDocPreviewAudioMsg.update_forward_refs()
DocsDocPreviewGraffiti.update_forward_refs()
DocsDocPreviewPhoto.update_forward_refs()
DocsDocPreviewPhotoSizes.update_forward_refs()
DocsDocPreviewVideo.update_forward_refs()
DocsDocTypes.update_forward_refs()
DocsDocUploadResponse.update_forward_refs()
EventsEventAttach.update_forward_refs()
FaveBookmark.update_forward_refs()
FavePage.update_forward_refs()
FaveTag.update_forward_refs()
FriendsFriendStatus.update_forward_refs()
FriendsFriendsList.update_forward_refs()
FriendsMutualFriend.update_forward_refs()
FriendsRequests.update_forward_refs()
FriendsRequestsMutual.update_forward_refs()
FriendsRequestsXtrMessage.update_forward_refs()
GiftsGift.update_forward_refs()
GiftsLayout.update_forward_refs()
GroupsAddress.update_forward_refs()
GroupsAddressTimetable.update_forward_refs()
GroupsAddressTimetableDay.update_forward_refs()
GroupsAddressesInfo.update_forward_refs()
GroupsBanInfo.update_forward_refs()
GroupsCallbackServer.update_forward_refs()
GroupsCallbackSettings.update_forward_refs()
GroupsContactsItem.update_forward_refs()
GroupsCountersGroup.update_forward_refs()
GroupsCover.update_forward_refs()
GroupsGroup.update_forward_refs()
GroupsGroupAttach.update_forward_refs()
GroupsGroupBanInfo.update_forward_refs()
GroupsGroupCategory.update_forward_refs()
GroupsGroupCategoryFull.update_forward_refs()
GroupsGroupCategoryType.update_forward_refs()
GroupsGroupLink.update_forward_refs()
GroupsGroupPublicCategoryList.update_forward_refs()
GroupsGroupXtrInvitedBy.update_forward_refs()
GroupsGroupsArray.update_forward_refs()
GroupsLinksItem.update_forward_refs()
GroupsLiveCovers.update_forward_refs()
GroupsLongPollEvents.update_forward_refs()
GroupsLongPollServer.update_forward_refs()
GroupsLongPollSettings.update_forward_refs()
GroupsMarketInfo.update_forward_refs()
GroupsMemberRole.update_forward_refs()
GroupsMemberStatus.update_forward_refs()
GroupsMemberStatusFull.update_forward_refs()
GroupsOnlineStatus.update_forward_refs()
GroupsOwnerXtrBanInfo.update_forward_refs()
GroupsSettingsTwitter.update_forward_refs()
GroupsSubjectItem.update_forward_refs()
GroupsTokenPermissionSetting.update_forward_refs()
LeadsChecked.update_forward_refs()
LeadsComplete.update_forward_refs()
LeadsEntry.update_forward_refs()
LeadsLead.update_forward_refs()
LeadsLeadDays.update_forward_refs()
LeadsStart.update_forward_refs()
LinkTargetObject.update_forward_refs()
MarketCurrency.update_forward_refs()
MarketMarketAlbum.update_forward_refs()
MarketMarketCategory.update_forward_refs()
MarketMarketItem.update_forward_refs()
MarketPrice.update_forward_refs()
MarketSection.update_forward_refs()
MediaRestriction.update_forward_refs()
MessageChatPreview.update_forward_refs()
MessagesAudioMessage.update_forward_refs()
MessagesChat.update_forward_refs()
MessagesChatFull.update_forward_refs()
MessagesChatPushSettings.update_forward_refs()
MessagesChatRestrictions.update_forward_refs()
MessagesConversation.update_forward_refs()
MessagesConversationMember.update_forward_refs()
MessagesConversationPeer.update_forward_refs()
MessagesConversationWithMessage.update_forward_refs()
MessagesForeignMessage.update_forward_refs()
MessagesGraffiti.update_forward_refs()
MessagesHistoryAttachment.update_forward_refs()
MessagesHistoryMessageAttachment.update_forward_refs()
MessagesKeyboard.update_forward_refs()
MessagesKeyboardButton.update_forward_refs()
MessagesKeyboardButtonAction.update_forward_refs()
MessagesLastActivity.update_forward_refs()
MessagesLongpollMessages.update_forward_refs()
MessagesLongpollParams.update_forward_refs()
MessagesMessage.update_forward_refs()
MessagesMessageAction.update_forward_refs()
MessagesMessageActionPhoto.update_forward_refs()
MessagesMessageAttachment.update_forward_refs()
MessagesMessageRequestData.update_forward_refs()
MessagesPinnedMessage.update_forward_refs()
NewsfeedEventActivity.update_forward_refs()
NewsfeedItemAudioAudio.update_forward_refs()
NewsfeedItemBase.update_forward_refs()
NewsfeedItemFriendFriends.update_forward_refs()
NewsfeedItemHolidayRecommendationsBlockHeader.update_forward_refs()
NewsfeedItemNoteNotes.update_forward_refs()
NewsfeedItemPhotoPhotos.update_forward_refs()
NewsfeedItemPhotoTagPhotoTags.update_forward_refs()
NewsfeedItemPromoButtonAction.update_forward_refs()
NewsfeedItemPromoButtonImage.update_forward_refs()
NewsfeedItemVideoVideo.update_forward_refs()
NewsfeedItemWallpostFeedback.update_forward_refs()
NewsfeedItemWallpostFeedbackAnswer.update_forward_refs()
NewsfeedList.update_forward_refs()
NewsfeedNewsfeedItem.update_forward_refs()
NewsfeedNewsfeedNote.update_forward_refs()
NotesNote.update_forward_refs()
NotesNoteComment.update_forward_refs()
NotificationsFeedback.update_forward_refs()
NotificationsNotification.update_forward_refs()
NotificationsNotificationItem.update_forward_refs()
NotificationsNotificationsComment.update_forward_refs()
NotificationsReply.update_forward_refs()
NotificationsSendMessageError.update_forward_refs()
NotificationsSendMessageItem.update_forward_refs()
OauthError.update_forward_refs()
OrdersAmount.update_forward_refs()
OrdersAmountItem.update_forward_refs()
OrdersOrder.update_forward_refs()
OrdersSubscription.update_forward_refs()
OwnerState.update_forward_refs()
PagesWikipage.update_forward_refs()
PagesWikipageFull.update_forward_refs()
PagesWikipageHistory.update_forward_refs()
PhotosCommentXtrPid.update_forward_refs()
PhotosImage.update_forward_refs()
PhotosMarketAlbumUploadResponse.update_forward_refs()
PhotosMarketUploadResponse.update_forward_refs()
PhotosMessageUploadResponse.update_forward_refs()
PhotosOwnerUploadResponse.update_forward_refs()
PhotosPhoto.update_forward_refs()
PhotosPhotoAlbum.update_forward_refs()
PhotosPhotoAlbumFull.update_forward_refs()
PhotosPhotoFull.update_forward_refs()
PhotosPhotoFullXtrRealOffset.update_forward_refs()
PhotosPhotoSizes.update_forward_refs()
PhotosPhotoTag.update_forward_refs()
PhotosPhotoUpload.update_forward_refs()
PhotosPhotoUploadResponse.update_forward_refs()
PhotosPhotoXtrRealOffset.update_forward_refs()
PhotosPhotoXtrTagInfo.update_forward_refs()
PhotosTagsSuggestionItem.update_forward_refs()
PhotosTagsSuggestionItemButton.update_forward_refs()
PhotosWallUploadResponse.update_forward_refs()
PollsAnswer.update_forward_refs()
PollsBackground.update_forward_refs()
PollsFriend.update_forward_refs()
PollsPoll.update_forward_refs()
PollsVoters.update_forward_refs()
PollsVotersUsers.update_forward_refs()
PrettyCardsPrettyCard.update_forward_refs()
SearchHint.update_forward_refs()
SecureLevel.update_forward_refs()
SecureSmsNotification.update_forward_refs()
SecureTokenChecked.update_forward_refs()
SecureTransaction.update_forward_refs()
StatsActivity.update_forward_refs()
StatsCity.update_forward_refs()
StatsCountry.update_forward_refs()
StatsPeriod.update_forward_refs()
StatsReach.update_forward_refs()
StatsSexAge.update_forward_refs()
StatsViews.update_forward_refs()
StatsWallpostStat.update_forward_refs()
StatusStatus.update_forward_refs()
StorageValue.update_forward_refs()
StoriesClickableArea.update_forward_refs()
StoriesClickableSticker.update_forward_refs()
StoriesClickableStickers.update_forward_refs()
StoriesFeedItem.update_forward_refs()
StoriesPromoBlock.update_forward_refs()
StoriesReplies.update_forward_refs()
StoriesStatLine.update_forward_refs()
StoriesStory.update_forward_refs()
StoriesStoryLink.update_forward_refs()
StoriesStoryStats.update_forward_refs()
StoriesStoryStatsStat.update_forward_refs()
StoriesViewersItem.update_forward_refs()
UsersCareer.update_forward_refs()
UsersExports.update_forward_refs()
UsersLastSeen.update_forward_refs()
UsersMilitary.update_forward_refs()
UsersOccupation.update_forward_refs()
UsersOnlineInfo.update_forward_refs()
UsersPersonal.update_forward_refs()
UsersRelative.update_forward_refs()
UsersSchool.update_forward_refs()
UsersSubscriptionsItem.update_forward_refs()
UsersUniversity.update_forward_refs()
UsersUserConnections.update_forward_refs()
UsersUserCounters.update_forward_refs()
UsersUserMin.update_forward_refs()
UsersUserSettingsXtr.update_forward_refs()
UsersUsersArray.update_forward_refs()
UtilsDomainResolved.update_forward_refs()
UtilsLastShortenedLink.update_forward_refs()
UtilsLinkChecked.update_forward_refs()
UtilsLinkStats.update_forward_refs()
UtilsLinkStatsExtended.update_forward_refs()
UtilsShortLink.update_forward_refs()
UtilsStats.update_forward_refs()
UtilsStatsCity.update_forward_refs()
UtilsStatsCountry.update_forward_refs()
UtilsStatsExtended.update_forward_refs()
UtilsStatsSexAge.update_forward_refs()
VideoLiveSettings.update_forward_refs()
VideoRestrictionButton.update_forward_refs()
VideoSaveResult.update_forward_refs()
VideoVideoAlbumFull.update_forward_refs()
VideoVideoFiles.update_forward_refs()
WallAppPost.update_forward_refs()
WallAttachedNote.update_forward_refs()
WallCarouselBase.update_forward_refs()
WallCommentAttachment.update_forward_refs()
WallGeo.update_forward_refs()
WallGraffiti.update_forward_refs()
WallPostCopyright.update_forward_refs()
WallPostSource.update_forward_refs()
WallPostedPhoto.update_forward_refs()
WallViews.update_forward_refs()
WallWallComment.update_forward_refs()
WallWallpost.update_forward_refs()
WallWallpostAttachment.update_forward_refs()
WallWallpostToId.update_forward_refs()
WidgetsCommentMedia.update_forward_refs()
WidgetsCommentReplies.update_forward_refs()
WidgetsCommentRepliesItem.update_forward_refs()
WidgetsWidgetComment.update_forward_refs()
WidgetsWidgetLikes.update_forward_refs()
WidgetsWidgetPage.update_forward_refs()

AdsTargSettings.update_forward_refs()
AppsApp.update_forward_refs()
FriendsFriendExtendedStatus.update_forward_refs()
GroupsGroupFull.update_forward_refs()
MarketMarketItemFull.update_forward_refs()
NewsfeedItemDigest.update_forward_refs()
NewsfeedItemFriend.update_forward_refs()
NewsfeedItemNote.update_forward_refs()
NewsfeedItemPromoButton.update_forward_refs()
NewsfeedItemTopic.update_forward_refs()
NewsfeedListFull.update_forward_refs()
UsersUser.update_forward_refs()
UsersUserFull.update_forward_refs()
UsersUserXtrCounters.update_forward_refs()
UsersUserXtrType.update_forward_refs()
VideoVideoFull.update_forward_refs()
VideoVideoImage.update_forward_refs()
WallWallpostFull.update_forward_refs()
AccountUserSettings.update_forward_refs()
FriendsUserXtrPhone.update_forward_refs()
MessagesUserXtrInvitedBy.update_forward_refs()
FriendsUserXtrLists.update_forward_refs()
GroupsUserXtrRole.update_forward_refs()
NewsfeedNewsfeedPhoto.update_forward_refs()
NewsfeedItemWallpost.update_forward_refs()
NewsfeedItemVideo.update_forward_refs()
NewsfeedItemPhotoTag.update_forward_refs()
NewsfeedItemPhoto.update_forward_refs()
NewsfeedItemAudio.update_forward_refs()
GroupsBannedItem.update_forward_refs()
MessagesClientInfo.update_forward_refs()
MarketOrder.update_forward_refs()
