import typing

from vkbottle_types.base_model import Field
from vkbottle_types.objects import VideoLiveCategory, VideoSaveResult, VideoVideoAlbumFull
from vkbottle_types.responses.base_response import BaseResponse


class VideoAddAlbumResponse(BaseResponse):
    response: typing.Dict[str, typing.Any] = Field()


class VideoChangeVideoAlbumsResponse(BaseResponse):
    response: typing.List[int] = Field()


class VideoCreateCommentResponse(BaseResponse):
    response: int = Field()


class VideoEditResponse(BaseResponse):
    response: typing.Dict[str, typing.Any] = Field()


class VideoGetAlbumByIdResponse(BaseResponse):
    response: "VideoVideoAlbumFull" = Field()


class VideoGetAlbumsByVideoExtendedResponse(BaseResponse):
    response: typing.Dict[str, typing.Any] = Field()


class VideoGetAlbumsByVideoResponse(BaseResponse):
    response: typing.List[int] = Field()


class VideoGetAlbumsExtendedResponse(BaseResponse):
    response: typing.Dict[str, typing.Any] = Field()


class VideoGetAlbumsResponse(BaseResponse):
    response: typing.Dict[str, typing.Any] = Field()


class VideoGetCommentsExtendedResponse(BaseResponse):
    response: typing.Dict[str, typing.Any] = Field()


class VideoGetCommentsResponse(BaseResponse):
    response: typing.Dict[str, typing.Any] = Field()


class VideoGetLongPollServerResponse(BaseResponse):
    response: typing.Dict[str, typing.Any] = Field()


class VideoGetResponse(BaseResponse):
    response: typing.Dict[str, typing.Any] = Field()


class VideoLiveGetCategoriesResponse(BaseResponse):
    response: typing.List[VideoLiveCategory] = Field()


class VideoSaveResponse(BaseResponse):
    response: "VideoSaveResult" = Field()


class VideoSearchExtendedResponse(BaseResponse):
    response: typing.Dict[str, typing.Any] = Field()


class VideoSearchResponse(BaseResponse):
    response: typing.Dict[str, typing.Any] = Field()


class VideoStartStreamingResponse(BaseResponse):
    response: typing.Dict[str, typing.Any] = Field()


class VideoStopStreamingResponse(BaseResponse):
    response: typing.Dict[str, typing.Any] = Field()


class VideoUploadResponse(BaseResponse):
    response: typing.Dict[str, typing.Any] = Field()
