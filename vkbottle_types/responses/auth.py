import inspect
import typing

from .base_response import BaseResponse


class RestoreResponse(BaseResponse):
    response: typing.Optional["RestoreResponseModel"] = None


class RestoreResponseModel(BaseResponse):
    success: typing.Optional[int] = None
    sid: typing.Optional[str] = None


for item in locals().copy().values():
    if inspect.isclass(item) and issubclass(item, BaseResponse):
        item.update_forward_refs()
