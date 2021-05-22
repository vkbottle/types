import inspect
import typing
from .base_response import BaseResponse
from vkbottle_types.objects import (
    GroupsGroupsArray,
    UsersSubscriptionsItem,
    UsersUserFull,
    UsersUserXtrCounters,
    UsersUsersArray
)


class GetFollowersFieldsResponse(BaseResponse):
    response: typing.Optional["GetFollowersFieldsResponseModel"] = None


class GetFollowersResponse(BaseResponse):
    response: typing.Optional["GetFollowersResponseModel"] = None


class GetSubscriptionsExtendedResponse(BaseResponse):
    response: typing.Optional["GetSubscriptionsExtendedResponseModel"] = None


class GetSubscriptionsResponse(BaseResponse):
    response: typing.Optional["GetSubscriptionsResponseModel"] = None


class GetResponse(BaseResponse):
    response: typing.Optional["GetResponseModel"] = None


class SearchResponse(BaseResponse):
    response: typing.Optional["SearchResponseModel"] = None


class GetFollowersFieldsResponseModel(BaseResponse):
    count: typing.Optional[int] = None
    items: typing.Optional[typing.List["UsersUserFull"]] = None


class GetFollowersResponseModel(BaseResponse):
    count: typing.Optional[int] = None
    items: typing.Optional[typing.List[int]] = None


class GetSubscriptionsExtendedResponseModel(BaseResponse):
    count: typing.Optional[int] = None
    items: typing.Optional[typing.List["UsersSubscriptionsItem"]] = None


class GetSubscriptionsResponseModel(BaseResponse):
    users: typing.Optional["UsersUsersArray"] = None
    groups: typing.Optional["GroupsGroupsArray"] = None


GetResponseModel = typing.List[UsersUserXtrCounters]


class SearchResponseModel(BaseResponse):
    count: typing.Optional[int] = None
    items: typing.Optional[typing.List["UsersUserFull"]] = None


for item in locals().copy().values():
    if inspect.isclass(item) and issubclass(item, BaseResponse):
        item.update_forward_refs()
