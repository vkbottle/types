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
    items: list["PhotosPhotoAlbumFull"] = Field()


class PhotosGetAlbumsResponse(BaseResponse):
    response: "PhotosGetAlbumsResponseModel" = Field()


class PhotosGetAllCommentsResponseModel(BaseModel):
    count: int = Field()
    items: list["WallWallComment"] = Field()


class PhotosGetAllCommentsResponse(BaseResponse):
    response: "PhotosGetAllCommentsResponseModel" = Field()


class PhotosGetAllResponseModel(BaseModel):
    count: int = Field()
    items: list["PhotosPhoto"] = Field()
    more: bool | None = Field(
        default=None,
    )


class PhotosGetAllResponse(BaseResponse):
    response: "PhotosGetAllResponseModel" = Field()


class PhotosGetByIdResponse(BaseResponse):
    response: list["PhotosPhoto"] = Field()


class PhotosGetCommentsExtendedResponseModel(BaseModel):
    count: int = Field()
    items: list["WallWallComment"] = Field()
    profiles: list["UsersUserFull"] = Field()
    groups: list["GroupsGroupFull"] = Field()
    real_offset: int | None = Field(
        default=None,
    )


class PhotosGetCommentsExtendedResponse(BaseResponse):
    response: "PhotosGetCommentsExtendedResponseModel" = Field()


class PhotosGetCommentsResponseModel(BaseModel):
    count: int = Field()
    items: list["WallWallComment"] = Field()
    real_offset: int | None = Field(
        default=None,
    )


class PhotosGetCommentsResponse(BaseResponse):
    response: "PhotosGetCommentsResponseModel" = Field()


class PhotosGetMessagesUploadServerResponse(BaseResponse):
    response: "PhotosPhotoUpload" = Field()


class PhotosGetNewTagsResponseModel(BaseModel):
    count: int = Field()
    items: list["PhotosPhotoXtrTagInfo"] = Field()


class PhotosGetNewTagsResponse(BaseResponse):
    response: "PhotosGetNewTagsResponseModel" = Field()


class PhotosGetTagsResponse(BaseResponse):
    response: list["PhotosPhotoTag"] = Field()


class PhotosGetUploadServerResponse(BaseResponse):
    response: "PhotosPhotoUpload" = Field()


class PhotosGetUserPhotosResponseModel(BaseModel):
    count: int = Field()
    items: list["PhotosPhoto"] = Field()
    next_from: str | None = Field(
        default=None,
    )


class PhotosGetUserPhotosResponse(BaseResponse):
    response: "PhotosGetUserPhotosResponseModel" = Field()


class PhotosGetWallUploadServerResponse(BaseResponse):
    response: "PhotosPhotoUpload" = Field()


class PhotosGetResponseModel(BaseModel):
    count: int = Field()
    items: list["PhotosPhoto"] = Field()
    next_from: str | None = Field(
        default=None,
    )


class PhotosGetResponse(BaseResponse):
    response: "PhotosGetResponseModel" = Field()


class PhotosMarketAlbumUploadResponseModel(BaseModel):
    gid: int | None = Field(
        default=None,
    )
    hash: str | None = Field(
        default=None,
    )
    photo: str | None = Field(
        default=None,
    )
    server: int | None = Field(
        default=None,
    )


class PhotosMarketAlbumUploadResponse(BaseResponse):
    response: "PhotosMarketAlbumUploadResponseModel" = Field()


class PhotosMarketUploadResponseModel(BaseModel):
    crop_data: str | None = Field(
        default=None,
    )
    crop_hash: str | None = Field(
        default=None,
    )
    group_id: int | None = Field(
        default=None,
    )
    hash: str | None = Field(
        default=None,
    )
    photo: str | None = Field(
        default=None,
    )
    server: int | None = Field(
        default=None,
    )


class PhotosMarketUploadResponse(BaseResponse):
    response: "PhotosMarketUploadResponseModel" = Field()


class PhotosMessageUploadResponseModel(BaseModel):
    hash: str | None = Field(
        default=None,
    )
    photo: str | None = Field(
        default=None,
    )
    server: int | None = Field(
        default=None,
    )


class PhotosMessageUploadResponse(BaseResponse):
    response: "PhotosMessageUploadResponseModel" = Field()


class PhotosOwnerCoverUploadResponseModel(BaseModel):
    hash: str | None = Field(
        default=None,
    )
    photo: str | None = Field(
        default=None,
    )


class PhotosOwnerCoverUploadResponse(BaseResponse):
    response: "PhotosOwnerCoverUploadResponseModel" = Field()


class PhotosOwnerUploadResponseModel(BaseModel):
    hash: str | None = Field(
        default=None,
    )
    photo: str | None = Field(
        default=None,
    )
    server: int | None = Field(
        default=None,
    )


class PhotosOwnerUploadResponse(BaseResponse):
    response: "PhotosOwnerUploadResponseModel" = Field()


class PhotosPhotoUploadResponseModel(BaseModel):
    aid: int | None = Field(
        default=None,
    )
    hash: str | None = Field(
        default=None,
    )
    photo: str | None = Field(
        default=None,
    )
    photos_list: str | None = Field(
        default=None,
    )
    server: int | None = Field(
        default=None,
    )


class PhotosPhotoUploadResponse(BaseResponse):
    response: "PhotosPhotoUploadResponseModel" = Field()


class PhotosPutTagResponse(BaseResponse):
    response: int = Field()


class PhotosSaveMarketAlbumPhotoResponse(BaseResponse):
    response: list["PhotosPhoto"] = Field()


class PhotosSaveMessagesPhotoResponse(BaseResponse):
    response: list["PhotosPhoto"] = Field()


class PhotosSaveOwnerCoverPhotoResponseModel(BaseModel):
    images: list["BaseImage"] | None = Field(
        default=None,
    )


class PhotosSaveOwnerCoverPhotoResponse(BaseResponse):
    response: "PhotosSaveOwnerCoverPhotoResponseModel" = Field()


class PhotosSaveOwnerPhotoResponseModel(BaseModel):
    photo_hash: str = Field()
    photo_src: str = Field()
    photo_src_big: str | None = Field(
        default=None,
    )
    photo_src_small: str | None = Field(
        default=None,
    )
    saved: int | None = Field(
        default=None,
    )
    post_id: int | None = Field(
        default=None,
    )


class PhotosSaveOwnerPhotoResponse(BaseResponse):
    response: "PhotosSaveOwnerPhotoResponseModel" = Field()


class PhotosSaveWallPhotoResponse(BaseResponse):
    response: list["PhotosPhoto"] = Field()


class PhotosSaveResponse(BaseResponse):
    response: list["PhotosPhoto"] = Field()


class PhotosSearchResponseModel(BaseModel):
    count: int = Field()
    items: list["PhotosPhoto"] = Field()


class PhotosSearchResponse(BaseResponse):
    response: "PhotosSearchResponseModel" = Field()


class PhotosWallUploadResponseModel(BaseModel):
    hash: str | None = Field(
        default=None,
    )
    photo: str | None = Field(
        default=None,
    )
    server: int | None = Field(
        default=None,
    )


class PhotosWallUploadResponse(BaseResponse):
    response: "PhotosWallUploadResponseModel" = Field()


__all__ = (
    "PhotosCopyResponse",
    "PhotosCreateAlbumResponse",
    "PhotosCreateCommentResponse",
    "PhotosGetAlbumsCountResponse",
    "PhotosGetAlbumsResponse",
    "PhotosGetAlbumsResponseModel",
    "PhotosGetAllCommentsResponse",
    "PhotosGetAllCommentsResponseModel",
    "PhotosGetAllResponse",
    "PhotosGetAllResponseModel",
    "PhotosGetByIdResponse",
    "PhotosGetCommentsExtendedResponse",
    "PhotosGetCommentsExtendedResponseModel",
    "PhotosGetCommentsResponse",
    "PhotosGetCommentsResponseModel",
    "PhotosGetMessagesUploadServerResponse",
    "PhotosGetNewTagsResponse",
    "PhotosGetNewTagsResponseModel",
    "PhotosGetResponse",
    "PhotosGetResponseModel",
    "PhotosGetTagsResponse",
    "PhotosGetUploadServerResponse",
    "PhotosGetUserPhotosResponse",
    "PhotosGetUserPhotosResponseModel",
    "PhotosGetWallUploadServerResponse",
    "PhotosMarketAlbumUploadResponse",
    "PhotosMarketAlbumUploadResponseModel",
    "PhotosMarketUploadResponse",
    "PhotosMarketUploadResponseModel",
    "PhotosMessageUploadResponse",
    "PhotosMessageUploadResponseModel",
    "PhotosOwnerCoverUploadResponse",
    "PhotosOwnerCoverUploadResponseModel",
    "PhotosOwnerUploadResponse",
    "PhotosOwnerUploadResponseModel",
    "PhotosPhotoUploadResponse",
    "PhotosPhotoUploadResponseModel",
    "PhotosPutTagResponse",
    "PhotosSaveMarketAlbumPhotoResponse",
    "PhotosSaveMessagesPhotoResponse",
    "PhotosSaveOwnerCoverPhotoResponse",
    "PhotosSaveOwnerCoverPhotoResponseModel",
    "PhotosSaveOwnerPhotoResponse",
    "PhotosSaveOwnerPhotoResponseModel",
    "PhotosSaveResponse",
    "PhotosSaveWallPhotoResponse",
    "PhotosSearchResponse",
    "PhotosSearchResponseModel",
    "PhotosWallUploadResponse",
    "PhotosWallUploadResponseModel",
)
