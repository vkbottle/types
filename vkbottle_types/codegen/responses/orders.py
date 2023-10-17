import typing
import enum
from vkbottle_types.responses.base_response import BaseResponse, BaseModel
from vkbottle_types.base_model import Field

from vkbottle_types.objects import OrdersAmountItem


class OrdersAmountResponseModel(BaseModel):
    amounts: typing.Optional[typing.List[OrdersAmountItem]] = Field(
        default=None,
    )

    currency: typing.Optional[str] = Field(
        default=None,
        description="Currency name",
    )


class OrdersAmountResponse(BaseResponse):
    response: "OrdersAmountResponseModel"


class OrdersAmountItemResponseModel(BaseModel):
    amount: typing.Optional[float] = Field(
        default=None,
        description="Votes amount in user's currency",
    )

    description: typing.Optional[str] = Field(
        default=None,
        description="Amount description",
    )

    votes: typing.Optional[str] = Field(
        default=None,
        description="Votes number",
    )


class OrdersAmountItemResponse(BaseResponse):
    response: "OrdersAmountItemResponseModel"


class OrdersOrderResponseModel(BaseModel):
    amount: str = Field(
        description="Amount",
    )

    app_order_id: str = Field(
        description="App order ID",
    )

    date: str = Field(
        description="Date of creation in Unixtime",
    )

    id: str = Field(
        description="Order ID",
    )

    item: str = Field(
        description="Order item",
    )

    receiver_id: str = Field(
        description="Receiver ID",
    )

    status: typing.Literal[
        "created", "charged", "refunded", "chargeable", "cancelled", "declined"
    ] = Field(
        description="Order status",
    )

    user_id: str = Field(
        description="User ID",
    )

    cancel_transaction_id: typing.Optional[str] = Field(
        default=None,
        description="Cancel transaction ID",
    )

    transaction_id: typing.Optional[str] = Field(
        default=None,
        description="Transaction ID",
    )


class OrdersOrderResponse(BaseResponse):
    response: "OrdersOrderResponseModel"


class OrdersSubscriptionResponseModel(BaseModel):
    create_time: int = Field(
        description="Date of creation in Unixtime",
    )

    id: int = Field(
        description="Subscription ID",
    )

    item_id: str = Field(
        description="Subscription order item",
    )

    period: int = Field(
        description="Subscription period",
    )

    period_start_time: int = Field(
        description="Date of last period start in Unixtime",
    )

    price: int = Field(
        description="Subscription price",
    )

    status: str = Field(
        description="Subscription status",
    )

    update_time: int = Field(
        description="Date of last change in Unixtime",
    )

    cancel_reason: typing.Optional[str] = Field(
        default=None,
        description="Cancel reason",
    )

    next_bill_time: typing.Optional[int] = Field(
        default=None,
        description="Date of next bill in Unixtime",
    )

    expire_time: typing.Optional[int] = Field(
        default=None,
        description="Subscription expiration time in Unixtime",
    )

    pending_cancel: typing.Optional[bool] = Field(
        default=None,
        description="Pending cancel state",
    )

    title: typing.Optional[str] = Field(
        default=None,
        description="Subscription name",
    )

    app_id: typing.Optional[int] = Field(
        default=None,
        description="Subscription's application id",
    )

    application_name: typing.Optional[str] = Field(
        default=None,
        description="Subscription's application name",
    )

    photo_url: typing.Optional[str] = Field(
        default=None,
        description="Item photo image url",
    )

    test_mode: typing.Optional[bool] = Field(
        default=None,
        description="Is test subscription",
    )

    trial_expire_time: typing.Optional[int] = Field(
        default=None,
        description="Date of trial expire in Unixtime",
    )

    is_game: typing.Optional[bool] = Field(
        default=None,
        description="Is game (not miniapp) subscription",
    )


class OrdersSubscriptionResponse(BaseResponse):
    response: "OrdersSubscriptionResponseModel"
