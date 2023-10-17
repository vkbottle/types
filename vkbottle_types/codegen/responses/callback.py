import typing
from vkbottle_types.responses.base_response import BaseResponse, BaseModel
from vkbottle_types.base_model import Field

from vkbottle_types.objects import (
    PhotosPhoto,
    CallbackGroupOfficerRole,
    GroupsGroupWall,
    CallbackGroupJoinType,
    CallbackGroupMarket,
    BaseBoolInt,
    CallbackType,
    GroupsGroupPhotos,
    CallbackMessageAllowObject,
    MessagesMessage,
    GroupsGroupVideo,
    ClientInfoForBots,
    GroupsGroupAudio,
    GroupsGroupFullAgeLimits,
    GroupsGroupIsClosed,
)


class CallbackBaseResponseModel(BaseModel):
    type: "CallbackType" = Field()

    group_id: int = Field()

    event_id: str = Field(
        description="Unique event id. If it passed twice or more - you should ignore it.",
    )

    v: str = Field(
        description="API object version",
    )

    secret: typing.Optional[str] = Field(
        default=None,
    )


class CallbackBaseResponse(BaseResponse):
    response: "CallbackBaseResponseModel"


class CallbackBoardPostDeleteResponseModel(BaseModel):
    topic_owner_id: int = Field()

    topic_id: int = Field()

    id: int = Field()


class CallbackBoardPostDeleteResponse(BaseResponse):
    response: "CallbackBoardPostDeleteResponseModel"


class CallbackConfirmationResponseModel(CallbackBase):
    type: typing.Optional[str] = Field(
        default=None,
    )


class CallbackConfirmationResponse(BaseResponse):
    response: "CallbackConfirmationResponseModel"


class CallbackDonutMoneyWithdrawResponseModel(BaseModel):
    amount: float = Field()

    amount_without_fee: float = Field()


class CallbackDonutMoneyWithdrawResponse(BaseResponse):
    response: "CallbackDonutMoneyWithdrawResponseModel"


class CallbackDonutMoneyWithdrawErrorResponseModel(BaseModel):
    reason: str = Field()


class CallbackDonutMoneyWithdrawErrorResponse(BaseResponse):
    response: "CallbackDonutMoneyWithdrawErrorResponseModel"


class CallbackDonutSubscriptionCancelledResponseModel(BaseModel):
    user_id: typing.Optional[int] = Field(
        default=None,
    )


class CallbackDonutSubscriptionCancelledResponse(BaseResponse):
    response: "CallbackDonutSubscriptionCancelledResponseModel"


class CallbackDonutSubscriptionCreateResponseModel(BaseModel):
    amount: int = Field()

    amount_without_fee: float = Field()

    user_id: typing.Optional[int] = Field(
        default=None,
    )


class CallbackDonutSubscriptionCreateResponse(BaseResponse):
    response: "CallbackDonutSubscriptionCreateResponseModel"


class CallbackDonutSubscriptionExpiredResponseModel(BaseModel):
    user_id: typing.Optional[int] = Field(
        default=None,
    )


class CallbackDonutSubscriptionExpiredResponse(BaseResponse):
    response: "CallbackDonutSubscriptionExpiredResponseModel"


class CallbackDonutSubscriptionPriceChangedResponseModel(BaseModel):
    amount_old: int = Field()

    amount_new: int = Field()

    user_id: typing.Optional[int] = Field(
        default=None,
    )

    amount_diff: typing.Optional[float] = Field(
        default=None,
    )

    amount_diff_without_fee: typing.Optional[float] = Field(
        default=None,
    )


class CallbackDonutSubscriptionPriceChangedResponse(BaseResponse):
    response: "CallbackDonutSubscriptionPriceChangedResponseModel"


class CallbackDonutSubscriptionProlongedResponseModel(BaseModel):
    amount: int = Field()

    amount_without_fee: float = Field()

    user_id: typing.Optional[int] = Field(
        default=None,
    )


class CallbackDonutSubscriptionProlongedResponse(BaseResponse):
    response: "CallbackDonutSubscriptionProlongedResponseModel"


class CallbackGroupChangePhotoResponseModel(BaseModel):
    user_id: int = Field()

    photo: "PhotosPhoto" = Field()


class CallbackGroupChangePhotoResponse(BaseResponse):
    response: "CallbackGroupChangePhotoResponseModel"


class CallbackGroupChangeSettingsResponseModel(BaseModel):
    user_id: int = Field()

    self: bool = Field()


class CallbackGroupChangeSettingsResponse(BaseResponse):
    response: "CallbackGroupChangeSettingsResponseModel"


class CallbackGroupJoinResponseModel(BaseModel):
    user_id: int = Field()

    join_type: "CallbackGroupJoinType" = Field()


class CallbackGroupJoinResponse(BaseResponse):
    response: "CallbackGroupJoinResponseModel"


class CallbackGroupJoinTypeResponseModel(enum.Enum):
    JOIN = "join"

    UNSURE = "unsure"

    ACCEPTED = "accepted"

    APPROVED = "approved"

    REQUEST = "request"


class CallbackGroupJoinTypeResponse(BaseResponse):
    response: "CallbackGroupJoinTypeResponseModel"


class CallbackGroupLeaveResponseModel(BaseModel):
    user_id: typing.Optional[int] = Field(
        default=None,
    )

    self: typing.Optional[bool] = Field(
        default=None,
    )


class CallbackGroupLeaveResponse(BaseResponse):
    response: "CallbackGroupLeaveResponseModel"


class CallbackGroupMarketResponseModel(enum.IntEnum):
    DISABLED = 0

    OPEN = 1


class CallbackGroupMarketResponse(BaseResponse):
    response: "CallbackGroupMarketResponseModel"


class CallbackGroupOfficerRoleResponseModel(enum.IntEnum):
    NONE = 0

    MODERATOR = 1

    EDITOR = 2

    ADMINISTRATOR = 3


class CallbackGroupOfficerRoleResponse(BaseResponse):
    response: "CallbackGroupOfficerRoleResponseModel"


class CallbackGroupOfficersEditResponseModel(BaseModel):
    admin_id: int = Field()

    user_id: int = Field()

    level_old: "CallbackGroupOfficerRole" = Field()

    level_new: "CallbackGroupOfficerRole" = Field()


class CallbackGroupOfficersEditResponse(BaseResponse):
    response: "CallbackGroupOfficersEditResponseModel"


class CallbackGroupSettingsChangesResponseModel(BaseModel):
    title: typing.Optional[str] = Field(
        default=None,
    )

    description: typing.Optional[str] = Field(
        default=None,
    )

    access: typing.Optional["GroupsGroupIsClosed"] = Field(
        default=None,
    )

    screen_name: typing.Optional[str] = Field(
        default=None,
    )

    public_category: typing.Optional[int] = Field(
        default=None,
    )

    public_subcategory: typing.Optional[int] = Field(
        default=None,
    )

    age_limits: typing.Optional["GroupsGroupFullAgeLimits"] = Field(
        default=None,
    )

    website: typing.Optional[str] = Field(
        default=None,
    )

    enable_status_default: typing.Optional["GroupsGroupWall"] = Field(
        default=None,
    )

    enable_audio: typing.Optional["GroupsGroupAudio"] = Field(
        default=None,
    )

    enable_video: typing.Optional["GroupsGroupVideo"] = Field(
        default=None,
    )

    enable_photo: typing.Optional["GroupsGroupPhotos"] = Field(
        default=None,
    )

    enable_market: typing.Optional["CallbackGroupMarket"] = Field(
        default=None,
    )


class CallbackGroupSettingsChangesResponse(BaseResponse):
    response: "CallbackGroupSettingsChangesResponseModel"


class CallbackLikeAddRemoveResponseModel(BaseModel):
    liker_id: int = Field()

    object_type: typing.Literal[
        "video",
        "photo",
        "post",
        "comment",
        "note",
        "topic_comment",
        "photo_comment",
        "video_comment",
        "market",
        "market_comment",
    ] = Field()

    object_owner_id: int = Field()

    object_id: int = Field()

    post_id: int = Field()

    thread_reply_id: typing.Optional[int] = Field(
        default=None,
    )


class CallbackLikeAddRemoveResponse(BaseResponse):
    response: "CallbackLikeAddRemoveResponseModel"


class CallbackMarketCommentResponseModel(BaseModel):
    id: int = Field()

    from_id: int = Field()

    date: int = Field()

    text: typing.Optional[str] = Field(
        default=None,
    )

    market_owner_id: typing.Optional[int] = Field(
        default=None,
    )

    photo_id: typing.Optional[int] = Field(
        default=None,
    )


class CallbackMarketCommentResponse(BaseResponse):
    response: "CallbackMarketCommentResponseModel"


class CallbackMarketCommentDeleteResponseModel(BaseModel):
    owner_id: int = Field()

    id: int = Field()

    user_id: int = Field()

    item_id: int = Field()


class CallbackMarketCommentDeleteResponse(BaseResponse):
    response: "CallbackMarketCommentDeleteResponseModel"


class CallbackMessageAllowResponseModel(CallbackBase):
    object: "CallbackMessageAllowObject" = Field()

    type: typing.Optional[str] = Field(
        default=None,
    )


class CallbackMessageAllowResponse(BaseResponse):
    response: "CallbackMessageAllowResponseModel"


class CallbackMessageAllowObjectResponseModel(BaseModel):
    user_id: int = Field()

    key: str = Field()


class CallbackMessageAllowObjectResponse(BaseResponse):
    response: "CallbackMessageAllowObjectResponseModel"


class CallbackMessageDenyResponseModel(BaseModel):
    user_id: int = Field()


class CallbackMessageDenyResponse(BaseResponse):
    response: "CallbackMessageDenyResponseModel"


class CallbackMessageEditResponseModel(CallbackBase):
    object: "MessagesMessage" = Field()

    type: typing.Optional[str] = Field(
        default=None,
    )


class CallbackMessageEditResponse(BaseResponse):
    response: "CallbackMessageEditResponseModel"


class CallbackMessageNewResponseModel(CallbackBase):
    object: dict = Field()

    type: typing.Optional[str] = Field(
        default=None,
    )


class CallbackMessageNewResponse(BaseResponse):
    response: "CallbackMessageNewResponseModel"


class CallbackMessageObjectResponseModel(BaseModel):
    client_info: typing.Optional["ClientInfoForBots"] = Field(
        default=None,
    )

    message: typing.Optional["MessagesMessage"] = Field(
        default=None,
    )


class CallbackMessageObjectResponse(BaseResponse):
    response: "CallbackMessageObjectResponseModel"


class CallbackMessageReplyResponseModel(CallbackBase):
    object: "MessagesMessage" = Field()

    type: typing.Optional[str] = Field(
        default=None,
    )


class CallbackMessageReplyResponse(BaseResponse):
    response: "CallbackMessageReplyResponseModel"


class CallbackPhotoCommentResponseModel(BaseModel):
    id: int = Field()

    from_id: int = Field()

    date: int = Field()

    text: str = Field()

    photo_owner_id: int = Field()


class CallbackPhotoCommentResponse(BaseResponse):
    response: "CallbackPhotoCommentResponseModel"


class CallbackPhotoCommentDeleteResponseModel(BaseModel):
    id: int = Field()

    owner_id: int = Field()

    user_id: int = Field()

    photo_id: int = Field()


class CallbackPhotoCommentDeleteResponse(BaseResponse):
    response: "CallbackPhotoCommentDeleteResponseModel"


class CallbackPollVoteNewResponseModel(BaseModel):
    owner_id: int = Field()

    poll_id: int = Field()

    option_id: int = Field()

    user_id: int = Field()


class CallbackPollVoteNewResponse(BaseResponse):
    response: "CallbackPollVoteNewResponseModel"


class CallbackTypeResponseModel(enum.Enum):
    AUDIO_NEW = "audio_new"

    BOARD_POST_NEW = "board_post_new"

    BOARD_POST_EDIT = "board_post_edit"

    BOARD_POST_RESTORE = "board_post_restore"

    BOARD_POST_DELETE = "board_post_delete"

    CONFIRMATION = "confirmation"

    GROUP_LEAVE = "group_leave"

    GROUP_JOIN = "group_join"

    GROUP_CHANGE_PHOTO = "group_change_photo"

    GROUP_CHANGE_SETTINGS = "group_change_settings"

    GROUP_OFFICERS_EDIT = "group_officers_edit"

    LEAD_FORMS_NEW = "lead_forms_new"

    MARKET_COMMENT_NEW = "market_comment_new"

    MARKET_COMMENT_DELETE = "market_comment_delete"

    MARKET_COMMENT_EDIT = "market_comment_edit"

    MARKET_COMMENT_RESTORE = "market_comment_restore"

    MARKET_ORDER_NEW = "market_order_new"

    MARKET_ORDER_EDIT = "market_order_edit"

    MESSAGE_NEW = "message_new"

    MESSAGE_REPLY = "message_reply"

    MESSAGE_EDIT = "message_edit"

    MESSAGE_ALLOW = "message_allow"

    MESSAGE_DENY = "message_deny"

    MESSAGE_READ = "message_read"

    MESSAGE_TYPING_STATE = "message_typing_state"

    MESSAGES_EDIT = "messages_edit"

    MESSAGE_REACTION_EVENT = "message_reaction_event"

    PHOTO_NEW = "photo_new"

    PHOTO_COMMENT_NEW = "photo_comment_new"

    PHOTO_COMMENT_DELETE = "photo_comment_delete"

    PHOTO_COMMENT_EDIT = "photo_comment_edit"

    PHOTO_COMMENT_RESTORE = "photo_comment_restore"

    POLL_VOTE_NEW = "poll_vote_new"

    USER_BLOCK = "user_block"

    USER_UNBLOCK = "user_unblock"

    VIDEO_NEW = "video_new"

    VIDEO_COMMENT_NEW = "video_comment_new"

    VIDEO_COMMENT_DELETE = "video_comment_delete"

    VIDEO_COMMENT_EDIT = "video_comment_edit"

    VIDEO_COMMENT_RESTORE = "video_comment_restore"

    WALL_POST_NEW = "wall_post_new"

    WALL_REPLY_NEW = "wall_reply_new"

    WALL_REPLY_EDIT = "wall_reply_edit"

    WALL_REPLY_DELETE = "wall_reply_delete"

    WALL_REPLY_RESTORE = "wall_reply_restore"

    WALL_REPOST = "wall_repost"


class CallbackTypeResponse(BaseResponse):
    response: "CallbackTypeResponseModel"


class CallbackUserBlockResponseModel(BaseModel):
    admin_id: int = Field()

    user_id: int = Field()

    unblock_date: int = Field()

    reason: int = Field()

    comment: typing.Optional[str] = Field(
        default=None,
    )


class CallbackUserBlockResponse(BaseResponse):
    response: "CallbackUserBlockResponseModel"


class CallbackUserUnblockResponseModel(BaseModel):
    admin_id: int = Field()

    user_id: int = Field()

    by_end_date: int = Field()


class CallbackUserUnblockResponse(BaseResponse):
    response: "CallbackUserUnblockResponseModel"


class CallbackVideoCommentResponseModel(BaseModel):
    id: int = Field()

    from_id: int = Field()

    date: int = Field()

    text: str = Field()

    video_owner_id: int = Field()


class CallbackVideoCommentResponse(BaseResponse):
    response: "CallbackVideoCommentResponseModel"


class CallbackVideoCommentDeleteResponseModel(BaseModel):
    id: int = Field()

    owner_id: int = Field()

    user_id: int = Field()

    video_id: int = Field()


class CallbackVideoCommentDeleteResponse(BaseResponse):
    response: "CallbackVideoCommentDeleteResponseModel"


class CallbackWallCommentDeleteResponseModel(BaseModel):
    owner_id: int = Field()

    id: int = Field()

    user_id: int = Field()

    post_id: int = Field()


class CallbackWallCommentDeleteResponse(BaseResponse):
    response: "CallbackWallCommentDeleteResponseModel"
