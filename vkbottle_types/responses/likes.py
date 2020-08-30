from .base_response import BaseResponse
from vkbottle_types.objects import users, base
from typing import Optional, Any, List, Union
import typing


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
    items: Optional[List["users.UserMin"]] = None


class GetListResponseModel(BaseResponse):
    count: Optional[int] = None
    items: Optional[List[int]] = None


class IsLikedResponseModel(BaseResponse):
    liked: Optional["base.BoolInt"] = None
    copied: Optional["base.BoolInt"] = None
