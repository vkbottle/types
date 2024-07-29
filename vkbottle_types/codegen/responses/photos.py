import typing

from vkbottle_types.base_model import Field
from vkbottle_types.objects import (
    BaseUploadServer,
    PhotosPhoto,
    PhotosPhotoAlbumFull,
    PhotosPhotoTag,
    PhotosPhotoUpload,
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


class PhotosGetAlbumsResponse(BaseResponse):
    response: typing.Dict[str, typing.Any] = Field()


class PhotosGetAllCommentsResponse(BaseResponse):
    response: typing.Dict[str, typing.Any] = Field()


class PhotosGetAllResponse(BaseResponse):
    response: typing.Dict[str, typing.Any] = Field()


class PhotosGetByIdResponse(BaseResponse):
    response: typing.List[PhotosPhoto] = Field()


class PhotosGetCommentsExtendedResponse(BaseResponse):
    response: typing.Dict[str, typing.Any] = Field()


class PhotosGetCommentsResponse(BaseResponse):
    response: typing.Dict[str, typing.Any] = Field()


class PhotosGetMarketUploadServerResponse(BaseResponse):
    response: "BaseUploadServer" = Field()


class PhotosGetMessagesUploadServerResponse(BaseResponse):
    response: "PhotosPhotoUpload" = Field()


class PhotosGetNewTagsResponse(BaseResponse):
    response: typing.Dict[str, typing.Any] = Field()


class PhotosGetTagsResponse(BaseResponse):
    response: typing.List[PhotosPhotoTag] = Field()


class PhotosGetUploadServerResponse(BaseResponse):
    response: "PhotosPhotoUpload" = Field()


class PhotosGetUserPhotosResponse(BaseResponse):
    response: typing.Dict[str, typing.Any] = Field()


class PhotosGetWallUploadServerResponse(BaseResponse):
    response: "PhotosPhotoUpload" = Field()


class PhotosGetResponse(BaseResponse):
    response: typing.Dict[str, typing.Any] = Field()


class PhotosMarketAlbumUploadResponse(BaseResponse):
    response: typing.Dict[str, typing.Any] = Field()


class PhotosMarketUploadResponse(BaseResponse):
    response: typing.Dict[str, typing.Any] = Field()


class PhotosMessageUploadResponse(BaseResponse):
    response: typing.Dict[str, typing.Any] = Field()


class PhotosOwnerCoverUploadResponse(BaseResponse):
    response: typing.Dict[str, typing.Any] = Field()


class PhotosOwnerUploadResponse(BaseResponse):
    response: typing.Dict[str, typing.Any] = Field()


class PhotosPhotoUploadResponse(BaseResponse):
    response: typing.Dict[str, typing.Any] = Field()


class PhotosPutTagResponse(BaseResponse):
    response: int = Field()


class PhotosSaveMarketAlbumPhotoResponse(BaseResponse):
    response: typing.List[PhotosPhoto] = Field()


class PhotosSaveMarketPhotoResponse(BaseResponse):
    response: typing.List[PhotosPhoto] = Field()


class PhotosSaveMessagesPhotoResponse(BaseResponse):
    response: typing.List[PhotosPhoto] = Field()


class PhotosSaveOwnerCoverPhotoResponse(BaseResponse):
    response: typing.Dict[str, typing.Any] = Field()


class PhotosSaveOwnerPhotoResponse(BaseResponse):
    response: typing.Dict[str, typing.Any] = Field()


class PhotosSaveWallPhotoResponse(BaseResponse):
    response: typing.List[PhotosPhoto] = Field()


class PhotosSaveResponse(BaseResponse):
    response: typing.List[PhotosPhoto] = Field()


class PhotosSearchResponse(BaseResponse):
    response: typing.Dict[str, typing.Any] = Field()


class PhotosWallUploadResponse(BaseResponse):
    response: typing.Dict[str, typing.Any] = Field()
