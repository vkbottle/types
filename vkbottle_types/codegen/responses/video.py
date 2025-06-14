import typing

from vkbottle_types.base_model import BaseModel, Field
from vkbottle_types.objects import (
    GroupsGroupFull,
    UsersUser,
    UsersUserFull,
    VideoLiveCategory,
    VideoSaveResult,
    VideoStreamInputParams,
    VideoVideoAlbum,
    VideoVideoAlbumFull,
    VideoVideoFull,
    VideoVideoImage,
    WallWallComment,
)
from vkbottle_types.responses.base_response import BaseResponse


class VideoAddAlbumResponseModel(BaseModel):
    album_id: int = Field()


class VideoAddAlbumResponse(BaseResponse):
    response: "VideoAddAlbumResponseModel" = Field()


class VideoChangeVideoAlbumsResponse(BaseResponse):
    response: typing.List[int] = Field()


class VideoCreateCommentResponse(BaseResponse):
    response: int = Field()


class VideoEditResponseModel(BaseModel):
    success: bool = Field()
    access_key: typing.Optional[str] = Field(
        default=None,
    )


class VideoEditResponse(BaseResponse):
    response: "VideoEditResponseModel" = Field()


class VideoGetAlbumByIdResponse(BaseResponse):
    response: "VideoVideoAlbumFull" = Field()


class VideoGetAlbumsByVideoExtendedResponseModel(BaseModel):
    count: int = Field()
    items: typing.List["VideoVideoAlbumFull"] = Field()


class VideoGetAlbumsByVideoExtendedResponse(BaseResponse):
    response: "VideoGetAlbumsByVideoExtendedResponseModel" = Field()


class VideoGetAlbumsByVideoResponse(BaseResponse):
    response: typing.List[int] = Field()


class VideoGetAlbumsExtendedResponseModel(BaseModel):
    count: int = Field()
    items: typing.List["VideoVideoAlbumFull"] = Field()


class VideoGetAlbumsExtendedResponse(BaseResponse):
    response: "VideoGetAlbumsExtendedResponseModel" = Field()


class VideoGetAlbumsResponseModel(BaseModel):
    count: int = Field()
    items: typing.List["VideoVideoAlbum"] = Field()


class VideoGetAlbumsResponse(BaseResponse):
    response: "VideoGetAlbumsResponseModel" = Field()


class VideoGetCommentsExtendedResponseModel(BaseModel):
    count: int = Field()
    items: typing.List["WallWallComment"] = Field()
    profiles: typing.List["UsersUserFull"] = Field()
    groups: typing.List["GroupsGroupFull"] = Field()
    current_level_count: typing.Optional[int] = Field(
        default=None,
    )
    can_post: typing.Optional[bool] = Field(
        default=None,
    )
    show_reply_button: typing.Optional[bool] = Field(
        default=None,
    )
    groups_can_post: typing.Optional[bool] = Field(
        default=None,
    )
    real_offset: typing.Optional[int] = Field(
        default=None,
    )


class VideoGetCommentsExtendedResponse(BaseResponse):
    response: "VideoGetCommentsExtendedResponseModel" = Field()


class VideoGetCommentsResponseModel(BaseModel):
    count: int = Field()
    items: typing.List["WallWallComment"] = Field()
    current_level_count: typing.Optional[int] = Field(
        default=None,
    )
    can_post: typing.Optional[bool] = Field(
        default=None,
    )
    show_reply_button: typing.Optional[bool] = Field(
        default=None,
    )
    groups_can_post: typing.Optional[bool] = Field(
        default=None,
    )
    real_offset: typing.Optional[int] = Field(
        default=None,
    )


class VideoGetCommentsResponse(BaseResponse):
    response: "VideoGetCommentsResponseModel" = Field()


class VideoGetLongPollServerResponseModel(BaseModel):
    url: str = Field()


class VideoGetLongPollServerResponse(BaseResponse):
    response: "VideoGetLongPollServerResponseModel" = Field()


class VideoGetOembedResponseModel(BaseModel):
    version: str = Field()
    type: str = Field()
    html: str = Field()
    title: typing.Optional[str] = Field(
        default=None,
    )
    author_name: typing.Optional[str] = Field(
        default=None,
    )
    width: typing.Optional[int] = Field(
        default=None,
    )
    height: typing.Optional[int] = Field(
        default=None,
    )
    provider_name: typing.Optional[str] = Field(
        default=None,
    )
    provider_url: typing.Optional[str] = Field(
        default=None,
    )
    thumbnail_url: typing.Optional[str] = Field(
        default=None,
    )
    thumbnail_width: typing.Optional[int] = Field(
        default=None,
    )
    thumbnail_height: typing.Optional[int] = Field(
        default=None,
    )


class VideoGetOembedResponse(BaseResponse):
    response: "VideoGetOembedResponseModel" = Field()


class VideoGetThumbUploadUrlResponseModel(BaseModel):
    upload_url: str = Field()


class VideoGetThumbUploadUrlResponse(BaseResponse):
    response: "VideoGetThumbUploadUrlResponseModel" = Field()


class VideoGetResponseModel(BaseModel):
    count: int = Field()
    items: typing.List["VideoVideoFull"] = Field()
    profiles: typing.Optional[typing.List["UsersUserFull"]] = Field(
        default=None,
    )
    groups: typing.Optional[typing.List["GroupsGroupFull"]] = Field(
        default=None,
    )
    max_attached_short_videos: typing.Optional[int] = Field(
        default=None,
    )


class VideoGetResponse(BaseResponse):
    response: "VideoGetResponseModel" = Field()


class VideoLiveGetCategoriesResponse(BaseResponse):
    response: typing.List["VideoLiveCategory"] = Field()


class VideoSaveUploadedThumbResponseModel(BaseModel):
    photo_id: int = Field()
    photo_hash: str = Field()
    image: typing.Optional[typing.List["VideoVideoImage"]] = Field(
        default=None,
    )
    photo_owner_id: typing.Optional[int] = Field(
        default=None,
    )


class VideoSaveUploadedThumbResponse(BaseResponse):
    response: "VideoSaveUploadedThumbResponseModel" = Field()


class VideoSaveResponse(BaseResponse):
    response: "VideoSaveResult" = Field()


class VideoSearchExtendedResponseModel(BaseModel):
    count: int = Field()
    items: typing.List["VideoVideoFull"] = Field()
    profiles: typing.List["UsersUser"] = Field()
    groups: typing.List["GroupsGroupFull"] = Field()


class VideoSearchExtendedResponse(BaseResponse):
    response: "VideoSearchExtendedResponseModel" = Field()


class VideoSearchResponseModel(BaseModel):
    count: int = Field()
    items: typing.List["VideoVideoFull"] = Field()


class VideoSearchResponse(BaseResponse):
    response: "VideoSearchResponseModel" = Field()


class VideoStartStreamingResponseModel(BaseModel):
    owner_id: int = Field()
    video_id: int = Field()
    name: str = Field()
    description: str = Field()
    access_key: str = Field()
    stream: "VideoStreamInputParams" = Field()
    post_id: typing.Optional[int] = Field(
        default=None,
    )


class VideoStartStreamingResponse(BaseResponse):
    response: "VideoStartStreamingResponseModel" = Field()


class VideoStopStreamingResponseModel(BaseModel):
    unique_viewers: typing.Optional[int] = Field(
        default=None,
    )


class VideoStopStreamingResponse(BaseResponse):
    response: "VideoStopStreamingResponseModel" = Field()


class VideoUploadResponseModel(BaseModel):
    size: typing.Optional[int] = Field(
        default=None,
    )
    video_id: typing.Optional[int] = Field(
        default=None,
    )


class VideoUploadResponse(BaseResponse):
    response: "VideoUploadResponseModel" = Field()
