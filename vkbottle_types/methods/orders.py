import typing
from .base_category import BaseCategory
from vkbottle_types.responses import orders


class OrdersCategory(BaseCategory):
    async def cancel_subscription(
        self,
        user_id: int,
        subscription_id: int,
        pending_cancel: typing.Optional[bool] = None,
        **kwargs
    ) -> orders.BaseBoolInt:
        """orders.cancelSubscription method
        :param user_id:
        :param subscription_id:
        :param pending_cancel:
        """

        params = self.get_set_params(locals())
        response = await self.api.request("orders.cancelSubscription", params)
        model = orders.CancelSubscriptionResponse
        return model(**response).response

    async def change_state(
        self,
        order_id: int,
        action: str,
        app_order_id: typing.Optional[int] = None,
        test_mode: typing.Optional[bool] = None,
        **kwargs
    ) -> str:
        """Changes order status.
        :param order_id: order ID.
        :param action: action to be done with the order. Available actions: *cancel — to cancel unconfirmed order. *charge — to confirm unconfirmed order. Applies only if processing of [vk.com/dev/payments_status|order_change_state] notification failed. *refund — to cancel confirmed order.
        :param app_order_id: internal ID of the order in the application.
        :param test_mode: if this parameter is set to 1, this method returns a list of test mode orders. By default — 0.
        """

        params = self.get_set_params(locals())
        response = await self.api.request("orders.changeState", params)
        model = orders.ChangeStateResponse
        return model(**response).response

    async def get(
        self,
        offset: typing.Optional[int] = None,
        count: typing.Optional[int] = None,
        test_mode: typing.Optional[bool] = None,
        **kwargs
    ) -> typing.List[orders.OrdersOrder]:
        """Returns a list of orders.
        :param offset:
        :param count: number of returned orders.
        :param test_mode: if this parameter is set to 1, this method returns a list of test mode orders. By default — 0.
        """

        params = self.get_set_params(locals())
        response = await self.api.request("orders.get", params)
        model = orders.GetResponse
        return model(**response).response

    async def get_amount(
        self, user_id: int, votes: typing.List[str], **kwargs
    ) -> typing.List[orders.OrdersAmount]:
        """orders.getAmount method
        :param user_id:
        :param votes:
        """

        params = self.get_set_params(locals())
        response = await self.api.request("orders.getAmount", params)
        model = orders.GetAmountResponse
        return model(**response).response

    async def get_by_id(
        self,
        order_id: typing.Optional[int] = None,
        order_ids: typing.Optional[typing.List[int]] = None,
        test_mode: typing.Optional[bool] = None,
        **kwargs
    ) -> typing.List[orders.OrdersOrder]:
        """Returns information about orders by their IDs.
        :param order_id: order ID.
        :param order_ids: order IDs (when information about several orders is requested).
        :param test_mode: if this parameter is set to 1, this method returns a list of test mode orders. By default — 0.
        """

        params = self.get_set_params(locals())
        response = await self.api.request("orders.getById", params)
        model = orders.GetByIdResponse
        return model(**response).response

    async def get_user_subscription_by_id(
        self, user_id: int, subscription_id: int, **kwargs
    ) -> orders.OrdersSubscription:
        """orders.getUserSubscriptionById method
        :param user_id:
        :param subscription_id:
        """

        params = self.get_set_params(locals())
        response = await self.api.request("orders.getUserSubscriptionById", params)
        model = orders.GetUserSubscriptionByIdResponse
        return model(**response).response

    async def get_user_subscriptions(
        self, user_id: int, **kwargs
    ) -> orders.GetUserSubscriptionsResponseModel:
        """orders.getUserSubscriptions method
        :param user_id:
        """

        params = self.get_set_params(locals())
        response = await self.api.request("orders.getUserSubscriptions", params)
        model = orders.GetUserSubscriptionsResponse
        return model(**response).response

    async def update_subscription(
        self, user_id: int, subscription_id: int, price: int, **kwargs
    ) -> orders.BaseBoolInt:
        """orders.updateSubscription method
        :param user_id:
        :param subscription_id:
        :param price:
        """

        params = self.get_set_params(locals())
        response = await self.api.request("orders.updateSubscription", params)
        model = orders.UpdateSubscriptionResponse
        return model(**response).response
