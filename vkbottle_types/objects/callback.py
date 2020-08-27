from .base_model import BaseObject
from . import base, groups, photos
from typing import Optional, Union, Any, List
import typing
import enum


class BoardPostDelete(BaseObject):
    """VK Object callback/BoardPostDelete"""

    topic_owner_id: Optional[int] = None
    topic_id: Optional[int] = None
    id: Optional[int] = None


class ConfirmationMessage(BaseObject):
    """VK Object callback/ConfirmationMessage"""

    type: Optional["MessageType"]
    group_id: Optional[int] = None
    secret: Optional[str] = None


class GroupChangePhoto(BaseObject):
    """VK Object callback/GroupChangePhoto"""

    user_id: Optional[int] = None
    photo: Optional[photos.Photo] = None


class GroupChangeSettings(BaseObject):
    """VK Object callback/GroupChangeSettings"""

    user_id: Optional[int] = None
    self: Optional[base.BoolInt] = None


class GroupJoin(BaseObject):
    """VK Object callback/GroupJoin"""

    user_id: Optional[int] = None
    join_type: Optional["GroupJoinType"]


class GroupJoinType(enum.Enum):
    """ GroupJoinType enum """

    JOIN = "join"
    UNSURE = "unsure"
    ACCEPTED = "accepted"
    APPROVED = "approved"
    REQUEST = "request"


class GroupLeave(BaseObject):
    """VK Object callback/GroupLeave"""

    user_id: Optional[int] = None
    self: Optional[base.BoolInt] = None


class GroupMarket(enum.IntEnum):
    """ GroupMarket enum """

    disabled = 0
    open = 1


class GroupOfficerRole(enum.IntEnum):
    """ GroupOfficerRole enum """

    none = 0
    moderator = 1
    editor = 2
    administrator = 3


class GroupOfficersEdit(BaseObject):
    """VK Object callback/GroupOfficersEdit"""

    admin_id: Optional[int] = None
    user_id: Optional[int] = None
    level_old: Optional["GroupOfficerRole"]
    level_new: Optional["GroupOfficerRole"]


class GroupSettingsChanges(BaseObject):
    """VK Object callback/GroupSettingsChanges"""

    title: Optional[str] = None
    description: Optional[str] = None
    access: Optional[groups.GroupIsClosed] = None
    screen_name: Optional[str] = None
    public_category: Optional[int] = None
    public_subcategory: Optional[int] = None
    age_limits: Optional[groups.GroupFullAgeLimits] = None
    website: Optional[str] = None
    enable_status_default: Optional[groups.GroupWall] = None
    enable_audio: Optional[groups.GroupAudio] = None
    enable_video: Optional[groups.GroupVideo] = None
    enable_photo: Optional[groups.GroupPhotos] = None
    enable_market: Optional["GroupMarket"]


class LikeAddRemove(BaseObject):
    """VK Object callback/LikeAddRemove"""

    liker_id: Optional[int] = None
    object_type: Optional[str] = None
    object_owner_id: Optional[int] = None
    object_id: Optional[int] = None
    post_id: Optional[int] = None
    thread_reply_id: Optional[int] = None


class MarketComment(BaseObject):
    """VK Object callback/MarketComment"""

    id: Optional[int] = None
    from_id: Optional[int] = None
    date: Optional[int] = None
    text: Optional[str] = None
    market_owner_od: Optional[int] = None
    photo_id: Optional[int] = None


class MarketCommentDelete(BaseObject):
    """VK Object callback/MarketCommentDelete"""

    owner_id: Optional[int] = None
    id: Optional[int] = None
    user_id: Optional[int] = None
    item_id: Optional[int] = None


class MessageAllow(BaseObject):
    """VK Object callback/MessageAllow"""

    user_id: Optional[int] = None
    key: Optional[str] = None


class MessageBase(BaseObject):
    """VK Object callback/MessageBase"""

    type: Optional["MessageType"]
    object: Optional[typing.Dict[Any, Any]] = None
    group_id: Optional[int] = None


class MessageDeny(BaseObject):
    """VK Object callback/MessageDeny"""

    user_id: Optional[int] = None


class MessageType(enum.Enum):
    """ MessageType enum """

    CONFIRMATION = "confirmation"
    GROUP_CHANGE_PHOTO = "group_change_photo"
    GROUP_CHANGE_SETTINGS = "group_change_settings"
    GROUP_OFFICERS_EDIT = "group_officers_edit"
    LEAD_FORMS_NEW = "lead_forms_new"
    MARKET_COMMENT_DELETE = "market_comment_delete"
    MARKET_COMMENT_EDIT = "market_comment_edit"
    MARKET_COMMENT_RESTORE = "market_comment_restore"
    MESSAGE_ALLOW = "message_allow"
    MESSAGE_DENY = "message_deny"
    MESSAGE_READ = "message_read"
    MESSAGE_REPLY = "message_reply"
    MESSAGE_TYPING_STATE = "message_typing_state"
    MESSAGES_EDIT = "messages_edit"
    PHOTO_COMMENT_DELETE = "photo_comment_delete"
    PHOTO_COMMENT_EDIT = "photo_comment_edit"
    PHOTO_COMMENT_RESTORE = "photo_comment_restore"
    POLL_VOTE_NEW = "poll_vote_new"
    USER_BLOCK = "user_block"
    USER_UNBLOCK = "user_unblock"
    VIDEO_COMMENT_DELETE = "video_comment_delete"
    VIDEO_COMMENT_EDIT = "video_comment_edit"
    VIDEO_COMMENT_RESTORE = "video_comment_restore"
    WALL_REPLY_DELETE = "wall_reply_delete"
    WALL_REPLY_RESTORE = "wall_reply_restore"
    WALL_REPOST = "wall_repost"


class PhotoComment(BaseObject):
    """VK Object callback/PhotoComment"""

    id: Optional[int] = None
    from_id: Optional[int] = None
    date: Optional[int] = None
    text: Optional[str] = None
    photo_owner_od: Optional[int] = None


class PhotoCommentDelete(BaseObject):
    """VK Object callback/PhotoCommentDelete"""

    id: Optional[int] = None
    owner_id: Optional[int] = None
    user_id: Optional[int] = None
    photo_id: Optional[int] = None


class PollVoteNew(BaseObject):
    """VK Object callback/PollVoteNew"""

    owner_id: Optional[int] = None
    poll_id: Optional[int] = None
    option_id: Optional[int] = None
    user_id: Optional[int] = None


class QrScan(BaseObject):
    """VK Object callback/QrScan"""

    user_id: Optional[int] = None
    data: Optional[str] = None
    type: Optional[str] = None
    subtype: Optional[str] = None
    reread: Optional[bool] = None


class UserBlock(BaseObject):
    """VK Object callback/UserBlock"""

    admin_id: Optional[int] = None
    user_id: Optional[int] = None
    unblock_date: Optional[int] = None
    reason: Optional[int] = None
    comment: Optional[str] = None


class UserUnblock(BaseObject):
    """VK Object callback/UserUnblock"""

    admin_id: Optional[int] = None
    user_id: Optional[int] = None
    by_end_date: Optional[int] = None


class VideoComment(BaseObject):
    """VK Object callback/VideoComment"""

    id: Optional[int] = None
    from_id: Optional[int] = None
    date: Optional[int] = None
    text: Optional[str] = None
    video_owner_od: Optional[int] = None


class VideoCommentDelete(BaseObject):
    """VK Object callback/VideoCommentDelete"""

    id: Optional[int] = None
    owner_id: Optional[int] = None
    user_id: Optional[int] = None
    video_id: Optional[int] = None


class WallCommentDelete(BaseObject):
    """VK Object callback/WallCommentDelete"""

    owner_id: Optional[int] = None
    id: Optional[int] = None
    user_id: Optional[int] = None
    post_id: Optional[int] = None
