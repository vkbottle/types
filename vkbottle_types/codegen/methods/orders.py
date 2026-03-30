import typing

from vkbottle_types.methods.base_category import BaseCategory
from vkbottle_types.objects import OrdersAmount, OrdersOrder, OrdersSubscription
from vkbottle_types.responses.base import (
    BaseBoolResponse,
)
from vkbottle_types.responses.orders import *  # noqa: F401,F403  # type: ignore


class OrdersCategory(BaseCategory):
    async def cancel_subscription(
        self,
        subscription_id: int,
        user_id: int,
        pending_cancel: bool | None = None,
        **kwargs: typing.Any,
    ) -> bool:
        """Method `orders.cancelSubscription()`

        :param subscription_id:
        :param user_id:
        :param pending_cancel:
        """

        params = self.get_set_params(locals())
        response = await self.api.request("orders.cancelSubscription", params)
        model = BaseBoolResponse
        return model(**response).response

    async def change_state(
        self,
        action: str,
        order_id: int,
        app_order_id: int | None = None,
        test_mode: bool | None = None,
        **kwargs: typing.Any,
    ) -> str:
        """Method `orders.changeState()`

        :param action: action to be done with the order. Available actions: *cancel - to cancel unconfirmed order. *charge - to confirm unconfirmed order. Applies only if processing of [vk.com/dev/payments_status|order_change_state] notification failed. *refund - to cancel confirmed order.
        :param order_id: order ID.
        :param app_order_id: internal ID of the order in the application.
        :param test_mode: if this parameter is set to 1, this method returns a list of test mode orders. By default - 0.
        """

        params = self.get_set_params(locals())
        response = await self.api.request("orders.changeState", params)
        model = OrdersChangeStateResponse
        return model(**response).response

    async def get(
        self,
        count: int | None = None,
        offset: int | None = None,
        test_mode: bool | None = None,
        **kwargs: typing.Any,
    ) -> list[OrdersOrder]:
        """Method `orders.get()`

        :param count: number of returned orders.
        :param offset:
        :param test_mode: if this parameter is set to 1, this method returns a list of test mode orders. By default - 0.
        """

        params = self.get_set_params(locals())
        response = await self.api.request("orders.get", params)
        model = OrdersGetResponse
        return model(**response).response

    async def get_amount(
        self,
        user_id: int,
        votes: list[str],
        **kwargs: typing.Any,
    ) -> list[OrdersAmount]:
        """Method `orders.getAmount()`

        :param user_id:
        :param votes:
        """

        params = self.get_set_params(locals())
        response = await self.api.request("orders.getAmount", params)
        model = OrdersGetAmountResponse
        return model(**response).response

    async def get_by_id(
        self,
        order_id: int | None = None,
        order_ids: list[int] | None = None,
        test_mode: bool | None = None,
        **kwargs: typing.Any,
    ) -> list[OrdersOrder]:
        """Method `orders.getById()`

        :param order_id: order ID.
        :param order_ids: order IDs (when information about several orders is requested).
        :param test_mode: if this parameter is set to 1, this method returns a list of test mode orders. By default - 0.
        """

        params = self.get_set_params(locals())
        response = await self.api.request("orders.getById", params)
        model = OrdersGetByIdResponse
        return model(**response).response

    async def get_user_subscription_by_id(
        self,
        subscription_id: int,
        user_id: int,
        **kwargs: typing.Any,
    ) -> "OrdersSubscription":
        """Method `orders.getUserSubscriptionById()`

        :param subscription_id:
        :param user_id:
        """

        params = self.get_set_params(locals())
        response = await self.api.request("orders.getUserSubscriptionById", params)
        model = OrdersGetUserSubscriptionByIdResponse
        return model(**response).response

    async def get_user_subscriptions(
        self,
        user_id: int,
        **kwargs: typing.Any,
    ) -> OrdersGetUserSubscriptionsResponseModel:
        """Method `orders.getUserSubscriptions()`

        :param user_id:
        """

        params = self.get_set_params(locals())
        response = await self.api.request("orders.getUserSubscriptions", params)
        model = OrdersGetUserSubscriptionsResponse
        return model(**response).response


__all__ = ("OrdersCategory",)
