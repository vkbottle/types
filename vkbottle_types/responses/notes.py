import inspect
import typing
from .base_response import BaseResponse
from vkbottle_types.objects import NotesNote, NotesNoteComment


class AddResponse(BaseResponse):
    response: typing.Optional["AddResponseModel"] = None


class CreateCommentResponse(BaseResponse):
    response: typing.Optional["CreateCommentResponseModel"] = None


class GetByIdResponse(BaseResponse):
    response: typing.Optional["GetByIdResponseModel"] = None


class GetCommentsResponse(BaseResponse):
    response: typing.Optional["GetCommentsResponseModel"] = None


class GetResponse(BaseResponse):
    response: typing.Optional["GetResponseModel"] = None


AddResponseModel = int


CreateCommentResponseModel = int


GetByIdResponseModel = NotesNote


class GetCommentsResponseModel(BaseResponse):
    count: typing.Optional[int] = None
    items: typing.Optional[typing.List["NotesNoteComment"]] = None


class GetResponseModel(BaseResponse):
    count: typing.Optional[int] = None
    items: typing.Optional[typing.List["NotesNote"]] = None


for item in locals().copy().values():
    if inspect.isclass(item) and issubclass(item, BaseResponse):
        item.update_forward_refs()
