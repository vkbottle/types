from typing import Optional, List

from vkbottle_types.responses import search
from .base_category import BaseCategory


class SearchCategory(BaseCategory):
    async def get_hints(
        self,
        q: Optional[str] = None,
        offset: Optional[int] = None,
        limit: Optional[int] = None,
        filters: Optional[List[str]] = None,
        fields: Optional[List[str]] = None,
        search_global: Optional[bool] = None,
        **kwargs
    ) -> search.GetHintsResponseModel:
        """Allows the programmer to do a quick search for any substring.
        :param q: Search query string.
        :param offset: Offset for querying specific result subset
        :param limit: Maximum number of results to return.
        :param filters:
        :param fields:
        :param search_global:
        """

        params = self.get_set_params(locals())
        return search.GetHintsResponse(
            **await self.api.request("search.getHints", params)
        )
