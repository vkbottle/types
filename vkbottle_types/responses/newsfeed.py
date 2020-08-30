from .base_response import BaseResponse
from vkbottle_types.objects import users, newsfeed, wall, groups
from typing import Optional, Any, List, Union
import typing


class GetBannedExtendedResponse(BaseResponse):
    response: Optional["GetBannedExtendedResponseModel"] = None


class GetBannedResponse(BaseResponse):
    response: Optional["GetBannedResponseModel"] = None


class GetCommentsResponse(BaseResponse):
    response: Optional["GetCommentsResponseModel"] = None


class GetListsExtendedResponse(BaseResponse):
    response: Optional["GetListsExtendedResponseModel"] = None


class GetListsResponse(BaseResponse):
    response: Optional["GetListsResponseModel"] = None


class GetMentionsResponse(BaseResponse):
    response: Optional["GetMentionsResponseModel"] = None


class GetRecommendedResponse(BaseResponse):
    response: Optional["GetRecommendedResponseModel"] = None


class GetSuggestedSourcesResponse(BaseResponse):
    response: Optional["GetSuggestedSourcesResponseModel"] = None


class GetResponse(BaseResponse):
    response: Optional["GetResponseModel"] = None


class SaveListResponse(BaseResponse):
    response: Optional["SaveListResponseModel"] = None


class SearchExtendedResponse(BaseResponse):
    response: Optional["SearchExtendedResponseModel"] = None


class SearchResponse(BaseResponse):
    response: Optional["SearchResponseModel"] = None


class GetBannedExtendedResponseModel(BaseResponse):
    groups: Optional[List["users.UserFull"]] = None
    profiles: Optional[List["groups.GroupFull"]] = None


class GetBannedResponseModel(BaseResponse):
    groups: Optional[List[int]] = None
    members: Optional[List[int]] = None


class GetCommentsResponseModel(BaseResponse):
    items: Optional[List["newsfeed.NewsfeedItem"]] = None
    profiles: Optional[List["users.UserFull"]] = None
    groups: Optional[List["groups.GroupFull"]] = None
    next_from: Optional[str] = None


class GetListsExtendedResponseModel(BaseResponse):
    count: Optional[int] = None
    items: Optional[List["newsfeed.ListFull"]] = None


class GetListsResponseModel(BaseResponse):
    count: Optional[int] = None
    items: Optional[List["newsfeed.List"]] = None


class GetMentionsResponseModel(BaseResponse):
    count: Optional[int] = None
    items: Optional[List["wall.WallpostToId"]] = None


class GetRecommendedResponseModel(BaseResponse):
    items: Optional[List["newsfeed.NewsfeedItem"]] = None
    profiles: Optional[List["users.UserFull"]] = None
    groups: Optional[List["groups.GroupFull"]] = None
    new_offset: Optional[str] = None
    next_from: Optional[str] = None


class GetSuggestedSourcesResponseModel(BaseResponse):
    count: Optional[int] = None
    items: Optional[Union["groups.GroupFull", "users.UserXtrType"]] = None


class GetResponseModel(BaseResponse):
    items: Optional[List["newsfeed.NewsfeedItem"]] = None
    profiles: Optional[List["users.UserFull"]] = None
    groups: Optional[List["groups.GroupFull"]] = None
    next_from: Optional[str] = None


SaveListResponseModel = int


class SearchExtendedResponseModel(BaseResponse):
    items: Optional[List["wall.WallpostFull"]] = None
    profiles: Optional[List["users.UserFull"]] = None
    groups: Optional[List["groups.GroupFull"]] = None
    suggested_queries: Optional[List[str]] = None
    next_from: Optional[str] = None
    count: Optional[int] = None
    total_count: Optional[int] = None


class SearchResponseModel(BaseResponse):
    items: Optional[List["wall.WallpostFull"]] = None
    suggested_queries: Optional[List[str]] = None
    next_from: Optional[str] = None
    count: Optional[int] = None
    total_count: Optional[int] = None
