from .base_model import BaseObject
from . import wall
from typing import Optional, Union, Any, List
import typing
import enum


class Thread(BaseObject):
    """VK Object comment/Thread"""

    can_post: Optional[bool] = None
    count: Optional[int] = None
    groups_can_post: Optional[bool] = None
    items: Optional[List[wall.WallComment]] = None
    show_reply_button: Optional[bool] = None
