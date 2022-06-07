import typing

from vkbottle_types.objects import (
    FriendsFriendExtendedStatus,
    FriendsFriendsList,
    FriendsFriendStatus,
    FriendsMutualFriend,
    FriendsRequests,
    FriendsRequestsXtrMessage,
    FriendsUserXtrPhone,
    UsersUserFull,
)
from vkbottle_types.responses.base_response import BaseResponse


class AddListResponse(BaseResponse):
    response: "AddListResponseModel"


class AddResponse(BaseResponse):
    response: int


class AreFriendsExtendedResponse(BaseResponse):
    response: typing.List["FriendsFriendExtendedStatus"]


class AreFriendsResponse(BaseResponse):
    response: typing.List["FriendsFriendStatus"]


class DeleteResponse(BaseResponse):
    response: "DeleteResponseModel"


class GetAppUsersResponse(BaseResponse):
    response: typing.List[int]


class GetByPhonesResponse(BaseResponse):
    response: typing.List["FriendsUserXtrPhone"]


class GetListsResponse(BaseResponse):
    response: "GetListsResponseModel"


class GetMutualResponse(BaseResponse):
    response: typing.List[int]


class GetMutualTargetUidsResponse(BaseResponse):
    response: typing.List["FriendsMutualFriend"]


class GetOnlineOnlineMobileResponse(BaseResponse):
    response: "GetOnlineOnlineMobileResponseModel"


class GetOnlineResponse(BaseResponse):
    response: typing.List[int]


class GetRecentResponse(BaseResponse):
    response: typing.List[int]


class GetRequestsExtendedResponse(BaseResponse):
    response: "GetRequestsExtendedResponseModel"


class GetRequestsNeedMutualResponse(BaseResponse):
    response: "GetRequestsNeedMutualResponseModel"


class GetRequestsResponse(BaseResponse):
    response: "GetRequestsResponseModel"


class GetSuggestionsResponse(BaseResponse):
    response: "GetSuggestionsResponseModel"


class GetFieldsResponse(BaseResponse):
    response: "GetFieldsResponseModel"


class GetResponse(BaseResponse):
    response: "GetResponseModel"


class SearchResponse(BaseResponse):
    response: "SearchResponseModel"


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


__all__ = (
    "AddListResponse",
    "AddListResponseModel",
    "AddResponse",
    "AreFriendsExtendedResponse",
    "AreFriendsResponse",
    "DeleteResponse",
    "DeleteResponseModel",
    "FriendsFriendExtendedStatus",
    "FriendsFriendStatus",
    "FriendsFriendsList",
    "FriendsMutualFriend",
    "FriendsRequests",
    "FriendsRequestsXtrMessage",
    "FriendsUserXtrPhone",
    "GetAppUsersResponse",
    "GetByPhonesResponse",
    "GetFieldsResponse",
    "GetFieldsResponseModel",
    "GetListsResponse",
    "GetListsResponseModel",
    "GetMutualResponse",
    "GetMutualTargetUidsResponse",
    "GetOnlineOnlineMobileResponse",
    "GetOnlineOnlineMobileResponseModel",
    "GetOnlineResponse",
    "GetRecentResponse",
    "GetRequestsExtendedResponse",
    "GetRequestsExtendedResponseModel",
    "GetRequestsNeedMutualResponse",
    "GetRequestsNeedMutualResponseModel",
    "GetRequestsResponse",
    "GetRequestsResponseModel",
    "GetResponse",
    "GetResponseModel",
    "GetSuggestionsResponse",
    "GetSuggestionsResponseModel",
    "SearchResponse",
    "SearchResponseModel",
    "UsersUserFull",
)
