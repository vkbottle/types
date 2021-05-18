import inspect
import typing

from vkbottle_types.objects import (
    BaseBoolInt,
    OrdersAmount,
    OrdersOrder,
    OrdersSubscription,
)

from .base_response import BaseResponse


class CancelSubscriptionResponse(BaseResponse):
    response: typing.Optional["CancelSubscriptionResponseModel"] = None


class ChangeStateResponse(BaseResponse):
    response: typing.Optional["ChangeStateResponseModel"] = None


class GetAmountResponse(BaseResponse):
    response: typing.Optional["GetAmountResponseModel"] = None


class GetByIdResponse(BaseResponse):
    response: typing.Optional["GetByIdResponseModel"] = None


class GetUserSubscriptionByIdResponse(BaseResponse):
    response: typing.Optional["GetUserSubscriptionByIdResponseModel"] = None


class GetUserSubscriptionsResponse(BaseResponse):
    response: typing.Optional["GetUserSubscriptionsResponseModel"] = None


class GetResponse(BaseResponse):
    response: typing.Optional["GetResponseModel"] = None


class UpdateSubscriptionResponse(BaseResponse):
    response: typing.Optional["UpdateSubscriptionResponseModel"] = None


CancelSubscriptionResponseModel = BaseBoolInt


ChangeStateResponseModel = str


GetAmountResponseModel = OrdersAmount


GetByIdResponseModel = typing.List[OrdersOrder]


GetUserSubscriptionByIdResponseModel = OrdersSubscription


class GetUserSubscriptionsResponseModel(BaseResponse):
    count: typing.Optional[int] = None
    items: typing.Optional[typing.List["OrdersSubscription"]] = None


GetResponseModel = typing.List[OrdersOrder]


UpdateSubscriptionResponseModel = BaseBoolInt


for item in locals().copy().values():
    if inspect.isclass(item) and issubclass(item, BaseResponse):
        item.update_forward_refs()
