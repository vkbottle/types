import enum
from typing import Any, Callable, Optional, Union

from vkbottle_types.objects import (
    AudioAudio,
    BoardTopicComment,
    CallbackGroupJoinType,
    GroupsGroupAdminLevel,
    MarketOrder,
    MessagesClientInfo,
    MessagesMessage,
    ObjectType,
    PhotosPhoto,
    UsersBlockReason,
    VideoVideo,
    WallWallComment,
    WallWallpost,
)

from .base_event_object import BaseEventObject


class MessageNewObject(BaseEventObject):
    message: Optional[MessagesMessage] = None
    client_info: Optional[MessagesClientInfo] = None


class MessageObject(MessagesMessage):
    pass


class MessageAllowObject(BaseEventObject):
    user_id: Optional[int] = None
    key: Optional[str] = None
    api: Optional[list] = None


class MessageTypingStateObject(BaseEventObject):
    state: Optional[str] = None
    from_id: Optional[int] = None
    to_id: Optional[int] = None
    api: Optional[list] = None


class MessageDenyObject(BaseEventObject):
    user_id: Optional[int] = None


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


class PhotoCommentObject(WallWallComment):
    photo_id: Optional[int] = None
    photo_owner_id: Optional[int] = None


class PhotoCommentDeleteObject(BaseEventObject):
    owner_id: Optional[int] = None
    id: Optional[int] = None
    user_id: Optional[int] = None
    photo_id: Optional[int] = None


class AudioNewObject(AudioAudio):
    pass


class VideoNewObject(VideoVideo):
    pass


class VideoCommentObject(WallWallComment):
    video_id: Optional[int] = None
    video_owner_id: Optional[int] = None


class VideoCommentDeleteObject(BaseEventObject):
    owner_id: Optional[int] = None
    id: Optional[int] = None
    user_id: Optional[int] = None
    video_id: Optional[int] = None


class WallPostNewObject(WallWallpost):
    postponed_id: Optional[int] = None


class WallReplyNewObject(WallWallComment):
    post_id: Optional[int] = None
    post_owner_id: Optional[int] = None
    api: Optional[list] = None


class WallReplyDeleteObject(BaseEventObject):
    owner_id: Optional[int] = None
    id: Optional[int] = None
    user_id: Optional[int] = None
    deleter_id: Optional[int] = None
    post_id: Optional[int] = None


class LikeObject(BaseEventObject):
    liker_id: Optional[int] = None
    object_type: Optional[ObjectType] = None
    object_owner_id: Optional[int] = None
    object_id: Optional[int] = None
    thread_reply_id: Optional[int] = None
    post_id: Optional[int] = None


class BoardPostNewObject(BoardTopicComment):
    topic_id: Optional[int] = None
    topic_owner_id: Optional[int] = None


class BoardPostDeleteObject(BaseEventObject):
    topic_id: Optional[int] = None
    id: Optional[int] = None


class MarketCommentNewObject(WallWallComment):
    market_owner_id: Optional[int] = None
    item_id: Optional[int] = None


class MarketCommentDeleteObject(BaseEventObject):
    owner_id: Optional[int] = None
    id: Optional[int] = None
    user_id: Optional[int] = None
    item_id: Optional[int] = None


class GroupLeaveObject(BaseEventObject):
    user_id: Optional[int] = None
    self: Optional[int] = None


class GroupJoinObject(BaseEventObject):
    user_id: Optional[int] = None
    join_type: Optional[CallbackGroupJoinType] = None


class UserBlockObject(BaseEventObject):
    admin_id: Optional[int] = None
    user_id: Optional[int] = None
    unblock_data: Optional[int] = None
    reason: Optional[UsersBlockReason] = None
    comment: Optional[str] = None


class UserUnblockObject(BaseEventObject):
    admin_id: Optional[int] = None
    user_id: Optional[int] = None
    by_end_date: Optional[int] = None


class PollVoteNewObject(BaseEventObject):
    owner_id: Optional[int] = None
    poll_id: Optional[int] = None
    option_id: Optional[int] = None
    user_id: Optional[int] = None


class GroupOfficersEditObject(BaseEventObject):
    admin_id: Optional[int] = None
    user_id: Optional[int] = None
    level_old: Optional[GroupsGroupAdminLevel] = None
    level_new: Optional[GroupsGroupAdminLevel] = None


class GroupChangeSettingsChangesSectionEnableObject(enum.Enum):
    STATUS_DEFAULT = "status_default"
    AUDIO = "audio"
    PHOTO = "photo"
    VIDEO = "video"
    MARKET = "market"


class GroupChangeSettingsChangesSectionNameObject(enum.Enum):
    TITLE = "title"
    DESCRIPTION = "description"
    COMMUNITY_TYPE = "access"
    SCREEN_NAME = "screen_name"
    PUBLIC_CATEGORY = "public_category"
    PUBLIC_SUBCATEGORY = "public_subcategory"
    AGE_LIMITS = "age_limits"
    WEBSITE = "website"
    ENABLE_SECTION = GroupChangeSettingsChangesSectionEnableObject


class GroupChangeSettingsChangesObject(BaseEventObject):
    section_name: Optional[GroupChangeSettingsChangesSectionNameObject] = None
    old_value: Any = None
    new_value: Any = None


class GroupChangeSettingsObject(BaseEventObject):
    user_id: Optional[int] = None
    changes: Optional[GroupChangeSettingsChangesObject] = None


class GroupChangePhotoObject(BaseEventObject):
    user_id: Optional[int] = None
    photo: Optional[PhotosPhoto] = None


class MarketOrderObject(MarketOrder):
    pass


class VkPayTransactionObject(BaseEventObject):
    from_id: Optional[int] = None
    amount: Optional[int] = None
    description: Optional[str] = None
    date: Optional[int] = None


class AppPayloadObject(BaseEventObject):
    user_id: Optional[int] = None
    app_id: Optional[int] = None
    payload: Optional[str] = None
    group_id: Optional[int] = None


class DonutSubscriptionObject(BaseEventObject):
    user_id: Optional[int] = None


class DonutSubscriptionCreateObject(DonutSubscriptionObject):
    amount: Optional[int] = None
    amount_without_fee: Optional[float] = None


class DonutSubscriptionProlongedObject(DonutSubscriptionCreateObject):
    pass


class DonutSubscriptionExpiredObject(DonutSubscriptionObject):
    pass


class DonutSubscriptionCancelledObject(DonutSubscriptionObject):
    pass


class DonutSubscriptionPriceChangedObject(DonutSubscriptionObject):
    amount_old: Optional[int] = None
    amount_new: Optional[int] = None
    amount_diff: Optional[float] = None
    amount_diff_without_fee: Optional[float] = None


class DonutMoneyWithdrawObject(BaseEventObject):
    amount: Optional[float] = None
    amount_without_fee: Optional[float] = None


class DonutMoneyWithdrawErrorObject(BaseEventObject):
    reason: Optional[str] = None


MessageAllowObject.update_forward_refs()
MessageTypingStateObject.update_forward_refs()
MessageDenyObject.update_forward_refs()
MessageEventObject.update_forward_refs()
PhotoCommentObject.update_forward_refs()
PhotoCommentDeleteObject.update_forward_refs()
VideoCommentObject.update_forward_refs()
VideoCommentDeleteObject.update_forward_refs()
WallPostNewObject.update_forward_refs()
WallReplyNewObject.update_forward_refs()
WallReplyDeleteObject.update_forward_refs()
BoardPostNewObject.update_forward_refs()
BoardPostDeleteObject.update_forward_refs()
MarketCommentNewObject.update_forward_refs()
MarketCommentDeleteObject.update_forward_refs()
GroupLeaveObject.update_forward_refs()
GroupJoinObject.update_forward_refs()
UserBlockObject.update_forward_refs()
UserUnblockObject.update_forward_refs()
PollVoteNewObject.update_forward_refs()
GroupOfficersEditObject.update_forward_refs()
GroupChangeSettingsChangesObject.update_forward_refs()
GroupChangeSettingsObject.update_forward_refs()
GroupChangePhotoObject.update_forward_refs()
