import typing
from typing_extensions import Literal
from .base_category import BaseCategory
from vkbottle_types.responses.notifications import (
    GetResponse,
    GetResponseModel,
    MarkAsViewedResponse,
    NotificationsSendMessageItem,
    SendMessageResponse,
)
from vkbottle_types.responses.base import BaseBoolInt


class NotificationsCategory(BaseCategory):
    async def get(
        self,
        count: typing.Optional[int] = None,
        start_from: typing.Optional[str] = None,
        filters: typing.Optional[typing.List[str]] = None,
        start_time: typing.Optional[int] = None,
        end_time: typing.Optional[int] = None,
        **kwargs
    ) -> GetResponseModel:
        """Returns a list of notifications about other users' feedback to the current user's wall posts.

        :param count: Number of notifications to return.
        :param start_from:
        :param filters: Type of notifications to return: 'wall' — wall posts, 'mentions' — mentions in wall posts, comments, or topics, 'comments' — comments to wall posts, photos, and videos, 'likes' — likes, 'reposted' — wall posts that are copied from the current user's wall, 'followers' — new followers, 'friends' — accepted friend requests
        :param start_time: Earliest timestamp (in Unix time) of a notification to return. By default, 24 hours ago.
        :param end_time: Latest timestamp (in Unix time) of a notification to return. By default, the current time.
        """

        params = self.get_set_params(locals())
        response = await self.api.request("notifications.get", params)
        model = GetResponse
        return model(**response).response

    async def mark_as_viewed(self, **kwargs) -> BaseBoolInt:
        """Resets the counter of new notifications about other users' feedback to the current user's wall posts."""

        params = self.get_set_params(locals())
        response = await self.api.request("notifications.markAsViewed", params)
        model = MarkAsViewedResponse
        return model(**response).response

    async def send_message(
        self,
        user_ids: typing.List[int],
        message: str,
        fragment: typing.Optional[str] = None,
        group_id: typing.Optional[int] = None,
        random_id: typing.Optional[int] = None,
        sending_mode: Literal["delayed", "delayed_push", "immediately"] = None,
        **kwargs
    ) -> typing.List[NotificationsSendMessageItem]:
        """notifications.sendMessage method

        :param user_ids:
        :param message:
        :param fragment:
        :param group_id:
        :param random_id:
        :param sending_mode: Type of sending (delivering) notifications: 'immediately' — push and bell notifications will be delivered as soon as possible, 'delayed' — push and bell notifications will be delivered in the most comfortable time for the user, 'delayed_push' — only push notifications will be delivered in the most comfortable time, while the bell notifications will be delivered as soon as possible
        """

        params = self.get_set_params(locals())
        response = await self.api.request("notifications.sendMessage", params)
        model = SendMessageResponse
        return model(**response).response
