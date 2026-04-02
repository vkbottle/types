import typing

from vkbottle_types.methods.base_category import BaseCategory
from vkbottle_types.objects import *
from vkbottle_types.responses.base import (
    BaseBoolResponse,
)
from vkbottle_types.responses.notifications import *  # noqa: F401,F403  # type: ignore


class NotificationsCategory(BaseCategory):
    async def get(
        self,
        count: int | None = None,
        end_time: int | None = None,
        filters: list[typing.Literal["wall", "mentions", "comments", "likes", "reposted", "followers", "friends"]] | None = None,
        start_from: str | None = None,
        start_time: int | None = None,
        **kwargs: typing.Any,
    ) -> NotificationsGetResponseModel:
        """Method `notifications.get()`

        :param count: Number of notifications to return.
        :param end_time: Latest timestamp (in Unix time) of a notification to return. By default, the current time.
        :param filters: Type of notifications to return: 'wall' - wall posts, 'mentions' - mentions in wall posts, comments, or topics, 'comments' - comments to wall posts, photos, and videos, 'likes' - likes, 'reposted' - wall posts that are copied from the current user's wall, 'followers' - new followers, 'friends' - accepted friend requests
        :param start_from:
        :param start_time: Earliest timestamp (in Unix time) of a notification to return. By default, 24 hours ago.
        """

        params = self.get_set_params(locals())
        response = await self.api.request("notifications.get", params)
        model = NotificationsGetResponse
        return model(**response).response

    async def mark_as_viewed(
        self,
        **kwargs: typing.Any,
    ) -> bool:
        """Method `notifications.markAsViewed()`"""

        params = self.get_set_params(locals())
        response = await self.api.request("notifications.markAsViewed", params)
        model = BaseBoolResponse
        return model(**response).response

    async def send_message(
        self,
        message: str,
        user_ids: list[int],
        fragment: str | None = None,
        group_id: int | None = None,
        random_id: int | None = None,
        sending_mode: str | None = None,
        **kwargs: typing.Any,
    ) -> list[NotificationsSendMessageItem]:
        """Method `notifications.sendMessage()`

        :param message:
        :param user_ids:
        :param fragment:
        :param group_id:
        :param random_id:
        :param sending_mode: Type of sending (delivering) notifications: 'immediately' - push and bell notifications will be delivered as soon as possible, 'delayed' - push and bell notifications will be delivered in the most comfortable time for the user, 'delayed_push' - only push notifications will be delivered in the most comfortable time, while the bell notifications will be delivered as soon as possible
        """

        params = self.get_set_params(locals())
        response = await self.api.request("notifications.sendMessage", params)
        model = NotificationsSendMessageResponse
        return model(**response).response


__all__ = ("NotificationsCategory",)
