from .base_response import BaseResponse
from vkbottle_types.objects import stats
from typing import Optional, Any, List, Union
import typing


class GetPostReachResponse(BaseResponse):
    response: Optional["GetPostReachResponseModel"] = None


class GetResponse(BaseResponse):
    response: Optional["GetResponseModel"] = None


GetPostReachResponseModel = List["stats.WallpostStat"]


GetResponseModel = List["stats.Period"]
