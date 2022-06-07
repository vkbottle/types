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
from vkbottle_types.responses.base_response import BaseResponse


class GenericResponse(BaseResponse):
    response: "GenericResponseModel"


class GetBannedExtendedResponse(BaseResponse):
    response: "GetBannedExtendedResponseModel"


class GetBannedResponse(BaseResponse):
    response: "GetBannedResponseModel"


class GetCommentsResponse(BaseResponse):
    response: "GetCommentsResponseModel"


class GetListsExtendedResponse(BaseResponse):
    response: "GetListsExtendedResponseModel"


class GetListsResponse(BaseResponse):
    response: "GetListsResponseModel"


class GetMentionsResponse(BaseResponse):
    response: "GetMentionsResponseModel"


class GetSuggestedSourcesResponse(BaseResponse):
    response: "GetSuggestedSourcesResponseModel"


class IgnoreItemResponse(BaseResponse):
    response: "IgnoreItemResponseModel"


class SaveListResponse(BaseResponse):
    response: int


class SearchExtendedResponse(BaseResponse):
    response: "SearchExtendedResponseModel"


class SearchResponse(BaseResponse):
    response: "SearchResponseModel"


class GenericResponseModel(BaseResponse):
    items: typing.Optional[typing.List["NewsfeedNewsfeedItem"]] = None
    profiles: typing.Optional[typing.List["UsersUserFull"]] = None
    groups: typing.Optional[typing.List["GroupsGroupFull"]] = None
    new_returned_news_items_count: typing.Optional[int] = None


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


class GetSuggestedSourcesResponseModel(BaseResponse):
    count: typing.Optional[int] = None
    items: typing.Optional[typing.List["UsersSubscriptionsItem"]] = None


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


__all__ = (
    "GenericResponse",
    "GenericResponseModel",
    "GetBannedExtendedResponse",
    "GetBannedExtendedResponseModel",
    "GetBannedResponse",
    "GetBannedResponseModel",
    "GetCommentsResponse",
    "GetCommentsResponseModel",
    "GetListsExtendedResponse",
    "GetListsExtendedResponseModel",
    "GetListsResponse",
    "GetListsResponseModel",
    "GetMentionsResponse",
    "GetMentionsResponseModel",
    "GetSuggestedSourcesResponse",
    "GetSuggestedSourcesResponseModel",
    "GroupsGroupFull",
    "IgnoreItemResponse",
    "IgnoreItemResponseModel",
    "NewsfeedList",
    "NewsfeedListFull",
    "NewsfeedNewsfeedItem",
    "SaveListResponse",
    "SearchExtendedResponse",
    "SearchExtendedResponseModel",
    "SearchResponse",
    "SearchResponseModel",
    "UsersSubscriptionsItem",
    "UsersUserFull",
    "WallWallpostFull",
    "WallWallpostToId",
)
