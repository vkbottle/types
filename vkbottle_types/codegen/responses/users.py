import typing

from vkbottle_types.objects import (
    GroupsGroupsArray,
    UsersSubscriptionsItem,
    UsersUserFull,
    UsersUsersArray,
)
from vkbottle_types.responses.base_response import BaseResponse


class GetFollowersFieldsResponse(BaseResponse):
    response: "GetFollowersFieldsResponseModel"


class GetFollowersResponse(BaseResponse):
    response: "GetFollowersResponseModel"


class GetSubscriptionsExtendedResponse(BaseResponse):
    response: "GetSubscriptionsExtendedResponseModel"


class GetSubscriptionsResponse(BaseResponse):
    response: "GetSubscriptionsResponseModel"


class GetResponse(BaseResponse):
    response: typing.List["UsersUserFull"]


class SearchResponse(BaseResponse):
    response: "SearchResponseModel"


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


__all__ = (
    "GetFollowersFieldsResponse",
    "GetFollowersFieldsResponseModel",
    "GetFollowersResponse",
    "GetFollowersResponseModel",
    "GetResponse",
    "GetSubscriptionsExtendedResponse",
    "GetSubscriptionsExtendedResponseModel",
    "GetSubscriptionsResponse",
    "GetSubscriptionsResponseModel",
    "GroupsGroupsArray",
    "SearchResponse",
    "SearchResponseModel",
    "UsersSubscriptionsItem",
    "UsersUserFull",
    "UsersUsersArray",
)
