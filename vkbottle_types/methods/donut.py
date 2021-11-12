import typing
from .base_category import BaseCategory
from vkbottle_types.responses.groups import GetMembersFieldsResponse
from vkbottle_types.responses.donut import (
    DonutDonatorSubscriptionInfo,
    GetSubscriptionResponse,
    GetSubscriptionsResponse,
    GetSubscriptionsResponseModel
)
from vkbottle_types.responses.base import BaseBoolInt, BoolResponse


class DonutCategory(BaseCategory):
    async def get_friends(
        self,
        owner_id: int,
        offset: typing.Optional[int] = None,
        count: typing.Optional[int] = None,
        fields: typing.Optional[typing.List[str]] = None,
        **kwargs
    ) -> GetMembersFieldsResponse:
        """donut.getFriends method
        :param owner_id:
        :param offset:
        :param count:
        :param fields:
        """

        params = self.get_set_params(locals())
        response = await self.api.request("donut.getFriends", params)
        model = GetMembersFieldsResponse
        return model(**response).response

    async def get_subscription(
        self, owner_id: int, **kwargs
    ) -> DonutDonatorSubscriptionInfo:
        """donut.getSubscription method
        :param owner_id:
        """

        params = self.get_set_params(locals())
        response = await self.api.request("donut.getSubscription", params)
        model = GetSubscriptionResponse
        return model(**response).response

    async def get_subscriptions(
        self,
        fields: typing.Optional[typing.List[str]] = None,
        offset: typing.Optional[int] = None,
        count: typing.Optional[int] = None,
        **kwargs
    ) -> GetSubscriptionsResponseModel:
        """Returns a list of user's VK Donut subscriptions.
        :param fields:
        :param offset:
        :param count:
        """

        params = self.get_set_params(locals())
        response = await self.api.request("donut.getSubscriptions", params)
        model = GetSubscriptionsResponse
        return model(**response).response

    async def is_don(
        self, owner_id: int, **kwargs
    ) -> BaseBoolInt:
        """donut.isDon method
        :param owner_id:
        """

        params = self.get_set_params(locals())
        response = await self.api.request("donut.isDon", params)
        model = BoolResponse
        return model(**response).response
