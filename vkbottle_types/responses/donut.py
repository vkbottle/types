import inspect
import typing
from .base_response import BaseResponse
from vkbottle_types.objects import DonutDonatorSubscriptionInfo, GroupsGroupFull, UsersUserFull


class GetSubscriptionResponse(BaseResponse):
    response: typing.Optional["GetSubscriptionResponseModel"] = None


class GetSubscriptionsResponse(BaseResponse):
    response: typing.Optional["GetSubscriptionsResponseModel"] = None


GetSubscriptionResponseModel = DonutDonatorSubscriptionInfo


class GetSubscriptionsResponseModel(BaseResponse):
    subscriptions: typing.Optional[typing.List["DonutDonatorSubscriptionInfo"]] = None
    count: typing.Optional[int] = None
    profiles: typing.Optional[typing.List["UsersUserFull"]] = None
    groups: typing.Optional[typing.List["GroupsGroupFull"]] = None


for item in locals().copy().values():
    if inspect.isclass(item) and issubclass(item, BaseResponse):
        item.update_forward_refs()
