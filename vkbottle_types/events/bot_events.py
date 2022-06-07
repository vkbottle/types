import inspect
from typing import TYPE_CHECKING, Any, Optional, Union

from pydantic import BaseModel

from .enums import GroupEventType
from .events_base import EventsBase
from .objects import BaseEventObject, group_event_objects

if TYPE_CHECKING:
    from vkbottle import ABCAPI, API


class BaseGroupEvent(BaseModel):
    type: Optional[GroupEventType] = None
    object: Optional["BaseEventObject"] = None
    secret: Optional[str] = None
    event_id: Optional[str] = None
    group_id: Optional[int] = None
    unprepared_ctx_api: Optional[Any] = None

    @property
    def ctx_api(self) -> Optional[Union["ABCAPI", "API"]]:
        return getattr(self, "unprepared_ctx_api")


class MessageNew(BaseGroupEvent):
    object: group_event_objects.MessageNewObject


class MessageReply(BaseGroupEvent):
    object: group_event_objects.MessageReplyObject


class MessageEdit(BaseGroupEvent):
    object: group_event_objects.MessageEditObject


class MessageAllow(BaseGroupEvent):
    object: group_event_objects.MessageAllowObject


class MessageDeny(BaseGroupEvent):
    object: group_event_objects.MessageDenyObject


class MessageTypingState(BaseGroupEvent):
    object: group_event_objects.MessageTypingStateObject


class MessageEvent(BaseGroupEvent):
    object: group_event_objects.MessageEventObject


class PhotoNew(BaseGroupEvent):
    object: group_event_objects.PhotoNewObject


class PhotoCommentNew(BaseGroupEvent):
    object: group_event_objects.PhotoCommentNewObject


class PhotoCommentEdit(BaseGroupEvent):
    object: group_event_objects.PhotoCommentNewObject


class PhotoCommentRestore(BaseGroupEvent):
    object: group_event_objects.PhotoCommentRestoreObject


class PhotoCommentDelete(BaseGroupEvent):
    object: group_event_objects.PhotoCommentDeleteObject


class AudioNew(BaseGroupEvent):
    object: group_event_objects.AudioNewObject


class VideoNew(BaseGroupEvent):
    object: group_event_objects.VideoNewObject


class VideoCommentNew(BaseGroupEvent):
    object: group_event_objects.VideoCommentNewObject


class VideoCommentEdit(BaseGroupEvent):
    object: group_event_objects.VideoCommentEditObject


class VideoCommentRestore(BaseGroupEvent):
    object: group_event_objects.VideoCommentRestoreObject


class VideoCommentDelete(BaseGroupEvent):
    object: group_event_objects.VideoCommentDeleteObject


class WallPostNew(BaseGroupEvent):
    object: group_event_objects.WallPostNewObject


class WallRepost(BaseGroupEvent):
    object: group_event_objects.WallRepostObject


class WallReplyNew(BaseGroupEvent):
    object: group_event_objects.WallReplyNewObject


class WallReplyEdit(BaseGroupEvent):
    object: group_event_objects.WallReplyRestoreObject


class WallReplyRestore(BaseGroupEvent):
    object: group_event_objects.WallReplyRestoreObject


class WallReplyDelete(BaseGroupEvent):
    object: group_event_objects.WallReplyDeleteObject


class LikeAdd(BaseGroupEvent):
    object: group_event_objects.LikeAddObject


class LikeRemove(BaseGroupEvent):
    object: group_event_objects.LikeRemoveObject


class BoardPostNew(BaseGroupEvent):
    object: group_event_objects.BoardPostNewObject


class BoardPostEdit(BaseGroupEvent):
    object: group_event_objects.BoardPostEditObject


class BoardPostRestore(BaseGroupEvent):
    object: group_event_objects.BoardPostRestoreObject


class BoardPostDelete(BaseGroupEvent):
    object: group_event_objects.BoardPostDeleteObject


class MarketCommentNew(BaseGroupEvent):
    object: group_event_objects.MarketCommentNewObject


class MarketCommentEdit(BaseGroupEvent):
    object: group_event_objects.MarketCommentEditObject


class MarketCommentRestore(BaseGroupEvent):
    object: group_event_objects.MarketCommentRestoreObject


class MarketCommentDelete(BaseGroupEvent):
    object: group_event_objects.MarketCommentDeleteObject


class MarketOrderNew(BaseGroupEvent):
    object: group_event_objects.MarketOrderNewObject


class MarketOrderEdit(BaseGroupEvent):
    object: group_event_objects.MarketOrderEditObject


class GroupLeave(BaseGroupEvent):
    object: group_event_objects.GroupLeaveObject


class GroupJoin(BaseGroupEvent):
    object: group_event_objects.GroupJoinObject


class UserBlock(BaseGroupEvent):
    object: group_event_objects.UserBlockObject


class UserUnblock(BaseGroupEvent):
    object: group_event_objects.UserUnblockObject


class PollVoteNew(BaseGroupEvent):
    object: group_event_objects.PollVoteNewObject


class GroupOfficersEdit(BaseGroupEvent):
    object: group_event_objects.GroupOfficersEditObject


class GroupChangeSettings(BaseGroupEvent):
    object: group_event_objects.GroupChangeSettingsObject


class GroupChangePhoto(BaseGroupEvent):
    object: group_event_objects.GroupChangePhotoObject


class VkpayTransaction(BaseGroupEvent):
    object: group_event_objects.VkpayTransactionObject


class AppPayload(BaseGroupEvent):
    object: group_event_objects.AppPayloadObject


class DonutSubscriptionCreate(BaseGroupEvent):
    object: group_event_objects.DonutSubscriptionCreateObject


class DonutSubscriptionProlonged(BaseGroupEvent):
    object: group_event_objects.DonutSubscriptionProlongedObject


class DonutSubscriptionExpired(BaseGroupEvent):
    object: group_event_objects.DonutSubscriptionExpiredObject


class DonutSubscriptionCancelled(BaseGroupEvent):
    object: group_event_objects.DonutSubscriptionCancelledObject


class DonutSubscriptionPriceChanged(BaseGroupEvent):
    object: group_event_objects.DonutSubscriptionPriceChangedObject


class DonutMoneyWithdraw(BaseGroupEvent):
    object: group_event_objects.DonutMoneyWithdrawObject


class DonutMoneyWithdrawError(BaseGroupEvent):
    object: group_event_objects.DonutMoneyWithdrawErrorObject


DEFAULT_EVENTS_BASE_GROUP = EventsBase(GroupEventType)
_locals = locals().copy()
_locals_values = _locals.values()
for item in _locals_values:
    if (
        not inspect.isclass(item)
        or not issubclass(item, BaseGroupEvent)
        or item is BaseGroupEvent
    ):
        continue
    item.update_forward_refs(**_locals)
    event_type = GroupEventType[
        "".join(f"_{i}" if i.isupper() else i for i in item.__name__)
        .lstrip("_")
        .upper()
    ]

    DEFAULT_EVENTS_BASE_GROUP.register(event_type, item)

__all__ = (
    "DEFAULT_EVENTS_BASE_GROUP",
    "BaseGroupEvent",
    "MessageNew",
    "MessageReply",
    "MessageEdit",
    "MessageAllow",
    "MessageDeny",
    "MessageTypingState",
    "MessageEvent",
    "PhotoNew",
    "PhotoCommentNew",
    "PhotoCommentEdit",
    "PhotoCommentRestore",
    "PhotoCommentDelete",
    "AudioNew",
    "VideoNew",
    "VideoCommentNew",
    "VideoCommentEdit",
    "VideoCommentRestore",
    "VideoCommentDelete",
    "WallPostNew",
    "WallRepost",
    "WallReplyNew",
    "WallReplyEdit",
    "WallReplyRestore",
    "WallReplyDelete",
    "LikeAdd",
    "LikeRemove",
    "BoardPostNew",
    "BoardPostEdit",
    "BoardPostRestore",
    "BoardPostDelete",
    "MarketCommentNew",
    "MarketCommentEdit",
    "MarketCommentRestore",
    "MarketCommentDelete",
    "MarketOrderNew",
    "MarketOrderEdit",
    "GroupLeave",
    "GroupJoin",
    "UserBlock",
    "UserUnblock",
    "PollVoteNew",
    "GroupOfficersEdit",
    "GroupChangeSettings",
    "GroupChangePhoto",
    "VkpayTransaction",
    "AppPayload",
    "DonutSubscriptionCreate",
    "DonutSubscriptionProlonged",
    "DonutSubscriptionExpired",
    "DonutSubscriptionCancelled",
    "DonutSubscriptionPriceChanged",
    "DonutMoneyWithdraw",
    "DonutMoneyWithdrawError",
)
