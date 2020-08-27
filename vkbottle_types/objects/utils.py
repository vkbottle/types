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
    """VK Object utils/LastShortenedLink"""

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
    """VK Object utils/LinkStats"""

    key: Optional[str] = None
    stats: Optional[List["Stats"]]


class LinkStatsExtended(BaseObject):
    """VK Object utils/LinkStatsExtended"""

    key: Optional[str] = None
    stats: Optional[List["StatsExtended"]]


class ShortLink(BaseObject):
    """VK Object utils/ShortLink"""

    access_key: Optional[str] = None
    key: Optional[str] = None
    short_url: Optional[str] = None
    url: Optional[str] = None


class Stats(BaseObject):
    """VK Object utils/Stats"""

    timestamp: Optional[int] = None
    views: Optional[int] = None


class StatsCity(BaseObject):
    """VK Object utils/StatsCity"""

    city_id: Optional[int] = None
    views: Optional[int] = None


class StatsCountry(BaseObject):
    """VK Object utils/StatsCountry"""

    country_id: Optional[int] = None
    views: Optional[int] = None


class StatsExtended(BaseObject):
    """VK Object utils/StatsExtended"""

    cities: Optional[List["StatsCity"]]
    countries: Optional[List["StatsCountry"]]
    sex_age: Optional[List["StatsSexAge"]]
    timestamp: Optional[int] = None
    views: Optional[int] = None


class StatsSexAge(BaseObject):
    """VK Object utils/StatsSexAge"""

    age_range: Optional[str] = None
    female: Optional[int] = None
    male: Optional[int] = None
