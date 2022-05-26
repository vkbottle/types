import typing

from typing_extensions import Literal
from vkbottle_types.responses.base import OkResponse
from vkbottle_types.responses.stats import (
    GetPostReachResponse,
    GetResponse,
    StatsPeriod,
    StatsWallpostStat,
)

from .base_category import BaseCategory


class StatsCategory(BaseCategory):
    async def get(
        self,
        group_id: typing.Optional[int] = None,
        app_id: typing.Optional[int] = None,
        timestamp_from: typing.Optional[int] = None,
        timestamp_to: typing.Optional[int] = None,
        interval: typing.Optional[
            Literal["all", "day", "month", "week", "year"]
        ] = None,
        intervals_count: typing.Optional[int] = None,
        filters: typing.Optional[typing.List[str]] = None,
        stats_groups: typing.Optional[typing.List[str]] = None,
        extended: typing.Optional[bool] = None,
        **kwargs
    ) -> typing.List[StatsPeriod]:
        """Returns statistics of a community or an application.

        :param group_id: Community ID.
        :param app_id: Application ID.
        :param timestamp_from:
        :param timestamp_to:
        :param interval:
        :param intervals_count:
        :param filters:
        :param stats_groups:
        :param extended:
        """

        params = self.get_set_params(locals())
        response = await self.api.request("stats.get", params)
        model = GetResponse
        return model(**response).response

    async def get_post_reach(
        self, owner_id: str, post_ids: typing.List[int], **kwargs
    ) -> typing.List[StatsWallpostStat]:
        """Returns stats for a wall post.

        :param owner_id: post owner community id. Specify with "-" sign.
        :param post_ids: wall posts id
        """

        params = self.get_set_params(locals())
        response = await self.api.request("stats.getPostReach", params)
        model = GetPostReachResponse
        return model(**response).response

    async def track_visitor(self, **kwargs) -> int:
        """stats.trackVisitor method"""

        params = self.get_set_params(locals())
        response = await self.api.request("stats.trackVisitor", params)
        model = OkResponse
        return model(**response).response


__all__ = ("StatsCategory",)
