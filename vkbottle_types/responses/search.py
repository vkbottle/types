from typing import List, Optional

from vkbottle_types.objects import SearchHint

from .base_response import BaseResponse


class GetHintsResponse(BaseResponse):
    response: Optional["GetHintsResponseModel"] = None


class GetHintsResponseModel(BaseResponse):
    count: Optional[int] = None
    items: Optional[List["SearchHint"]] = None
    suggested_queries: Optional[List[str]] = None


GetHintsResponse.update_forward_refs()
