import typing

from vkbottle_types.responses.base_response import BaseResponse


class GetServerUrlResponse(BaseResponse):
    response: "GetServerUrlResponseModel"


class GetServerUrlResponseModel(BaseResponse):
    endpoint: typing.Optional[str] = None
    key: typing.Optional[str] = None


__all__ = (
    "GetServerUrlResponse",
    "GetServerUrlResponseModel",
)
