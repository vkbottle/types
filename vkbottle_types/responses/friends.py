import inspect
import typing
from .base_response import BaseResponse
from vkbottle_types.objects import (
    FriendsFriendExtendedStatus,
    FriendsFriendStatus,
    FriendsFriendsList,
    FriendsMutualFriend,
    FriendsRequests,
    FriendsRequestsXtrMessage,
    FriendsUserXtrLists,
    FriendsUserXtrPhone,
    UsersUserFull
)


class AddListResponse(BaseResponse):
    response: typing.Optional["AddListResponseModel"] = None


class AddResponse(BaseResponse):
    response: typing.Optional["AddResponseModel"] = None


class AreFriendsExtendedResponse(BaseResponse):
    response: typing.Optional["AreFriendsExtendedResponseModel"] = None


class AreFriendsResponse(BaseResponse):
    response: typing.Optional["AreFriendsResponseModel"] = None


class DeleteResponse(BaseResponse):
    response: typing.Optional["DeleteResponseModel"] = None


class GetAppUsersResponse(BaseResponse):
    response: typing.Optional["GetAppUsersResponseModel"] = None


class GetByPhonesResponse(BaseResponse):
    response: typing.Optional["GetByPhonesResponseModel"] = None


class GetListsResponse(BaseResponse):
    response: typing.Optional["GetListsResponseModel"] = None


class GetMutualResponse(BaseResponse):
    response: typing.Optional["GetMutualResponseModel"] = None


class GetMutualTargetUidsResponse(BaseResponse):
    response: typing.Optional["GetMutualTargetUidsResponseModel"] = None


class GetOnlineOnlineMobileResponse(BaseResponse):
    response: typing.Optional["GetOnlineOnlineMobileResponseModel"] = None


class GetOnlineResponse(BaseResponse):
    response: typing.Optional["GetOnlineResponseModel"] = None


class GetRecentResponse(BaseResponse):
    response: typing.Optional["GetRecentResponseModel"] = None


class GetRequestsExtendedResponse(BaseResponse):
    response: typing.Optional["GetRequestsExtendedResponseModel"] = None


class GetRequestsNeedMutualResponse(BaseResponse):
    response: typing.Optional["GetRequestsNeedMutualResponseModel"] = None


class GetRequestsResponse(BaseResponse):
    response: typing.Optional["GetRequestsResponseModel"] = None


class GetSuggestionsResponse(BaseResponse):
    response: typing.Optional["GetSuggestionsResponseModel"] = None


class GetFieldsResponse(BaseResponse):
    response: typing.Optional["GetFieldsResponseModel"] = None


class GetResponse(BaseResponse):
    response: typing.Optional["GetResponseModel"] = None


class SearchResponse(BaseResponse):
    response: typing.Optional["SearchResponseModel"] = None


class AddListResponseModel(BaseResponse):
    list_id: typing.Optional[int] = None


AddResponseModel = int


AreFriendsExtendedResponseModel = typing.List[FriendsFriendExtendedStatus]


AreFriendsResponseModel = typing.List[FriendsFriendStatus]


class DeleteResponseModel(BaseResponse):
    success: typing.Optional[int] = None
    friend_deleted: typing.Optional[int] = None
    out_request_deleted: typing.Optional[int] = None
    in_request_deleted: typing.Optional[int] = None
    suggestion_deleted: typing.Optional[int] = None


GetAppUsersResponseModel = typing.List[int]


GetByPhonesResponseModel = typing.List[FriendsUserXtrPhone]


class GetListsResponseModel(BaseResponse):
    count: typing.Optional[int] = None
    items: typing.Optional[typing.List["FriendsFriendsList"]] = None


GetMutualResponseModel = typing.List[int]


GetMutualTargetUidsResponseModel = typing.List[FriendsMutualFriend]


class GetOnlineOnlineMobileResponseModel(BaseResponse):
    online: typing.Optional[typing.List[int]] = None
    online_mobile: typing.Optional[typing.List[int]] = None


GetOnlineResponseModel = typing.List[int]


GetRecentResponseModel = typing.List[int]


class GetRequestsExtendedResponseModel(BaseResponse):
    count: typing.Optional[int] = None
    items: typing.Optional[typing.List["FriendsRequestsXtrMessage"]] = None


class GetRequestsNeedMutualResponseModel(BaseResponse):
    count: typing.Optional[int] = None
    items: typing.Optional[typing.List["FriendsRequests"]] = None


class GetRequestsResponseModel(BaseResponse):
    count: typing.Optional[int] = None
    items: typing.Optional[typing.List[int]] = None
    count_unread: typing.Optional[int] = None


class GetSuggestionsResponseModel(BaseResponse):
    count: typing.Optional[int] = None
    items: typing.Optional[typing.List["UsersUserFull"]] = None


class GetFieldsResponseModel(BaseResponse):
    count: typing.Optional[int] = None
    items: typing.Optional[typing.List["FriendsUserXtrLists"]] = None


class GetResponseModel(BaseResponse):
    count: typing.Optional[int] = None
    items: typing.Optional[typing.List[int]] = None


class SearchResponseModel(BaseResponse):
    count: typing.Optional[int] = None
    items: typing.Optional[typing.List["UsersUserFull"]] = None


for item in locals().copy().values():
    if inspect.isclass(item) and issubclass(item, BaseResponse):
        item.update_forward_refs()
