import typing

from vkbottle_types.events import Event, GroupTypes, UserTypes

API_URL: typing.Final[str] = "https://api.vk.ru/method/"
API_VERSION: typing.Final[str] = "5.199"


__all__ = (
    "API_URL",
    "API_VERSION",
    "Event",
    "GroupTypes",
    "UserTypes",
)
