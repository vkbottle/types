import typing
import enum
from vkbottle_types.responses.base_response import BaseResponse, BaseModel
from vkbottle_types.base_model import Field

from vkbottle_types.objects import StreamingStatsPoint


class StreamingStatsResponseModel(BaseModel):
    event_type: typing.Literal["post", "comment", "share"] = Field(
        description="Events type",
    )

    stats: typing.List[StreamingStatsPoint] = Field(
        description="Statistics",
    )


class StreamingStatsResponse(BaseResponse):
    response: "StreamingStatsResponseModel"


class StreamingStatsPointResponseModel(BaseModel):
    timestamp: int = Field()

    value: int = Field()


class StreamingStatsPointResponse(BaseResponse):
    response: "StreamingStatsPointResponseModel"
