from .user_events import (
    AddConversationsToFolder,
    Call,
    ChangeFolderOrder,
    ChatEdit,
    ChatInfoEdit,
    ChatTypingState,
    ChatVoiceMessageStates,
    Counter,
    CounterUnreadDialogsInFolders,
    CreateFolder,
    DeleteFolder,
    DialogTypingState,
    FriendAction,
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
    RemoveConversationsFromFolder,
    RenameFolder,
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
    FriendAction = FriendAction
    NotificationsSettingsChanged = NotificationsSettingsChanged
    InRead = InRead
    OutRead = OutRead
    CreateFolder = CreateFolder
    RenameFolder = RenameFolder
    DeleteFolder = DeleteFolder
    AddConversationsToFolder = AddConversationsToFolder
    RemoveConversationsFromFolder = RemoveConversationsFromFolder
    ChangeFolderOrder = ChangeFolderOrder
    CounterUnreadDialogsInFolders = CounterUnreadDialogsInFolders


__all__ = ("UserTypes",)
