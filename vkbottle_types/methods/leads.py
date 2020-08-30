from typing import Optional

from vkbottle_types.responses import leads
from .base_category import BaseCategory


class LeadsCategory(BaseCategory):
    async def check_user(
        self,
        lead_id: int,
        test_result: Optional[int] = None,
        test_mode: Optional[bool] = None,
        auto_start: Optional[bool] = None,
        age: Optional[int] = None,
        country: Optional[str] = None,
        **kwargs
    ) -> leads.CheckUserResponseModel:
        """Checks if the user can start the lead.
        :param lead_id: Lead ID.
        :param test_result: Value to be return in 'result' field when test mode is used.
        :param test_mode:
        :param auto_start:
        :param age: User age.
        :param country: User country code.
        """

        params = self.get_set_params(locals())
        return leads.CheckUserResponse(
            **await self.api.request("leads.checkUser", params)
        ).response

    async def complete(
        self, vk_sid: str, secret: str, comment: Optional[str] = None, **kwargs
    ) -> leads.CompleteResponseModel:
        """Completes the lead started by user.
        :param vk_sid: Session obtained as GET parameter when session started.
        :param secret: Secret key from the lead testing interface.
        :param comment: Comment text.
        """

        params = self.get_set_params(locals())
        return leads.CompleteResponse(
            **await self.api.request("leads.complete", params)
        ).response

    async def get_stats(
        self,
        lead_id: int,
        secret: Optional[str] = None,
        date_start: Optional[str] = None,
        date_end: Optional[str] = None,
        **kwargs
    ) -> leads.GetStatsResponseModel:
        """Returns lead stats data.
        :param lead_id: Lead ID.
        :param secret: Secret key obtained from the lead testing interface.
        :param date_start: Day to start stats from (YYYY_MM_DD, e.g.2011-09-17).
        :param date_end: Day to finish stats (YYYY_MM_DD, e.g.2011-09-17).
        """

        params = self.get_set_params(locals())
        return leads.GetStatsResponse(
            **await self.api.request("leads.getStats", params)
        ).response

    async def get_users(
        self,
        offer_id: int,
        secret: str,
        offset: Optional[int] = None,
        count: Optional[int] = None,
        status: Optional[int] = None,
        reverse: Optional[bool] = None,
        **kwargs
    ) -> leads.GetUsersResponseModel:
        """Returns a list of last user actions for the offer.
        :param offer_id: Offer ID.
        :param secret: Secret key obtained in the lead testing interface.
        :param offset: Offset needed to return a specific subset of results.
        :param count: Number of results to return.
        :param status: Action type. Possible values: *'0' — start,, *'1' — finish,, *'2' — blocking users,, *'3' — start in a test mode,, *'4' — finish in a test mode.
        :param reverse: Sort order. Possible values: *'1' — chronological,, *'0' — reverse chronological.
        """

        params = self.get_set_params(locals())
        return leads.GetUsersResponse(
            **await self.api.request("leads.getUsers", params)
        ).response

    async def metric_hit(self, data: str, **kwargs) -> leads.MetricHitResponseModel:
        """Counts the metric event.
        :param data: Metric data obtained in the lead interface.
        """

        params = self.get_set_params(locals())
        return leads.MetricHitResponse(
            **await self.api.request("leads.metricHit", params)
        ).response

    async def start(
        self,
        lead_id: int,
        secret: str,
        uid: Optional[int] = None,
        aid: Optional[int] = None,
        test_mode: Optional[bool] = None,
        force: Optional[bool] = None,
        **kwargs
    ) -> leads.StartResponseModel:
        """Creates new session for the user passing the offer.
        :param lead_id: Lead ID.
        :param secret: Secret key from the lead testing interface.
        :param uid:
        :param aid:
        :param test_mode:
        :param force:
        """

        params = self.get_set_params(locals())
        return leads.StartResponse(
            **await self.api.request("leads.start", params)
        ).response
