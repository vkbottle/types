import enum
import typing

from vkbottle_types.base_model import BaseModel, Field
from vkbottle_types.objects import (
    FriendsFriendExtendedStatus,
    FriendsFriendsList,
    FriendsFriendStatus,
    FriendsMutualFriend,
    FriendsOnlineUsers,
    FriendsOnlineUsersWithMobile,
    FriendsRequestsXtrMessage,
    FriendsRequestsXtrMutual,
    UsersUserFull,
)
from vkbottle_types.responses.base_response import BaseResponse


class FriendsAddListResponseModel(BaseModel):
    list_id: int = Field()


class FriendsAddListResponse(BaseResponse):
    response: "FriendsAddListResponseModel" = Field()


class FriendsAddResponseModel(enum.IntEnum):
    SEND = 1
    APPROVED = 2
    RESEND = 4


class FriendsAddResponse(BaseResponse):
    response: "FriendsAddResponseModel" = Field()


class FriendsAreFriendsExtendedResponse(BaseResponse):
    response: typing.List["FriendsFriendExtendedStatus"] = Field()


class FriendsAreFriendsResponse(BaseResponse):
    response: typing.List["FriendsFriendStatus"] = Field()


class FriendsDeleteResponseModel(BaseModel):
    success: int = Field(default=1)
    friend_deleted: typing.Optional[int] = Field(
        default=None,
    )
    out_request_deleted: typing.Optional[int] = Field(
        default=None,
    )
    in_request_deleted: typing.Optional[int] = Field(
        default=None,
    )
    suggestion_deleted: typing.Optional[int] = Field(
        default=None,
    )


class FriendsDeleteResponse(BaseResponse):
    response: "FriendsDeleteResponseModel" = Field()


class FriendsGetAppUsersResponse(BaseResponse):
    response: typing.List[int] = Field()


class FriendsGetListsResponseModel(BaseModel):
    count: int = Field()
    items: typing.List["FriendsFriendsList"] = Field()


class FriendsGetListsResponse(BaseResponse):
    response: "FriendsGetListsResponseModel" = Field()


class FriendsGetMutualResponse(BaseResponse):
    response: typing.List[int] = Field()


class FriendsGetMutualTargetUidsResponse(BaseResponse):
    response: typing.List["FriendsMutualFriend"] = Field()


class FriendsGetMutualTotalCountResponse(BaseResponse):
    response: "FriendsMutualFriend" = Field()


class FriendsGetOnlineExtendedResponse(BaseResponse):
    response: "FriendsOnlineUsers" = Field()


class FriendsGetOnlineOnlineMobileExtendedResponse(BaseResponse):
    response: "FriendsOnlineUsersWithMobile" = Field()


class FriendsGetOnlineOnlineMobileResponseModel(BaseModel):
    online: typing.List[int] = Field()
    online_mobile: typing.List[int] = Field()


class FriendsGetOnlineOnlineMobileResponse(BaseResponse):
    response: "FriendsGetOnlineOnlineMobileResponseModel" = Field()


class FriendsGetOnlineResponse(BaseResponse):
    response: typing.List[int] = Field()


class FriendsGetRecentResponse(BaseResponse):
    response: typing.List[int] = Field()


class FriendsGetRequestsExtendedResponseModel(BaseModel):
    count: int = Field()
    items: typing.List["FriendsRequestsXtrMessage"] = Field()
    count_unread: typing.Optional[int] = Field(
        default=None,
    )
    last_viewed: typing.Optional[int] = Field(
        default=None,
    )


class FriendsGetRequestsExtendedResponse(BaseResponse):
    response: "FriendsGetRequestsExtendedResponseModel" = Field()


class FriendsGetRequestsNeedMutualResponseModel(BaseModel):
    count: int = Field()
    items: typing.List["FriendsRequestsXtrMutual"] = Field()
    count_unread: typing.Optional[int] = Field(
        default=None,
    )
    last_viewed: typing.Optional[int] = Field(
        default=None,
    )


class FriendsGetRequestsNeedMutualResponse(BaseResponse):
    response: "FriendsGetRequestsNeedMutualResponseModel" = Field()


class FriendsGetRequestsResponseModel(BaseModel):
    count: int = Field()
    items: typing.List[int] = Field()
    count_unread: typing.Optional[int] = Field(
        default=None,
    )
    last_viewed: typing.Optional[int] = Field(
        default=None,
    )


class FriendsGetRequestsResponse(BaseResponse):
    response: "FriendsGetRequestsResponseModel" = Field()


class FriendsGetSuggestionsResponseModel(BaseModel):
    count: int = Field()
    items: typing.List["UsersUserFull"] = Field()


class FriendsGetSuggestionsResponse(BaseResponse):
    response: "FriendsGetSuggestionsResponseModel" = Field()


class FriendsGetFieldsResponseModel(BaseModel):
    count: int = Field()
    items: typing.List["UsersUserFull"] = Field()
    profiles: typing.Optional[typing.List["UsersUserFull"]] = Field(
        default=None,
    )


class FriendsGetFieldsResponse(BaseResponse):
    response: "FriendsGetFieldsResponseModel" = Field()


class FriendsGetResponseModel(BaseModel):
    count: int = Field()
    items: typing.List[int] = Field()


class FriendsGetResponse(BaseResponse):
    response: "FriendsGetResponseModel" = Field()


class FriendsSearchResponseModel(BaseModel):
    count: int = Field()
    items: typing.List["UsersUserFull"] = Field()


class FriendsSearchResponse(BaseResponse):
    response: "FriendsSearchResponseModel" = Field()
