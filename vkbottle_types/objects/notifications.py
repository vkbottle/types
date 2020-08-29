from typing import Optional, List

from . import board, wall, photos, video, base
from .base_model import BaseObject


class Feedback(BaseObject):
    """VK Object notifications/Feedback

    from_id - Reply author's ID
    id - Item ID
    text - Reply text
    to_id - Wall owner's ID
    """

    attachments: Optional[List[wall.WallpostAttachment]] = None
    from_id: Optional[int] = None
    geo: Optional[base.Geo] = None
    id: Optional[int] = None
    likes: Optional[base.LikesInfo] = None
    text: Optional[str] = None
    to_id: Optional[int] = None


class Notification(BaseObject):
    """VK Object notifications/Notification

    date - Date when the event has been occurred
    type - Notification type
    """

    date: Optional[int] = None
    feedback: Optional["Feedback"] = None
    parent: Optional["NotificationParent"] = None
    reply: Optional["Reply"] = None
    type: Optional[str] = None


class NotificationItem(BaseObject):
    """VK Object notifications/NotificationItem"""


class NotificationParent(BaseObject):
    """VK Object notifications/NotificationParent"""


class NotificationsComment(BaseObject):
    """VK Object notifications/NotificationsComment

    date - Date when the comment has been added in Unixtime
    id - Comment ID
    owner_id - Author ID
    text - Comment text
    """

    date: Optional[int] = None
    id: Optional[int] = None
    owner_id: Optional[int] = None
    photo: Optional[photos.Photo] = None
    post: Optional[wall.Wallpost] = None
    text: Optional[str] = None
    topic: Optional[board.Topic] = None
    video: Optional[video.Video] = None


class Reply(BaseObject):
    """VK Object notifications/Reply

    date - Date when the reply has been created in Unixtime
    id - Reply ID
    text - Reply text
    """

    date: Optional[int] = None
    id: Optional[int] = None
    text: Optional[int] = None


class SendMessageError(BaseObject):
    """VK Object notifications/SendMessageError

    code - Error code
    description - Error description
    """

    code: Optional[int] = None
    description: Optional[str] = None


class SendMessageItem(BaseObject):
    """VK Object notifications/SendMessageItem

    user_id - User ID
    status - Notification status
    """

    user_id: Optional[int] = None
    status: Optional[bool] = None
    error: Optional["SendMessageError"] = None
