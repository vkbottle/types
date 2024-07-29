import typing

from vkbottle_types.base_model import Field
from vkbottle_types.objects import NotesNote
from vkbottle_types.responses.base_response import BaseResponse


class NotesAddResponse(BaseResponse):
    response: int = Field()


class NotesCreateCommentResponse(BaseResponse):
    response: int = Field()


class NotesGetByIdResponse(BaseResponse):
    response: "NotesNote" = Field()


class NotesGetCommentsResponse(BaseResponse):
    response: typing.Dict[str, typing.Any] = Field()


class NotesGetResponse(BaseResponse):
    response: typing.Dict[str, typing.Any] = Field()
