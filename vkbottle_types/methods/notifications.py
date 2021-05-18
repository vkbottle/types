from typing import List, Optional

from vkbottle_types.responses import notifications

from .base_category import BaseCategory


class NotificationsCategory(BaseCategory):
    async def get(
        self,
        count: Optional[int] = None,
        start_from: Optional[str] = None,
        filters: Optional[List[str]] = None,
        start_time: Optional[int] = None,
        end_time: Optional[int] = None,
        **kwargs
    ) -> notifications.GetResponseModel:
        """Returns a list of notifications about other users' feedback to the current user's wall posts.
        :param count: Number of notifications to return.
        :param start_from:
        :param filters: Type of notifications to return: 'wall' — wall posts, 'mentions' — mentions in wall posts, comments, or topics, 'comments' — comments to wall posts, photos, and videos, 'likes' — likes, 'reposted' — wall posts that are copied from the current user's wall, 'followers' — new followers, 'friends' — accepted friend requests
        :param start_time: Earliest timestamp (in Unix time) of a notification to return. By default, 24 hours ago.
        :param end_time: Latest timestamp (in Unix time) of a notification to return. By default, the current time.
        """

        params = self.get_set_params(locals())
        response = await self.api.request("notifications.get", params)
        model = notifications.GetResponse
        return model(**response).response

    async def mark_as_viewed(self, **kwargs) -> notifications.MarkAsViewedResponseModel:
        """Resets the counter of new notifications about other users' feedback to the current user's wall posts."""

        params = self.get_set_params(locals())
        response = await self.api.request("notifications.markAsViewed", params)
        model = notifications.MarkAsViewedResponse
        return model(**response).response

    async def send_message(
        self,
        user_ids: List[int],
        message: str,
        fragment: Optional[str] = None,
        group_id: Optional[int] = None,
        random_id: Optional[int] = None,
        **kwargs
    ) -> notifications.SendMessageResponseModel:
        """notifications.sendMessage method
        :param user_ids:
        :param message:
        :param fragment:
        :param group_id:
        :param random_id:
        """

        params = self.get_set_params(locals())
        response = await self.api.request("notifications.sendMessage", params)
        model = notifications.SendMessageResponse
        return model(**response).response
