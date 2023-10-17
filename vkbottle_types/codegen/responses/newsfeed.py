import typing
import enum
from vkbottle_types.responses.base_response import BaseResponse, BaseModel
from vkbottle_types.base_model import Field

from vkbottle_types.objects import (
    BaseLinkButtonAction,
    NewsfeedItemFriendFriends,
    WallWallpostAttachment,
    BaseLikesInfo,
    NewsfeedItemWallpostFeedbackAnswer,
    NewsfeedItemDigestItem,
    NewsfeedItemVideoVideo,
    NewsfeedItemDigestHeader,
    BaseCommentsInfo,
    BaseImage,
    NewsfeedItemAudioAudio,
    NewsfeedNewsfeedItemType,
    PhotosPhoto,
    NewsfeedCommentsBase,
    NewsfeedItemPhotoTagPhotoTags,
    NewsfeedItemDigestButton,
    NewsfeedItemWallpostFeedbackType,
    BaseUserId,
    NewsfeedItemPhotoPhotos,
    NewsfeedItemWallpost,
    WallWallComment,
    NewsfeedItemPromoButtonAction,
    BaseLikes,
    BaseBoolInt,
    AudioAudio,
    VideoVideoFull,
    NewsfeedItemWallpostFeedback,
    NewsfeedItemPromoButtonImage,
    NewsfeedItemDigestFooter,
)


class NewsfeedCommentsBaseResponseModel(BaseCommentsInfo):
    list: typing.Optional[typing.List[WallWallComment]] = Field(
        default=None,
    )


class NewsfeedCommentsBaseResponse(BaseResponse):
    response: "NewsfeedCommentsBaseResponseModel"


class NewsfeedCommentsFiltersResponseModel(enum.Enum):
    POST = "post"

    PHOTO = "photo"

    VIDEO = "video"

    TOPIC = "topic"

    NOTE = "note"


class NewsfeedCommentsFiltersResponse(BaseResponse):
    response: "NewsfeedCommentsFiltersResponseModel"


class NewsfeedCommentsItemResponseModel(BaseModel):
    pass


class NewsfeedCommentsItemResponse(BaseResponse):
    response: "NewsfeedCommentsItemResponseModel"


class NewsfeedCommentsItemBaseResponseModel(BaseModel):
    type: "NewsfeedNewsfeedItemType" = Field()

    source_id: typing.Optional[int] = Field(
        default=None,
    )

    date: typing.Optional[int] = Field(
        default=None,
    )

    post_id: typing.Optional[int] = Field(
        default=None,
    )


class NewsfeedCommentsItemBaseResponse(BaseResponse):
    response: "NewsfeedCommentsItemBaseResponseModel"


class NewsfeedCommentsItemTypeMarketResponseModel(
    MarketMarketItem, NewsfeedCommentsItemBase
):
    comments: typing.Optional["NewsfeedCommentsBase"] = Field(
        default=None,
    )

    likes: typing.Optional["BaseLikes"] = Field(
        default=None,
    )


class NewsfeedCommentsItemTypeMarketResponse(BaseResponse):
    response: "NewsfeedCommentsItemTypeMarketResponseModel"


class NewsfeedCommentsItemTypeNotesResponseModel(NewsfeedCommentsItemBase):
    text: typing.Optional[str] = Field(
        default=None,
    )

    comments: typing.Optional["NewsfeedCommentsBase"] = Field(
        default=None,
    )

    likes: typing.Optional["BaseLikes"] = Field(
        default=None,
    )


class NewsfeedCommentsItemTypeNotesResponse(BaseResponse):
    response: "NewsfeedCommentsItemTypeNotesResponseModel"


class NewsfeedCommentsItemTypePhotoResponseModel(PhotosPhoto, NewsfeedCommentsItemBase):
    comments: typing.Optional["NewsfeedCommentsBase"] = Field(
        default=None,
    )

    likes: typing.Optional["BaseLikes"] = Field(
        default=None,
    )


class NewsfeedCommentsItemTypePhotoResponse(BaseResponse):
    response: "NewsfeedCommentsItemTypePhotoResponseModel"


class NewsfeedCommentsItemTypePostResponseModel(
    WallWallpostFull, NewsfeedCommentsItemBase
):
    from_id: typing.Optional[int] = Field(
        default=None,
    )

    comments: typing.Optional["NewsfeedCommentsBase"] = Field(
        default=None,
    )


class NewsfeedCommentsItemTypePostResponse(BaseResponse):
    response: "NewsfeedCommentsItemTypePostResponseModel"


class NewsfeedCommentsItemTypeTopicResponseModel(NewsfeedCommentsItemBase):
    text: typing.Optional[str] = Field(
        default=None,
    )

    comments: typing.Optional["NewsfeedCommentsBase"] = Field(
        default=None,
    )

    likes: typing.Optional["BaseLikes"] = Field(
        default=None,
    )


class NewsfeedCommentsItemTypeTopicResponse(BaseResponse):
    response: "NewsfeedCommentsItemTypeTopicResponseModel"


class NewsfeedCommentsItemTypeVideoResponseModel(VideoVideo, NewsfeedCommentsItemBase):
    text: typing.Optional[str] = Field(
        default=None,
    )

    comments: typing.Optional["NewsfeedCommentsBase"] = Field(
        default=None,
    )

    likes: typing.Optional["BaseLikes"] = Field(
        default=None,
    )

    type: typing.Optional[str] = Field(
        default=None,
    )


class NewsfeedCommentsItemTypeVideoResponse(BaseResponse):
    response: "NewsfeedCommentsItemTypeVideoResponseModel"


class NewsfeedIgnoreItemTypeResponseModel(enum.Enum):
    WALL = "wall"

    TAG = "tag"

    PROFILEPHOTO = "profilephoto"

    VIDEO = "video"

    PHOTO = "photo"

    AUDIO = "audio"


class NewsfeedIgnoreItemTypeResponse(BaseResponse):
    response: "NewsfeedIgnoreItemTypeResponseModel"


class NewsfeedItemAudioResponseModel(NewsfeedItemBase):
    audio: typing.Optional["NewsfeedItemAudioAudio"] = Field(
        default=None,
    )

    post_id: typing.Optional[int] = Field(
        default=None,
        description="Post ID",
    )


class NewsfeedItemAudioResponse(BaseResponse):
    response: "NewsfeedItemAudioResponseModel"


class NewsfeedItemAudioAudioResponseModel(BaseModel):
    count: typing.Optional[int] = Field(
        default=None,
        description="Audios number",
    )

    items: typing.Optional[typing.List[AudioAudio]] = Field(
        default=None,
    )


class NewsfeedItemAudioAudioResponse(BaseResponse):
    response: "NewsfeedItemAudioAudioResponseModel"


class NewsfeedItemBaseResponseModel(BaseModel):
    type: "NewsfeedNewsfeedItemType" = Field()

    source_id: int = Field(
        description="Item source ID",
    )

    date: int = Field(
        description="Date when item has been added in Unixtime",
    )

    short_text_rate: typing.Optional[float] = Field(
        default=None,
        description="Preview length control parameter",
    )

    feedback: typing.Optional["NewsfeedItemWallpostFeedback"] = Field(
        default=None,
    )


class NewsfeedItemBaseResponse(BaseResponse):
    response: "NewsfeedItemBaseResponseModel"


class NewsfeedItemDigestResponseModel(NewsfeedItemBase):
    feed_id: typing.Optional[str] = Field(
        default=None,
        description="id of feed in digest",
    )

    items: typing.Optional[typing.List[NewsfeedItemDigestItem]] = Field(
        default=None,
    )

    main_post_ids: typing.Optional[typing.List[str]] = Field(
        default=None,
    )

    template: typing.Optional[str] = Field(
        default=None,
        description="type of digest",
    )

    header: typing.Optional["NewsfeedItemDigestHeader"] = Field(
        default=None,
    )

    footer: typing.Optional["NewsfeedItemDigestFooter"] = Field(
        default=None,
    )


class NewsfeedItemDigestResponse(BaseResponse):
    response: "NewsfeedItemDigestResponseModel"


class NewsfeedItemDigestButtonResponseModel(BaseModel):
    title: str = Field()

    style: typing.Optional[typing.Literal["primary"]] = Field(
        default=None,
    )


class NewsfeedItemDigestButtonResponse(BaseResponse):
    response: "NewsfeedItemDigestButtonResponseModel"


class NewsfeedItemDigestFooterResponseModel(BaseModel):
    style: typing.Literal["text", "button"] = Field()

    text: str = Field(
        description="text for invite to enable smart feed",
    )

    button: typing.Optional["NewsfeedItemDigestButton"] = Field(
        default=None,
    )


class NewsfeedItemDigestFooterResponse(BaseResponse):
    response: "NewsfeedItemDigestFooterResponseModel"


class NewsfeedItemDigestFullItemResponseModel(NewsfeedItemBase):
    post: "NewsfeedItemWallpost" = Field()

    text: typing.Optional[str] = Field(
        default=None,
    )

    source_name: typing.Optional[str] = Field(
        default=None,
    )

    attachment_index: typing.Optional[int] = Field(
        default=None,
    )

    attachment: typing.Optional["WallWallpostAttachment"] = Field(
        default=None,
    )

    style: typing.Optional[str] = Field(
        default=None,
    )

    badge_text: typing.Optional[str] = Field(
        default=None,
        description="Optional red badge for posts in digest block",
    )


class NewsfeedItemDigestFullItemResponse(BaseResponse):
    response: "NewsfeedItemDigestFullItemResponseModel"


class NewsfeedItemDigestHeaderResponseModel(BaseModel):
    title: str = Field(
        description="Title of the header",
    )

    style: typing.Literal["singleline", "multiline"] = Field()

    subtitle: typing.Optional[str] = Field(
        default=None,
        description="Subtitle of the header, when title have two strings",
    )

    badge_text: typing.Optional[str] = Field(
        default=None,
        description="Optional field for red badge in Trends feed blocks",
    )

    button: typing.Optional["NewsfeedItemDigestButton"] = Field(
        default=None,
    )


class NewsfeedItemDigestHeaderResponse(BaseResponse):
    response: "NewsfeedItemDigestHeaderResponseModel"


class NewsfeedItemDigestItemResponseModel(BaseModel):
    pass


class NewsfeedItemDigestItemResponse(BaseResponse):
    response: "NewsfeedItemDigestItemResponseModel"


class NewsfeedItemFriendResponseModel(NewsfeedItemBase):
    friends: typing.Optional["NewsfeedItemFriendFriends"] = Field(
        default=None,
    )


class NewsfeedItemFriendResponse(BaseResponse):
    response: "NewsfeedItemFriendResponseModel"


class NewsfeedItemFriendFriendsResponseModel(BaseModel):
    count: typing.Optional[int] = Field(
        default=None,
        description="Number of friends has been added",
    )

    items: typing.Optional[typing.List[BaseUserId]] = Field(
        default=None,
    )


class NewsfeedItemFriendFriendsResponse(BaseResponse):
    response: "NewsfeedItemFriendFriendsResponseModel"


class NewsfeedItemHolidayRecommendationsBlockHeaderResponseModel(BaseModel):
    title: typing.Optional[str] = Field(
        default=None,
        description="Title of the header",
    )

    subtitle: typing.Optional[str] = Field(
        default=None,
        description="Subtitle of the header",
    )

    image: typing.Optional[typing.List[BaseImage]] = Field(
        default=None,
    )

    action: typing.Optional["BaseLinkButtonAction"] = Field(
        default=None,
    )


class NewsfeedItemHolidayRecommendationsBlockHeaderResponse(BaseResponse):
    response: "NewsfeedItemHolidayRecommendationsBlockHeaderResponseModel"


class NewsfeedItemPhotoResponseModel(WallCarouselBase, NewsfeedItemBase):
    photos: typing.Optional["NewsfeedItemPhotoPhotos"] = Field(
        default=None,
    )

    post_id: typing.Optional[int] = Field(
        default=None,
        description="Post ID",
    )


class NewsfeedItemPhotoResponse(BaseResponse):
    response: "NewsfeedItemPhotoResponseModel"


class NewsfeedItemPhotoPhotosResponseModel(BaseModel):
    count: typing.Optional[int] = Field(
        default=None,
        description="Photos number",
    )

    items: typing.Optional[typing.List[PhotosPhoto]] = Field(
        default=None,
    )


class NewsfeedItemPhotoPhotosResponse(BaseResponse):
    response: "NewsfeedItemPhotoPhotosResponseModel"


class NewsfeedItemPhotoTagResponseModel(WallCarouselBase, NewsfeedItemBase):
    photo_tags: typing.Optional["NewsfeedItemPhotoTagPhotoTags"] = Field(
        default=None,
    )

    post_id: typing.Optional[int] = Field(
        default=None,
        description="Post ID",
    )


class NewsfeedItemPhotoTagResponse(BaseResponse):
    response: "NewsfeedItemPhotoTagResponseModel"


class NewsfeedItemPhotoTagPhotoTagsResponseModel(BaseModel):
    count: typing.Optional[int] = Field(
        default=None,
        description="Tags number",
    )

    items: typing.Optional[typing.List[PhotosPhoto]] = Field(
        default=None,
    )


class NewsfeedItemPhotoTagPhotoTagsResponse(BaseResponse):
    response: "NewsfeedItemPhotoTagPhotoTagsResponseModel"


class NewsfeedItemPromoButtonResponseModel(NewsfeedItemBase):
    text: typing.Optional[str] = Field(
        default=None,
    )

    title: typing.Optional[str] = Field(
        default=None,
    )

    action: typing.Optional["NewsfeedItemPromoButtonAction"] = Field(
        default=None,
    )

    images: typing.Optional[typing.List[NewsfeedItemPromoButtonImage]] = Field(
        default=None,
    )


class NewsfeedItemPromoButtonResponse(BaseResponse):
    response: "NewsfeedItemPromoButtonResponseModel"


class NewsfeedItemPromoButtonActionResponseModel(BaseModel):
    url: typing.Optional[str] = Field(
        default=None,
    )

    type: typing.Optional[str] = Field(
        default=None,
    )

    target: typing.Optional[str] = Field(
        default=None,
    )


class NewsfeedItemPromoButtonActionResponse(BaseResponse):
    response: "NewsfeedItemPromoButtonActionResponseModel"


class NewsfeedItemPromoButtonImageResponseModel(BaseModel):
    width: typing.Optional[int] = Field(
        default=None,
    )

    height: typing.Optional[int] = Field(
        default=None,
    )

    url: typing.Optional[str] = Field(
        default=None,
    )


class NewsfeedItemPromoButtonImageResponse(BaseResponse):
    response: "NewsfeedItemPromoButtonImageResponseModel"


class NewsfeedItemTopicResponseModel(NewsfeedItemBase):
    post_id: int = Field(
        description="Topic post ID",
    )

    text: str = Field(
        description="Post text",
    )

    comments: typing.Optional["BaseCommentsInfo"] = Field(
        default=None,
    )

    likes: typing.Optional["BaseLikesInfo"] = Field(
        default=None,
    )


class NewsfeedItemTopicResponse(BaseResponse):
    response: "NewsfeedItemTopicResponseModel"


class NewsfeedItemVideoResponseModel(WallCarouselBase, NewsfeedItemBase):
    video: typing.Optional["NewsfeedItemVideoVideo"] = Field(
        default=None,
    )

    post_id: typing.Optional[int] = Field(
        default=None,
        description="Post ID",
    )


class NewsfeedItemVideoResponse(BaseResponse):
    response: "NewsfeedItemVideoResponseModel"


class NewsfeedItemVideoVideoResponseModel(BaseModel):
    count: typing.Optional[int] = Field(
        default=None,
        description="Tags number",
    )

    items: typing.Optional[typing.List[VideoVideoFull]] = Field(
        default=None,
    )


class NewsfeedItemVideoVideoResponse(BaseResponse):
    response: "NewsfeedItemVideoVideoResponseModel"


class NewsfeedItemWallpostResponseModel(
    WallCarouselBase, NewsfeedItemBase, WallWallpostFull
):
    pass


class NewsfeedItemWallpostResponse(BaseResponse):
    response: "NewsfeedItemWallpostResponseModel"


class NewsfeedItemWallpostFeedbackResponseModel(BaseModel):
    type: "NewsfeedItemWallpostFeedbackType" = Field()

    question: str = Field()

    answers: typing.Optional[typing.List[NewsfeedItemWallpostFeedbackAnswer]] = Field(
        default=None,
    )

    stars_count: typing.Optional[int] = Field(
        default=None,
    )

    descriptions: typing.Optional[typing.List[str]] = Field(
        default=None,
    )

    gratitude: typing.Optional[str] = Field(
        default=None,
    )

    track_code: typing.Optional[str] = Field(
        default=None,
    )


class NewsfeedItemWallpostFeedbackResponse(BaseResponse):
    response: "NewsfeedItemWallpostFeedbackResponseModel"


class NewsfeedItemWallpostFeedbackAnswerResponseModel(BaseModel):
    title: str = Field()

    id: str = Field()


class NewsfeedItemWallpostFeedbackAnswerResponse(BaseResponse):
    response: "NewsfeedItemWallpostFeedbackAnswerResponseModel"


class NewsfeedItemWallpostFeedbackTypeResponseModel(enum.Enum):
    BUTTONS = "buttons"

    STARS = "stars"


class NewsfeedItemWallpostFeedbackTypeResponse(BaseResponse):
    response: "NewsfeedItemWallpostFeedbackTypeResponseModel"


class NewsfeedListResponseModel(BaseModel):
    id: int = Field(
        description="List ID",
    )

    title: str = Field(
        description="List title",
    )


class NewsfeedListResponse(BaseResponse):
    response: "NewsfeedListResponseModel"


class NewsfeedListFullResponseModel(NewsfeedList):
    no_reposts: typing.Optional[bool] = Field(
        default=None,
        description="Information whether reposts hiding is enabled",
    )

    source_ids: typing.Optional[typing.List[int]] = Field(
        default=None,
    )


class NewsfeedListFullResponse(BaseResponse):
    response: "NewsfeedListFullResponseModel"


class NewsfeedNewsfeedItemResponseModel(BaseModel):
    pass


class NewsfeedNewsfeedItemResponse(BaseResponse):
    response: "NewsfeedNewsfeedItemResponseModel"


class NewsfeedNewsfeedItemTypeResponseModel(enum.Enum):
    POST = "post"

    PHOTO = "photo"

    PHOTO_TAG = "photo_tag"

    WALL_PHOTO = "wall_photo"

    FRIEND = "friend"

    AUDIO = "audio"

    VIDEO = "video"

    TOPIC = "topic"

    DIGEST = "digest"

    STORIES = "stories"

    NOTE = "note"

    AUDIO_PLAYLIST = "audio_playlist"

    CLIP = "clip"


class NewsfeedNewsfeedItemTypeResponse(BaseResponse):
    response: "NewsfeedNewsfeedItemTypeResponseModel"
