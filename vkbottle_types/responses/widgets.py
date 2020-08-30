from typing import Optional, List

from vkbottle_types.objects import WidgetsWidgetPage, WidgetsWidgetComment
from .base_response import BaseResponse


class GetCommentsResponse(BaseResponse):
    response: Optional["GetCommentsResponseModel"] = None


class GetPagesResponse(BaseResponse):
    response: Optional["GetPagesResponseModel"] = None


class GetCommentsResponseModel(BaseResponse):
    count: Optional[int] = None
    posts: Optional[List["WidgetsWidgetComment"]] = None


class GetPagesResponseModel(BaseResponse):
    count: Optional[int] = None
    pages: Optional[List["WidgetsWidgetPage"]] = None

GetCommentsResponse.update_forward_refs()
GetPagesResponse.update_forward_refs()
