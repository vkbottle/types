from .base_model import BaseObject
from . import video, base
from typing import Optional, Union, Any, List
import typing
import enum


class Restriction(BaseObject):
    """VK Object media/Restriction

    always_shown - Need show restriction always or not
    blur - Need blur current video or not
    can_play - Can play video or not
    can_preview - Can preview video or not
    """

    text: Optional[str] = None
    title: Optional[str] = None
    button: Optional[video.RestrictionButton] = None
    always_shown: Optional[base.BoolInt] = None
    blur: Optional[base.BoolInt] = None
    can_play: Optional[base.BoolInt] = None
    can_preview: Optional[base.BoolInt] = None
    card_icon: Optional[List[base.Image]] = None
    list_icon: Optional[List[base.Image]] = None
