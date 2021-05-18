from typing import Union

from .bot_events import *
from .bot_typings import GroupTypes
from .enums import GroupEventType, UserEventType
from .events_base import EventsBase
from .user_events import *
from .user_typings import UserTypes

Event = Union[UserEventType, GroupEventType]
