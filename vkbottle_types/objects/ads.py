from .base_model import BaseObject
from . import base
from typing import Optional, Union, Any, List
import typing
import enum


class AccessRole(enum.Enum):
    """ Current user's role """

    ADMIN = "admin"
    MANAGER = "manager"
    REPORTS = "reports"


class Accesses(BaseObject):
    """VK Object ads/Accesses"""

    client_id: Optional[str] = None
    role: Optional["AccessRole"]


class Account(BaseObject):
    """VK Object ads/Account"""

    access_role: Optional["AccessRole"]
    account_id: Optional[int] = None
    account_status: Optional[base.BoolInt] = None
    account_type: Optional["AccountType"]
    account_name: Optional[str] = None


class AccountType(enum.Enum):
    """ Account type """

    GENERAL = "general"
    AGENCY = "agency"


class Ad(BaseObject):
    """VK Object ads/Ad"""

    ad_format: Optional[int] = None
    ad_platform: Optional[Union[int, str]] = None
    all_limit: Optional[int] = None
    approved: Optional["AdApproved"]
    campaign_id: Optional[int] = None
    category1_id: Optional[int] = None
    category2_id: Optional[int] = None
    cost_type: Optional["AdCostType"]
    cpc: Optional[int] = None
    cpm: Optional[int] = None
    cpa: Optional[int] = None
    ocpm: Optional[int] = None
    autobidding_max_cost: Optional[int] = None
    disclaimer_medical: Optional[base.BoolInt] = None
    disclaimer_specialist: Optional[base.BoolInt] = None
    disclaimer_supplements: Optional[base.BoolInt] = None
    id: Optional[int] = None
    impressions_limit: Optional[int] = None
    impressions_limited: Optional[base.BoolInt] = None
    name: Optional[str] = None
    status: Optional["AdStatus"]
    video: Optional[base.BoolInt] = None


class AdApproved(enum.IntEnum):
    """ Review status """

    not_moderated = 0
    pending_moderation = 1
    approved = 2
    rejected = 3


class AdCostType(enum.IntEnum):
    """ Cost type """

    per_clicks = 0
    per_impressions = 1
    per_actions = 2
    per_impressions_optimized = 3


class AdLayout(BaseObject):
    """VK Object ads/AdLayout"""

    ad_format: Optional[int] = None
    campaign_id: Optional[int] = None
    cost_type: Optional["AdCostType"]
    description: Optional[str] = None
    id: Optional[int] = None
    image_src: Optional[str] = None
    image_src_2x: Optional[str] = None
    link_domain: Optional[str] = None
    link_url: Optional[str] = None
    preview_link: Optional[Union[int, str]] = None
    title: Optional[str] = None
    video: Optional[base.BoolInt] = None


class AdStatus(enum.IntEnum):
    """ Ad atatus """

    stopped = 0
    started = 1
    deleted = 2


class Campaign(BaseObject):
    """VK Object ads/Campaign"""

    all_limit: Optional[str] = None
    day_limit: Optional[str] = None
    id: Optional[int] = None
    name: Optional[str] = None
    start_time: Optional[int] = None
    status: Optional["CampaignStatus"]
    stop_time: Optional[int] = None
    type: Optional["CampaignType"]


class CampaignStatus(enum.IntEnum):
    """ Campaign status """

    stopped = 0
    started = 1
    deleted = 2


class CampaignType(enum.Enum):
    """ Campaign type """

    NORMAL = "normal"
    VK_APPS_MANAGED = "vk_apps_managed"
    MOBILE_APPS = "mobile_apps"
    PROMOTED_POSTS = "promoted_posts"


class Category(BaseObject):
    """VK Object ads/Category"""

    id: Optional[int] = None
    name: Optional[str] = None
    subcategories: Optional[List[base.ObjectWithName]] = None


class Client(BaseObject):
    """VK Object ads/Client"""

    all_limit: Optional[str] = None
    day_limit: Optional[str] = None
    id: Optional[int] = None
    name: Optional[str] = None


class Criteria(BaseObject):
    """VK Object ads/Criteria"""

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
    paying: Optional[base.BoolInt] = None
    positions: Optional[str] = None
    religions: Optional[str] = None
    retargeting_groups: Optional[str] = None
    retargeting_groups_not: Optional[str] = None
    school_from: Optional[int] = None
    school_to: Optional[int] = None
    schools: Optional[str] = None
    sex: Optional["CriteriaSex"]
    stations: Optional[str] = None
    statuses: Optional[str] = None
    streets: Optional[str] = None
    travellers: Optional[base.PropertyExists] = None
    uni_from: Optional[int] = None
    uni_to: Optional[int] = None
    user_browsers: Optional[str] = None
    user_devices: Optional[str] = None
    user_os: Optional[str] = None


class CriteriaSex(enum.IntEnum):
    """ Sex """

    any = 0
    male = 1
    female = 2


class DemoStats(BaseObject):
    """VK Object ads/DemoStats"""

    id: Optional[int] = None
    stats: Optional["DemostatsFormat"]
    type: Optional["ObjectType"]


class DemostatsFormat(BaseObject):
    """VK Object ads/DemostatsFormat"""

    age: Optional[List["StatsAge"]]
    cities: Optional[List["StatsCities"]]
    day: Optional[str] = None
    month: Optional[str] = None
    overall: Optional[int] = None
    sex: Optional[List["StatsSex"]]
    sex_age: Optional[List["StatsSexAge"]]


class FloodStats(BaseObject):
    """VK Object ads/FloodStats"""

    left: Optional[int] = None
    refresh: Optional[int] = None


class LinkStatus(BaseObject):
    """VK Object ads/LinkStatus"""

    description: Optional[str] = None
    redirect_url: Optional[str] = None
    status: Optional[str] = None


class LookalikeRequest(BaseObject):
    """VK Object ads/LookalikeRequest"""

    id: Optional[int] = None
    create_time: Optional[int] = None
    update_time: Optional[int] = None
    scheduled_delete_time: Optional[int] = None
    status: Optional[str] = None
    source_type: Optional[str] = None
    source_retargeting_group_id: Optional[int] = None
    source_name: Optional[str] = None
    audience_count: Optional[int] = None
    save_audience_levels: Optional[List["LookalikeRequestSaveAudienceLevel"]]


class LookalikeRequestSaveAudienceLevel(BaseObject):
    """VK Object ads/LookalikeRequestSaveAudienceLevel"""

    level: Optional[int] = None
    audience_count: Optional[int] = None


class Musician(BaseObject):
    """VK Object ads/Musician"""

    id: Optional[int] = None
    name: Optional[str] = None


class ObjectType(enum.Enum):
    """ Object type """

    AD = "ad"
    CAMPAIGN = "campaign"
    CLIENT = "client"
    OFFICE = "office"


class Paragraphs(BaseObject):
    """VK Object ads/Paragraphs"""

    paragraph: Optional[str] = None


class PromotedPostReach(BaseObject):
    """VK Object ads/PromotedPostReach"""

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


class RejectReason(BaseObject):
    """VK Object ads/RejectReason"""

    comment: Optional[str] = None
    rules: Optional[List["Rules"]]


class Rules(BaseObject):
    """VK Object ads/Rules"""

    paragraphs: Optional[List["Paragraphs"]]
    title: Optional[str] = None


class Stats(BaseObject):
    """VK Object ads/Stats"""

    id: Optional[int] = None
    stats: Optional["StatsFormat"]
    type: Optional["ObjectType"]
    views_times: Optional["StatsViewsTimes"]


class StatsAge(BaseObject):
    """VK Object ads/StatsAge"""

    clicks_rate: Optional[float] = None
    impressions_rate: Optional[float] = None
    value: Optional[str] = None


class StatsCities(BaseObject):
    """VK Object ads/StatsCities"""

    clicks_rate: Optional[float] = None
    impressions_rate: Optional[float] = None
    name: Optional[str] = None
    value: Optional[int] = None


class StatsFormat(BaseObject):
    """VK Object ads/StatsFormat"""

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


class StatsSex(BaseObject):
    """VK Object ads/StatsSex"""

    clicks_rate: Optional[float] = None
    impressions_rate: Optional[float] = None
    value: Optional["StatsSexValue"]


class StatsSexAge(BaseObject):
    """VK Object ads/StatsSexAge"""

    clicks_rate: Optional[float] = None
    impressions_rate: Optional[float] = None
    value: Optional[str] = None


class StatsSexValue(enum.Enum):
    """ Sex """

    F = "f"
    M = "m"


class StatsViewsTimes(BaseObject):
    """VK Object ads/StatsViewsTimes"""

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


class TargSettings(BaseObject):
    """VK Object ads/TargSettings"""


class TargStats(BaseObject):
    """VK Object ads/TargStats"""

    audience_count: Optional[int] = None
    recommended_cpc: Optional[float] = None
    recommended_cpm: Optional[float] = None
    recommended_cpc_50: Optional[float] = None
    recommended_cpm_50: Optional[float] = None
    recommended_cpc_70: Optional[float] = None
    recommended_cpm_70: Optional[float] = None
    recommended_cpc_90: Optional[float] = None
    recommended_cpm_90: Optional[float] = None


class TargSuggestions(BaseObject):
    """VK Object ads/TargSuggestions"""

    id: Optional[int] = None
    name: Optional[str] = None


class TargSuggestionsCities(BaseObject):
    """VK Object ads/TargSuggestionsCities"""

    id: Optional[int] = None
    name: Optional[str] = None
    parent: Optional[str] = None


class TargSuggestionsRegions(BaseObject):
    """VK Object ads/TargSuggestionsRegions"""

    id: Optional[int] = None
    name: Optional[str] = None
    type: Optional[str] = None


class TargSuggestionsSchools(BaseObject):
    """VK Object ads/TargSuggestionsSchools"""

    desc: Optional[str] = None
    id: Optional[int] = None
    name: Optional[str] = None
    parent: Optional[str] = None
    type: Optional["TargSuggestionsSchoolsType"]


class TargSuggestionsSchoolsType(enum.Enum):
    """ School type """

    SCHOOL = "school"
    UNIVERSITY = "university"
    FACULTY = "faculty"
    CHAIR = "chair"


class TargetGroup(BaseObject):
    """VK Object ads/TargetGroup"""

    audience_count: Optional[int] = None
    domain: Optional[str] = None
    id: Optional[int] = None
    lifetime: Optional[int] = None
    name: Optional[str] = None
    pixel: Optional[str] = None


class Users(BaseObject):
    """VK Object ads/Users"""

    accesses: Optional[List["Accesses"]]
    user_id: Optional[int] = None
