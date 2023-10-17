import typing
import enum
from vkbottle_types.responses.base_response import BaseResponse, BaseModel
from vkbottle_types.base_model import Field

from vkbottle_types.objects import FriendsRequestsMutual, FriendsFriendStatusStatus


class FriendsFriendExtendedStatusResponseModel(FriendsFriendStatus):
    is_request_unread: typing.Optional[bool] = Field(
        default=None,
        description="Is friend request from other user unread",
    )


class FriendsFriendExtendedStatusResponse(BaseResponse):
    response: "FriendsFriendExtendedStatusResponseModel"


class FriendsFriendStatusResponseModel(BaseModel):
    friend_status: "FriendsFriendStatusStatus" = Field()

    user_id: int = Field(
        description="User ID",
    )

    sign: typing.Optional[str] = Field(
        default=None,
        description="MD5 hash for the result validation",
    )


class FriendsFriendStatusResponse(BaseResponse):
    response: "FriendsFriendStatusResponseModel"


class FriendsFriendStatusStatusResponseModel(enum.IntEnum):
    NOT_A_FRIEND = 0

    OUTCOMING_REQUEST = 1

    INCOMING_REQUEST = 2

    IS_FRIEND = 3


class FriendsFriendStatusStatusResponse(BaseResponse):
    response: "FriendsFriendStatusStatusResponseModel"


class FriendsFriendsListResponseModel(BaseModel):
    id: int = Field(
        description="List ID",
    )

    name: str = Field(
        description="List title",
    )


class FriendsFriendsListResponse(BaseResponse):
    response: "FriendsFriendsListResponseModel"


class FriendsMutualFriendResponseModel(BaseModel):
    common_count: typing.Optional[int] = Field(
        default=None,
        description="Total mutual friends number",
    )

    common_friends: typing.Optional[typing.List[int]] = Field(
        default=None,
    )

    id: typing.Optional[int] = Field(
        default=None,
        description="User ID",
    )


class FriendsMutualFriendResponse(BaseResponse):
    response: "FriendsMutualFriendResponseModel"


class FriendsRequestsMutualResponseModel(BaseModel):
    count: typing.Optional[int] = Field(
        default=None,
        description="Total mutual friends number",
    )

    users: typing.Optional[typing.List[int]] = Field(
        default=None,
    )


class FriendsRequestsMutualResponse(BaseResponse):
    response: "FriendsRequestsMutualResponseModel"


class FriendsRequestsXtrMessageResponseModel(FriendsRequestsXtrMutual):
    message: typing.Optional[str] = Field(
        default=None,
        description="Message sent with a request",
    )


class FriendsRequestsXtrMessageResponse(BaseResponse):
    response: "FriendsRequestsXtrMessageResponseModel"


class FriendsRequestsXtrMutualResponseModel(UsersUserFull):
    user_id: int = Field(
        description="User ID",
    )

    id: typing.Optional[int] = Field(
        default=None,
        description="User ID",
    )

    _from: typing.Optional[str] = Field(
        default=None,
        description="ID of the user by whom friend has been suggested",
        alias="from",
    )

    mutual: typing.Optional["FriendsRequestsMutual"] = Field(
        default=None,
    )

    track_code: typing.Optional[str] = Field(
        default=None,
    )

    message: typing.Optional[str] = Field(
        default=None,
        description="Message sent with a request",
    )

    timestamp: typing.Optional[int] = Field(
        default=None,
        description="Request timestamp",
    )

    descriptions: typing.Optional[typing.List[str]] = Field(
        default=None,
    )


class FriendsRequestsXtrMutualResponse(BaseResponse):
    response: "FriendsRequestsXtrMutualResponseModel"


class FriendsUserXtrPhoneResponseModel(UsersUserFull):
    phone: typing.Optional[str] = Field(
        default=None,
        description="User phone",
    )


class FriendsUserXtrPhoneResponse(BaseResponse):
    response: "FriendsUserXtrPhoneResponseModel"
