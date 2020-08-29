from typing import Optional

from .base_response import BaseResponse


class PaidStatusResponse(BaseResponse):
    response: Optional["PaidStatusResponseModel"] = None


class PaidStatusResponseModel(BaseResponse):
    is_paid: Optional[bool] = None
