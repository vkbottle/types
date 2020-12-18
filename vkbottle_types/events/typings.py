from .bot_events import *
from .user_events import *
from typing import Any, Union


class GroupTypes:
    MessageNew = MessageNew
    MessageAllow = MessageAllow
    MessageReply = Message
    MessageEdit = Message
    MessageTypingState = MessageTypingState
    MessageDeny = MessageDeny
    MessageEvent = MessageEvent
    PhotoNew = PhotoNew
    PhotoComment = PhotoComment
    PhotoCommentDelete = PhotoCommentDelete
    AudioNew = AudioNew
    VideoNew = VideoNew
    VideoCommentNew = VideoComment
    VideoCommentEdit = VideoComment
    VideoCommentRestore = VideoComment
    VideoCommentDelete = VideoCommentDelete
    WallPostNew = WallPostNew
    WallRepost = WallPostNew
    WallReplyNew = WallReply
    WallReplyEdit = WallReply
    WallReplyRestore = WallReply
    WallReplyDelete = WallReplyDelete
    LikeAdd = Like
    LikeRemove = Like
    BoardPostNew = BoardPost
    BoardPostEdit = BoardPost
    BoardPostRestore = BoardPost
    BoardPostDelete = BoardPostDelete
    MarketCommentNew = MarketComment
    MarketCommentEdit = MarketComment
    MarketCommentRestore = MarketComment
    MarketCommentDelete = MarketCommentDelete
    GroupJoin = GroupJoin
    GroupLeave = GroupLeave
    UserBlock = UserBlock
    UserUnblock = UserUnblock
    PollVoteNew = PollVoteNew
    GroupOfficersEdit = GroupOfficersEdit
    GroupChangeSettings = GroupChangeSettings
    GroupChangePhoto = GroupChangePhoto
    VkPayTransaction = VkPayTransaction
    AppPayload = AppPayload
    DonutSubscriptionCreate = DonutSubscriptionCreate
    DonutSubscriptionProlonged = DonutSubscriptionProlonged
    DonutSubscriptionCancelled = DonutSubscriptionCancelled
    DonutSubscriptionExpired = DonutSubscriptionExpired
    DonutSubscriptionPriceChanged = DonutSubscriptionPriceChanged
    DonutMoneyWithdraw = DonutMoneyWithdraw
    DonutMoneyWithdrawError = DonutMoneyWithdrawError

    UnifiedTypes = Union[
        BaseGroupEvent,
        MessageNew,
        Message,
        MessageAllow,
        MessageTypingState,
        MessageDeny,
        MessageEvent,
        PhotoNew,
        PhotoComment,
        PhotoCommentDelete,
        AudioNew,
        VideoNew,
        VideoComment,
        VideoCommentDelete,
        WallPostNew,
        WallReply,
        WallReplyDelete,
        Like,
        BoardPost,
        BoardPostDelete,
        MarketComment,
        MarketCommentDelete,
        GroupJoin,
        GroupLeave,
        UserBlock,
        UserUnblock,
        PollVoteNew,
        GroupOfficersEdit,
        GroupChangeSettings,
        GroupChangePhoto,
        VkPayTransaction,
        AppPayload,
        DonutSubscriptionCreate,
        DonutSubscriptionProlonged,
        DonutSubscriptionCancelled,
        DonutSubscriptionExpired,
        DonutSubscriptionPriceChanged,
        DonutMoneyWithdraw,
        DonutMoneyWithdrawError,
    ]


class UserTypes:
    UnifiedTypes = Union[BaseUserEvent, Any]
