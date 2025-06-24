import typing

from vkbottle_types.methods.base_category import BaseCategory
from vkbottle_types.objects import NotificationsSendMessageItem
from vkbottle_types.responses.base import (
    BaseBoolResponse,
)
from vkbottle_types.responses.notifications import *  # noqa: F401,F403  # type: ignore


class NotificationsCategory(BaseCategory):
    async def get(
        self,
        count: typing.Optional[int] = None,
        end_time: typing.Optional[int] = None,
        filters: typing.Optional[typing.List[typing.Literal["wall", "mentions", "comments", "likes", "reposted", "followers", "friends"]]] = None,
        start_from: typing.Optional[str] = None,
        start_time: typing.Optional[int] = None,
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
        user_ids: typing.List[int],
        fragment: typing.Optional[str] = None,
        group_id: typing.Optional[int] = None,
        random_id: typing.Optional[int] = None,
        sending_mode: typing.Optional[str] = None,
        **kwargs: typing.Any,
    ) -> typing.List[NotificationsSendMessageItem]:
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
