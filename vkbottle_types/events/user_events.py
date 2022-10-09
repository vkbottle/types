import inspect
from typing import TYPE_CHECKING, Any, List, Optional, Union

from pydantic import BaseModel

from .objects import BaseEventObject, user_event_objects

if TYPE_CHECKING:
    from vkbottle import ABCAPI, API


class BaseUserEvent(BaseModel):
    unprepared_ctx_api: Optional[Any] = None
    object: Optional["BaseEventObject"] = None

    def __init__(self, *args, **data: Any) -> None:
        data["object"] = args
        super().__init__(**data)

    @property
    def ctx_api(self) -> Union["ABCAPI", "API"]:
        return self.unprepared_ctx_api  # type: ignore


class RawUserEvent(BaseUserEvent):
    object: List[Any]


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


_locals = locals().copy()
_locals_values = _locals.values()
for item in _locals_values:
    if inspect.isclass(item) and issubclass(item, BaseUserEvent):
        item.update_forward_refs(**_locals)

__all__ = (
    "BaseUserEvent",
    "Call",
    "ChatEdit",
    "ChatInfoEdit",
    "ChatTypingState",
    "ChatVoiceMessageStates",
    "Counter",
    "DialogTypingState",
    "FriendOffline",
    "FriendOnline",
    "InRead",
    "InstallDialogFlags",
    "InstallMessageFlags",
    "MessageEdit",
    "MessageNew",
    "MessagesDelete",
    "MessagesRestore",
    "NotificationsSettingsChanged",
    "OutRead",
    "RawUserEvent",
    "ReplaceDialogFlags",
    "ReplaceMessageFlags",
    "ResetDialogFlags",
    "ResetMessageFlags",
    "UsersTypingState",
)
