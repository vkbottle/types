from typing import Union

from .bot_events import (
    AppPayload,
    AudioNew,
    BaseGroupEvent,
    BoardPostDelete,
    BoardPostEdit,
    BoardPostNew,
    BoardPostRestore,
    DonutMoneyWithdraw,
    DonutMoneyWithdrawError,
    DonutSubscriptionCancelled,
    DonutSubscriptionCreate,
    DonutSubscriptionExpired,
    DonutSubscriptionPriceChanged,
    DonutSubscriptionProlonged,
    GroupChangePhoto,
    GroupChangeSettings,
    GroupJoin,
    GroupLeave,
    GroupOfficersEdit,
    LikeAdd,
    LikeRemove,
    MarketCommentDelete,
    MarketCommentEdit,
    MarketCommentNew,
    MarketCommentRestore,
    MarketOrderEdit,
    MarketOrderNew,
    MessageAllow,
    MessageDeny,
    MessageEdit,
    MessageEvent,
    MessageNew,
    MessageReply,
    MessageTypingState,
    PhotoCommentDelete,
    PhotoCommentEdit,
    PhotoCommentNew,
    PhotoCommentRestore,
    PhotoNew,
    PollVoteNew,
    UserBlock,
    UserUnblock,
    VideoCommentDelete,
    VideoCommentEdit,
    VideoCommentNew,
    VideoCommentRestore,
    VideoNew,
    VkpayTransaction,
    WallPostNew,
    WallReplyDelete,
    WallReplyEdit,
    WallReplyNew,
    WallReplyRestore,
    WallRepost,
)


class GroupTypes:
    MessageNew = MessageNew
    MessageReply = MessageReply
    MessageEdit = MessageEdit
    MessageAllow = MessageAllow
    MessageDeny = MessageDeny
    MessageTypingState = MessageTypingState
    MessageEvent = MessageEvent
    PhotoNew = PhotoNew
    PhotoCommentNew = PhotoCommentNew
    PhotoCommentEdit = PhotoCommentEdit
    PhotoCommentRestore = PhotoCommentRestore
    PhotoCommentDelete = PhotoCommentDelete
    AudioNew = AudioNew
    VideoNew = VideoNew
    VideoCommentNew = VideoCommentNew
    VideoCommentEdit = VideoCommentEdit
    VideoCommentRestore = VideoCommentRestore
    VideoCommentDelete = VideoCommentDelete
    WallPostNew = WallPostNew
    WallRepost = WallRepost
    WallReplyNew = WallReplyNew
    WallReplyEdit = WallReplyEdit
    WallReplyRestore = WallReplyRestore
    WallReplyDelete = WallReplyDelete
    LikeAdd = LikeAdd
    LikeRemove = LikeRemove
    BoardPostNew = BoardPostNew
    BoardPostEdit = BoardPostEdit
    BoardPostRestore = BoardPostRestore
    BoardPostDelete = BoardPostDelete
    MarketCommentNew = MarketCommentNew
    MarketCommentEdit = MarketCommentEdit
    MarketCommentRestore = MarketCommentRestore
    MarketCommentDelete = MarketCommentDelete
    MarketOrderNew = MarketOrderNew
    MarketOrderEdit = MarketOrderEdit
    GroupLeave = GroupLeave
    GroupJoin = GroupJoin
    UserBlock = UserBlock
    UserUnblock = UserUnblock
    PollVoteNew = PollVoteNew
    GroupOfficersEdit = GroupOfficersEdit
    GroupChangeSettings = GroupChangeSettings
    GroupChangePhoto = GroupChangePhoto
    VkpayTransaction = VkpayTransaction
    AppPayload = AppPayload
    DonutSubscriptionCreate = DonutSubscriptionCreate
    DonutSubscriptionProlonged = DonutSubscriptionProlonged
    DonutSubscriptionExpired = DonutSubscriptionExpired
    DonutSubscriptionCancelled = DonutSubscriptionCancelled
    DonutSubscriptionPriceChanged = DonutSubscriptionPriceChanged
    DonutMoneyWithdraw = DonutMoneyWithdraw
    DonutMoneyWithdrawError = DonutMoneyWithdrawError

    UnifiedTypes = Union[
        BaseGroupEvent,
        MessageNew,
        MessageReply,
        MessageEdit,
        MessageAllow,
        MessageDeny,
        MessageTypingState,
        MessageEvent,
        PhotoNew,
        PhotoCommentNew,
        PhotoCommentEdit,
        PhotoCommentRestore,
        PhotoCommentDelete,
        AudioNew,
        VideoNew,
        VideoCommentNew,
        VideoCommentEdit,
        VideoCommentRestore,
        VideoCommentDelete,
        WallPostNew,
        WallRepost,
        WallReplyNew,
        WallReplyEdit,
        WallReplyRestore,
        WallReplyDelete,
        LikeAdd,
        LikeRemove,
        BoardPostNew,
        BoardPostEdit,
        BoardPostRestore,
        BoardPostDelete,
        MarketCommentNew,
        MarketCommentEdit,
        MarketCommentRestore,
        MarketCommentDelete,
        MarketOrderNew,
        MarketOrderEdit,
        GroupLeave,
        GroupJoin,
        UserBlock,
        UserUnblock,
        PollVoteNew,
        GroupOfficersEdit,
        GroupChangeSettings,
        GroupChangePhoto,
        VkpayTransaction,
        AppPayload,
        DonutSubscriptionCreate,
        DonutSubscriptionProlonged,
        DonutSubscriptionExpired,
        DonutSubscriptionCancelled,
        DonutSubscriptionPriceChanged,
        DonutMoneyWithdraw,
        DonutMoneyWithdrawError,
    ]
