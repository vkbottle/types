import typing

from vkbottle_types.objects import (
    DonutDonatorSubscriptionInfo,
    GroupsGroupFull,
    UsersUserFull,
)
from vkbottle_types.responses.base_response import BaseResponse


class GetSubscriptionResponse(BaseResponse):
    response: DonutDonatorSubscriptionInfo


class GetSubscriptionsResponse(BaseResponse):
    response: "GetSubscriptionsResponseModel"


class GetSubscriptionsResponseModel(BaseResponse):
    subscriptions: typing.Optional[typing.List["DonutDonatorSubscriptionInfo"]] = None
    count: typing.Optional[int] = None
    profiles: typing.Optional[typing.List["UsersUserFull"]] = None
    groups: typing.Optional[typing.List["GroupsGroupFull"]] = None


__all__ = (
    "DonutDonatorSubscriptionInfo",
    "GetSubscriptionResponse",
    "GetSubscriptionsResponse",
    "GetSubscriptionsResponseModel",
    "GroupsGroupFull",
    "UsersUserFull",
)
