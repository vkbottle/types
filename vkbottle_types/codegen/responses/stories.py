import typing
import enum
from vkbottle_types.responses.base_response import BaseResponse, BaseModel
from vkbottle_types.base_model import Field

from vkbottle_types.objects import (
    StoriesFeedItem,
    MarketMarketItem,
    StoriesStory,
    StoriesClickableStickers,
    StoriesStoryStatsState,
    StoriesClickableSticker,
    StoriesStoryLink,
    StoriesStoryStatsStat,
    PollsPoll,
    AppsAppMin,
    StoriesClickableArea,
    PhotosPhoto,
    StoriesStoryType,
    BaseLink,
    StoriesReplies,
    StoriesStatLine,
    StoriesPromoBlock,
    BaseBoolInt,
    AudioAudio,
    VideoVideoFull,
    UsersUserFull,
)


class StoriesClickableAreaResponseModel(BaseModel):
    x: int = Field()

    y: int = Field()


class StoriesClickableAreaResponse(BaseResponse):
    response: "StoriesClickableAreaResponseModel"


class StoriesClickableStickerResponseModel(BaseModel):
    clickable_area: typing.List[StoriesClickableArea] = Field()

    id: int = Field(
        description="Clickable sticker ID",
    )

    type: typing.Literal[
        "hashtag",
        "mention",
        "link",
        "question",
        "place",
        "market_item",
        "music",
        "story_reply",
        "owner",
        "post",
        "poll",
        "sticker",
        "app",
        "situational_theme",
        "playlist",
        "clip",
    ] = Field()

    hashtag: typing.Optional[str] = Field(
        default=None,
    )

    link_object: typing.Optional["BaseLink"] = Field(
        default=None,
    )

    mention: typing.Optional[str] = Field(
        default=None,
    )

    tooltip_text: typing.Optional[str] = Field(
        default=None,
    )

    owner_id: typing.Optional[int] = Field(
        default=None,
    )

    story_id: typing.Optional[int] = Field(
        default=None,
    )

    clip_id: typing.Optional[int] = Field(
        default=None,
    )

    question: typing.Optional[str] = Field(
        default=None,
    )

    question_button: typing.Optional[str] = Field(
        default=None,
    )

    place_id: typing.Optional[int] = Field(
        default=None,
    )

    market_item: typing.Optional["MarketMarketItem"] = Field(
        default=None,
    )

    audio: typing.Optional["AudioAudio"] = Field(
        default=None,
    )

    audio_start_time: typing.Optional[int] = Field(
        default=None,
    )

    style: typing.Optional[
        typing.Literal[
            "transparent",
            "blue_gradient",
            "red_gradient",
            "underline",
            "blue",
            "green",
            "white",
            "question_reply",
            "light",
            "impressive",
        ]
    ] = Field(
        default=None,
    )

    subtype: typing.Optional[
        typing.Literal["market_item", "aliexpress_product"]
    ] = Field(
        default=None,
    )

    post_owner_id: typing.Optional[int] = Field(
        default=None,
    )

    post_id: typing.Optional[int] = Field(
        default=None,
    )

    poll: typing.Optional["PollsPoll"] = Field(
        default=None,
    )

    color: typing.Optional[str] = Field(
        default=None,
        description="Color, hex format",
    )

    sticker_id: typing.Optional[int] = Field(
        default=None,
        description="Sticker ID",
    )

    sticker_pack_id: typing.Optional[int] = Field(
        default=None,
        description="Sticker pack ID",
    )

    app: typing.Optional["AppsAppMin"] = Field(
        default=None,
    )

    app_context: typing.Optional[str] = Field(
        default=None,
        description="Additional context for app sticker",
    )

    has_new_interactions: typing.Optional[bool] = Field(
        default=None,
        description="Whether current user has unread interaction with this app",
    )

    is_broadcast_notify_allowed: typing.Optional[bool] = Field(
        default=None,
        description="Whether current user allowed broadcast notify from this app",
    )

    situational_theme_id: typing.Optional[int] = Field(
        default=None,
    )

    situational_app_url: typing.Optional[str] = Field(
        default=None,
    )


class StoriesClickableStickerResponse(BaseResponse):
    response: "StoriesClickableStickerResponseModel"


class StoriesClickableStickersResponseModel(BaseModel):
    clickable_stickers: typing.List[StoriesClickableSticker] = Field()

    original_height: int = Field()

    original_width: int = Field()


class StoriesClickableStickersResponse(BaseResponse):
    response: "StoriesClickableStickersResponseModel"


class StoriesFeedItemResponseModel(BaseModel):
    type: typing.Literal[
        "promo_stories",
        "stories",
        "live_active",
        "live_finished",
        "app_grouped_stories",
        "discover",
    ] = Field(
        description="Type of Feed Item",
    )

    id: typing.Optional[str] = Field(
        default=None,
    )

    owner_id: typing.Optional[int] = Field(
        default=None,
    )

    stories: typing.Optional[typing.List[StoriesStory]] = Field(
        default=None,
        description="Author stories",
    )

    grouped: typing.Optional[typing.List[StoriesFeedItem]] = Field(
        default=None,
        description="Grouped stories of various authors (for types community_grouped_stories/app_grouped_stories type)",
    )

    app: typing.Optional["AppsAppMin"] = Field(
        default=None,
        description="App, which stories has been grouped (for type app_grouped_stories)",
    )

    promo_data: typing.Optional["StoriesPromoBlock"] = Field(
        default=None,
        description="Additional data for promo stories (for type promo_stories)",
    )

    track_code: typing.Optional[str] = Field(
        default=None,
    )

    has_unseen: typing.Optional[bool] = Field(
        default=None,
    )

    name: typing.Optional[str] = Field(
        default=None,
    )


class StoriesFeedItemResponse(BaseResponse):
    response: "StoriesFeedItemResponseModel"


class StoriesPromoBlockResponseModel(BaseModel):
    name: str = Field(
        description="Promo story title",
    )

    photo_50: str = Field(
        description="RL of square photo of the story with 50 pixels in width",
    )

    photo_100: str = Field(
        description="RL of square photo of the story with 100 pixels in width",
    )

    not_animated: bool = Field(
        description="Hide animation for promo story",
    )

    is_advice: bool = Field(
        description="Promo story from advice",
    )


class StoriesPromoBlockResponse(BaseResponse):
    response: "StoriesPromoBlockResponseModel"


class StoriesRepliesResponseModel(BaseModel):
    count: int = Field(
        description="Replies number.",
    )

    new: typing.Optional[int] = Field(
        default=None,
        description="New replies number.",
    )


class StoriesRepliesResponse(BaseResponse):
    response: "StoriesRepliesResponseModel"


class StoriesStatCategoryResponseModel(BaseModel):
    header: str = Field()

    lines: typing.List[StoriesStatLine] = Field()


class StoriesStatCategoryResponse(BaseResponse):
    response: "StoriesStatCategoryResponseModel"


class StoriesStatLineResponseModel(BaseModel):
    name: str = Field()

    counter: typing.Optional[int] = Field(
        default=None,
    )

    is_unavailable: typing.Optional[bool] = Field(
        default=None,
    )


class StoriesStatLineResponse(BaseResponse):
    response: "StoriesStatLineResponseModel"


class StoriesStoryResponseModel(BaseModel):
    id: int = Field(
        description="Story ID.",
    )

    owner_id: int = Field(
        description="Story owner's ID.",
    )

    access_key: typing.Optional[str] = Field(
        default=None,
        description="Access key for private object.",
    )

    can_comment: typing.Optional[bool] = Field(
        default=None,
        description="Information whether current user can comment the story (0 - no, 1 - yes).",
    )

    can_reply: typing.Optional[bool] = Field(
        default=None,
        description="Information whether current user can reply to the story (0 - no, 1 - yes).",
    )

    can_see: typing.Optional[bool] = Field(
        default=None,
        description="Information whether current user can see the story (0 - no, 1 - yes).",
    )

    can_like: typing.Optional[bool] = Field(
        default=None,
        description="Information whether current user can like the story.",
    )

    can_share: typing.Optional[bool] = Field(
        default=None,
        description="Information whether current user can share the story (0 - no, 1 - yes).",
    )

    can_hide: typing.Optional[bool] = Field(
        default=None,
        description="Information whether current user can hide the story (0 - no, 1 - yes).",
    )

    date: typing.Optional[int] = Field(
        default=None,
        description="Date when story has been added in Unixtime.",
    )

    expires_at: typing.Optional[int] = Field(
        default=None,
        description="Story expiration time. Unixtime.",
    )

    is_deleted: typing.Optional[bool] = Field(
        default=None,
        description="Information whether the story is deleted (false - no, true - yes).",
    )

    is_expired: typing.Optional[bool] = Field(
        default=None,
        description="Information whether the story is expired (false - no, true - yes).",
    )

    link: typing.Optional["StoriesStoryLink"] = Field(
        default=None,
    )

    parent_story: typing.Optional["StoriesStory"] = Field(
        default=None,
    )

    parent_story_access_key: typing.Optional[str] = Field(
        default=None,
        description="Access key for private object.",
    )

    parent_story_id: typing.Optional[int] = Field(
        default=None,
        description="Parent story ID.",
    )

    parent_story_owner_id: typing.Optional[int] = Field(
        default=None,
        description="Parent story owner's ID.",
    )

    photo: typing.Optional["PhotosPhoto"] = Field(
        default=None,
    )

    replies: typing.Optional["StoriesReplies"] = Field(
        default=None,
        description="Replies counters to current story.",
    )

    seen: typing.Optional[bool] = Field(
        default=None,
        description="Information whether current user has seen the story or not (0 - no, 1 - yes).",
    )

    type: typing.Optional["StoriesStoryType"] = Field(
        default=None,
    )

    clickable_stickers: typing.Optional["StoriesClickableStickers"] = Field(
        default=None,
    )

    video: typing.Optional["VideoVideoFull"] = Field(
        default=None,
    )

    views: typing.Optional[int] = Field(
        default=None,
        description="Views number.",
    )

    can_ask: typing.Optional[bool] = Field(
        default=None,
        description="Information whether story has question sticker and current user can send question to the author",
    )

    can_ask_anonymous: typing.Optional[bool] = Field(
        default=None,
        description="Information whether story has question sticker and current user can send anonymous question to the author",
    )

    narratives_count: typing.Optional[int] = Field(
        default=None,
    )

    first_narrative_title: typing.Optional[str] = Field(
        default=None,
    )

    can_use_in_narrative: typing.Optional[bool] = Field(
        default=None,
    )


class StoriesStoryResponse(BaseResponse):
    response: "StoriesStoryResponseModel"


class StoriesStoryLinkResponseModel(BaseModel):
    text: str = Field(
        description="Link text",
    )

    url: str = Field(
        description="Link URL",
    )

    link_url_target: typing.Optional[str] = Field(
        default=None,
        description="How to open url",
    )


class StoriesStoryLinkResponse(BaseResponse):
    response: "StoriesStoryLinkResponseModel"


class StoriesStoryStatsResponseModel(BaseModel):
    answer: "StoriesStoryStatsStat" = Field()

    bans: "StoriesStoryStatsStat" = Field()

    open_link: "StoriesStoryStatsStat" = Field()

    replies: "StoriesStoryStatsStat" = Field()

    shares: "StoriesStoryStatsStat" = Field()

    subscribers: "StoriesStoryStatsStat" = Field()

    views: "StoriesStoryStatsStat" = Field()

    likes: "StoriesStoryStatsStat" = Field()


class StoriesStoryStatsResponse(BaseResponse):
    response: "StoriesStoryStatsResponseModel"


class StoriesStoryStatsStatResponseModel(BaseModel):
    state: "StoriesStoryStatsState" = Field()

    count: typing.Optional[int] = Field(
        default=None,
        description="Stat value",
    )


class StoriesStoryStatsStatResponse(BaseResponse):
    response: "StoriesStoryStatsStatResponseModel"


class StoriesStoryStatsStateResponseModel(enum.Enum):
    ON = "on"

    OFF = "off"

    HIDDEN = "hidden"


class StoriesStoryStatsStateResponse(BaseResponse):
    response: "StoriesStoryStatsStateResponseModel"


class StoriesStoryTypeResponseModel(enum.Enum):
    PHOTO = "photo"

    VIDEO = "video"

    LIVE_ACTIVE = "live_active"

    LIVE_FINISHED = "live_finished"


class StoriesStoryTypeResponse(BaseResponse):
    response: "StoriesStoryTypeResponseModel"


class StoriesUploadLinkTextResponseModel(enum.Enum):
    TO_STORE = "to_store"

    VOTE = "vote"

    MORE = "more"

    BOOK = "book"

    ORDER = "order"

    ENROLL = "enroll"

    FILL = "fill"

    SIGNUP = "signup"

    BUY = "buy"

    TICKET = "ticket"

    WRITE = "write"

    OPEN = "open"

    LEARN_MORE = "learn_more"

    VIEW = "view"

    GO_TO = "go_to"

    CONTACT = "contact"

    WATCH = "watch"

    PLAY = "play"

    INSTALL = "install"

    READ = "read"

    CALENDAR = "calendar"


class StoriesUploadLinkTextResponse(BaseResponse):
    response: "StoriesUploadLinkTextResponseModel"


class StoriesUploadResultResponseModel(BaseModel):
    upload_result: typing.Optional[str] = Field(
        default=None,
    )


class StoriesUploadResultResponse(BaseResponse):
    response: "StoriesUploadResultResponseModel"


class StoriesViewersItemResponseModel(BaseModel):
    is_liked: bool = Field(
        description="user has like for this object",
    )

    user_id: int = Field(
        description="user id",
    )

    user: typing.Optional["UsersUserFull"] = Field(
        default=None,
    )


class StoriesViewersItemResponse(BaseResponse):
    response: "StoriesViewersItemResponseModel"
