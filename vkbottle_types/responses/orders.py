from .base_response import BaseResponse
from vkbottle_types.objects import orders, base
from typing import Optional, Any, List, Union
import typing


class CancelSubscriptionResponse(BaseResponse):
    response: Optional["CancelSubscriptionResponseModel"] = None


class ChangeStateResponse(BaseResponse):
    response: Optional["ChangeStateResponseModel"] = None


class GetAmountResponse(BaseResponse):
    response: Optional["GetAmountResponseModel"] = None


class GetByIdResponse(BaseResponse):
    response: Optional["GetByIdResponseModel"] = None


class GetUserSubscriptionByIdResponse(BaseResponse):
    response: Optional["GetUserSubscriptionByIdResponseModel"] = None


class GetUserSubscriptionsResponse(BaseResponse):
    response: Optional["GetUserSubscriptionsResponseModel"] = None


class GetResponse(BaseResponse):
    response: Optional["GetResponseModel"] = None


class UpdateSubscriptionResponse(BaseResponse):
    response: Optional["UpdateSubscriptionResponseModel"] = None


CancelSubscriptionResponseModel = Optional["base.BoolInt"]


ChangeStateResponseModel = str


GetAmountResponseModel = Optional["orders.Amount"]


GetByIdResponseModel = List["orders.Order"]


GetUserSubscriptionByIdResponseModel = Optional["orders.Subscription"]


class GetUserSubscriptionsResponseModel(BaseResponse):
    count: Optional[int] = None
    items: Optional[List["orders.Subscription"]] = None


GetResponseModel = List["orders.Order"]


UpdateSubscriptionResponseModel = Optional["base.BoolInt"]
