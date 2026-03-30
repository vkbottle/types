from typing import TypeAlias

from .bot_typings import GroupTypes
from .enums import GroupEventType, UserEventType
from .user_typings import UserTypes

Event: TypeAlias = UserEventType | GroupEventType


__all__ = ("Event", "GroupEventType", "GroupTypes", "UserEventType", "UserTypes")
