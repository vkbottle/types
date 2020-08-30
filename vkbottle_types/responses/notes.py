from .base_response import BaseResponse
from vkbottle_types.objects import notes
from typing import Optional, Any, List, Union
import typing


class AddResponse(BaseResponse):
    response: Optional["AddResponseModel"] = None


class CreateCommentResponse(BaseResponse):
    response: Optional["CreateCommentResponseModel"] = None


class GetByIdResponse(BaseResponse):
    response: Optional["GetByIdResponseModel"] = None


class GetCommentsResponse(BaseResponse):
    response: Optional["GetCommentsResponseModel"] = None


class GetResponse(BaseResponse):
    response: Optional["GetResponseModel"] = None


AddResponseModel = int


CreateCommentResponseModel = int


GetByIdResponseModel = Optional["notes.Note"]


class GetCommentsResponseModel(BaseResponse):
    count: Optional[int] = None
    items: Optional[List["notes.NoteComment"]] = None


class GetResponseModel(BaseResponse):
    count: Optional[int] = None
    items: Optional[List["notes.Note"]] = None
