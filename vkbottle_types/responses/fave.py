import typing
from typing import Optional

from vkbottle_types.objects import fave, groups, users
from .base_response import BaseResponse


class AddTagResponse(BaseResponse):
    response: Optional[typing.List["fave.Tag"]] = None


class GetPagesResponse(BaseResponse):
    response: Optional["GetPagesResponseModel"] = None


class GetTagsResponse(BaseResponse):
    response: Optional["GetTagsResponseModel"] = None


class GetExtendedResponse(BaseResponse):
    response: Optional["GetExtendedResponseModel"] = None


class GetResponse(BaseResponse):
    response: Optional["GetResponseModel"] = None


class GetPagesResponseModel(BaseResponse):
    count: Optional[int] = None
    items: Optional[typing.List["fave.Page"]] = None


class GetTagsResponseModel(BaseResponse):
    count: Optional[int] = None
    items: Optional[typing.List["fave.Tag"]] = None


class GetExtendedResponseModel(BaseResponse):
    count: Optional[int] = None
    items: Optional[typing.List["fave.Bookmark"]] = None
    profiles: Optional[typing.List["users.UserFull"]] = None
    groups: Optional[typing.List["groups.Group"]] = None


class GetResponseModel(BaseResponse):
    count: Optional[int] = None
    items: Optional[typing.List["fave.Bookmark"]] = None
