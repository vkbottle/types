from typing import Any

import pydantic

from vkbottle_types.base_model import BaseModel
from vkbottle_types.objects import *


class BaseEventObject(BaseModel):
    model_config = pydantic.ConfigDict(frozen=False)


class MessageNewObject(BaseEventObject):
    client_info: ClientInfoForBots | None = None
    message: MessagesMessage | None = None


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
    state: str | None = None
    from_id: int | None = None
    to_id: int | None = None


class MessageEventObject(BaseEventObject):
    user_id: int
    peer_id: int
    event_id: str
    payload: dict[str, Any] | None = None
    conversation_message_id: int | None = None


class PhotoNewObject(BaseEventObject, PhotosPhoto):
    pass


class PhotoCommentNewObject(BaseEventObject, WallWallComment):
    photo_id: int  # type: ignore
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
    video_id: int  # type: ignore
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
    postponed_id: int | None = None


class WallRepostObject(WallPostNewObject):
    pass


class WallReplyNewObject(BaseEventObject, WallWallComment):
    post_id: int | None = None
    post_owner_id: int | None = None


class WallReplyEditObject(WallReplyNewObject):
    pass


class WallReplyRestoreObject(WallReplyNewObject):
    pass


class WallReplyDeleteObject(BaseEventObject):
    owner_id: int | None = None
    id: int | None = None
    deleter_id: int | None = None
    post_id: int | None = None


class LikeAddObject(BaseEventObject):
    liker_id: int
    object_id: int
    object_owner_id: int
    object_type: CallbackLikeAddRemoveObjectType | None = None
    post_id: int
    thread_reply_id: int | None = None


class LikeRemoveObject(LikeAddObject):
    pass


class LeadFormAnswerModel(BaseModel):
    key: str
    question: str
    answer: str | None = None


class LeadFormsNewObject(BaseEventObject):
    lead_id: int
    group_id: int
    form_id: int
    user_id: int
    form_name: str
    answers: list[LeadFormAnswerModel] | None = None


class BoardPostNewObject(BaseEventObject, BoardTopicComment):
    topic_id: int | None = None
    topic_owner_id: int | None = None


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
    market_owner_id: int | None = None
    photo_id: int | None = None
    text: str | None = None


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
    self: bool | None = None
    user_id: int | None = None


class GroupJoinObject(BaseEventObject):
    join_type: CallbackGroupJoinType
    user_id: int


class UserBlockObject(BaseEventObject):
    admin_id: int
    comment: str | None = None
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
    level_new: CallbackGroupOfficerRole
    level_old: CallbackGroupOfficerRole
    user_id: int


class GroupSettingsChangesObject(BaseEventObject):
    access: GroupsGroupIsClosed | None = None
    age_limits: GroupsGroupFullAgeLimits | None = None
    description: str | None = None
    enable_audio: GroupsGroupAudio | None = None
    enable_market: CallbackGroupMarket | None = None
    enable_photo: GroupsGroupPhotos | None = None
    enable_status_default: GroupsGroupWall | None = None
    enable_video: GroupsGroupVideo | None = None
    public_category: int | None = None
    public_subcategory: int | None = None
    screen_name: str | None = None
    title: str | None = None
    website: str | None = None
    old_value: Any
    new_value: Any


class GroupChangeSettingsObject(BaseEventObject):
    changes: GroupSettingsChangesObject | None = None
    user_id: int


class GroupChangePhotoObject(BaseEventObject):
    photo: PhotosPhoto
    user_id: int


class VkpayTransactionObject(BaseEventObject):
    amount: int | None = None
    date: int | None = None
    description: str | None = None
    from_id: int | None = None


class AppPayloadObject(BaseEventObject):
    user_id: int | None = None
    app_id: int | None = None
    payload: str | None = None
    group_id: int | None = None


class DonutSubscriptionCreateObject(BaseEventObject):
    amount: int
    amount_without_fee: float
    user_id: int | None = None


class DonutSubscriptionProlongedObject(BaseEventObject):
    pass


class DonutSubscriptionExpiredObject(BaseEventObject):
    user_id: int | None = None


class DonutSubscriptionCancelledObject(BaseEventObject):
    user_id: int | None = None


class DonutSubscriptionPriceChangedObject(BaseEventObject):
    amount_diff: float | None = None
    amount_diff_without_fee: float | None = None
    amount_new: int
    amount_old: int
    user_id: int | None = None


class DonutMoneyWithdrawObject(BaseEventObject):
    amount: float
    amount_without_fee: float


class DonutMoneyWithdrawErrorObject(BaseEventObject):
    reason: str


class MessageReactionEventObject(BaseEventObject):
    reacted_id: int
    peer_id: int
    cmid: int
    reaction_id: int | None = None


class MessageReadObject(BaseEventObject):
    from_id: int
    peer_id: int
    read_message_id: int
    conversation_message_id: int


__all__ = (
    "AppPayloadObject",
    "AudioNewObject",
    "BoardPostDeleteObject",
    "BoardPostEditObject",
    "BoardPostNewObject",
    "BoardPostRestoreObject",
    "ClientInfoForBots",
    "DonutMoneyWithdrawErrorObject",
    "DonutMoneyWithdrawObject",
    "DonutSubscriptionCancelledObject",
    "DonutSubscriptionCreateObject",
    "DonutSubscriptionExpiredObject",
    "DonutSubscriptionPriceChangedObject",
    "DonutSubscriptionProlongedObject",
    "GroupChangePhotoObject",
    "GroupChangeSettingsObject",
    "GroupLeaveObject",
    "GroupOfficersEditObject",
    "GroupSettingsChangesObject",
    "LeadFormsNewObject",
    "LikeAddObject",
    "LikeRemoveObject",
    "MarketCommentDeleteObject",
    "MarketCommentEditObject",
    "MarketCommentNewObject",
    "MarketCommentRestoreObject",
    "MarketOrderEditObject",
    "MarketOrderNewObject",
    "MessageAllowObject",
    "MessageDenyObject",
    "MessageEditObject",
    "MessageEventObject",
    "MessageNewObject",
    "MessageReactionEventObject",
    "MessageReadObject",
    "MessageReplyObject",
    "MessageTypingStateObject",
    "PhotoCommentDeleteObject",
    "PhotoCommentEditObject",
    "PhotoCommentNewObject",
    "PhotoCommentRestoreObject",
    "PhotoNewObject",
    "PollVoteNewObject",
    "UserBlockObject",
    "UserUnblockObject",
    "VideoCommentDeleteObject",
    "VideoCommentEditObject",
    "VideoCommentNewObject",
    "VideoCommentRestoreObject",
    "VideoNewObject",
    "WallPostNewObject",
    "WallReplyDeleteObject",
    "WallReplyEditObject",
    "WallReplyNewObject",
    "WallReplyRestoreObject",
    "WallRepostObject",
)
