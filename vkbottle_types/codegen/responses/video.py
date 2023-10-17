import typing
import enum
from vkbottle_types.responses.base_response import BaseResponse, BaseModel
from vkbottle_types.base_model import Field

from vkbottle_types.objects import (
    BasePropertyExists,
    BaseLikes,
    BaseRepostsInfo,
    BaseBoolInt,
    VideoLiveSettings,
    VideoVideoImage,
    VideoLiveCategory,
    VideoVideoFiles,
    VideoEpisode,
)


class VideoEpisodeResponseModel(BaseModel):
    time: typing.Optional[int] = Field(
        default=None,
        description="Seconds from start of the video",
    )

    text: typing.Optional[str] = Field(
        default=None,
        description="Description of episode",
    )


class VideoEpisodeResponse(BaseResponse):
    response: "VideoEpisodeResponseModel"


class VideoLiveCategoryResponseModel(BaseModel):
    id: int = Field()

    label: str = Field()

    sublist: typing.Optional[typing.List[VideoLiveCategory]] = Field(
        default=None,
    )


class VideoLiveCategoryResponse(BaseResponse):
    response: "VideoLiveCategoryResponseModel"


class VideoLiveInfoResponseModel(BaseModel):
    enabled: bool = Field()

    is_notifications_blocked: typing.Optional[bool] = Field(
        default=None,
    )


class VideoLiveInfoResponse(BaseResponse):
    response: "VideoLiveInfoResponseModel"


class VideoLiveSettingsResponseModel(BaseModel):
    can_rewind: typing.Optional[bool] = Field(
        default=None,
        description="If user car rewind live or not",
    )

    is_endless: typing.Optional[bool] = Field(
        default=None,
        description="If live is endless or not",
    )

    max_duration: typing.Optional[int] = Field(
        default=None,
        description="Max possible time for rewind",
    )

    is_clips_live: typing.Optional[bool] = Field(
        default=None,
        description="If live in clips apps",
    )


class VideoLiveSettingsResponse(BaseResponse):
    response: "VideoLiveSettingsResponseModel"


class VideoSaveResultResponseModel(BaseModel):
    access_key: typing.Optional[str] = Field(
        default=None,
        description="Video access key",
    )

    description: typing.Optional[str] = Field(
        default=None,
        description="Video description",
    )

    owner_id: typing.Optional[int] = Field(
        default=None,
        description="Video owner ID",
    )

    title: typing.Optional[str] = Field(
        default=None,
        description="Video title",
    )

    upload_url: typing.Optional[str] = Field(
        default=None,
        description="URL for the video uploading",
    )

    video_id: typing.Optional[int] = Field(
        default=None,
        description="Video ID",
    )


class VideoSaveResultResponse(BaseResponse):
    response: "VideoSaveResultResponseModel"


class VideoStreamInputParamsResponseModel(BaseModel):
    url: typing.Optional[str] = Field(
        default=None,
    )

    key: typing.Optional[str] = Field(
        default=None,
    )

    okmp_url: typing.Optional[str] = Field(
        default=None,
    )

    webrtc_url: typing.Optional[str] = Field(
        default=None,
    )


class VideoStreamInputParamsResponse(BaseResponse):
    response: "VideoStreamInputParamsResponseModel"


class VideoVideoResponseModel(BaseModel):
    response_type: typing.Optional[typing.Literal["min", "full"]] = Field(
        default=None,
    )

    access_key: typing.Optional[str] = Field(
        default=None,
        description="Video access key",
    )

    adding_date: typing.Optional[int] = Field(
        default=None,
        description="Date when the video has been added in Unixtime",
    )

    can_comment: typing.Optional[bool] = Field(
        default=None,
        description="Information whether current user can comment the video",
    )

    can_edit: typing.Optional[bool] = Field(
        default=None,
        description="Information whether current user can edit the video",
    )

    can_delete: typing.Optional[bool] = Field(
        default=None,
        description="Information whether current user can delete the video",
    )

    can_like: typing.Optional[bool] = Field(
        default=None,
        description="Information whether current user can like the video",
    )

    can_repost: typing.Optional[int] = Field(
        default=None,
        description="Information whether current user can repost the video",
    )

    can_subscribe: typing.Optional[bool] = Field(
        default=None,
        description="Information whether current user can subscribe to author of the video",
    )

    can_add_to_faves: typing.Optional[bool] = Field(
        default=None,
        description="Information whether current user can add the video to favourites",
    )

    can_add: typing.Optional[bool] = Field(
        default=None,
        description="Information whether current user can add the video",
    )

    can_attach_link: typing.Optional[bool] = Field(
        default=None,
        description="Information whether current user can attach action button to the video",
    )

    can_edit_privacy: typing.Optional[bool] = Field(
        default=None,
        description="Information whether current user can edit the video privacy",
    )

    is_private: typing.Optional[bool] = Field(
        default=None,
        description="1 if video is private",
    )

    comments: typing.Optional[int] = Field(
        default=None,
        description="Number of comments",
    )

    date: typing.Optional[int] = Field(
        default=None,
        description="Date when video has been uploaded in Unixtime",
    )

    description: typing.Optional[str] = Field(
        default=None,
        description="Video description",
    )

    duration: typing.Optional[int] = Field(
        default=None,
        description="Video duration in seconds",
    )

    image: typing.Optional[typing.List[VideoVideoImage]] = Field(
        default=None,
    )

    first_frame: typing.Optional[typing.List[VideoVideoImage]] = Field(
        default=None,
    )

    width: typing.Optional[int] = Field(
        default=None,
        description="Video width",
    )

    height: typing.Optional[int] = Field(
        default=None,
        description="Video height",
    )

    id: typing.Optional[int] = Field(
        default=None,
        description="Video ID",
    )

    owner_id: typing.Optional[int] = Field(
        default=None,
        description="Video owner ID",
    )

    user_id: typing.Optional[int] = Field(
        default=None,
        description="Id of the user who uploaded the video if it was uploaded to a group by member",
    )

    title: typing.Optional[str] = Field(
        default=None,
        description="Video title",
    )

    is_favorite: typing.Optional[bool] = Field(
        default=None,
        description="Whether video is added to bookmarks",
    )

    player: typing.Optional[str] = Field(
        default=None,
        description="Video embed URL",
    )

    processing: typing.Optional["BasePropertyExists"] = Field(
        default=None,
        description="Returns if the video is processing",
    )

    converting: typing.Optional[bool] = Field(
        default=None,
        description="1 if  video is being converted",
    )

    added: typing.Optional[bool] = Field(
        default=None,
        description="1 if video is added to user's albums",
    )

    is_subscribed: typing.Optional[bool] = Field(
        default=None,
        description="1 if user is subscribed to author of the video",
    )

    track_code: typing.Optional[str] = Field(
        default=None,
    )

    repeat: typing.Optional["BasePropertyExists"] = Field(
        default=None,
        description="Information whether the video is repeated",
    )

    type: typing.Optional[
        typing.Literal["video", "music_video", "movie", "live", "short_video"]
    ] = Field(
        default=None,
    )

    views: typing.Optional[int] = Field(
        default=None,
        description="Number of views",
    )

    local_views: typing.Optional[int] = Field(
        default=None,
        description="If video is external, number of views on vk",
    )

    content_restricted: typing.Optional[int] = Field(
        default=None,
        description="Restriction code",
    )

    content_restricted_message: typing.Optional[str] = Field(
        default=None,
        description="Restriction text",
    )

    balance: typing.Optional[int] = Field(
        default=None,
        description="Live donations balance",
    )

    live: typing.Optional["BasePropertyExists"] = Field(
        default=None,
        description="1 if the video is a live stream",
    )

    upcoming: typing.Optional["BasePropertyExists"] = Field(
        default=None,
        description="1 if the video is an upcoming stream",
    )

    live_start_time: typing.Optional[int] = Field(
        default=None,
        description="Date in Unixtime when the live stream is scheduled to start by the author",
    )

    live_notify: typing.Optional[bool] = Field(
        default=None,
        description="Whether current user is subscribed to the upcoming live stream notification (if not subscribed to the author)",
    )

    spectators: typing.Optional[int] = Field(
        default=None,
        description="Number of spectators of the stream",
    )

    platform: typing.Optional[str] = Field(
        default=None,
        description="External platform",
    )

    likes: typing.Optional["BaseLikes"] = Field(
        default=None,
    )

    reposts: typing.Optional["BaseRepostsInfo"] = Field(
        default=None,
    )


class VideoVideoResponse(BaseResponse):
    response: "VideoVideoResponseModel"


class VideoVideoAlbumResponseModel(BaseModel):
    id: int = Field(
        description="Album ID",
    )

    owner_id: int = Field(
        description="Album owner's ID",
    )

    title: str = Field(
        description="Album title",
    )

    track_code: typing.Optional[str] = Field(
        default=None,
        description="Album trackcode",
    )

    response_type: typing.Optional[typing.Literal["min", "full"]] = Field(
        default=None,
    )


class VideoVideoAlbumResponse(BaseResponse):
    response: "VideoVideoAlbumResponseModel"


class VideoVideoAlbumFullResponseModel(VideoVideoAlbum):
    count: int = Field(
        description="Total number of videos in album",
    )

    updated_time: int = Field(
        description="Date when the album has been updated last time in Unixtime",
    )

    image: typing.Optional[typing.List[VideoVideoImage]] = Field(
        default=None,
        description="Album cover image in different sizes",
    )

    image_blur: typing.Optional["BasePropertyExists"] = Field(
        default=None,
        description="Need blur album thumb or not",
    )

    is_system: typing.Optional["BasePropertyExists"] = Field(
        default=None,
        description="Information whether album is system",
    )

    can_edit: typing.Optional[bool] = Field(
        default=None,
        description="Is user can edit playlist",
    )

    can_delete: typing.Optional[bool] = Field(
        default=None,
        description="Is user can delete playlist",
    )

    can_upload: typing.Optional[bool] = Field(
        default=None,
        description="Is user can upload video to playlist",
    )


class VideoVideoAlbumFullResponse(BaseResponse):
    response: "VideoVideoAlbumFullResponseModel"


class VideoVideoFilesResponseModel(BaseModel):
    external: typing.Optional[str] = Field(
        default=None,
        description="URL of the external player",
    )

    mp4_144: typing.Optional[str] = Field(
        default=None,
        description="URL of the mpeg4 file with 144p quality",
    )

    mp4_240: typing.Optional[str] = Field(
        default=None,
        description="URL of the mpeg4 file with 240p quality",
    )

    mp4_360: typing.Optional[str] = Field(
        default=None,
        description="URL of the mpeg4 file with 360p quality",
    )

    mp4_480: typing.Optional[str] = Field(
        default=None,
        description="URL of the mpeg4 file with 480p quality",
    )

    mp4_720: typing.Optional[str] = Field(
        default=None,
        description="URL of the mpeg4 file with 720p quality",
    )

    mp4_1080: typing.Optional[str] = Field(
        default=None,
        description="URL of the mpeg4 file with 1080p quality",
    )

    mp4_1440: typing.Optional[str] = Field(
        default=None,
        description="URL of the mpeg4 file with 2K quality",
    )

    mp4_2160: typing.Optional[str] = Field(
        default=None,
        description="URL of the mpeg4 file with 4K quality",
    )

    flv_320: typing.Optional[str] = Field(
        default=None,
        description="URL of the flv file with 320p quality",
    )


class VideoVideoFilesResponse(BaseResponse):
    response: "VideoVideoFilesResponseModel"


class VideoVideoFullResponseModel(VideoVideo):
    files: typing.Optional["VideoVideoFiles"] = Field(
        default=None,
    )

    trailer: typing.Optional["VideoVideoFiles"] = Field(
        default=None,
    )

    episodes: typing.Optional[typing.List[VideoEpisode]] = Field(
        default=None,
        description="List of video episodes with timecodes",
    )

    live_settings: typing.Optional["VideoLiveSettings"] = Field(
        default=None,
        description="Settings for live stream",
    )


class VideoVideoFullResponse(BaseResponse):
    response: "VideoVideoFullResponseModel"


class VideoVideoImageResponseModel(BaseImage):
    with_padding: typing.Optional["BasePropertyExists"] = Field(
        default=None,
    )


class VideoVideoImageResponse(BaseResponse):
    response: "VideoVideoImageResponseModel"
