import inspect
import typing
from .base_response import BaseResponse
from vkbottle_types.objects import StatusStatus


class GetResponse(BaseResponse):
    response: StatusStatus = None


for item in locals().copy().values():
    if inspect.isclass(item) and issubclass(item, BaseResponse):
        item.update_forward_refs()
