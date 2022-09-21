from typing import Union

from .bot_events import *  # noqa
from .enums import GroupEventType, UserEventType
from .user_events import *  # noqa

Event = Union[UserEventType, GroupEventType]
