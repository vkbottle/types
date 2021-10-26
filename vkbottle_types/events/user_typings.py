from typing import Union

from .user_events import (
    BaseUserEvent,
    ReplaceMessageFlags,
    InstallMessageFlags,
    ResetMessageFlags,
    MessageNew,
    MessagesDelete,
    MessagesRestore,
    MessageEdit,
    ChatVoiceMessageStates,
    ChatEdit,
    ChatInfoEdit,
    ChatTypingState,
    DialogTypingState,
    UsersTypingState,
    ResetDialogFlags,
    ReplaceDialogFlags,
    InstallDialogFlags,
    FriendOnline,
    FriendOffline,
    Counter,
    Call,
    NotificationsSettingsChanged,
    InRead,
    OutRead,
)


class UserTypes:
    ReplaceMessageFlags = ReplaceMessageFlags
    InstallMessageFlags = InstallMessageFlags
    ResetMessageFlags = ResetMessageFlags
    MessageNew = MessageNew
    MessagesDelete = MessagesDelete
    MessagesRestore = MessagesRestore
    MessageEdit = MessageEdit
    ChatVoiceMessageStates = ChatVoiceMessageStates
    ChatEdit = ChatEdit
    ChatInfoEdit = ChatInfoEdit
    ChatTypingState = ChatTypingState
    DialogTypingState = DialogTypingState
    UsersTypingState = UsersTypingState
    ResetDialogFlags = ResetDialogFlags
    ReplaceDialogFlags = ReplaceDialogFlags
    InstallDialogFlags = InstallDialogFlags
    FriendOnline = FriendOnline
    FriendOffline = FriendOffline
    Counter = Counter
    Call = Call
    NotificationsSettingsChanged = NotificationsSettingsChanged
    InRead = InRead
    OutRead = OutRead
    UnifiedTypes = Union[
        BaseUserEvent,
        ReplaceMessageFlags,
        InstallMessageFlags,
        ResetMessageFlags,
        MessageNew,
        MessagesDelete,
        MessagesRestore,
        MessageEdit,
        ChatVoiceMessageStates,
        ChatEdit,
        ChatInfoEdit,
        ChatTypingState,
        DialogTypingState,
        UsersTypingState,
        ResetDialogFlags,
        ReplaceDialogFlags,
        InstallDialogFlags,
        FriendOnline,
        FriendOffline,
        Counter,
        Call,
        NotificationsSettingsChanged,
        InRead,
        OutRead,
    ]
