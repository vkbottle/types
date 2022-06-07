import typing

from vkbottle_types.objects import BaseBoolInt, UsersUserMin
from vkbottle_types.responses.base_response import BaseResponse


class AddResponse(BaseResponse):
    response: "AddResponseModel"


class DeleteResponse(BaseResponse):
    response: "DeleteResponseModel"


class GetListExtendedResponse(BaseResponse):
    response: "GetListExtendedResponseModel"


class GetListResponse(BaseResponse):
    response: "GetListResponseModel"


class IsLikedResponse(BaseResponse):
    response: "IsLikedResponseModel"


class AddResponseModel(BaseResponse):
    likes: typing.Optional[int] = None


class DeleteResponseModel(BaseResponse):
    likes: typing.Optional[int] = None


class GetListExtendedResponseModel(BaseResponse):
    count: typing.Optional[int] = None
    items: typing.Optional[typing.List["UsersUserMin"]] = None


class GetListResponseModel(BaseResponse):
    count: typing.Optional[int] = None
    items: typing.Optional[typing.List[int]] = None


class IsLikedResponseModel(BaseResponse):
    liked: typing.Optional["BaseBoolInt"] = None
    copied: typing.Optional["BaseBoolInt"] = None


__all__ = (
    "AddResponse",
    "AddResponseModel",
    "BaseBoolInt",
    "DeleteResponse",
    "DeleteResponseModel",
    "GetListExtendedResponse",
    "GetListExtendedResponseModel",
    "GetListResponse",
    "GetListResponseModel",
    "IsLikedResponse",
    "IsLikedResponseModel",
    "UsersUserMin",
)
