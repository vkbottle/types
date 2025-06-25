import typing

from vkbottle_types.base_model import BaseModel, Field
from vkbottle_types.objects import BoardDefaultOrder, BoardTopic, BoardTopicComment, GroupsGroupFull, UsersUserFull
from vkbottle_types.responses.base_response import BaseResponse


class BoardAddTopicResponse(BaseResponse):
    response: int = Field()


class BoardCreateCommentResponse(BaseResponse):
    response: int = Field()


class BoardGetCommentsExtendedResponseModel(BaseModel):
    count: int = Field()
    items: typing.List["BoardTopicComment"] = Field()
    profiles: typing.List["UsersUserFull"] = Field()
    groups: typing.List["GroupsGroupFull"] = Field()
    poll: typing.Optional[dict] = Field(
        default=None,
    )
    real_offset: typing.Optional[int] = Field(
        default=None,
    )


class BoardGetCommentsExtendedResponse(BaseResponse):
    response: "BoardGetCommentsExtendedResponseModel" = Field()


class BoardGetCommentsResponseModel(BaseModel):
    count: int = Field()
    items: typing.List["BoardTopicComment"] = Field()
    poll: typing.Optional[dict] = Field(
        default=None,
    )
    real_offset: typing.Optional[int] = Field(
        default=None,
    )


class BoardGetCommentsResponse(BaseResponse):
    response: "BoardGetCommentsResponseModel" = Field()


class BoardGetTopicsExtendedResponseModel(BaseModel):
    count: int = Field()
    items: typing.List["BoardTopic"] = Field()
    default_order: "BoardDefaultOrder" = Field()
    can_add_topics: bool = Field()
    profiles: typing.List["UsersUserFull"] = Field()
    groups: typing.List["GroupsGroupFull"] = Field()


class BoardGetTopicsExtendedResponse(BaseResponse):
    response: "BoardGetTopicsExtendedResponseModel" = Field()


class BoardGetTopicsResponseModel(BaseModel):
    count: int = Field()
    items: typing.List["BoardTopic"] = Field()
    default_order: "BoardDefaultOrder" = Field()
    can_add_topics: bool = Field()


class BoardGetTopicsResponse(BaseResponse):
    response: "BoardGetTopicsResponseModel" = Field()
