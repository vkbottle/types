import inspect
import typing

from .base_response import BaseResponse


class GetServerUrlResponse(BaseResponse):
    response: typing.Optional["GetServerUrlResponseModel"] = None


class GetServerUrlResponseModel(BaseResponse):
    endpoint: typing.Optional[str] = None
    key: typing.Optional[str] = None


for item in locals().copy().values():
    if inspect.isclass(item) and issubclass(item, BaseResponse):
        item.update_forward_refs()
