import enum
import inspect
from typing import Any, Dict, List, NamedTuple, Optional, Union

import msgspec

Attachments = Union[Dict[str, Any], List[Any]]


class BaseEventObject(msgspec.Struct, omit_defaults=True, array_like=True):
    pass


class MessageObject(BaseEventObject):
    message_id: Optional[int] = None
    peer_id: Optional[int] = None
    timestamp: Optional[int] = None
    text: Optional[str] = None
    subject: Optional[str] = None
    info: Optional[str] = None
    attachments: Optional[Attachments] = None
    random_id: Optional[int] = None


class ReplaceMessageFlagsObject(MessageObject):
    flags: Optional[int] = None


class InstallMessageFlagsObject(MessageObject):
    mask: Optional[int] = None


class ResetMessageFlagsObject(MessageObject):
    mask: Optional[int] = None


class  MessageNewObject(MessageObject):
    minor_id: Optional[int] = None
    flags: Optional[int] = None


class MessageEditObject(BaseEventObject):
    message_id: Optional[int] = None
    mask: Optional[int] = None
    peer_id: Optional[int] = None
    timestamp: Optional[int] = None
    new_text: Optional[str] = ""
    attachments: Optional[Attachments] = None


class InReadObject(BaseEventObject):
    peer_id: Optional[int] = None
    local_id: Optional[int] = None


class OutReadObject(InReadObject):
    pass


class FriendOnlineObject(BaseEventObject):
    user_id: Optional[int] = None
    extra: Optional[int] = 0
    timestamp: Optional[int] = None


class FriendOfflineObject(BaseEventObject):
    user_id: Optional[int] = None
    flags: Optional[int] = 0
    timestamp: Optional[int] = None


class ResetDialogFlagsObject(BaseEventObject):
    peer_id: Optional[int] = None
    mask: Optional[int] = None


class ReplaceDialogFlagsObject(BaseEventObject):
    peer_id: Optional[int] = None
    flags: Optional[int] = None


class InstallDialogFlagsObject(ResetDialogFlagsObject):
    pass


class MessagesDeleteObject(InReadObject):
    pass


class MessagesRestoreObject(InReadObject):
    pass


class ChangeConversationParamsObject(BaseEventObject):
    chat_id: Optional[int] = None
    self: Optional[int] = None


class DialogTypingStateObject(BaseEventObject):
    user_id: Optional[int] = None
    flags: Optional[int] = None


class ConversationTypingStateObject(BaseEventObject):
    user_id: Optional[int] = None
    chat_id: Optional[int] = None


class UsersTypingStateObject(BaseEventObject):
    user_ids: Optional[List[int]] = None
    peer_id: Optional[int] = None
    total_count: Optional[int] = None
    ts: Optional[int] = None


class CallObject(BaseEventObject):
    user_id: Optional[int] = None
    call_id: Optional[int] = None


class CounterObject(BaseEventObject):
    count: Optional[int] = None


class NotificationsSettingsChangedObject(BaseEventObject):
    peer_id: Optional[int] = None
    sound: Optional[int] = None
    disabled_until: Optional[int] = None


class ChatInfoEditObject(BaseEventObject):
    type_id: Optional[int] = None
    peer_id: Optional[int] = None
    info: Optional[Union[str, int]] = None


class ChatVoiceMessageStatesObject(BaseEventObject):
    user_ids: Optional[List[int]] = None
    peer_id: Optional[int] = None
    total_count: Optional[int] = None
    ts: Optional[int] = None


class ChatEditObject(BaseEventObject):
    chat_id: Optional[int] = None
    self: Optional[int] = None


class ActionType(enum.IntEnum):
    ACCEPT = 2
    REMOVE_OR_CANCEL = 3


class FriendActionObject(BaseEventObject):
    action_type: Optional[ActionType] = None
    user_id: Optional[int] = None


class CreateFolderObject(BaseEventObject):
    folder_id: Optional[int] = None
    folder_name: Optional[str] = None
    random_id: Optional[int] = None


class DeleteFolderObject(BaseEventObject):
    folder_id: Optional[int] = None


class RenameFolderObject(BaseEventObject):
    folder_id: Optional[int] = None
    new_folder_name: Optional[str] = None


class AddConversationsToFolderObject(BaseEventObject):
    folder_id: Optional[int] = None
    peer_ids: Optional[List[int]] = None


class RemoveConversationsFromFolderObject(BaseEventObject):
    folder_id: Optional[int] = None
    peer_ids: Optional[List[int]] = None


class ChangeFolderOrderObject(BaseEventObject):
    folder_ids: Optional[List[int]] = None


class CounterUnreadDialogsInFoldersObject(BaseEventObject):
    folder_id: Optional[int] = None
    unread_count: Optional[int] = None
    unread_unmuted_count: Optional[int] = None


__all__ = (
    "AddConversationsToFolderObject",
    "CallObject",
    "ChatEditObject",
    "ChatInfoEditObject",
    "ChatVoiceMessageStatesObject",
    "ChangeConversationParamsObject",
    "ChangeFolderOrderObject",
    "ConversationTypingStateObject",
    "CounterObject",
    "CounterUnreadDialogsInFoldersObject",
    "CreateFolderObject",
    "DeleteFolderObject",
    "DialogTypingStateObject",
    "FriendActionObject",
    "FriendOfflineObject",
    "FriendOnlineObject",
    "InReadObject",
    "InstallDialogFlagsObject",
    "InstallMessageFlagsObject",
    "MessagesDeleteObject",
    "MessagesRestoreObject",
    "NotificationsSettingsChangedObject",
    "OutReadObject",
    "RemoveConversationsFromFolderObject",
    "ReplaceDialogFlagsObject",
    "ReplaceMessageFlagsObject",
    "ResetDialogFlagsObject",
    "ResetMessageFlagsObject",
    "RenameFolderObject",
    "UsersTypingStateObject",
)
