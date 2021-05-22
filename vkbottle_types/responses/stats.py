import inspect
import typing
from .base_response import BaseResponse
from vkbottle_types.objects import StatsPeriod, StatsWallpostStat


class GetPostReachResponse(BaseResponse):
    response: typing.Optional["GetPostReachResponseModel"] = None


class GetResponse(BaseResponse):
    response: typing.Optional["GetResponseModel"] = None


GetPostReachResponseModel = typing.List[StatsWallpostStat]


GetResponseModel = typing.List[StatsPeriod]


for item in locals().copy().values():
    if inspect.isclass(item) and issubclass(item, BaseResponse):
        item.update_forward_refs()
