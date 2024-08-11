from .bot_events import (
    AppPayload,
    AudioNew,
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
    LeadFormsNew,
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
    MessageReactionEvent,
    MessageRead,
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
    MessageRead = MessageRead
    MessageAllow = MessageAllow
    MessageDeny = MessageDeny
    MessageReactionEvent = MessageReactionEvent
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
    LeadFormsNew = LeadFormsNew
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


__all__ = ("GroupTypes",)
