import typing

from vkbottle_types.base_model import BaseModel, Field
from vkbottle_types.objects import GroupsGroupsArray, UsersSubscriptionsItem, UsersUserFull, UsersUsersArray
from vkbottle_types.responses.base_response import BaseResponse


class UsersGetFollowersFieldsResponseModel(BaseModel):
    count: int = Field()
    items: typing.List["UsersUserFull"] = Field()
    friends_count: typing.Optional[int] = Field(
        default=None,
    )


class UsersGetFollowersFieldsResponse(BaseResponse):
    response: "UsersGetFollowersFieldsResponseModel" = Field()


class UsersGetFollowersResponseModel(BaseModel):
    count: int = Field()
    items: typing.List[int] = Field()


class UsersGetFollowersResponse(BaseResponse):
    response: "UsersGetFollowersResponseModel" = Field()


class UsersGetSubscriptionsExtendedResponseModel(BaseModel):
    count: int = Field()
    items: typing.List["UsersSubscriptionsItem"] = Field()


class UsersGetSubscriptionsExtendedResponse(BaseResponse):
    response: "UsersGetSubscriptionsExtendedResponseModel" = Field()


class UsersGetSubscriptionsResponseModel(BaseModel):
    users: "UsersUsersArray" = Field()
    groups: "GroupsGroupsArray" = Field()


class UsersGetSubscriptionsResponse(BaseResponse):
    response: "UsersGetSubscriptionsResponseModel" = Field()


class UsersGetResponse(BaseResponse):
    response: typing.List["UsersUserFull"] = Field()


class UsersSearchResponseModel(BaseModel):
    count: int = Field()
    items: typing.List["UsersUserFull"] = Field()


class UsersSearchResponse(BaseResponse):
    response: "UsersSearchResponseModel" = Field()
