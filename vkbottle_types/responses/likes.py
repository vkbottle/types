import inspect
import typing
from .base_response import BaseResponse
from vkbottle_types.objects import BaseBoolInt, UsersUserMin


class AddResponse(BaseResponse):
    response: "AddResponseModel" = None


class DeleteResponse(BaseResponse):
    response: "DeleteResponseModel" = None


class GetListExtendedResponse(BaseResponse):
    response: "GetListExtendedResponseModel" = None


class GetListResponse(BaseResponse):
    response: "GetListResponseModel" = None


class IsLikedResponse(BaseResponse):
    response: "IsLikedResponseModel" = None


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
