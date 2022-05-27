import inspect
import typing

from vkbottle_types.responses.base_response import BaseResponse


class GetServerUrlResponse(BaseResponse):
    response: "GetServerUrlResponseModel"


class GetServerUrlResponseModel(BaseResponse):
    endpoint: typing.Optional[str] = None
    key: typing.Optional[str] = None


for item in locals().copy().values():
    if inspect.isclass(item) and issubclass(item, BaseResponse):
        item.update_forward_refs()


__all__ = (
    "GetServerUrlResponse",
    "GetServerUrlResponseModel",
)
