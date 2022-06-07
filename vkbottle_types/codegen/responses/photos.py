import typing

from vkbottle_types.objects import (
    BaseBoolInt,
    BaseImage,
    BaseUploadServer,
    GroupsGroupFull,
    PhotosPhoto,
    PhotosPhotoAlbumFull,
    PhotosPhotoFullXtrRealOffset,
    PhotosPhotoTag,
    PhotosPhotoUpload,
    PhotosPhotoXtrRealOffset,
    PhotosPhotoXtrTagInfo,
    UsersUserFull,
    WallWallComment,
)
from vkbottle_types.responses.base_response import BaseResponse


class CopyResponse(BaseResponse):
    response: int


class CreateAlbumResponse(BaseResponse):
    response: PhotosPhotoAlbumFull


class CreateCommentResponse(BaseResponse):
    response: int


class DeleteCommentResponse(BaseResponse):
    response: BaseBoolInt


class GetAlbumsCountResponse(BaseResponse):
    response: int


class GetAlbumsResponse(BaseResponse):
    response: "GetAlbumsResponseModel"


class GetAllCommentsResponse(BaseResponse):
    response: "GetAllCommentsResponseModel"


class GetAllExtendedResponse(BaseResponse):
    response: "GetAllExtendedResponseModel"


class GetAllResponse(BaseResponse):
    response: "GetAllResponseModel"


class GetByIdResponse(BaseResponse):
    response: typing.List["PhotosPhoto"]


class GetCommentsExtendedResponse(BaseResponse):
    response: "GetCommentsExtendedResponseModel"


class GetCommentsResponse(BaseResponse):
    response: "GetCommentsResponseModel"


class GetMarketUploadServerResponse(BaseResponse):
    response: BaseUploadServer


class GetMessagesUploadServerResponse(BaseResponse):
    response: PhotosPhotoUpload


class GetNewTagsResponse(BaseResponse):
    response: "GetNewTagsResponseModel"


class GetTagsResponse(BaseResponse):
    response: typing.List["PhotosPhotoTag"]


class GetUploadServerResponse(BaseResponse):
    response: PhotosPhotoUpload


class GetUserPhotosResponse(BaseResponse):
    response: "GetUserPhotosResponseModel"


class GetWallUploadServerResponse(BaseResponse):
    response: PhotosPhotoUpload


class GetResponse(BaseResponse):
    response: "GetResponseModel"


class MarketAlbumUploadResponse(BaseResponse):
    response: "MarketAlbumUploadResponseModel"


class MarketUploadResponse(BaseResponse):
    response: "MarketUploadResponseModel"


class MessageUploadResponse(BaseResponse):
    response: "MessageUploadResponseModel"


class OwnerCoverUploadResponse(BaseResponse):
    response: "OwnerCoverUploadResponseModel"


class OwnerUploadResponse(BaseResponse):
    response: "OwnerUploadResponseModel"


class PhotoUploadResponse(BaseResponse):
    response: "PhotoUploadResponseModel"


class PutTagResponse(BaseResponse):
    response: int


class RestoreCommentResponse(BaseResponse):
    response: BaseBoolInt


class SaveMarketAlbumPhotoResponse(BaseResponse):
    response: typing.List["PhotosPhoto"]


class SaveMarketPhotoResponse(BaseResponse):
    response: typing.List["PhotosPhoto"]


class SaveMessagesPhotoResponse(BaseResponse):
    response: typing.List["PhotosPhoto"]


class SaveOwnerCoverPhotoResponse(BaseResponse):
    response: "SaveOwnerCoverPhotoResponseModel"


class SaveOwnerPhotoResponse(BaseResponse):
    response: "SaveOwnerPhotoResponseModel"


class SaveWallPhotoResponse(BaseResponse):
    response: typing.List["PhotosPhoto"]


class SaveResponse(BaseResponse):
    response: typing.List["PhotosPhoto"]


class SearchResponse(BaseResponse):
    response: "SearchResponseModel"


class WallUploadResponse(BaseResponse):
    response: "WallUploadResponseModel"


class GetAlbumsResponseModel(BaseResponse):
    count: typing.Optional[int] = None
    items: typing.Optional[typing.List["PhotosPhotoAlbumFull"]] = None


class GetAllCommentsResponseModel(BaseResponse):
    count: typing.Optional[int] = None
    items: typing.Optional[typing.List["WallWallComment"]] = None


class GetAllExtendedResponseModel(BaseResponse):
    count: typing.Optional[int] = None
    items: typing.Optional[typing.List["PhotosPhotoFullXtrRealOffset"]] = None
    more: typing.Optional["BaseBoolInt"] = None


class GetAllResponseModel(BaseResponse):
    count: typing.Optional[int] = None
    items: typing.Optional[typing.List["PhotosPhotoXtrRealOffset"]] = None
    more: typing.Optional["BaseBoolInt"] = None


class GetCommentsExtendedResponseModel(BaseResponse):
    count: typing.Optional[int] = None
    real_offset: typing.Optional[int] = None
    items: typing.Optional[typing.List["WallWallComment"]] = None
    profiles: typing.Optional[typing.List["UsersUserFull"]] = None
    groups: typing.Optional[typing.List["GroupsGroupFull"]] = None


class GetCommentsResponseModel(BaseResponse):
    count: typing.Optional[int] = None
    real_offset: typing.Optional[int] = None
    items: typing.Optional[typing.List["WallWallComment"]] = None


class GetNewTagsResponseModel(BaseResponse):
    count: typing.Optional[int] = None
    items: typing.Optional[typing.List["PhotosPhotoXtrTagInfo"]] = None


class GetUserPhotosResponseModel(BaseResponse):
    count: typing.Optional[int] = None
    items: typing.Optional[typing.List["PhotosPhoto"]] = None


class GetResponseModel(BaseResponse):
    count: typing.Optional[int] = None
    items: typing.Optional[typing.List["PhotosPhoto"]] = None


class MarketAlbumUploadResponseModel(BaseResponse):
    gid: typing.Optional[int] = None
    hash: typing.Optional[str] = None
    photo: typing.Optional[str] = None
    server: typing.Optional[int] = None


class MarketUploadResponseModel(BaseResponse):
    crop_data: typing.Optional[str] = None
    crop_hash: typing.Optional[str] = None
    group_id: typing.Optional[int] = None
    hash: typing.Optional[str] = None
    photo: typing.Optional[str] = None
    server: typing.Optional[int] = None


class MessageUploadResponseModel(BaseResponse):
    hash: typing.Optional[str] = None
    photo: typing.Optional[str] = None
    server: typing.Optional[int] = None


class OwnerCoverUploadResponseModel(BaseResponse):
    hash: typing.Optional[str] = None
    photo: typing.Optional[str] = None


class OwnerUploadResponseModel(BaseResponse):
    hash: typing.Optional[str] = None
    photo: typing.Optional[str] = None
    server: typing.Optional[int] = None


class PhotoUploadResponseModel(BaseResponse):
    aid: typing.Optional[int] = None
    hash: typing.Optional[str] = None
    photo: typing.Optional[str] = None
    photos_list: typing.Optional[str] = None
    server: typing.Optional[int] = None


class SaveOwnerCoverPhotoResponseModel(BaseResponse):
    images: typing.Optional[typing.List["BaseImage"]] = None


class SaveOwnerPhotoResponseModel(BaseResponse):
    photo_hash: typing.Optional[str] = None
    photo_src: typing.Optional[str] = None
    photo_src_big: typing.Optional[str] = None
    photo_src_small: typing.Optional[str] = None
    saved: typing.Optional[int] = None
    post_id: typing.Optional[int] = None


class SearchResponseModel(BaseResponse):
    count: typing.Optional[int] = None
    items: typing.Optional[typing.List["PhotosPhoto"]] = None


class WallUploadResponseModel(BaseResponse):
    hash: typing.Optional[str] = None
    photo: typing.Optional[str] = None
    server: typing.Optional[int] = None


__all__ = (
    "BaseBoolInt",
    "BaseImage",
    "BaseUploadServer",
    "CopyResponse",
    "CreateAlbumResponse",
    "CreateCommentResponse",
    "DeleteCommentResponse",
    "GetAlbumsCountResponse",
    "GetAlbumsResponse",
    "GetAlbumsResponseModel",
    "GetAllCommentsResponse",
    "GetAllCommentsResponseModel",
    "GetAllExtendedResponse",
    "GetAllExtendedResponseModel",
    "GetAllResponse",
    "GetAllResponseModel",
    "GetByIdResponse",
    "GetCommentsExtendedResponse",
    "GetCommentsExtendedResponseModel",
    "GetCommentsResponse",
    "GetCommentsResponseModel",
    "GetMarketUploadServerResponse",
    "GetMessagesUploadServerResponse",
    "GetNewTagsResponse",
    "GetNewTagsResponseModel",
    "GetResponse",
    "GetResponseModel",
    "GetTagsResponse",
    "GetUploadServerResponse",
    "GetUserPhotosResponse",
    "GetUserPhotosResponseModel",
    "GetWallUploadServerResponse",
    "GroupsGroupFull",
    "MarketAlbumUploadResponse",
    "MarketAlbumUploadResponseModel",
    "MarketUploadResponse",
    "MarketUploadResponseModel",
    "MessageUploadResponse",
    "MessageUploadResponseModel",
    "OwnerCoverUploadResponse",
    "OwnerCoverUploadResponseModel",
    "OwnerUploadResponse",
    "OwnerUploadResponseModel",
    "PhotoUploadResponse",
    "PhotoUploadResponseModel",
    "PhotosPhoto",
    "PhotosPhotoAlbumFull",
    "PhotosPhotoFullXtrRealOffset",
    "PhotosPhotoTag",
    "PhotosPhotoUpload",
    "PhotosPhotoXtrRealOffset",
    "PhotosPhotoXtrTagInfo",
    "PutTagResponse",
    "RestoreCommentResponse",
    "SaveMarketAlbumPhotoResponse",
    "SaveMarketPhotoResponse",
    "SaveMessagesPhotoResponse",
    "SaveOwnerCoverPhotoResponse",
    "SaveOwnerCoverPhotoResponseModel",
    "SaveOwnerPhotoResponse",
    "SaveOwnerPhotoResponseModel",
    "SaveResponse",
    "SaveWallPhotoResponse",
    "SearchResponse",
    "SearchResponseModel",
    "UsersUserFull",
    "WallUploadResponse",
    "WallUploadResponseModel",
    "WallWallComment",
)
