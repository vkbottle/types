import typing

from vkbottle_types.base_model import Field
from vkbottle_types.responses.base_response import BaseResponse


class LikesAddResponse(BaseResponse):
    response: typing.Dict[str, typing.Any] = Field()


class LikesDeleteResponse(BaseResponse):
    response: typing.Dict[str, typing.Any] = Field()


class LikesGetListExtendedResponse(BaseResponse):
    response: typing.Dict[str, typing.Any] = Field()


class LikesGetListResponse(BaseResponse):
    response: typing.Dict[str, typing.Any] = Field()


class LikesIsLikedResponse(BaseResponse):
    response: typing.Dict[str, typing.Any] = Field()
