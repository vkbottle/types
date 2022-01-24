import inspect

from vkbottle_types.objects import BaseBoolInt, BaseUploadServer

from .base_response import BaseResponse


class BoolResponse(BaseResponse):
    response: BaseBoolInt


class OkResponse(BaseResponse):
    response: int


class BaseGetUploadServerResponse(BaseResponse):
    response: BaseUploadServer


for item in locals().copy().values():
    if inspect.isclass(item) and issubclass(item, BaseResponse):
        item.update_forward_refs()
