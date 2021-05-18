import typing

from vkbottle_types.responses import base, donut

from .base_category import BaseCategory


class DonutCategory(BaseCategory):
    async def get_friends(
        self,
        owner_id: int,
        offset: typing.Optional[int] = None,
        count: typing.Optional[int] = None,
        fields: typing.Optional[typing.List[str]] = None,
        **kwargs
    ) -> donut.GroupsGetmembersFieldsResponseModel:
        """donut.getFriends method
        :param owner_id:
        :param offset:
        :param count:
        :param fields:
        """

        params = self.get_set_params(locals())
        response = await self.api.request("donut.getFriends", params)
        model = donut.GroupsGetmembersFieldsResponse
        return model(**response).response

    async def get_subscription(
        self, owner_id: int, **kwargs
    ) -> donut.GetSubscriptionResponseModel:
        """donut.getSubscription method
        :param owner_id:
        """

        params = self.get_set_params(locals())
        response = await self.api.request("donut.getSubscription", params)
        model = donut.GetSubscriptionResponse
        return model(**response).response

    async def get_subscriptions(
        self,
        fields: typing.Optional[typing.List[str]] = None,
        offset: typing.Optional[int] = None,
        count: typing.Optional[int] = None,
        **kwargs
    ) -> donut.GetSubscriptionsResponseModel:
        """Returns a list of user's VK Donut subscriptions.
        :param fields:
        :param offset:
        :param count:
        """

        params = self.get_set_params(locals())
        response = await self.api.request("donut.getSubscriptions", params)
        model = donut.GetSubscriptionsResponse
        return model(**response).response

    async def is_don(self, owner_id: int, **kwargs) -> base.BoolModel:
        """donut.isDon method
        :param owner_id:
        """

        params = self.get_set_params(locals())
        response = await self.api.request("donut.isDon", params)
        model = base.Bool
        return model(**response).response
