import typing
from vkbottle_types.responses.base_response import BaseResponse, BaseModel
from vkbottle_types.base_model import Field

from vkbottle_types.objects import (
    WallPostSource,
    WidgetsCommentMediaType,
    WallCommentAttachment,
    WidgetsWidgetLikes,
    BaseBoolInt,
    UsersUserFull,
    WidgetsCommentReplies,
    WidgetsCommentRepliesItem,
    BaseObjectCount,
    BaseRepostsInfo,
    WidgetsCommentMedia,
    BaseLikesInfo,
)


class WidgetsCommentMediaResponseModel(BaseModel):
    item_id: typing.Optional[int] = Field(
        default=None,
        description="Media item ID",
    )

    owner_id: typing.Optional[int] = Field(
        default=None,
        description="Media owner's ID",
    )

    thumb_src: typing.Optional[str] = Field(
        default=None,
        description="URL of the preview image (type=photo only)",
    )

    type: typing.Optional["WidgetsCommentMediaType"] = Field(
        default=None,
    )


class WidgetsCommentMediaResponse(BaseResponse):
    response: "WidgetsCommentMediaResponseModel"


class WidgetsCommentMediaTypeResponseModel(enum.Enum):
    AUDIO = "audio"

    PHOTO = "photo"

    VIDEO = "video"


class WidgetsCommentMediaTypeResponse(BaseResponse):
    response: "WidgetsCommentMediaTypeResponseModel"


class WidgetsCommentRepliesResponseModel(BaseModel):
    can_post: typing.Optional[bool] = Field(
        default=None,
        description="Information whether current user can comment the post",
    )

    count: typing.Optional[int] = Field(
        default=None,
        description="Comments number",
    )

    replies: typing.Optional[typing.List[WidgetsCommentRepliesItem]] = Field(
        default=None,
    )

    groups_can_post: typing.Optional[bool] = Field(
        default=None,
        description="Information whether groups can comment the post",
    )

    can_view: typing.Optional[bool] = Field(
        default=None,
        description="Information whether current user can view the comments",
    )


class WidgetsCommentRepliesResponse(BaseResponse):
    response: "WidgetsCommentRepliesResponseModel"


class WidgetsCommentRepliesItemResponseModel(BaseModel):
    cid: typing.Optional[int] = Field(
        default=None,
        description="Comment ID",
    )

    date: typing.Optional[int] = Field(
        default=None,
        description="Date when the comment has been added in Unixtime",
    )

    likes: typing.Optional["WidgetsWidgetLikes"] = Field(
        default=None,
    )

    text: typing.Optional[str] = Field(
        default=None,
        description="Comment text",
    )

    uid: typing.Optional[int] = Field(
        default=None,
        description="User ID",
    )

    user: typing.Optional["UsersUserFull"] = Field(
        default=None,
    )


class WidgetsCommentRepliesItemResponse(BaseResponse):
    response: "WidgetsCommentRepliesItemResponseModel"


class WidgetsWidgetCommentResponseModel(BaseModel):
    date: int = Field(
        description="Date when the comment has been added in Unixtime",
    )

    from_id: int = Field(
        description="Comment author ID",
    )

    id: int = Field(
        description="Comment ID",
    )

    post_type: str = Field(
        description="Post type",
    )

    text: str = Field(
        description="Comment text",
    )

    to_id: int = Field(
        description="Wall owner",
    )

    attachments: typing.Optional[typing.List[WallCommentAttachment]] = Field(
        default=None,
    )

    owner_id: typing.Optional[int] = Field(
        default=None,
        description="Wall owner's ID",
    )

    can_delete: typing.Optional[bool] = Field(
        default=None,
        description="Information whether current user can delete the comment",
    )

    comments: typing.Optional["WidgetsCommentReplies"] = Field(
        default=None,
    )

    likes: typing.Optional["BaseLikesInfo"] = Field(
        default=None,
    )

    media: typing.Optional["WidgetsCommentMedia"] = Field(
        default=None,
    )

    post_source: typing.Optional["WallPostSource"] = Field(
        default=None,
    )

    reposts: typing.Optional["BaseRepostsInfo"] = Field(
        default=None,
    )

    user: typing.Optional["UsersUserFull"] = Field(
        default=None,
    )

    is_favorite: typing.Optional[bool] = Field(
        default=None,
        description="Information whether the post in favorites list",
    )

    short_text_rate: typing.Optional[float] = Field(
        default=None,
        description="Preview length control parameter",
    )


class WidgetsWidgetCommentResponse(BaseResponse):
    response: "WidgetsWidgetCommentResponseModel"


class WidgetsWidgetLikesResponseModel(BaseModel):
    count: typing.Optional[int] = Field(
        default=None,
        description="Likes number",
    )


class WidgetsWidgetLikesResponse(BaseResponse):
    response: "WidgetsWidgetLikesResponseModel"


class WidgetsWidgetPageResponseModel(BaseModel):
    comments: typing.Optional["BaseObjectCount"] = Field(
        default=None,
    )

    date: typing.Optional[int] = Field(
        default=None,
        description="Date when widgets on the page has been initialized firstly in Unixtime",
    )

    description: typing.Optional[str] = Field(
        default=None,
        description="Page description",
    )

    id: typing.Optional[int] = Field(
        default=None,
        description="Page ID",
    )

    likes: typing.Optional["BaseObjectCount"] = Field(
        default=None,
    )

    page_id: typing.Optional[str] = Field(
        default=None,
        description="page_id parameter value",
    )

    photo: typing.Optional[str] = Field(
        default=None,
        description="URL of the preview image",
    )

    title: typing.Optional[str] = Field(
        default=None,
        description="Page title",
    )

    url: typing.Optional[str] = Field(
        default=None,
        description="Page absolute URL",
    )


class WidgetsWidgetPageResponse(BaseResponse):
    response: "WidgetsWidgetPageResponseModel"
