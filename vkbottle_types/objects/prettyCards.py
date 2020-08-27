from .base_model import BaseObject
from . import base
from typing import Optional, Union, Any, List
import typing
import enum


class PrettyCard(BaseObject):
    """VK Object prettyCards/PrettyCard

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
    images: Optional[List[base.Image]] = None
    link_url: Optional[str] = None
    photo: Optional[str] = None
    price: Optional[str] = None
    price_old: Optional[str] = None
    title: Optional[str] = None
