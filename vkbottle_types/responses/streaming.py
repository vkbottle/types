from .base_response import BaseResponse

from typing import Optional, Any, List, Union
import typing


class GetServerUrlResponse(BaseResponse):
    response: Optional["GetServerUrlResponseModel"] = None


class GetServerUrlResponseModel(BaseResponse):
    endpoint: Optional[str] = None
    key: Optional[str] = None
