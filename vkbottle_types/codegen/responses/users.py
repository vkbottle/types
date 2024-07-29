import typing

from vkbottle_types.base_model import Field
from vkbottle_types.objects import UsersUserFull
from vkbottle_types.responses.base_response import BaseResponse


class UsersGetFollowersFieldsResponse(BaseResponse):
    response: typing.Dict[str, typing.Any] = Field()


class UsersGetFollowersResponse(BaseResponse):
    response: typing.Dict[str, typing.Any] = Field()


class UsersGetSubscriptionsExtendedResponse(BaseResponse):
    response: typing.Dict[str, typing.Any] = Field()


class UsersGetSubscriptionsResponse(BaseResponse):
    response: typing.Dict[str, typing.Any] = Field()


class UsersGetResponse(BaseResponse):
    response: typing.List[UsersUserFull] = Field()


class UsersSearchResponse(BaseResponse):
    response: typing.Dict[str, typing.Any] = Field()
