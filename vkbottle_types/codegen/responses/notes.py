import typing

from vkbottle_types.objects import NotesNote, NotesNoteComment
from vkbottle_types.responses.base_response import BaseResponse


class AddResponse(BaseResponse):
    response: int


class CreateCommentResponse(BaseResponse):
    response: int


class GetByIdResponse(BaseResponse):
    response: NotesNote


class GetCommentsResponse(BaseResponse):
    response: "GetCommentsResponseModel"


class GetResponse(BaseResponse):
    response: "GetResponseModel"


class GetCommentsResponseModel(BaseResponse):
    count: typing.Optional[int] = None
    items: typing.Optional[typing.List["NotesNoteComment"]] = None


class GetResponseModel(BaseResponse):
    count: typing.Optional[int] = None
    items: typing.Optional[typing.List["NotesNote"]] = None


__all__ = (
    "AddResponse",
    "CreateCommentResponse",
    "GetByIdResponse",
    "GetCommentsResponse",
    "GetCommentsResponseModel",
    "GetResponse",
    "GetResponseModel",
    "NotesNote",
    "NotesNoteComment",
)
