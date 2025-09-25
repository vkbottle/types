import typing

from vkbottle_types.methods.base_category import BaseCategory
from vkbottle_types.objects import (
    AccountAccountCounters,
    AccountInfo,
    AccountPushSettings,
    AccountUserSettings,
    BaseUserGroupFields,
)
from vkbottle_types.responses.account import *  # noqa: F401,F403  # type: ignore
from vkbottle_types.responses.base import (
    BaseOkResponse,
    BaseOkResponseModel,
)


class AccountCategory(BaseCategory):
    async def ban(
        self,
        owner_id: typing.Optional[int] = None,
        **kwargs: typing.Any,
    ) -> BaseOkResponseModel:
        """Method `account.ban()`

        :param owner_id:
        """

        params = self.get_set_params(locals())
        response = await self.api.request("account.ban", params)
        model = BaseOkResponse
        return model(**response).response

    async def change_password(
        self,
        new_password: str,
        change_password_hash: typing.Optional[str] = None,
        old_password: typing.Optional[str] = None,
        restore_sid: typing.Optional[str] = None,
        **kwargs: typing.Any,
    ) -> AccountChangePasswordResponseModel:
        """Method `account.changePassword()`

        :param new_password: New password that will be set as a current
        :param change_password_hash: Hash received after a successful OAuth authorization with a code got by SMS. (If the password is changed right after the access was restored)
        :param old_password: Current user password.
        :param restore_sid: Session id received after the [vk.ru/dev/auth.restore|auth.restore] method is executed. (If the password is changed right after the access was restored)
        """

        params = self.get_set_params(locals())
        response = await self.api.request("account.changePassword", params)
        model = AccountChangePasswordResponse
        return model(**response).response

    async def get_active_offers(
        self,
        count: typing.Optional[int] = None,
        offset: typing.Optional[int] = None,
        **kwargs: typing.Any,
    ) -> AccountGetActiveOffersResponseModel:
        """Method `account.getActiveOffers()`

        :param count: Number of results to return.
        :param offset:
        """

        params = self.get_set_params(locals())
        response = await self.api.request("account.getActiveOffers", params)
        model = AccountGetActiveOffersResponse
        return model(**response).response

    async def get_app_permissions(
        self,
        user_id: typing.Optional[int] = None,
        **kwargs: typing.Any,
    ) -> int:
        """Method `account.getAppPermissions()`

        :param user_id: User ID whose settings information shall be got. By default: current user.
        """

        params = self.get_set_params(locals())
        response = await self.api.request("account.getAppPermissions", params)
        model = AccountGetAppPermissionsResponse
        return model(**response).response

    async def get_banned(
        self,
        count: typing.Optional[int] = None,
        fields: typing.Optional[typing.List[BaseUserGroupFields]] = None,
        offset: typing.Optional[int] = None,
        **kwargs: typing.Any,
    ) -> AccountGetBannedResponseModel:
        """Method `account.getBanned()`

        :param count: Number of results to return.
        :param fields: Additional fields of [vk.ru/dev/fields|profiles] and [vk.ru/dev/fields_groups|communities] to return.
        :param offset: Offset needed to return a specific subset of results.
        """

        params = self.get_set_params(locals())
        response = await self.api.request("account.getBanned", params)
        model = AccountGetBannedResponse
        return model(**response).response

    async def get_counters(
        self,
        filter: typing.Optional[typing.List[str]] = None,
        **kwargs: typing.Any,
    ) -> "AccountAccountCounters":
        """Method `account.getCounters()`

        :param filter: Counters to be returned.
        """

        params = self.get_set_params(locals())
        response = await self.api.request("account.getCounters", params)
        model = AccountGetCountersResponse
        return model(**response).response

    async def get_info(
        self,
        fields: typing.Optional[
            typing.List[typing.Literal["country", "https_required", "own_posts_default", "no_wall_replies", "intro", "lang", "audio_autoplay"]]
        ] = None,
        **kwargs: typing.Any,
    ) -> "AccountInfo":
        """Method `account.getInfo()`

        :param fields: Fields to return. Possible values: *'country' - user country,, *'https_required' - is "HTTPS only" option enabled,, *'own_posts_default' - is "Show my posts only" option is enabled,, *'no_wall_replies' - are wall replies disabled or not,, *'intro' - is intro passed by user or not,, *'lang' - user language. By default: all.
        """

        params = self.get_set_params(locals())
        response = await self.api.request("account.getInfo", params)
        model = AccountGetInfoResponse
        return model(**response).response

    async def get_profile_info(
        self,
        **kwargs: typing.Any,
    ) -> "AccountUserSettings":
        """Method `account.getProfileInfo()`"""

        params = self.get_set_params(locals())
        response = await self.api.request("account.getProfileInfo", params)
        model = AccountGetProfileInfoResponse
        return model(**response).response

    async def get_push_settings(
        self,
        device_id: typing.Optional[str] = None,
        **kwargs: typing.Any,
    ) -> "AccountPushSettings":
        """Method `account.getPushSettings()`

        :param device_id: Unique device ID.
        """

        params = self.get_set_params(locals())
        response = await self.api.request("account.getPushSettings", params)
        model = AccountGetPushSettingsResponse
        return model(**response).response

    async def register_device(
        self,
        device_id: str,
        token: str,
        device_model: typing.Optional[str] = None,
        device_year: typing.Optional[int] = None,
        pushes_granted: typing.Optional[bool] = None,
        sandbox: typing.Optional[bool] = None,
        settings: typing.Optional[str] = None,
        system_version: typing.Optional[str] = None,
        **kwargs: typing.Any,
    ) -> BaseOkResponseModel:
        """Method `account.registerDevice()`

        :param device_id: Unique device ID.
        :param token: Device token used to send notifications. (for mpns, the token shall be URL for sending of notifications)
        :param device_model: String name of device model.
        :param device_year: Device year.
        :param pushes_granted:
        :param sandbox:
        :param settings: Push settings in a [vk.ru/dev/push_settings|special format].
        :param system_version: String version of device operating system.
        """

        params = self.get_set_params(locals())
        response = await self.api.request("account.registerDevice", params)
        model = BaseOkResponse
        return model(**response).response

    async def save_profile_info(
        self,
        bdate: typing.Optional[str] = None,
        bdate_visibility: typing.Optional[int] = None,
        cancel_request_id: typing.Optional[int] = None,
        city_id: typing.Optional[int] = None,
        country_id: typing.Optional[int] = None,
        first_name: typing.Optional[str] = None,
        home_town: typing.Optional[str] = None,
        last_name: typing.Optional[str] = None,
        maiden_name: typing.Optional[str] = None,
        relation: typing.Optional[int] = None,
        relation_partner_id: typing.Optional[int] = None,
        screen_name: typing.Optional[str] = None,
        sex: typing.Optional[int] = None,
        status: typing.Optional[str] = None,
        **kwargs: typing.Any,
    ) -> AccountSaveProfileInfoResponseModel:
        """Method `account.saveProfileInfo()`

        :param bdate: User birth date, format: DD.MM.YYYY.
        :param bdate_visibility: Birth date visibility. Returned values: , * '1' - show birth date,, * '2' - show only month and day,, * '0' - hide birth date.
        :param cancel_request_id: ID of the name change request to be canceled. If this parameter is sent, all the others are ignored.
        :param city_id: User city.
        :param country_id: User country.
        :param first_name: User first name.
        :param home_town: User home town.
        :param last_name: User last name.
        :param maiden_name: User maiden name (female only)
        :param relation: User relationship status. Possible values: , * '1' - single,, * '2' - in a relationship,, * '3' - engaged,, * '4' - married,, * '5' - it's complicated,, * '6' - actively searching,, * '7' - in love,, * '0' - not specified.
        :param relation_partner_id: ID of the relationship partner.
        :param screen_name: User screen name.
        :param sex: User sex. Possible values: , * '1' - female,, * '2' - male.
        :param status: Status text.
        """

        params = self.get_set_params(locals())
        response = await self.api.request("account.saveProfileInfo", params)
        model = AccountSaveProfileInfoResponse
        return model(**response).response

    async def set_info(
        self,
        name: typing.Optional[str] = None,
        value: typing.Optional[str] = None,
        **kwargs: typing.Any,
    ) -> BaseOkResponseModel:
        """Method `account.setInfo()`

        :param name: Setting name.
        :param value: Setting value.
        """

        params = self.get_set_params(locals())
        response = await self.api.request("account.setInfo", params)
        model = BaseOkResponse
        return model(**response).response

    async def set_offline(
        self,
        **kwargs: typing.Any,
    ) -> BaseOkResponseModel:
        """Method `account.setOffline()`"""

        params = self.get_set_params(locals())
        response = await self.api.request("account.setOffline", params)
        model = BaseOkResponse
        return model(**response).response

    async def set_online(
        self,
        voip: typing.Optional[bool] = None,
        **kwargs: typing.Any,
    ) -> BaseOkResponseModel:
        """Method `account.setOnline()`

        :param voip: '1' if videocalls are available for current device.
        """

        params = self.get_set_params(locals())
        response = await self.api.request("account.setOnline", params)
        model = BaseOkResponse
        return model(**response).response

    async def set_push_settings(
        self,
        device_id: str,
        key: typing.Optional[str] = None,
        settings: typing.Optional[str] = None,
        value: typing.Optional[typing.List[str]] = None,
        **kwargs: typing.Any,
    ) -> BaseOkResponseModel:
        """Method `account.setPushSettings()`

        :param device_id: Unique device ID.
        :param key: Notification key.
        :param settings: Push settings in a [vk.ru/dev/push_settings|special format].
        :param value: New value for the key in a [vk.ru/dev/push_settings|special format].
        """

        params = self.get_set_params(locals())
        response = await self.api.request("account.setPushSettings", params)
        model = BaseOkResponse
        return model(**response).response

    async def set_silence_mode(
        self,
        device_id: typing.Optional[str] = None,
        peer_id: typing.Optional[int] = None,
        sound: typing.Optional[int] = None,
        time: typing.Optional[int] = None,
        **kwargs: typing.Any,
    ) -> BaseOkResponseModel:
        """Method `account.setSilenceMode()`

        :param device_id: Unique device ID.
        :param peer_id: Destination ID. "For user: 'User ID', e.g. '12345'. For chat: '2000000000' + 'Chat ID', e.g. '2000000001'. For community: '- Community ID', e.g. '-12345'. "
        :param sound: '1' - to enable sound in this dialog, '0' - to disable sound. Only if 'peer_id' contains user or community ID.
        :param time: Time in seconds for what notifications should be disabled. '-1' to disable forever.
        """

        params = self.get_set_params(locals())
        response = await self.api.request("account.setSilenceMode", params)
        model = BaseOkResponse
        return model(**response).response

    async def unban(
        self,
        owner_id: typing.Optional[int] = None,
        **kwargs: typing.Any,
    ) -> BaseOkResponseModel:
        """Method `account.unban()`

        :param owner_id:
        """

        params = self.get_set_params(locals())
        response = await self.api.request("account.unban", params)
        model = BaseOkResponse
        return model(**response).response

    async def unregister_device(
        self,
        device_id: typing.Optional[str] = None,
        sandbox: typing.Optional[bool] = None,
        **kwargs: typing.Any,
    ) -> BaseOkResponseModel:
        """Method `account.unregisterDevice()`

        :param device_id: Unique device ID.
        :param sandbox:
        """

        params = self.get_set_params(locals())
        response = await self.api.request("account.unregisterDevice", params)
        model = BaseOkResponse
        return model(**response).response


__all__ = ("AccountCategory",)
