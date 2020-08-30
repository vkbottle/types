from .base_response import BaseResponse
from vkbottle_types.objects import widgets
from typing import Optional, Any, List, Union
import typing


class GetCommentsResponse(BaseResponse):
    response: Optional["GetCommentsResponseModel"] = None


class GetPagesResponse(BaseResponse):
    response: Optional["GetPagesResponseModel"] = None


class GetCommentsResponseModel(BaseResponse):
    count: Optional[int] = None
    posts: Optional[List["widgets.WidgetComment"]] = None


class GetPagesResponseModel(BaseResponse):
    count: Optional[int] = None
    pages: Optional[List["widgets.WidgetPage"]] = None
