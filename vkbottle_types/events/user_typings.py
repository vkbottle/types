from .user_events import (
    Call,
    ChatEdit,
    ChatInfoEdit,
    ChatTypingState,
    ChatVoiceMessageStates,
    Counter,
    DialogTypingState,
    FriendOffline,
    FriendOnline,
    InRead,
    InstallDialogFlags,
    InstallMessageFlags,
    MessageEdit,
    MessageNew,
    MessagesDelete,
    MessagesRestore,
    NotificationsSettingsChanged,
    OutRead,
    RawUserEvent,
    ReplaceDialogFlags,
    ReplaceMessageFlags,
    ResetDialogFlags,
    ResetMessageFlags,
    UsersTypingState,
)


class UserTypes:
    RawUserEvent = RawUserEvent
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
