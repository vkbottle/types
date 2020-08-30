from .base_response import BaseResponse
from vkbottle_types.objects import leads
from typing import Optional, Any, List, Union
import typing


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


CheckUserResponseModel = Optional["leads.Checked"]


CompleteResponseModel = Optional["leads.Complete"]


GetStatsResponseModel = Optional["leads.Lead"]


GetUsersResponseModel = List["leads.Entry"]


class MetricHitResponseModel(BaseResponse):
    result: Optional[bool] = None
    redirect_link: Optional[str] = None


StartResponseModel = Optional["leads.Start"]
