import inspect
import typing

from vkbottle_types.objects import PodcastExternalData

from .base_response import BaseResponse


class SearchPodcastResponse(BaseResponse):
    response: "SearchPodcastResponseModel"


class SearchPodcastResponseModel(BaseResponse):
    podcasts: typing.Optional[typing.List["PodcastExternalData"]] = None
    results_total: typing.Optional[int] = None


for item in locals().copy().values():
    if inspect.isclass(item) and issubclass(item, BaseResponse):
        item.update_forward_refs()


__all__ = ("SearchPodcastResponse",)
