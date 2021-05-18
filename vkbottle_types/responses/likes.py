import inspect
import typing

from vkbottle_types.objects import BaseBoolInt, UsersUserMin

from .base_response import BaseResponse


class AddResponse(BaseResponse):
    response: typing.Optional["AddResponseModel"] = None


class DeleteResponse(BaseResponse):
    response: typing.Optional["DeleteResponseModel"] = None


class GetListExtendedResponse(BaseResponse):
    response: typing.Optional["GetListExtendedResponseModel"] = None


class GetListResponse(BaseResponse):
    response: typing.Optional["GetListResponseModel"] = None


class IsLikedResponse(BaseResponse):
    response: typing.Optional["IsLikedResponseModel"] = None


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
