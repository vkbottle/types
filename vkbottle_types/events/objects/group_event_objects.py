import inspect
from typing import Any, Optional

from vkbottle_types.objects import (
    AudioAudio,
    BaseBoolInt,
    BoardTopicComment,
    CallbackGroupJoinType,
    CallbackGroupMarket,
    CallbackGroupOfficerRole,
    CallbackLikeAddRemoveObjectType,
    ClientInfoForBots,
    GroupsGroupAudio,
    GroupsGroupFullAgeLimits,
    GroupsGroupIsClosed,
    GroupsGroupPhotos,
    GroupsGroupVideo,
    GroupsGroupWall,
    MarketOrder,
    MessagesMessage,
    PhotosPhoto,
    VideoVideo,
    WallWallComment,
    WallWallpostFull,
)

from .base_event_object import BaseEventObject


class MessageNewObject(BaseEventObject):
    client_info: Optional["ClientInfoForBots"] = None
    message: Optional["MessagesMessage"] = None


class MessageReplyObject(BaseEventObject, MessagesMessage):
    pass


class MessageEditObject(BaseEventObject, MessagesMessage):
    pass


class MessageAllowObject(BaseEventObject):
    key: str
    user_id: int


class MessageDenyObject(BaseEventObject):
    user_id: int


class MessageTypingStateObject(BaseEventObject):
    state: Optional[str] = None
    from_id: Optional[int] = None
    to_id: Optional[int] = None


class MessageEventObject(BaseEventObject):
    user_id: int
    peer_id: int
    event_id: str
    payload: Optional[dict] = None
    conversation_message_id: Optional[int] = None


class PhotoNewObject(BaseEventObject, PhotosPhoto):
    pass


class PhotoCommentNewObject(BaseEventObject, WallWallComment):
    photo_id: int
    photo_owner_id: int


class PhotoCommentEditObject(PhotoCommentNewObject):
    pass


class PhotoCommentRestoreObject(PhotoCommentNewObject):
    pass


class PhotoCommentDeleteObject(BaseEventObject):
    id: int
    owner_id: int
    photo_id: int
    user_id: int


class AudioNewObject(BaseEventObject, AudioAudio):
    pass


class VideoNewObject(BaseEventObject, VideoVideo):
    pass


class VideoCommentNewObject(BaseEventObject, WallWallComment):
    video_id: int
    video_owner_id: int


class VideoCommentEditObject(VideoCommentNewObject):
    pass


class VideoCommentRestoreObject(VideoCommentNewObject):
    pass


class VideoCommentDeleteObject(BaseEventObject):
    id: int
    deleter_id: int
    owner_id: int
    user_id: int
    video_id: int


class WallPostNewObject(BaseEventObject, WallWallpostFull):
    postponed_id: Optional[int] = None


class WallRepostObject(WallPostNewObject):
    pass


class WallReplyNewObject(BaseEventObject, WallWallComment):
    post_id: Optional[int] = None
    post_owner_id: Optional[int] = None


class WallReplyEditObject(WallReplyNewObject):
    pass


class WallReplyRestoreObject(WallReplyNewObject):
    pass


class WallReplyDeleteObject(BaseEventObject):
    owner_id: Optional[int] = None
    id: Optional[int] = None
    deleter_id: Optional[int] = None
    post_id: Optional[int] = None


class LikeAddObject(BaseEventObject):
    liker_id: int
    object_id: int
    object_owner_id: int
    object_type: Optional["CallbackLikeAddRemoveObjectType"] = None
    post_id: int
    thread_reply_id: Optional[int] = None


class LikeRemoveObject(LikeAddObject):
    pass


class BoardPostNewObject(BaseEventObject, BoardTopicComment):
    topic_id: Optional[int] = None
    topic_owner_id: Optional[int] = None


class BoardPostEditObject(BoardPostNewObject):
    pass


class BoardPostRestoreObject(BoardPostNewObject):
    pass


class BoardPostDeleteObject(BaseEventObject):
    id: int
    topic_id: int
    topic_owner_id: int


class MarketCommentNewObject(BaseEventObject):
    date: int
    from_id: int
    id: int
    market_owner_id: Optional[int] = None
    photo_id: Optional[int] = None
    text: Optional[str] = None


class MarketCommentEditObject(MarketCommentNewObject):
    pass


class MarketCommentRestoreObject(MarketCommentNewObject):
    pass


class MarketCommentDeleteObject(BaseEventObject):
    id: int
    item_id: int
    owner_id: int
    user_id: int


class MarketOrderNewObject(BaseEventObject, MarketOrder):
    pass


class MarketOrderEditObject(MarketOrderNewObject):
    pass


class GroupLeaveObject(BaseEventObject):
    self: Optional["BaseBoolInt"] = None
    user_id: Optional[int] = None


class GroupJoinObject(BaseEventObject):
    join_type: "CallbackGroupJoinType"
    user_id: int


class UserBlockObject(BaseEventObject):
    admin_id: int
    comment: Optional[str] = None
    reason: int
    unblock_date: int
    user_id: int


class UserUnblockObject(BaseEventObject):
    admin_id: int
    by_end_date: int
    user_id: int


class PollVoteNewObject(BaseEventObject):
    option_id: int
    owner_id: int
    poll_id: int
    user_id: int


class GroupOfficersEditObject(BaseEventObject):
    admin_id: int
    level_new: "CallbackGroupOfficerRole"
    level_old: "CallbackGroupOfficerRole"
    user_id: int


class GroupSettingsChangesObject(BaseEventObject):
    access: Optional["GroupsGroupIsClosed"] = None
    age_limits: Optional["GroupsGroupFullAgeLimits"] = None
    description: Optional[str] = None
    enable_audio: Optional["GroupsGroupAudio"] = None
    enable_market: Optional["CallbackGroupMarket"] = None
    enable_photo: Optional["GroupsGroupPhotos"] = None
    enable_status_default: Optional["GroupsGroupWall"] = None
    enable_video: Optional["GroupsGroupVideo"] = None
    public_category: Optional[int] = None
    public_subcategory: Optional[int] = None
    screen_name: Optional[str] = None
    title: Optional[str] = None
    website: Optional[str] = None
    old_value: Any
    new_value: Any


class GroupChangeSettingsObject(BaseEventObject):
    changes: Optional[GroupSettingsChangesObject] = None
    user_id: int


class GroupChangePhotoObject(BaseEventObject):
    photo: "PhotosPhoto"
    user_id: int


class VkpayTransactionObject(BaseEventObject):
    amount: Optional[int] = None
    date: Optional[int] = None
    description: Optional[str] = None
    from_id: Optional[int] = None


class AppPayloadObject(BaseEventObject):
    user_id: Optional[int] = None
    app_id: Optional[int] = None
    payload: Optional[str] = None
    group_id: Optional[int] = None


class DonutSubscriptionCreateObject(BaseEventObject):
    amount: int
    amount_without_fee: float
    user_id: Optional[int] = None


class DonutSubscriptionProlongedObject(BaseEventObject):
    pass


class DonutSubscriptionExpiredObject(BaseEventObject):
    user_id: Optional[int] = None


class DonutSubscriptionCancelledObject(BaseEventObject):
    user_id: Optional[int] = None


class DonutSubscriptionPriceChangedObject(BaseEventObject):
    amount_diff: Optional[float] = None
    amount_diff_without_fee: Optional[float] = None
    amount_new: int
    amount_old: int
    user_id: Optional[int] = None


class DonutMoneyWithdrawObject(BaseEventObject):
    amount: float
    amount_without_fee: float


class DonutMoneyWithdrawErrorObject(BaseEventObject):
    reason: str


_locals = locals().copy()
_locals_values = _locals.values()
for item in _locals_values:
    if inspect.isclass(item) and issubclass(item, BaseEventObject):
        item.update_forward_refs()
