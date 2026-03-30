import typing

from vkbottle_types.events import Event, GroupTypes, UserTypes
from vkbottle_types.events.bot_events import BaseGroupEvent
from vkbottle_types.events.user_events import BaseUserEvent

API_URL: typing.Final = "https://api.vk.ru/method/"
API_VERSION: typing.Final = "5.199"


__all__ = (
    "API_URL",
    "API_VERSION",
    "BaseGroupEvent",
    "BaseUserEvent",
    "Event",
    "GroupTypes",
    "UserTypes",
)
