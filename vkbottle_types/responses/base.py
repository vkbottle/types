import inspect
import typing

from vkbottle_types.objects import BaseBoolInt, BaseUploadServer

from .base_response import BaseResponse


class BoolResponse(BaseResponse):
    response: typing.Optional["BoolResponseModel"] = None


class GetUploadServerResponse(BaseResponse):
    response: typing.Optional["GetUploadServerResponseModel"] = None


class OkResponse(BaseResponse):
    response: typing.Optional["OkResponseModel"] = None


BoolResponseModel = BaseBoolInt


GetUploadServerResponseModel = BaseUploadServer


OkResponseModel = int


for item in locals().copy().values():
    if inspect.isclass(item) and issubclass(item, BaseResponse):
        item.update_forward_refs()
