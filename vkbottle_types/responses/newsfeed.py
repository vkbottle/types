import inspect
import typing
from .base_response import BaseResponse
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


class GetBannedExtendedResponse(BaseResponse):
    response: "GetBannedExtendedResponseModel" = None


class GetBannedResponse(BaseResponse):
    response: "GetBannedResponseModel" = None


class GetCommentsResponse(BaseResponse):
    response: "GetCommentsResponseModel" = None


class GetListsExtendedResponse(BaseResponse):
    response: "GetListsExtendedResponseModel" = None


class GetListsResponse(BaseResponse):
    response: "GetListsResponseModel" = None


class GetMentionsResponse(BaseResponse):
    response: "GetMentionsResponseModel" = None


class GetRecommendedResponse(BaseResponse):
    response: "GetRecommendedResponseModel" = None


class GetSuggestedSourcesResponse(BaseResponse):
    response: "GetSuggestedSourcesResponseModel" = None


class GetResponse(BaseResponse):
    response: "GetResponseModel" = None


class IgnoreItemResponse(BaseResponse):
    response: "IgnoreItemResponseModel" = None


class SaveListResponse(BaseResponse):
    response: int = None


class SearchExtendedResponse(BaseResponse):
    response: "SearchExtendedResponseModel" = None


class SearchResponse(BaseResponse):
    response: "SearchResponseModel" = None


class GetBannedExtendedResponseModel(BaseResponse):
    profiles: typing.Optional[typing.List["UsersUserFull"]] = None
    groups: typing.Optional[typing.List["GroupsGroupFull"]] = None


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
