import typing
from vkbottle_types.responses.base_response import BaseResponse, BaseModel
from vkbottle_types.base_model import Field


class DonutDonatorSubscriptionInfoResponseModel(BaseModel):
    owner_id: int = Field()

    next_payment_date: int = Field()

    amount: int = Field()

    status: typing.Literal["active", "expiring"] = Field()


class DonutDonatorSubscriptionInfoResponse(BaseResponse):
    response: "DonutDonatorSubscriptionInfoResponseModel"
