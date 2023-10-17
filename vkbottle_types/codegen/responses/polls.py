import typing
from vkbottle_types.responses.base_response import BaseResponse, BaseModel
from vkbottle_types.base_model import Field

from vkbottle_types.objects import (
    PollsFriend,
    PollsBackground,
    BaseGradientPoint,
    PollsVotersUsers,
    BaseImage,
    UsersUserFull,
    PollsAnswer,
    PollsVotersFieldsUsers,
    PollsPollAnonymous,
)


class PollsAnswerResponseModel(BaseModel):
    id: int = Field(
        description="Answer ID",
    )

    rate: float = Field(
        description="Answer rate in percents",
    )

    text: str = Field(
        description="Answer text",
    )

    votes: int = Field(
        description="Votes number",
    )


class PollsAnswerResponse(BaseResponse):
    response: "PollsAnswerResponseModel"


class PollsBackgroundResponseModel(BaseModel):
    angle: typing.Optional[int] = Field(
        default=None,
        description="Gradient angle with 0 on positive X axis",
    )

    color: typing.Optional[str] = Field(
        default=None,
        description="Hex color code without #",
    )

    height: typing.Optional[int] = Field(
        default=None,
        description="Original height of pattern tile",
    )

    id: typing.Optional[int] = Field(
        default=None,
    )

    name: typing.Optional[str] = Field(
        default=None,
    )

    images: typing.Optional[typing.List[BaseImage]] = Field(
        default=None,
        description="Pattern tiles",
    )

    points: typing.Optional[typing.List[BaseGradientPoint]] = Field(
        default=None,
        description="Gradient points",
    )

    type: typing.Optional[typing.Literal["gradient", "tile"]] = Field(
        default=None,
    )

    width: typing.Optional[int] = Field(
        default=None,
        description="Original with of pattern tile",
    )


class PollsBackgroundResponse(BaseResponse):
    response: "PollsBackgroundResponseModel"


class PollsFieldsVotersResponseModel(BaseModel):
    answer_id: typing.Optional[int] = Field(
        default=None,
        description="Answer ID",
    )

    users: typing.Optional["PollsVotersFieldsUsers"] = Field(
        default=None,
    )

    answer_offset: typing.Optional[str] = Field(
        default=None,
        description="Answer offset",
    )


class PollsFieldsVotersResponse(BaseResponse):
    response: "PollsFieldsVotersResponseModel"


class PollsFriendResponseModel(BaseModel):
    id: int = Field()


class PollsFriendResponse(BaseResponse):
    response: "PollsFriendResponseModel"


class PollsPollResponseModel(BaseModel):
    multiple: bool = Field(
        description="Information whether the poll with multiple choices",
    )

    end_date: int = Field()

    closed: bool = Field()

    is_board: bool = Field()

    can_edit: bool = Field()

    can_vote: bool = Field()

    can_report: bool = Field()

    can_share: bool = Field()

    answers: typing.List[PollsAnswer] = Field()

    created: int = Field(
        description="Date when poll has been created in Unixtime",
    )

    id: int = Field(
        description="Poll ID",
    )

    owner_id: int = Field(
        description="Poll owner's ID",
    )

    question: str = Field(
        description="Poll question",
    )

    votes: int = Field(
        description="Votes number",
    )

    disable_unvote: bool = Field()

    anonymous: typing.Optional["PollsPollAnonymous"] = Field(
        default=None,
    )

    friends: typing.Optional[typing.List[PollsFriend]] = Field(
        default=None,
    )

    answer_id: typing.Optional[int] = Field(
        default=None,
        description="Current user's answer ID",
    )

    answer_ids: typing.Optional[typing.List[int]] = Field(
        default=None,
        description="Current user's answer IDs",
    )

    embed_hash: typing.Optional[str] = Field(
        default=None,
    )

    photo: typing.Optional["PollsBackground"] = Field(
        default=None,
    )

    author_id: typing.Optional[int] = Field(
        default=None,
        description="Poll author's ID",
    )

    background: typing.Optional["PollsBackground"] = Field(
        default=None,
    )


class PollsPollResponse(BaseResponse):
    response: "PollsPollResponseModel"


PollsPollAnonymousResponseModel = bool


class PollsPollAnonymousResponse(BaseResponse):
    response: "PollsPollAnonymousResponseModel"


class PollsVotersResponseModel(BaseModel):
    answer_id: typing.Optional[int] = Field(
        default=None,
        description="Answer ID",
    )

    users: typing.Optional["PollsVotersUsers"] = Field(
        default=None,
    )

    answer_offset: typing.Optional[str] = Field(
        default=None,
        description="Answer offset",
    )


class PollsVotersResponse(BaseResponse):
    response: "PollsVotersResponseModel"


class PollsVotersFieldsUsersResponseModel(BaseModel):
    count: typing.Optional[int] = Field(
        default=None,
        description="Votes number",
    )

    items: typing.Optional[typing.List[UsersUserFull]] = Field(
        default=None,
    )


class PollsVotersFieldsUsersResponse(BaseResponse):
    response: "PollsVotersFieldsUsersResponseModel"


class PollsVotersUsersResponseModel(BaseModel):
    count: typing.Optional[int] = Field(
        default=None,
        description="Votes number",
    )

    items: typing.Optional[typing.List[int]] = Field(
        default=None,
    )


class PollsVotersUsersResponse(BaseResponse):
    response: "PollsVotersUsersResponseModel"
