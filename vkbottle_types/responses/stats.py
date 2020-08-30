from typing import Optional, List

from vkbottle_types.objects import StatsWallpostStat, StatsPeriod
from .base_response import BaseResponse


class GetPostReachResponse(BaseResponse):
    response: Optional["GetPostReachResponseModel"] = None


class GetResponse(BaseResponse):
    response: Optional["GetResponseModel"] = None


GetPostReachResponseModel = List[StatsWallpostStat]

GetResponseModel = List[StatsPeriod]

GetPostReachResponse.update_forward_refs()
GetResponse.update_forward_refs()
