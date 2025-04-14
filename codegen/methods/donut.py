import typing

from vkbottle_types.methods.base_category import BaseCategory
from vkbottle_types.objects import BaseUserGroupFields, DonutDonatorSubscriptionInfo
from vkbottle_types.responses.base import (
    BaseBoolResponse,
)
from vkbottle_types.responses.donut import *  # noqa: F401,F403  # type: ignore


class DonutCategory(BaseCategory):
    async def get_friends(
        self,
        owner_id: int,
        count: typing.Optional[int] = None,
        fields: typing.Optional[typing.List[str]] = None,
        offset: typing.Optional[int] = None,
        **kwargs: typing.Any,
    ) -> GroupsGetMembersFieldsResponseModel:
        """Method `donut.getFriends()`

        :param owner_id:
        :param count:
        :param fields:
        :param offset:
        """

        params = self.get_set_params(locals())
        response = await self.api.request("donut.getFriends", params)
        model = GroupsGetMembersFieldsResponse
        return model(**response).response

    async def get_subscription(
        self,
        owner_id: int,
        **kwargs: typing.Any,
    ) -> "DonutDonatorSubscriptionInfo":
        """Method `donut.getSubscription()`

        :param owner_id:
        """

        params = self.get_set_params(locals())
        response = await self.api.request("donut.getSubscription", params)
        model = DonutGetSubscriptionResponse
        return model(**response).response

    async def get_subscriptions(
        self,
        count: typing.Optional[int] = None,
        fields: typing.Optional[typing.List[BaseUserGroupFields]] = None,
        offset: typing.Optional[int] = None,
        **kwargs: typing.Any,
    ) -> DonutGetSubscriptionsResponseModel:
        """Method `donut.getSubscriptions()`

        :param count:
        :param fields:
        :param offset:
        """

        params = self.get_set_params(locals())
        response = await self.api.request("donut.getSubscriptions", params)
        model = DonutGetSubscriptionsResponse
        return model(**response).response

    async def is_don(
        self,
        owner_id: int,
        **kwargs: typing.Any,
    ) -> bool:
        """Method `donut.isDon()`

        :param owner_id:
        """

        params = self.get_set_params(locals())
        response = await self.api.request("donut.isDon", params)
        model = BaseBoolResponse
        return model(**response).response


__all__ = ("DonutCategory",)
