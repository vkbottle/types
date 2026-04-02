from vkbottle_types.base_model import BaseModel, Field
from vkbottle_types.objects import GroupsGroupFull, UsersUser, UsersUserFull, WallWallComment, WallWallItem, WallWallpostAttachment, WallWallpostFull
from vkbottle_types.responses.base_response import BaseResponse


class WallCreateCommentResponseModel(BaseModel):
    comment_id: int = Field()
    parents_stack: list[int] | None = Field(
        default=None,
    )


class WallCreateCommentResponse(BaseResponse):
    response: "WallCreateCommentResponseModel" = Field()


class WallEditResponseModel(BaseModel):
    post_id: int = Field()


class WallEditResponse(BaseResponse):
    response: "WallEditResponseModel" = Field()


class WallGetByIdExtendedResponseModel(BaseModel):
    items: list["WallWallItem"] = Field()
    profiles: list["UsersUserFull"] = Field()
    groups: list["GroupsGroupFull"] = Field()


class WallGetByIdExtendedResponse(BaseResponse):
    response: "WallGetByIdExtendedResponseModel" = Field()


class WallGetByIdResponseModel(BaseModel):
    items: list["WallWallItem"] | None = Field(
        default=None,
    )


class WallGetByIdResponse(BaseResponse):
    response: "WallGetByIdResponseModel" = Field()


class WallGetCommentExtendedResponseModel(BaseModel):
    items: list["WallWallComment"] = Field()
    profiles: list["UsersUserFull"] = Field()
    groups: list["GroupsGroupFull"] = Field()
    can_post: bool | None = Field(
        default=None,
    )
    show_reply_button: bool | None = Field(
        default=None,
    )
    groups_can_post: bool | None = Field(
        default=None,
    )
    post_author_id: int | None = Field(
        default=None,
    )


class WallGetCommentExtendedResponse(BaseResponse):
    response: "WallGetCommentExtendedResponseModel" = Field()


class WallGetCommentResponseModel(BaseModel):
    items: list["WallWallComment"] = Field()
    can_post: bool | None = Field(
        default=None,
    )
    show_reply_button: bool | None = Field(
        default=None,
    )
    groups_can_post: bool | None = Field(
        default=None,
    )


class WallGetCommentResponse(BaseResponse):
    response: "WallGetCommentResponseModel" = Field()


class WallGetCommentsExtendedResponseModel(BaseModel):
    count: int = Field()
    items: list["WallWallComment"] = Field()
    profiles: list["UsersUserFull"] = Field()
    groups: list["GroupsGroupFull"] = Field()
    current_level_count: int | None = Field(
        default=None,
    )
    can_post: bool | None = Field(
        default=None,
    )
    show_reply_button: bool | None = Field(
        default=None,
    )
    groups_can_post: bool | None = Field(
        default=None,
    )
    post_author_id: int | None = Field(
        default=None,
    )


class WallGetCommentsExtendedResponse(BaseResponse):
    response: "WallGetCommentsExtendedResponseModel" = Field()


class WallGetCommentsResponseModel(BaseModel):
    count: int = Field()
    items: list["WallWallComment"] = Field()
    current_level_count: int | None = Field(
        default=None,
    )
    can_post: bool | None = Field(
        default=None,
    )
    show_reply_button: bool | None = Field(
        default=None,
    )
    groups_can_post: bool | None = Field(
        default=None,
    )


class WallGetCommentsResponse(BaseResponse):
    response: "WallGetCommentsResponseModel" = Field()


class WallGetRepostsResponseModel(BaseModel):
    items: list["WallWallpostFull"] = Field()
    profiles: list["UsersUserFull"] = Field()
    groups: list["GroupsGroupFull"] = Field()


class WallGetRepostsResponse(BaseResponse):
    response: "WallGetRepostsResponseModel" = Field()


class WallGetExtendedResponseModel(BaseModel):
    count: int = Field()
    items: list["WallWallItem"] = Field()
    profiles: list["UsersUserFull"] = Field()
    groups: list["GroupsGroupFull"] = Field()


class WallGetExtendedResponse(BaseResponse):
    response: "WallGetExtendedResponseModel" = Field()


class WallGetResponseModel(BaseModel):
    count: int = Field()
    items: list["WallWallItem"] = Field()


class WallGetResponse(BaseResponse):
    response: "WallGetResponseModel" = Field()


class WallParseAttachedLinkResponseModel(BaseModel):
    data: list["WallWallpostAttachment"] = Field()
    groups: list["GroupsGroupFull"] | None = Field(
        default=None,
    )
    profiles: list["UsersUser"] | None = Field(
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
    wall_repost_count: int | None = Field(
        default=None,
    )
    mail_repost_count: int | None = Field(
        default=None,
    )


class WallRepostResponse(BaseResponse):
    response: "WallRepostResponseModel" = Field()


class WallSearchExtendedResponseModel(BaseModel):
    count: int = Field()
    items: list["WallWallItem"] = Field()
    profiles: list["UsersUserFull"] = Field()
    groups: list["GroupsGroupFull"] = Field()


class WallSearchExtendedResponse(BaseResponse):
    response: "WallSearchExtendedResponseModel" = Field()


class WallSearchResponseModel(BaseModel):
    count: int = Field()
    items: list["WallWallItem"] = Field()


class WallSearchResponse(BaseResponse):
    response: "WallSearchResponseModel" = Field()


__all__ = (
    "WallCreateCommentResponse",
    "WallCreateCommentResponseModel",
    "WallEditResponse",
    "WallEditResponseModel",
    "WallGetByIdExtendedResponse",
    "WallGetByIdExtendedResponseModel",
    "WallGetByIdResponse",
    "WallGetByIdResponseModel",
    "WallGetCommentExtendedResponse",
    "WallGetCommentExtendedResponseModel",
    "WallGetCommentResponse",
    "WallGetCommentResponseModel",
    "WallGetCommentsExtendedResponse",
    "WallGetCommentsExtendedResponseModel",
    "WallGetCommentsResponse",
    "WallGetCommentsResponseModel",
    "WallGetExtendedResponse",
    "WallGetExtendedResponseModel",
    "WallGetRepostsResponse",
    "WallGetRepostsResponseModel",
    "WallGetResponse",
    "WallGetResponseModel",
    "WallParseAttachedLinkResponse",
    "WallParseAttachedLinkResponseModel",
    "WallPostAdsStealthResponse",
    "WallPostAdsStealthResponseModel",
    "WallPostResponse",
    "WallPostResponseModel",
    "WallRepostResponse",
    "WallRepostResponseModel",
    "WallSearchExtendedResponse",
    "WallSearchExtendedResponseModel",
    "WallSearchResponse",
    "WallSearchResponseModel",
)
