from typing import Optional

from .base_response import BaseResponse


class GetServerUrlResponse(BaseResponse):
    response: Optional["GetServerUrlResponseModel"] = None


class GetServerUrlResponseModel(BaseResponse):
    endpoint: Optional[str] = None
    key: Optional[str] = None

GetServerUrlResponse.update_forward_refs()
