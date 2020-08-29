from typing import Optional

from .base_response import BaseResponse


class RestoreResponse(BaseResponse):
    response: Optional["RestoreResponseModel"] = None


class RestoreResponseModel(BaseResponse):
    success: Optional[int] = None
    sid: Optional[str] = None
