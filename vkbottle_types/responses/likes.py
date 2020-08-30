from typing import Optional, List

from vkbottle_types.objects import UsersUserMin, BaseBoolInt
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
    items: Optional[List["UsersUserMin"]] = None


class GetListResponseModel(BaseResponse):
    count: Optional[int] = None
    items: Optional[List[int]] = None


class IsLikedResponseModel(BaseResponse):
    liked: Optional["BaseBoolInt"] = None
    copied: Optional["BaseBoolInt"] = None


AddResponse.update_forward_refs()
DeleteResponse.update_forward_refs()
GetListExtendedResponse.update_forward_refs()
GetListResponse.update_forward_refs()
IsLikedResponse.update_forward_refs()
