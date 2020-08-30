from .base_response import BaseResponse

from typing import Optional, Any, List, Union
import typing


class PaidStatusResponse(BaseResponse):
    response: Optional["PaidStatusResponseModel"] = None


class PaidStatusResponseModel(BaseResponse):
    is_paid: Optional[bool] = None
