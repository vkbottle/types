from .enums import UserEventType
from .objects import BaseEventObject, user_event_objects
from .events_base import EventsBase
from pydantic import BaseModel
from typing import Optional, Any, Union, TYPE_CHECKING

if TYPE_CHECKING:
    from vkbottle import ABCAPI, API


class BaseUserEvent(BaseModel):
    unprepared_ctx_api: Optional[Any] = None

    @property
    def ctx_api(self) -> Optional[Union["ABCAPI", "API"]]:
        return getattr(self, "unprepared_ctx_api")


class Message(BaseUserEvent):
	object: "user_event_objects.MessageObject"


class MessageNew(BaseUserEvent):
	object: "user_event_objects.MessageNewObject"


class MessagesDelete(BaseUserEvent):
	object: "user_event_objects.DeleteMessagesObject"


class MessageRestore(BaseUserEvent):
	object: "user_event_objects.RestoreDeletedObject"


class EditMessage(BaseUserEvent):
	object: "user_event_objects.EditMessageObject"


class ReplaceMessageFlags(BaseUserEvent):
	object: "user_event_objects.ReplaceMessageFlagsObject"


class InstallMessageFlags(BaseUserEvent):
	object: "user_event_objects.InstallMessageFlagsObject"


class ResetMessageFlags(BaseUserEvent):
	object: "user_event_objects.ResetMessageFlagsObject"


class ChatVoiceMessageStates(BaseUserEvent):
	object: "user_event_objects.ChatVoiceMessageStatesObject"


class ChatEdit(BaseUserEvent):
	object: "user_event_objects.ChatEditObject"


class ChatInfoEdit(BaseUserEvent):
	object: "user_event_objects.ChatInfoEditObject"


class ChatTypingState(BaseUserEvent):
	object: "user_event_objects.ConversationTypingStateObject"


class ChangeConversationParams(BaseUserEvent):
	object: "user_event_objects.ChangeConversationParamsObject"


class DialogTypingState(BaseUserEvent):
	object: "user_event_objects.DialogTypingStateObject"


class ResetDialogFlags(BaseUserEvent):
	object: "user_event_objects.ResetDialogFlagsObject"


class ReplaceDialogFlags(BaseUserEvent):
	object: "user_event_objects.ReplaceDialogFlagsObject"


class InstallDialogFlags(BaseUserEvent):
	object: "user_event_objects.InstallDialogFlagsObject"


class FriendOnline(BaseUserEvent):
	object: "user_event_objects.FriendOnlineObject"


class FriendOffline(BaseUserEvent):
	object: "user_event_objects.FriendOfflineObject"


class Counter(BaseUserEvent):
	object: "user_event_objects.CounterObject"


class Call(BaseUserEvent):
	object: "user_event_objects.CallObject"


class ChangedNotificationsSettings(BaseUserEvent):
	object: "user_event_objects.ChangedNotificationsSettingsObject"


class InRead(BaseUserEvent):
	object: "user_event_objects.InReadObject"


class OutRead(BaseUserEvent):
	object: "user_event_objects.OutReadObject"


MessageNew.update_forward_refs()
MessagesDelete.update_forward_refs()
MessageRestore.update_forward_refs()
EditMessage.update_forward_refs()
ReplaceMessageFlags.update_forward_refs()
InstallMessageFlags.update_forward_refs()
ResetMessageFlags.update_forward_refs()
ChatVoiceMessageStates.update_forward_refs()
ChatEdit.update_forward_refs()
ChatInfoEdit.update_forward_refs()
ChatTypingState.update_forward_refs()
ChangeConversationParams.update_forward_refs()
DialogTypingState.update_forward_refs()
ResetDialogFlags.update_forward_refs()
ReplaceDialogFlags.update_forward_refs()
InstallDialogFlags.update_forward_refs()
FriendOnline.update_forward_refs()
FriendOffline.update_forward_refs()
Counter.update_forward_refs()
Call.update_forward_refs()
ChangedNotificationsSettings.update_forward_refs()
InRead.update_forward_refs()
OutRead.update_forward_refs()

DEFAULT_EVENTS_BASE_USER = EventsBase(UserEventType)
DEFAULT_EVENTS_BASE_USER.register(UserEventType.NEW_MESSAGE, MessageNew)
DEFAULT_EVENTS_BASE_USER.register(UserEventType.DELETE_MESSAGES, MessagesDelete)
DEFAULT_EVENTS_BASE_USER.register(UserEventType.EDIT_MESSAGE, EditMessage)
DEFAULT_EVENTS_BASE_USER.register(UserEventType.MESSAGE_RESTORE, MessageRestore)
DEFAULT_EVENTS_BASE_USER.register(UserEventType.INSTALL_MESSAGE_FLAGS, InstallMessageFlags)
DEFAULT_EVENTS_BASE_USER.register(UserEventType.REPLACE_MESSAGE_FLAGS, ReplaceMessageFlags)
DEFAULT_EVENTS_BASE_USER.register(UserEventType.RESET_MESSAGE_FLAGS, ResetMessageFlags)
DEFAULT_EVENTS_BASE_USER.register(UserEventType.IN_READ, InRead)
DEFAULT_EVENTS_BASE_USER.register(UserEventType.OUT_READ, OutRead)
DEFAULT_EVENTS_BASE_USER.register(UserEventType.CHAT_INFO_EDIT, ChatInfoEdit)
DEFAULT_EVENTS_BASE_USER.register(UserEventType.CALL, Call)
DEFAULT_EVENTS_BASE_USER.register(UserEventType.COUNTER, Counter)
DEFAULT_EVENTS_BASE_USER.register(UserEventType.NOTIFICATIONS_SETTINGS_CHANGED, ChangedNotificationsSettings)
DEFAULT_EVENTS_BASE_USER.register(UserEventType.FRIEND_ONLINE, FriendOnline)
DEFAULT_EVENTS_BASE_USER.register(UserEventType.FRIEND_OFFLINE, FriendOffline)
DEFAULT_EVENTS_BASE_USER.register(UserEventType.USER_TYPING_STATE, DialogTypingState)
DEFAULT_EVENTS_BASE_USER.register(UserEventType.USERS_TYPING_STATE, ChatTypingState)
DEFAULT_EVENTS_BASE_USER.register(UserEventType.RESET_DIALOG_FLAGS, ResetDialogFlags)
DEFAULT_EVENTS_BASE_USER.register(UserEventType.REPLACE_DIALOG_FLAGS, ReplaceDialogFlags)
DEFAULT_EVENTS_BASE_USER.register(UserEventType.INSTALL_DIALOG_FLAGS, InstallDialogFlags)
DEFAULT_EVENTS_BASE_USER.register(UserEventType.NOTIFICATIONS_SETTINGS_CHANGED, ChatVoiceMessageStates)
