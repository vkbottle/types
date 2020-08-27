from .base_model import BaseObject
from . import wall, users, base
from typing import Optional, Union, Any, List
import typing
import enum


class CommentMedia(BaseObject):
    """VK Object widgets/CommentMedia"""

    item_id: Optional[int] = None
    owner_id: Optional[int] = None
    thumb_src: Optional[str] = None
    type: Optional["CommentMediaType"] = None


class CommentMediaType(enum.Enum):
    """ Media type """

    AUDIO = "audio"
    PHOTO = "photo"
    VIDEO = "video"


class CommentReplies(BaseObject):
    """VK Object widgets/CommentReplies

    can_post - Information whether current user can comment the post
    count - Comments number
    """

    can_post: Optional[base.BoolInt] = None
    count: Optional[int] = None
    replies: Optional[List["CommentRepliesItem"]] = None


class CommentRepliesItem(BaseObject):
    """VK Object widgets/CommentRepliesItem

    cid - Comment ID
    date - Date when the comment has been added in Unixtime
    text - Comment text
    uid - User ID
    """

    cid: Optional[int] = None
    date: Optional[int] = None
    likes: Optional["WidgetLikes"] = None
    text: Optional[str] = None
    uid: Optional[int] = None
    user: Optional[users.UserFull] = None


class WidgetComment(BaseObject):
    """VK Object widgets/WidgetComment

    can_delete - Information whether current user can delete the comment
    date - Date when the comment has been added in Unixtime
    from_id - Comment author ID
    id - Comment ID
    post_type - Post type
    text - Comment text
    to_id - Wall owner
    """

    attachments: Optional[List[wall.CommentAttachment]] = None
    can_delete: Optional[base.BoolInt] = None
    comments: Optional["CommentReplies"] = None
    date: Optional[int] = None
    from_id: Optional[int] = None
    id: Optional[int] = None
    likes: Optional[base.LikesInfo] = None
    media: Optional["CommentMedia"] = None
    post_source: Optional[wall.PostSource] = None
    post_type: Optional[int] = None
    reposts: Optional[base.RepostsInfo] = None
    text: Optional[str] = None
    to_id: Optional[int] = None
    user: Optional[users.UserFull] = None


class WidgetLikes(BaseObject):
    """VK Object widgets/WidgetLikes

    count - Likes number
    """

    count: Optional[int] = None


class WidgetPage(BaseObject):
    """VK Object widgets/WidgetPage

    date - Date when widgets on the page has been initialized firstly in Unixtime
    description - Page description
    id - Page ID
    page_id - page_id parameter value
    photo - URL of the preview image
    title - Page title
    url - Page absolute URL
    """

    comments: Optional[base.ObjectCount] = None
    date: Optional[int] = None
    description: Optional[str] = None
    id: Optional[int] = None
    likes: Optional[base.ObjectCount] = None
    page_id: Optional[str] = None
    photo: Optional[str] = None
    title: Optional[str] = None
    url: Optional[str] = None
