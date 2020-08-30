from .base_response import BaseResponse
from vkbottle_types.objects import users, groups
from typing import Optional, Any, List, Union
import typing


class GetFollowersFieldsResponse(BaseResponse):
    response: Optional["GetFollowersFieldsResponseModel"] = None


class GetFollowersResponse(BaseResponse):
    response: Optional["GetFollowersResponseModel"] = None


class GetSubscriptionsExtendedResponse(BaseResponse):
    response: Optional["GetSubscriptionsExtendedResponseModel"] = None


class GetSubscriptionsResponse(BaseResponse):
    response: Optional["GetSubscriptionsResponseModel"] = None


class GetResponse(BaseResponse):
    response: Optional["GetResponseModel"] = None


class SearchResponse(BaseResponse):
    response: Optional["SearchResponseModel"] = None


class GetFollowersFieldsResponseModel(BaseResponse):
    count: Optional[int] = None
    items: Optional[List["users.UserFull"]] = None


class GetFollowersResponseModel(BaseResponse):
    count: Optional[int] = None
    items: Optional[List[int]] = None


class GetSubscriptionsExtendedResponseModel(BaseResponse):
    count: Optional[int] = None
    items: Optional[List["users.SubscriptionsItem"]] = None


class GetSubscriptionsResponseModel(BaseResponse):
    users: Optional["users.UsersArray"] = None
    groups: Optional["groups.GroupsArray"] = None


GetResponseModel = List["users.UserXtrCounters"]


class SearchResponseModel(BaseResponse):
    count: Optional[int] = None
    items: Optional[List["users.UserFull"]] = None
