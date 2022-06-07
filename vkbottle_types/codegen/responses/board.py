import typing

from vkbottle_types.objects import (
    BaseBoolInt,
    BoardDefaultOrder,
    BoardTopic,
    BoardTopicComment,
    GroupsGroupFull,
    PollsPoll,
    UsersUserFull,
)
from vkbottle_types.responses.base_response import BaseResponse


class AddTopicResponse(BaseResponse):
    response: int


class CreateCommentResponse(BaseResponse):
    response: int


class GetCommentsExtendedResponse(BaseResponse):
    response: "GetCommentsExtendedResponseModel"


class GetCommentsResponse(BaseResponse):
    response: "GetCommentsResponseModel"


class GetTopicsExtendedResponse(BaseResponse):
    response: "GetTopicsExtendedResponseModel"


class GetTopicsResponse(BaseResponse):
    response: "GetTopicsResponseModel"


class GetCommentsExtendedResponseModel(BaseResponse):
    count: typing.Optional[int] = None
    items: typing.Optional[typing.List["BoardTopicComment"]] = None
    poll: typing.Optional[typing.Any] = None
    profiles: typing.Optional[typing.List["UsersUserFull"]] = None
    groups: typing.Optional[typing.List["GroupsGroupFull"]] = None
    real_offset: typing.Optional[int] = None


class GetCommentsResponseModel(BaseResponse):
    count: typing.Optional[int] = None
    items: typing.Optional[typing.List["BoardTopicComment"]] = None
    poll: typing.Optional[typing.Any] = None
    real_offset: typing.Optional[int] = None


class GetTopicsExtendedResponseModel(BaseResponse):
    count: typing.Optional[int] = None
    items: typing.Optional[typing.List["BoardTopic"]] = None
    default_order: typing.Optional["BoardDefaultOrder"] = None
    can_add_topics: typing.Optional["BaseBoolInt"] = None
    profiles: typing.Optional[typing.List["UsersUserFull"]] = None
    groups: typing.Optional[typing.List["GroupsGroupFull"]] = None


class GetTopicsResponseModel(BaseResponse):
    count: typing.Optional[int] = None
    items: typing.Optional[typing.List["BoardTopic"]] = None
    default_order: typing.Optional["BoardDefaultOrder"] = None
    can_add_topics: typing.Optional["BaseBoolInt"] = None


__all__ = (
    "AddTopicResponse",
    "BaseBoolInt",
    "BoardDefaultOrder",
    "BoardTopic",
    "BoardTopicComment",
    "CreateCommentResponse",
    "GetCommentsExtendedResponse",
    "GetCommentsExtendedResponseModel",
    "GetCommentsResponse",
    "GetCommentsResponseModel",
    "GetTopicsExtendedResponse",
    "GetTopicsExtendedResponseModel",
    "GetTopicsResponse",
    "GetTopicsResponseModel",
    "GroupsGroupFull",
    "PollsPoll",
    "UsersUserFull",
)
