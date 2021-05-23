from typing import Union

from .user_events import *


class UserTypes:
    MessageNew = MessageNew
    MessagesDelete = MessagesDelete
    ChatRestore = ChatRestore
    EditMessage = EditMessage
    ReplaceMessageFlags = ReplaceMessageFlags
    InstallMessageFlags = InstallMessageFlags
    ResetMessageFlags = ResetMessageFlags
    ChatVoiceMessageStates = ChatVoiceMessageStates
    ChatEdit = ChatEdit
    ChatInfoEdit = ChatInfoEdit
    ChatTypingState = ChatTypingState
    ChangeConversationParams = ChangeConversationParams
    DialogTypingState = DialogTypingState
    ResetDialogFlags = ResetDialogFlags
    ReplaceDialogFlags = ReplaceDialogFlags
    InstallDialogFlags = InstallDialogFlags
    FriendOnline = FriendOnline
    FriendOffline = FriendOffline
    Counter = Counter
    ChangedNotificationsSettings = ChangedNotificationsSettings
    InRead = InRead
    OutRead = OutRead
    UnifiedTypes = Union[
        BaseUserEvent,
        MessageNew,
        Message,
        MessagesDelete,
        ChatRestore,
        EditMessage,
        ReplaceMessageFlags,
        InstallMessageFlags,
        ResetMessageFlags,
        ChatVoiceMessageStates,
        ChatEdit,
        ChatInfoEdit,
        ChatTypingState,
        ChangeConversationParams,
        DialogTypingState,
        ResetDialogFlags,
        ReplaceDialogFlags,
        FriendOnline,
        FriendOffline,
        Counter,
        ChangedNotificationsSettings,
        InRead,
        OutRead,
    ]
