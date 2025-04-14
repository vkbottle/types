import typing

from vkbottle_types.methods.base_category import BaseCategory
from vkbottle_types.objects import StatsPeriod, StatsWallpostStat
from vkbottle_types.responses.base import (
    BaseOkResponse,
    BaseOkResponseModel,
)
from vkbottle_types.responses.stats import *  # noqa: F401,F403  # type: ignore


class StatsCategory(BaseCategory):
    async def get(
        self,
        app_id: typing.Optional[int] = None,
        extended: typing.Optional[bool] = None,
        filters: typing.Optional[typing.List[str]] = None,
        group_id: typing.Optional[int] = None,
        interval: typing.Optional[str] = None,
        intervals_count: typing.Optional[int] = None,
        stats_groups: typing.Optional[typing.List[str]] = None,
        timestamp_from: typing.Optional[float] = None,
        timestamp_to: typing.Optional[float] = None,
        **kwargs: typing.Any,
    ) -> typing.List[StatsPeriod]:
        """Method `stats.get()`

        :param app_id: Application ID.
        :param extended:
        :param filters:
        :param group_id: Community ID.
        :param interval:
        :param intervals_count:
        :param stats_groups:
        :param timestamp_from:
        :param timestamp_to:
        """

        params = self.get_set_params(locals())
        response = await self.api.request("stats.get", params)
        model = StatsGetResponse
        return model(**response).response

    async def get_post_reach(
        self,
        owner_id: int,
        post_ids: typing.List[int],
        **kwargs: typing.Any,
    ) -> typing.List[StatsWallpostStat]:
        """Method `stats.getPostReach()`

        :param owner_id: post owner community id. Specify with "-" sign.
        :param post_ids: wall posts id
        """

        params = self.get_set_params(locals())
        response = await self.api.request("stats.getPostReach", params)
        model = StatsGetPostReachResponse
        return model(**response).response

    async def track_visitor(
        self,
        type: typing.Optional[str] = None,
        **kwargs: typing.Any,
    ) -> BaseOkResponseModel:
        """Method `stats.trackVisitor()`

        :param type:
        """

        params = self.get_set_params(locals())
        response = await self.api.request("stats.trackVisitor", params)
        model = BaseOkResponse
        return model(**response).response


__all__ = ("StatsCategory",)
