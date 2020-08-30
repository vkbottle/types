from .base_response import BaseResponse
from vkbottle_types.objects import search
from typing import Optional, Any, List, Union
import typing


class GetHintsResponse(BaseResponse):
    response: Optional["GetHintsResponseModel"] = None


class GetHintsResponseModel(BaseResponse):
    count: Optional[int] = None
    items: Optional[List["search.Hint"]] = None
    suggested_queries: Optional[List[str]] = None
