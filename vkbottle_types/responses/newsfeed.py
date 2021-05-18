import inspect
import typing

from vkbottle_types.objects import (
    GroupsGroupFull,
    NewsfeedList,
    NewsfeedListFull,
    NewsfeedNewsfeedItem,
    UsersSubscriptionsItem,
    UsersUserFull,
    WallWallpostFull,
    WallWallpostToId,
)

from .base_response import BaseResponse


class GetBannedExtendedResponse(BaseResponse):
    response: typing.Optional["GetBannedExtendedResponseModel"] = None


class GetBannedResponse(BaseResponse):
    response: typing.Optional["GetBannedResponseModel"] = None


class GetCommentsResponse(BaseResponse):
    response: typing.Optional["GetCommentsResponseModel"] = None


class GetListsExtendedResponse(BaseResponse):
    response: typing.Optional["GetListsExtendedResponseModel"] = None


class GetListsResponse(BaseResponse):
    response: typing.Optional["GetListsResponseModel"] = None


class GetMentionsResponse(BaseResponse):
    response: typing.Optional["GetMentionsResponseModel"] = None


class GetRecommendedResponse(BaseResponse):
    response: typing.Optional["GetRecommendedResponseModel"] = None


class GetSuggestedSourcesResponse(BaseResponse):
    response: typing.Optional["GetSuggestedSourcesResponseModel"] = None


class GetResponse(BaseResponse):
    response: typing.Optional["GetResponseModel"] = None


class IgnoreItemResponse(BaseResponse):
    response: typing.Optional["IgnoreItemResponseModel"] = None


class SaveListResponse(BaseResponse):
    response: typing.Optional["SaveListResponseModel"] = None


class SearchExtendedResponse(BaseResponse):
    response: typing.Optional["SearchExtendedResponseModel"] = None


class SearchResponse(BaseResponse):
    response: typing.Optional["SearchResponseModel"] = None


class GetBannedExtendedResponseModel(BaseResponse):
    groups: typing.Optional[typing.List["UsersUserFull"]] = None
    profiles: typing.Optional[typing.List["GroupsGroupFull"]] = None


class GetBannedResponseModel(BaseResponse):
    groups: typing.Optional[typing.List[int]] = None
    members: typing.Optional[typing.List[int]] = None


class GetCommentsResponseModel(BaseResponse):
    items: typing.Optional[typing.List["NewsfeedNewsfeedItem"]] = None
    profiles: typing.Optional[typing.List["UsersUserFull"]] = None
    groups: typing.Optional[typing.List["GroupsGroupFull"]] = None
    next_from: typing.Optional[str] = None


class GetListsExtendedResponseModel(BaseResponse):
    count: typing.Optional[int] = None
    items: typing.Optional[typing.List["NewsfeedListFull"]] = None


class GetListsResponseModel(BaseResponse):
    count: typing.Optional[int] = None
    items: typing.Optional[typing.List["NewsfeedList"]] = None


class GetMentionsResponseModel(BaseResponse):
    count: typing.Optional[int] = None
    items: typing.Optional[typing.List["WallWallpostToId"]] = None


class GetRecommendedResponseModel(BaseResponse):
    items: typing.Optional[typing.List["NewsfeedNewsfeedItem"]] = None
    profiles: typing.Optional[typing.List["UsersUserFull"]] = None
    groups: typing.Optional[typing.List["GroupsGroupFull"]] = None
    next_from: typing.Optional[str] = None


class GetSuggestedSourcesResponseModel(BaseResponse):
    count: typing.Optional[int] = None
    items: typing.Optional[typing.List["UsersSubscriptionsItem"]] = None


class GetResponseModel(BaseResponse):
    items: typing.Optional[typing.List["NewsfeedNewsfeedItem"]] = None
    profiles: typing.Optional[typing.List["UsersUserFull"]] = None
    groups: typing.Optional[typing.List["GroupsGroupFull"]] = None
    next_from: typing.Optional[str] = None


class IgnoreItemResponseModel(BaseResponse):
    status: typing.Optional[bool] = None


SaveListResponseModel = int


class SearchExtendedResponseModel(BaseResponse):
    items: typing.Optional[typing.List["WallWallpostFull"]] = None
    profiles: typing.Optional[typing.List["UsersUserFull"]] = None
    groups: typing.Optional[typing.List["GroupsGroupFull"]] = None
    suggested_queries: typing.Optional[typing.List[str]] = None
    next_from: typing.Optional[str] = None
    count: typing.Optional[int] = None
    total_count: typing.Optional[int] = None


class SearchResponseModel(BaseResponse):
    items: typing.Optional[typing.List["WallWallpostFull"]] = None
    suggested_queries: typing.Optional[typing.List[str]] = None
    next_from: typing.Optional[str] = None
    count: typing.Optional[int] = None
    total_count: typing.Optional[int] = None


for item in locals().copy().values():
    if inspect.isclass(item) and issubclass(item, BaseResponse):
        item.update_forward_refs()
