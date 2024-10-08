from typing import Union

from .bot_typings import GroupTypes
from .enums import GroupEventType, UserEventType
from .user_typings import UserTypes

Event = Union[UserEventType, GroupEventType]


__all__ = ("GroupTypes", "GroupEventType", "UserEventType", "UserTypes", "Event")
