from typing import Optional

from vkbottle_types.responses import base, utils
from .base_category import BaseCategory


class UtilsCategory(BaseCategory):
    async def check_link(self, url: str, **kwargs) -> utils.CheckLinkResponseModel:
        """Checks whether a link is blocked in VK.
        :param url: Link to check (e.g., 'http://google.com').
        """

        params = self.get_set_params(locals())
        return utils.CheckLinkResponse(
            **await self.api.request("utils.checkLink", params)
        ).response

    async def delete_from_last_shortened(
        self, key: str, **kwargs
    ) -> base.OkResponseModel:
        """Deletes shortened link from user's list.
        :param key: Link key (characters after vk.cc/).
        """

        params = self.get_set_params(locals())
        return base.OkResponse(
            **await self.api.request("utils.deleteFromLastShortened", params)
        ).response

    async def get_last_shortened_links(
        self, count: Optional[int] = None, offset: Optional[int] = None, **kwargs
    ) -> utils.GetLastShortenedLinksResponseModel:
        """Returns a list of user's shortened links.
        :param count: Number of links to return.
        :param offset: Offset needed to return a specific subset of links.
        """

        params = self.get_set_params(locals())
        return utils.GetLastShortenedLinksResponse(
            **await self.api.request("utils.getLastShortenedLinks", params)
        ).response

    async def get_link_stats(
        self,
        key: str,
        source: Optional[str] = None,
        access_key: Optional[str] = None,
        interval: Optional[str] = None,
        intervals_count: Optional[int] = None,
        extended: Optional[bool] = None,
        **kwargs
    ) -> utils.GetLinkStatsExtendedResponseModel:
        """Returns stats data for shortened link.
        :param key: Link key (characters after vk.cc/).
        :param source: Source of scope
        :param access_key: Access key for private link stats.
        :param interval: Interval.
        :param intervals_count: Number of intervals to return.
        :param extended: 1 — to return extended stats data (sex, age, geo). 0 — to return views number only.
        """

        params = self.get_set_params(locals())
        return utils.GetLinkStatsExtendedResponse(
            **await self.api.request("utils.getLinkStats", params)
        ).response

    async def get_server_time(self, **kwargs) -> utils.GetServerTimeResponseModel:
        """Returns the current time of the VK server."""

        params = self.get_set_params(locals())
        return utils.GetServerTimeResponse(
            **await self.api.request("utils.getServerTime", params)
        ).response

    async def get_short_link(
        self, url: str, private: Optional[bool] = None, **kwargs
    ) -> utils.GetShortLinkResponseModel:
        """Allows to receive a link shortened via vk.cc.
        :param url: URL to be shortened.
        :param private: 1 — private stats, 0 — public stats.
        """

        params = self.get_set_params(locals())
        return utils.GetShortLinkResponse(
            **await self.api.request("utils.getShortLink", params)
        ).response

    async def resolve_screen_name(
        self, screen_name: str, **kwargs
    ) -> utils.ResolveScreenNameResponseModel:
        """Detects a type of object (e.g., user, community, application, **kwargs) and its ID by screen name.
        :param screen_name: Screen name of the user, community (e.g., 'apiclub,' 'andrew', or 'rules_of_war'), or application.
        """

        params = self.get_set_params(locals())
        return utils.ResolveScreenNameResponse(
            **await self.api.request("utils.resolveScreenName", params)
        ).response
