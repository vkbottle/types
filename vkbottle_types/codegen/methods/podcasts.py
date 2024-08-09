import typing

from vkbottle_types.methods.base_category import BaseCategory
from vkbottle_types.responses.podcasts import *  # noqa: F401,F403  # type: ignore


class PodcastsCategory(BaseCategory):
    async def search_podcast(
        self,
        search_string: str,
        count: typing.Optional[int] = None,
        offset: typing.Optional[int] = None,
        **kwargs: typing.Any,
    ) -> PodcastsSearchPodcastResponseModel:
        """Method `podcasts.searchPodcast()`

        :param search_string:
        :param count:
        :param offset:
        """

        params = self.get_set_params(locals())
        response = await self.api.request("podcasts.searchPodcast", params)
        model = PodcastsSearchPodcastResponse
        return model(**response).response


__all__ = ("PodcastsCategory",)
