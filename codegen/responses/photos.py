import typing

from vkbottle_types.base_model import BaseModel, Field
from vkbottle_types.objects import (
    BaseImage,
    GroupsGroupFull,
    PhotosPhoto,
    PhotosPhotoAlbumFull,
    PhotosPhotoTag,
    PhotosPhotoUpload,
    PhotosPhotoXtrTagInfo,
    UsersUserFull,
    WallWallComment,
)
from vkbottle_types.responses.base_response import BaseResponse


class PhotosCopyResponse(BaseResponse):
    response: int = Field()


class PhotosCreateAlbumResponse(BaseResponse):
    response: "PhotosPhotoAlbumFull" = Field()


class PhotosCreateCommentResponse(BaseResponse):
    response: int = Field()


class PhotosGetAlbumsCountResponse(BaseResponse):
    response: int = Field()


class PhotosGetAlbumsResponseModel(BaseModel):
    count: int = Field()
    items: typing.List["PhotosPhotoAlbumFull"] = Field()


class PhotosGetAlbumsResponse(BaseResponse):
    response: "PhotosGetAlbumsResponseModel" = Field()


class PhotosGetAllCommentsResponseModel(BaseModel):
    count: int = Field()
    items: typing.List["WallWallComment"] = Field()


class PhotosGetAllCommentsResponse(BaseResponse):
    response: "PhotosGetAllCommentsResponseModel" = Field()


class PhotosGetAllResponseModel(BaseModel):
    count: int = Field()
    items: typing.List["PhotosPhoto"] = Field()
    more: typing.Optional[bool] = Field(
        default=None,
    )


class PhotosGetAllResponse(BaseResponse):
    response: "PhotosGetAllResponseModel" = Field()


class PhotosGetByIdResponse(BaseResponse):
    response: typing.List["PhotosPhoto"] = Field()


class PhotosGetCommentsExtendedResponseModel(BaseModel):
    count: int = Field()
    items: typing.List["WallWallComment"] = Field()
    profiles: typing.List["UsersUserFull"] = Field()
    groups: typing.List["GroupsGroupFull"] = Field()
    real_offset: typing.Optional[int] = Field(
        default=None,
    )


class PhotosGetCommentsExtendedResponse(BaseResponse):
    response: "PhotosGetCommentsExtendedResponseModel" = Field()


class PhotosGetCommentsResponseModel(BaseModel):
    count: int = Field()
    items: typing.List["WallWallComment"] = Field()
    real_offset: typing.Optional[int] = Field(
        default=None,
    )


class PhotosGetCommentsResponse(BaseResponse):
    response: "PhotosGetCommentsResponseModel" = Field()


class PhotosGetMessagesUploadServerResponse(BaseResponse):
    response: "PhotosPhotoUpload" = Field()


class PhotosGetNewTagsResponseModel(BaseModel):
    count: int = Field()
    items: typing.List["PhotosPhotoXtrTagInfo"] = Field()


class PhotosGetNewTagsResponse(BaseResponse):
    response: "PhotosGetNewTagsResponseModel" = Field()


class PhotosGetTagsResponse(BaseResponse):
    response: typing.List["PhotosPhotoTag"] = Field()


class PhotosGetUploadServerResponse(BaseResponse):
    response: "PhotosPhotoUpload" = Field()


class PhotosGetUserPhotosResponseModel(BaseModel):
    count: int = Field()
    items: typing.List["PhotosPhoto"] = Field()
    next_from: typing.Optional[str] = Field(
        default=None,
    )


class PhotosGetUserPhotosResponse(BaseResponse):
    response: "PhotosGetUserPhotosResponseModel" = Field()


class PhotosGetWallUploadServerResponse(BaseResponse):
    response: "PhotosPhotoUpload" = Field()


class PhotosGetResponseModel(BaseModel):
    count: int = Field()
    items: typing.List["PhotosPhoto"] = Field()
    next_from: typing.Optional[str] = Field(
        default=None,
    )


class PhotosGetResponse(BaseResponse):
    response: "PhotosGetResponseModel" = Field()


class PhotosMarketAlbumUploadResponseModel(BaseModel):
    gid: typing.Optional[int] = Field(
        default=None,
    )
    hash: typing.Optional[str] = Field(
        default=None,
    )
    photo: typing.Optional[str] = Field(
        default=None,
    )
    server: typing.Optional[int] = Field(
        default=None,
    )


class PhotosMarketAlbumUploadResponse(BaseResponse):
    response: "PhotosMarketAlbumUploadResponseModel" = Field()


class PhotosMarketUploadResponseModel(BaseModel):
    crop_data: typing.Optional[str] = Field(
        default=None,
    )
    crop_hash: typing.Optional[str] = Field(
        default=None,
    )
    group_id: typing.Optional[int] = Field(
        default=None,
    )
    hash: typing.Optional[str] = Field(
        default=None,
    )
    photo: typing.Optional[str] = Field(
        default=None,
    )
    server: typing.Optional[int] = Field(
        default=None,
    )


class PhotosMarketUploadResponse(BaseResponse):
    response: "PhotosMarketUploadResponseModel" = Field()


class PhotosMessageUploadResponseModel(BaseModel):
    hash: typing.Optional[str] = Field(
        default=None,
    )
    photo: typing.Optional[str] = Field(
        default=None,
    )
    server: typing.Optional[int] = Field(
        default=None,
    )


class PhotosMessageUploadResponse(BaseResponse):
    response: "PhotosMessageUploadResponseModel" = Field()


class PhotosOwnerCoverUploadResponseModel(BaseModel):
    hash: typing.Optional[str] = Field(
        default=None,
    )
    photo: typing.Optional[str] = Field(
        default=None,
    )


class PhotosOwnerCoverUploadResponse(BaseResponse):
    response: "PhotosOwnerCoverUploadResponseModel" = Field()


class PhotosOwnerUploadResponseModel(BaseModel):
    hash: typing.Optional[str] = Field(
        default=None,
    )
    photo: typing.Optional[str] = Field(
        default=None,
    )
    server: typing.Optional[int] = Field(
        default=None,
    )


class PhotosOwnerUploadResponse(BaseResponse):
    response: "PhotosOwnerUploadResponseModel" = Field()


class PhotosPhotoUploadResponseModel(BaseModel):
    aid: typing.Optional[int] = Field(
        default=None,
    )
    hash: typing.Optional[str] = Field(
        default=None,
    )
    photo: typing.Optional[str] = Field(
        default=None,
    )
    photos_list: typing.Optional[str] = Field(
        default=None,
    )
    server: typing.Optional[int] = Field(
        default=None,
    )


class PhotosPhotoUploadResponse(BaseResponse):
    response: "PhotosPhotoUploadResponseModel" = Field()


class PhotosPutTagResponse(BaseResponse):
    response: int = Field()


class PhotosSaveMarketAlbumPhotoResponse(BaseResponse):
    response: typing.List["PhotosPhoto"] = Field()


class PhotosSaveMessagesPhotoResponse(BaseResponse):
    response: typing.List["PhotosPhoto"] = Field()


class PhotosSaveOwnerCoverPhotoResponseModel(BaseModel):
    images: typing.Optional[typing.List["BaseImage"]] = Field(
        default=None,
    )


class PhotosSaveOwnerCoverPhotoResponse(BaseResponse):
    response: "PhotosSaveOwnerCoverPhotoResponseModel" = Field()


class PhotosSaveOwnerPhotoResponseModel(BaseModel):
    photo_hash: str = Field()
    photo_src: str = Field()
    photo_src_big: typing.Optional[str] = Field(
        default=None,
    )
    photo_src_small: typing.Optional[str] = Field(
        default=None,
    )
    saved: typing.Optional[int] = Field(
        default=None,
    )
    post_id: typing.Optional[int] = Field(
        default=None,
    )


class PhotosSaveOwnerPhotoResponse(BaseResponse):
    response: "PhotosSaveOwnerPhotoResponseModel" = Field()


class PhotosSaveWallPhotoResponse(BaseResponse):
    response: typing.List["PhotosPhoto"] = Field()


class PhotosSaveResponse(BaseResponse):
    response: typing.List["PhotosPhoto"] = Field()


class PhotosSearchResponseModel(BaseModel):
    count: int = Field()
    items: typing.List["PhotosPhoto"] = Field()


class PhotosSearchResponse(BaseResponse):
    response: "PhotosSearchResponseModel" = Field()


class PhotosWallUploadResponseModel(BaseModel):
    hash: typing.Optional[str] = Field(
        default=None,
    )
    photo: typing.Optional[str] = Field(
        default=None,
    )
    server: typing.Optional[int] = Field(
        default=None,
    )


class PhotosWallUploadResponse(BaseResponse):
    response: "PhotosWallUploadResponseModel" = Field()
