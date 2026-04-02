from vkbottle_types.base_model import BaseModel, Field
from vkbottle_types.objects import PodcastExternalData
from vkbottle_types.responses.base_response import BaseResponse


class PodcastsSearchPodcastResponseModel(BaseModel):
    podcasts: list["PodcastExternalData"] = Field()
    results_total: int = Field()


class PodcastsSearchPodcastResponse(BaseResponse):
    response: "PodcastsSearchPodcastResponseModel" = Field()


__all__ = (
    "PodcastsSearchPodcastResponse",
    "PodcastsSearchPodcastResponseModel",
)
