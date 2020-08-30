from typing import Optional, List

from vkbottle_types.objects import (
    PhotosPhotoTag,
    PhotosPhotoXtrTagInfo,
    GroupsGroupFull,
    PhotosCommentXtrPid,
    PhotosPhotoXtrRealOffset,
    WallWallComment,
    PhotosPhotoUpload,
    PhotosPhoto,
    PhotosPhotoFullXtrRealOffset,
    UsersUserFull,
    PhotosPhotoAlbumFull,
    PhotosPhotoFull,
    BaseBoolInt,
    BaseImage,
    BaseUploadServer,
)
from .base_response import BaseResponse


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

CreateAlbumResponseModel = Optional[PhotosPhotoAlbumFull]

CreateCommentResponseModel = int

DeleteCommentResponseModel = Optional[BaseBoolInt]


GetAlbumsCountResponseModel = int


class GetAlbumsResponseModel(BaseResponse):
    count: Optional[int] = None
    items: Optional[List["PhotosPhotoAlbumFull"]] = None


class GetAllCommentsResponseModel(BaseResponse):
    count: Optional[int] = None
    items: Optional[List["PhotosCommentXtrPid"]] = None


class GetAllExtendedResponseModel(BaseResponse):
    count: Optional[int] = None
    items: Optional[List["PhotosPhotoFullXtrRealOffset"]] = None
    more: Optional["BaseBoolInt"] = None


class GetAllResponseModel(BaseResponse):
    count: Optional[int] = None
    items: Optional[List["PhotosPhotoXtrRealOffset"]] = None
    more: Optional["BaseBoolInt"] = None


GetByIdExtendedResponseModel = List[PhotosPhotoFull]

GetByIdResponseModel = List[PhotosPhoto]


class GetCommentsExtendedResponseModel(BaseResponse):
    count: Optional[int] = None
    real_offset: Optional[int] = None
    items: Optional[List["WallWallComment"]] = None
    profiles: Optional[List["UsersUserFull"]] = None
    groups: Optional[List["GroupsGroupFull"]] = None


class GetCommentsResponseModel(BaseResponse):
    count: Optional[int] = None
    real_offset: Optional[int] = None
    items: Optional[List["WallWallComment"]] = None


GetMarketUploadServerResponseModel = Optional[BaseUploadServer]

GetMessagesUploadServerResponseModel = Optional[PhotosPhotoUpload]


class GetNewTagsResponseModel(BaseResponse):
    count: Optional[int] = None
    items: Optional[List["PhotosPhotoXtrTagInfo"]] = None


GetTagsResponseModel = List[PhotosPhotoTag]

GetUploadServerResponseModel = Optional[PhotosPhotoUpload]


class GetUserPhotosExtendedResponseModel(BaseResponse):
    count: Optional[int] = None
    items: Optional[List["PhotosPhotoFull"]] = None


class GetUserPhotosResponseModel(BaseResponse):
    count: Optional[int] = None
    items: Optional[List["PhotosPhoto"]] = None


GetWallUploadServerResponseModel = Optional[PhotosPhotoUpload]


class GetExtendedResponseModel(BaseResponse):
    count: Optional[int] = None
    items: Optional[List["PhotosPhotoFull"]] = None


class GetResponseModel(BaseResponse):
    count: Optional[int] = None
    items: Optional[List["PhotosPhoto"]] = None


PutTagResponseModel = int

RestoreCommentResponseModel = Optional[BaseBoolInt]

SaveMarketAlbumPhotoResponseModel = List[PhotosPhoto]

SaveMarketPhotoResponseModel = List[PhotosPhoto]

SaveMessagesPhotoResponseModel = List[PhotosPhoto]

SaveOwnerCoverPhotoResponseModel = List[BaseImage]


class SaveOwnerPhotoResponseModel(BaseResponse):
    photo_hash: Optional[str] = None
    photo_src: Optional[str] = None
    photo_src_big: Optional[str] = None
    photo_src_small: Optional[str] = None
    saved: Optional[int] = None
    post_id: Optional[int] = None


SaveWallPhotoResponseModel = List[PhotosPhoto]

SaveResponseModel = List[PhotosPhoto]


class SearchResponseModel(BaseResponse):
    count: Optional[int] = None
    items: Optional[List["PhotosPhoto"]] = None


CopyResponse.update_forward_refs()
CreateAlbumResponse.update_forward_refs()
CreateCommentResponse.update_forward_refs()
DeleteCommentResponse.update_forward_refs()
GetAlbumsCountResponse.update_forward_refs()
GetAlbumsResponse.update_forward_refs()
GetAllCommentsResponse.update_forward_refs()
GetAllExtendedResponse.update_forward_refs()
GetAllResponse.update_forward_refs()
GetByIdExtendedResponse.update_forward_refs()
GetByIdResponse.update_forward_refs()
GetCommentsExtendedResponse.update_forward_refs()
GetCommentsResponse.update_forward_refs()
GetMarketUploadServerResponse.update_forward_refs()
GetMessagesUploadServerResponse.update_forward_refs()
GetNewTagsResponse.update_forward_refs()
GetTagsResponse.update_forward_refs()
GetUploadServerResponse.update_forward_refs()
GetUserPhotosExtendedResponse.update_forward_refs()
GetUserPhotosResponse.update_forward_refs()
GetWallUploadServerResponse.update_forward_refs()
GetExtendedResponse.update_forward_refs()
GetResponse.update_forward_refs()
PutTagResponse.update_forward_refs()
RestoreCommentResponse.update_forward_refs()
SaveMarketAlbumPhotoResponse.update_forward_refs()
SaveMarketPhotoResponse.update_forward_refs()
SaveMessagesPhotoResponse.update_forward_refs()
SaveOwnerCoverPhotoResponse.update_forward_refs()
SaveOwnerPhotoResponse.update_forward_refs()
SaveWallPhotoResponse.update_forward_refs()
SaveResponse.update_forward_refs()
SearchResponse.update_forward_refs()
