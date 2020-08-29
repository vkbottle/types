import typing
from typing import Optional

from vkbottle_types.objects import search
from .base_response import BaseResponse


class GetHintsResponse(BaseResponse):
    response: Optional["GetHintsResponseModel"] = None


class GetHintsResponseModel(BaseResponse):
    count: Optional[int] = None
    items: Optional[typing.List["search.Hint"]] = None
    suggested_queries: Optional[typing.List[str]] = None
