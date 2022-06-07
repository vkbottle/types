import typing

from vkbottle_types.objects import WidgetsWidgetComment, WidgetsWidgetPage
from vkbottle_types.responses.base_response import BaseResponse


class GetCommentsResponse(BaseResponse):
    response: "GetCommentsResponseModel"


class GetPagesResponse(BaseResponse):
    response: "GetPagesResponseModel"


class GetCommentsResponseModel(BaseResponse):
    count: typing.Optional[int] = None
    posts: typing.Optional[typing.List["WidgetsWidgetComment"]] = None


class GetPagesResponseModel(BaseResponse):
    count: typing.Optional[int] = None
    pages: typing.Optional[typing.List["WidgetsWidgetPage"]] = None


__all__ = (
    "GetCommentsResponse",
    "GetCommentsResponseModel",
    "GetPagesResponse",
    "GetPagesResponseModel",
    "WidgetsWidgetComment",
    "WidgetsWidgetPage",
)
