from .base_model import BaseObject
from . import base
from typing import Optional, Union, Any, List
import typing
import enum


class PrettyCard(BaseObject):
    """VK Object prettyCards/PrettyCard"""

    button: Optional[str] = None
    button_text: Optional[str] = None
    card_id: Optional[str] = None
    images: Optional[List[base.Image]] = None
    link_url: Optional[str] = None
    photo: Optional[str] = None
    price: Optional[str] = None
    price_old: Optional[str] = None
    title: Optional[str] = None
