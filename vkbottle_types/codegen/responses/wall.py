import typing
from vkbottle_types.responses.base_response import BaseResponse, BaseModel
from vkbottle_types.base_model import Field

from vkbottle_types.objects import (
    CommentThread,
    WallPostSource,
    BaseSticker,
    PollsPoll,
    VideoVideoAlbumFull,
    NotesNote,
    PagesWikipageFull,
    WallWallpostFull,
    AudioAudio,
    WallAppPost,
    BaseCommentsInfo,
    WallViews,
    DocsDoc,
    WallPostSourceType,
    WallWallpostCommentsDonutPlaceholder,
    WallWallpostDonut,
    WallWallCommentDonut,
    WallWallCommentDonutPlaceholder,
    WallWallpostAttachmentType,
    WallPostCopyright,
    NewsfeedItemWallpostFeedback,
    WallCommentAttachmentType,
    GroupsGroupAttach,
    PhotosPhotoAlbum,
    VideoVideo,
    WallAttachedNote,
    WallWallpostDonutPlaceholder,
    BaseBoolInt,
    EventsEventAttach,
    BaseLink,
    BaseLikesInfo,
    WallGeo,
    VideoVideoFull,
    WallPostedPhoto,
    WallGraffiti,
    PhotosPhoto,
    MarketMarketItem,
    MarketMarketAlbum,
    BaseRepostsInfo,
    WallPostType,
    WallWallpostAttachment,
)


class WallAppPostResponseModel(BaseModel):
    id: typing.Optional[int] = Field(
        default=None,
        description="Application ID",
    )

    name: typing.Optional[str] = Field(
        default=None,
        description="Application name",
    )

    photo_130: typing.Optional[str] = Field(
        default=None,
        description="URL of the preview image with 130 px in width",
    )

    photo_604: typing.Optional[str] = Field(
        default=None,
        description="URL of the preview image with 604 px in width",
    )


class WallAppPostResponse(BaseResponse):
    response: "WallAppPostResponseModel"


class WallAttachedNoteResponseModel(BaseModel):
    comments: int = Field(
        description="Comments number",
    )

    date: int = Field(
        description="Date when the note has been created in Unixtime",
    )

    id: int = Field(
        description="Note ID",
    )

    owner_id: int = Field(
        description="Note owner's ID",
    )

    read_comments: int = Field(
        description="Read comments number",
    )

    title: str = Field(
        description="Note title",
    )

    view_url: str = Field(
        description="URL of the page with note preview",
    )

    text: typing.Optional[str] = Field(
        default=None,
        description="Note text",
    )

    privacy_view: typing.Optional[typing.List[str]] = Field(
        default=None,
    )

    privacy_comment: typing.Optional[typing.List[str]] = Field(
        default=None,
    )

    can_comment: typing.Optional[int] = Field(
        default=None,
    )

    text_wiki: typing.Optional[str] = Field(
        default=None,
        description="Note wiki text",
    )


class WallAttachedNoteResponse(BaseResponse):
    response: "WallAttachedNoteResponseModel"


class WallCarouselBaseResponseModel(BaseModel):
    carousel_offset: typing.Optional[int] = Field(
        default=None,
        description="Index of current carousel element",
    )


class WallCarouselBaseResponse(BaseResponse):
    response: "WallCarouselBaseResponseModel"


class WallCommentAttachmentResponseModel(BaseModel):
    type: "WallCommentAttachmentType" = Field()

    audio: typing.Optional["AudioAudio"] = Field(
        default=None,
    )

    doc: typing.Optional["DocsDoc"] = Field(
        default=None,
    )

    link: typing.Optional["BaseLink"] = Field(
        default=None,
    )

    market: typing.Optional["MarketMarketItem"] = Field(
        default=None,
    )

    market_market_album: typing.Optional["MarketMarketAlbum"] = Field(
        default=None,
    )

    note: typing.Optional["WallAttachedNote"] = Field(
        default=None,
    )

    page: typing.Optional["PagesWikipageFull"] = Field(
        default=None,
    )

    photo: typing.Optional["PhotosPhoto"] = Field(
        default=None,
    )

    sticker: typing.Optional["BaseSticker"] = Field(
        default=None,
    )

    video: typing.Optional["VideoVideo"] = Field(
        default=None,
    )

    graffiti: typing.Optional["WallGraffiti"] = Field(
        default=None,
    )


class WallCommentAttachmentResponse(BaseResponse):
    response: "WallCommentAttachmentResponseModel"


class WallCommentAttachmentTypeResponseModel(enum.Enum):
    PHOTO = "photo"

    AUDIO = "audio"

    AUDIO_PLAYLIST = "audio_playlist"

    VIDEO = "video"

    DOC = "doc"

    LINK = "link"

    NOTE = "note"

    PAGE = "page"

    MARKET_MARKET_ALBUM = "market_market_album"

    MARKET = "market"

    STICKER = "sticker"

    GRAFFITI = "graffiti"


class WallCommentAttachmentTypeResponse(BaseResponse):
    response: "WallCommentAttachmentTypeResponseModel"


class WallGeoResponseModel(BaseModel):
    coordinates: typing.Optional[str] = Field(
        default=None,
        description="Coordinates as string. <latitude> <longtitude>",
    )

    showmap: typing.Optional[int] = Field(
        default=None,
        description="Information whether a map is showed",
    )

    type: typing.Optional[typing.Literal["place", "point"]] = Field(
        default=None,
        description="Place type",
    )


class WallGeoResponse(BaseResponse):
    response: "WallGeoResponseModel"


class WallGetFilterResponseModel(enum.Enum):
    OWNER = "owner"

    OTHERS = "others"

    ALL = "all"

    POSTPONED = "postponed"

    SUGGESTS = "suggests"

    ARCHIVED = "archived"

    DONUT = "donut"


class WallGetFilterResponse(BaseResponse):
    response: "WallGetFilterResponseModel"


class WallGraffitiResponseModel(BaseModel):
    id: typing.Optional[int] = Field(
        default=None,
        description="Graffiti ID",
    )

    owner_id: typing.Optional[int] = Field(
        default=None,
        description="Graffiti owner's ID",
    )

    photo_200: typing.Optional[str] = Field(
        default=None,
        description="URL of the preview image with 200 px in width",
    )

    photo_586: typing.Optional[str] = Field(
        default=None,
        description="URL of the preview image with 586 px in width",
    )

    height: typing.Optional[int] = Field(
        default=None,
        description="Graffiti height",
    )

    url: typing.Optional[str] = Field(
        default=None,
        description="Graffiti URL",
    )

    width: typing.Optional[int] = Field(
        default=None,
        description="Graffiti width",
    )

    access_key: typing.Optional[str] = Field(
        default=None,
        description="Access key for graffiti",
    )


class WallGraffitiResponse(BaseResponse):
    response: "WallGraffitiResponseModel"


class WallPostCopyrightResponseModel(BaseModel):
    link: str = Field()

    name: str = Field()

    type: str = Field()

    id: typing.Optional[int] = Field(
        default=None,
    )


class WallPostCopyrightResponse(BaseResponse):
    response: "WallPostCopyrightResponseModel"


class WallPostSourceResponseModel(BaseModel):
    data: typing.Optional[str] = Field(
        default=None,
        description="Additional data",
    )

    platform: typing.Optional[str] = Field(
        default=None,
        description="Platform name",
    )

    type: typing.Optional["WallPostSourceType"] = Field(
        default=None,
    )

    url: typing.Optional[str] = Field(
        default=None,
        description="URL to an external site used to publish the post",
    )

    link: typing.Optional["BaseLink"] = Field(
        default=None,
    )


class WallPostSourceResponse(BaseResponse):
    response: "WallPostSourceResponseModel"


class WallPostSourceTypeResponseModel(enum.Enum):
    VK = "vk"

    WIDGET = "widget"

    API = "api"

    RSS = "rss"

    SMS = "sms"

    MVK = "mvk"


class WallPostSourceTypeResponse(BaseResponse):
    response: "WallPostSourceTypeResponseModel"


class WallPostTypeResponseModel(enum.Enum):
    POST = "post"

    COPY = "copy"

    REPLY = "reply"

    POSTPONE = "postpone"

    SUGGEST = "suggest"

    POST_ADS = "post_ads"

    PHOTO = "photo"

    VIDEO = "video"


class WallPostTypeResponse(BaseResponse):
    response: "WallPostTypeResponseModel"


class WallPostedPhotoResponseModel(BaseModel):
    id: typing.Optional[int] = Field(
        default=None,
        description="Photo ID",
    )

    owner_id: typing.Optional[int] = Field(
        default=None,
        description="Photo owner's ID",
    )

    photo_130: typing.Optional[str] = Field(
        default=None,
        description="URL of the preview image with 130 px in width",
    )

    photo_604: typing.Optional[str] = Field(
        default=None,
        description="URL of the preview image with 604 px in width",
    )


class WallPostedPhotoResponse(BaseResponse):
    response: "WallPostedPhotoResponseModel"


class WallViewsResponseModel(BaseModel):
    count: typing.Optional[int] = Field(
        default=None,
        description="Count",
    )


class WallViewsResponse(BaseResponse):
    response: "WallViewsResponseModel"


class WallWallCommentResponseModel(BaseModel):
    id: int = Field(
        description="Comment ID",
    )

    from_id: int = Field(
        description="Author ID",
    )

    date: int = Field(
        description="Date when the comment has been added in Unixtime",
    )

    text: str = Field(
        description="Comment text",
    )

    can_edit: typing.Optional[bool] = Field(
        default=None,
    )

    post_id: typing.Optional[int] = Field(
        default=None,
    )

    owner_id: typing.Optional[int] = Field(
        default=None,
    )

    parents_stack: typing.Optional[typing.List[int]] = Field(
        default=None,
    )

    photo_id: typing.Optional[int] = Field(
        default=None,
    )

    video_id: typing.Optional[int] = Field(
        default=None,
    )

    attachments: typing.Optional[typing.List[WallWallpostAttachment]] = Field(
        default=None,
    )

    donut: typing.Optional["WallWallCommentDonut"] = Field(
        default=None,
    )

    likes: typing.Optional["BaseLikesInfo"] = Field(
        default=None,
    )

    real_offset: typing.Optional[int] = Field(
        default=None,
        description="Real position of the comment",
    )

    reply_to_user: typing.Optional[int] = Field(
        default=None,
        description="Replied user ID",
    )

    reply_to_comment: typing.Optional[int] = Field(
        default=None,
        description="Replied comment ID",
    )

    thread: typing.Optional["CommentThread"] = Field(
        default=None,
    )

    deleted: typing.Optional[bool] = Field(
        default=None,
    )

    pid: typing.Optional[int] = Field(
        default=None,
        description="Photo ID",
    )


class WallWallCommentResponse(BaseResponse):
    response: "WallWallCommentResponseModel"


class WallWallCommentDonutResponseModel(BaseModel):
    is_don: typing.Optional[bool] = Field(
        default=None,
        description="Means commentator is donator",
    )

    placeholder: typing.Optional["WallWallCommentDonutPlaceholder"] = Field(
        default=None,
    )


class WallWallCommentDonutResponse(BaseResponse):
    response: "WallWallCommentDonutResponseModel"


class WallWallCommentDonutPlaceholderResponseModel(BaseModel):
    text: str = Field()


class WallWallCommentDonutPlaceholderResponse(BaseResponse):
    response: "WallWallCommentDonutPlaceholderResponseModel"


class WallWallItemResponseModel(BaseModel):
    pass


class WallWallItemResponse(BaseResponse):
    response: "WallWallItemResponseModel"


class WallWallpostResponseModel(BaseModel):
    access_key: typing.Optional[str] = Field(
        default=None,
        description="Access key to private object",
    )

    is_deleted: typing.Optional[bool] = Field(
        default=None,
    )

    deleted_reason: typing.Optional[str] = Field(
        default=None,
    )

    deleted_details: typing.Optional[str] = Field(
        default=None,
    )

    attachments: typing.Optional[typing.List[WallWallpostAttachment]] = Field(
        default=None,
    )

    copyright: typing.Optional["WallPostCopyright"] = Field(
        default=None,
        description="Information about the source of the post",
    )

    date: typing.Optional[int] = Field(
        default=None,
        description="Date of publishing in Unixtime",
    )

    edited: typing.Optional[int] = Field(
        default=None,
        description="Date of editing in Unixtime",
    )

    from_id: typing.Optional[int] = Field(
        default=None,
        description="Post author ID",
    )

    geo: typing.Optional["WallGeo"] = Field(
        default=None,
    )

    id: typing.Optional[int] = Field(
        default=None,
        description="Post ID",
    )

    is_archived: typing.Optional[bool] = Field(
        default=None,
        description="Is post archived, only for post owners",
    )

    is_favorite: typing.Optional[bool] = Field(
        default=None,
        description="Information whether the post in favorites list",
    )

    likes: typing.Optional["BaseLikesInfo"] = Field(
        default=None,
        description="Count of likes",
    )

    owner_id: typing.Optional[int] = Field(
        default=None,
        description="Wall owner's ID",
    )

    post_id: typing.Optional[int] = Field(
        default=None,
        description="If post type 'reply', contains original post ID",
    )

    parents_stack: typing.Optional[typing.List[int]] = Field(
        default=None,
        description="If post type 'reply', contains original parent IDs stack",
    )

    post_source: typing.Optional["WallPostSource"] = Field(
        default=None,
    )

    post_type: typing.Optional["WallPostType"] = Field(
        default=None,
    )

    reposts: typing.Optional["BaseRepostsInfo"] = Field(
        default=None,
    )

    signer_id: typing.Optional[int] = Field(
        default=None,
        description="Post signer ID",
    )

    text: typing.Optional[str] = Field(
        default=None,
        description="Post text",
    )

    views: typing.Optional["WallViews"] = Field(
        default=None,
        description="Count of views",
    )


class WallWallpostResponse(BaseResponse):
    response: "WallWallpostResponseModel"


class WallWallpostAttachmentResponseModel(BaseModel):
    type: "WallWallpostAttachmentType" = Field()

    access_key: typing.Optional[str] = Field(
        default=None,
        description="Access key for the audio",
    )

    album: typing.Optional["PhotosPhotoAlbum"] = Field(
        default=None,
    )

    app: typing.Optional["WallAppPost"] = Field(
        default=None,
    )

    audio: typing.Optional["AudioAudio"] = Field(
        default=None,
    )

    doc: typing.Optional["DocsDoc"] = Field(
        default=None,
    )

    event: typing.Optional["EventsEventAttach"] = Field(
        default=None,
    )

    group: typing.Optional["GroupsGroupAttach"] = Field(
        default=None,
    )

    graffiti: typing.Optional["WallGraffiti"] = Field(
        default=None,
    )

    link: typing.Optional["BaseLink"] = Field(
        default=None,
    )

    market: typing.Optional["MarketMarketItem"] = Field(
        default=None,
    )

    market_album: typing.Optional["MarketMarketAlbum"] = Field(
        default=None,
    )

    note: typing.Optional["NotesNote"] = Field(
        default=None,
    )

    page: typing.Optional["PagesWikipageFull"] = Field(
        default=None,
    )

    photo: typing.Optional["PhotosPhoto"] = Field(
        default=None,
    )

    poll: typing.Optional["PollsPoll"] = Field(
        default=None,
    )

    posted_photo: typing.Optional["WallPostedPhoto"] = Field(
        default=None,
    )

    video: typing.Optional["VideoVideoFull"] = Field(
        default=None,
    )

    video_playlist: typing.Optional["VideoVideoAlbumFull"] = Field(
        default=None,
    )


class WallWallpostAttachmentResponse(BaseResponse):
    response: "WallWallpostAttachmentResponseModel"


class WallWallpostAttachmentTypeResponseModel(enum.Enum):
    PHOTO = "photo"

    PHOTOS_LIST = "photos_list"

    POSTED_PHOTO = "posted_photo"

    AUDIO = "audio"

    AUDIO_PLAYLIST = "audio_playlist"

    VIDEO = "video"

    VIDEO_PLAYLIST = "video_playlist"

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


class WallWallpostAttachmentTypeResponse(BaseResponse):
    response: "WallWallpostAttachmentTypeResponseModel"


class WallWallpostCommentsDonutResponseModel(BaseModel):
    placeholder: typing.Optional["WallWallpostCommentsDonutPlaceholder"] = Field(
        default=None,
    )


class WallWallpostCommentsDonutResponse(BaseResponse):
    response: "WallWallpostCommentsDonutResponseModel"


class WallWallpostCommentsDonutPlaceholderResponseModel(BaseModel):
    text: str = Field()


class WallWallpostCommentsDonutPlaceholderResponse(BaseResponse):
    response: "WallWallpostCommentsDonutPlaceholderResponseModel"


class WallWallpostDonutResponseModel(BaseModel):
    is_donut: bool = Field(
        description="Post only for dons",
    )

    paid_duration: typing.Optional[int] = Field(
        default=None,
        description="Value of this field need to pass in wall.post/edit in donut_paid_duration",
    )

    placeholder: typing.Optional["WallWallpostDonutPlaceholder"] = Field(
        default=None,
        description="If placeholder was respond, text and all attachments will be hidden",
    )

    can_publish_free_copy: typing.Optional[bool] = Field(
        default=None,
        description="Says whether group admin can post free copy of this donut post",
    )

    edit_mode: typing.Optional[typing.Literal["all", "duration"]] = Field(
        default=None,
        description="Says what user can edit in post about donut properties",
    )


class WallWallpostDonutResponse(BaseResponse):
    response: "WallWallpostDonutResponseModel"


class WallWallpostDonutPlaceholderResponseModel(BaseModel):
    text: str = Field()


class WallWallpostDonutPlaceholderResponse(BaseResponse):
    response: "WallWallpostDonutPlaceholderResponseModel"


class WallWallpostFullResponseModel(WallCarouselBase, WallWallpost):
    copy_history: typing.Optional[typing.List[WallWallpostFull]] = Field(
        default=None,
    )

    can_edit: typing.Optional[bool] = Field(
        default=None,
        description="Information whether current user can edit the post",
    )

    created_by: typing.Optional[int] = Field(
        default=None,
        description="Post creator ID (if post still can be edited)",
    )

    can_delete: typing.Optional[bool] = Field(
        default=None,
        description="Information whether current user can delete the post",
    )

    can_pin: typing.Optional[bool] = Field(
        default=None,
        description="Information whether current user can pin the post",
    )

    donut: typing.Optional["WallWallpostDonut"] = Field(
        default=None,
    )

    is_pinned: typing.Optional[bool] = Field(
        default=None,
        description="Information whether the post is pinned",
    )

    comments: typing.Optional["BaseCommentsInfo"] = Field(
        default=None,
    )

    marked_as_ads: typing.Optional[bool] = Field(
        default=None,
        description="Information whether the post is marked as ads",
    )

    topic_id: typing.Optional[int] = Field(
        default=None,
        description="Topic ID. Allowed values can be obtained from newsfeed.getPostTopics method",
    )

    short_text_rate: typing.Optional[float] = Field(
        default=None,
        description="Preview length control parameter",
    )

    hash: typing.Optional[str] = Field(
        default=None,
        description="Hash for sharing",
    )

    type: typing.Optional["WallPostType"] = Field(
        default=None,
    )

    feedback: typing.Optional["NewsfeedItemWallpostFeedback"] = Field(
        default=None,
    )

    to_id: typing.Optional[int] = Field(
        default=None,
    )


class WallWallpostFullResponse(BaseResponse):
    response: "WallWallpostFullResponseModel"
