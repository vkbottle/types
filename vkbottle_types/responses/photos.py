import typing
from typing import Optional

from vkbottle_types.objects import photos, base, groups, wall, users
from .base_response import BaseResponse


class CopyResponse(BaseResponse):
    response: Optional[int] = None


class CreateAlbumResponse(BaseResponse):
    response: Optional[typing.List["photos.PhotoAlbumFull"]] = None


class CreateCommentResponse(BaseResponse):
    response: Optional[int] = None


class DeleteCommentResponse(BaseResponse):
    response: Optional[typing.List["base.BoolInt"]] = None


class GetAlbumsCountResponse(BaseResponse):
    response: Optional[int] = None


class GetAlbumsResponse(BaseResponse):
    response: Optional["GetAlbumsResponseModel"] = None


class GetAllCommentsResponse(BaseResponse):
    response: Optional["GetAllCommentsResponseModel"] = None


class GetAllExtendedResponse(BaseResponse):
    response: Optional["GetAllExtendedResponseModel"] = None


class GetAllResponse(BaseResponse):
    response: Optional["GetAllResponseModel"] = None


class GetByIdExtendedResponse(BaseResponse):
    response: Optional[typing.List["photos.PhotoFull"]] = None


class GetByIdResponse(BaseResponse):
    response: Optional[typing.List["photos.Photo"]] = None


class GetCommentsExtendedResponse(BaseResponse):
    response: Optional["GetCommentsExtendedResponseModel"] = None


class GetCommentsResponse(BaseResponse):
    response: Optional["GetCommentsResponseModel"] = None


class GetMarketUploadServerResponse(BaseResponse):
    response: Optional[typing.List["base.UploadServer"]] = None


class GetMessagesUploadServerResponse(BaseResponse):
    response: Optional[typing.List["photos.PhotoUpload"]] = None


class GetNewTagsResponse(BaseResponse):
    response: Optional["GetNewTagsResponseModel"] = None


class GetTagsResponse(BaseResponse):
    response: Optional[typing.List["photos.PhotoTag"]] = None


class GetUploadServerResponse(BaseResponse):
    response: Optional[typing.List["photos.PhotoUpload"]] = None


class GetUserPhotosExtendedResponse(BaseResponse):
    response: Optional["GetUserPhotosExtendedResponseModel"] = None


class GetUserPhotosResponse(BaseResponse):
    response: Optional["GetUserPhotosResponseModel"] = None


class GetWallUploadServerResponse(BaseResponse):
    response: Optional[typing.List["photos.PhotoUpload"]] = None


class GetExtendedResponse(BaseResponse):
    response: Optional["GetExtendedResponseModel"] = None


class GetResponse(BaseResponse):
    response: Optional["GetResponseModel"] = None


class PutTagResponse(BaseResponse):
    response: Optional[int] = None


class RestoreCommentResponse(BaseResponse):
    response: Optional[typing.List["base.BoolInt"]] = None


class SaveMarketAlbumPhotoResponse(BaseResponse):
    response: Optional[typing.List["photos.Photo"]] = None


class SaveMarketPhotoResponse(BaseResponse):
    response: Optional[typing.List["photos.Photo"]] = None


class SaveMessagesPhotoResponse(BaseResponse):
    response: Optional[typing.List["photos.Photo"]] = None


class SaveOwnerCoverPhotoResponse(BaseResponse):
    response: Optional[typing.List["base.Image"]] = None


class SaveOwnerPhotoResponse(BaseResponse):
    response: Optional["SaveOwnerPhotoResponseModel"] = None


class SaveWallPhotoResponse(BaseResponse):
    response: Optional[typing.List["photos.Photo"]] = None


class SaveResponse(BaseResponse):
    response: Optional[typing.List["photos.Photo"]] = None


class SearchResponse(BaseResponse):
    response: Optional["SearchResponseModel"] = None


class GetAlbumsResponseModel(BaseResponse):
    count: Optional[int] = None
    items: Optional[typing.List["photos.PhotoAlbumFull"]] = None


class GetAllCommentsResponseModel(BaseResponse):
    count: Optional[int] = None
    items: Optional[typing.List["photos.CommentXtrPid"]] = None


class GetAllExtendedResponseModel(BaseResponse):
    count: Optional[int] = None
    items: Optional[typing.List["photos.PhotoFullXtrRealOffset"]] = None
    more: Optional[typing.List["base.BoolInt"]] = None


class GetAllResponseModel(BaseResponse):
    count: Optional[int] = None
    items: Optional[typing.List["photos.PhotoXtrRealOffset"]] = None
    more: Optional[typing.List["base.BoolInt"]] = None


class GetCommentsExtendedResponseModel(BaseResponse):
    count: Optional[int] = None
    real_offset: Optional[int] = None
    items: Optional[typing.List["wall.WallComment"]] = None
    profiles: Optional[typing.List["users.UserFull"]] = None
    groups: Optional[typing.List["groups.GroupFull"]] = None


class GetCommentsResponseModel(BaseResponse):
    count: Optional[int] = None
    real_offset: Optional[int] = None
    items: Optional[typing.List["wall.WallComment"]] = None


class GetNewTagsResponseModel(BaseResponse):
    count: Optional[int] = None
    items: Optional[typing.List["photos.PhotoXtrTagInfo"]] = None


class GetUserPhotosExtendedResponseModel(BaseResponse):
    count: Optional[int] = None
    items: Optional[typing.List["photos.PhotoFull"]] = None


class GetUserPhotosResponseModel(BaseResponse):
    count: Optional[int] = None
    items: Optional[typing.List["photos.Photo"]] = None


class GetExtendedResponseModel(BaseResponse):
    count: Optional[int] = None
    items: Optional[typing.List["photos.PhotoFull"]] = None


class GetResponseModel(BaseResponse):
    count: Optional[int] = None
    items: Optional[typing.List["photos.Photo"]] = None


class SaveOwnerPhotoResponseModel(BaseResponse):
    photo_hash: Optional[str] = None
    photo_src: Optional[str] = None
    photo_src_big: Optional[str] = None
    photo_src_small: Optional[str] = None
    saved: Optional[int] = None
    post_id: Optional[int] = None


class SearchResponseModel(BaseResponse):
    count: Optional[int] = None
    items: Optional[typing.List["photos.Photo"]] = None
