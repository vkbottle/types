from .base_response import BaseResponse

from typing import Optional, Any, List, Union
import typing


class RestoreResponse(BaseResponse):
    response: Optional["RestoreResponseModel"] = None


class RestoreResponseModel(BaseResponse):
    success: Optional[int] = None
    sid: Optional[str] = None
