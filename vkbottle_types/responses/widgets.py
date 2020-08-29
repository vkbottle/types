import typing
from typing import Optional

from vkbottle_types.objects import widgets
from .base_response import BaseResponse


class GetCommentsResponse(BaseResponse):
    response: Optional["GetCommentsResponseModel"] = None


class GetPagesResponse(BaseResponse):
    response: Optional["GetPagesResponseModel"] = None


class GetCommentsResponseModel(BaseResponse):
    count: Optional[int] = None
    posts: Optional[typing.List["widgets.WidgetComment"]] = None


class GetPagesResponseModel(BaseResponse):
    count: Optional[int] = None
    pages: Optional[typing.List["widgets.WidgetPage"]] = None
