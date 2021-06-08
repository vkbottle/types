import inspect
import typing
from .base_response import BaseResponse
from vkbottle_types.objects import WidgetsWidgetComment, WidgetsWidgetPage


class GetCommentsResponse(BaseResponse):
    response: "GetCommentsResponseModel" = None


class GetPagesResponse(BaseResponse):
    response: "GetPagesResponseModel" = None


class GetCommentsResponseModel(BaseResponse):
    count: typing.Optional[int] = None
    posts: typing.Optional[typing.List["WidgetsWidgetComment"]] = None


class GetPagesResponseModel(BaseResponse):
    count: typing.Optional[int] = None
    pages: typing.Optional[typing.List["WidgetsWidgetPage"]] = None


for item in locals().copy().values():
    if inspect.isclass(item) and issubclass(item, BaseResponse):
        item.update_forward_refs()
