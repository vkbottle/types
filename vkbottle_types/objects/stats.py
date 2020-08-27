from .base_model import BaseObject
from typing import Optional, Union, Any, List
import typing
import enum


class Activity(BaseObject):
    """VK Object stats/Activity"""

    comments: Optional[int] = None
    copies: Optional[int] = None
    hidden: Optional[int] = None
    likes: Optional[int] = None
    subscribed: Optional[int] = None
    unsubscribed: Optional[int] = None


class City(BaseObject):
    """VK Object stats/City"""

    count: Optional[int] = None
    name: Optional[str] = None
    value: Optional[int] = None


class Country(BaseObject):
    """VK Object stats/Country"""

    code: Optional[str] = None
    count: Optional[int] = None
    name: Optional[str] = None
    value: Optional[int] = None


class Period(BaseObject):
    """VK Object stats/Period"""

    activity: Optional["Activity"]
    period_from: Optional[int] = None
    period_to: Optional[int] = None
    reach: Optional["Reach"]
    visitors: Optional["Views"]


class Reach(BaseObject):
    """VK Object stats/Reach"""

    age: Optional[List["SexAge"]]
    cities: Optional[List["City"]]
    countries: Optional[List["Country"]]
    mobile_reach: Optional[int] = None
    reach: Optional[int] = None
    reach_subscribers: Optional[int] = None
    sex: Optional[List["SexAge"]]
    sex_age: Optional[List["SexAge"]]


class SexAge(BaseObject):
    """VK Object stats/SexAge"""

    count: Optional[int] = None
    value: Optional[str] = None
    reach: Optional[int] = None
    reach_subscribers: Optional[int] = None
    count_subscribers: Optional[int] = None


class Views(BaseObject):
    """VK Object stats/Views"""

    age: Optional[List["SexAge"]]
    cities: Optional[List["City"]]
    countries: Optional[List["Country"]]
    mobile_views: Optional[int] = None
    sex: Optional[List["SexAge"]]
    sex_age: Optional[List["SexAge"]]
    views: Optional[int] = None
    visitors: Optional[int] = None


class WallpostStat(BaseObject):
    """VK Object stats/WallpostStat"""

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
    sex_age: Optional[List["SexAge"]]
