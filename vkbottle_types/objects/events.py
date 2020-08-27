from .base_model import BaseObject
from . import groups
from typing import Optional, Union, Any, List
import typing
import enum


class EventAttach(BaseObject):
    """VK Object events/EventAttach

    address - address of event
    button_text - text of attach
    friends - array of friends ids
    id - event ID
    is_favorite - is favorite
    member_status - Current user's member status
    text - text of attach
    time - event start time
    """

    address: Optional[str] = None
    button_text: Optional[str] = None
    friends: Optional[List[int]] = None
    id: Optional[int] = None
    is_favorite: Optional[bool] = None
    member_status: Optional[groups.GroupFullMemberStatus] = None
    text: Optional[str] = None
    time: Optional[int] = None
