import inspect
import typing

from vkbottle_types.objects import (
    GroupsGroup,
    GroupsGroupFull,
    UsersUser,
    UsersUserFull,
    WallWallComment,
    WallWallpostFull,
)

from .base_response import BaseResponse


class CreateCommentResponse(BaseResponse):
    response: typing.Optional["CreateCommentResponseModel"] = None


class EditResponse(BaseResponse):
    response: typing.Optional["EditResponseModel"] = None


class GetByIdExtendedResponse(BaseResponse):
    response: typing.Optional["GetByIdExtendedResponseModel"] = None


class GetByIdLegacyResponse(BaseResponse):
    response: typing.Optional["GetByIdLegacyResponseModel"] = None


class GetByIdResponse(BaseResponse):
    response: typing.Optional["GetByIdResponseModel"] = None


class GetCommentExtendedResponse(BaseResponse):
    response: typing.Optional["GetCommentExtendedResponseModel"] = None


class GetCommentResponse(BaseResponse):
    response: typing.Optional["GetCommentResponseModel"] = None


class GetCommentsExtendedResponse(BaseResponse):
    response: typing.Optional["GetCommentsExtendedResponseModel"] = None


class GetCommentsResponse(BaseResponse):
    response: typing.Optional["GetCommentsResponseModel"] = None


class GetRepostsResponse(BaseResponse):
    response: typing.Optional["GetRepostsResponseModel"] = None


class GetExtendedResponse(BaseResponse):
    response: typing.Optional["GetExtendedResponseModel"] = None


class GetResponse(BaseResponse):
    response: typing.Optional["GetResponseModel"] = None


class PostAdsStealthResponse(BaseResponse):
    response: typing.Optional["PostAdsStealthResponseModel"] = None


class PostResponse(BaseResponse):
    response: typing.Optional["PostResponseModel"] = None


class RepostResponse(BaseResponse):
    response: typing.Optional["RepostResponseModel"] = None


class SearchExtendedResponse(BaseResponse):
    response: typing.Optional["SearchExtendedResponseModel"] = None


class SearchResponse(BaseResponse):
    response: typing.Optional["SearchResponseModel"] = None


class CreateCommentResponseModel(BaseResponse):
    comment_id: typing.Optional[int] = None


class EditResponseModel(BaseResponse):
    post_id: typing.Optional[int] = None


class GetByIdExtendedResponseModel(BaseResponse):
    items: typing.Optional[typing.List["WallWallpostFull"]] = None
    profiles: typing.Optional[typing.List["UsersUserFull"]] = None
    groups: typing.Optional[typing.List["GroupsGroupFull"]] = None


GetByIdLegacyResponseModel = typing.List[WallWallpostFull]


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
