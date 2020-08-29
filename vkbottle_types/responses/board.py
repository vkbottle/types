import typing
from typing import Optional

from vkbottle_types.objects import board, groups, base, users
from .base_response import BaseResponse


class AddTopicResponse(BaseResponse):
    response: Optional[int] = None


class CreateCommentResponse(BaseResponse):
    response: Optional[int] = None


class GetCommentsExtendedResponse(BaseResponse):
    response: Optional["GetCommentsExtendedResponseModel"] = None


class GetCommentsResponse(BaseResponse):
    response: Optional["GetCommentsResponseModel"] = None


class GetTopicsExtendedResponse(BaseResponse):
    response: Optional["GetTopicsExtendedResponseModel"] = None


class GetTopicsResponse(BaseResponse):
    response: Optional["GetTopicsResponseModel"] = None


class GetCommentsExtendedResponseModel(BaseResponse):
    count: Optional[int] = None
    items: Optional[typing.List["board.TopicComment"]] = None
    poll: Optional[typing.List["board.TopicPoll"]] = None
    profiles: Optional[typing.List["users.User"]] = None
    groups: Optional[typing.List["groups.Group"]] = None


class GetCommentsResponseModel(BaseResponse):
    count: Optional[int] = None
    items: Optional[typing.List["board.TopicComment"]] = None
    poll: Optional[typing.List["board.TopicPoll"]] = None


class GetTopicsExtendedResponseModel(BaseResponse):
    count: Optional[int] = None
    items: Optional[typing.List["board.Topic"]] = None
    default_order: Optional[typing.List["board.DefaultOrder"]] = None
    can_add_topics: Optional[typing.List["base.BoolInt"]] = None
    profiles: Optional[typing.List["users.UserMin"]] = None


class GetTopicsResponseModel(BaseResponse):
    count: Optional[int] = None
    items: Optional[typing.List["board.Topic"]] = None
    default_order: Optional[typing.List["board.DefaultOrder"]] = None
    can_add_topics: Optional[typing.List["base.BoolInt"]] = None
