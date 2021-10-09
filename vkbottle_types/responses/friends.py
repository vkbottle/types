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
    FriendsUserXtrPhone,
    UsersUserFull
)


class AddListResponse(BaseResponse):
    response: "AddListResponseModel" = None


class AddResponse(BaseResponse):
    response: int = None


class AreFriendsExtendedResponse(BaseResponse):
    response: typing.List["FriendsFriendExtendedStatus"] = None


class AreFriendsResponse(BaseResponse):
    response: typing.List["FriendsFriendStatus"] = None


class DeleteResponse(BaseResponse):
    response: "DeleteResponseModel" = None


class GetAppUsersResponse(BaseResponse):
    response: typing.List[int] = None


class GetByPhonesResponse(BaseResponse):
    response: typing.List["FriendsUserXtrPhone"] = None


class GetListsResponse(BaseResponse):
    response: "GetListsResponseModel" = None


class GetMutualResponse(BaseResponse):
    response: typing.List[int] = None


class GetMutualTargetUidsResponse(BaseResponse):
    response: typing.List["FriendsMutualFriend"] = None


class GetOnlineOnlineMobileResponse(BaseResponse):
    response: "GetOnlineOnlineMobileResponseModel" = None


class GetOnlineResponse(BaseResponse):
    response: typing.List[int] = None


class GetRecentResponse(BaseResponse):
    response: typing.List[int] = None


class GetRequestsExtendedResponse(BaseResponse):
    response: "GetRequestsExtendedResponseModel" = None


class GetRequestsNeedMutualResponse(BaseResponse):
    response: "GetRequestsNeedMutualResponseModel" = None


class GetRequestsResponse(BaseResponse):
    response: "GetRequestsResponseModel" = None


class GetSuggestionsResponse(BaseResponse):
    response: "GetSuggestionsResponseModel" = None


class GetFieldsResponse(BaseResponse):
    response: "GetFieldsResponseModel" = None


class GetResponse(BaseResponse):
    response: "GetResponseModel" = None


class SearchResponse(BaseResponse):
    response: "SearchResponseModel" = None


class AddListResponseModel(BaseResponse):
    list_id: typing.Optional[int] = None


class DeleteResponseModel(BaseResponse):
    success: typing.Optional[int] = None
    friend_deleted: typing.Optional[int] = None
    out_request_deleted: typing.Optional[int] = None
    in_request_deleted: typing.Optional[int] = None
    suggestion_deleted: typing.Optional[int] = None


class GetListsResponseModel(BaseResponse):
    count: typing.Optional[int] = None
    items: typing.Optional[typing.List["FriendsFriendsList"]] = None


class GetOnlineOnlineMobileResponseModel(BaseResponse):
    online: typing.Optional[typing.List[int]] = None
    online_mobile: typing.Optional[typing.List[int]] = None


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
    items: typing.Optional[typing.List["UsersUserFull"]] = None


class GetResponseModel(BaseResponse):
    count: typing.Optional[int] = None
    items: typing.Optional[typing.List[int]] = None


class SearchResponseModel(BaseResponse):
    count: typing.Optional[int] = None
    items: typing.Optional[typing.List["UsersUserFull"]] = None


for item in locals().copy().values():
    if inspect.isclass(item) and issubclass(item, BaseResponse):
        item.update_forward_refs()
