import typing

from vkbottle_types.base_model import Field
from vkbottle_types.objects import StatsPeriod, StatsWallpostStat
from vkbottle_types.responses.base_response import BaseResponse


class StatsGetPostReachResponse(BaseResponse):
    response: typing.List["StatsWallpostStat"] = Field()


class StatsGetResponse(BaseResponse):
    response: typing.List["StatsPeriod"] = Field()
