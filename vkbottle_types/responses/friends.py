import typing
from typing import Optional

from vkbottle_types.objects import friends, users
from .base_response import BaseResponse


class AddListResponse(BaseResponse):
    response: Optional["AddListResponseModel"] = None


class AddResponse(BaseResponse):
    response: Optional[int] = None


class AreFriendsExtendedResponse(BaseResponse):
    response: Optional[typing.List["friends.FriendExtendedStatus"]] = None


class AreFriendsResponse(BaseResponse):
    response: Optional[typing.List["friends.FriendStatus"]] = None


class DeleteResponse(BaseResponse):
    response: Optional["DeleteResponseModel"] = None


class GetAppUsersResponse(BaseResponse):
    response: Optional[typing.List[int]] = None


class GetByPhonesResponse(BaseResponse):
    response: Optional[typing.List["friends.UserXtrPhone"]] = None


class GetListsResponse(BaseResponse):
    response: Optional["GetListsResponseModel"] = None


class GetMutualResponse(BaseResponse):
    response: Optional[typing.List[int]] = None


class GetMutualTargetUidsResponse(BaseResponse):
    response: Optional[typing.List["friends.MutualFriend"]] = None


class GetOnlineOnlineMobileResponse(BaseResponse):
    response: Optional["GetOnlineOnlineMobileResponseModel"] = None


class GetOnlineResponse(BaseResponse):
    response: Optional[typing.List[int]] = None


class GetRecentResponse(BaseResponse):
    response: Optional[typing.List[int]] = None


class GetRequestsExtendedResponse(BaseResponse):
    response: Optional["GetRequestsExtendedResponseModel"] = None


class GetRequestsNeedMutualResponse(BaseResponse):
    response: Optional["GetRequestsNeedMutualResponseModel"] = None


class GetRequestsResponse(BaseResponse):
    response: Optional["GetRequestsResponseModel"] = None


class GetSuggestionsResponse(BaseResponse):
    response: Optional["GetSuggestionsResponseModel"] = None


class GetFieldsResponse(BaseResponse):
    response: Optional["GetFieldsResponseModel"] = None


class GetResponse(BaseResponse):
    response: Optional["GetResponseModel"] = None


class SearchResponse(BaseResponse):
    response: Optional["SearchResponseModel"] = None


class AddListResponseModel(BaseResponse):
    list_id: Optional[int] = None


class DeleteResponseModel(BaseResponse):
    success: Optional[int] = None
    friend_deleted: Optional[int] = None
    out_request_deleted: Optional[int] = None
    in_request_deleted: Optional[int] = None
    suggestion_deleted: Optional[int] = None


class GetListsResponseModel(BaseResponse):
    count: Optional[int] = None
    items: Optional[typing.List["friends.FriendsList"]] = None


class GetOnlineOnlineMobileResponseModel(BaseResponse):
    online: Optional[typing.List[int]] = None
    online_mobile: Optional[typing.List[int]] = None


class GetRequestsExtendedResponseModel(BaseResponse):
    count: Optional[int] = None
    items: Optional[typing.List["friends.RequestsXtrMessage"]] = None


class GetRequestsNeedMutualResponseModel(BaseResponse):
    count: Optional[int] = None
    items: Optional[typing.List["friends.Requests"]] = None


class GetRequestsResponseModel(BaseResponse):
    count: Optional[int] = None
    items: Optional[typing.List[int]] = None
    count_unread: Optional[int] = None


class GetSuggestionsResponseModel(BaseResponse):
    count: Optional[int] = None
    items: Optional[typing.List["users.UserFull"]] = None


class GetFieldsResponseModel(BaseResponse):
    count: Optional[int] = None
    items: Optional[typing.List["friends.UserXtrLists"]] = None


class GetResponseModel(BaseResponse):
    count: Optional[int] = None
    items: Optional[typing.List[int]] = None


class SearchResponseModel(BaseResponse):
    count: Optional[int] = None
    items: Optional[typing.List["users.UserFull"]] = None
