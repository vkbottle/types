from typing import Optional, List

from vkbottle_types.responses import account, base
from .base_category import BaseCategory


class AccountCategory(BaseCategory):
    async def ban(
        self, owner_id: Optional[int] = None, **kwargs
    ) -> base.OkResponseModel:
        """account.ban method
        :param owner_id:
        """

        params = self.get_set_params(locals())
        return base.OkResponse(**await self.api.request("account.ban", params)).response

    async def change_password(
        self,
        new_password: str,
        restore_sid: Optional[str] = None,
        change_password_hash: Optional[str] = None,
        old_password: Optional[str] = None,
        **kwargs
    ) -> account.ChangePasswordResponseModel:
        """Changes a user password after access is successfully restored with the [vk.com/dev/auth.restore|auth.restore] method.
        :param new_password: New password that will be set as a current
        :param restore_sid: Session id received after the [vk.com/dev/auth.restore|auth.restore] method is executed. (If the password is changed right after the access was restored)
        :param change_password_hash: Hash received after a successful OAuth authorization with a code got by SMS. (If the password is changed right after the access was restored)
        :param old_password: Current user password.
        """

        params = self.get_set_params(locals())
        return account.ChangePasswordResponse(
            **await self.api.request("account.changePassword", params)
        ).response

    async def get_active_offers(
        self, offset: Optional[int] = None, count: Optional[int] = None, **kwargs
    ) -> account.GetActiveOffersResponseModel:
        """Returns a list of active ads (offers, **kwargs) which executed by the user will bring him/her respective number of votes to his balance in the application.
        :param offset:
        :param count: Number of results to return.
        """

        params = self.get_set_params(locals())
        return account.GetActiveOffersResponse(
            **await self.api.request("account.getActiveOffers", params)
        ).response

    async def get_app_permissions(
        self, user_id: int, **kwargs
    ) -> account.GetAppPermissionsResponseModel:
        """Gets settings of the user in this application.
        :param user_id: User ID whose settings information shall be got. By default: current user.
        """

        params = self.get_set_params(locals())
        return account.GetAppPermissionsResponse(
            **await self.api.request("account.getAppPermissions", params)
        ).response

    async def get_banned(
        self, offset: Optional[int] = None, count: Optional[int] = None, **kwargs
    ) -> account.GetBannedResponseModel:
        """Returns a user's blacklist.
        :param offset: Offset needed to return a specific subset of results.
        :param count: Number of results to return.
        """

        params = self.get_set_params(locals())
        return account.GetBannedResponse(
            **await self.api.request("account.getBanned", params)
        ).response

    async def get_counters(
        self, filter: Optional[List[str]] = None, **kwargs
    ) -> account.GetCountersResponseModel:
        """Returns non-null values of user counters.
        :param filter: Counters to be returned.
        """

        params = self.get_set_params(locals())
        return account.GetCountersResponse(
            **await self.api.request("account.getCounters", params)
        ).response

    async def get_info(
        self, fields: Optional[List[str]] = None, **kwargs
    ) -> account.GetInfoResponseModel:
        """Returns current account info.
        :param fields: Fields to return. Possible values: *'country' — user country,, *'https_required' — is "HTTPS only" option enabled,, *'own_posts_default' — is "Show my posts only" option is enabled,, *'no_wall_replies' — are wall replies disabled or not,, *'intro' — is intro passed by user or not,, *'lang' — user language. By default: all.
        """

        params = self.get_set_params(locals())
        return account.GetInfoResponse(
            **await self.api.request("account.getInfo", params)
        ).response

    async def get_profile_info(self, **kwargs) -> account.GetProfileInfoResponseModel:
        """Returns the current account info."""

        params = self.get_set_params(locals())
        return account.GetProfileInfoResponse(
            **await self.api.request("account.getProfileInfo", params)
        ).response

    async def get_push_settings(
        self, device_id: Optional[str] = None, **kwargs
    ) -> account.GetPushSettingsResponseModel:
        """Gets settings of push notifications.
        :param device_id: Unique device ID.
        """

        params = self.get_set_params(locals())
        return account.GetPushSettingsResponse(
            **await self.api.request("account.getPushSettings", params)
        ).response

    async def register_device(
        self,
        token: str,
        device_id: str,
        device_model: Optional[str] = None,
        device_year: Optional[int] = None,
        system_version: Optional[str] = None,
        settings: Optional[str] = None,
        sandbox: Optional[bool] = None,
        **kwargs
    ) -> base.OkResponseModel:
        """Subscribes an iOS/Android/Windows Phone-based device to receive push notifications
        :param token: Device token used to send notifications. (for mpns, the token shall be URL for sending of notifications)
        :param device_id: Unique device ID.
        :param device_model: String name of device model.
        :param device_year: Device year.
        :param system_version: String version of device operating system.
        :param settings: Push settings in a [vk.com/dev/push_settings|special format].
        :param sandbox:
        """

        params = self.get_set_params(locals())
        return base.OkResponse(
            **await self.api.request("account.registerDevice", params)
        ).response

    async def save_profile_info(
        self,
        first_name: Optional[str] = None,
        last_name: Optional[str] = None,
        maiden_name: Optional[str] = None,
        screen_name: Optional[str] = None,
        cancel_request_id: Optional[int] = None,
        sex: Optional[int] = None,
        relation: Optional[int] = None,
        relation_partner_id: Optional[int] = None,
        bdate: Optional[str] = None,
        bdate_visibility: Optional[int] = None,
        home_town: Optional[str] = None,
        country_id: Optional[int] = None,
        city_id: Optional[int] = None,
        status: Optional[str] = None,
        **kwargs
    ) -> account.SaveProfileInfoResponseModel:
        """Edits current profile info.
        :param first_name: User first name.
        :param last_name: User last name.
        :param maiden_name: User maiden name (female only)
        :param screen_name: User screen name.
        :param cancel_request_id: ID of the name change request to be canceled. If this parameter is sent, all the others are ignored.
        :param sex: User sex. Possible values: , * '1' – female,, * '2' – male.
        :param relation: User relationship status. Possible values: , * '1' – single,, * '2' – in a relationship,, * '3' – engaged,, * '4' – married,, * '5' – it's complicated,, * '6' – actively searching,, * '7' – in love,, * '0' – not specified.
        :param relation_partner_id: ID of the relationship partner.
        :param bdate: User birth date, format: DD.MM.YYYY.
        :param bdate_visibility: Birth date visibility. Returned values: , * '1' – show birth date,, * '2' – show only month and day,, * '0' – hide birth date.
        :param home_town: User home town.
        :param country_id: User country.
        :param city_id: User city.
        :param status: Status text.
        """

        params = self.get_set_params(locals())
        return account.SaveProfileInfoResponse(
            **await self.api.request("account.saveProfileInfo", params)
        ).response

    async def set_info(
        self, name: Optional[str] = None, value: Optional[str] = None, **kwargs
    ) -> base.OkResponseModel:
        """Allows to edit the current account info.
        :param name: Setting name.
        :param value: Setting value.
        """

        params = self.get_set_params(locals())
        return base.OkResponse(
            **await self.api.request("account.setInfo", params)
        ).response

    async def set_name_in_menu(
        self, user_id: int, name: Optional[str] = None, **kwargs
    ) -> base.OkResponseModel:
        """Sets an application screen name (up to 17 characters), that is shown to the user in the left menu.
        :param user_id: User ID.
        :param name: Application screen name.
        """

        params = self.get_set_params(locals())
        return base.OkResponse(
            **await self.api.request("account.setNameInMenu", params)
        ).response

    async def set_offline(self, **kwargs) -> base.OkResponseModel:
        """Marks a current user as offline."""

        params = self.get_set_params(locals())
        return base.OkResponse(
            **await self.api.request("account.setOffline", params)
        ).response

    async def set_online(
        self, voip: Optional[bool] = None, **kwargs
    ) -> base.OkResponseModel:
        """Marks the current user as online for 15 minutes.
        :param voip: '1' if videocalls are available for current device.
        """

        params = self.get_set_params(locals())
        return base.OkResponse(
            **await self.api.request("account.setOnline", params)
        ).response

    async def set_push_settings(
        self,
        device_id: str,
        settings: Optional[str] = None,
        key: Optional[str] = None,
        value: Optional[List[str]] = None,
        **kwargs
    ) -> base.OkResponseModel:
        """Change push settings.
        :param device_id: Unique device ID.
        :param settings: Push settings in a [vk.com/dev/push_settings|special format].
        :param key: Notification key.
        :param value: New value for the key in a [vk.com/dev/push_settings|special format].
        """

        params = self.get_set_params(locals())
        return base.OkResponse(
            **await self.api.request("account.setPushSettings", params)
        ).response

    async def set_silence_mode(
        self,
        device_id: Optional[str] = None,
        time: Optional[int] = None,
        peer_id: Optional[int] = None,
        sound: Optional[int] = None,
        **kwargs
    ) -> base.OkResponseModel:
        """Mutes push notifications for the set period of time.
        :param device_id: Unique device ID.
        :param time: Time in seconds for what notifications should be disabled. '-1' to disable forever.
        :param peer_id: Destination ID. "For user: 'User ID', e.g. '12345'. For chat: '2000000000' + 'Chat ID', e.g. '2000000001'. For community: '- Community ID', e.g. '-12345'. "
        :param sound: '1' — to enable sound in this dialog, '0' — to disable sound. Only if 'peer_id' contains user or community ID.
        """

        params = self.get_set_params(locals())
        return base.OkResponse(
            **await self.api.request("account.setSilenceMode", params)
        ).response

    async def unban(
        self, owner_id: Optional[int] = None, **kwargs
    ) -> base.OkResponseModel:
        """account.unban method
        :param owner_id:
        """

        params = self.get_set_params(locals())
        return base.OkResponse(
            **await self.api.request("account.unban", params)
        ).response

    async def unregister_device(
        self, device_id: Optional[str] = None, sandbox: Optional[bool] = None, **kwargs
    ) -> base.OkResponseModel:
        """Unsubscribes a device from push notifications.
        :param device_id: Unique device ID.
        :param sandbox:
        """

        params = self.get_set_params(locals())
        return base.OkResponse(
            **await self.api.request("account.unregisterDevice", params)
        ).response
