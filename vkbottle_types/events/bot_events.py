from typing import TYPE_CHECKING, Any, Optional, Union

from pydantic import BaseModel

from .enums import GroupEventType
from .events_base import EventsBase
from .objects import BaseEventObject, group_event_objects

if TYPE_CHECKING:
    from vkbottle import ABCAPI, API


class BaseGroupEvent(BaseModel):
    type: Optional[GroupEventType] = None
    object: Optional[BaseEventObject] = None
    group_id: Optional[int] = None
    unprepared_ctx_api: Optional[Any] = None

    @property
    def ctx_api(self) -> Optional[Union["ABCAPI", "API"]]:
        return getattr(self, "unprepared_ctx_api")


class Message(BaseGroupEvent):
    object: "group_event_objects.MessageObject"


class MessageNew(BaseGroupEvent):
    object: "group_event_objects.MessageNewObject"


class MessageAllow(BaseGroupEvent):
    object: "group_event_objects.MessageAllowObject"


class MessageTypingState(BaseGroupEvent):
    object: "group_event_objects.MessageTypingStateObject"


class MessageDeny(BaseGroupEvent):
    object: "group_event_objects.MessageDenyObject"


class MessageEvent(BaseGroupEvent):
    object: "group_event_objects.MessageEventObject"


class PhotoNew(BaseGroupEvent):
    object: "group_event_objects.PhotosPhoto"


class PhotoComment(BaseGroupEvent):
    object: "group_event_objects.PhotoCommentObject"


class PhotoCommentDelete(BaseGroupEvent):
    object: "group_event_objects.PhotoCommentDeleteObject"


class AudioNew(BaseGroupEvent):
    object: "group_event_objects.AudioNewObject"


class VideoNew(BaseGroupEvent):
    object: "group_event_objects.VideoNewObject"


class VideoComment(BaseGroupEvent):
    object: "group_event_objects.VideoCommentObject"


class VideoCommentDelete(BaseGroupEvent):
    object: "group_event_objects.VideoCommentDeleteObject"


class WallPostNew(BaseGroupEvent):
    object: "group_event_objects.WallPostNewObject"


class WallReply(BaseGroupEvent):
    object: "group_event_objects.WallReplyNewObject"


class WallReplyDelete(BaseGroupEvent):
    object: "group_event_objects.WallReplyDeleteObject"


class Like(BaseGroupEvent):
    object: "group_event_objects.LikeObject"


class BoardPost(BaseGroupEvent):
    object: "group_event_objects.BoardPostNewObject"


class BoardPostDelete(BaseGroupEvent):
    object: "group_event_objects.BoardPostDeleteObject"


class MarketOrder(BaseGroupEvent):
    object: "group_event_objects.MarketOrderObject"


class MarketComment(BaseGroupEvent):
    object: "group_event_objects.MarketCommentNewObject"


class MarketCommentDelete(BaseGroupEvent):
    object: "group_event_objects.MarketCommentDeleteObject"


class GroupLeave(BaseGroupEvent):
    object: "group_event_objects.GroupLeaveObject"


class GroupJoin(BaseGroupEvent):
    object: "group_event_objects.GroupJoinObject"


class UserBlock(BaseGroupEvent):
    object: "group_event_objects.UserBlockObject"


class UserUnblock(BaseGroupEvent):
    object: "group_event_objects.UserUnblockObject"


class PollVoteNew(BaseGroupEvent):
    object: "group_event_objects.PollVoteNewObject"


class GroupOfficersEdit(BaseGroupEvent):
    object: "group_event_objects.GroupOfficersEditObject"


class GroupChangeSettings(BaseGroupEvent):
    object: "group_event_objects.GroupChangeSettingsObject"


class GroupChangePhoto(BaseGroupEvent):
    object: "group_event_objects.GroupChangePhotoObject"


class VkPayTransaction(BaseGroupEvent):
    object: "group_event_objects.VkPayTransactionObject"


class AppPayload(BaseGroupEvent):
    object: "group_event_objects.AppPayloadObject"


class DonutSubscriptionCreate(BaseGroupEvent):
    object: "group_event_objects.DonutSubscriptionCreateObject"


class DonutSubscriptionProlonged(BaseGroupEvent):
    object: "group_event_objects.DonutSubscriptionProlongedObject"


class DonutSubscriptionExpired(BaseGroupEvent):
    object: "group_event_objects.DonutSubscriptionExpiredObject"


class DonutSubscriptionCancelled(BaseGroupEvent):
    object: "group_event_objects.DonutSubscriptionCancelledObject"


class DonutSubscriptionPriceChanged(BaseGroupEvent):
    object: "group_event_objects.DonutSubscriptionPriceChangedObject"


class DonutMoneyWithdraw(BaseGroupEvent):
    object: "group_event_objects.DonutMoneyWithdrawObject"


class DonutMoneyWithdrawError(BaseGroupEvent):
    object: "group_event_objects.DonutMoneyWithdrawErrorObject"


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
DonutSubscriptionCreate.update_forward_refs()
DonutSubscriptionProlonged.update_forward_refs()
DonutSubscriptionExpired.update_forward_refs()
DonutSubscriptionCancelled.update_forward_refs()
DonutSubscriptionPriceChanged.update_forward_refs()
DonutMoneyWithdraw.update_forward_refs()
DonutMoneyWithdrawError.update_forward_refs()

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
DEFAULT_EVENTS_BASE_GROUP.register(
    GroupEventType.DONUT_SUBSCRIPTION_CREATE, DonutSubscriptionCreate
)
DEFAULT_EVENTS_BASE_GROUP.register(
    GroupEventType.DONUT_SUBSCRIPTION_PROLONGED, DonutSubscriptionProlonged
)
DEFAULT_EVENTS_BASE_GROUP.register(
    GroupEventType.DONUT_SUBSCRIPTION_EXPIRED, DonutSubscriptionExpired
)
DEFAULT_EVENTS_BASE_GROUP.register(
    GroupEventType.DONUT_SUBSCRIPTION_CANCELLED, DonutSubscriptionCancelled
)
DEFAULT_EVENTS_BASE_GROUP.register(
    GroupEventType.DONUT_SUBSCRIPTION_PRICE_CHANGED, DonutSubscriptionPriceChanged
)
DEFAULT_EVENTS_BASE_GROUP.register(
    GroupEventType.DONUT_MONEY_WITHDRAW, DonutMoneyWithdraw
)
DEFAULT_EVENTS_BASE_GROUP.register(
    GroupEventType.DONUT_MONEY_WITHDRAW_ERROR, DonutMoneyWithdrawError
)

__all__ = (
    "DEFAULT_EVENTS_BASE_GROUP",
    "BaseGroupEvent",
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
    "DonutSubscriptionCreate",
    "DonutSubscriptionProlonged",
    "DonutSubscriptionExpired",
    "DonutSubscriptionCancelled",
    "DonutSubscriptionPriceChanged",
    "DonutMoneyWithdraw",
    "DonutMoneyWithdrawError",
)
