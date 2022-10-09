from typing import Union

from .bot_events import *  # noqa
from .bot_typings import GroupTypes  # noqa
from .enums import GroupEventType, UserEventType
from .user_events import *  # noqa
from .user_typings import UserTypes  # noqa

Event = Union[UserEventType, GroupEventType]
