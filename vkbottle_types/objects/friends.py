from .base_model import BaseObject
from typing import Optional, Union, Any, List
import typing
import enum


class FriendExtendedStatus(BaseObject):
    """VK Object friends/FriendExtendedStatus"""


class FriendStatus(BaseObject):
    """VK Object friends/FriendStatus"""

    friend_status: Optional["FriendStatusStatus"]
    sign: Optional[str] = None
    user_id: Optional[int] = None


class FriendStatusStatus(enum.IntEnum):
    """ Friend status with the user """

    not_a_friend = 0
    outcoming_request = 1
    incoming_request = 2
    is_friend = 3


class FriendsList(BaseObject):
    """VK Object friends/FriendsList"""

    id: Optional[int] = None
    name: Optional[str] = None


class MutualFriend(BaseObject):
    """VK Object friends/MutualFriend"""

    common_count: Optional[int] = None
    common_friends: Optional[List[int]] = None
    id: Optional[int] = None


class Requests(BaseObject):
    """VK Object friends/Requests"""

    _from: Optional[str] = None
    mutual: Optional["RequestsMutual"]
    user_id: Optional[int] = None


class RequestsMutual(BaseObject):
    """VK Object friends/RequestsMutual"""

    count: Optional[int] = None
    users: Optional[List[int]] = None


class RequestsXtrMessage(BaseObject):
    """VK Object friends/RequestsXtrMessage"""

    _from: Optional[str] = None
    message: Optional[str] = None
    mutual: Optional["RequestsMutual"]
    user_id: Optional[int] = None


class UserXtrLists(BaseObject):
    """VK Object friends/UserXtrLists"""


class UserXtrPhone(BaseObject):
    """VK Object friends/UserXtrPhone"""
