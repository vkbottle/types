from enum import Enum

from typing_extensions import List, Optional, TypeAlias, Union

from vkbottle_types.base_model import BaseEnumMeta, BaseModel, Field
from vkbottle_types.codegen.objects import *  # noqa: F403  # type: ignore


class MessagesMessageActionStatus(str, Enum, metaclass=BaseEnumMeta):  # type: ignore
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


class MessagesMessageAttachmentType(str, Enum, metaclass=BaseEnumMeta):  # type: ignore
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
    MINI_APP = "mini_app"
    VIDEO_PLAYLIST = "video_playlist"
    NARRATIVE = "narrative"


class VideoVideoType(str, Enum, metaclass=BaseEnumMeta):  # type: ignore
    INTERACTIVE = "interactive"
    VIDEO = "video"
    MUSIC_VIDEO = "music_video"
    MOVIE = "movie"
    VIDEO_MESSAGE = "video_message"
    LIVE = "live"
    SHORT_VIDEO = "short_video"
    STORY = "story"


class WallWallpostAttachmentType(str, Enum, metaclass=BaseEnumMeta):  # type: ignore
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
    PRETTY_CARDS = "pretty_cards"
    MINI_APP = "mini_app"
    CLIP = "clip"
    VIDEO_PLAYLIST = "video_playlist"


class PhotosPhoto(PhotosPhoto):  # type: ignore
    orig_photo: Optional["PhotosPhotoSizes"] = None


class PrettyCardsList(BaseModel):
    cards: Optional[List["PrettyCardsPrettyCard"]] = None


class PollsPoll(PollsPoll):  # type: ignore[no-redef]
    anonymous: Optional[bool] = None  # type: ignore[assignment]


class WallWallpostAttachment(WallWallpostAttachment):  # type: ignore
    mini_app: Optional["AppsApp"] = None
    pretty_cards: Optional["PrettyCardsList"] = None
    poll: Optional["PollsPoll"] = None


class PollsPollExtended(PollsPoll):  # type: ignore[no-redef]
    pass


class CallbackLikeAddRemoveObjectType(str, Enum, metaclass=BaseEnumMeta):  # type: ignore[no-redef]
    VIDEO = "video"
    PHOTO = "photo"
    POST = "post"
    COMMENT = "comment"
    NOTE = "note"
    TOPIC_COMMENT = "topic_comment"
    PHOTO_COMMENT = "photo_comment"
    VIDEO_COMMENT = "video_comment"
    MARKET = "market"
    MARKET_COMMENT = "market_comment"
    CLIP = "clip"


class BaseLinkButtonActionType(str, Enum, metaclass=BaseEnumMeta):  # type: ignore
    OPEN_URL = "open_url"
    JOIN_GROUP_AND_OPEN_URL = "join_group_and_open_url"
    MARKET_CLEAR_RECENT_QUERIES = "market_clear_recent_queries"
    CLOSE_WEB_APP = "close_web_app"
    ADD_PLAYLIST = "add_playlist"
    OPEN_SEARCH_TAB = "open_search_tab"
    OPEN_SEARCH_FILTERS = "open_search_filters"
    RESET_SEARCH_FILTERS = "reset_search_filters"
    IMPORT_CONTACTS = "import_contacts"
    ADD_FRIENDS = "add_friends"
    ONBOARDING = "onboarding"
    SHOW_FILTERS = "show_filters"


class GroupsUserXtrRole(UsersUserFull, GroupsMemberRole):  # type: ignore
    pass


class MessagesMessageAction(MessagesMessageAction):  # type: ignore
    type: "MessagesMessageActionStatus"  # type: ignore
    style: Optional[str] = None


class GroupCallInProgress(CallsCall):
    receiver_id: Optional[int] = None  # type: ignore
    time: Optional[int] = None  # type: ignore
    join_link: Optional[str] = None
    state: Optional["CallsEndState"] = None  # type: ignore


class AppsApp(AppsApp):  # type: ignore
    id: Optional[int] = None  # type: ignore
    type: Optional[str] = None  # type: ignore


class MessagesAudioMessage(MessagesAudioMessage):  # type: ignore
    transcript_state: Optional[str] = None
    transcript: Optional[str] = None


class BaseLinkAttachment(BaseLink):
    photo: Optional["LinkPhoto"] = None


class LinkPhoto(PhotosPhoto):
    has_tags: Optional[bool] = None  # type: ignore
    date: Optional[int] = None  # type: ignore


class PhotosPhotoAlbumFull(PhotosPhotoAlbumFull):  # type: ignore
    created: Optional[int] = None
    updated: Optional[int] = None


class PhotosPhoto(PhotosPhoto):  # type: ignore
    has_tags: Optional[bool] = None  # type: ignore


class MessagesMessage(MessagesMessage):  # type: ignore
    attachments: Optional[List["MessagesMessageAttachment"]] = None
    reply_message: Optional["MessagesForeignMessage"] = None
    fwd_messages: Optional[List["MessagesForeignMessage"]] = None  # type: ignore


class MessagesForeignMessage(MessagesForeignMessage):  # type: ignore
    attachments: Optional[List["MessagesMessageAttachment"]] = None
    reply_message: Optional["MessagesForeignMessage"] = None
    fwd_messages: Optional[List["MessagesForeignMessage"]] = None


class MessagesPinnedMessage(MessagesPinnedMessage):  # type: ignore
    attachments: Optional[List["MessagesMessageAttachment"]] = None
    reply_message: Optional["MessagesForeignMessage"] = None
    fwd_messages: Optional[List["MessagesForeignMessage"]] = None


class VideoVideo(VideoVideo):  # type: ignore
    type: Optional["VideoVideoType"] = None


class VideoVideoFull(VideoVideo, VideoVideoFull):  # type: ignore
    type: Optional["VideoVideoType"] = None


class MessagesSendUserIdsResponseItem(BaseModel):  # type: ignore
    conversation_message_id: Optional[int] = None
    error: Optional["BaseMessageError"] = None
    message_id: Optional[int]
    peer_id: int


class MessagesMessageAttachment(MessagesMessageAttachment):  # type: ignore
    audio_message: Optional["MessagesAudioMessage"] = None
    story: Optional["StoriesStory"] = None
    group_call_in_progress: Optional["GroupCallInProgress"] = None
    link: Optional["BaseLinkAttachment"] = None
    wall: Optional["WallWallpostFull"] = None
    photo: Optional["PhotosPhoto"] = None
    mini_app: Optional["AppsApp"] = None
    sticker: Optional["BaseSticker"] = None
    video: Optional["VideoVideoFull"] = None
    type: "MessagesMessageAttachmentType"  # type: ignore
    poll: Optional["PollsPoll"] = None
    # NOTE: Add `narrative` field. Now, we've no docs and schema about this attachment.


class BaseLinkNoProduct(BaseLinkNoProduct):  # type: ignore
    photo: Optional["PhotosPhoto"] = None


class BaseCropPhoto(BaseCropPhoto):  # type: ignore
    photo: "PhotosPhoto" = Field()


class BugtrackerAttachment(BugtrackerAttachment):  # type: ignore
    photo: Optional["PhotosPhoto"] = None


class CallbackGroupChangePhoto(CallbackGroupChangePhoto):  # type: ignore
    photo: "PhotosPhoto" = Field()


class MarketMarketAlbum(MarketMarketAlbum):  # type: ignore
    photo: Optional["PhotosPhoto"] = None


class MarketOrderItem(MarketOrderItem):  # type: ignore
    photo: Optional["PhotosPhoto"] = None


class MessagesHistoryMessageAttachment(MessagesHistoryMessageAttachment):  # type: ignore
    photo: Optional["PhotosPhoto"] = None


class PhotosPhotoAlbum(PhotosPhotoAlbum):  # type: ignore
    thumb: Optional["PhotosPhoto"] = None


class StoriesStory(StoriesStory):  # type: ignore
    photo: Optional["PhotosPhoto"] = None


class WallCommentAttachment(WallCommentAttachment):  # type: ignore
    photo: Optional["PhotosPhoto"] = None


class WallWallpostAttachment(WallWallpostAttachment):  # type: ignore
    photo: Optional["PhotosPhoto"] = None


class NewsfeedItemPhotoPhotos(NewsfeedItemPhotoPhotos):  # type: ignore
    items: Optional[List["PhotosPhoto"]] = None


class NewsfeedItemPhotoTagPhotoTags(NewsfeedItemPhotoTagPhotoTags):  # type: ignore
    items: Optional[List["PhotosPhoto"]] = None


class UsersUserFull(UsersUserFull):  # type: ignore
    photo_max_size: Optional["PhotosPhoto"] = None


class MarketMarketItemFull(MarketMarketItemFull):  # type: ignore
    photos: Optional[List["PhotosPhoto"]] = None


class MessagesKeyboardButtonPropertyAction(MessagesKeyboardButtonPropertyAction):  # type: ignore
    label: str = Field()
    type: str = Field()
    payload: str = Field()


class StoriesClickableSticker(StoriesClickableSticker):  # type: ignore[no-redef]
    poll: Optional["PollsPoll"] = None


class ClientInfoForBots(BaseModel):
    """
    Model: `ClientInfoForBots`
    """

    button_actions: Optional[List["MessagesTemplateActionTypeNames"]] = Field(
        default=None,
    )
    """Property `ClientInfoForBots.button_actions`."""

    keyboard: Optional[bool] = Field(
        default=None,
    )
    """client has support keyboard."""

    inline_keyboard: Optional[bool] = Field(
        default=None,
    )
    """client has support inline keyboard."""

    carousel: Optional[bool] = Field(
        default=None,
    )
    """client has support carousel."""

    lang_id: Optional[int] = Field(
        default=None,
    )
    """client or user language id."""


UsersSubscriptionsItem: TypeAlias = Union[GroupsGroupFull, UsersUserFull]  # type: ignore


localns = locals().copy()
for item in localns.values():
    if not (isinstance(item, type) and item is not BaseModel and issubclass(item, BaseModel)):
        continue

    item.model_rebuild(force=True, _types_namespace=localns)

    for parent in item.__bases__:
        if parent.__name__ == item.__name__ and issubclass(parent, BaseModel):
            parent.__pydantic_fields__.update(item.__pydantic_fields__)
            parent.model_rebuild(force=True, _types_namespace=localns)
            item.__pydantic_fields__.update(
                {name: field for name, field in parent.__pydantic_fields__.items() if name not in item.__pydantic_fields__},
            )
