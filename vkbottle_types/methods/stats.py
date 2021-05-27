import typing
from .base_category import BaseCategory
from vkbottle_types.responses import base, stats


class StatsCategory(BaseCategory):
    async def get(
        self,
        group_id: typing.Optional[int] = None,
        app_id: typing.Optional[int] = None,
        timestamp_from: typing.Optional[int] = None,
        timestamp_to: typing.Optional[int] = None,
        interval: typing.Optional[str] = None,
        intervals_count: typing.Optional[int] = None,
        filters: typing.Optional[typing.List[str]] = None,
        stats_groups: typing.Optional[typing.List[str]] = None,
        extended: typing.Optional[bool] = None,
        **kwargs
    ) -> stats.GetResponseModel:
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
        model = stats.GetResponse
        return model(**response).response

    async def get_post_reach(
        self, owner_id: str, post_ids: typing.List[int], **kwargs
    ) -> stats.GetPostReachResponseModel:
        """Returns stats for a wall post.
        :param owner_id: post owner community id. Specify with "-" sign.
        :param post_ids: wall posts id
        """

        params = self.get_set_params(locals())
        response = await self.api.request("stats.getPostReach", params)
        model = stats.GetPostReachResponse
        return model(**response).response

    async def track_visitor(
        self, id: str, **kwargs
    ) -> base.OkResponseModel:
        """stats.trackVisitor method
        :param id:
        """

        params = self.get_set_params(locals())
        response = await self.api.request("stats.trackVisitor", params)
        model = base.OkResponse
        return model(**response).response
