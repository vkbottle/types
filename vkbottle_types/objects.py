# flake8: noqa: F405
import inspect
from pydantic import BaseModel
from enum import Enum
from typing import Optional
from vkbottle_types.codegen.objects import *  # noqa: F403,F401

# There is too many objects to import, so we will use * to import them all


class GroupCallInProgress(CallsCall):
    """VK Object GroupCallInProgress"""

    receiver_id: Optional[int] = None
    time: Optional[int] = None
    join_link: Optional[str] = None
    state: Optional["CallsEndState"] = None


class GroupsUserXtrRole(UsersUserFull, GroupsMemberRole):
    """VK Object GroupsUserXtrRole"""

    pass


class MessagesHistoryMessageAttachment(BaseModel):
    """VK Object MessagesHistoryMessageAttachment"""

    share: Optional["BaseLink"] = None


class MessagesMessageAction(MessagesMessageAction):
    """VK Object MessagesMessageAction

    conversation_message_id - Message ID
    email - Email address for chat_invite_user or chat_kick_user actions
    member_id - User or email peer ID
    message - Message body of related message
    photo -
    text - New chat title for chat_create and chat_title_update actions
    type -
    """

    style: Optional[str] = None


class MessagesMessageActionStatus(Enum):
    """Action status"""

    CHAT_PHOTO_UPDATE = "chat_photo_update"
    CHAT_PHOTO_REMOVE = "chat_photo_remove"
    CHAT_CREATE = "chat_create"
    CHAT_TITLE_UPDATE = "chat_title_update"
    CHAT_INVITE_USER = "chat_invite_user"
    CHAT_KICK_USER = "chat_kick_user"
    CHAT_PIN_MESSAGE = "chat_pin_message"
    CHAT_UNPIN_MESSAGE = "chat_unpin_message"
    CHAT_INVITE_USER_BY_LINK = "chat_invite_user_by_link"
    CHAT_INVITE_USER_BY_MESSAGE_REQUEST = "chat_invite_user_by_message_request"
    CHAT_SCREENSHOT = "chat_screenshot"


class MessagesMessageAttachment(MessagesMessageAttachment):
    """VK Object MessagesMessageAttachment"""

    group_call_in_progress: Optional["GroupCallInProgress"] = None
    link: Optional["BaseLink"] = None
    wall: Optional["WallWallpostFull"] = None


class MessagesMessageAttachmentType(Enum):
    """Attachment type"""

    PHOTO = "photo"
    AUDIO = "audio"
    VIDEO = "video"
    DOC = "doc"
    LINK = "link"
    MARKET = "market"
    MARKET_ALBUM = "market_album"
    GIFT = "gift"
    STICKER = "sticker"
    WALL = "wall"
    WALL_REPLY = "wall_reply"
    ARTICLE = "article"
    POLL = "poll"
    CALL = "call"
    GRAFFITI = "graffiti"
    AUDIO_MESSAGE = "audio_message"
    STORY = "story"
    GROUP_CALL_IN_PROGRESS = "group_call_in_progress"


class MessagesSendUserIdsResponseItem(BaseModel):
    """VK Object MessagesSendUserIdsResponseItem"""

    conversation_message_id: Optional[int] = None
    error: Optional["BaseMessageError"] = None
    message_id: Optional[int]
    peer_id: int


GroupCallInProgress.update_forward_refs()
GroupsUserXtrRole.update_forward_refs()
MessagesHistoryMessageAttachment.update_forward_refs()
MessagesMessageAction.update_forward_refs()
MessagesMessageAttachment.update_forward_refs()
MessagesSendUserIdsResponseItem.update_forward_refs()
NewsfeedItemWallpost.update_forward_refs()
