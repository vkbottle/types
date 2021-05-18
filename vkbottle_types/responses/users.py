from typing import List, Optional

from vkbottle_types.objects import (
    GroupsGroupsArray,
    UsersSubscriptionsItem,
    UsersUserFull,
    UsersUsersArray,
    UsersUserXtrCounters,
)

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
    response: Optional["GetResponseModel"] = None


class SearchResponse(BaseResponse):
    response: Optional["SearchResponseModel"] = None


class GetFollowersFieldsResponseModel(BaseResponse):
    count: Optional[int] = None
    items: Optional[List["UsersUserFull"]] = None


class GetFollowersResponseModel(BaseResponse):
    count: Optional[int] = None
    items: Optional[List[int]] = None


class GetSubscriptionsExtendedResponseModel(BaseResponse):
    count: Optional[int] = None
    items: Optional[List["UsersSubscriptionsItem"]] = None


class GetSubscriptionsResponseModel(BaseResponse):
    users: Optional["UsersUsersArray"] = None
    groups: Optional["GroupsGroupsArray"] = None


GetResponseModel = List[UsersUserXtrCounters]


class SearchResponseModel(BaseResponse):
    count: Optional[int] = None
    items: Optional[List["UsersUserFull"]] = None


GetFollowersFieldsResponse.update_forward_refs()
GetFollowersResponse.update_forward_refs()
GetSubscriptionsExtendedResponse.update_forward_refs()
GetSubscriptionsResponse.update_forward_refs()
GetResponse.update_forward_refs()
SearchResponse.update_forward_refs()
