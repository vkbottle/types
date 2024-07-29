import typing

from vkbottle_types.base_model import Field
from vkbottle_types.objects import StoriesStoryStats
from vkbottle_types.responses.base_response import BaseResponse


class StoriesGetBannedExtendedResponse(BaseResponse):
    response: typing.Dict[str, typing.Any] = Field()


class StoriesGetBannedResponse(BaseResponse):
    response: typing.Dict[str, typing.Any] = Field()


class StoriesGetByIdExtendedResponse(BaseResponse):
    response: typing.Dict[str, typing.Any] = Field()


class StoriesGetPhotoUploadServerResponse(BaseResponse):
    response: typing.Dict[str, typing.Any] = Field()


class StoriesGetStatsV5200Response(BaseResponse):
    response: typing.Dict[str, typing.Any] = Field()


class StoriesGetStatsResponse(BaseResponse):
    response: "StoriesStoryStats" = Field()


class StoriesGetVideoUploadServerResponse(BaseResponse):
    response: typing.Dict[str, typing.Any] = Field()


class StoriesGetViewersExtendedV5115Response(BaseResponse):
    response: typing.Dict[str, typing.Any] = Field()


class StoriesGetV5113Response(BaseResponse):
    response: typing.Dict[str, typing.Any] = Field()


class StoriesSaveResponse(BaseResponse):
    response: typing.Dict[str, typing.Any] = Field()


class StoriesUploadResponse(BaseResponse):
    response: typing.Dict[str, typing.Any] = Field()
