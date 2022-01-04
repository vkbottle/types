import typing
from .base_category import BaseCategory
from vkbottle_types.responses.base import OkResponse
from vkbottle_types.responses.secure import (
    CheckTokenResponse,
    GetAppBalanceResponse,
    GetSMSHistoryResponse,
    GetTransactionsHistoryResponse,
    GetUserLevelResponse,
    GiveEventStickerResponse,
    SecureGiveEventStickerItem,
    SecureLevel,
    SecureSmsNotification,
    SecureTokenChecked,
    SecureTransaction,
    SendNotificationResponse,
)


class SecureCategory(BaseCategory):
    async def add_app_event(
        self,
        user_id: int,
        activity_id: int,
        value: typing.Optional[int] = None,
        **kwargs
    ) -> int:
        """Adds user activity information to an application

        :param user_id: ID of a user to save the data
        :param activity_id: there are 2 default activities: , * 1 - level. Works similar to ,, * 2 - points, saves points amount, Any other value is for saving completed missions
        :param value: depends on activity_id: * 1 - number, current level number,, * 2 - number, current user's points amount, , Any other value is ignored
        """

        params = self.get_set_params(locals())
        response = await self.api.request("secure.addAppEvent", params)
        model = OkResponse
        return model(**response).response

    async def check_token(
        self,
        token: typing.Optional[str] = None,
        ip: typing.Optional[str] = None,
        **kwargs
    ) -> SecureTokenChecked:
        """Checks the user authentication in 'IFrame' and 'Flash' apps using the 'access_token' parameter.

        :param token: client 'access_token'
        :param ip: user 'ip address'. Note that user may access using the 'ipv6' address, in this case it is required to transmit the 'ipv6' address. If not transmitted, the address will not be checked.
        """

        params = self.get_set_params(locals())
        response = await self.api.request("secure.checkToken", params)
        model = CheckTokenResponse
        return model(**response).response

    async def get_app_balance(self, **kwargs) -> int:
        """Returns payment balance of the application in hundredth of a vote."""

        params = self.get_set_params(locals())
        response = await self.api.request("secure.getAppBalance", params)
        model = GetAppBalanceResponse
        return model(**response).response

    async def get_sms_history(
        self,
        user_id: typing.Optional[int] = None,
        date_from: typing.Optional[int] = None,
        date_to: typing.Optional[int] = None,
        limit: typing.Optional[int] = None,
        **kwargs
    ) -> typing.List[SecureSmsNotification]:
        """Shows a list of SMS notifications sent by the application using [vk.com/dev/secure.sendSMSNotification|secure.sendSMSNotification] method.

        :param user_id:
        :param date_from: filter by start date. It is set as UNIX-time.
        :param date_to: filter by end date. It is set as UNIX-time.
        :param limit: number of returned posts. By default — 1000.
        """

        params = self.get_set_params(locals())
        response = await self.api.request("secure.getSMSHistory", params)
        model = GetSMSHistoryResponse
        return model(**response).response

    async def get_transactions_history(
        self,
        type: typing.Optional[int] = None,
        uid_from: typing.Optional[int] = None,
        uid_to: typing.Optional[int] = None,
        date_from: typing.Optional[int] = None,
        date_to: typing.Optional[int] = None,
        limit: typing.Optional[int] = None,
        **kwargs
    ) -> typing.List[SecureTransaction]:
        """Shows history of votes transaction between users and the application.

        :param type:
        :param uid_from:
        :param uid_to:
        :param date_from:
        :param date_to:
        :param limit:
        """

        params = self.get_set_params(locals())
        response = await self.api.request("secure.getTransactionsHistory", params)
        model = GetTransactionsHistoryResponse
        return model(**response).response

    async def get_user_level(
        self, user_ids: typing.List[int], **kwargs
    ) -> typing.List[SecureLevel]:
        """Returns one of the previously set game levels of one or more users in the application.

        :param user_ids:
        """

        params = self.get_set_params(locals())
        response = await self.api.request("secure.getUserLevel", params)
        model = GetUserLevelResponse
        return model(**response).response

    async def give_event_sticker(
        self, user_ids: typing.List[int], achievement_id: int, **kwargs
    ) -> typing.List[SecureGiveEventStickerItem]:
        """Opens the game achievement and gives the user a sticker

        :param user_ids:
        :param achievement_id:
        """

        params = self.get_set_params(locals())
        response = await self.api.request("secure.giveEventSticker", params)
        model = GiveEventStickerResponse
        return model(**response).response

    async def send_notification(
        self,
        message: str,
        user_ids: typing.Optional[typing.List[int]] = None,
        user_id: typing.Optional[int] = None,
        **kwargs
    ) -> typing.List[int]:
        """Sends notification to the user.

        :param message: notification text which should be sent in 'UTF-8' encoding ('254' characters maximum).
        :param user_ids:
        :param user_id:
        """

        params = self.get_set_params(locals())
        response = await self.api.request("secure.sendNotification", params)
        model = SendNotificationResponse
        return model(**response).response

    async def send_sms_notification(self, user_id: int, message: str, **kwargs) -> int:
        """Sends 'SMS' notification to a user's mobile device.

        :param user_id: ID of the user to whom SMS notification is sent. The user shall allow the application to send him/her notifications (, +1).
        :param message: 'SMS' text to be sent in 'UTF-8' encoding. Only Latin letters and numbers are allowed. Maximum size is '160' characters.
        """

        params = self.get_set_params(locals())
        response = await self.api.request("secure.sendSMSNotification", params)
        model = OkResponse
        return model(**response).response

    async def set_counter(
        self,
        counters: typing.Optional[typing.List[str]] = None,
        user_id: typing.Optional[int] = None,
        counter: typing.Optional[int] = None,
        increment: typing.Optional[bool] = None,
        **kwargs
    ) -> int:
        """Sets a counter which is shown to the user in bold in the left menu.

        :param counters:
        :param user_id:
        :param counter: counter value.
        :param increment:
        """

        params = self.get_set_params(locals())
        response = await self.api.request("secure.setCounter", params)
        model = OkResponse
        return model(**response).response
