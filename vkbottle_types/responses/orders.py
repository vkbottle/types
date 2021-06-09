import inspect
import typing
from .base_response import BaseResponse
from vkbottle_types.objects import BaseBoolInt, OrdersAmount, OrdersOrder, OrdersSubscription


class CancelSubscriptionResponse(BaseResponse):
    response: BaseBoolInt = None


class ChangeStateResponse(BaseResponse):
    response: str = None


class GetAmountResponse(BaseResponse):
    response: OrdersAmount = None


class GetByIdResponse(BaseResponse):
    response: typing.List["OrdersOrder"] = None


class GetUserSubscriptionByIdResponse(BaseResponse):
    response: OrdersSubscription = None


class GetUserSubscriptionsResponse(BaseResponse):
    response: "GetUserSubscriptionsResponseModel" = None


class GetResponse(BaseResponse):
    response: typing.List["OrdersOrder"] = None


class UpdateSubscriptionResponse(BaseResponse):
    response: BaseBoolInt = None


class GetUserSubscriptionsResponseModel(BaseResponse):
    count: typing.Optional[int] = None
    items: typing.Optional[typing.List["OrdersSubscription"]] = None


for item in locals().copy().values():
    if inspect.isclass(item) and issubclass(item, BaseResponse):
        item.update_forward_refs()
