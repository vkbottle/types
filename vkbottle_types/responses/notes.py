from typing import Optional, List

from vkbottle_types.objects import NotesNoteComment, NotesNote
from .base_response import BaseResponse


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

GetByIdResponseModel = Optional[NotesNote]


class GetCommentsResponseModel(BaseResponse):
    count: Optional[int] = None
    items: Optional[List["NotesNoteComment"]] = None


class GetResponseModel(BaseResponse):
    count: Optional[int] = None
    items: Optional[List["NotesNote"]] = None

AddResponse.update_forward_refs()
CreateCommentResponse.update_forward_refs()
GetByIdResponse.update_forward_refs()
GetCommentsResponse.update_forward_refs()
GetResponse.update_forward_refs()
