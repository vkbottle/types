from typing import List, Optional

from vkbottle_types.responses import base, stats

from .base_category import BaseCategory


class StatsCategory(BaseCategory):
    async def get(
        self,
        group_id: Optional[int] = None,
        app_id: Optional[int] = None,
        timestamp_from: Optional[int] = None,
        timestamp_to: Optional[int] = None,
        interval: Optional[str] = None,
        intervals_count: Optional[int] = None,
        filters: Optional[List[str]] = None,
        stats_groups: Optional[List[str]] = None,
        extended: Optional[bool] = None,
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
        self, owner_id: str, post_ids: List[int], **kwargs
    ) -> stats.GetPostReachResponseModel:
        """Returns stats for a wall post.
        :param owner_id: post owner community id. Specify with "-" sign.
        :param post_ids: wall posts id
        """

        params = self.get_set_params(locals())
        response = await self.api.request("stats.getPostReach", params)
        model = stats.GetPostReachResponse
        return model(**response).response

    async def track_visitor(self, id: str, **kwargs) -> base.OkResponseModel:
        """stats.trackVisitor method
        :param id:
        """

        params = self.get_set_params(locals())
        response = await self.api.request("stats.trackVisitor", params)
        model = base.OkResponse
        return model(**response).response
