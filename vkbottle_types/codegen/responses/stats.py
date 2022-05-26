import inspect
import typing

from vkbottle_types.objects import StatsPeriod, StatsWallpostStat

from .base_response import BaseResponse


class GetPostReachResponse(BaseResponse):
    response: typing.List["StatsWallpostStat"]


class GetResponse(BaseResponse):
    response: typing.List["StatsPeriod"]


for item in locals().copy().values():
    if inspect.isclass(item) and issubclass(item, BaseResponse):
        item.update_forward_refs()


__all__ = (
    "GetPostReachResponse",
    "GetResponse",
)
