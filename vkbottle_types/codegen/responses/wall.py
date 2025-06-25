import typing

from vkbottle_types.base_model import BaseModel, Field
from vkbottle_types.objects import GroupsGroupFull, UsersUser, UsersUserFull, WallWallComment, WallWallItem, WallWallpostAttachment, WallWallpostFull
from vkbottle_types.responses.base_response import BaseResponse


class WallCreateCommentResponseModel(BaseModel):
    comment_id: int = Field()
    parents_stack: typing.Optional[typing.List[int]] = Field(
        default=None,
    )


class WallCreateCommentResponse(BaseResponse):
    response: "WallCreateCommentResponseModel" = Field()


class WallEditResponseModel(BaseModel):
    post_id: int = Field()


class WallEditResponse(BaseResponse):
    response: "WallEditResponseModel" = Field()


class WallGetByIdExtendedResponseModel(BaseModel):
    items: typing.List["WallWallItem"] = Field()
    profiles: typing.List["UsersUserFull"] = Field()
    groups: typing.List["GroupsGroupFull"] = Field()


class WallGetByIdExtendedResponse(BaseResponse):
    response: "WallGetByIdExtendedResponseModel" = Field()


class WallGetByIdResponseModel(BaseModel):
    items: typing.Optional[typing.List["WallWallItem"]] = Field(
        default=None,
    )


class WallGetByIdResponse(BaseResponse):
    response: "WallGetByIdResponseModel" = Field()


class WallGetCommentExtendedResponseModel(BaseModel):
    items: typing.List["WallWallComment"] = Field()
    profiles: typing.List["UsersUserFull"] = Field()
    groups: typing.List["GroupsGroupFull"] = Field()
    can_post: typing.Optional[bool] = Field(
        default=None,
    )
    show_reply_button: typing.Optional[bool] = Field(
        default=None,
    )
    groups_can_post: typing.Optional[bool] = Field(
        default=None,
    )
    post_author_id: typing.Optional[int] = Field(
        default=None,
    )


class WallGetCommentExtendedResponse(BaseResponse):
    response: "WallGetCommentExtendedResponseModel" = Field()


class WallGetCommentResponseModel(BaseModel):
    items: typing.List["WallWallComment"] = Field()
    can_post: typing.Optional[bool] = Field(
        default=None,
    )
    show_reply_button: typing.Optional[bool] = Field(
        default=None,
    )
    groups_can_post: typing.Optional[bool] = Field(
        default=None,
    )


class WallGetCommentResponse(BaseResponse):
    response: "WallGetCommentResponseModel" = Field()


class WallGetCommentsExtendedResponseModel(BaseModel):
    count: int = Field()
    items: typing.List["WallWallComment"] = Field()
    profiles: typing.List["UsersUserFull"] = Field()
    groups: typing.List["GroupsGroupFull"] = Field()
    current_level_count: typing.Optional[int] = Field(
        default=None,
    )
    can_post: typing.Optional[bool] = Field(
        default=None,
    )
    show_reply_button: typing.Optional[bool] = Field(
        default=None,
    )
    groups_can_post: typing.Optional[bool] = Field(
        default=None,
    )
    post_author_id: typing.Optional[int] = Field(
        default=None,
    )


class WallGetCommentsExtendedResponse(BaseResponse):
    response: "WallGetCommentsExtendedResponseModel" = Field()


class WallGetCommentsResponseModel(BaseModel):
    count: int = Field()
    items: typing.List["WallWallComment"] = Field()
    current_level_count: typing.Optional[int] = Field(
        default=None,
    )
    can_post: typing.Optional[bool] = Field(
        default=None,
    )
    show_reply_button: typing.Optional[bool] = Field(
        default=None,
    )
    groups_can_post: typing.Optional[bool] = Field(
        default=None,
    )


class WallGetCommentsResponse(BaseResponse):
    response: "WallGetCommentsResponseModel" = Field()


class WallGetRepostsResponseModel(BaseModel):
    items: typing.List["WallWallpostFull"] = Field()
    profiles: typing.List["UsersUserFull"] = Field()
    groups: typing.List["GroupsGroupFull"] = Field()


class WallGetRepostsResponse(BaseResponse):
    response: "WallGetRepostsResponseModel" = Field()


class WallGetExtendedResponseModel(BaseModel):
    count: int = Field()
    items: typing.List["WallWallItem"] = Field()
    profiles: typing.List["UsersUserFull"] = Field()
    groups: typing.List["GroupsGroupFull"] = Field()


class WallGetExtendedResponse(BaseResponse):
    response: "WallGetExtendedResponseModel" = Field()


class WallGetResponseModel(BaseModel):
    count: int = Field()
    items: typing.List["WallWallItem"] = Field()


class WallGetResponse(BaseResponse):
    response: "WallGetResponseModel" = Field()


class WallParseAttachedLinkResponseModel(BaseModel):
    data: typing.List["WallWallpostAttachment"] = Field()
    groups: typing.Optional[typing.List["GroupsGroupFull"]] = Field(
        default=None,
    )
    profiles: typing.Optional[typing.List["UsersUser"]] = Field(
        default=None,
    )


class WallParseAttachedLinkResponse(BaseResponse):
    response: "WallParseAttachedLinkResponseModel" = Field()


class WallPostAdsStealthResponseModel(BaseModel):
    post_id: int = Field()


class WallPostAdsStealthResponse(BaseResponse):
    response: "WallPostAdsStealthResponseModel" = Field()


class WallPostResponseModel(BaseModel):
    post_id: int = Field()


class WallPostResponse(BaseResponse):
    response: "WallPostResponseModel" = Field()


class WallRepostResponseModel(BaseModel):
    success: int = Field(default=1)
    post_id: int = Field()
    reposts_count: int = Field()
    likes_count: int = Field()
    wall_repost_count: typing.Optional[int] = Field(
        default=None,
    )
    mail_repost_count: typing.Optional[int] = Field(
        default=None,
    )


class WallRepostResponse(BaseResponse):
    response: "WallRepostResponseModel" = Field()


class WallSearchExtendedResponseModel(BaseModel):
    count: int = Field()
    items: typing.List["WallWallItem"] = Field()
    profiles: typing.List["UsersUserFull"] = Field()
    groups: typing.List["GroupsGroupFull"] = Field()


class WallSearchExtendedResponse(BaseResponse):
    response: "WallSearchExtendedResponseModel" = Field()


class WallSearchResponseModel(BaseModel):
    count: int = Field()
    items: typing.List["WallWallItem"] = Field()


class WallSearchResponse(BaseResponse):
    response: "WallSearchResponseModel" = Field()
