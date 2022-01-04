import inspect
import typing
from .base_response import BaseResponse
from vkbottle_types.objects import (
    GroupsGroupsArray,
    UsersSubscriptionsItem,
    UsersUserFull,
    UsersUsersArray,
)


class GetFollowersFieldsResponse(BaseResponse):
    response: "GetFollowersFieldsResponseModel" = None


class GetFollowersResponse(BaseResponse):
    response: "GetFollowersResponseModel" = None


class GetSubscriptionsExtendedResponse(BaseResponse):
    response: "GetSubscriptionsExtendedResponseModel" = None


class GetSubscriptionsResponse(BaseResponse):
    response: "GetSubscriptionsResponseModel" = None


class GetResponse(BaseResponse):
    response: typing.List["UsersUserFull"] = None


class SearchResponse(BaseResponse):
    response: "SearchResponseModel" = None


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


class SearchResponseModel(BaseResponse):
    count: typing.Optional[int] = None
    items: typing.Optional[typing.List["UsersUserFull"]] = None


for item in locals().copy().values():
    if inspect.isclass(item) and issubclass(item, BaseResponse):
        item.update_forward_refs()
