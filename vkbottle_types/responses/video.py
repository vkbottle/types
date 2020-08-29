import typing
from typing import Optional

from vkbottle_types.objects import video, base, groups, wall, users
from .base_response import BaseResponse


class AddAlbumResponse(BaseResponse):
    response: Optional["AddAlbumResponseModel"] = None


class CreateCommentResponse(BaseResponse):
    response: Optional[int] = None


class GetAlbumByIdResponse(BaseResponse):
    response: Optional[typing.List["video.VideoAlbumFull"]] = None


class GetAlbumsByVideoExtendedResponse(BaseResponse):
    response: Optional["GetAlbumsByVideoExtendedResponseModel"] = None


class GetAlbumsByVideoResponse(BaseResponse):
    response: Optional[typing.List[int]] = None


class GetAlbumsExtendedResponse(BaseResponse):
    response: Optional["GetAlbumsExtendedResponseModel"] = None


class GetAlbumsResponse(BaseResponse):
    response: Optional["GetAlbumsResponseModel"] = None


class GetCommentsExtendedResponse(BaseResponse):
    response: Optional["GetCommentsExtendedResponseModel"] = None


class GetCommentsResponse(BaseResponse):
    response: Optional["GetCommentsResponseModel"] = None


class GetExtendedResponse(BaseResponse):
    response: Optional["GetExtendedResponseModel"] = None


class GetResponse(BaseResponse):
    response: Optional["GetResponseModel"] = None


class RestoreCommentResponse(BaseResponse):
    response: Optional[typing.List["base.BoolInt"]] = None


class SaveResponse(BaseResponse):
    response: Optional[typing.List["video.SaveResult"]] = None


class SearchExtendedResponse(BaseResponse):
    response: Optional["SearchExtendedResponseModel"] = None


class SearchResponse(BaseResponse):
    response: Optional["SearchResponseModel"] = None


class AddAlbumResponseModel(BaseResponse):
    album_id: Optional[int] = None


class GetAlbumsByVideoExtendedResponseModel(BaseResponse):
    count: Optional[int] = None
    items: Optional[typing.List["video.VideoAlbumFull"]] = None


class GetAlbumsExtendedResponseModel(BaseResponse):
    count: Optional[int] = None
    items: Optional[typing.List["video.VideoAlbumFull"]] = None


class GetAlbumsResponseModel(BaseResponse):
    count: Optional[int] = None
    items: Optional[typing.List["video.VideoAlbumFull"]] = None


class GetCommentsExtendedResponseModel(BaseResponse):
    count: Optional[int] = None
    items: Optional[typing.List["wall.WallComment"]] = None
    profiles: Optional[typing.List["users.UserMin"]] = None
    groups: Optional[typing.List["groups.GroupFull"]] = None


class GetCommentsResponseModel(BaseResponse):
    count: Optional[int] = None
    items: Optional[typing.List["wall.WallComment"]] = None


class GetExtendedResponseModel(BaseResponse):
    count: Optional[int] = None
    items: Optional[typing.List["video.VideoFull"]] = None
    profiles: Optional[typing.List["users.UserMin"]] = None
    groups: Optional[typing.List["groups.GroupFull"]] = None


class GetResponseModel(BaseResponse):
    count: Optional[int] = None
    items: Optional[typing.List["video.Video"]] = None


class SearchExtendedResponseModel(BaseResponse):
    count: Optional[int] = None
    items: Optional[typing.List["video.Video"]] = None
    profiles: Optional[typing.List["users.UserMin"]] = None
    groups: Optional[typing.List["groups.GroupFull"]] = None


class SearchResponseModel(BaseResponse):
    count: Optional[int] = None
    items: Optional[typing.List["video.Video"]] = None
