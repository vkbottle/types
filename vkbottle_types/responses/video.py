import inspect
import typing

from vkbottle_types.objects import (
    BaseBoolInt,
    GroupsGroupFull,
    UsersUserMin,
    VideoSaveResult,
    VideoVideo,
    VideoVideoAlbumFull,
    VideoVideoFull,
    WallWallComment,
)

from .base_response import BaseResponse


class AddAlbumResponse(BaseResponse):
    response: typing.Optional["AddAlbumResponseModel"] = None


class CreateCommentResponse(BaseResponse):
    response: typing.Optional["CreateCommentResponseModel"] = None


class GetAlbumByIdResponse(BaseResponse):
    response: typing.Optional["GetAlbumByIdResponseModel"] = None


class GetAlbumsByVideoExtendedResponse(BaseResponse):
    response: typing.Optional["GetAlbumsByVideoExtendedResponseModel"] = None


class GetAlbumsByVideoResponse(BaseResponse):
    response: typing.Optional["GetAlbumsByVideoResponseModel"] = None


class GetAlbumsExtendedResponse(BaseResponse):
    response: typing.Optional["GetAlbumsExtendedResponseModel"] = None


class GetAlbumsResponse(BaseResponse):
    response: typing.Optional["GetAlbumsResponseModel"] = None


class GetCommentsExtendedResponse(BaseResponse):
    response: typing.Optional["GetCommentsExtendedResponseModel"] = None


class GetCommentsResponse(BaseResponse):
    response: typing.Optional["GetCommentsResponseModel"] = None


class GetResponse(BaseResponse):
    response: typing.Optional["GetResponseModel"] = None


class RestoreCommentResponse(BaseResponse):
    response: typing.Optional["RestoreCommentResponseModel"] = None


class SaveResponse(BaseResponse):
    response: typing.Optional["SaveResponseModel"] = None


class SearchExtendedResponse(BaseResponse):
    response: typing.Optional["SearchExtendedResponseModel"] = None


class SearchResponse(BaseResponse):
    response: typing.Optional["SearchResponseModel"] = None


class UploadResponse(BaseResponse):
    response: typing.Optional["UploadResponseModel"] = None


class AddAlbumResponseModel(BaseResponse):
    album_id: typing.Optional[int] = None


CreateCommentResponseModel = int


GetAlbumByIdResponseModel = VideoVideoAlbumFull


class GetAlbumsByVideoExtendedResponseModel(BaseResponse):
    count: typing.Optional[int] = None
    items: typing.Optional[typing.List["VideoVideoAlbumFull"]] = None


GetAlbumsByVideoResponseModel = typing.List[int]


class GetAlbumsExtendedResponseModel(BaseResponse):
    count: typing.Optional[int] = None
    items: typing.Optional[typing.List["VideoVideoAlbumFull"]] = None


class GetAlbumsResponseModel(BaseResponse):
    count: typing.Optional[int] = None
    items: typing.Optional[typing.List["VideoVideoAlbumFull"]] = None


class GetCommentsExtendedResponseModel(BaseResponse):
    count: typing.Optional[int] = None
    items: typing.Optional[typing.List["WallWallComment"]] = None
    profiles: typing.Optional[typing.List["UsersUserMin"]] = None
    groups: typing.Optional[typing.List["GroupsGroupFull"]] = None


class GetCommentsResponseModel(BaseResponse):
    count: typing.Optional[int] = None
    items: typing.Optional[typing.List["WallWallComment"]] = None


class GetResponseModel(BaseResponse):
    count: typing.Optional[int] = None
    items: typing.Optional[typing.List["VideoVideoFull"]] = None
    profiles: typing.Optional[typing.List["UsersUserMin"]] = None
    groups: typing.Optional[typing.List["GroupsGroupFull"]] = None


RestoreCommentResponseModel = BaseBoolInt


SaveResponseModel = VideoSaveResult


class SearchExtendedResponseModel(BaseResponse):
    count: typing.Optional[int] = None
    items: typing.Optional[typing.List["VideoVideoFull"]] = None
    profiles: typing.Optional[typing.List["UsersUserMin"]] = None
    groups: typing.Optional[typing.List["GroupsGroupFull"]] = None


class SearchResponseModel(BaseResponse):
    count: typing.Optional[int] = None
    items: typing.Optional[typing.List["VideoVideo"]] = None


class UploadResponseModel(BaseResponse):
    size: typing.Optional[int] = None
    video_id: typing.Optional[int] = None


for item in locals().copy().values():
    if inspect.isclass(item) and issubclass(item, BaseResponse):
        item.update_forward_refs()
