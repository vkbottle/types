# flake8: noqa: F405
import inspect
from enum import Enum
from typing import List, Optional

from vkbottle_types.base_model import BaseModel
from vkbottle_types.codegen.objects import *  # noqa: F403  # type: ignore


class MessagesMessageActionStatus(Enum):  # type: ignore
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


class MessagesMessageAttachmentType(Enum):  # type: ignore
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
    GROUP_CALL_IN_PROGRESS = "group_call_in_progress"  # https://github.com/VKCOM/vk-api-schema/issues/225
    MINI_APP = "mini_app"  # https://github.com/VKCOM/vk-api-schema/issues/225


class VideoVideoType(Enum):  # type: ignore
    VIDEO = "video"
    MUSIC_VIDEO = "music_video"
    MOVIE = "movie"
    SHORT_VIDEO = "short_video"  # https://github.com/VKCOM/vk-api-schema/issues/212
    LIVE = "live"  # https://github.com/VKCOM/vk-api-schema/issues/230


class WallWallpostAttachmentType(Enum):  # type: ignore
    """Attachment type"""

    PHOTO = "photo"
    PHOTOS_LIST = "photos_list"
    POSTED_PHOTO = "posted_photo"
    AUDIO = "audio"
    AUDIO_PLAYLIST = "audio_playlist"
    VIDEO = "video"
    DOC = "doc"
    LINK = "link"
    GRAFFITI = "graffiti"
    NOTE = "note"
    APP = "app"
    POLL = "poll"
    PAGE = "page"
    ALBUM = "album"
    MARKET_ALBUM = "market_album"
    MARKET = "market"
    EVENT = "event"
    DONUT_LINK = "donut_link"
    ARTICLE = "article"
    TEXTLIVE = "textlive"
    TEXTPOST = "textpost"
    TEXTPOST_PUBLISH = "textpost_publish"
    SITUATIONAL_THEME = "situational_theme"
    GROUP = "group"
    STICKER = "sticker"
    PODCAST = "podcast"
    PRETTY_CARDS = "pretty_cards"  # https://github.com/VKCOM/vk-api-schema/issues/232
    MINI_APP = "mini_app"  # https://github.com/VKCOM/vk-api-schema/issues/225


class PrettyCardsList(BaseModel):
    cards: Optional[List["PrettyCardsPrettyCard"]] = None


class WallWallpostAttachment(WallWallpostAttachment):  # type: ignore
    mini_app: Optional["AppsApp"] = None
    pretty_cards: Optional["PrettyCardsList"] = None


class WallCommentAttachmentType(Enum):  # type: ignore
    """Attachment type"""

    PHOTO = "photo"
    AUDIO = "audio"
    VIDEO = "video"
    DOC = "doc"
    LINK = "link"
    NOTE = "note"
    PAGE = "page"
    MARKET_MARKET_ALBUM = "market_market_album"
    MARKET = "market"
    STICKER = "sticker"
    GRAFFITI = "graffiti"  # https://github.com/VKCOM/vk-api-schema/issues/233


class BaseLinkButtonActionType(Enum):  # type: ignore
    # https://github.com/VKCOM/vk-api-schema/issues/227
    OPEN_URL = "open_url"
    JOIN_GROUP_AND_OPEN_URL = "join_group_and_open_url"


class GroupsUserXtrRole(UsersUserFull, GroupsMemberRole):  # type: ignore
    # https://github.com/VKCOM/vk-api-schema/issues/224
    pass


class MessagesMessageAction(MessagesMessageAction):  # type: ignore
    # https://github.com/VKCOM/vk-api-schema/issues/226
    type: "MessagesMessageActionStatus"
    style: Optional[str] = None


class GroupCallInProgress(CallsCall):
    # https://github.com/VKCOM/vk-api-schema/issues/225
    receiver_id: Optional[int] = None  # type: ignore
    time: Optional[int] = None  # type: ignore
    join_link: Optional[str] = None
    state: Optional["CallsEndState"] = None  # type: ignore


class AppsApp(AppsApp):  # type: ignore
    id: Optional[int] = None  # type: ignore
    type: Optional[str] = None  # type: ignore


class MessagesMessageAttachment(MessagesMessageAttachment):  # type: ignore
    # https://github.com/VKCOM/vk-api-schema/issues/225
    sticker: Optional["BaseStickerNew"] = None  # type: ignore
    story: Optional["StoriesStory"] = None
    group_call_in_progress: Optional["GroupCallInProgress"] = None
    link: Optional["BaseLinkAttachment"] = None
    wall: Optional["WallWallpostFull"] = None
    mini_app: Optional["AppsApp"] = None
    type: "MessagesMessageAttachmentType"


class MessagesAudioMessage(MessagesAudioMessage):  # type: ignore
    # https://github.com/VKCOM/vk-api-schema/issues/236
    transcript_state: Optional[str] = None
    transcript: Optional[str] = None


class BaseLinkAttachment(BaseLink):
    # https://github.com/VKCOM/vk-api-schema/issues/225
    photo: Optional["LinkPhoto"] = None


class LinkPhoto(PhotosPhoto):
    # https://github.com/VKCOM/vk-api-schema/issues/225
    has_tags: Optional[bool] = None  # type: ignore
    date: Optional[int] = None  # type: ignore


class PhotosPhotoAlbumFull(PhotosPhotoAlbumFull):  # type: ignore
    # https://github.com/VKCOM/vk-api-schema/issues/228
    created: Optional[int] = None
    updated: Optional[int] = None


class PhotosPhoto(PhotosPhoto):  # type: ignore
    # https://github.com/VKCOM/vk-api-schema/issues/229
    has_tags: Optional[bool] = None  # type: ignore


class MessagesMessage(MessagesMessage):  # type: ignore
    # https://github.com/VKCOM/vk-api-schema/issues/225
    attachments: Optional[List["MessagesMessageAttachment"]] = None
    reply_message: Optional["MessagesForeignMessage"] = None
    fwd_messages: Optional[List["MessagesForeignMessage"]] = None  # type: ignore


class MessagesForeignMessage(MessagesForeignMessage):  # type: ignore
    # https://github.com/VKCOM/vk-api-schema/issues/225
    attachments: Optional[List["MessagesMessageAttachment"]] = None
    reply_message: Optional["MessagesForeignMessage"] = None
    fwd_messages: Optional[List["MessagesForeignMessage"]] = None


class VideoVideo(VideoVideo):  # type: ignore
    # https://github.com/VKCOM/vk-api-schema/issues/212
    type: Optional["VideoVideoType"] = None


class VideoVideoFull(VideoVideo, VideoVideoFull):  # type: ignore
    # https://github.com/VKCOM/vk-api-schema/issues/212
    type: Optional["VideoVideoType"] = None


class MessagesSendUserIdsResponseItem(BaseModel):  # type: ignore
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
            parent.__fields__.update(item.__fields__)  # type: ignore
            parent.update_forward_refs(**_locals)  # type: ignore
