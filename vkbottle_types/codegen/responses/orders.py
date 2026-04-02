from vkbottle_types.base_model import BaseModel, Field
from vkbottle_types.objects import OrdersAmount, OrdersOrder, OrdersSubscription
from vkbottle_types.responses.base_response import BaseResponse


class OrdersChangeStateResponse(BaseResponse):
    response: str = Field()


class OrdersGetAmountResponse(BaseResponse):
    response: list["OrdersAmount"] = Field()


class OrdersGetByIdResponse(BaseResponse):
    response: list["OrdersOrder"] = Field()


class OrdersGetUserSubscriptionByIdResponse(BaseResponse):
    response: "OrdersSubscription" = Field()


class OrdersGetUserSubscriptionsResponseModel(BaseModel):
    count: int = Field()
    items: list["OrdersSubscription"] = Field()


class OrdersGetUserSubscriptionsResponse(BaseResponse):
    response: "OrdersGetUserSubscriptionsResponseModel" = Field()


class OrdersGetResponse(BaseResponse):
    response: list["OrdersOrder"] = Field()


__all__ = (
    "OrdersChangeStateResponse",
    "OrdersGetAmountResponse",
    "OrdersGetByIdResponse",
    "OrdersGetResponse",
    "OrdersGetUserSubscriptionByIdResponse",
    "OrdersGetUserSubscriptionsResponse",
    "OrdersGetUserSubscriptionsResponseModel",
)
