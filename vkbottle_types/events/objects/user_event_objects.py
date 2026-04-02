import enum
from datetime import datetime, timezone
from functools import cached_property
from typing import Any

import msgspec

JsonObject = dict[str, Any] | list[Any]
Attachments = JsonObject
ExtraValues = JsonObject


class BaseEventObject(msgspec.Struct, omit_defaults=True, array_like=True, dict=True):
    pass


class MessageObject(BaseEventObject):
    message_id: int | None = None
    flags: int | None = None
    peer_id: int | None = None
    timestamp: int | None = None
    text: str | None = None
    extra_values: ExtraValues | None = None
    attachments: Attachments | None = None
    random_id: int | None = None

    @cached_property
    def date(self) -> datetime | None:
        if self.timestamp is None:
            return None
        return datetime.fromtimestamp(timestamp=self.timestamp, tz=timezone.utc)

    @property
    def message(self) -> str | None:
        if self.text is None:
            return None
        return self.text.replace("<br>", "\n").replace("&lt;", "<").replace("&gt;", ">").replace("&quot;", '"').replace("&amp;", "&")


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
    peer_id: int | None = None
    local_id: int | None = None


class OutReadObject(InReadObject):
    pass


class FriendOnlineObject(BaseEventObject):
    user_id: int | None = None
    extra: int = 0
    timestamp: int | None = None


class FriendOfflineObject(BaseEventObject):
    user_id: int | None = None
    flags: int = 0
    timestamp: int | None = None


class DialogResetFlagsObject(BaseEventObject):
    peer_id: int | None = None
    mask: int | None = None


class DialogFlagsReplaceObject(BaseEventObject):
    peer_id: int | None = None
    flags: int | None = None


class DialogSetFlagsObject(DialogResetFlagsObject):
    pass


class MessagesDeleteObject(InReadObject):
    pass


class MessagesRestoreObject(InReadObject):
    pass


class ChangeConversationParamsObject(BaseEventObject):
    chat_id: int | None = None
    self: int | None = None


class DialogTypingStateObject(BaseEventObject):
    user_id: int | None = None
    flags: int | None = None


class ConversationTypingStateObject(BaseEventObject):
    user_id: int | None = None
    chat_id: int | None = None


class UsersTypingStateObject(BaseEventObject):
    user_ids: list[int] | None = None
    peer_id: int | None = None
    total_count: int | None = None
    ts: int | None = None


class CallObject(BaseEventObject):
    user_id: int | None = None
    call_id: int | None = None


class CounterObject(BaseEventObject):
    count: int | None = None


class NotificationsSettingsChangedObject(BaseEventObject):
    peer_id: int | None = None
    sound: int | None = None
    disabled_until: int | None = None


class ChatInfoEditObject(BaseEventObject):
    type_id: int | None = None
    peer_id: int | None = None
    info: str | int | None = None


class ChatVoiceMessageStatesObject(BaseEventObject):
    user_ids: list[int] | None = None
    peer_id: int | None = None
    total_count: int | None = None
    ts: int | None = None


class ChatEditObject(BaseEventObject):
    chat_id: int | None = None
    self: int | None = None


class ActionType(enum.IntEnum):
    ACCEPT = 2
    REMOVE_OR_CANCEL = 3


class FriendActionObject(BaseEventObject):
    action_type: ActionType | None = None
    user_id: int | None = None


class CreateFolderObject(BaseEventObject):
    folder_id: int | None = None
    folder_name: str | None = None
    random_id: int | None = None


class DeleteFolderObject(BaseEventObject):
    folder_id: int | None = None


class RenameFolderObject(BaseEventObject):
    folder_id: int | None = None
    new_folder_name: str | None = None


class AddConversationsToFolderObject(BaseEventObject):
    folder_id: int | None = None
    peer_ids: list[int] | None = None


class RemoveConversationsFromFolderObject(BaseEventObject):
    folder_id: int | None = None
    peer_ids: list[int] | None = None


class ChangeFolderOrderObject(BaseEventObject):
    folder_ids: list[int] | None = None


class CounterUnreadDialogsInFoldersObject(BaseEventObject):
    folder_id: int | None = None
    unread_count: int | None = None
    unread_unmuted_count: int | None = None


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
    "DialogFlagsReplaceObject",
    "DialogResetFlagsObject",
    "DialogSetFlagsObject",
    "DialogTypingStateObject",
    "FriendActionObject",
    "FriendOfflineObject",
    "FriendOnlineObject",
    "InReadObject",
    "MessageEditObject",
    "MessageFlagsReplaceObject",
    "MessageFlagsReplaceObject",
    "MessageNewObject",
    "MessageObject",
    "MessageResetFlagsObject",
    "MessageResetFlagsObject",
    "MessageSetFlagsObject",
    "MessageSetFlagsObject",
    "MessagesDeleteObject",
    "MessagesRestoreObject",
    "NotificationsSettingsChangedObject",
    "OutReadObject",
    "RemoveConversationsFromFolderObject",
    "RenameFolderObject",
    "UsersTypingStateObject",
)
