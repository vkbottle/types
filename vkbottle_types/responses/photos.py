import inspect
import typing
from .base_response import BaseResponse
from vkbottle_types.objects import (
    BaseBoolInt,
    BaseImage,
    BaseUploadServer,
    GroupsGroupFull,
    PhotosCommentXtrPid,
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
    response: typing.Optional["CopyResponseModel"] = None


class CreateAlbumResponse(BaseResponse):
    response: typing.Optional["CreateAlbumResponseModel"] = None


class CreateCommentResponse(BaseResponse):
    response: typing.Optional["CreateCommentResponseModel"] = None


class DeleteCommentResponse(BaseResponse):
    response: typing.Optional["DeleteCommentResponseModel"] = None


class GetAlbumsCountResponse(BaseResponse):
    response: typing.Optional["GetAlbumsCountResponseModel"] = None


class GetAlbumsResponse(BaseResponse):
    response: typing.Optional["GetAlbumsResponseModel"] = None


class GetAllCommentsResponse(BaseResponse):
    response: typing.Optional["GetAllCommentsResponseModel"] = None


class GetAllExtendedResponse(BaseResponse):
    response: typing.Optional["GetAllExtendedResponseModel"] = None


class GetAllResponse(BaseResponse):
    response: typing.Optional["GetAllResponseModel"] = None


class GetByIdExtendedResponse(BaseResponse):
    response: typing.Optional["GetByIdExtendedResponseModel"] = None


class GetByIdLegacyExtendedResponse(BaseResponse):
    response: typing.Optional["GetByIdLegacyExtendedResponseModel"] = None


class GetByIdLegacyResponse(BaseResponse):
    response: typing.Optional["GetByIdLegacyResponseModel"] = None


class GetByIdResponse(BaseResponse):
    response: typing.Optional["GetByIdResponseModel"] = None


class GetCommentsExtendedResponse(BaseResponse):
    response: typing.Optional["GetCommentsExtendedResponseModel"] = None


class GetCommentsResponse(BaseResponse):
    response: typing.Optional["GetCommentsResponseModel"] = None


class GetMarketUploadServerResponse(BaseResponse):
    response: typing.Optional["GetMarketUploadServerResponseModel"] = None


class GetMessagesUploadServerResponse(BaseResponse):
    response: typing.Optional["GetMessagesUploadServerResponseModel"] = None


class GetNewTagsResponse(BaseResponse):
    response: typing.Optional["GetNewTagsResponseModel"] = None


class GetTagsResponse(BaseResponse):
    response: typing.Optional["GetTagsResponseModel"] = None


class GetUploadServerResponse(BaseResponse):
    response: typing.Optional["GetUploadServerResponseModel"] = None


class GetUserPhotosExtendedResponse(BaseResponse):
    response: typing.Optional["GetUserPhotosExtendedResponseModel"] = None


class GetUserPhotosResponse(BaseResponse):
    response: typing.Optional["GetUserPhotosResponseModel"] = None


class GetWallUploadServerResponse(BaseResponse):
    response: typing.Optional["GetWallUploadServerResponseModel"] = None


class GetExtendedResponse(BaseResponse):
    response: typing.Optional["GetExtendedResponseModel"] = None


class GetResponse(BaseResponse):
    response: typing.Optional["GetResponseModel"] = None


class MarketAlbumUploadResponse(BaseResponse):
    response: typing.Optional["MarketAlbumUploadResponseModel"] = None


class MarketUploadResponse(BaseResponse):
    response: typing.Optional["MarketUploadResponseModel"] = None


class MessageUploadResponse(BaseResponse):
    response: typing.Optional["MessageUploadResponseModel"] = None


class OwnerCoverUploadResponse(BaseResponse):
    response: typing.Optional["OwnerCoverUploadResponseModel"] = None


class OwnerUploadResponse(BaseResponse):
    response: typing.Optional["OwnerUploadResponseModel"] = None


class PhotoUploadResponse(BaseResponse):
    response: typing.Optional["PhotoUploadResponseModel"] = None


class PutTagResponse(BaseResponse):
    response: typing.Optional["PutTagResponseModel"] = None


class RestoreCommentResponse(BaseResponse):
    response: typing.Optional["RestoreCommentResponseModel"] = None


class SaveMarketAlbumPhotoResponse(BaseResponse):
    response: typing.Optional["SaveMarketAlbumPhotoResponseModel"] = None


class SaveMarketPhotoResponse(BaseResponse):
    response: typing.Optional["SaveMarketPhotoResponseModel"] = None


class SaveMessagesPhotoResponse(BaseResponse):
    response: typing.Optional["SaveMessagesPhotoResponseModel"] = None


class SaveOwnerCoverPhotoResponse(BaseResponse):
    response: typing.Optional["SaveOwnerCoverPhotoResponseModel"] = None


class SaveOwnerPhotoResponse(BaseResponse):
    response: typing.Optional["SaveOwnerPhotoResponseModel"] = None


class SaveWallPhotoResponse(BaseResponse):
    response: typing.Optional["SaveWallPhotoResponseModel"] = None


class SaveResponse(BaseResponse):
    response: typing.Optional["SaveResponseModel"] = None


class SearchResponse(BaseResponse):
    response: typing.Optional["SearchResponseModel"] = None


class WallUploadResponse(BaseResponse):
    response: typing.Optional["WallUploadResponseModel"] = None


CopyResponseModel = int


CreateAlbumResponseModel = PhotosPhotoAlbumFull


CreateCommentResponseModel = int


DeleteCommentResponseModel = BaseBoolInt


GetAlbumsCountResponseModel = int


class GetAlbumsResponseModel(BaseResponse):
    count: typing.Optional[int] = None
    items: typing.Optional[typing.List["PhotosPhotoAlbumFull"]] = None


class GetAllCommentsResponseModel(BaseResponse):
    count: typing.Optional[int] = None
    items: typing.Optional[typing.List["PhotosCommentXtrPid"]] = None


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


GetByIdLegacyExtendedResponseModel = typing.List[PhotosPhotoFull]


GetByIdLegacyResponseModel = typing.List[PhotosPhoto]


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


GetMarketUploadServerResponseModel = BaseUploadServer


GetMessagesUploadServerResponseModel = PhotosPhotoUpload


class GetNewTagsResponseModel(BaseResponse):
    count: typing.Optional[int] = None
    items: typing.Optional[typing.List["PhotosPhotoXtrTagInfo"]] = None


GetTagsResponseModel = typing.List[PhotosPhotoTag]


GetUploadServerResponseModel = PhotosPhotoUpload


class GetUserPhotosExtendedResponseModel(BaseResponse):
    count: typing.Optional[int] = None
    items: typing.Optional[typing.List["PhotosPhotoFull"]] = None


class GetUserPhotosResponseModel(BaseResponse):
    count: typing.Optional[int] = None
    items: typing.Optional[typing.List["PhotosPhoto"]] = None


GetWallUploadServerResponseModel = PhotosPhotoUpload


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


PutTagResponseModel = int


RestoreCommentResponseModel = BaseBoolInt


SaveMarketAlbumPhotoResponseModel = typing.List[PhotosPhoto]


SaveMarketPhotoResponseModel = typing.List[PhotosPhoto]


SaveMessagesPhotoResponseModel = typing.List[PhotosPhoto]


SaveOwnerCoverPhotoResponseModel = typing.List[BaseImage]


class SaveOwnerPhotoResponseModel(BaseResponse):
    photo_hash: typing.Optional[str] = None
    photo_src: typing.Optional[str] = None
    photo_src_big: typing.Optional[str] = None
    photo_src_small: typing.Optional[str] = None
    saved: typing.Optional[int] = None
    post_id: typing.Optional[int] = None


SaveWallPhotoResponseModel = typing.List[PhotosPhoto]


SaveResponseModel = typing.List[PhotosPhoto]


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
