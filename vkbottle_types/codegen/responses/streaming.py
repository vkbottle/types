from vkbottle_types.base_model import BaseModel, Field
from vkbottle_types.objects import StreamingStats
from vkbottle_types.responses.base_response import BaseResponse


class StreamingGetServerUrlResponseModel(BaseModel):
    endpoint: str | None = Field(
        default=None,
    )
    key: str | None = Field(
        default=None,
    )


class StreamingGetServerUrlResponse(BaseResponse):
    response: "StreamingGetServerUrlResponseModel" = Field()


class StreamingGetStatsResponse(BaseResponse):
    response: list["StreamingStats"] = Field()


class StreamingGetStemResponseModel(BaseModel):
    stem: str | None = Field(
        default=None,
    )


class StreamingGetStemResponse(BaseResponse):
    response: "StreamingGetStemResponseModel" = Field()
