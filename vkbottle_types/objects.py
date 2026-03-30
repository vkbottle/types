from typing_extensions import TypeAlias

from vkbottle_types.base_model import BaseEnumMeta, BaseModel, Field, StrEnum
from vkbottle_types.codegen.objects import *  # noqa: F403  # type: ignore


class MessagesMessageActionStatus(StrEnum, metaclass=BaseEnumMeta):  # type: ignore
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


class MessagesMessageAttachmentType(StrEnum, metaclass=BaseEnumMeta):  # type: ignore
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


class VideoVideoType(StrEnum, metaclass=BaseEnumMeta):  # type: ignore
    INTERACTIVE = "interactive"
    VIDEO = "video"
    MUSIC_VIDEO = "music_video"
    MOVIE = "movie"
    VIDEO_MESSAGE = "video_message"
    LIVE = "live"
    SHORT_VIDEO = "short_video"
    STORY = "story"


class WallWallpostAttachmentType(StrEnum, metaclass=BaseEnumMeta):  # type: ignore
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
    orig_photo: "PhotosPhotoSizes | None" = None


class PrettyCardsList(BaseModel):
    cards: "PrettyCardsPrettyCard | None" = None


class PollsPoll(PollsPoll):  # type: ignore[no-redef]
    anonymous: bool | None = None  # type: ignore[assignment]


class WallWallpostAttachment(WallWallpostAttachment):  # type: ignore
    mini_app: "AppsApp | None" = None
    pretty_cards: "PrettyCardsList | None" = None
    poll: "PollsPoll | None" = None


class PollsPollExtended(PollsPoll):  # type: ignore[no-redef]
    pass


class CallbackLikeAddRemoveObjectType(StrEnum, metaclass=BaseEnumMeta):  # type: ignore[no-redef]
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


class BaseLinkButtonActionType(StrEnum, metaclass=BaseEnumMeta):  # type: ignore
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
    style: str | None = None


class GroupCallInProgress(CallsCall):
    receiver_id: int | None = None  # type: ignore
    time: int | None = None  # type: ignore
    join_link: str | None = None
    state: "CallsEndState | None" = None  # type: ignore


class AppsApp(AppsApp):  # type: ignore
    id: int | None = None  # type: ignore
    type: str | None = None  # type: ignore


class MessagesAudioMessage(MessagesAudioMessage):  # type: ignore
    transcript_state: str | None = None
    transcript: str | None = None


class BaseLinkAttachment(BaseLink):
    photo: "LinkPhoto | None" = None


class LinkPhoto(PhotosPhoto):
    has_tags: bool | None = None  # type: ignore
    date: int | None = None  # type: ignore


class PhotosPhotoAlbumFull(PhotosPhotoAlbumFull):  # type: ignore
    created: int | None = None
    updated: int | None = None


class PhotosPhoto(PhotosPhoto):  # type: ignore
    has_tags: bool | None = None  # type: ignore


class MessagesMessage(MessagesMessage):  # type: ignore
    attachments: list["MessagesMessageAttachment"] | None = None
    reply_message: "MessagesForeignMessage | None" = None
    fwd_messages: list["MessagesForeignMessage"] | None = None  # type: ignore


class MessagesForeignMessage(MessagesForeignMessage):  # type: ignore
    attachments: list["MessagesMessageAttachment"] | None = None
    reply_message: "MessagesForeignMessage | None" = None
    fwd_messages: list["MessagesForeignMessage"] | None = None


class MessagesPinnedMessage(MessagesPinnedMessage):  # type: ignore
    attachments: list["MessagesMessageAttachment"] | None = None
    reply_message: "MessagesForeignMessage | None" = None
    fwd_messages: list["MessagesForeignMessage"] | None = None


class VideoVideo(VideoVideo):  # type: ignore
    type: "VideoVideoType | None" = None


class VideoVideoFull(VideoVideo, VideoVideoFull):  # type: ignore
    type: "VideoVideoType | None" = None


class MessagesSendUserIdsResponseItem(BaseModel):  # type: ignore
    conversation_message_id: int | None = None
    error: "BaseMessageError | None" = None
    message_id: int | None
    peer_id: int


class MessagesMessageAttachment(MessagesMessageAttachment):  # type: ignore
    type: "MessagesMessageAttachmentType"  # type: ignore
    audio_message: "MessagesAudioMessage | None" = None
    story: "StoriesStory | None" = None
    group_call_in_progress: "GroupCallInProgress | None" = None
    link: "BaseLinkAttachment | None" = None
    wall: "WallWallpostFull | None" = None
    photo: "PhotosPhoto | None" = None
    mini_app: "AppsApp | None" = None
    sticker: "BaseSticker | None" = None
    video: "VideoVideoFull | None" = None
    poll: "PollsPoll | None" = None
    # NOTE: Add `narrative` field. Now, we've no docs and schema about this attachment.


class BaseLinkNoProduct(BaseLinkNoProduct):  # type: ignore
    photo: "PhotosPhoto | None" = None


class BaseCropPhoto(BaseCropPhoto):  # type: ignore
    photo: "PhotosPhoto" = Field()


class BugtrackerAttachment(BugtrackerAttachment):  # type: ignore
    photo: "PhotosPhoto | None" = None


class CallbackGroupChangePhoto(CallbackGroupChangePhoto):  # type: ignore
    photo: "PhotosPhoto" = Field()


class MarketMarketAlbum(MarketMarketAlbum):  # type: ignore
    photo: "PhotosPhoto | None" = None


class MarketOrderItem(MarketOrderItem):  # type: ignore
    photo: "PhotosPhoto | None" = None


class MessagesHistoryMessageAttachment(MessagesHistoryMessageAttachment):  # type: ignore
    photo: "PhotosPhoto | None" = None


class PhotosPhotoAlbum(PhotosPhotoAlbum):  # type: ignore
    thumb: "PhotosPhoto | None" = None


class StoriesStory(StoriesStory):  # type: ignore
    photo: "PhotosPhoto | None" = None


class WallCommentAttachment(WallCommentAttachment):  # type: ignore
    photo: "PhotosPhoto | None" = None


class WallWallpostAttachment(WallWallpostAttachment):  # type: ignore
    photo: "PhotosPhoto | None" = None


class NewsfeedItemPhotoPhotos(NewsfeedItemPhotoPhotos):  # type: ignore
    items: list["PhotosPhoto"] | None = None


class NewsfeedItemPhotoTagPhotoTags(NewsfeedItemPhotoTagPhotoTags):  # type: ignore
    items: list["PhotosPhoto"] | None = None


class UsersUserFull(UsersUserFull):  # type: ignore
    photo_max_size: "PhotosPhoto | None" = None


class MarketMarketItemFull(MarketMarketItemFull):  # type: ignore
    photos: "PhotosPhoto | None" = None


class MessagesKeyboardButtonPropertyAction(MessagesKeyboardButtonPropertyAction):  # type: ignore
    label: str = Field()
    type: str = Field()
    payload: str = Field()


class StoriesClickableSticker(StoriesClickableSticker):  # type: ignore[no-redef]
    poll: "PollsPoll | None" = None


class ClientInfoForBots(BaseModel):
    """
    Model: `ClientInfoForBots`
    """

    button_actions: list["MessagesTemplateActionTypeNames"] | None = Field(
        default=None,
    )
    """Property `ClientInfoForBots.button_actions`."""

    keyboard: bool | None = Field(
        default=None,
    )
    """client has support keyboard."""

    inline_keyboard: bool | None = Field(
        default=None,
    )
    """client has support inline keyboard."""

    carousel: bool | None = Field(
        default=None,
    )
    """client has support carousel."""

    lang_id: int | None = Field(
        default=None,
    )
    """client or user language id."""


UsersSubscriptionsItem: TypeAlias = GroupsGroupFull | UsersUserFull  # type: ignore


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
