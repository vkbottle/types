import inspect
import typing
from .base_response import BaseResponse
from vkbottle_types.objects import PodcastExternalData


class SearchPodcastResponse(BaseResponse):
    response: typing.Optional["SearchPodcastResponseModel"] = None


class SearchPodcastResponseModel(BaseResponse):
    podcasts: typing.Optional[typing.List["PodcastExternalData"]] = None
    results_total: typing.Optional[int] = None


for item in locals().copy().values():
    if inspect.isclass(item) and issubclass(item, BaseResponse):
        item.update_forward_refs()
