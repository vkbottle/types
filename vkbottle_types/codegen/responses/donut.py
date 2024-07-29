import typing

from vkbottle_types.base_model import Field
from vkbottle_types.objects import DonutDonatorSubscriptionInfo
from vkbottle_types.responses.base_response import BaseResponse


class DonutGetSubscriptionResponse(BaseResponse):
    response: "DonutDonatorSubscriptionInfo" = Field()


class DonutGetSubscriptionsResponse(BaseResponse):
    response: typing.Dict[str, typing.Any] = Field()
