from .base_event_object import BaseEventObject
from vkbottle_types.objects import MessagesMessage
from typing import Optional, Union, List


class MessageObject(BaseEventObject):
    message_id: Optional[int] = None
    peer_id: Optional[int] = None
    timestamp: Optional[int] = None
    text: Optional[str] = None
    subject: Optional[str] = None
    info: Optional[str] = None
    attachments: Optional[Union[dict, list]] = None
    random_id: Optional[int] = None


class MessageNewObject(MessagesMessage):
    pass


class ReplaceMessageFlagsObject(MessageObject):
    flags: Optional[int] = None


class InstallMessageFlagsObject(MessageObject):
    mask: Optional[int] = None


class ResetMessageFlagsObject(MessageObject):
    mask: Optional[int] = None


class EditMessageObject(BaseEventObject):
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


class DeleteMessagesObject(InReadObject):
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


class CallObject(BaseEventObject):
    user_id: Optional[int] = None
    call_id: Optional[int] = None


class CounterObject(BaseEventObject):
    count: Optional[int] = None


class ChangedNotificationsSettingsObject(BaseEventObject):
    peer_id: Optional[int] = None
    sound: Optional[int] = None
    disabled_until: Optional[int] = None


class RestoreDeletedObject(DeleteMessagesObject):
    pass


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


MessageObject.update_forward_refs()
ReplaceMessageFlagsObject.update_forward_refs()
InstallMessageFlagsObject.update_forward_refs()
ResetMessageFlagsObject.update_forward_refs()
EditMessageObject.update_forward_refs()
InReadObject.update_forward_refs()
OutReadObject.update_forward_refs()
FriendOnlineObject.update_forward_refs()
FriendOfflineObject.update_forward_refs()
ResetDialogFlagsObject.update_forward_refs()
ReplaceDialogFlagsObject.update_forward_refs()
InstallDialogFlagsObject.update_forward_refs()
DeleteMessagesObject.update_forward_refs()
ChangeConversationParamsObject.update_forward_refs()
DialogTypingStateObject.update_forward_refs()
ConversationTypingStateObject.update_forward_refs()
CallObject.update_forward_refs()
CounterObject.update_forward_refs()
ChangedNotificationsSettingsObject.update_forward_refs()
RestoreDeletedObject.update_forward_refs()
ChatInfoEditObject.update_forward_refs()
ChatVoiceMessageStatesObject.update_forward_refs()
ChatEditObject.update_forward_refs()
