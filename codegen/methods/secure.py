import typing

from vkbottle_types.methods.base_category import BaseCategory
from vkbottle_types.objects import (
    SecureGiveEventStickerItem,
    SecureLevel,
    SecureSmsNotification,
    SecureTokenChecked,
    SecureTransaction,
)
from vkbottle_types.responses.base import (
    BaseOkResponse,
    BaseOkResponseModel,
)
from vkbottle_types.responses.base_response import DictResponse
from vkbottle_types.responses.secure import *  # noqa: F401,F403  # type: ignore


class SecureCategory(BaseCategory):
    async def add_app_event(
        self,
        activity_id: int,
        user_id: typing.Optional[int] = None,
        value: typing.Optional[int] = None,
        **kwargs: typing.Any,
    ) -> BaseOkResponseModel:
        """Method `secure.addAppEvent()`

        :param activity_id: there are 2 default activities: , * 1 - level. Works similar to ,, * 2 - points, saves points amount, Any other value is for saving completed missions
        :param user_id: ID of a user to save the data
        :param value: depends on activity_id: * 1 - number, current level number,, * 2 - number, current user's points amount, , Any other value is ignored
        """

        params = self.get_set_params(locals())
        response = await self.api.request("secure.addAppEvent", params)
        model = BaseOkResponse
        return model(**response).response

    async def check_token(
        self,
        ip: typing.Optional[str] = None,
        token: typing.Optional[str] = None,
        **kwargs: typing.Any,
    ) -> "SecureTokenChecked":
        """Method `secure.checkToken()`

        :param ip: user 'ip address'. Note that user may access using the 'ipv6' address, in this case it is required to transmit the 'ipv6' address. If not transmitted, the address will not be checked.
        :param token: client 'access_token'
        """

        params = self.get_set_params(locals())
        response = await self.api.request("secure.checkToken", params)
        model = SecureCheckTokenResponse
        return model(**response).response

    async def get_app_balance(
        self,
        **kwargs: typing.Any,
    ) -> int:
        """Method `secure.getAppBalance()`"""

        params = self.get_set_params(locals())
        response = await self.api.request("secure.getAppBalance", params)
        model = SecureGetAppBalanceResponse
        return model(**response).response

    async def get_smshistory(
        self,
        date_from: typing.Optional[int] = None,
        date_to: typing.Optional[int] = None,
        limit: typing.Optional[int] = None,
        user_id: typing.Optional[int] = None,
        **kwargs: typing.Any,
    ) -> typing.List[SecureSmsNotification]:
        """Method `secure.getSMSHistory()`

        :param date_from: filter by start date. It is set as UNIX-time.
        :param date_to: filter by end date. It is set as UNIX-time.
        :param limit: number of returned posts. By default - 1000.
        :param user_id:
        """

        params = self.get_set_params(locals())
        response = await self.api.request("secure.getSMSHistory", params)
        model = SecureGetSMSHistoryResponse
        return model(**response).response

    async def get_transactions_history(
        self,
        date_from: typing.Optional[int] = None,
        date_to: typing.Optional[int] = None,
        limit: typing.Optional[int] = None,
        type: typing.Optional[int] = None,
        uid_from: typing.Optional[int] = None,
        uid_to: typing.Optional[int] = None,
        **kwargs: typing.Any,
    ) -> typing.List[SecureTransaction]:
        """Method `secure.getTransactionsHistory()`

        :param date_from:
        :param date_to:
        :param limit:
        :param type:
        :param uid_from:
        :param uid_to:
        """

        params = self.get_set_params(locals())
        response = await self.api.request("secure.getTransactionsHistory", params)
        model = SecureGetTransactionsHistoryResponse
        return model(**response).response

    async def get_user_level(
        self,
        user_ids: typing.List[int],
        **kwargs: typing.Any,
    ) -> typing.List[SecureLevel]:
        """Method `secure.getUserLevel()`

        :param user_ids:
        """

        params = self.get_set_params(locals())
        response = await self.api.request("secure.getUserLevel", params)
        model = SecureGetUserLevelResponse
        return model(**response).response

    async def give_event_sticker(
        self,
        achievement_id: int,
        user_ids: typing.List[int],
        **kwargs: typing.Any,
    ) -> typing.List[SecureGiveEventStickerItem]:
        """Method `secure.giveEventSticker()`

        :param achievement_id:
        :param user_ids:
        """

        params = self.get_set_params(locals())
        response = await self.api.request("secure.giveEventSticker", params)
        model = SecureGiveEventStickerResponse
        return model(**response).response

    async def send_notification(
        self,
        message: str,
        notification_id: typing.Optional[int] = None,
        promo_id: typing.Optional[int] = None,
        user_id: typing.Optional[int] = None,
        user_ids: typing.Optional[typing.List[int]] = None,
        **kwargs: typing.Any,
    ) -> typing.List[int]:
        """Method `secure.sendNotification()`

        :param message: notification text which should be sent in 'UTF-8' encoding ('254' characters maximum).
        :param notification_id:
        :param promo_id:
        :param user_id:
        :param user_ids:
        """

        params = self.get_set_params(locals())
        response = await self.api.request("secure.sendNotification", params)
        model = SecureSendNotificationResponse
        return model(**response).response

    async def send_smsnotification(
        self,
        message: str,
        user_id: int,
        **kwargs: typing.Any,
    ) -> BaseOkResponseModel:
        """Method `secure.sendSMSNotification()`

        :param message: 'SMS' text to be sent in 'UTF-8' encoding. Only Latin letters and numbers are allowed. Maximum size is '160' characters.
        :param user_id: ID of the user to whom SMS notification is sent. The user shall allow the application to send him/her notifications (, +1).
        """

        params = self.get_set_params(locals())
        response = await self.api.request("secure.sendSMSNotification", params)
        model = BaseOkResponse
        return model(**response).response

    async def set_counter(
        self,
        counter: typing.Optional[int] = None,
        counters: typing.Optional[typing.List[str]] = None,
        increment: typing.Optional[bool] = None,
        user_id: typing.Optional[int] = None,
        **kwargs: typing.Any,
    ) -> typing.Dict[str, typing.Any]:
        """Method `secure.setCounter()`

        :param counter: counter value.
        :param counters:
        :param increment:
        :param user_id:
        """

        params = self.get_set_params(locals())
        response = await self.api.request("secure.setCounter", params)
        model = DictResponse
        return model(**response).response


__all__ = ("SecureCategory",)
