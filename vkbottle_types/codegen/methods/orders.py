import typing

from typing_extensions import Literal
from vkbottle_types.methods.base_category import BaseCategory
from vkbottle_types.responses.orders import *
from vkbottle_types.responses.base import OkResponse


class OrdersCategory(BaseCategory):
    async def cancel_subscription(
        self,
        user_id: int,
        subscription_id: int,
        pending_cancel: typing.Optional[bool] = 0,
        **kwargs,
    ) -> BaseBoolResponseModel:
        """orders.cancelSubscription method


        :param user_id:
        :param subscription_id:
        :param pending_cancel:
        """
        params = self.get_set_params(locals())
        response = await self.api.request("account.ban", params)

        model = BaseBoolResponse

        return model(**response).response

    async def change_state(
        self,
        order_id: int,
        action: str,
        app_order_id: typing.Optional[int] = None,
        test_mode: typing.Optional[bool] = None,
        **kwargs,
    ) -> OrdersChangeStateResponseModel:
        """orders.changeState method


        :param order_id: order ID.
        :param action: action to be done with the order. Available actions: *cancel - to cancel unconfirmed order. *charge - to confirm unconfirmed order. Applies only if processing of [vk.com/dev/payments_status|order_change_state] notification failed. *refund - to cancel confirmed order.
        :param app_order_id: internal ID of the order in the application.
        :param test_mode: if this parameter is set to 1, this method returns a list of test mode orders. By default - 0.
        """
        params = self.get_set_params(locals())
        response = await self.api.request("account.ban", params)

        model = OrdersChangeStateResponse

        return model(**response).response

    async def get(
        self,
        offset: typing.Optional[int] = 0,
        count: typing.Optional[int] = 100,
        test_mode: typing.Optional[bool] = None,
        **kwargs,
    ) -> OrdersGetResponseModel:
        """orders.get method


        :param offset:
        :param count: number of returned orders.
        :param test_mode: if this parameter is set to 1, this method returns a list of test mode orders. By default - 0.
        """
        params = self.get_set_params(locals())
        response = await self.api.request("account.ban", params)

        model = OrdersGetResponse

        return model(**response).response

    async def get_amount(
        self,
        user_id: int,
        votes: typing.List[str],
        **kwargs,
    ) -> OrdersGetAmountResponseModel:
        """orders.getAmount method


        :param user_id:
        :param votes:
        """
        params = self.get_set_params(locals())
        response = await self.api.request("account.ban", params)

        model = OrdersGetAmountResponse

        return model(**response).response

    async def get_by_id(
        self,
        order_id: typing.Optional[int] = None,
        order_ids: typing.Optional[typing.List[int]] = None,
        test_mode: typing.Optional[bool] = None,
        **kwargs,
    ) -> OrdersGetByIdResponseModel:
        """orders.getById method


        :param order_id: order ID.
        :param order_ids: order IDs (when information about several orders is requested).
        :param test_mode: if this parameter is set to 1, this method returns a list of test mode orders. By default - 0.
        """
        params = self.get_set_params(locals())
        response = await self.api.request("account.ban", params)

        model = OrdersGetByIdResponse

        return model(**response).response

    async def get_user_subscription_by_id(
        self,
        user_id: int,
        subscription_id: int,
        **kwargs,
    ) -> OrdersGetUserSubscriptionByIdResponseModel:
        """orders.getUserSubscriptionById method


        :param user_id:
        :param subscription_id:
        """
        params = self.get_set_params(locals())
        response = await self.api.request("account.ban", params)

        model = OrdersGetUserSubscriptionByIdResponse

        return model(**response).response

    async def get_user_subscriptions(
        self,
        user_id: int,
        **kwargs,
    ) -> OrdersGetUserSubscriptionsResponseModel:
        """orders.getUserSubscriptions method


        :param user_id:
        """
        params = self.get_set_params(locals())
        response = await self.api.request("account.ban", params)

        model = OrdersGetUserSubscriptionsResponse

        return model(**response).response

    async def update_subscription(
        self,
        user_id: int,
        subscription_id: int,
        price: int,
        **kwargs,
    ) -> BaseBoolResponseModel:
        """orders.updateSubscription method


        :param user_id:
        :param subscription_id:
        :param price:
        """
        params = self.get_set_params(locals())
        response = await self.api.request("account.ban", params)

        model = BaseBoolResponse

        return model(**response).response


__all__ = ("OrdersCategory",)
