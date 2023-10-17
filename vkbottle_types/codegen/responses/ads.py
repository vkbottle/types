import typing
from vkbottle_types.responses.base_response import BaseResponse, BaseModel
from vkbottle_types.base_model import Field

from vkbottle_types.objects import (
    AdsLookalikeRequestSaveAudienceLevel,
    WallWallpostAttachment,
    AdsAdApproved,
    AdsTargSuggestionsSchoolsType,
    AdsClipItem,
    AdsPostEasyPromote,
    AdsPostLikes,
    AdsCriteriaSex,
    AdsClipItemLink,
    AdsStatsAge,
    AdsStoryItemLink,
    AdsStatsSexValue,
    AdsFloodStatsByUserItem,
    AdsTargetGroupTargetPixelRule,
    AdsStoryItem,
    BaseBoolInt,
    AdsStatsSexAge,
    AdsStatsCities,
    AdsAccessRole,
    AdsDemostatsFormat,
    AdsPostOwner,
    AdsAccessRolePublic,
    AdsStoryItemStatsFollow,
    AdsCategory,
    AdsPostComments,
    AdsPost,
    AdsStoriesOwner,
    AdsStatsSex,
    AdsStories,
    AdsEventsRetargetingGroup,
    AdsOrdSubagent,
    AdsAccesses,
    AdsAdCostType,
    AdsRulesHelpUrl,
    AdsStatsFormat,
    AdsOrdClientType,
    AdsPostDonut,
    AdsAdStatus,
    AdsPostReposts,
    AdsOrdData,
    AdsMobileStatItem,
    AdsCampaignStatus,
    AdsStoryItemStatsUrlView,
    AdsObjectType,
    AdsStoryItemStats,
    AdsPostViews,
    AdsRules,
    BaseError,
    AdsAccountType,
    AdsCampaignType,
    AdsStatsViewsTimes,
)


class AdsAccessRoleResponseModel(enum.Enum):
    ADMIN = "admin"

    MANAGER = "manager"

    REPORTS = "reports"


class AdsAccessRoleResponse(BaseResponse):
    response: "AdsAccessRoleResponseModel"


class AdsAccessRolePublicResponseModel(enum.Enum):
    MANAGER = "manager"

    REPORTS = "reports"


class AdsAccessRolePublicResponse(BaseResponse):
    response: "AdsAccessRolePublicResponseModel"


class AdsAccessesResponseModel(BaseModel):
    client_id: typing.Optional[str] = Field(
        default=None,
        description="Client ID",
    )

    role: typing.Optional["AdsAccessRole"] = Field(
        default=None,
    )


class AdsAccessesResponse(BaseResponse):
    response: "AdsAccessesResponseModel"


class AdsAccountResponseModel(BaseModel):
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


class AdsAccountResponse(BaseResponse):
    response: "AdsAccountResponseModel"


class AdsAccountTypeResponseModel(enum.Enum):
    GENERAL = "general"

    AGENCY = "agency"


class AdsAccountTypeResponse(BaseResponse):
    response: "AdsAccountTypeResponseModel"


class AdsAdResponseModel(BaseModel):
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
        typing.List[AdsEventsRetargetingGroup]
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


class AdsAdResponse(BaseResponse):
    response: "AdsAdResponseModel"


class AdsAdApprovedResponseModel(enum.IntEnum):
    NOT_MODERATED = 0

    PENDING_MODERATION = 1

    APPROVED = 2

    REJECTED = 3


class AdsAdApprovedResponse(BaseResponse):
    response: "AdsAdApprovedResponseModel"


class AdsAdCostTypeResponseModel(enum.IntEnum):
    PER_CLICKS = 0

    PER_IMPRESSIONS = 1

    PER_ACTIONS = 2

    PER_IMPRESSIONS_OPTIMIZED = 3


class AdsAdCostTypeResponse(BaseResponse):
    response: "AdsAdCostTypeResponseModel"


class AdsAdLayoutResponseModel(BaseModel):
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

    clips_list: typing.Optional[typing.List[AdsClipItem]] = Field(
        default=None,
    )


class AdsAdLayoutResponse(BaseResponse):
    response: "AdsAdLayoutResponseModel"


class AdsAdStatusResponseModel(enum.IntEnum):
    STOPPED = 0

    STARTED = 1

    DELETED = 2


class AdsAdStatusResponse(BaseResponse):
    response: "AdsAdStatusResponseModel"


class AdsCampaignResponseModel(BaseModel):
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


class AdsCampaignResponse(BaseResponse):
    response: "AdsCampaignResponseModel"


class AdsCampaignStatusResponseModel(enum.IntEnum):
    STOPPED = 0

    STARTED = 1

    DELETED = 2


class AdsCampaignStatusResponse(BaseResponse):
    response: "AdsCampaignStatusResponseModel"


class AdsCampaignTypeResponseModel(enum.Enum):
    NORMAL = "normal"

    VK_APPS_MANAGED = "vk_apps_managed"

    MOBILE_APPS = "mobile_apps"

    PROMOTED_POSTS = "promoted_posts"

    ADAPTIVE_ADS = "adaptive_ads"

    STORIES = "stories"


class AdsCampaignTypeResponse(BaseResponse):
    response: "AdsCampaignTypeResponseModel"


class AdsCategoryResponseModel(BaseModel):
    id: int = Field(
        description="Category ID",
    )

    name: str = Field(
        description="Category name",
    )

    subcategories: typing.Optional[typing.List[AdsCategory]] = Field(
        default=None,
    )


class AdsCategoryResponse(BaseResponse):
    response: "AdsCategoryResponseModel"


class AdsClientResponseModel(BaseModel):
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


class AdsClientResponse(BaseResponse):
    response: "AdsClientResponseModel"


class AdsClipItemResponseModel(BaseModel):
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


class AdsClipItemResponse(BaseResponse):
    response: "AdsClipItemResponseModel"


class AdsClipItemLinkResponseModel(BaseModel):
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


class AdsClipItemLinkResponse(BaseResponse):
    response: "AdsClipItemLinkResponseModel"


class AdsCreateAdStatusResponseModel(BaseModel):
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


class AdsCreateAdStatusResponse(BaseResponse):
    response: "AdsCreateAdStatusResponseModel"


class AdsCreateCampaignStatusResponseModel(BaseModel):
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


class AdsCreateCampaignStatusResponse(BaseResponse):
    response: "AdsCreateCampaignStatusResponseModel"


class AdsCreateClientsStatusResponseModel(BaseModel):
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


class AdsCreateClientsStatusResponse(BaseResponse):
    response: "AdsCreateClientsStatusResponseModel"


class AdsCriteriaResponseModel(BaseModel):
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


class AdsCriteriaResponse(BaseResponse):
    response: "AdsCriteriaResponseModel"


class AdsCriteriaSexResponseModel(enum.Enum):
    _0 = "0"

    _1 = "1"

    _2 = "2"


class AdsCriteriaSexResponse(BaseResponse):
    response: "AdsCriteriaSexResponseModel"


class AdsDemoStatsResponseModel(BaseModel):
    id: typing.Optional[int] = Field(
        default=None,
        description="Object ID",
    )

    stats: typing.Optional[typing.List[AdsDemostatsFormat]] = Field(
        default=None,
    )

    type: typing.Optional["AdsObjectType"] = Field(
        default=None,
    )


class AdsDemoStatsResponse(BaseResponse):
    response: "AdsDemoStatsResponseModel"


class AdsDemographicStatsPeriodItemBaseResponseModel(BaseModel):
    clicks_rate: typing.Optional[float] = Field(
        default=None,
        description="Clicks rate",
    )

    impressions_rate: typing.Optional[float] = Field(
        default=None,
        description="Impressions rate",
    )


class AdsDemographicStatsPeriodItemBaseResponse(BaseResponse):
    response: "AdsDemographicStatsPeriodItemBaseResponseModel"


class AdsDemostatsFormatResponseModel(BaseModel):
    age: typing.Optional[typing.List[AdsStatsAge]] = Field(
        default=None,
    )

    cities: typing.Optional[typing.List[AdsStatsCities]] = Field(
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

    sex: typing.Optional[typing.List[AdsStatsSex]] = Field(
        default=None,
    )

    sex_age: typing.Optional[typing.List[AdsStatsSexAge]] = Field(
        default=None,
    )


class AdsDemostatsFormatResponse(BaseResponse):
    response: "AdsDemostatsFormatResponseModel"


class AdsEventsRetargetingGroupResponseModel(BaseModel):
    id: typing.Optional[int] = Field(
        default=None,
    )

    value: typing.Optional[typing.List[int]] = Field(
        default=None,
    )


class AdsEventsRetargetingGroupResponse(BaseResponse):
    response: "AdsEventsRetargetingGroupResponseModel"


class AdsFloodStatsResponseModel(BaseModel):
    left: int = Field(
        description="Requests left",
    )

    refresh: int = Field(
        description="Time to refresh in seconds",
    )

    stats_by_user: typing.Optional[typing.List[AdsFloodStatsByUserItem]] = Field(
        default=None,
        description="Used requests per user",
    )


class AdsFloodStatsResponse(BaseResponse):
    response: "AdsFloodStatsResponseModel"


class AdsFloodStatsByUserItemResponseModel(BaseModel):
    user_id: int = Field(
        description="User ID",
    )

    requests_count: int = Field(
        description="Used requests",
    )


class AdsFloodStatsByUserItemResponse(BaseResponse):
    response: "AdsFloodStatsByUserItemResponseModel"


class AdsLinkStatusResponseModel(BaseModel):
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


class AdsLinkStatusResponse(BaseResponse):
    response: "AdsLinkStatusResponseModel"


class AdsLookalikeRequestResponseModel(BaseModel):
    id: int = Field(
        description="Lookalike request ID",
    )

    create_time: int = Field(
        description="Lookalike request create time, as Unixtime",
    )

    update_time: int = Field(
        description="Lookalike request update time, as Unixtime",
    )

    status: typing.Literal[
        "search_in_progress",
        "search_failed",
        "search_done",
        "save_in_progress",
        "save_failed",
        "save_done",
    ] = Field(
        description="Lookalike request status",
    )

    source_type: typing.Literal["retargeting_group"] = Field(
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
        typing.List[AdsLookalikeRequestSaveAudienceLevel]
    ] = Field(
        default=None,
    )


class AdsLookalikeRequestResponse(BaseResponse):
    response: "AdsLookalikeRequestResponseModel"


class AdsLookalikeRequestSaveAudienceLevelResponseModel(BaseModel):
    level: typing.Optional[int] = Field(
        default=None,
        description="Save audience level id, which is used in save audience queries",
    )

    audience_count: typing.Optional[int] = Field(
        default=None,
        description="Saved audience audience size for according level",
    )


class AdsLookalikeRequestSaveAudienceLevelResponse(BaseResponse):
    response: "AdsLookalikeRequestSaveAudienceLevelResponseModel"


class AdsMobileStatItemResponseModel(BaseModel):
    key: typing.Optional[str] = Field(
        default=None,
    )

    value: typing.Optional[float] = Field(
        default=None,
    )


class AdsMobileStatItemResponse(BaseResponse):
    response: "AdsMobileStatItemResponseModel"


class AdsMusicianResponseModel(BaseModel):
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


class AdsMusicianResponse(BaseResponse):
    response: "AdsMusicianResponseModel"


class AdsObjectTypeResponseModel(enum.Enum):
    AD = "ad"

    CAMPAIGN = "campaign"

    CLIENT = "client"

    OFFICE = "office"


class AdsObjectTypeResponse(BaseResponse):
    response: "AdsObjectTypeResponseModel"


class AdsOrdClientTypeResponseModel(enum.Enum):
    PERSON = "person"

    INDIVIDUAL = "individual"

    LEGAL = "legal"

    FOREIGN = "foreign"

    UNKNOWN = "unknown"


class AdsOrdClientTypeResponse(BaseResponse):
    response: "AdsOrdClientTypeResponseModel"


class AdsOrdDataResponseModel(BaseModel):
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


class AdsOrdDataResponse(BaseResponse):
    response: "AdsOrdDataResponseModel"


class AdsOrdSubagentResponseModel(BaseModel):
    type: "AdsOrdClientType" = Field()

    name: str = Field()

    phone: str = Field()

    inn: typing.Optional[str] = Field(
        default=None,
    )


class AdsOrdSubagentResponse(BaseResponse):
    response: "AdsOrdSubagentResponseModel"


class AdsPostResponseModel(BaseModel):
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

    attachments: typing.Optional[typing.List[WallWallpostAttachment]] = Field(
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


class AdsPostResponse(BaseResponse):
    response: "AdsPostResponseModel"


class AdsPostCommentsResponseModel(BaseModel):
    count: typing.Optional[int] = Field(
        default=None,
        description="Count",
    )


class AdsPostCommentsResponse(BaseResponse):
    response: "AdsPostCommentsResponseModel"


class AdsPostDonutResponseModel(BaseModel):
    is_donut: typing.Optional[bool] = Field(
        default=None,
        description="Is donut",
    )


class AdsPostDonutResponse(BaseResponse):
    response: "AdsPostDonutResponseModel"


class AdsPostEasyPromoteResponseModel(BaseModel):
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


class AdsPostEasyPromoteResponse(BaseResponse):
    response: "AdsPostEasyPromoteResponseModel"


class AdsPostLikesResponseModel(BaseModel):
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


class AdsPostLikesResponse(BaseResponse):
    response: "AdsPostLikesResponseModel"


class AdsPostOwnerResponseModel(BaseModel):
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


class AdsPostOwnerResponse(BaseResponse):
    response: "AdsPostOwnerResponseModel"


class AdsPostRepostsResponseModel(BaseModel):
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


class AdsPostRepostsResponse(BaseResponse):
    response: "AdsPostRepostsResponseModel"


class AdsPostViewsResponseModel(BaseModel):
    count: typing.Optional[int] = Field(
        default=None,
        description="Count",
    )


class AdsPostViewsResponse(BaseResponse):
    response: "AdsPostViewsResponseModel"


class AdsPromotedPostReachResponseModel(BaseModel):
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


class AdsPromotedPostReachResponse(BaseResponse):
    response: "AdsPromotedPostReachResponseModel"


class AdsRejectReasonResponseModel(BaseModel):
    comment: typing.Optional[str] = Field(
        default=None,
        description="Comment text",
    )

    rules: typing.Optional[typing.List[AdsRules]] = Field(
        default=None,
    )


class AdsRejectReasonResponse(BaseResponse):
    response: "AdsRejectReasonResponseModel"


class AdsRulesResponseModel(BaseModel):
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


class AdsRulesResponse(BaseResponse):
    response: "AdsRulesResponseModel"


class AdsRulesHelpUrlResponseModel(BaseModel):
    pass


class AdsRulesHelpUrlResponse(BaseResponse):
    response: "AdsRulesHelpUrlResponseModel"


class AdsStatisticClickActionResponseModel(BaseModel):
    type: typing.Optional[
        typing.Literal[
            "load",
            "impression",
            "click_deeplink",
            "click",
            "click_post_owner",
            "click_post_link",
            "click_pretty_card",
            "like_post",
            "share_post",
            "video_start",
            "video_pause",
            "video_resume",
            "video_play_3s",
            "video_play_10s",
            "video_play_25",
            "video_play_50",
            "video_play_75",
            "video_play_95",
            "video_play_100",
            "video_volume_on",
            "video_volume_off",
            "video_fullscreen_on",
            "video_fullscreen_off",
            "hide",
        ]
    ] = Field(
        default=None,
    )

    url: typing.Optional[str] = Field(
        default=None,
    )


class AdsStatisticClickActionResponse(BaseResponse):
    response: "AdsStatisticClickActionResponseModel"


class AdsStatsResponseModel(BaseModel):
    id: typing.Optional[int] = Field(
        default=None,
        description="Object ID",
    )

    stats: typing.Optional[typing.List[AdsStatsFormat]] = Field(
        default=None,
    )

    type: typing.Optional["AdsObjectType"] = Field(
        default=None,
    )

    views_times: typing.Optional["AdsStatsViewsTimes"] = Field(
        default=None,
    )


class AdsStatsResponse(BaseResponse):
    response: "AdsStatsResponseModel"


class AdsStatsAgeResponseModel(AdsDemographicStatsPeriodItemBase):
    value: typing.Optional[str] = Field(
        default=None,
        description="Age interval",
    )


class AdsStatsAgeResponse(BaseResponse):
    response: "AdsStatsAgeResponseModel"


class AdsStatsCitiesResponseModel(AdsDemographicStatsPeriodItemBase):
    name: typing.Optional[str] = Field(
        default=None,
        description="City name",
    )

    value: typing.Optional[typing.Union["int", "str"]] = Field(
        default=None,
        description="City ID",
    )


class AdsStatsCitiesResponse(BaseResponse):
    response: "AdsStatsCitiesResponseModel"


class AdsStatsFormatResponseModel(BaseModel):
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

    mobile_app_stat: typing.Optional[typing.List[AdsMobileStatItem]] = Field(
        default=None,
        description="Mobile app stat",
    )


class AdsStatsFormatResponse(BaseResponse):
    response: "AdsStatsFormatResponseModel"


class AdsStatsSexResponseModel(AdsDemographicStatsPeriodItemBase):
    value: typing.Optional["AdsStatsSexValue"] = Field(
        default=None,
    )


class AdsStatsSexResponse(BaseResponse):
    response: "AdsStatsSexResponseModel"


class AdsStatsSexAgeResponseModel(AdsDemographicStatsPeriodItemBase):
    value: typing.Optional[str] = Field(
        default=None,
        description="Sex and age interval",
    )


class AdsStatsSexAgeResponse(BaseResponse):
    response: "AdsStatsSexAgeResponseModel"


class AdsStatsSexValueResponseModel(enum.Enum):
    F = "f"

    M = "m"


class AdsStatsSexValueResponse(BaseResponse):
    response: "AdsStatsSexValueResponseModel"


class AdsStatsViewsTimesResponseModel(BaseModel):
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


class AdsStatsViewsTimesResponse(BaseResponse):
    response: "AdsStatsViewsTimesResponseModel"


class AdsStoriesResponseModel(BaseModel):
    stories: typing.Optional[typing.List[AdsStoryItem]] = Field(
        default=None,
    )

    owner: typing.Optional["AdsStoriesOwner"] = Field(
        default=None,
    )

    stories_disclaimers_text: typing.Optional[str] = Field(
        default=None,
        description="Stories disclaimers text",
    )


class AdsStoriesResponse(BaseResponse):
    response: "AdsStoriesResponseModel"


class AdsStoriesOwnerResponseModel(BaseModel):
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


class AdsStoriesOwnerResponse(BaseResponse):
    response: "AdsStoriesOwnerResponseModel"


class AdsStoryItemResponseModel(BaseModel):
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


class AdsStoryItemResponse(BaseResponse):
    response: "AdsStoryItemResponseModel"


class AdsStoryItemLinkResponseModel(BaseModel):
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


class AdsStoryItemLinkResponse(BaseResponse):
    response: "AdsStoryItemLinkResponseModel"


class AdsStoryItemStatsResponseModel(BaseModel):
    follow: typing.Optional["AdsStoryItemStatsFollow"] = Field(
        default=None,
    )

    url_view: typing.Optional["AdsStoryItemStatsUrlView"] = Field(
        default=None,
    )


class AdsStoryItemStatsResponse(BaseResponse):
    response: "AdsStoryItemStatsResponseModel"


class AdsStoryItemStatsFollowResponseModel(BaseModel):
    event_type: typing.Optional[str] = Field(
        default=None,
        description="Event type",
    )

    rhash: typing.Optional[str] = Field(
        default=None,
        description="Event hash",
    )


class AdsStoryItemStatsFollowResponse(BaseResponse):
    response: "AdsStoryItemStatsFollowResponseModel"


class AdsStoryItemStatsUrlViewResponseModel(BaseModel):
    event_type: typing.Optional[str] = Field(
        default=None,
        description="Event type",
    )

    rhash: typing.Optional[str] = Field(
        default=None,
        description="Event hash",
    )


class AdsStoryItemStatsUrlViewResponse(BaseResponse):
    response: "AdsStoryItemStatsUrlViewResponseModel"


class AdsTargSettingsResponseModel(AdsCriteria):
    id: typing.Optional[str] = Field(
        default=None,
        description="Ad ID",
    )

    campaign_id: typing.Optional[str] = Field(
        default=None,
        description="Campaign ID",
    )


class AdsTargSettingsResponse(BaseResponse):
    response: "AdsTargSettingsResponseModel"


class AdsTargStatsResponseModel(BaseModel):
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


class AdsTargStatsResponse(BaseResponse):
    response: "AdsTargStatsResponseModel"


class AdsTargSuggestionsResponseModel(BaseModel):
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


class AdsTargSuggestionsResponse(BaseResponse):
    response: "AdsTargSuggestionsResponseModel"


class AdsTargSuggestionsCitiesResponseModel(BaseModel):
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


class AdsTargSuggestionsCitiesResponse(BaseResponse):
    response: "AdsTargSuggestionsCitiesResponseModel"


class AdsTargSuggestionsRegionsResponseModel(BaseModel):
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


class AdsTargSuggestionsRegionsResponse(BaseResponse):
    response: "AdsTargSuggestionsRegionsResponseModel"


class AdsTargSuggestionsSchoolsResponseModel(BaseModel):
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


class AdsTargSuggestionsSchoolsResponse(BaseResponse):
    response: "AdsTargSuggestionsSchoolsResponseModel"


class AdsTargSuggestionsSchoolsTypeResponseModel(enum.Enum):
    SCHOOL = "school"

    UNIVERSITY = "university"

    FACULTY = "faculty"

    CHAIR = "chair"


class AdsTargSuggestionsSchoolsTypeResponse(BaseResponse):
    response: "AdsTargSuggestionsSchoolsTypeResponseModel"


class AdsTargetGroupResponseModel(BaseModel):
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
        typing.List[AdsTargetGroupTargetPixelRule]
    ] = Field(
        default=None,
        description="Target Pixel rules",
    )

    last_updated: typing.Optional[int] = Field(
        default=None,
        description="Last updated",
    )


class AdsTargetGroupResponse(BaseResponse):
    response: "AdsTargetGroupResponseModel"


class AdsTargetGroupTargetPixelRuleResponseModel(BaseModel):
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


class AdsTargetGroupTargetPixelRuleResponse(BaseResponse):
    response: "AdsTargetGroupTargetPixelRuleResponseModel"


class AdsTargetPixelInfoResponseModel(BaseModel):
    target_pixel_id: int = Field()

    name: str = Field()

    domain: str = Field()

    category_id: int = Field()

    last_updated: int = Field()

    pixel: str = Field()


class AdsTargetPixelInfoResponse(BaseResponse):
    response: "AdsTargetPixelInfoResponseModel"


class AdsUpdateOfficeUsersResultResponseModel(BaseModel):
    user_id: int = Field()

    is_success: bool = Field()

    error: typing.Optional["BaseError"] = Field(
        default=None,
    )


class AdsUpdateOfficeUsersResultResponse(BaseResponse):
    response: "AdsUpdateOfficeUsersResultResponseModel"


class AdsUpdateAdsStatusResponseModel(BaseModel):
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


class AdsUpdateAdsStatusResponse(BaseResponse):
    response: "AdsUpdateAdsStatusResponseModel"


class AdsUpdateClientsStatusResponseModel(BaseModel):
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


class AdsUpdateClientsStatusResponse(BaseResponse):
    response: "AdsUpdateClientsStatusResponseModel"


class AdsUserSpecificationResponseModel(BaseModel):
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


class AdsUserSpecificationResponse(BaseResponse):
    response: "AdsUserSpecificationResponseModel"


class AdsUserSpecificationCuttedResponseModel(BaseModel):
    user_id: int = Field()

    role: "AdsAccessRolePublic" = Field()

    client_id: typing.Optional[int] = Field(
        default=None,
    )

    view_budget: typing.Optional[bool] = Field(
        default=None,
    )


class AdsUserSpecificationCuttedResponse(BaseResponse):
    response: "AdsUserSpecificationCuttedResponseModel"


class AdsUsersResponseModel(BaseModel):
    accesses: typing.List[AdsAccesses] = Field()

    user_id: int = Field(
        description="User ID",
    )


class AdsUsersResponse(BaseResponse):
    response: "AdsUsersResponseModel"
