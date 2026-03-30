from typing import TypeAlias

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
    MessageNew: TypeAlias = MessageNew
    MessageReply: TypeAlias = MessageReply
    MessageEdit: TypeAlias = MessageEdit
    MessageRead: TypeAlias = MessageRead
    MessageAllow: TypeAlias = MessageAllow
    MessageDeny: TypeAlias = MessageDeny
    MessageReactionEvent: TypeAlias = MessageReactionEvent
    MessageTypingState: TypeAlias = MessageTypingState
    MessageEvent: TypeAlias = MessageEvent
    PhotoNew: TypeAlias = PhotoNew
    PhotoCommentNew: TypeAlias = PhotoCommentNew
    PhotoCommentEdit: TypeAlias = PhotoCommentEdit
    PhotoCommentRestore: TypeAlias = PhotoCommentRestore
    PhotoCommentDelete: TypeAlias = PhotoCommentDelete
    AudioNew: TypeAlias = AudioNew
    VideoNew: TypeAlias = VideoNew
    VideoCommentNew: TypeAlias = VideoCommentNew
    VideoCommentEdit: TypeAlias = VideoCommentEdit
    VideoCommentRestore: TypeAlias = VideoCommentRestore
    VideoCommentDelete: TypeAlias = VideoCommentDelete
    WallPostNew: TypeAlias = WallPostNew
    WallRepost: TypeAlias = WallRepost
    WallReplyNew: TypeAlias = WallReplyNew
    WallReplyEdit: TypeAlias = WallReplyEdit
    WallReplyRestore: TypeAlias = WallReplyRestore
    WallReplyDelete: TypeAlias = WallReplyDelete
    LeadFormsNew: TypeAlias = LeadFormsNew
    LikeAdd: TypeAlias = LikeAdd
    LikeRemove: TypeAlias = LikeRemove
    BoardPostNew: TypeAlias = BoardPostNew
    BoardPostEdit: TypeAlias = BoardPostEdit
    BoardPostRestore: TypeAlias = BoardPostRestore
    BoardPostDelete: TypeAlias = BoardPostDelete
    MarketCommentNew: TypeAlias = MarketCommentNew
    MarketCommentEdit: TypeAlias = MarketCommentEdit
    MarketCommentRestore: TypeAlias = MarketCommentRestore
    MarketCommentDelete: TypeAlias = MarketCommentDelete
    MarketOrderNew: TypeAlias = MarketOrderNew
    MarketOrderEdit: TypeAlias = MarketOrderEdit
    GroupLeave: TypeAlias = GroupLeave
    GroupJoin: TypeAlias = GroupJoin
    UserBlock: TypeAlias = UserBlock
    UserUnblock: TypeAlias = UserUnblock
    PollVoteNew: TypeAlias = PollVoteNew
    GroupOfficersEdit: TypeAlias = GroupOfficersEdit
    GroupChangeSettings: TypeAlias = GroupChangeSettings
    GroupChangePhoto: TypeAlias = GroupChangePhoto
    VkpayTransaction: TypeAlias = VkpayTransaction
    AppPayload: TypeAlias = AppPayload
    DonutSubscriptionCreate: TypeAlias = DonutSubscriptionCreate
    DonutSubscriptionProlonged: TypeAlias = DonutSubscriptionProlonged
    DonutSubscriptionExpired: TypeAlias = DonutSubscriptionExpired
    DonutSubscriptionCancelled: TypeAlias = DonutSubscriptionCancelled
    DonutSubscriptionPriceChanged: TypeAlias = DonutSubscriptionPriceChanged
    DonutMoneyWithdraw: TypeAlias = DonutMoneyWithdraw
    DonutMoneyWithdrawError: TypeAlias = DonutMoneyWithdrawError


__all__ = ("GroupTypes",)
