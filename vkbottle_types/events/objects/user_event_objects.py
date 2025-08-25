import enum
from datetime import datetime, timezone
from functools import cached_property
from typing import Any, Dict, List, Optional, Union

import msgspec

JsonObject = Union[Dict[str, Any], List[Any]]
Attachments = JsonObject
ExtraValues = JsonObject


class BaseEventObject(msgspec.Struct, omit_defaults=True, array_like=True, dict=True):
    pass


class MessageObject(BaseEventObject):
    message_id: Optional[int] = None
    flags: Optional[int] = None
    peer_id: Optional[int] = None
    timestamp: Optional[int] = None
    text: Optional[str] = None
    extra_values: Optional[ExtraValues] = None
    attachments: Optional[Attachments] = None
    random_id: Optional[int] = None

    @cached_property
    def date(self) -> Optional[datetime]:
        if not self.timestamp:
            return None
        return datetime.fromtimestamp(timestamp=self.timestamp, tz=timezone.utc)

    @property
    def message(self) -> Optional[str]:
        if not self.text:
            return None
        return (
            self.text.replace("<br>", "\n")
            .replace("&lt;", "<")
            .replace("&gt;", ">")
            .replace("&quot;", '"')
            .replace("&amp;", "&")
        )


class MessageFlagsReplaceObject(MessageObject):
    pass


class MessageSetFlagsObject(MessageObject):
    pass


class MessageResetFlagsObject(MessageObject):
    pass


class MessageNewObject(MessageObject):
    pass


class MessageEditObject(MessageObject):
    pass


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


class DialogResetFlagsObject(BaseEventObject):
    peer_id: Optional[int] = None
    mask: Optional[int] = None


class DialogFlagsReplaceObject(BaseEventObject):
    peer_id: Optional[int] = None
    flags: Optional[int] = None


class DialogSetFlagsObject(DialogResetFlagsObject):
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
    "ChangeConversationParamsObject",
    "ChangeFolderOrderObject",
    "ChatEditObject",
    "ChatInfoEditObject",
    "ChatVoiceMessageStatesObject",
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
    "MessageEditObject",
    "MessageNewObject",
    "MessageObject",
    "MessageResetFlagsObject",
    "MessageFlagsReplaceObject",
    "MessageSetFlagsObject",
    "MessagesDeleteObject",
    "MessagesRestoreObject",
    "NotificationsSettingsChangedObject",
    "OutReadObject",
    "RemoveConversationsFromFolderObject",
    "RenameFolderObject",
    "DialogSetFlagsObject",
    "DialogFlagsReplaceObject",
    "DialogResetFlagsObject",
    "MessageFlagsReplaceObject",
    "MessageSetFlagsObject",
    "MessageResetFlagsObject",
    "UsersTypingStateObject",
)
