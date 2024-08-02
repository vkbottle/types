import typing

from vkbottle_types.base_model import BaseModel, Field
from vkbottle_types.objects import NotesNote, NotesNoteComment
from vkbottle_types.responses.base_response import BaseResponse


class NotesAddResponse(BaseResponse):
    response: int = Field()


class NotesCreateCommentResponse(BaseResponse):
    response: int = Field()


class NotesGetByIdResponse(BaseResponse):
    response: "NotesNote" = Field()


class NotesGetCommentsResponseModel(BaseModel):
    count: int = Field()
    items: typing.List["NotesNoteComment"] = Field()


class NotesGetCommentsResponse(BaseResponse):
    response: "NotesGetCommentsResponseModel" = Field()


class NotesGetResponseModel(BaseModel):
    count: int = Field()
    items: typing.List["NotesNote"] = Field()


class NotesGetResponse(BaseResponse):
    response: "NotesGetResponseModel" = Field()
