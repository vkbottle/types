import typing
import enum
from vkbottle_types.responses.base_response import BaseResponse, BaseModel
from vkbottle_types.base_model import Field

from vkbottle_types.objects import BaseBoolInt


class NotesNoteResponseModel(BaseModel):
    comments: int = Field(
        description="Comments number",
    )

    date: int = Field(
        description="Date when the note has been created in Unixtime",
    )

    id: int = Field(
        description="Note ID",
    )

    owner_id: int = Field(
        description="Note owner's ID",
    )

    title: str = Field(
        description="Note title",
    )

    view_url: str = Field(
        description="URL of the page with note preview",
    )

    read_comments: typing.Optional[int] = Field(
        default=None,
    )

    can_comment: typing.Optional[bool] = Field(
        default=None,
        description="Information whether current user can comment the note",
    )

    text: typing.Optional[str] = Field(
        default=None,
        description="Note text",
    )

    text_wiki: typing.Optional[str] = Field(
        default=None,
        description="Note text in wiki format",
    )

    privacy_view: typing.Optional[typing.List[str]] = Field(
        default=None,
    )

    privacy_comment: typing.Optional[typing.List[str]] = Field(
        default=None,
    )


class NotesNoteResponse(BaseResponse):
    response: "NotesNoteResponseModel"


class NotesNoteCommentResponseModel(BaseModel):
    date: int = Field(
        description="Date when the comment has beed added in Unixtime",
    )

    id: int = Field(
        description="Comment ID",
    )

    message: str = Field(
        description="Comment text",
    )

    nid: int = Field(
        description="Note ID",
    )

    oid: int = Field(
        description="Note ID",
    )

    uid: int = Field(
        description="Comment author's ID",
    )

    reply_to: typing.Optional[int] = Field(
        default=None,
        description="ID of replied comment ",
    )


class NotesNoteCommentResponse(BaseResponse):
    response: "NotesNoteCommentResponseModel"
