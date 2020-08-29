import typing
from typing import Optional

from vkbottle_types.objects import groups, users
from .base_response import BaseResponse


class GetFollowersFieldsResponse(BaseResponse):
    response: Optional["GetFollowersFieldsResponseModel"] = None


class GetFollowersResponse(BaseResponse):
    response: Optional["GetFollowersResponseModel"] = None


class GetSubscriptionsExtendedResponse(BaseResponse):
    response: Optional["GetSubscriptionsExtendedResponseModel"] = None


class GetSubscriptionsResponse(BaseResponse):
    response: Optional["GetSubscriptionsResponseModel"] = None


class GetResponse(BaseResponse):
    response: Optional[typing.List["users.UserXtrCounters"]] = None


class SearchResponse(BaseResponse):
    response: Optional["SearchResponseModel"] = None


class GetFollowersFieldsResponseModel(BaseResponse):
    count: Optional[int] = None
    items: Optional[typing.List["users.UserFull"]] = None


class GetFollowersResponseModel(BaseResponse):
    count: Optional[int] = None
    items: Optional[typing.List[int]] = None


class GetSubscriptionsExtendedResponseModel(BaseResponse):
    count: Optional[int] = None
    items: Optional[typing.List["users.SubscriptionsItem"]] = None


class GetSubscriptionsResponseModel(BaseResponse):
    users: Optional[typing.List["users.UsersArray"]] = None
    groups: Optional[typing.List["groups.GroupsArray"]] = None


class SearchResponseModel(BaseResponse):
    count: Optional[int] = None
    items: Optional[typing.List["users.UserFull"]] = None
