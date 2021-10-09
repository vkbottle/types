import inspect
import typing
from .base_response import BaseResponse
from vkbottle_types.objects import (
    BaseBoolInt,
    BaseImage,
    BaseUploadServer,
    GroupsGroupFull,
    PhotosPhoto,
    PhotosPhotoAlbumFull,
    PhotosPhotoFull,
    PhotosPhotoFullXtrRealOffset,
    PhotosPhotoTag,
    PhotosPhotoUpload,
    PhotosPhotoXtrRealOffset,
    PhotosPhotoXtrTagInfo,
    UsersUserFull,
    WallWallComment
)


class CopyResponse(BaseResponse):
    response: int = None


class CreateAlbumResponse(BaseResponse):
    response: PhotosPhotoAlbumFull = None


class CreateCommentResponse(BaseResponse):
    response: int = None


class DeleteCommentResponse(BaseResponse):
    response: BaseBoolInt = None


class GetAlbumsCountResponse(BaseResponse):
    response: int = None


class GetAlbumsResponse(BaseResponse):
    response: "GetAlbumsResponseModel" = None


class GetAllCommentsResponse(BaseResponse):
    response: "GetAllCommentsResponseModel" = None


class GetAllExtendedResponse(BaseResponse):
    response: "GetAllExtendedResponseModel" = None


class GetAllResponse(BaseResponse):
    response: "GetAllResponseModel" = None


class GetByIdExtendedResponse(BaseResponse):
    response: "GetByIdExtendedResponseModel" = None


class GetByIdLegacyExtendedResponse(BaseResponse):
    response: typing.List["PhotosPhotoFull"] = None


class GetByIdLegacyResponse(BaseResponse):
    response: typing.List["PhotosPhoto"] = None


class GetByIdResponse(BaseResponse):
    response: "GetByIdResponseModel" = None


class GetCommentsExtendedResponse(BaseResponse):
    response: "GetCommentsExtendedResponseModel" = None


class GetCommentsResponse(BaseResponse):
    response: "GetCommentsResponseModel" = None


class GetMarketUploadServerResponse(BaseResponse):
    response: BaseUploadServer = None


class GetMessagesUploadServerResponse(BaseResponse):
    response: PhotosPhotoUpload = None


class GetNewTagsResponse(BaseResponse):
    response: "GetNewTagsResponseModel" = None


class GetTagsResponse(BaseResponse):
    response: typing.List["PhotosPhotoTag"] = None


class GetUploadServerResponse(BaseResponse):
    response: PhotosPhotoUpload = None


class GetUserPhotosExtendedResponse(BaseResponse):
    response: "GetUserPhotosExtendedResponseModel" = None


class GetUserPhotosResponse(BaseResponse):
    response: "GetUserPhotosResponseModel" = None


class GetWallUploadServerResponse(BaseResponse):
    response: PhotosPhotoUpload = None


class GetExtendedResponse(BaseResponse):
    response: "GetExtendedResponseModel" = None


class GetResponse(BaseResponse):
    response: "GetResponseModel" = None


class MarketAlbumUploadResponse(BaseResponse):
    response: "MarketAlbumUploadResponseModel" = None


class MarketUploadResponse(BaseResponse):
    response: "MarketUploadResponseModel" = None


class MessageUploadResponse(BaseResponse):
    response: "MessageUploadResponseModel" = None


class OwnerCoverUploadResponse(BaseResponse):
    response: "OwnerCoverUploadResponseModel" = None


class OwnerUploadResponse(BaseResponse):
    response: "OwnerUploadResponseModel" = None


class PhotoUploadResponse(BaseResponse):
    response: "PhotoUploadResponseModel" = None


class PutTagResponse(BaseResponse):
    response: int = None


class RestoreCommentResponse(BaseResponse):
    response: BaseBoolInt = None


class SaveMarketAlbumPhotoResponse(BaseResponse):
    response: typing.List["PhotosPhoto"] = None


class SaveMarketPhotoResponse(BaseResponse):
    response: typing.List["PhotosPhoto"] = None


class SaveMessagesPhotoResponse(BaseResponse):
    response: typing.List["PhotosPhoto"] = None


class SaveOwnerCoverPhotoResponse(BaseResponse):
    response: "SaveOwnerCoverPhotoResponseModel" = None


class SaveOwnerPhotoResponse(BaseResponse):
    response: "SaveOwnerPhotoResponseModel" = None


class SaveWallPhotoResponse(BaseResponse):
    response: typing.List["PhotosPhoto"] = None


class SaveResponse(BaseResponse):
    response: typing.List["PhotosPhoto"] = None


class SearchResponse(BaseResponse):
    response: "SearchResponseModel" = None


class WallUploadResponse(BaseResponse):
    response: "WallUploadResponseModel" = None


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


class GetByIdExtendedResponseModel(BaseResponse):
    items: typing.Optional[typing.List["PhotosPhotoFull"]] = None


class GetByIdResponseModel(BaseResponse):
    items: typing.Optional[typing.List["PhotosPhoto"]] = None


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


class GetUserPhotosExtendedResponseModel(BaseResponse):
    count: typing.Optional[int] = None
    items: typing.Optional[typing.List["PhotosPhotoFull"]] = None


class GetUserPhotosResponseModel(BaseResponse):
    count: typing.Optional[int] = None
    items: typing.Optional[typing.List["PhotosPhoto"]] = None


class GetExtendedResponseModel(BaseResponse):
    count: typing.Optional[int] = None
    items: typing.Optional[typing.List["PhotosPhotoFull"]] = None


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


for item in locals().copy().values():
    if inspect.isclass(item) and issubclass(item, BaseResponse):
        item.update_forward_refs()
