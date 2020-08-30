from .base_response import BaseResponse
from vkbottle_types.objects import users, board, base, groups
from typing import Optional, Any, List, Union
import typing


class AddTopicResponse(BaseResponse):
    response: Optional["AddTopicResponseModel"] = None


class CreateCommentResponse(BaseResponse):
    response: Optional["CreateCommentResponseModel"] = None


class GetCommentsExtendedResponse(BaseResponse):
    response: Optional["GetCommentsExtendedResponseModel"] = None


class GetCommentsResponse(BaseResponse):
    response: Optional["GetCommentsResponseModel"] = None


class GetTopicsExtendedResponse(BaseResponse):
    response: Optional["GetTopicsExtendedResponseModel"] = None


class GetTopicsResponse(BaseResponse):
    response: Optional["GetTopicsResponseModel"] = None


AddTopicResponseModel = int


CreateCommentResponseModel = int


class GetCommentsExtendedResponseModel(BaseResponse):
    count: Optional[int] = None
    items: Optional[List["board.TopicComment"]] = None
    poll: Optional["board.TopicPoll"] = None
    profiles: Optional[List["users.User"]] = None
    groups: Optional[List["groups.Group"]] = None


class GetCommentsResponseModel(BaseResponse):
    count: Optional[int] = None
    items: Optional[List["board.TopicComment"]] = None
    poll: Optional["board.TopicPoll"] = None


class GetTopicsExtendedResponseModel(BaseResponse):
    count: Optional[int] = None
    items: Optional[List["board.Topic"]] = None
    default_order: Optional["board.DefaultOrder"] = None
    can_add_topics: Optional["base.BoolInt"] = None
    profiles: Optional[List["users.UserMin"]] = None


class GetTopicsResponseModel(BaseResponse):
    count: Optional[int] = None
    items: Optional[List["board.Topic"]] = None
    default_order: Optional["board.DefaultOrder"] = None
    can_add_topics: Optional["base.BoolInt"] = None
