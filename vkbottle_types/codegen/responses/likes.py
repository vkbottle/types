import inspect
import typing

from vkbottle_types.objects import BaseBoolInt, UsersUserMin

from .base_response import BaseResponse


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


for item in locals().copy().values():
    if inspect.isclass(item) and issubclass(item, BaseResponse):
        item.update_forward_refs()


__all__ = (
    "AddResponse",
    "DeleteResponse",
    "GetListExtendedResponse",
    "GetListResponse",
    "IsLikedResponse",
)
