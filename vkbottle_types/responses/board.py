from typing import Optional, List

from vkbottle_types.objects import (
    BoardTopicComment,
    UsersUserMin,
    UsersUser,
    GroupsGroup,
    BaseBoolInt,
    BoardTopicPoll,
    BoardDefaultOrder,
    BoardTopic,
)
from .base_response import BaseResponse


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
    items: Optional[List["BoardTopicComment"]] = None
    poll: Optional["BoardTopicPoll"] = None
    profiles: Optional[List["UsersUser"]] = None
    groups: Optional[List["GroupsGroup"]] = None


class GetCommentsResponseModel(BaseResponse):
    count: Optional[int] = None
    items: Optional[List["BoardTopicComment"]] = None
    poll: Optional["BoardTopicPoll"] = None


class GetTopicsExtendedResponseModel(BaseResponse):
    count: Optional[int] = None
    items: Optional[List["BoardTopic"]] = None
    default_order: Optional["BoardDefaultOrder"] = None
    can_add_topics: Optional["BaseBoolInt"] = None
    profiles: Optional[List["UsersUserMin"]] = None


class GetTopicsResponseModel(BaseResponse):
    count: Optional[int] = None
    items: Optional[List["BoardTopic"]] = None
    default_order: Optional["BoardDefaultOrder"] = None
    can_add_topics: Optional["BaseBoolInt"] = None

AddTopicResponse.update_forward_refs()
CreateCommentResponse.update_forward_refs()
GetCommentsExtendedResponse.update_forward_refs()
GetCommentsResponse.update_forward_refs()
GetTopicsExtendedResponse.update_forward_refs()
GetTopicsResponse.update_forward_refs()
