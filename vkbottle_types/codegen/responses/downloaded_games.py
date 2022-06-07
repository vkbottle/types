import typing

from vkbottle_types.responses.base_response import BaseResponse


class PaidStatusResponse(BaseResponse):
    response: "PaidStatusResponseModel"


class PaidStatusResponseModel(BaseResponse):
    is_paid: typing.Optional[bool] = None


__all__ = (
    "PaidStatusResponse",
    "PaidStatusResponseModel",
)
