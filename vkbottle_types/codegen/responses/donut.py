import typing

from vkbottle_types.base_model import BaseModel, Field
from vkbottle_types.objects import DonutDonatorSubscriptionInfo, GroupsGroupFull, UsersUserFull
from vkbottle_types.responses.base_response import BaseResponse


class DonutGetSubscriptionResponse(BaseResponse):
    response: "DonutDonatorSubscriptionInfo" = Field()


class DonutGetSubscriptionsResponseModel(BaseModel):
    subscriptions: typing.List["DonutDonatorSubscriptionInfo"] = Field()
    count: typing.Optional[int] = Field(
        default=None,
    )
    profiles: typing.Optional[typing.List["UsersUserFull"]] = Field(
        default=None,
    )
    groups: typing.Optional[typing.List["GroupsGroupFull"]] = Field(
        default=None,
    )


class DonutGetSubscriptionsResponse(BaseResponse):
    response: "DonutGetSubscriptionsResponseModel" = Field()
