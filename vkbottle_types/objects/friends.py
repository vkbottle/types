import enum
from typing import Optional, List

from .base_model import BaseObject


class FriendExtendedStatus(BaseObject):
    """VK Object friends/FriendExtendedStatus"""


class FriendStatus(BaseObject):
    """VK Object friends/FriendStatus"""

    friend_status: Optional["FriendStatusStatus"] = None
    sign: Optional[str] = None
    user_id: Optional[int] = None


class FriendStatusStatus(enum.IntEnum):
    """ Friend status with the user """

    not_a_friend = 0
    outcoming_request = 1
    incoming_request = 2
    is_friend = 3


class FriendsList(BaseObject):
    """VK Object friends/FriendsList

    id - List ID
    name - List title
    """

    id: Optional[int] = None
    name: Optional[str] = None


class MutualFriend(BaseObject):
    """VK Object friends/MutualFriend

    common_count - Total mutual friends number
    id - User ID
    """

    common_count: Optional[int] = None
    common_friends: Optional[List[int]] = None
    id: Optional[int] = None


class Requests(BaseObject):
    """VK Object friends/Requests

    from - ID of the user by whom friend has been suggested
    user_id - User ID
    """

    _from: Optional[str] = None
    mutual: Optional["RequestsMutual"] = None
    user_id: Optional[int] = None


class RequestsMutual(BaseObject):
    """VK Object friends/RequestsMutual

    count - Total mutual friends number
    """

    count: Optional[int] = None
    users: Optional[List[int]] = None


class RequestsXtrMessage(BaseObject):
    """VK Object friends/RequestsXtrMessage

    from - ID of the user by whom friend has been suggested
    message - Message sent with a request
    user_id - User ID
    """

    _from: Optional[str] = None
    message: Optional[str] = None
    mutual: Optional["RequestsMutual"] = None
    user_id: Optional[int] = None


class UserXtrLists(BaseObject):
    """VK Object friends/UserXtrLists"""


class UserXtrPhone(BaseObject):
    """VK Object friends/UserXtrPhone"""
