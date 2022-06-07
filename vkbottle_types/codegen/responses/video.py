import typing

from vkbottle_types.objects import (
    BaseBoolInt,
    GroupsGroup,
    GroupsGroupFull,
    UsersUser,
    UsersUserFull,
    VideoSaveResult,
    VideoVideoAlbum,
    VideoVideoAlbumFull,
    VideoVideoFull,
    WallWallComment,
)
from vkbottle_types.responses.base_response import BaseResponse


class AddAlbumResponse(BaseResponse):
    response: "AddAlbumResponseModel"


class ChangeVideoAlbumsResponse(BaseResponse):
    response: typing.List[int]


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
    items: typing.Optional[typing.List["VideoVideoAlbum"]] = None


class GetCommentsExtendedResponseModel(BaseResponse):
    count: typing.Optional[int] = None
    items: typing.Optional[typing.List["WallWallComment"]] = None
    profiles: typing.Optional[typing.List["UsersUser"]] = None
    groups: typing.Optional[typing.List["GroupsGroup"]] = None
    current_level_count: typing.Optional[int] = None
    can_post: typing.Optional[bool] = None
    show_reply_button: typing.Optional[bool] = None
    groups_can_post: typing.Optional[bool] = None
    real_offset: typing.Optional[int] = None


class GetCommentsResponseModel(BaseResponse):
    count: typing.Optional[int] = None
    items: typing.Optional[typing.List["WallWallComment"]] = None
    current_level_count: typing.Optional[int] = None
    can_post: typing.Optional[bool] = None
    show_reply_button: typing.Optional[bool] = None
    groups_can_post: typing.Optional[bool] = None
    real_offset: typing.Optional[int] = None


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
    items: typing.Optional[typing.List["VideoVideoFull"]] = None


class UploadResponseModel(BaseResponse):
    size: typing.Optional[int] = None
    video_id: typing.Optional[int] = None


__all__ = (
    "AddAlbumResponse",
    "AddAlbumResponseModel",
    "BaseBoolInt",
    "ChangeVideoAlbumsResponse",
    "CreateCommentResponse",
    "GetAlbumByIdResponse",
    "GetAlbumsByVideoExtendedResponse",
    "GetAlbumsByVideoExtendedResponseModel",
    "GetAlbumsByVideoResponse",
    "GetAlbumsExtendedResponse",
    "GetAlbumsExtendedResponseModel",
    "GetAlbumsResponse",
    "GetAlbumsResponseModel",
    "GetCommentsExtendedResponse",
    "GetCommentsExtendedResponseModel",
    "GetCommentsResponse",
    "GetCommentsResponseModel",
    "GetResponse",
    "GetResponseModel",
    "GroupsGroup",
    "GroupsGroupFull",
    "RestoreCommentResponse",
    "SaveResponse",
    "SearchExtendedResponse",
    "SearchExtendedResponseModel",
    "SearchResponse",
    "SearchResponseModel",
    "UploadResponse",
    "UploadResponseModel",
    "UsersUser",
    "UsersUserFull",
    "VideoSaveResult",
    "VideoVideoAlbum",
    "VideoVideoAlbumFull",
    "VideoVideoFull",
    "WallWallComment",
)
