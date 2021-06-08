import inspect
import typing
from .base_response import BaseResponse
from vkbottle_types.objects import (
    BaseBoolInt,
    BoardDefaultOrder,
    BoardTopic,
    BoardTopicComment,
    BoardTopicPoll,
    GroupsGroup,
    UsersUser,
    UsersUserMin
)


class AddTopicResponse(BaseResponse):
    response: int = None


class CreateCommentResponse(BaseResponse):
    response: int = None


class GetCommentsExtendedResponse(BaseResponse):
    response: "GetCommentsExtendedResponseModel" = None


class GetCommentsResponse(BaseResponse):
    response: "GetCommentsResponseModel" = None


class GetTopicsExtendedResponse(BaseResponse):
    response: "GetTopicsExtendedResponseModel" = None


class GetTopicsResponse(BaseResponse):
    response: "GetTopicsResponseModel" = None


class GetCommentsExtendedResponseModel(BaseResponse):
    count: typing.Optional[int] = None
    items: typing.Optional[typing.List["BoardTopicComment"]] = None
    poll: typing.Optional["BoardTopicPoll"] = None
    profiles: typing.Optional[typing.List["UsersUser"]] = None
    groups: typing.Optional[typing.List["GroupsGroup"]] = None


class GetCommentsResponseModel(BaseResponse):
    count: typing.Optional[int] = None
    items: typing.Optional[typing.List["BoardTopicComment"]] = None
    poll: typing.Optional["BoardTopicPoll"] = None


class GetTopicsExtendedResponseModel(BaseResponse):
    count: typing.Optional[int] = None
    items: typing.Optional[typing.List["BoardTopic"]] = None
    default_order: typing.Optional["BoardDefaultOrder"] = None
    can_add_topics: typing.Optional["BaseBoolInt"] = None
    profiles: typing.Optional[typing.List["UsersUserMin"]] = None


class GetTopicsResponseModel(BaseResponse):
    count: typing.Optional[int] = None
    items: typing.Optional[typing.List["BoardTopic"]] = None
    default_order: typing.Optional["BoardDefaultOrder"] = None
    can_add_topics: typing.Optional["BaseBoolInt"] = None


for item in locals().copy().values():
    if inspect.isclass(item) and issubclass(item, BaseResponse):
        item.update_forward_refs()
