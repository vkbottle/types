import inspect
import typing

from vkbottle_types.responses.base_response import BaseResponse


class RestoreResponse(BaseResponse):
    response: "RestoreResponseModel"


class RestoreResponseModel(BaseResponse):
    success: typing.Optional[int] = None
    sid: typing.Optional[str] = None


for item in locals().copy().values():
    if inspect.isclass(item) and issubclass(item, BaseResponse):
        item.update_forward_refs()


__all__ = (
    "RestoreResponse",
    "RestoreResponseModel",
)
