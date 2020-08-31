from .events_base import EventsBase
from .enums import GroupEventType, UserEventType
from .bot_events import *


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
