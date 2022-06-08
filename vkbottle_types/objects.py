# flake8: noqa: F405
import inspect
from enum import Enum
from typing import List, Optional

from vkbottle_types.codegen.objects import *  # noqa: F403,F401

from vkbottle_types.base_model import BaseModel


class MessagesMessageActionStatus(Enum):
    # https://github.com/VKCOM/vk-api-schema/issues/226
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
    CONVERSATION_STYLE_UPDATE = "conversation_style_update"


class MessagesMessageAttachmentType(Enum):
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
    GROUP_CALL_IN_PROGRESS = (
        "group_call_in_progress"  # https://github.com/VKCOM/vk-api-schema/issues/225
    )


class VideoVideoType(Enum):
    VIDEO = "video"
    MUSIC_VIDEO = "music_video"
    MOVIE = "movie"
    SHORT_VIDEO = "short_video"  # https://github.com/VKCOM/vk-api-schema/issues/212


class GroupsUserXtrRole(UsersUserFull, GroupsMemberRole):
    #  https://github.com/VKCOM/vk-api-schema/issues/224
    pass


class MessagesMessageAction(MessagesMessageAction):
    # https://github.com/VKCOM/vk-api-schema/issues/226
    type: "MessagesMessageActionStatus"
    style: Optional[str] = None


class GroupCallInProgress(CallsCall):
    # https://github.com/VKCOM/vk-api-schema/issues/225
    receiver_id: Optional[int] = None
    time: Optional[int] = None
    join_link: Optional[str] = None
    state: Optional["CallsEndState"] = None


class MessagesMessageAttachment(MessagesMessageAttachment):
    # https://github.com/VKCOM/vk-api-schema/issues/225
    story: Optional["StoriesStory"] = None
    group_call_in_progress: Optional["GroupCallInProgress"] = None
    link: Optional["BaseLinkAttachment"] = None
    wall: Optional["WallWallpostFull"] = None
    type: "MessagesMessageAttachmentType"


class BaseLinkAttachment(BaseLink):
    # https://github.com/VKCOM/vk-api-schema/issues/225
    photo: Optional["LinkPhoto"] = None


class LinkPhoto(PhotosPhoto):
    # https://github.com/VKCOM/vk-api-schema/issues/225
    has_tags: Optional[bool] = None
    date: Optional[int] = None


class MessagesMessage(MessagesMessage):
    # https://github.com/VKCOM/vk-api-schema/issues/225
    attachments: Optional[List["MessagesMessageAttachment"]] = None
    reply_message: Optional["MessagesForeignMessage"] = None
    fwd_messages: Optional[List["MessagesForeignMessage"]] = None


class MessagesForeignMessage(MessagesForeignMessage):
    # https://github.com/VKCOM/vk-api-schema/issues/225
    attachments: Optional[List["MessagesMessageAttachment"]] = None
    reply_message: Optional["MessagesForeignMessage"] = None
    fwd_messages: Optional[List["MessagesForeignMessage"]] = None


class VideoVideo(VideoVideo):
    # https://github.com/VKCOM/vk-api-schema/issues/212
    type: Optional["VideoVideoType"] = None


class VideoVideoFull(VideoVideo, VideoVideoFull):
    # https://github.com/VKCOM/vk-api-schema/issues/212
    pass


class MessagesSendUserIdsResponseItem(BaseModel):
    # https://github.com/VKCOM/vk-api-schema/issues/208
    conversation_message_id: Optional[int] = None
    error: Optional["BaseMessageError"] = None
    message_id: Optional[int]
    peer_id: int


_locals = locals().copy()
_locals_values = _locals.values()
for item in _locals_values:
    if not (inspect.isclass(item) and issubclass(item, BaseModel)):
        continue
    item.update_forward_refs(**_locals)
    for parent in item.__bases__:
        if parent.__name__ == item.__name__:
            parent.update_forward_refs(**_locals)  # type: ignore
