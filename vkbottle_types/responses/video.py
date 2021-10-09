import inspect
import typing
from .base_response import BaseResponse
from vkbottle_types.objects import (
    BaseBoolInt,
    GroupsGroupFull,
    UsersUser,
    UsersUserMin,
    VideoSaveResult,
    VideoVideo,
    VideoVideoAlbumFull,
    VideoVideoFull,
    WallWallComment
)


class AddAlbumResponse(BaseResponse):
    response: "AddAlbumResponseModel" = None


class CreateCommentResponse(BaseResponse):
    response: int = None


class GetAlbumByIdResponse(BaseResponse):
    response: VideoVideoAlbumFull = None


class GetAlbumsByVideoExtendedResponse(BaseResponse):
    response: "GetAlbumsByVideoExtendedResponseModel" = None


class GetAlbumsByVideoResponse(BaseResponse):
    response: typing.List[int] = None


class GetAlbumsExtendedResponse(BaseResponse):
    response: "GetAlbumsExtendedResponseModel" = None


class GetAlbumsResponse(BaseResponse):
    response: "GetAlbumsResponseModel" = None


class GetCommentsExtendedResponse(BaseResponse):
    response: "GetCommentsExtendedResponseModel" = None


class GetCommentsResponse(BaseResponse):
    response: "GetCommentsResponseModel" = None


class GetResponse(BaseResponse):
    response: "GetResponseModel" = None


class RestoreCommentResponse(BaseResponse):
    response: BaseBoolInt = None


class SaveResponse(BaseResponse):
    response: VideoSaveResult = None


class SearchExtendedResponse(BaseResponse):
    response: "SearchExtendedResponseModel" = None


class SearchResponse(BaseResponse):
    response: "SearchResponseModel" = None


class UploadResponse(BaseResponse):
    response: "UploadResponseModel" = None


class AddAlbumResponseModel(BaseResponse):
    album_id: typing.Optional[int] = None


class GetAlbumsByVideoExtendedResponseModel(BaseResponse):
    count: typing.Optional[int] = None
    items: typing.Optional[typing.List["VideoVideoAlbumFull"]] = None


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


class SearchExtendedResponseModel(BaseResponse):
    count: typing.Optional[int] = None
    items: typing.Optional[typing.List["VideoVideoFull"]] = None
    profiles: typing.Optional[typing.List["UsersUser"]] = None
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
