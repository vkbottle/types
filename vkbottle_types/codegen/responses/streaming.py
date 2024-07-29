import typing

from vkbottle_types.base_model import Field
from vkbottle_types.objects import StreamingStats
from vkbottle_types.responses.base_response import BaseResponse


class StreamingGetServerUrlResponse(BaseResponse):
    response: typing.Dict[str, typing.Any] = Field()


class StreamingGetStatsResponse(BaseResponse):
    response: typing.List[StreamingStats] = Field()


class StreamingGetStemResponse(BaseResponse):
    response: typing.Dict[str, typing.Any] = Field()
