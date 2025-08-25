import msgspec
from typing_extensions import TYPE_CHECKING, Any, Dict, List, Optional, Self, Union

from .objects import user_event_objects

if TYPE_CHECKING:
    from vkbottle import ABCAPI, API  # type: ignore


class BaseUserEvent(msgspec.Struct, omit_defaults=True):
    object: Optional[Any]
    unprepared_ctx_api: Optional[Any] = None

    @classmethod
    def from_raw(cls, data: bytes) -> Self:
        return msgspec.json.decode(data, type=cls)

    @classmethod
    def parse(cls, obj: List[Any]) -> Self:
        return msgspec.convert({"object": obj}, type=cls)

    def to_dict(self) -> Dict[str, Any]:
        return msgspec.structs.asdict(self)

    @property
    def ctx_api(self) -> Union["ABCAPI", "API"]:
        assert self.unprepared_ctx_api is not None
        return self.unprepared_ctx_api


class RawUserEvent(BaseUserEvent):
    object: List[Any]


class MessageFlagsReplace(BaseUserEvent):
    object: user_event_objects.MessageFlagsReplaceObject


class MessageSetFlags(BaseUserEvent):
    object: user_event_objects.MessageSetFlagsObject


class MessageResetFlags(BaseUserEvent):
    object: user_event_objects.MessageResetFlagsObject


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


class DialogResetFlags(BaseUserEvent):
    object: user_event_objects.DialogResetFlagsObject


class DialogFlagsReplace(BaseUserEvent):
    object: user_event_objects.DialogFlagsReplaceObject


class DialogSetFlags(BaseUserEvent):
    object: user_event_objects.DialogSetFlagsObject


class FriendOnline(BaseUserEvent):
    object: user_event_objects.FriendOnlineObject


class FriendOffline(BaseUserEvent):
    object: user_event_objects.FriendOfflineObject


class FriendAction(BaseUserEvent):
    object: user_event_objects.FriendActionObject


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


class CreateFolder(BaseUserEvent):
    object: user_event_objects.CreateFolderObject


class DeleteFolder(BaseUserEvent):
    object: user_event_objects.DeleteFolderObject


class RenameFolder(BaseUserEvent):
    object: user_event_objects.RenameFolderObject


class AddConversationsToFolder(BaseUserEvent):
    object: user_event_objects.AddConversationsToFolderObject


class RemoveConversationsFromFolder(BaseUserEvent):
    object: user_event_objects.RemoveConversationsFromFolderObject


class ChangeFolderOrder(BaseUserEvent):
    object: user_event_objects.ChangeFolderOrderObject


class CounterUnreadDialogsInFolders(BaseUserEvent):
    object: List[user_event_objects.CounterUnreadDialogsInFoldersObject]


__all__ = (
    "AddConversationsToFolder",
    "BaseUserEvent",
    "Call",
    "ChangeFolderOrder",
    "ChatEdit",
    "ChatInfoEdit",
    "ChatTypingState",
    "ChatVoiceMessageStates",
    "Counter",
    "CounterUnreadDialogsInFolders",
    "CreateFolder",
    "DeleteFolder",
    "DialogTypingState",
    "FriendOffline",
    "FriendOnline",
    "InRead",
    "MessageFlagsReplace",
    "MessageSetFlags",
    "MessageResetFlags",
    "MessageEdit",
    "MessageNew",
    "MessagesDelete",
    "MessagesRestore",
    "NotificationsSettingsChanged",
    "OutRead",
    "RawUserEvent",
    "RemoveConversationsFromFolder",
    "RenameFolder",
    "DialogFlagsReplace",
    "DialogResetFlags",
    "DialogSetFlags",
    "UsersTypingState",
)
