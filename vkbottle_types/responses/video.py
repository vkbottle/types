from .base_response import BaseResponse
from vkbottle_types.objects import users, groups, wall, video, base
from typing import Optional, Any, List, Union
import typing


class AddAlbumResponse(BaseResponse):
    response: Optional["AddAlbumResponseModel"] = None


class CreateCommentResponse(BaseResponse):
    response: Optional["CreateCommentResponseModel"] = None


class GetAlbumByIdResponse(BaseResponse):
    response: Optional["GetAlbumByIdResponseModel"] = None


class GetAlbumsByVideoExtendedResponse(BaseResponse):
    response: Optional["GetAlbumsByVideoExtendedResponseModel"] = None


class GetAlbumsByVideoResponse(BaseResponse):
    response: Optional["GetAlbumsByVideoResponseModel"] = None


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
    response: Optional["RestoreCommentResponseModel"] = None


class SaveResponse(BaseResponse):
    response: Optional["SaveResponseModel"] = None


class SearchExtendedResponse(BaseResponse):
    response: Optional["SearchExtendedResponseModel"] = None


class SearchResponse(BaseResponse):
    response: Optional["SearchResponseModel"] = None


class AddAlbumResponseModel(BaseResponse):
    album_id: Optional[int] = None


CreateCommentResponseModel = int


GetAlbumByIdResponseModel = Optional["video.VideoAlbumFull"]


class GetAlbumsByVideoExtendedResponseModel(BaseResponse):
    count: Optional[int] = None
    items: Optional[List["video.VideoAlbumFull"]] = None


GetAlbumsByVideoResponseModel = List[int]


class GetAlbumsExtendedResponseModel(BaseResponse):
    count: Optional[int] = None
    items: Optional[List["video.VideoAlbumFull"]] = None


class GetAlbumsResponseModel(BaseResponse):
    count: Optional[int] = None
    items: Optional[List["video.VideoAlbumFull"]] = None


class GetCommentsExtendedResponseModel(BaseResponse):
    count: Optional[int] = None
    items: Optional[List["wall.WallComment"]] = None
    profiles: Optional[List["users.UserMin"]] = None
    groups: Optional[List["groups.GroupFull"]] = None


class GetCommentsResponseModel(BaseResponse):
    count: Optional[int] = None
    items: Optional[List["wall.WallComment"]] = None


class GetExtendedResponseModel(BaseResponse):
    count: Optional[int] = None
    items: Optional[List["video.VideoFull"]] = None
    profiles: Optional[List["users.UserMin"]] = None
    groups: Optional[List["groups.GroupFull"]] = None


class GetResponseModel(BaseResponse):
    count: Optional[int] = None
    items: Optional[List["video.Video"]] = None


RestoreCommentResponseModel = Optional["base.BoolInt"]


SaveResponseModel = Optional["video.SaveResult"]


class SearchExtendedResponseModel(BaseResponse):
    count: Optional[int] = None
    items: Optional[List["video.Video"]] = None
    profiles: Optional[List["users.UserMin"]] = None
    groups: Optional[List["groups.GroupFull"]] = None


class SearchResponseModel(BaseResponse):
    count: Optional[int] = None
    items: Optional[List["video.Video"]] = None
