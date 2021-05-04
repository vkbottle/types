from .events_base import EventsBase
from .enums import GroupEventType, UserEventType
from .bot_events import *
from .bot_typings import GroupTypes
from .user_events import *
from .user_typings import UserTypes
from typing import Union

Event = Union[UserEventType, GroupEventType]
