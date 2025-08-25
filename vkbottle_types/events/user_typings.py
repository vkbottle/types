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
    DialogFlagsReplace,
    DialogResetFlags,
    DialogSetFlags,
    DialogTypingState,
    FriendAction,
    FriendOffline,
    FriendOnline,
    InRead,
    MessageEdit,
    MessageFlagsReplace,
    MessageNew,
    MessageResetFlags,
    MessagesDelete,
    MessageSetFlags,
    MessagesRestore,
    NotificationsSettingsChanged,
    OutRead,
    RawUserEvent,
    RemoveConversationsFromFolder,
    RenameFolder,
    UsersTypingState,
)


class UserTypes:
    RawUserEvent = RawUserEvent
    MessageFlagsReplace = MessageFlagsReplace
    MessageSetFlags = MessageSetFlags
    MessageResetFlags = MessageResetFlags
    MessageNew = MessageNew
    MessageEdit = MessageEdit
    MessagesDelete = MessagesDelete
    MessagesRestore = MessagesRestore
    ChatVoiceMessageStates = ChatVoiceMessageStates
    ChatEdit = ChatEdit
    ChatInfoEdit = ChatInfoEdit
    ChatTypingState = ChatTypingState
    DialogTypingState = DialogTypingState
    UsersTypingState = UsersTypingState
    DialogResetFlags = DialogResetFlags
    DialogFlagsReplace = DialogFlagsReplace
    DialogSetFlags = DialogSetFlags
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
