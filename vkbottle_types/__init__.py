from .events import GroupTypes, UserTypes
from .state import BaseStateGroup, StatePeer

API_URL = "https://api.vk.com/method/"
API_VERSION = "5.131"

__all__ = (
    "GroupTypes",
    "UserTypes",
    "API_URL",
    "API_VERSION",
    "BaseStateGroup",
    "StatePeer",
)
