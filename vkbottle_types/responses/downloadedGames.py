import inspect
import typing

from .base_response import BaseResponse


class PaidStatusResponse(BaseResponse):
    response: typing.Optional["PaidStatusResponseModel"] = None


class PaidStatusResponseModel(BaseResponse):
    is_paid: typing.Optional[bool] = None


for item in locals().copy().values():
    if inspect.isclass(item) and issubclass(item, BaseResponse):
        item.update_forward_refs()
