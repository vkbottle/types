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
    response: list[int] = Field()


class VideoCreateCommentResponse(BaseResponse):
    response: int = Field()


class VideoEditResponseModel(BaseModel):
    success: bool = Field()
    access_key: str | None = Field(
        default=None,
    )


class VideoEditResponse(BaseResponse):
    response: "VideoEditResponseModel" = Field()


class VideoGetAlbumByIdResponse(BaseResponse):
    response: "VideoVideoAlbumFull" = Field()


class VideoGetAlbumsByVideoExtendedResponseModel(BaseModel):
    count: int = Field()
    items: list["VideoVideoAlbumFull"] = Field()


class VideoGetAlbumsByVideoExtendedResponse(BaseResponse):
    response: "VideoGetAlbumsByVideoExtendedResponseModel" = Field()


class VideoGetAlbumsByVideoResponse(BaseResponse):
    response: list[int] = Field()


class VideoGetAlbumsExtendedResponseModel(BaseModel):
    count: int = Field()
    items: list["VideoVideoAlbumFull"] = Field()


class VideoGetAlbumsExtendedResponse(BaseResponse):
    response: "VideoGetAlbumsExtendedResponseModel" = Field()


class VideoGetAlbumsResponseModel(BaseModel):
    count: int = Field()
    items: list["VideoVideoAlbum"] = Field()


class VideoGetAlbumsResponse(BaseResponse):
    response: "VideoGetAlbumsResponseModel" = Field()


class VideoGetCommentsExtendedResponseModel(BaseModel):
    count: int = Field()
    items: list["WallWallComment"] = Field()
    profiles: list["UsersUserFull"] = Field()
    groups: list["GroupsGroupFull"] = Field()
    current_level_count: int | None = Field(
        default=None,
    )
    can_post: bool | None = Field(
        default=None,
    )
    show_reply_button: bool | None = Field(
        default=None,
    )
    groups_can_post: bool | None = Field(
        default=None,
    )
    real_offset: int | None = Field(
        default=None,
    )


class VideoGetCommentsExtendedResponse(BaseResponse):
    response: "VideoGetCommentsExtendedResponseModel" = Field()


class VideoGetCommentsResponseModel(BaseModel):
    count: int = Field()
    items: list["WallWallComment"] = Field()
    current_level_count: int | None = Field(
        default=None,
    )
    can_post: bool | None = Field(
        default=None,
    )
    show_reply_button: bool | None = Field(
        default=None,
    )
    groups_can_post: bool | None = Field(
        default=None,
    )
    real_offset: int | None = Field(
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
    title: str | None = Field(
        default=None,
    )
    author_name: str | None = Field(
        default=None,
    )
    width: int | None = Field(
        default=None,
    )
    height: int | None = Field(
        default=None,
    )
    provider_name: str | None = Field(
        default=None,
    )
    provider_url: str | None = Field(
        default=None,
    )
    thumbnail_url: str | None = Field(
        default=None,
    )
    thumbnail_width: int | None = Field(
        default=None,
    )
    thumbnail_height: int | None = Field(
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
    items: list["VideoVideoFull"] = Field()
    profiles: list["UsersUserFull"] | None = Field(
        default=None,
    )
    groups: list["GroupsGroupFull"] | None = Field(
        default=None,
    )
    max_attached_short_videos: int | None = Field(
        default=None,
    )


class VideoGetResponse(BaseResponse):
    response: "VideoGetResponseModel" = Field()


class VideoLiveGetCategoriesResponse(BaseResponse):
    response: list["VideoLiveCategory"] = Field()


class VideoSaveUploadedThumbResponseModel(BaseModel):
    photo_id: int = Field()
    photo_hash: str = Field()
    image: list["VideoVideoImage"] | None = Field(
        default=None,
    )
    photo_owner_id: int | None = Field(
        default=None,
    )


class VideoSaveUploadedThumbResponse(BaseResponse):
    response: "VideoSaveUploadedThumbResponseModel" = Field()


class VideoSaveResponse(BaseResponse):
    response: "VideoSaveResult" = Field()


class VideoSearchExtendedResponseModel(BaseModel):
    count: int = Field()
    items: list["VideoVideoFull"] = Field()
    profiles: list["UsersUser"] = Field()
    groups: list["GroupsGroupFull"] = Field()


class VideoSearchExtendedResponse(BaseResponse):
    response: "VideoSearchExtendedResponseModel" = Field()


class VideoSearchResponseModel(BaseModel):
    count: int = Field()
    items: list["VideoVideoFull"] = Field()


class VideoSearchResponse(BaseResponse):
    response: "VideoSearchResponseModel" = Field()


class VideoStartStreamingResponseModel(BaseModel):
    owner_id: int = Field()
    video_id: int = Field()
    name: str = Field()
    description: str = Field()
    access_key: str = Field()
    stream: "VideoStreamInputParams" = Field()
    post_id: int | None = Field(
        default=None,
    )


class VideoStartStreamingResponse(BaseResponse):
    response: "VideoStartStreamingResponseModel" = Field()


class VideoStopStreamingResponseModel(BaseModel):
    unique_viewers: int | None = Field(
        default=None,
    )


class VideoStopStreamingResponse(BaseResponse):
    response: "VideoStopStreamingResponseModel" = Field()


class VideoUploadResponseModel(BaseModel):
    size: int | None = Field(
        default=None,
    )
    video_id: int | None = Field(
        default=None,
    )


class VideoUploadResponse(BaseResponse):
    response: "VideoUploadResponseModel" = Field()


__all__ = (
    "VideoAddAlbumResponse",
    "VideoAddAlbumResponseModel",
    "VideoChangeVideoAlbumsResponse",
    "VideoCreateCommentResponse",
    "VideoEditResponse",
    "VideoEditResponseModel",
    "VideoGetAlbumByIdResponse",
    "VideoGetAlbumsByVideoExtendedResponse",
    "VideoGetAlbumsByVideoExtendedResponseModel",
    "VideoGetAlbumsByVideoResponse",
    "VideoGetAlbumsExtendedResponse",
    "VideoGetAlbumsExtendedResponseModel",
    "VideoGetAlbumsResponse",
    "VideoGetAlbumsResponseModel",
    "VideoGetCommentsExtendedResponse",
    "VideoGetCommentsExtendedResponseModel",
    "VideoGetCommentsResponse",
    "VideoGetCommentsResponseModel",
    "VideoGetLongPollServerResponse",
    "VideoGetLongPollServerResponseModel",
    "VideoGetOembedResponse",
    "VideoGetOembedResponseModel",
    "VideoGetResponse",
    "VideoGetResponseModel",
    "VideoGetThumbUploadUrlResponse",
    "VideoGetThumbUploadUrlResponseModel",
    "VideoLiveGetCategoriesResponse",
    "VideoSaveResponse",
    "VideoSaveUploadedThumbResponse",
    "VideoSaveUploadedThumbResponseModel",
    "VideoSearchExtendedResponse",
    "VideoSearchExtendedResponseModel",
    "VideoSearchResponse",
    "VideoSearchResponseModel",
    "VideoStartStreamingResponse",
    "VideoStartStreamingResponseModel",
    "VideoStopStreamingResponse",
    "VideoStopStreamingResponseModel",
    "VideoUploadResponse",
    "VideoUploadResponseModel",
)
