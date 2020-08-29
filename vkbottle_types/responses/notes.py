import typing
from typing import Optional

from vkbottle_types.objects import notes
from .base_response import BaseResponse


class AddResponse(BaseResponse):
    response: Optional[int] = None


class CreateCommentResponse(BaseResponse):
    response: Optional[int] = None


class GetByIdResponse(BaseResponse):
    response: Optional[typing.List["notes.Note"]] = None


class GetCommentsResponse(BaseResponse):
    response: Optional["GetCommentsResponseModel"] = None


class GetResponse(BaseResponse):
    response: Optional["GetResponseModel"] = None


class GetCommentsResponseModel(BaseResponse):
    count: Optional[int] = None
    items: Optional[typing.List["notes.NoteComment"]] = None


class GetResponseModel(BaseResponse):
    count: Optional[int] = None
    items: Optional[typing.List["notes.Note"]] = None
