from typing import TypeAlias

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
    RawUserEvent: TypeAlias = RawUserEvent
    MessageFlagsReplace: TypeAlias = MessageFlagsReplace
    MessageSetFlags: TypeAlias = MessageSetFlags
    MessageResetFlags: TypeAlias = MessageResetFlags
    MessageNew: TypeAlias = MessageNew
    MessageEdit: TypeAlias = MessageEdit
    MessagesDelete: TypeAlias = MessagesDelete
    MessagesRestore: TypeAlias = MessagesRestore
    ChatVoiceMessageStates: TypeAlias = ChatVoiceMessageStates
    ChatEdit: TypeAlias = ChatEdit
    ChatInfoEdit: TypeAlias = ChatInfoEdit
    ChatTypingState: TypeAlias = ChatTypingState
    DialogTypingState: TypeAlias = DialogTypingState
    UsersTypingState: TypeAlias = UsersTypingState
    DialogResetFlags: TypeAlias = DialogResetFlags
    DialogFlagsReplace: TypeAlias = DialogFlagsReplace
    DialogSetFlags: TypeAlias = DialogSetFlags
    FriendOnline: TypeAlias = FriendOnline
    FriendOffline: TypeAlias = FriendOffline
    Counter: TypeAlias = Counter
    Call: TypeAlias = Call
    FriendAction: TypeAlias = FriendAction
    NotificationsSettingsChanged: TypeAlias = NotificationsSettingsChanged
    InRead: TypeAlias = InRead
    OutRead: TypeAlias = OutRead
    CreateFolder: TypeAlias = CreateFolder
    RenameFolder: TypeAlias = RenameFolder
    DeleteFolder: TypeAlias = DeleteFolder
    AddConversationsToFolder: TypeAlias = AddConversationsToFolder
    RemoveConversationsFromFolder: TypeAlias = RemoveConversationsFromFolder
    ChangeFolderOrder: TypeAlias = ChangeFolderOrder
    CounterUnreadDialogsInFolders: TypeAlias = CounterUnreadDialogsInFolders


__all__ = ("UserTypes",)
