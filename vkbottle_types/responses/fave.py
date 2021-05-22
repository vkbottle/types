import inspect
import typing
from .base_response import BaseResponse
from vkbottle_types.objects import FaveBookmark, FavePage, FaveTag, GroupsGroup, UsersUserFull


class AddTagResponse(BaseResponse):
    response: typing.Optional["AddTagResponseModel"] = None


class GetPagesResponse(BaseResponse):
    response: typing.Optional["GetPagesResponseModel"] = None


class GetTagsResponse(BaseResponse):
    response: typing.Optional["GetTagsResponseModel"] = None


class GetExtendedResponse(BaseResponse):
    response: typing.Optional["GetExtendedResponseModel"] = None


class GetResponse(BaseResponse):
    response: typing.Optional["GetResponseModel"] = None


AddTagResponseModel = FaveTag


class GetPagesResponseModel(BaseResponse):
    count: typing.Optional[int] = None
    items: typing.Optional[typing.List["FavePage"]] = None


class GetTagsResponseModel(BaseResponse):
    count: typing.Optional[int] = None
    items: typing.Optional[typing.List["FaveTag"]] = None


class GetExtendedResponseModel(BaseResponse):
    count: typing.Optional[int] = None
    items: typing.Optional[typing.List["FaveBookmark"]] = None
    profiles: typing.Optional[typing.List["UsersUserFull"]] = None
    groups: typing.Optional[typing.List["GroupsGroup"]] = None


class GetResponseModel(BaseResponse):
    count: typing.Optional[int] = None
    items: typing.Optional[typing.List["FaveBookmark"]] = None


for item in locals().copy().values():
    if inspect.isclass(item) and issubclass(item, BaseResponse):
        item.update_forward_refs()
