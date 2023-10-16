import typing

from typing_extensions import Literal
from vkbottle_types.methods.base_category import BaseCategory
from vkbottle_types.responses.podcasts import *
from vkbottle_types.responses.base import OkResponse


class PodcastsCategory(BaseCategory):
    async def search_podcast(
        self,
        search_string: str,
        offset: typing.Optional[int] = 0,
        count: typing.Optional[int] = 20,
        **kwargs,
    ) -> PodcastsSearchPodcastResponseModel:
        """podcasts.searchPodcast method


        :param search_string:
        :param offset:
        :param count:
        """
        params = self.get_set_params(locals())
        response = await self.api.request("account.ban", params)

        model = PodcastsSearchPodcastResponse

        return model(**response).response


__all__ = ("PodcastsCategory",)
