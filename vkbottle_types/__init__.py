import typing

from .events import GroupTypes, UserTypes

API_URL: typing.Final[str] = "https://api.vk.com/method/"
API_VERSION: typing.Final[str] = "5.199"


__all__ = (
    "API_URL",
    "API_VERSION",
    "GroupTypes",
    "UserTypes",
)
