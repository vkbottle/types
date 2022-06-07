import typing

from vkbottle_types.objects import StatsPeriod, StatsWallpostStat
from vkbottle_types.responses.base_response import BaseResponse


class GetPostReachResponse(BaseResponse):
    response: typing.List["StatsWallpostStat"]


class GetResponse(BaseResponse):
    response: typing.List["StatsPeriod"]


__all__ = (
    "GetPostReachResponse",
    "GetResponse",
    "StatsPeriod",
    "StatsWallpostStat",
)
