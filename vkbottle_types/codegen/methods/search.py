import typing

from vkbottle_types.methods.base_category import BaseCategory
from vkbottle_types.responses.search import *  # noqa: F401,F403  # type: ignore


class SearchCategory(BaseCategory):
    async def get_hints(
        self,
        fields: list[str] | None = None,
        filters: list[str] | None = None,
        limit: int | None = None,
        offset: int | None = None,
        q: str | None = None,
        search_global: bool | None = None,
        **kwargs: typing.Any,
    ) -> SearchGetHintsResponseModel:
        """Method `search.getHints()`

        :param fields:
        :param filters:
        :param limit: Maximum number of results to return.
        :param offset: Offset for querying specific result subset
        :param q: Search query string.
        :param search_global:
        """

        params = self.get_set_params(locals())
        response = await self.api.request("search.getHints", params)
        model = SearchGetHintsResponse
        return model(**response).response


__all__ = ("SearchCategory",)
