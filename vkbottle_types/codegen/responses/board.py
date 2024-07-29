import typing

from vkbottle_types.base_model import Field
from vkbottle_types.responses.base_response import BaseResponse


class BoardAddTopicResponse(BaseResponse):
    response: int = Field()


class BoardCreateCommentResponse(BaseResponse):
    response: int = Field()


class BoardGetCommentsExtendedResponse(BaseResponse):
    response: typing.Dict[str, typing.Any] = Field()


class BoardGetCommentsResponse(BaseResponse):
    response: typing.Dict[str, typing.Any] = Field()


class BoardGetTopicsExtendedResponse(BaseResponse):
    response: typing.Dict[str, typing.Any] = Field()


class BoardGetTopicsResponse(BaseResponse):
    response: typing.Dict[str, typing.Any] = Field()
