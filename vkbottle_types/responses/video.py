import inspect
import typing
from .base_response import BaseResponse
from vkbottle_types.objects import (
    BaseBoolInt,
    GroupsGroupFull,
    UsersUser,
    UsersUserFull,
    VideoSaveResult,
    VideoVideo,
    VideoVideoAlbumFull,
    VideoVideoFull,
    WallWallComment,
)


class AddAlbumResponse(BaseResponse):
    response: "AddAlbumResponseModel"


class CreateCommentResponse(BaseResponse):
    response: int


class GetAlbumByIdResponse(BaseResponse):
    response: VideoVideoAlbumFull


class GetAlbumsByVideoExtendedResponse(BaseResponse):
    response: "GetAlbumsByVideoExtendedResponseModel"


class GetAlbumsByVideoResponse(BaseResponse):
    response: typing.List[int]


class GetAlbumsExtendedResponse(BaseResponse):
    response: "GetAlbumsExtendedResponseModel"


class GetAlbumsResponse(BaseResponse):
    response: "GetAlbumsResponseModel"


class GetCommentsExtendedResponse(BaseResponse):
    response: "GetCommentsExtendedResponseModel"


class GetCommentsResponse(BaseResponse):
    response: "GetCommentsResponseModel"


class GetResponse(BaseResponse):
    response: "GetResponseModel"


class RestoreCommentResponse(BaseResponse):
    response: BaseBoolInt


class SaveResponse(BaseResponse):
    response: VideoSaveResult


class SearchExtendedResponse(BaseResponse):
    response: "SearchExtendedResponseModel"


class SearchResponse(BaseResponse):
    response: "SearchResponseModel"


class UploadResponse(BaseResponse):
    response: "UploadResponseModel"


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
    profiles: typing.Optional[typing.List["UsersUserFull"]] = None
    groups: typing.Optional[typing.List["GroupsGroupFull"]] = None


class GetCommentsResponseModel(BaseResponse):
    count: typing.Optional[int] = None
    items: typing.Optional[typing.List["WallWallComment"]] = None


class GetResponseModel(BaseResponse):
    count: typing.Optional[int] = None
    items: typing.Optional[typing.List["VideoVideoFull"]] = None
    profiles: typing.Optional[typing.List["UsersUserFull"]] = None
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
