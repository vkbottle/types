import typing

from typing_extensions import Literal
from vkbottle_types.methods.base_category import BaseCategory
from vkbottle_types.responses.search import *
from vkbottle_types.responses.base import OkResponse


class SearchCategory(BaseCategory):
    async def get_hints(
        self,
        q: typing.Optional[str] = None,
        offset: typing.Optional[int] = None,
        limit: typing.Optional[int] = 9,
        filters: typing.Optional[typing.List[str]] = None,
        fields: typing.Optional[typing.List[str]] = None,
        search_global: typing.Optional[bool] = 1,
        **kwargs,
    ) -> SearchGetHintsResponseModel:
        """search.getHints method


        :param q: Search query string.
        :param offset: Offset for querying specific result subset
        :param limit: Maximum number of results to return.
        :param filters:
        :param fields:
        :param search_global:
        """
        params = self.get_set_params(locals())
        response = await self.api.request("account.ban", params)

        model = SearchGetHintsResponse

        return model(**response).response


__all__ = ("SearchCategory",)
