import typing

from vkbottle_types.objects import (
    BaseBoolInt,
    OrdersAmount,
    OrdersOrder,
    OrdersSubscription,
)
from vkbottle_types.responses.base_response import BaseResponse


class CancelSubscriptionResponse(BaseResponse):
    response: BaseBoolInt


class ChangeStateResponse(BaseResponse):
    response: str


class GetAmountResponse(BaseResponse):
    response: typing.List["OrdersAmount"]


class GetByIdResponse(BaseResponse):
    response: typing.List["OrdersOrder"]


class GetUserSubscriptionByIdResponse(BaseResponse):
    response: OrdersSubscription


class GetUserSubscriptionsResponse(BaseResponse):
    response: "GetUserSubscriptionsResponseModel"


class GetResponse(BaseResponse):
    response: typing.List["OrdersOrder"]


class UpdateSubscriptionResponse(BaseResponse):
    response: BaseBoolInt


class GetUserSubscriptionsResponseModel(BaseResponse):
    count: typing.Optional[int] = None
    items: typing.Optional[typing.List["OrdersSubscription"]] = None


__all__ = (
    "BaseBoolInt",
    "CancelSubscriptionResponse",
    "ChangeStateResponse",
    "GetAmountResponse",
    "GetByIdResponse",
    "GetResponse",
    "GetUserSubscriptionByIdResponse",
    "GetUserSubscriptionsResponse",
    "GetUserSubscriptionsResponseModel",
    "OrdersAmount",
    "OrdersOrder",
    "OrdersSubscription",
    "UpdateSubscriptionResponse",
)
