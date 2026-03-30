from vkbottle_types.base_model import BaseModel, Field
from vkbottle_types.objects import DonutDonatorSubscriptionInfo, GroupsGroupFull, UsersUserFull
from vkbottle_types.responses.base_response import BaseResponse


class DonutGetSubscriptionResponse(BaseResponse):
    response: "DonutDonatorSubscriptionInfo" = Field()


class DonutGetSubscriptionsResponseModel(BaseModel):
    subscriptions: list["DonutDonatorSubscriptionInfo"] = Field()
    count: int | None = Field(
        default=None,
    )
    profiles: list["UsersUserFull"] | None = Field(
        default=None,
    )
    groups: list["GroupsGroupFull"] | None = Field(
        default=None,
    )


class DonutGetSubscriptionsResponse(BaseResponse):
    response: "DonutGetSubscriptionsResponseModel" = Field()
