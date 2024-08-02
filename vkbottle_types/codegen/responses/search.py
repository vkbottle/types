import typing

from vkbottle_types.base_model import BaseModel, Field
from vkbottle_types.objects import SearchHint
from vkbottle_types.responses.base_response import BaseResponse


class SearchGetHintsResponseModel(BaseModel):
    count: int = Field()
    items: typing.List["SearchHint"] = Field()
    suggested_queries: typing.Optional[typing.List[str]] = Field(
        default=None,
    )


class SearchGetHintsResponse(BaseResponse):
    response: "SearchGetHintsResponseModel" = Field()
