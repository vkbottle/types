import inspect
from typing import List, Optional, Union

from .base_event_object import BaseEventObject


class MessageObject(BaseEventObject):
    message_id: Optional[int] = None
    peer_id: Optional[int] = None
    timestamp: Optional[int] = None
    text: Optional[str] = None
    subject: Optional[str] = None
    info: Optional[str] = None
    attachments: Optional[Union[dict, list]] = None
    random_id: Optional[int] = None


class ReplaceMessageFlagsObject(MessageObject):
    flags: Optional[int] = None


class InstallMessageFlagsObject(MessageObject):
    mask: Optional[int] = None


class ResetMessageFlagsObject(MessageObject):
    mask: Optional[int] = None


class MessageNewObject(MessageObject):
    minor_id: Optional[int] = None
    flags: Optional[int] = None


class MessageEditObject(BaseEventObject):
    message_id: Optional[int] = None
    mask: Optional[int] = None
    peer_id: Optional[int] = None
    timestamp: Optional[int] = None
    new_text: Optional[str] = ""
    attachments: Optional[Union[dict, list]] = None


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


_locals = locals().copy()
_locals_values = _locals.values()
for item in _locals_values:
    if inspect.isclass(item) and issubclass(item, BaseEventObject):
        item.update_forward_refs(**_locals)
