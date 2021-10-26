import inspect
from typing import Any, Callable, Optional, Union

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
    WallWallpost,
)

from .base_event_object import BaseEventObject


class MessageNewObject(BaseEventObject):
    client_info: Optional["ClientInfoForBots"] = None
    message: Optional["MessagesMessage"] = None


class MessageReplyObject(MessagesMessage):
    pass


class MessageEditObject(MessagesMessage):
    pass


class MessageAllowObject(BaseEventObject):
    key: str = None
    user_id: int = None


class MessageDenyObject(BaseEventObject):
    user_id: int = None


class MessageTypingStateObject(BaseEventObject):
    state: Optional[str] = None
    from_id: Optional[int] = None
    to_id: Optional[int] = None


class MessageEventObject(BaseEventObject):
    user_id: Optional[int] = None
    peer_id: Optional[int] = None
    event_id: Optional[str] = None
    payload: Optional[Union[dict, str, Any]] = None
    conversation_message_id: Optional[int] = None

    @property
    def chat_id(self) -> int:
        return self.peer_id - 2_000_000_000

    def get_payload_json(
        self,
        throw_error: bool = False,
        unpack_failure: Callable[[str], dict] = lambda payload: payload,
        json: Any = __import__("json"),
    ) -> Union[dict, None]:
        try:
            return json.loads(self.payload)
        except (json.decoder.JSONDecodeError, TypeError) as e:
            if throw_error:
                raise e
        return unpack_failure(self.payload)


class PhotoNewObject(PhotosPhoto):
    pass


class PhotoCommentNewObject(BaseEventObject):
    date: int = None
    from_id: int = None
    id: int = None
    photo_owner_id: int = None
    text: str = None


class PhotoCommentEditObject(PhotoCommentNewObject):
    pass


class PhotoCommentRestoreObject(PhotoCommentNewObject):
    pass


class PhotoCommentDeleteObject(BaseEventObject):
    id: int = None
    owner_id: int = None
    photo_id: int = None
    user_id: int = None


class AudioNewObject(AudioAudio):
    pass


class VideoNewObject(VideoVideo):
    pass


class VideoCommentNewObject(BaseEventObject):
    date: int = None
    from_id: int = None
    id: int = None
    text: str = None
    video_owner_id: int = None


class VideoCommentEditObject(VideoCommentNewObject):
    pass


class VideoCommentRestoreObject(VideoCommentNewObject):
    pass


class VideoCommentDeleteObject(BaseEventObject):
    id: int = None
    owner_id: int = None
    user_id: int = None
    video_id: int = None


class WallPostNewObject(WallWallpost):
    postponed_id: Optional[int] = None


class WallRepostObject(WallWallpost):
    postponed_id: Optional[int] = None


class WallReplyNewObject(WallWallComment):
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
    liker_id: int = None
    object_id: int = None
    object_owner_id: int = None
    object_type: "CallbackLikeAddRemoveObjectType" = None
    post_id: int = None
    thread_reply_id: Optional[int] = None


class LikeRemoveObject(LikeAddObject):
    pass


class BoardPostNewObject(BoardTopicComment):
    topic_id: Optional[int] = None
    topic_owner_id: Optional[int] = None


class BoardPostEditObject(BoardPostNewObject):
    pass


class BoardPostRestoreObject(BoardPostNewObject):
    pass


class BoardPostDeleteObject(BaseEventObject):
    id: int = None
    topic_id: int = None
    topic_owner_id: int = None


class MarketCommentNewObject(BaseEventObject):
    date: int = None
    from_id: int = None
    id: int = None
    market_owner_id: Optional[int] = None
    photo_id: Optional[int] = None
    text: Optional[str] = None


class MarketCommentEditObject(MarketCommentNewObject):
    pass


class MarketCommentRestoreObject(MarketCommentNewObject):
    pass


class MarketCommentDeleteObject(BaseEventObject):
    id: int = None
    item_id: int = None
    owner_id: int = None
    user_id: int = None


class MarketOrderNewObject(MarketOrder):
    pass


class MarketOrderEditObject(MarketOrder):
    pass


class GroupLeaveObject(BaseEventObject):
    self: Optional["BaseBoolInt"] = None
    user_id: Optional[int] = None


class GroupJoinObject(BaseEventObject):
    join_type: "CallbackGroupJoinType" = None
    user_id: int = None


class UserBlockObject(BaseEventObject):
    admin_id: int = None
    comment: Optional[str] = None
    reason: int = None
    unblock_date: int = None
    user_id: int = None


class UserUnblockObject(BaseEventObject):
    admin_id: int = None
    by_end_date: int = None
    user_id: int = None


class PollVoteNewObject(BaseEventObject):
    option_id: int = None
    owner_id: int = None
    poll_id: int = None
    user_id: int = None


class GroupOfficersEditObject(BaseEventObject):
    admin_id: int = None
    level_new: "CallbackGroupOfficerRole" = None
    level_old: "CallbackGroupOfficerRole" = None
    user_id: int = None


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
    old_value: Any = None
    new_value: Any = None


class GroupChangeSettingsObject(BaseEventObject):
    changes: Optional[GroupSettingsChangesObject] = None
    user_id: int = None


class GroupChangePhotoObject(BaseEventObject):
    photo: "PhotosPhoto" = None
    user_id: int = None


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
    amount: int = None
    amount_without_fee: float = None
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
    amount_new: int = None
    amount_old: int = None
    user_id: Optional[int] = None


class DonutMoneyWithdrawObject(BaseEventObject):
    amount: float = None
    amount_without_fee: float = None


class DonutMoneyWithdrawErrorObject(BaseEventObject):
    reason: str = None


for item in locals().copy().values():
    if inspect.isclass(item) and issubclass(item, BaseEventObject):
        item.update_forward_refs()
