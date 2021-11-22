import typing
from .base_category import BaseCategory
from vkbottle_types.responses.search import GetHintsResponse, GetHintsResponseModel


class SearchCategory(BaseCategory):
    async def get_hints(
        self,
        q: typing.Optional[str] = None,
        offset: typing.Optional[int] = None,
        limit: typing.Optional[int] = None,
        filters: typing.Optional[typing.List[str]] = None,
        fields: typing.Optional[typing.List[str]] = None,
        search_global: typing.Optional[bool] = None,
        **kwargs
    ) -> GetHintsResponseModel:
        """Allows the programmer to do a quick search for any substring.

        :param q: Search query string.
        :param offset: Offset for querying specific result subset
        :param limit: Maximum number of results to return.
        :param filters:
        :param fields:
        :param search_global:
        """

        params = self.get_set_params(locals())
        response = await self.api.request("search.getHints", params)
        model = GetHintsResponse
        return model(**response).response
