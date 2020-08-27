from .base_model import BaseObject
from . import photos
from typing import Optional, Union, Any, List
import typing
import enum


class Currency(BaseObject):
    """VK Object market/Currency

    id - Currency ID
    name - Currency sign
    """

    id: Optional[int] = None
    name: Optional[str] = None


class MarketAlbum(BaseObject):
    """VK Object market/MarketAlbum

    count - Items number
    id - Market album ID
    owner_id - Market album owner's ID
    title - Market album title
    updated_time - Date when album has been updated last time in Unixtime
    """

    count: Optional[int] = None
    id: Optional[int] = None
    owner_id: Optional[int] = None
    photo: Optional[photos.Photo] = None
    title: Optional[str] = None
    updated_time: Optional[int] = None


class MarketCategory(BaseObject):
    """VK Object market/MarketCategory

    id - Category ID
    name - Category name
    """

    id: Optional[int] = None
    name: Optional[str] = None
    section: Optional["Section"] = None


class MarketItem(BaseObject):
    """VK Object market/MarketItem"""

    access_key: Optional[str] = None
    availability: Optional["MarketItemAvailability"] = None
    button_title: Optional[str] = None
    category: Optional["MarketCategory"] = None
    date: Optional[int] = None
    description: Optional[str] = None
    external_id: Optional[str] = None
    id: Optional[int] = None
    is_favorite: Optional[bool] = None
    owner_id: Optional[int] = None
    price: Optional["Price"] = None
    thumb_photo: Optional[str] = None
    title: Optional[str] = None
    url: Optional[str] = None
    variants_grouping_id: Optional[int] = None
    is_main_variant: Optional[bool] = None


class MarketItemAvailability(enum.IntEnum):
    """ Information whether the item is available """

    available = 0
    removed = 1
    unavailable = 2


class MarketItemFull(BaseObject):
    """VK Object market/MarketItemFull"""


class Price(BaseObject):
    """VK Object market/Price

    amount - Amount
    text - Text
    """

    amount: Optional[str] = None
    currency: Optional["Currency"] = None
    discount_rate: Optional[int] = None
    old_amount: Optional[str] = None
    text: Optional[str] = None


class Section(BaseObject):
    """VK Object market/Section

    id - Section ID
    name - Section name
    """

    id: Optional[int] = None
    name: Optional[str] = None
