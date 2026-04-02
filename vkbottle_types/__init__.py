import typing

from vkbottle_types.categories import APICategories
from vkbottle_types.events import *

API_URL: typing.Final = "https://api.vk.ru/method/"
API_VERSION: typing.Final = "5.199"


__all__ = (
    "API_URL",
    "API_VERSION",
    "APICategories",
    "BaseGroupEvent",
    "BaseUserEvent",
    "Event",
    "GroupEventType",
    "GroupTypes",
    "UserEventType",
    "UserTypes",
)
