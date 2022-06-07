import typing

from vkbottle_types.objects import (
    FaveBookmark,
    FavePage,
    FaveTag,
    GroupsGroup,
    UsersUserFull,
)
from vkbottle_types.responses.base_response import BaseResponse


class AddTagResponse(BaseResponse):
    response: FaveTag


class GetPagesResponse(BaseResponse):
    response: "GetPagesResponseModel"


class GetTagsResponse(BaseResponse):
    response: "GetTagsResponseModel"


class GetExtendedResponse(BaseResponse):
    response: "GetExtendedResponseModel"


class GetResponse(BaseResponse):
    response: "GetResponseModel"


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


__all__ = (
    "AddTagResponse",
    "FaveBookmark",
    "FavePage",
    "FaveTag",
    "GetExtendedResponse",
    "GetExtendedResponseModel",
    "GetPagesResponse",
    "GetPagesResponseModel",
    "GetResponse",
    "GetResponseModel",
    "GetTagsResponse",
    "GetTagsResponseModel",
    "GroupsGroup",
    "UsersUserFull",
)
