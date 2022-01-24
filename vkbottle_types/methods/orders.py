import typing

from typing_extensions import Literal
from vkbottle_types.responses.base import BaseBoolInt
from vkbottle_types.responses.orders import (
    CancelSubscriptionResponse,
    ChangeStateResponse,
    GetAmountResponse,
    GetByIdResponse,
    GetResponse,
    GetUserSubscriptionByIdResponse,
    GetUserSubscriptionsResponse,
    GetUserSubscriptionsResponseModel,
    OrdersAmount,
    OrdersOrder,
    OrdersSubscription,
    UpdateSubscriptionResponse,
)

from .base_category import BaseCategory


class OrdersCategory(BaseCategory):
    async def cancel_subscription(
        self,
        user_id: int,
        subscription_id: int,
        pending_cancel: typing.Optional[bool] = None,
        **kwargs
    ) -> BaseBoolInt:
        """orders.cancelSubscription method

        :param user_id:
        :param subscription_id:
        :param pending_cancel:
        """

        params = self.get_set_params(locals())
        response = await self.api.request("orders.cancelSubscription", params)
        model = CancelSubscriptionResponse
        return model(**response).response

    async def change_state(
        self,
        order_id: int,
        action: Literal["cancel", "charge", "refund"],
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
        model = ChangeStateResponse
        return model(**response).response

    async def get(
        self,
        offset: typing.Optional[int] = None,
        count: typing.Optional[int] = None,
        test_mode: typing.Optional[bool] = None,
        **kwargs
    ) -> typing.List[OrdersOrder]:
        """Returns a list of orders.

        :param offset:
        :param count: number of returned orders.
        :param test_mode: if this parameter is set to 1, this method returns a list of test mode orders. By default — 0.
        """

        params = self.get_set_params(locals())
        response = await self.api.request("orders.get", params)
        model = GetResponse
        return model(**response).response

    async def get_amount(
        self, user_id: int, votes: typing.List[str], **kwargs
    ) -> typing.List[OrdersAmount]:
        """orders.getAmount method

        :param user_id:
        :param votes:
        """

        params = self.get_set_params(locals())
        response = await self.api.request("orders.getAmount", params)
        model = GetAmountResponse
        return model(**response).response

    async def get_by_id(
        self,
        order_id: typing.Optional[int] = None,
        order_ids: typing.Optional[typing.List[int]] = None,
        test_mode: typing.Optional[bool] = None,
        **kwargs
    ) -> typing.List[OrdersOrder]:
        """Returns information about orders by their IDs.

        :param order_id: order ID.
        :param order_ids: order IDs (when information about several orders is requested).
        :param test_mode: if this parameter is set to 1, this method returns a list of test mode orders. By default — 0.
        """

        params = self.get_set_params(locals())
        response = await self.api.request("orders.getById", params)
        model = GetByIdResponse
        return model(**response).response

    async def get_user_subscription_by_id(
        self, user_id: int, subscription_id: int, **kwargs
    ) -> OrdersSubscription:
        """orders.getUserSubscriptionById method

        :param user_id:
        :param subscription_id:
        """

        params = self.get_set_params(locals())
        response = await self.api.request("orders.getUserSubscriptionById", params)
        model = GetUserSubscriptionByIdResponse
        return model(**response).response

    async def get_user_subscriptions(
        self, user_id: int, **kwargs
    ) -> GetUserSubscriptionsResponseModel:
        """orders.getUserSubscriptions method

        :param user_id:
        """

        params = self.get_set_params(locals())
        response = await self.api.request("orders.getUserSubscriptions", params)
        model = GetUserSubscriptionsResponse
        return model(**response).response

    async def update_subscription(
        self, user_id: int, subscription_id: int, price: int, **kwargs
    ) -> BaseBoolInt:
        """orders.updateSubscription method

        :param user_id:
        :param subscription_id:
        :param price:
        """

        params = self.get_set_params(locals())
        response = await self.api.request("orders.updateSubscription", params)
        model = UpdateSubscriptionResponse
        return model(**response).response
