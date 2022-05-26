import typing

from vkbottle_types.responses.podcasts import (
    SearchPodcastResponse,
    SearchPodcastResponseModel,
)

from .base_category import BaseCategory


class PodcastsCategory(BaseCategory):
    async def search_podcast(
        self,
        search_string: str,
        offset: typing.Optional[int] = None,
        count: typing.Optional[int] = None,
        **kwargs
    ) -> SearchPodcastResponseModel:
        """podcasts.searchPodcast method

        :param search_string:
        :param offset:
        :param count:
        """

        params = self.get_set_params(locals())
        response = await self.api.request("podcasts.searchPodcast", params)
        model = SearchPodcastResponse
        return model(**response).response


__all__ = ("PodcastsCategory",)
