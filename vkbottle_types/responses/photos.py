from .base_response import BaseResponse
from vkbottle_types.objects import users, groups, wall, photos, base
from typing import Optional, Any, List, Union
import typing


class CopyResponse(BaseResponse):
    response: Optional["CopyResponseModel"] = None


class CreateAlbumResponse(BaseResponse):
    response: Optional["CreateAlbumResponseModel"] = None


class CreateCommentResponse(BaseResponse):
    response: Optional["CreateCommentResponseModel"] = None


class DeleteCommentResponse(BaseResponse):
    response: Optional["DeleteCommentResponseModel"] = None


class GetAlbumsCountResponse(BaseResponse):
    response: Optional["GetAlbumsCountResponseModel"] = None


class GetAlbumsResponse(BaseResponse):
    response: Optional["GetAlbumsResponseModel"] = None


class GetAllCommentsResponse(BaseResponse):
    response: Optional["GetAllCommentsResponseModel"] = None


class GetAllExtendedResponse(BaseResponse):
    response: Optional["GetAllExtendedResponseModel"] = None


class GetAllResponse(BaseResponse):
    response: Optional["GetAllResponseModel"] = None


class GetByIdExtendedResponse(BaseResponse):
    response: Optional["GetByIdExtendedResponseModel"] = None


class GetByIdResponse(BaseResponse):
    response: Optional["GetByIdResponseModel"] = None


class GetCommentsExtendedResponse(BaseResponse):
    response: Optional["GetCommentsExtendedResponseModel"] = None


class GetCommentsResponse(BaseResponse):
    response: Optional["GetCommentsResponseModel"] = None


class GetMarketUploadServerResponse(BaseResponse):
    response: Optional["GetMarketUploadServerResponseModel"] = None


class GetMessagesUploadServerResponse(BaseResponse):
    response: Optional["GetMessagesUploadServerResponseModel"] = None


class GetNewTagsResponse(BaseResponse):
    response: Optional["GetNewTagsResponseModel"] = None


class GetTagsResponse(BaseResponse):
    response: Optional["GetTagsResponseModel"] = None


class GetUploadServerResponse(BaseResponse):
    response: Optional["GetUploadServerResponseModel"] = None


class GetUserPhotosExtendedResponse(BaseResponse):
    response: Optional["GetUserPhotosExtendedResponseModel"] = None


class GetUserPhotosResponse(BaseResponse):
    response: Optional["GetUserPhotosResponseModel"] = None


class GetWallUploadServerResponse(BaseResponse):
    response: Optional["GetWallUploadServerResponseModel"] = None


class GetExtendedResponse(BaseResponse):
    response: Optional["GetExtendedResponseModel"] = None


class GetResponse(BaseResponse):
    response: Optional["GetResponseModel"] = None


class PutTagResponse(BaseResponse):
    response: Optional["PutTagResponseModel"] = None


class RestoreCommentResponse(BaseResponse):
    response: Optional["RestoreCommentResponseModel"] = None


class SaveMarketAlbumPhotoResponse(BaseResponse):
    response: Optional["SaveMarketAlbumPhotoResponseModel"] = None


class SaveMarketPhotoResponse(BaseResponse):
    response: Optional["SaveMarketPhotoResponseModel"] = None


class SaveMessagesPhotoResponse(BaseResponse):
    response: Optional["SaveMessagesPhotoResponseModel"] = None


class SaveOwnerCoverPhotoResponse(BaseResponse):
    response: Optional["SaveOwnerCoverPhotoResponseModel"] = None


class SaveOwnerPhotoResponse(BaseResponse):
    response: Optional["SaveOwnerPhotoResponseModel"] = None


class SaveWallPhotoResponse(BaseResponse):
    response: Optional["SaveWallPhotoResponseModel"] = None


class SaveResponse(BaseResponse):
    response: Optional["SaveResponseModel"] = None


class SearchResponse(BaseResponse):
    response: Optional["SearchResponseModel"] = None


CopyResponseModel = int


CreateAlbumResponseModel = Optional["photos.PhotoAlbumFull"]


CreateCommentResponseModel = int


DeleteCommentResponseModel = Optional["base.BoolInt"]


GetAlbumsCountResponseModel = int


class GetAlbumsResponseModel(BaseResponse):
    count: Optional[int] = None
    items: Optional[List["photos.PhotoAlbumFull"]] = None


class GetAllCommentsResponseModel(BaseResponse):
    count: Optional[int] = None
    items: Optional[List["photos.CommentXtrPid"]] = None


class GetAllExtendedResponseModel(BaseResponse):
    count: Optional[int] = None
    items: Optional[List["photos.PhotoFullXtrRealOffset"]] = None
    more: Optional["base.BoolInt"] = None


class GetAllResponseModel(BaseResponse):
    count: Optional[int] = None
    items: Optional[List["photos.PhotoXtrRealOffset"]] = None
    more: Optional["base.BoolInt"] = None


GetByIdExtendedResponseModel = List["photos.PhotoFull"]


GetByIdResponseModel = List["photos.Photo"]


class GetCommentsExtendedResponseModel(BaseResponse):
    count: Optional[int] = None
    real_offset: Optional[int] = None
    items: Optional[List["wall.WallComment"]] = None
    profiles: Optional[List["users.UserFull"]] = None
    groups: Optional[List["groups.GroupFull"]] = None


class GetCommentsResponseModel(BaseResponse):
    count: Optional[int] = None
    real_offset: Optional[int] = None
    items: Optional[List["wall.WallComment"]] = None


GetMarketUploadServerResponseModel = Optional["base.UploadServer"]


GetMessagesUploadServerResponseModel = Optional["photos.PhotoUpload"]


class GetNewTagsResponseModel(BaseResponse):
    count: Optional[int] = None
    items: Optional[List["photos.PhotoXtrTagInfo"]] = None


GetTagsResponseModel = List["photos.PhotoTag"]


GetUploadServerResponseModel = Optional["photos.PhotoUpload"]


class GetUserPhotosExtendedResponseModel(BaseResponse):
    count: Optional[int] = None
    items: Optional[List["photos.PhotoFull"]] = None


class GetUserPhotosResponseModel(BaseResponse):
    count: Optional[int] = None
    items: Optional[List["photos.Photo"]] = None


GetWallUploadServerResponseModel = Optional["photos.PhotoUpload"]


class GetExtendedResponseModel(BaseResponse):
    count: Optional[int] = None
    items: Optional[List["photos.PhotoFull"]] = None


class GetResponseModel(BaseResponse):
    count: Optional[int] = None
    items: Optional[List["photos.Photo"]] = None


PutTagResponseModel = int


RestoreCommentResponseModel = Optional["base.BoolInt"]


SaveMarketAlbumPhotoResponseModel = List["photos.Photo"]


SaveMarketPhotoResponseModel = List["photos.Photo"]


SaveMessagesPhotoResponseModel = List["photos.Photo"]


SaveOwnerCoverPhotoResponseModel = List["base.Image"]


class SaveOwnerPhotoResponseModel(BaseResponse):
    photo_hash: Optional[str] = None
    photo_src: Optional[str] = None
    photo_src_big: Optional[str] = None
    photo_src_small: Optional[str] = None
    saved: Optional[int] = None
    post_id: Optional[int] = None


SaveWallPhotoResponseModel = List["photos.Photo"]


SaveResponseModel = List["photos.Photo"]


class SearchResponseModel(BaseResponse):
    count: Optional[int] = None
    items: Optional[List["photos.Photo"]] = None
