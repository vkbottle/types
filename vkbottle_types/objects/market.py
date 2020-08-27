from .base_model import BaseObject
from . import photos
from typing import Optional, Union, Any, List
import typing
import enum


class Currency(BaseObject):
    """VK Object market/Currency"""

    id: Optional[int] = None
    name: Optional[str] = None


class MarketAlbum(BaseObject):
    """VK Object market/MarketAlbum"""

    count: Optional[int] = None
    id: Optional[int] = None
    owner_id: Optional[int] = None
    photo: Optional[photos.Photo] = None
    title: Optional[str] = None
    updated_time: Optional[int] = None


class MarketCategory(BaseObject):
    """VK Object market/MarketCategory"""

    id: Optional[int] = None
    name: Optional[str] = None
    section: Optional["Section"]


class MarketItem(BaseObject):
    """VK Object market/MarketItem"""

    access_key: Optional[str] = None
    availability: Optional["MarketItemAvailability"]
    button_title: Optional[str] = None
    category: Optional["MarketCategory"]
    date: Optional[int] = None
    description: Optional[str] = None
    external_id: Optional[str] = None
    id: Optional[int] = None
    is_favorite: Optional[bool] = None
    owner_id: Optional[int] = None
    price: Optional["Price"]
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
    """VK Object market/Price"""

    amount: Optional[str] = None
    currency: Optional["Currency"]
    discount_rate: Optional[int] = None
    old_amount: Optional[str] = None
    text: Optional[str] = None


class Section(BaseObject):
    """VK Object market/Section"""

    id: Optional[int] = None
    name: Optional[str] = None
