import inspect
import typing
from .base_response import BaseResponse
from vkbottle_types.objects import (
    GroupsGroup,
    GroupsGroupFull,
    UsersUser,
    UsersUserFull,
    WallWallComment,
    WallWallpostFull
)


class CreateCommentResponse(BaseResponse):
    response: "CreateCommentResponseModel" = None


class EditResponse(BaseResponse):
    response: "EditResponseModel" = None


class GetByIdExtendedResponse(BaseResponse):
    response: "GetByIdExtendedResponseModel" = None


class GetByIdLegacyResponse(BaseResponse):
    response: typing.List["WallWallpostFull"] = None


class GetByIdResponse(BaseResponse):
    response: "GetByIdResponseModel" = None


class GetCommentExtendedResponse(BaseResponse):
    response: "GetCommentExtendedResponseModel" = None


class GetCommentResponse(BaseResponse):
    response: "GetCommentResponseModel" = None


class GetCommentsExtendedResponse(BaseResponse):
    response: "GetCommentsExtendedResponseModel" = None


class GetCommentsResponse(BaseResponse):
    response: "GetCommentsResponseModel" = None


class GetRepostsResponse(BaseResponse):
    response: "GetRepostsResponseModel" = None


class GetExtendedResponse(BaseResponse):
    response: "GetExtendedResponseModel" = None


class GetResponse(BaseResponse):
    response: "GetResponseModel" = None


class PostAdsStealthResponse(BaseResponse):
    response: "PostAdsStealthResponseModel" = None


class PostResponse(BaseResponse):
    response: "PostResponseModel" = None


class RepostResponse(BaseResponse):
    response: "RepostResponseModel" = None


class SearchExtendedResponse(BaseResponse):
    response: "SearchExtendedResponseModel" = None


class SearchResponse(BaseResponse):
    response: "SearchResponseModel" = None


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
    show_reply_button: typing.Optional[bool] = None
    can_post: typing.Optional[bool] = None
    groups_can_post: typing.Optional[bool] = None
    current_level_count: typing.Optional[int] = None
    profiles: typing.Optional[typing.List["UsersUser"]] = None
    groups: typing.Optional[typing.List["GroupsGroup"]] = None


class GetCommentsResponseModel(BaseResponse):
    count: typing.Optional[int] = None
    items: typing.Optional[typing.List["WallWallComment"]] = None
    can_post: typing.Optional[bool] = None
    groups_can_post: typing.Optional[bool] = None
    current_level_count: typing.Optional[int] = None


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


for item in locals().copy().values():
    if inspect.isclass(item) and issubclass(item, BaseResponse):
        item.update_forward_refs()
