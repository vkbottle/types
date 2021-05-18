from typing import List, Optional

from vkbottle_types.responses import base, secure

from .base_category import BaseCategory


class SecureCategory(BaseCategory):
    async def add_app_event(
        self, user_id: int, activity_id: int, value: Optional[int] = None, **kwargs
    ) -> base.OkResponseModel:
        """Adds user activity information to an application
        :param user_id: ID of a user to save the data
        :param activity_id: there are 2 default activities: , * 1 – level. Works similar to ,, * 2 – points, saves points amount, Any other value is for saving completed missions
        :param value: depends on activity_id: * 1 – number, current level number,, * 2 – number, current user's points amount, , Any other value is ignored
        """

        params = self.get_set_params(locals())
        response = await self.api.request("secure.addAppEvent", params)
        model = base.OkResponse
        return model(**response).response

    async def check_token(
        self, token: Optional[str] = None, ip: Optional[str] = None, **kwargs
    ) -> secure.CheckTokenResponseModel:
        """Checks the user authentication in 'IFrame' and 'Flash' apps using the 'access_token' parameter.
        :param token: client 'access_token'
        :param ip: user 'ip address'. Note that user may access using the 'ipv6' address, in this case it is required to transmit the 'ipv6' address. If not transmitted, the address will not be checked.
        """

        params = self.get_set_params(locals())
        response = await self.api.request("secure.checkToken", params)
        model = secure.CheckTokenResponse
        return model(**response).response

    async def get_app_balance(self, **kwargs) -> secure.GetAppBalanceResponseModel:
        """Returns payment balance of the application in hundredth of a vote."""

        params = self.get_set_params(locals())
        response = await self.api.request("secure.getAppBalance", params)
        model = secure.GetAppBalanceResponse
        return model(**response).response

    async def get_s_m_s_history(
        self,
        user_id: Optional[int] = None,
        date_from: Optional[int] = None,
        date_to: Optional[int] = None,
        limit: Optional[int] = None,
        **kwargs
    ) -> secure.GetSMSHistoryResponseModel:
        """Shows a list of SMS notifications sent by the application using [vk.com/dev/secure.sendSMSNotification|secure.sendSMSNotification] method.
        :param user_id:
        :param date_from: filter by start date. It is set as UNIX-time.
        :param date_to: filter by end date. It is set as UNIX-time.
        :param limit: number of returned posts. By default — 1000.
        """

        params = self.get_set_params(locals())
        response = await self.api.request("secure.getSMSHistory", params)
        model = secure.GetSMSHistoryResponse
        return model(**response).response

    async def get_transactions_history(
        self,
        type: Optional[int] = None,
        uid_from: Optional[int] = None,
        uid_to: Optional[int] = None,
        date_from: Optional[int] = None,
        date_to: Optional[int] = None,
        limit: Optional[int] = None,
        **kwargs
    ) -> secure.GetTransactionsHistoryResponseModel:
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
        model = secure.GetTransactionsHistoryResponse
        return model(**response).response

    async def get_user_level(
        self, user_ids: List[int], **kwargs
    ) -> secure.GetUserLevelResponseModel:
        """Returns one of the previously set game levels of one or more users in the application.
        :param user_ids:
        """

        params = self.get_set_params(locals())
        response = await self.api.request("secure.getUserLevel", params)
        model = secure.GetUserLevelResponse
        return model(**response).response

    async def give_event_sticker(
        self, user_ids: List[int], achievement_id: int, **kwargs
    ) -> secure.GiveEventStickerResponseModel:
        """Opens the game achievement and gives the user a sticker
        :param user_ids:
        :param achievement_id:
        """

        params = self.get_set_params(locals())
        response = await self.api.request("secure.giveEventSticker", params)
        model = secure.GiveEventStickerResponse
        return model(**response).response

    async def send_notification(
        self,
        message: str,
        user_ids: Optional[List[int]] = None,
        user_id: Optional[int] = None,
        **kwargs
    ) -> secure.SendNotificationResponseModel:
        """Sends notification to the user.
        :param message: notification text which should be sent in 'UTF-8' encoding ('254' characters maximum).
        :param user_ids:
        :param user_id:
        """

        params = self.get_set_params(locals())
        response = await self.api.request("secure.sendNotification", params)
        model = secure.SendNotificationResponse
        return model(**response).response

    async def send_s_m_s_notification(
        self, user_id: int, message: str, **kwargs
    ) -> base.OkResponseModel:
        """Sends 'SMS' notification to a user's mobile device.
        :param user_id: ID of the user to whom SMS notification is sent. The user shall allow the application to send him/her notifications (, +1).
        :param message: 'SMS' text to be sent in 'UTF-8' encoding. Only Latin letters and numbers are allowed. Maximum size is '160' characters.
        """

        params = self.get_set_params(locals())
        response = await self.api.request("secure.sendSMSNotification", params)
        model = base.OkResponse
        return model(**response).response

    async def set_counter(
        self,
        counters: Optional[List[str]] = None,
        user_id: Optional[int] = None,
        counter: Optional[int] = None,
        increment: Optional[bool] = None,
        **kwargs
    ) -> base.OkResponseModel:
        """Sets a counter which is shown to the user in bold in the left menu.
        :param counters:
        :param user_id:
        :param counter: counter value.
        :param increment:
        """

        params = self.get_set_params(locals())
        response = await self.api.request("secure.setCounter", params)
        model = base.OkResponse
        return model(**response).response
