import typing

from vkbottle_types.objects import (
    GroupsGroup,
    GroupsGroupFull,
    UsersUser,
    UsersUserFull,
    WallWallComment,
    WallWallpostFull,
)
from vkbottle_types.responses.base_response import BaseResponse


class CreateCommentResponse(BaseResponse):
    response: "CreateCommentResponseModel"


class EditResponse(BaseResponse):
    response: "EditResponseModel"


class GetByIdExtendedResponse(BaseResponse):
    response: "GetByIdExtendedResponseModel"


class GetByIdLegacyResponse(BaseResponse):
    response: typing.List["WallWallpostFull"]


class GetByIdResponse(BaseResponse):
    response: "GetByIdResponseModel"


class GetCommentExtendedResponse(BaseResponse):
    response: "GetCommentExtendedResponseModel"


class GetCommentResponse(BaseResponse):
    response: "GetCommentResponseModel"


class GetCommentsExtendedResponse(BaseResponse):
    response: "GetCommentsExtendedResponseModel"


class GetCommentsResponse(BaseResponse):
    response: "GetCommentsResponseModel"


class GetRepostsResponse(BaseResponse):
    response: "GetRepostsResponseModel"


class GetExtendedResponse(BaseResponse):
    response: "GetExtendedResponseModel"


class GetResponse(BaseResponse):
    response: "GetResponseModel"


class PostAdsStealthResponse(BaseResponse):
    response: "PostAdsStealthResponseModel"


class PostResponse(BaseResponse):
    response: "PostResponseModel"


class RepostResponse(BaseResponse):
    response: "RepostResponseModel"


class SearchExtendedResponse(BaseResponse):
    response: "SearchExtendedResponseModel"


class SearchResponse(BaseResponse):
    response: "SearchResponseModel"


class CreateCommentResponseModel(BaseResponse):
    comment_id: typing.Optional[int] = None


class EditResponseModel(BaseResponse):
    post_id: typing.Optional[int] = None


class GetByIdExtendedResponseModel(BaseResponse):
    items: typing.Optional[typing.List["WallWallpostFull"]] = None
    profiles: typing.Optional[typing.List["UsersUserFull"]] = None
    groups: typing.Optional[typing.List["GroupsGroupFull"]] = None


class GetByIdResponseModel(BaseResponse):
    items: typing.Optional[typing.List["WallWallpostFull"]] = None


class GetCommentExtendedResponseModel(BaseResponse):
    items: typing.Optional[typing.List["WallWallComment"]] = None
    profiles: typing.Optional[typing.List["UsersUser"]] = None
    groups: typing.Optional[typing.List["GroupsGroup"]] = None


class GetCommentResponseModel(BaseResponse):
    items: typing.Optional[typing.List["WallWallComment"]] = None


class GetCommentsExtendedResponseModel(BaseResponse):
    count: typing.Optional[int] = None
    items: typing.Optional[typing.List["WallWallComment"]] = None
    profiles: typing.Optional[typing.List["UsersUser"]] = None
    groups: typing.Optional[typing.List["GroupsGroup"]] = None
    current_level_count: typing.Optional[int] = None
    can_post: typing.Optional[bool] = None
    show_reply_button: typing.Optional[bool] = None
    groups_can_post: typing.Optional[bool] = None


class GetCommentsResponseModel(BaseResponse):
    count: typing.Optional[int] = None
    items: typing.Optional[typing.List["WallWallComment"]] = None
    current_level_count: typing.Optional[int] = None
    can_post: typing.Optional[bool] = None
    show_reply_button: typing.Optional[bool] = None
    groups_can_post: typing.Optional[bool] = None


class GetRepostsResponseModel(BaseResponse):
    items: typing.Optional[typing.List["WallWallpostFull"]] = None
    profiles: typing.Optional[typing.List["UsersUser"]] = None
    groups: typing.Optional[typing.List["GroupsGroup"]] = None


class GetExtendedResponseModel(BaseResponse):
    count: typing.Optional[int] = None
    items: typing.Optional[typing.List["WallWallpostFull"]] = None
    profiles: typing.Optional[typing.List["UsersUserFull"]] = None
    groups: typing.Optional[typing.List["GroupsGroupFull"]] = None


class GetResponseModel(BaseResponse):
    count: typing.Optional[int] = None
    items: typing.Optional[typing.List["WallWallpostFull"]] = None


class PostAdsStealthResponseModel(BaseResponse):
    post_id: typing.Optional[int] = None


class PostResponseModel(BaseResponse):
    post_id: typing.Optional[int] = None


class RepostResponseModel(BaseResponse):
    success: typing.Optional[int] = None
    post_id: typing.Optional[int] = None
    reposts_count: typing.Optional[int] = None
    wall_repost_count: typing.Optional[int] = None
    mail_repost_count: typing.Optional[int] = None
    likes_count: typing.Optional[int] = None


class SearchExtendedResponseModel(BaseResponse):
    count: typing.Optional[int] = None
    items: typing.Optional[typing.List["WallWallpostFull"]] = None
    profiles: typing.Optional[typing.List["UsersUserFull"]] = None
    groups: typing.Optional[typing.List["GroupsGroupFull"]] = None


class SearchResponseModel(BaseResponse):
    count: typing.Optional[int] = None
    items: typing.Optional[typing.List["WallWallpostFull"]] = None


__all__ = (
    "CreateCommentResponse",
    "CreateCommentResponseModel",
    "EditResponse",
    "EditResponseModel",
    "GetByIdExtendedResponse",
    "GetByIdExtendedResponseModel",
    "GetByIdLegacyResponse",
    "GetByIdResponse",
    "GetByIdResponseModel",
    "GetCommentExtendedResponse",
    "GetCommentExtendedResponseModel",
    "GetCommentResponse",
    "GetCommentResponseModel",
    "GetCommentsExtendedResponse",
    "GetCommentsExtendedResponseModel",
    "GetCommentsResponse",
    "GetCommentsResponseModel",
    "GetExtendedResponse",
    "GetExtendedResponseModel",
    "GetRepostsResponse",
    "GetRepostsResponseModel",
    "GetResponse",
    "GetResponseModel",
    "GroupsGroup",
    "GroupsGroupFull",
    "PostAdsStealthResponse",
    "PostAdsStealthResponseModel",
    "PostResponse",
    "PostResponseModel",
    "RepostResponse",
    "RepostResponseModel",
    "SearchExtendedResponse",
    "SearchExtendedResponseModel",
    "SearchResponse",
    "SearchResponseModel",
    "UsersUser",
    "UsersUserFull",
    "WallWallComment",
    "WallWallpostFull",
)
