import inspect
from typing import TYPE_CHECKING, Any, Optional, Union

from pydantic import BaseModel

from .enums import UserEventType
from .events_base import EventsBase
from .objects import user_event_objects

if TYPE_CHECKING:
    from vkbottle import ABCAPI, API


class BaseUserEvent(BaseModel):
    unprepared_ctx_api: Optional[Any] = None

    @property
    def ctx_api(self) -> Optional[Union["ABCAPI", "API"]]:
        return getattr(self, "unprepared_ctx_api")


class ReplaceMessageFlags(BaseUserEvent):
    object: user_event_objects.ReplaceMessageFlagsObject


class InstallMessageFlags(BaseUserEvent):
    object: user_event_objects.InstallMessageFlagsObject


class ResetMessageFlags(BaseUserEvent):
    object: user_event_objects.ResetMessageFlagsObject


class MessageNew(BaseUserEvent):
    object: user_event_objects.MessageNewObject


class MessagesDelete(BaseUserEvent):
    object: user_event_objects.MessagesDeleteObject


class MessagesRestore(BaseUserEvent):
    object: user_event_objects.MessagesRestoreObject


class MessageEdit(BaseUserEvent):
    object: user_event_objects.MessageEditObject


class ChatVoiceMessageStates(BaseUserEvent):
    object: user_event_objects.ChatVoiceMessageStatesObject


class ChatEdit(BaseUserEvent):
    object: user_event_objects.ChatEditObject


class ChatInfoEdit(BaseUserEvent):
    object: user_event_objects.ChatInfoEditObject


class ChatTypingState(BaseUserEvent):
    object: user_event_objects.ConversationTypingStateObject


class DialogTypingState(BaseUserEvent):
    object: user_event_objects.DialogTypingStateObject


class UsersTypingState(BaseUserEvent):
    object: user_event_objects.UsersTypingStateObject


class ResetDialogFlags(BaseUserEvent):
    object: user_event_objects.ResetDialogFlagsObject


class ReplaceDialogFlags(BaseUserEvent):
    object: user_event_objects.ReplaceDialogFlagsObject


class InstallDialogFlags(BaseUserEvent):
    object: user_event_objects.InstallDialogFlagsObject


class FriendOnline(BaseUserEvent):
    object: user_event_objects.FriendOnlineObject


class FriendOffline(BaseUserEvent):
    object: user_event_objects.FriendOfflineObject


class Counter(BaseUserEvent):
    object: user_event_objects.CounterObject


class Call(BaseUserEvent):
    object: user_event_objects.CallObject


class NotificationsSettingsChanged(BaseUserEvent):
    object: user_event_objects.NotificationsSettingsChangedObject


class InRead(BaseUserEvent):
    object: user_event_objects.InReadObject


class OutRead(BaseUserEvent):
    object: user_event_objects.OutReadObject


DEFAULT_EVENTS_BASE_USER = EventsBase(UserEventType)
for item in locals().copy().values():
    if (
        not inspect.isclass(item)
        or not issubclass(item, BaseUserEvent)
        or item is BaseUserEvent
    ):
        continue
    item.update_forward_refs()
    event_type = UserEventType[
        "".join("_" + i if i.isupper() else i for i in item.__name__)
        .lstrip("_")
        .upper()
    ]
    DEFAULT_EVENTS_BASE_USER.register(event_type, item)
__all__ = (
    "DEFAULT_EVENTS_BASE_USER",
    "BaseUserEvent",
    "ReplaceMessageFlags",
    "InstallMessageFlags",
    "ResetMessageFlags",
    "MessageNew",
    "MessagesDelete",
    "MessagesRestore",
    "MessageEdit",
    "ChatVoiceMessageStates",
    "ChatEdit",
    "ChatInfoEdit",
    "ChatTypingState",
    "DialogTypingState",
    "UsersTypingState",
    "ResetDialogFlags",
    "ReplaceDialogFlags",
    "InstallDialogFlags",
    "FriendOnline",
    "FriendOffline",
    "Counter",
    "Call",
    "NotificationsSettingsChanged",
    "InRead",
    "OutRead",
)
