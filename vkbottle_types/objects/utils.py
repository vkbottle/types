from .base_model import BaseObject
from typing import Optional, Union, Any, List
import typing
import enum


class DomainResolved(BaseObject):
    """VK Object utils/DomainResolved"""

    object_id: Optional[int] = None
    group_id: Optional[int] = None
    type: Optional["DomainResolvedType"]


class DomainResolvedType(enum.Enum):
    """ Object type """

    USER = "user"
    GROUP = "group"
    APPLICATION = "application"
    PAGE = "page"


class LastShortenedLink(BaseObject):
    """VK Object utils/LastShortenedLink

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


class LinkChecked(BaseObject):
    """VK Object utils/LinkChecked"""

    link: Optional[str] = None
    status: Optional["LinkCheckedStatus"]


class LinkCheckedStatus(enum.Enum):
    """ Link status """

    NOT_BANNED = "not_banned"
    BANNED = "banned"
    PROCESSING = "processing"


class LinkStats(BaseObject):
    """VK Object utils/LinkStats

    key - Link key (characters after vk.cc/)
    """

    key: Optional[str] = None
    stats: Optional[List["Stats"]]


class LinkStatsExtended(BaseObject):
    """VK Object utils/LinkStatsExtended

    key - Link key (characters after vk.cc/)
    """

    key: Optional[str] = None
    stats: Optional[List["StatsExtended"]]


class ShortLink(BaseObject):
    """VK Object utils/ShortLink

    access_key - Access key for private stats
    key - Link key (characters after vk.cc/)
    short_url - Short link URL
    url - Full URL
    """

    access_key: Optional[str] = None
    key: Optional[str] = None
    short_url: Optional[str] = None
    url: Optional[str] = None


class Stats(BaseObject):
    """VK Object utils/Stats

    timestamp - Start time
    views - Total views number
    """

    timestamp: Optional[int] = None
    views: Optional[int] = None


class StatsCity(BaseObject):
    """VK Object utils/StatsCity

    city_id - City ID
    views - Views number
    """

    city_id: Optional[int] = None
    views: Optional[int] = None


class StatsCountry(BaseObject):
    """VK Object utils/StatsCountry

    country_id - Country ID
    views - Views number
    """

    country_id: Optional[int] = None
    views: Optional[int] = None


class StatsExtended(BaseObject):
    """VK Object utils/StatsExtended

    timestamp - Start time
    views - Total views number
    """

    cities: Optional[List["StatsCity"]]
    countries: Optional[List["StatsCountry"]]
    sex_age: Optional[List["StatsSexAge"]]
    timestamp: Optional[int] = None
    views: Optional[int] = None


class StatsSexAge(BaseObject):
    """VK Object utils/StatsSexAge

    age_range - Age denotation
    female -  Views by female users
    male -  Views by male users
    """

    age_range: Optional[str] = None
    female: Optional[int] = None
    male: Optional[int] = None
