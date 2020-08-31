from .enums import GroupEventType
from .objects import BaseEventObject, group_event_objects
from .events_base import EventsBase
from pydantic import BaseModel
from typing import Optional


class BaseBotEvent(BaseModel):
    type: Optional[GroupEventType] = None
    object: Optional[BaseEventObject] = None
    group_id: Optional[int] = None


class Message(BaseBotEvent):
    object: "group_event_objects.MessageObject"


class MessageNew(BaseBotEvent):
    object: "group_event_objects.MessageNewObject"


class MessageAllow(BaseBotEvent):
    object: "group_event_objects.MessageAllowObject"


class MessageTypingState(BaseBotEvent):
    object: "group_event_objects.MessageTypingStateObject"


class MessageDeny(BaseBotEvent):
    object: "group_event_objects.MessageDenyObject"


class MessageEvent(BaseBotEvent):
    object: "group_event_objects.MessageEventObject"


class PhotoNew(BaseBotEvent):
    object: "group_event_objects.PhotosPhoto"


class PhotoComment(BaseBotEvent):
    object: "group_event_objects.PhotoCommentObject"


class PhotoCommentDelete(BaseBotEvent):
    object: "group_event_objects.PhotoCommentDeleteObject"


class AudioNew(BaseBotEvent):
    object: "group_event_objects.AudioNewObject"


class VideoNew(BaseBotEvent):
    object: "group_event_objects.VideoNewObject"


class VideoComment(BaseBotEvent):
    object: "group_event_objects.VideoCommentObject"


class VideoCommentDelete(BaseBotEvent):
    object: "group_event_objects.VideoCommentDeleteObject"


class WallPostNew(BaseBotEvent):
    object: "group_event_objects.WallPostNewObject"


class WallReply(BaseBotEvent):
    object: "group_event_objects.WallReplyNewObject"


class WallReplyDelete(BaseBotEvent):
    object: "group_event_objects.WallReplyDeleteObject"


class Like(BaseBotEvent):
    object: "group_event_objects.LikeObject"


class BoardPost(BaseBotEvent):
    object: "group_event_objects.BoardPostNewObject"


class BoardPostDelete(BaseBotEvent):
    object: "group_event_objects.BoardPostDeleteObject"


class MarketOrder(BaseBotEvent):
    object: "group_event_objects.MarketOrderObject"


class MarketComment(BaseBotEvent):
    object: "group_event_objects.MarketCommentNewObject"


class MarketCommentDelete(BaseBotEvent):
    object: "group_event_objects.MarketCommentDeleteObject"


class GroupLeave(BaseBotEvent):
    object: "group_event_objects.GroupLeaveObject"


class GroupJoin(BaseBotEvent):
    object: "group_event_objects.GroupJoinObject"


class UserBlock(BaseBotEvent):
    object: "group_event_objects.UserBlockObject"


class UserUnblock(BaseBotEvent):
    object: "group_event_objects.UserUnblockObject"


class PollVoteNew(BaseBotEvent):
    object: "group_event_objects.PollVoteNewObject"


class GroupOfficersEdit(BaseBotEvent):
    object: "group_event_objects.GroupOfficersEditObject"


class GroupChangeSettings(BaseBotEvent):
    object: "group_event_objects.GroupChangeSettingsObject"


class GroupChangePhoto(BaseBotEvent):
    object: "group_event_objects.GroupChangePhotoObject"


class VkPayTransaction(BaseBotEvent):
    object: "group_event_objects.VkPayTransactionObject"


class AppPayload(BaseBotEvent):
    object: "group_event_objects.AppPayloadObject"


Message.update_forward_refs()
MessageNew.update_forward_refs()
MessageAllow.update_forward_refs()
MessageTypingState.update_forward_refs()
MessageDeny.update_forward_refs()
PhotoNew.update_forward_refs()
PhotoComment.update_forward_refs()
PhotoCommentDelete.update_forward_refs()
VideoComment.update_forward_refs()
VideoCommentDelete.update_forward_refs()
WallPostNew.update_forward_refs()
WallReply.update_forward_refs()
WallReplyDelete.update_forward_refs()
BoardPost.update_forward_refs()
BoardPostDelete.update_forward_refs()
MarketComment.update_forward_refs()
MarketCommentDelete.update_forward_refs()
GroupLeave.update_forward_refs()
GroupJoin.update_forward_refs()
UserBlock.update_forward_refs()
UserUnblock.update_forward_refs()
PollVoteNew.update_forward_refs()
GroupOfficersEdit.update_forward_refs()
GroupChangeSettings.update_forward_refs()
GroupChangePhoto.update_forward_refs()
VkPayTransaction.update_forward_refs()
AppPayload.update_forward_refs()

DEFAULT_EVENTS_BASE_GROUP = EventsBase(GroupEventType)
DEFAULT_EVENTS_BASE_GROUP.register(GroupEventType.MESSAGE_NEW, MessageNew)
DEFAULT_EVENTS_BASE_GROUP.register(GroupEventType.MESSAGE_REPLY, Message)
DEFAULT_EVENTS_BASE_GROUP.register(GroupEventType.MESSAGE_EDIT, Message)
DEFAULT_EVENTS_BASE_GROUP.register(GroupEventType.MESSAGE_ALLOW, MessageAllow)
DEFAULT_EVENTS_BASE_GROUP.register(
    GroupEventType.MESSAGE_TYPING_STATE, MessageTypingState
)
DEFAULT_EVENTS_BASE_GROUP.register(GroupEventType.MESSAGE_DENY, MessageDeny)
DEFAULT_EVENTS_BASE_GROUP.register(GroupEventType.MESSAGE_EVENT, MessageEvent)
DEFAULT_EVENTS_BASE_GROUP.register(GroupEventType.PHOTO_NEW, PhotoNew)
DEFAULT_EVENTS_BASE_GROUP.register(GroupEventType.PHOTO_COMMENT_NEW, PhotoComment)
DEFAULT_EVENTS_BASE_GROUP.register(GroupEventType.PHOTO_COMMENT_EDIT, PhotoComment)
DEFAULT_EVENTS_BASE_GROUP.register(GroupEventType.PHOTO_COMMENT_RESTORE, PhotoComment)
DEFAULT_EVENTS_BASE_GROUP.register(
    GroupEventType.PHOTO_COMMENT_DELETE, PhotoCommentDelete
)
DEFAULT_EVENTS_BASE_GROUP.register(GroupEventType.AUDIO_NEW, AudioNew)
DEFAULT_EVENTS_BASE_GROUP.register(GroupEventType.VIDEO_NEW, VideoNew)
DEFAULT_EVENTS_BASE_GROUP.register(GroupEventType.VIDEO_COMMENT_NEW, VideoComment)
DEFAULT_EVENTS_BASE_GROUP.register(GroupEventType.VIDEO_COMMENT_EDIT, VideoComment)
DEFAULT_EVENTS_BASE_GROUP.register(GroupEventType.VIDEO_COMMENT_RESTORE, VideoComment)
DEFAULT_EVENTS_BASE_GROUP.register(
    GroupEventType.VIDEO_COMMENT_DELETE, VideoCommentDelete
)
DEFAULT_EVENTS_BASE_GROUP.register(GroupEventType.WALL_POST_NEW, WallPostNew)
DEFAULT_EVENTS_BASE_GROUP.register(GroupEventType.WALL_REPOST, WallPostNew)
DEFAULT_EVENTS_BASE_GROUP.register(GroupEventType.WALL_REPLY_NEW, WallReply)
DEFAULT_EVENTS_BASE_GROUP.register(GroupEventType.WALL_REPLY_EDIT, WallReply)
DEFAULT_EVENTS_BASE_GROUP.register(GroupEventType.WALL_REPLY_RESTORE, WallReply)
DEFAULT_EVENTS_BASE_GROUP.register(GroupEventType.WALL_REPLY_DELETE, WallReplyDelete)
DEFAULT_EVENTS_BASE_GROUP.register(GroupEventType.LIKE_ADD, Like)
DEFAULT_EVENTS_BASE_GROUP.register(GroupEventType.LIKE_REMOVE, Like)
DEFAULT_EVENTS_BASE_GROUP.register(GroupEventType.BOARD_POST_NEW, BoardPost)
DEFAULT_EVENTS_BASE_GROUP.register(GroupEventType.BOARD_POST_EDIT, BoardPost)
DEFAULT_EVENTS_BASE_GROUP.register(GroupEventType.BOARD_POST_RESTORE, BoardPost)
DEFAULT_EVENTS_BASE_GROUP.register(GroupEventType.BOARD_POST_DELETE, BoardPostDelete)
DEFAULT_EVENTS_BASE_GROUP.register(GroupEventType.MARKET_ORDER_NEW, MarketOrder)
DEFAULT_EVENTS_BASE_GROUP.register(GroupEventType.MARKET_ORDER_EDIT, MarketOrder)
DEFAULT_EVENTS_BASE_GROUP.register(GroupEventType.BOARD_POST_DELETE, BoardPostDelete)
DEFAULT_EVENTS_BASE_GROUP.register(GroupEventType.MARKET_COMMENT_NEW, MarketComment)
DEFAULT_EVENTS_BASE_GROUP.register(GroupEventType.MARKET_COMMENT_EDIT, MarketComment)
DEFAULT_EVENTS_BASE_GROUP.register(GroupEventType.MARKET_COMMENT_RESTORE, MarketComment)
DEFAULT_EVENTS_BASE_GROUP.register(
    GroupEventType.MARKET_COMMENT_DELETE, MarketCommentDelete
)
DEFAULT_EVENTS_BASE_GROUP.register(GroupEventType.GROUP_LEAVE, GroupLeave)
DEFAULT_EVENTS_BASE_GROUP.register(GroupEventType.GROUP_JOIN, GroupJoin)
DEFAULT_EVENTS_BASE_GROUP.register(GroupEventType.USER_BLOCK, UserBlock)
DEFAULT_EVENTS_BASE_GROUP.register(GroupEventType.USER_UNBLOCK, UserUnblock)
DEFAULT_EVENTS_BASE_GROUP.register(GroupEventType.POLL_VOTE_NEW, PollVoteNew)
DEFAULT_EVENTS_BASE_GROUP.register(
    GroupEventType.GROUP_OFFICERS_EDIT, GroupOfficersEdit
)
DEFAULT_EVENTS_BASE_GROUP.register(
    GroupEventType.GROUP_CHANGE_SETTINGS, GroupChangeSettings
)
DEFAULT_EVENTS_BASE_GROUP.register(GroupEventType.GROUP_CHANGE_PHOTO, GroupChangePhoto)
DEFAULT_EVENTS_BASE_GROUP.register(GroupEventType.VKPAY_TRANSACTION, VkPayTransaction)
DEFAULT_EVENTS_BASE_GROUP.register(GroupEventType.APP_PAYLOAD, AppPayload)

__all__ = (
    "DEFAULT_EVENTS_BASE_GROUP",
    "MessageNew",
    "Message",
    "MessageAllow",
    "MessageTypingState",
    "MessageDeny",
    "MessageEvent",
    "PhotoNew",
    "PhotoComment",
    "PhotoCommentDelete",
    "AudioNew",
    "VideoNew",
    "VideoComment",
    "VideoCommentDelete",
    "WallPostNew",
    "WallReply",
    "WallReplyDelete",
    "Like",
    "BoardPost",
    "BoardPostDelete",
    "MarketComment",
    "MarketCommentDelete",
    "GroupJoin",
    "GroupLeave",
    "UserBlock",
    "UserUnblock",
    "PollVoteNew",
    "GroupOfficersEdit",
    "GroupChangeSettings",
    "GroupChangePhoto",
    "VkPayTransaction",
    "AppPayload",
)
