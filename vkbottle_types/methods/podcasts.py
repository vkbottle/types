import typing
from .base_category import BaseCategory
from vkbottle_types.responses import podcasts


class PodcastsCategory(BaseCategory):
    async def search_podcast(
        self,
        search_string: str,
        offset: typing.Optional[int] = None,
        count: typing.Optional[int] = None,
        **kwargs
    ) -> podcasts.SearchPodcastResponseModel:
        """podcasts.searchPodcast method
        :param search_string:
        :param offset:
        :param count:
        """

        params = self.get_set_params(locals())
        response = await self.api.request("podcasts.searchPodcast", params)
        model = podcasts.SearchPodcastResponse
        return model(**response).response
