from .base_model import BaseObject
from . import groups
from typing import Optional, Union, Any, List
import typing
import enum


class EventAttach(BaseObject):
    """VK Object events/EventAttach"""

    address: Optional[str] = None
    button_text: Optional[str] = None
    friends: Optional[List[int]] = None
    id: Optional[int] = None
    is_favorite: Optional[bool] = None
    member_status: Optional[groups.GroupFullMemberStatus] = None
    text: Optional[str] = None
    time: Optional[int] = None
