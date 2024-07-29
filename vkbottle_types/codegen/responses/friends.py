import enum
import typing

from vkbottle_types.base_model import Field
from vkbottle_types.objects import (
    FriendsFriendExtendedStatus,
    FriendsFriendStatus,
    FriendsMutualFriend,
    FriendsOnlineUsers,
    FriendsOnlineUsersWithMobile,
)
from vkbottle_types.responses.base_response import BaseResponse


class FriendsAddListResponse(BaseResponse):
    response: typing.Dict[str, typing.Any] = Field()


class FriendsAddResponseModel(enum.IntEnum):
    SEND = 1
    APPROVED = 2
    RESEND = 4


class FriendsAddResponse(BaseResponse):
    response: "FriendsAddResponseModel" = Field()


class FriendsAreFriendsExtendedResponse(BaseResponse):
    response: typing.List[FriendsFriendExtendedStatus] = Field()


class FriendsAreFriendsResponse(BaseResponse):
    response: typing.List[FriendsFriendStatus] = Field()


class FriendsDeleteResponse(BaseResponse):
    response: typing.Dict[str, typing.Any] = Field()


class FriendsGetAppUsersResponse(BaseResponse):
    response: typing.List[int] = Field()


class FriendsGetListsResponse(BaseResponse):
    response: typing.Dict[str, typing.Any] = Field()


class FriendsGetMutualResponse(BaseResponse):
    response: typing.List[int] = Field()


class FriendsGetMutualTargetUidsResponse(BaseResponse):
    response: typing.List[FriendsMutualFriend] = Field()


class FriendsGetMutualTotalCountResponse(BaseResponse):
    response: "FriendsMutualFriend" = Field()


class FriendsGetOnlineExtendedResponse(BaseResponse):
    response: "FriendsOnlineUsers" = Field()


class FriendsGetOnlineOnlineMobileExtendedResponse(BaseResponse):
    response: "FriendsOnlineUsersWithMobile" = Field()


class FriendsGetOnlineOnlineMobileResponse(BaseResponse):
    response: typing.Dict[str, typing.Any] = Field()


class FriendsGetOnlineResponse(BaseResponse):
    response: typing.List[int] = Field()


class FriendsGetRecentResponse(BaseResponse):
    response: typing.List[int] = Field()


class FriendsGetRequestsExtendedResponse(BaseResponse):
    response: typing.Dict[str, typing.Any] = Field()


class FriendsGetRequestsNeedMutualResponse(BaseResponse):
    response: typing.Dict[str, typing.Any] = Field()


class FriendsGetRequestsResponse(BaseResponse):
    response: typing.Dict[str, typing.Any] = Field()


class FriendsGetSuggestionsResponse(BaseResponse):
    response: typing.Dict[str, typing.Any] = Field()


class FriendsGetFieldsResponse(BaseResponse):
    response: typing.Dict[str, typing.Any] = Field()


class FriendsGetResponse(BaseResponse):
    response: typing.Dict[str, typing.Any] = Field()


class FriendsSearchResponse(BaseResponse):
    response: typing.Dict[str, typing.Any] = Field()
