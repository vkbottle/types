import typing
from typing import Optional

from vkbottle_types.objects import leads
from .base_response import BaseResponse


class CheckUserResponse(BaseResponse):
    response: Optional[typing.List["leads.Checked"]] = None


class CompleteResponse(BaseResponse):
    response: Optional[typing.List["leads.Complete"]] = None


class GetStatsResponse(BaseResponse):
    response: Optional[typing.List["leads.Lead"]] = None


class GetUsersResponse(BaseResponse):
    response: Optional[typing.List["leads.Entry"]] = None


class MetricHitResponse(BaseResponse):
    response: Optional["MetricHitResponseModel"] = None


class StartResponse(BaseResponse):
    response: Optional[typing.List["leads.Start"]] = None


class MetricHitResponseModel(BaseResponse):
    result: Optional[bool] = None
    redirect_link: Optional[str] = None
