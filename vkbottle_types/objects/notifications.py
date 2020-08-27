from .base_model import BaseObject
from . import photos, wall, video, base, board
from typing import Optional, Union, Any, List
import typing
import enum


class Feedback(BaseObject):
    """VK Object notifications/Feedback"""

    attachments: Optional[List[wall.WallpostAttachment]] = None
    from_id: Optional[int] = None
    geo: Optional[base.Geo] = None
    id: Optional[int] = None
    likes: Optional[base.LikesInfo] = None
    text: Optional[str] = None
    to_id: Optional[int] = None


class Notification(BaseObject):
    """VK Object notifications/Notification"""

    date: Optional[int] = None
    feedback: Optional["Feedback"]
    parent: Optional["NotificationParent"]
    reply: Optional["Reply"]
    type: Optional[str] = None


class NotificationItem(BaseObject):
    """VK Object notifications/NotificationItem"""


class NotificationParent(BaseObject):
    """VK Object notifications/NotificationParent"""


class NotificationsComment(BaseObject):
    """VK Object notifications/NotificationsComment"""

    date: Optional[int] = None
    id: Optional[int] = None
    owner_id: Optional[int] = None
    photo: Optional[photos.Photo] = None
    post: Optional[wall.Wallpost] = None
    text: Optional[str] = None
    topic: Optional[board.Topic] = None
    video: Optional[video.Video] = None


class Reply(BaseObject):
    """VK Object notifications/Reply"""

    date: Optional[int] = None
    id: Optional[int] = None
    text: Optional[int] = None


class SendMessageError(BaseObject):
    """VK Object notifications/SendMessageError"""

    code: Optional[int] = None
    description: Optional[str] = None


class SendMessageItem(BaseObject):
    """VK Object notifications/SendMessageItem"""

    user_id: Optional[int] = None
    status: Optional[bool] = None
    error: Optional["SendMessageError"]
