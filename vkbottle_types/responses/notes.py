import inspect
import typing
from .base_response import BaseResponse
from vkbottle_types.objects import NotesNote, NotesNoteComment


class AddResponse(BaseResponse):
    response: int = None


class CreateCommentResponse(BaseResponse):
    response: int = None


class GetByIdResponse(BaseResponse):
    response: NotesNote = None


class GetCommentsResponse(BaseResponse):
    response: "GetCommentsResponseModel" = None


class GetResponse(BaseResponse):
    response: "GetResponseModel" = None


class GetCommentsResponseModel(BaseResponse):
    count: typing.Optional[int] = None
    items: typing.Optional[typing.List["NotesNoteComment"]] = None


class GetResponseModel(BaseResponse):
    count: typing.Optional[int] = None
    items: typing.Optional[typing.List["NotesNote"]] = None


for item in locals().copy().values():
    if inspect.isclass(item) and issubclass(item, BaseResponse):
        item.update_forward_refs()
