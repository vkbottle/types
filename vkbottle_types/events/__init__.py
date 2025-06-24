from typing import Union

from .bot_typings import GroupTypes
from .enums import GroupEventType, UserEventType
from .user_typings import UserTypes

Event = Union[UserEventType, GroupEventType]


__all__ = ("Event", "GroupEventType", "GroupTypes", "UserEventType", "UserTypes")
