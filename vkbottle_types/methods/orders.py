from typing import Optional, List

from vkbottle_types.responses import orders
from .base_category import BaseCategory


class OrdersCategory(BaseCategory):
    async def cancel_subscription(
        self,
        user_id: int,
        subscription_id: int,
        pending_cancel: Optional[bool] = None,
        **kwargs
    ) -> orders.CancelSubscriptionResponseModel:
        """orders.cancelSubscription method
        :param user_id:
        :param subscription_id:
        :param pending_cancel:
        """

        params = self.get_set_params(locals())
        return orders.CancelSubscriptionResponse(
            **await self.api.request("orders.cancelSubscription", params)
        )

    async def change_state(
        self,
        order_id: int,
        action: str,
        app_order_id: Optional[int] = None,
        test_mode: Optional[bool] = None,
        **kwargs
    ) -> orders.ChangeStateResponseModel:
        """Changes order status.
        :param order_id: order ID.
        :param action: action to be done with the order. Available actions: *cancel — to cancel unconfirmed order. *charge — to confirm unconfirmed order. Applies only if processing of [vk.com/dev/payments_status|order_change_state] notification failed. *refund — to cancel confirmed order.
        :param app_order_id: internal ID of the order in the application.
        :param test_mode: if this parameter is set to 1, this method returns a list of test mode orders. By default — 0.
        """

        params = self.get_set_params(locals())
        return orders.ChangeStateResponse(
            **await self.api.request("orders.changeState", params)
        )

    async def get(
        self,
        offset: Optional[int] = None,
        count: Optional[int] = None,
        test_mode: Optional[bool] = None,
        **kwargs
    ) -> orders.GetResponseModel:
        """Returns a list of orders.
        :param offset:
        :param count: number of returned orders.
        :param test_mode: if this parameter is set to 1, this method returns a list of test mode orders. By default — 0.
        """

        params = self.get_set_params(locals())
        return orders.GetResponse(**await self.api.request("orders.get", params))

    async def get_amount(
        self, user_id: int, votes: List[str], **kwargs
    ) -> orders.GetAmountResponseModel:
        """orders.getAmount method
        :param user_id:
        :param votes:
        """

        params = self.get_set_params(locals())
        return orders.GetAmountResponse(
            **await self.api.request("orders.getAmount", params)
        )

    async def get_by_id(
        self,
        order_id: Optional[int] = None,
        order_ids: Optional[List[int]] = None,
        test_mode: Optional[bool] = None,
        **kwargs
    ) -> orders.GetByIdResponseModel:
        """Returns information about orders by their IDs.
        :param order_id: order ID.
        :param order_ids: order IDs (when information about several orders is requested).
        :param test_mode: if this parameter is set to 1, this method returns a list of test mode orders. By default — 0.
        """

        params = self.get_set_params(locals())
        return orders.GetByIdResponse(
            **await self.api.request("orders.getById", params)
        )

    async def get_user_subscription_by_id(
        self, user_id: int, subscription_id: int, **kwargs
    ) -> orders.GetUserSubscriptionByIdResponseModel:
        """orders.getUserSubscriptionById method
        :param user_id:
        :param subscription_id:
        """

        params = self.get_set_params(locals())
        return orders.GetUserSubscriptionByIdResponse(
            **await self.api.request("orders.getUserSubscriptionById", params)
        )

    async def get_user_subscriptions(
        self, user_id: int, **kwargs
    ) -> orders.GetUserSubscriptionsResponseModel:
        """orders.getUserSubscriptions method
        :param user_id:
        """

        params = self.get_set_params(locals())
        return orders.GetUserSubscriptionsResponse(
            **await self.api.request("orders.getUserSubscriptions", params)
        )

    async def update_subscription(
        self, user_id: int, subscription_id: int, price: int, **kwargs
    ) -> orders.UpdateSubscriptionResponseModel:
        """orders.updateSubscription method
        :param user_id:
        :param subscription_id:
        :param price:
        """

        params = self.get_set_params(locals())
        return orders.UpdateSubscriptionResponse(
            **await self.api.request("orders.updateSubscription", params)
        )
