import inspect
import typing
from .base_response import BaseResponse
from vkbottle_types.objects import (
    BaseBoolInt,
    OrdersAmount,
    OrdersOrder,
    OrdersSubscription,
)


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


for item in locals().copy().values():
    if inspect.isclass(item) and issubclass(item, BaseResponse):
        item.update_forward_refs()
