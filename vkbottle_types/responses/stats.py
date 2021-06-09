import inspect
import typing
from .base_response import BaseResponse
from vkbottle_types.objects import StatsPeriod, StatsWallpostStat


class GetPostReachResponse(BaseResponse):
    response: typing.List["StatsWallpostStat"] = None


class GetResponse(BaseResponse):
    response: typing.List["StatsPeriod"] = None


for item in locals().copy().values():
    if inspect.isclass(item) and issubclass(item, BaseResponse):
        item.update_forward_refs()
