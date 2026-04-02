from typing import TypeAlias

from .bot_events import BaseGroupEvent
from .bot_typings import GroupTypes
from .enums import GroupEventType, UserEventType
from .user_events import BaseUserEvent
from .user_typings import UserTypes

Event: TypeAlias = UserEventType | GroupEventType


__all__ = ("BaseGroupEvent", "BaseUserEvent", "Event", "GroupEventType", "GroupTypes", "UserEventType", "UserTypes")
