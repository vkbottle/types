from typing import Optional, List

from vkbottle_types.objects import (
    OrdersAmount,
    OrdersOrder,
    OrdersSubscription,
    BaseBoolInt,
)
from .base_response import BaseResponse


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


CancelSubscriptionResponseModel = Optional[BaseBoolInt]

ChangeStateResponseModel = str

GetAmountResponseModel = Optional[OrdersAmount]

GetByIdResponseModel = List[OrdersOrder]

GetUserSubscriptionByIdResponseModel = Optional[OrdersSubscription]


class GetUserSubscriptionsResponseModel(BaseResponse):
    count: Optional[int] = None
    items: Optional[List["OrdersSubscription"]] = None


GetResponseModel = List[OrdersOrder]

UpdateSubscriptionResponseModel = Optional[BaseBoolInt]


CancelSubscriptionResponse.update_forward_refs()
ChangeStateResponse.update_forward_refs()
GetAmountResponse.update_forward_refs()
GetByIdResponse.update_forward_refs()
GetUserSubscriptionByIdResponse.update_forward_refs()
GetUserSubscriptionsResponse.update_forward_refs()
GetResponse.update_forward_refs()
UpdateSubscriptionResponse.update_forward_refs()
