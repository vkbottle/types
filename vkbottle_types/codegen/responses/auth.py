import typing

from vkbottle_types.responses.base_response import BaseResponse


class RestoreResponse(BaseResponse):
    response: "RestoreResponseModel"


class RestoreResponseModel(BaseResponse):
    success: typing.Optional[int] = None
    sid: typing.Optional[str] = None


__all__ = (
    "RestoreResponse",
    "RestoreResponseModel",
)
