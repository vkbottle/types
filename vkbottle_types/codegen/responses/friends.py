from vkbottle_types.base_model import BaseEnumMeta, BaseModel, Field, IntEnum
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


class FriendsAddResponseModel(IntEnum, metaclass=BaseEnumMeta):
    SEND = 1
    APPROVED = 2
    RESEND = 4


class FriendsAddResponse(BaseResponse):
    response: "FriendsAddResponseModel" = Field()


class FriendsAreFriendsExtendedResponse(BaseResponse):
    response: list["FriendsFriendExtendedStatus"] = Field()


class FriendsAreFriendsResponse(BaseResponse):
    response: list["FriendsFriendStatus"] = Field()


class FriendsDeleteResponseModel(BaseModel):
    success: int = Field(default=1)
    friend_deleted: int | None = Field(
        default=None,
    )
    out_request_deleted: int | None = Field(
        default=None,
    )
    in_request_deleted: int | None = Field(
        default=None,
    )
    suggestion_deleted: int | None = Field(
        default=None,
    )


class FriendsDeleteResponse(BaseResponse):
    response: "FriendsDeleteResponseModel" = Field()


class FriendsGetAppUsersResponse(BaseResponse):
    response: list[int] = Field()


class FriendsGetListsResponseModel(BaseModel):
    count: int = Field()
    items: list["FriendsFriendsList"] = Field()


class FriendsGetListsResponse(BaseResponse):
    response: "FriendsGetListsResponseModel" = Field()


class FriendsGetMutualResponse(BaseResponse):
    response: list[int] = Field()


class FriendsGetMutualTargetUidsResponse(BaseResponse):
    response: list["FriendsMutualFriend"] = Field()


class FriendsGetMutualTotalCountResponse(BaseResponse):
    response: "FriendsMutualFriend" = Field()


class FriendsGetOnlineExtendedResponse(BaseResponse):
    response: "FriendsOnlineUsers" = Field()


class FriendsGetOnlineOnlineMobileExtendedResponse(BaseResponse):
    response: "FriendsOnlineUsersWithMobile" = Field()


class FriendsGetOnlineOnlineMobileResponseModel(BaseModel):
    online: list[int] = Field()
    online_mobile: list[int] = Field()


class FriendsGetOnlineOnlineMobileResponse(BaseResponse):
    response: "FriendsGetOnlineOnlineMobileResponseModel" = Field()


class FriendsGetOnlineResponse(BaseResponse):
    response: list[int] = Field()


class FriendsGetRecentResponse(BaseResponse):
    response: list[int] = Field()


class FriendsGetRequestsExtendedResponseModel(BaseModel):
    count: int = Field()
    items: list["FriendsRequestsXtrMessage"] = Field()
    count_unread: int | None = Field(
        default=None,
    )
    last_viewed: int | None = Field(
        default=None,
    )


class FriendsGetRequestsExtendedResponse(BaseResponse):
    response: "FriendsGetRequestsExtendedResponseModel" = Field()


class FriendsGetRequestsNeedMutualResponseModel(BaseModel):
    count: int = Field()
    items: list["FriendsRequestsXtrMutual"] = Field()
    count_unread: int | None = Field(
        default=None,
    )
    last_viewed: int | None = Field(
        default=None,
    )


class FriendsGetRequestsNeedMutualResponse(BaseResponse):
    response: "FriendsGetRequestsNeedMutualResponseModel" = Field()


class FriendsGetRequestsResponseModel(BaseModel):
    count: int = Field()
    items: list[int] = Field()
    count_unread: int | None = Field(
        default=None,
    )
    last_viewed: int | None = Field(
        default=None,
    )


class FriendsGetRequestsResponse(BaseResponse):
    response: "FriendsGetRequestsResponseModel" = Field()


class FriendsGetSuggestionsResponseModel(BaseModel):
    count: int = Field()
    items: list["UsersUserFull"] = Field()


class FriendsGetSuggestionsResponse(BaseResponse):
    response: "FriendsGetSuggestionsResponseModel" = Field()


class FriendsGetFieldsResponseModel(BaseModel):
    count: int = Field()
    items: list["UsersUserFull"] = Field()
    profiles: list["UsersUserFull"] | None = Field(
        default=None,
    )


class FriendsGetFieldsResponse(BaseResponse):
    response: "FriendsGetFieldsResponseModel" = Field()


class FriendsGetResponseModel(BaseModel):
    count: int = Field()
    items: list[int] = Field()


class FriendsGetResponse(BaseResponse):
    response: "FriendsGetResponseModel" = Field()


class FriendsSearchResponseModel(BaseModel):
    count: int = Field()
    items: list["UsersUserFull"] = Field()


class FriendsSearchResponse(BaseResponse):
    response: "FriendsSearchResponseModel" = Field()


__all__ = (
    "FriendsAddListResponse",
    "FriendsAddListResponseModel",
    "FriendsAddResponse",
    "FriendsAddResponseModel",
    "FriendsAreFriendsExtendedResponse",
    "FriendsAreFriendsResponse",
    "FriendsDeleteResponse",
    "FriendsDeleteResponseModel",
    "FriendsGetAppUsersResponse",
    "FriendsGetFieldsResponse",
    "FriendsGetFieldsResponseModel",
    "FriendsGetListsResponse",
    "FriendsGetListsResponseModel",
    "FriendsGetMutualResponse",
    "FriendsGetMutualTargetUidsResponse",
    "FriendsGetMutualTotalCountResponse",
    "FriendsGetOnlineExtendedResponse",
    "FriendsGetOnlineOnlineMobileExtendedResponse",
    "FriendsGetOnlineOnlineMobileResponse",
    "FriendsGetOnlineOnlineMobileResponseModel",
    "FriendsGetOnlineResponse",
    "FriendsGetRecentResponse",
    "FriendsGetRequestsExtendedResponse",
    "FriendsGetRequestsExtendedResponseModel",
    "FriendsGetRequestsNeedMutualResponse",
    "FriendsGetRequestsNeedMutualResponseModel",
    "FriendsGetRequestsResponse",
    "FriendsGetRequestsResponseModel",
    "FriendsGetResponse",
    "FriendsGetResponseModel",
    "FriendsGetSuggestionsResponse",
    "FriendsGetSuggestionsResponseModel",
    "FriendsSearchResponse",
    "FriendsSearchResponseModel",
)
