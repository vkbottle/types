from .events import GroupTypes, UserTypes
from .state import BaseStateGroup, StatePeer

API_URL = "https://api.vk.com/method/"
API_VERSION = "5.131"

__all__ = (
    "API_URL",
    "API_VERSION",
    "BaseStateGroup",
    "GroupTypes",
    "StatePeer",
    "UserTypes",
)
