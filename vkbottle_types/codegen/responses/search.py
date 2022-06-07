import typing

from vkbottle_types.objects import SearchHint
from vkbottle_types.responses.base_response import BaseResponse


class GetHintsResponse(BaseResponse):
    response: "GetHintsResponseModel"


class GetHintsResponseModel(BaseResponse):
    count: typing.Optional[int] = None
    items: typing.Optional[typing.List["SearchHint"]] = None
    suggested_queries: typing.Optional[typing.List[str]] = None


__all__ = (
    "GetHintsResponse",
    "GetHintsResponseModel",
    "SearchHint",
)
