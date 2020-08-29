import typing
from typing import Optional

from vkbottle_types.objects import base, users
from .base_response import BaseResponse


class AddResponse(BaseResponse):
    response: Optional["AddResponseModel"] = None


class DeleteResponse(BaseResponse):
    response: Optional["DeleteResponseModel"] = None


class GetListExtendedResponse(BaseResponse):
    response: Optional["GetListExtendedResponseModel"] = None


class GetListResponse(BaseResponse):
    response: Optional["GetListResponseModel"] = None


class IsLikedResponse(BaseResponse):
    response: Optional["IsLikedResponseModel"] = None


class AddResponseModel(BaseResponse):
    likes: Optional[int] = None


class DeleteResponseModel(BaseResponse):
    likes: Optional[int] = None


class GetListExtendedResponseModel(BaseResponse):
    count: Optional[int] = None
    items: Optional[typing.List["users.UserMin"]] = None


class GetListResponseModel(BaseResponse):
    count: Optional[int] = None
    items: Optional[typing.List[int]] = None


class IsLikedResponseModel(BaseResponse):
    liked: Optional[typing.List["base.BoolInt"]] = None
    copied: Optional[typing.List["base.BoolInt"]] = None
