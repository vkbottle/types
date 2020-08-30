from typing import Optional, List

from vkbottle_types.objects import (
    LeadsChecked,
    LeadsComplete,
    LeadsStart,
    LeadsLead,
    LeadsEntry,
)
from .base_response import BaseResponse


class CheckUserResponse(BaseResponse):
    response: Optional["CheckUserResponseModel"] = None


class CompleteResponse(BaseResponse):
    response: Optional["CompleteResponseModel"] = None


class GetStatsResponse(BaseResponse):
    response: Optional["GetStatsResponseModel"] = None


class GetUsersResponse(BaseResponse):
    response: Optional["GetUsersResponseModel"] = None


class MetricHitResponse(BaseResponse):
    response: Optional["MetricHitResponseModel"] = None


class StartResponse(BaseResponse):
    response: Optional["StartResponseModel"] = None

CheckUserResponseModel = Optional[LeadsChecked]

CompleteResponseModel = Optional[LeadsComplete]

GetStatsResponseModel = Optional[LeadsLead]

GetUsersResponseModel = List[LeadsEntry]


class MetricHitResponseModel(BaseResponse):
    result: Optional[bool] = None
    redirect_link: Optional[str] = None


StartResponseModel = Optional[LeadsStart]

CheckUserResponse.update_forward_refs()
CompleteResponse.update_forward_refs()
GetStatsResponse.update_forward_refs()
GetUsersResponse.update_forward_refs()
MetricHitResponse.update_forward_refs()
StartResponse.update_forward_refs()
