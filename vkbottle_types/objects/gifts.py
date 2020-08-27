from .base_model import BaseObject
from typing import Optional, Union, Any, List
import typing
import enum


class Gift(BaseObject):
    """VK Object gifts/Gift"""

    date: Optional[int] = None
    from_id: Optional[int] = None
    gift: Optional["Layout"]
    gift_hash: Optional[str] = None
    id: Optional[int] = None
    message: Optional[str] = None
    privacy: Optional["GiftPrivacy"]


class GiftPrivacy(enum.IntEnum):
    """ Gift privacy """

    name_and_message_for_all = 0
    name_for_all = 1
    name_and_message_for_recipient_only = 2


class Layout(BaseObject):
    """VK Object gifts/Layout"""

    id: Optional[int] = None
    thumb_512: Optional[str] = None
    thumb_256: Optional[str] = None
    thumb_48: Optional[str] = None
    thumb_96: Optional[str] = None
    stickers_product_id: Optional[int] = None
    build_id: Optional[str] = None
    keywords: Optional[str] = None
