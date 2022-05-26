import inspect
import typing

from vkbottle_types.objects import NotesNote, NotesNoteComment

from .base_response import BaseResponse


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


for item in locals().copy().values():
    if inspect.isclass(item) and issubclass(item, BaseResponse):
        item.update_forward_refs()


__all__ = (
    "AddResponse",
    "CreateCommentResponse",
    "GetByIdResponse",
    "GetCommentsResponse",
    "GetResponse",
)
