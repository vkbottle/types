import typing
from typing import Optional

from vkbottle_types.objects import stats
from .base_response import BaseResponse


class GetPostReachResponse(BaseResponse):
    response: Optional[typing.List["stats.WallpostStat"]] = None


class GetResponse(BaseResponse):
    response: Optional[typing.List["stats.Period"]] = None
