import inspect
from .base_response import BaseResponse
from vkbottle_types.objects import BaseBoolInt, BaseUploadServer


class BoolResponse(BaseResponse):
    response: BaseBoolInt = None


class GetUploadServerResponse(BaseResponse):
    response: BaseUploadServer = None


class OkResponse(BaseResponse):
    response: int = None


for item in locals().copy().values():
    if inspect.isclass(item) and issubclass(item, BaseResponse):
        item.update_forward_refs()
