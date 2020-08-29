import typing
from typing import Optional

from vkbottle_types.objects import groups, wall, newsfeed, users
from .base_response import BaseResponse


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
    response: Optional[int] = None


class SearchExtendedResponse(BaseResponse):
    response: Optional["SearchExtendedResponseModel"] = None


class SearchResponse(BaseResponse):
    response: Optional["SearchResponseModel"] = None


class GetBannedExtendedResponseModel(BaseResponse):
    groups: Optional[typing.List["users.UserFull"]] = None
    profiles: Optional[typing.List["groups.GroupFull"]] = None


class GetBannedResponseModel(BaseResponse):
    groups: Optional[typing.List[int]] = None
    members: Optional[typing.List[int]] = None


class GetCommentsResponseModel(BaseResponse):
    items: Optional[typing.List["newsfeed.NewsfeedItem"]] = None
    profiles: Optional[typing.List["users.UserFull"]] = None
    groups: Optional[typing.List["groups.GroupFull"]] = None
    next_from: Optional[str] = None


class GetListsExtendedResponseModel(BaseResponse):
    count: Optional[int] = None
    items: Optional[typing.List["newsfeed.ListFull"]] = None


class GetListsResponseModel(BaseResponse):
    count: Optional[int] = None
    items: Optional[typing.List["newsfeed.List"]] = None


class GetMentionsResponseModel(BaseResponse):
    count: Optional[int] = None
    items: Optional[typing.List["wall.WallpostToId"]] = None


class GetRecommendedResponseModel(BaseResponse):
    items: Optional[typing.List["newsfeed.NewsfeedItem"]] = None
    profiles: Optional[typing.List["users.UserFull"]] = None
    groups: Optional[typing.List["groups.GroupFull"]] = None
    new_offset: Optional[str] = None
    next_from: Optional[str] = None


class GetSuggestedSourcesResponseModel("groups.GroupFull", "users.UserXtrType"):
    count: Optional[int] = None


class GetResponseModel(BaseResponse):
    items: Optional[typing.List["newsfeed.NewsfeedItem"]] = None
    profiles: Optional[typing.List["users.UserFull"]] = None
    groups: Optional[typing.List["groups.GroupFull"]] = None
    next_from: Optional[str] = None


class SearchExtendedResponseModel(BaseResponse):
    items: Optional[typing.List["wall.WallpostFull"]] = None
    profiles: Optional[typing.List["users.UserFull"]] = None
    groups: Optional[typing.List["groups.GroupFull"]] = None
    suggested_queries: Optional[typing.List[str]] = None
    next_from: Optional[str] = None
    count: Optional[int] = None
    total_count: Optional[int] = None


class SearchResponseModel(BaseResponse):
    items: Optional[typing.List["wall.WallpostFull"]] = None
    suggested_queries: Optional[typing.List[str]] = None
    next_from: Optional[str] = None
    count: Optional[int] = None
    total_count: Optional[int] = None
