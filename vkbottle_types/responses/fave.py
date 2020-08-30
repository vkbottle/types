from .base_response import BaseResponse
from vkbottle_types.objects import fave, groups, users
from typing import Optional, Any, List, Union
import typing


class AddTagResponse(BaseResponse):
    response: Optional["AddTagResponseModel"] = None


class GetPagesResponse(BaseResponse):
    response: Optional["GetPagesResponseModel"] = None


class GetTagsResponse(BaseResponse):
    response: Optional["GetTagsResponseModel"] = None


class GetExtendedResponse(BaseResponse):
    response: Optional["GetExtendedResponseModel"] = None


class GetResponse(BaseResponse):
    response: Optional["GetResponseModel"] = None


AddTagResponseModel = Optional["fave.Tag"]


class GetPagesResponseModel(BaseResponse):
    count: Optional[int] = None
    items: Optional[List["fave.Page"]] = None


class GetTagsResponseModel(BaseResponse):
    count: Optional[int] = None
    items: Optional[List["fave.Tag"]] = None


class GetExtendedResponseModel(BaseResponse):
    count: Optional[int] = None
    items: Optional[List["fave.Bookmark"]] = None
    profiles: Optional[List["users.UserFull"]] = None
    groups: Optional[List["groups.Group"]] = None


class GetResponseModel(BaseResponse):
    count: Optional[int] = None
    items: Optional[List["fave.Bookmark"]] = None
