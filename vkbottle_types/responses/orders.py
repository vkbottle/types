import typing
from typing import Optional

from vkbottle_types.objects import orders, base
from .base_response import BaseResponse


class CancelSubscriptionResponse(BaseResponse):
    response: Optional[typing.List["base.BoolInt"]] = None


class ChangeStateResponse(BaseResponse):
    response: Optional[str] = None


class GetAmountResponse(BaseResponse):
    response: Optional[typing.List["orders.Amount"]] = None


class GetByIdResponse(BaseResponse):
    response: Optional[typing.List["orders.Order"]] = None


class GetUserSubscriptionByIdResponse(BaseResponse):
    response: Optional[typing.List["orders.Subscription"]] = None


class GetUserSubscriptionsResponse(BaseResponse):
    response: Optional["GetUserSubscriptionsResponseModel"] = None


class GetResponse(BaseResponse):
    response: Optional[typing.List["orders.Order"]] = None


class UpdateSubscriptionResponse(BaseResponse):
    response: Optional[typing.List["base.BoolInt"]] = None


class GetUserSubscriptionsResponseModel(BaseResponse):
    count: Optional[int] = None
    items: Optional[typing.List["orders.Subscription"]] = None
