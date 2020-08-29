from typing import Optional, List

from .base_model import BaseObject


class Activity(BaseObject):
    """VK Object stats/Activity

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


class City(BaseObject):
    """VK Object stats/City

    count - Visitors number
    name - City name
    value - City ID
    """

    count: Optional[int] = None
    name: Optional[str] = None
    value: Optional[int] = None


class Country(BaseObject):
    """VK Object stats/Country

    code - Country code
    count - Visitors number
    name - Country name
    value - Country ID
    """

    code: Optional[str] = None
    count: Optional[int] = None
    name: Optional[str] = None
    value: Optional[int] = None


class Period(BaseObject):
    """VK Object stats/Period

    period_from - Unix timestamp
    period_to - Unix timestamp
    """

    activity: Optional["Activity"] = None
    period_from: Optional[int] = None
    period_to: Optional[int] = None
    reach: Optional["Reach"] = None
    visitors: Optional["Views"] = None


class Reach(BaseObject):
    """VK Object stats/Reach

    mobile_reach - Reach count from mobile devices
    reach - Reach count
    reach_subscribers - Subscribers reach count
    """

    age: Optional[List["SexAge"]] = None
    cities: Optional[List["City"]] = None
    countries: Optional[List["Country"]] = None
    mobile_reach: Optional[int] = None
    reach: Optional[int] = None
    reach_subscribers: Optional[int] = None
    sex: Optional[List["SexAge"]] = None
    sex_age: Optional[List["SexAge"]] = None


class SexAge(BaseObject):
    """VK Object stats/SexAge

    count - Visitors number
    value - Sex/age value
    """

    count: Optional[int] = None
    value: Optional[str] = None
    reach: Optional[int] = None
    reach_subscribers: Optional[int] = None
    count_subscribers: Optional[int] = None


class Views(BaseObject):
    """VK Object stats/Views

    mobile_views - Number of views from mobile devices
    views - Views number
    visitors - Visitors number
    """

    age: Optional[List["SexAge"]] = None
    cities: Optional[List["City"]] = None
    countries: Optional[List["Country"]] = None
    mobile_views: Optional[int] = None
    sex: Optional[List["SexAge"]] = None
    sex_age: Optional[List["SexAge"]] = None
    views: Optional[int] = None
    visitors: Optional[int] = None


class WallpostStat(BaseObject):
    """VK Object stats/WallpostStat

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
    sex_age: Optional[List["SexAge"]] = None
