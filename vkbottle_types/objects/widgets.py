from .base_model import BaseObject
from . import base, users, wall
from typing import Optional, Union, Any, List
import typing
import enum


class CommentMedia(BaseObject):
    """VK Object widgets/CommentMedia"""

    item_id: Optional[int] = None
    owner_id: Optional[int] = None
    thumb_src: Optional[str] = None
    type: Optional["CommentMediaType"]


class CommentMediaType(enum.Enum):
    """ Media type """

    AUDIO = "audio"
    PHOTO = "photo"
    VIDEO = "video"


class CommentReplies(BaseObject):
    """VK Object widgets/CommentReplies"""

    can_post: Optional[base.BoolInt] = None
    count: Optional[int] = None
    replies: Optional[List["CommentRepliesItem"]]


class CommentRepliesItem(BaseObject):
    """VK Object widgets/CommentRepliesItem"""

    cid: Optional[int] = None
    date: Optional[int] = None
    likes: Optional["WidgetLikes"]
    text: Optional[str] = None
    uid: Optional[int] = None
    user: Optional[users.UserFull] = None


class WidgetComment(BaseObject):
    """VK Object widgets/WidgetComment"""

    attachments: Optional[List[wall.CommentAttachment]] = None
    can_delete: Optional[base.BoolInt] = None
    comments: Optional["CommentReplies"]
    date: Optional[int] = None
    from_id: Optional[int] = None
    id: Optional[int] = None
    likes: Optional[base.LikesInfo] = None
    media: Optional["CommentMedia"]
    post_source: Optional[wall.PostSource] = None
    post_type: Optional[int] = None
    reposts: Optional[base.RepostsInfo] = None
    text: Optional[str] = None
    to_id: Optional[int] = None
    user: Optional[users.UserFull] = None


class WidgetLikes(BaseObject):
    """VK Object widgets/WidgetLikes"""

    count: Optional[int] = None


class WidgetPage(BaseObject):
    """VK Object widgets/WidgetPage"""

    comments: Optional[base.ObjectCount] = None
    date: Optional[int] = None
    description: Optional[str] = None
    id: Optional[int] = None
    likes: Optional[base.ObjectCount] = None
    page_id: Optional[str] = None
    photo: Optional[str] = None
    title: Optional[str] = None
    url: Optional[str] = None
