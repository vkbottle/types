from typing import List, Optional

from vkbottle_types.objects import (
    FaveBookmark,
    FavePage,
    FaveTag,
    GroupsGroup,
    UsersUserFull,
)

from .base_response import BaseResponse


class AddTagResponse(BaseResponse):
    response: Optional["AddTagResponseModel"] = None


class GetPagesResponse(BaseResponse):
    response: Optional["GetPagesResponseModel"] = None


class GetTagsResponse(BaseResponse):
    response: Optional["GetTagsResponseModel"] = None


class GetExtendedResponse(BaseResponse):
    response: Optional["GetExtendedResponseModel"] = None


class GetResponse(BaseResponse):
    response: Optional["GetResponseModel"] = None


AddTagResponseModel = Optional[FaveTag]


class GetPagesResponseModel(BaseResponse):
    count: Optional[int] = None
    items: Optional[List["FavePage"]] = None


class GetTagsResponseModel(BaseResponse):
    count: Optional[int] = None
    items: Optional[List["FaveTag"]] = None


class GetExtendedResponseModel(BaseResponse):
    count: Optional[int] = None
    items: Optional[List["FaveBookmark"]] = None
    profiles: Optional[List["UsersUserFull"]] = None
    groups: Optional[List["GroupsGroup"]] = None


class GetResponseModel(BaseResponse):
    count: Optional[int] = None
    items: Optional[List["FaveBookmark"]] = None


AddTagResponse.update_forward_refs()
GetPagesResponse.update_forward_refs()
GetTagsResponse.update_forward_refs()
GetExtendedResponse.update_forward_refs()
GetResponse.update_forward_refs()
