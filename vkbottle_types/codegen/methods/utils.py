import typing

from typing_extensions import Literal
from vkbottle_types.responses.base import OkResponse
from vkbottle_types.responses.utils import (
    CheckLinkResponse,
    GetLastShortenedLinksResponse,
    GetLastShortenedLinksResponseModel,
    GetLinkStatsExtendedResponse,
    GetLinkStatsResponse,
    GetServerTimeResponse,
    GetShortLinkResponse,
    ResolveScreenNameResponse,
    UtilsDomainResolved,
    UtilsLinkChecked,
    UtilsLinkStats,
    UtilsLinkStatsExtended,
    UtilsShortLink,
)

from .base_category import BaseCategory


class UtilsCategory(BaseCategory):
    async def check_link(self, url: str, **kwargs) -> UtilsLinkChecked:
        """Checks whether a link is blocked in VK.

        :param url: Link to check (e.g., 'http://google.com').
        """

        params = self.get_set_params(locals())
        response = await self.api.request("utils.checkLink", params)
        model = CheckLinkResponse
        return model(**response).response

    async def delete_from_last_shortened(self, key: str, **kwargs) -> int:
        """Deletes shortened link from user's list.

        :param key: Link key (characters after vk.cc/).
        """

        params = self.get_set_params(locals())
        response = await self.api.request("utils.deleteFromLastShortened", params)
        model = OkResponse
        return model(**response).response

    async def get_last_shortened_links(
        self,
        count: typing.Optional[int] = None,
        offset: typing.Optional[int] = None,
        **kwargs
    ) -> GetLastShortenedLinksResponseModel:
        """Returns a list of user's shortened links.

        :param count: Number of links to return.
        :param offset: Offset needed to return a specific subset of links.
        """

        params = self.get_set_params(locals())
        response = await self.api.request("utils.getLastShortenedLinks", params)
        model = GetLastShortenedLinksResponse
        return model(**response).response

    @typing.overload
    async def get_link_stats(
        self,
        key: str,
        source: typing.Optional[Literal["vk_cc", "vk_link"]] = None,
        access_key: typing.Optional[str] = None,
        interval: typing.Optional[
            Literal["day", "forever", "hour", "month", "week"]
        ] = None,
        intervals_count: typing.Optional[int] = None,
        extended: typing.Optional[Literal[False]] = ...,
        **kwargs
    ) -> UtilsLinkStats:
        ...

    @typing.overload
    async def get_link_stats(
        self,
        key: str,
        source: typing.Optional[Literal["vk_cc", "vk_link"]] = None,
        access_key: typing.Optional[str] = None,
        interval: typing.Optional[
            Literal["day", "forever", "hour", "month", "week"]
        ] = None,
        intervals_count: typing.Optional[int] = None,
        extended: Literal[True] = ...,
        **kwargs
    ) -> UtilsLinkStatsExtended:
        ...

    async def get_link_stats(
        self,
        key=None,
        source=None,
        access_key=None,
        interval=None,
        intervals_count=None,
        extended=None,
        **kwargs
    ) -> typing.Union[UtilsLinkStats, UtilsLinkStatsExtended]:
        """Returns stats data for shortened link.

        :param key: Link key (characters after vk.cc/).
        :param source: Source of scope
        :param access_key: Access key for private link stats.
        :param interval: Interval.
        :param intervals_count: Number of intervals to return.
        :param extended: 1 — to return extended stats data (sex, age, geo). 0 — to return views number only.
        """

        params = self.get_set_params(locals())
        response = await self.api.request("utils.getLinkStats", params)
        model = self.get_model(
            ((("extended",), GetLinkStatsExtendedResponse),),
            default=GetLinkStatsResponse,
            params=params,
        )
        return model(**response).response

    async def get_server_time(self, **kwargs) -> int:
        """Returns the current time of the VK server."""

        params = self.get_set_params(locals())
        response = await self.api.request("utils.getServerTime", params)
        model = GetServerTimeResponse
        return model(**response).response

    async def get_short_link(
        self, url: str, private: typing.Optional[bool] = None, **kwargs
    ) -> UtilsShortLink:
        """Allows to receive a link shortened via vk.cc.

        :param url: URL to be shortened.
        :param private: 1 — private stats, 0 — public stats.
        """

        params = self.get_set_params(locals())
        response = await self.api.request("utils.getShortLink", params)
        model = GetShortLinkResponse
        return model(**response).response

    async def resolve_screen_name(
        self, screen_name: str, **kwargs
    ) -> UtilsDomainResolved:
        """Detects a type of object (e.g., user, community, application) and its ID by screen name.

        :param screen_name: Screen name of the user, community (e.g., 'apiclub,' 'andrew', or 'rules_of_war'), or application.
        """

        params = self.get_set_params(locals())
        response = await self.api.request("utils.resolveScreenName", params)
        model = ResolveScreenNameResponse
        return model(**response).response


__all__ = ("UtilsCategory",)
