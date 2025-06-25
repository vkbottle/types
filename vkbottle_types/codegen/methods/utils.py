import typing

from vkbottle_types.methods.base_category import BaseCategory
from vkbottle_types.objects import UtilsDomainResolved, UtilsLinkChecked, UtilsLinkStats, UtilsLinkStatsExtended, UtilsShortLink
from vkbottle_types.responses.base import (
    BaseOkResponse,
    BaseOkResponseModel,
)
from vkbottle_types.responses.utils import *  # noqa: F401,F403  # type: ignore


class UtilsCategory(BaseCategory):
    async def check_link(
        self,
        url: str,
        **kwargs: typing.Any,
    ) -> "UtilsLinkChecked":
        """Method `utils.checkLink()`

        :param url: Link to check (e.g., 'http://google.com').
        """

        params = self.get_set_params(locals())
        response = await self.api.request("utils.checkLink", params)
        model = UtilsCheckLinkResponse
        return model(**response).response

    async def delete_from_last_shortened(
        self,
        key: str,
        **kwargs: typing.Any,
    ) -> BaseOkResponseModel:
        """Method `utils.deleteFromLastShortened()`

        :param key: Link key (characters after vk.cc/).
        """

        params = self.get_set_params(locals())
        response = await self.api.request("utils.deleteFromLastShortened", params)
        model = BaseOkResponse
        return model(**response).response

    async def get_last_shortened_links(
        self,
        count: typing.Optional[int] = None,
        offset: typing.Optional[int] = None,
        **kwargs: typing.Any,
    ) -> UtilsGetLastShortenedLinksResponseModel:
        """Method `utils.getLastShortenedLinks()`

        :param count: Number of links to return.
        :param offset: Offset needed to return a specific subset of links.
        """

        params = self.get_set_params(locals())
        response = await self.api.request("utils.getLastShortenedLinks", params)
        model = UtilsGetLastShortenedLinksResponse
        return model(**response).response

    @typing.overload
    async def get_link_stats(
        self,
        key: str,
        extended: typing.Literal[True],
        access_key: typing.Optional[str] = None,
        interval: typing.Optional[str] = None,
        intervals_count: typing.Optional[int] = None,
        source: typing.Optional[str] = None,
        **kwargs: typing.Any,
    ) -> "UtilsLinkStatsExtended": ...

    @typing.overload
    async def get_link_stats(
        self,
        key: str,
        extended: typing.Optional[typing.Literal[False]] = None,
        access_key: typing.Optional[str] = None,
        interval: typing.Optional[str] = None,
        intervals_count: typing.Optional[int] = None,
        source: typing.Optional[str] = None,
        **kwargs: typing.Any,
    ) -> "UtilsLinkStats": ...

    async def get_link_stats(
        self,
        key: str,
        extended: typing.Optional[bool] = None,
        access_key: typing.Optional[str] = None,
        interval: typing.Optional[str] = None,
        intervals_count: typing.Optional[int] = None,
        source: typing.Optional[str] = None,
        **kwargs: typing.Any,
    ) -> typing.Union["UtilsLinkStats", "UtilsLinkStatsExtended"]:
        """Method `utils.getLinkStats()`

        :param key: Link key (characters after vk.cc/).
        :param extended: 1 - to return extended stats data (sex, age, geo). 0 - to return views number only.
        :param access_key: Access key for private link stats.
        :param interval: Interval.
        :param intervals_count: Number of intervals to return.
        :param source: Source of scope
        """

        params = self.get_set_params(locals())
        response = await self.api.request("utils.getLinkStats", params)
        model = self.get_model(
            ((("extended",), UtilsGetLinkStatsExtendedResponse),),
            default=UtilsGetLinkStatsResponse,
            params=params,
        )
        return model(**response).response

    async def get_server_time(
        self,
        **kwargs: typing.Any,
    ) -> int:
        """Method `utils.getServerTime()`"""

        params = self.get_set_params(locals())
        response = await self.api.request("utils.getServerTime", params)
        model = UtilsGetServerTimeResponse
        return model(**response).response

    async def get_short_link(
        self,
        url: str,
        private: typing.Optional[bool] = None,
        **kwargs: typing.Any,
    ) -> "UtilsShortLink":
        """Method `utils.getShortLink()`

        :param url: URL to be shortened.
        :param private: 1 - private stats, 0 - public stats.
        """

        params = self.get_set_params(locals())
        response = await self.api.request("utils.getShortLink", params)
        model = UtilsGetShortLinkResponse
        return model(**response).response

    async def resolve_screen_name(
        self,
        screen_name: str,
        **kwargs: typing.Any,
    ) -> "UtilsDomainResolved":
        """Method `utils.resolveScreenName()`

        :param screen_name: Screen name of the user, community (e.g., 'apiclub,' 'andrew', or 'rules_of_war'), or application.
        """

        params = self.get_set_params(locals())
        response = await self.api.request("utils.resolveScreenName", params)
        model = UtilsResolveScreenNameResponse
        return model(**response).response


__all__ = ("UtilsCategory",)
