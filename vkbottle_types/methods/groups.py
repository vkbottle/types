import typing
from typing import Optional, List

from vkbottle_types.responses import base, groups
from .base_category import BaseCategory

if typing.TYPE_CHECKING:
    from vkbottle_types.objects import (
        base as objects_base,
        addresses as objects_addresses,
        users as objects_users,
        groups as objects_groups,
    )


class GroupsCategory(BaseCategory):
    async def add_address(
        self,
        group_id: int,
        title: str,
        address: str,
        country_id: int,
        city_id: int,
        latitude: float,
        longitude: float,
        additional_address: Optional[str] = None,
        metro_id: Optional[int] = None,
        phone: Optional[str] = None,
        work_info_status: Optional[str] = None,
        timetable: Optional[str] = None,
        is_main_address: Optional[bool] = None,
        **kwargs
    ) -> groups.AddAddressResponseModel:
        """groups.addAddress method
        :param group_id:
        :param title:
        :param address:
        :param country_id:
        :param city_id:
        :param latitude:
        :param longitude:
        :param additional_address:
        :param metro_id:
        :param phone:
        :param work_info_status:
        :param timetable:
        :param is_main_address:
        """

        params = self.get_set_params(locals())
        return groups.AddAddressResponse(
            **await self.api.request("groups.addAddress", params)
        ).response

    async def add_callback_server(
        self,
        group_id: int,
        url: str,
        title: str,
        secret_key: Optional[str] = None,
        **kwargs
    ) -> groups.AddCallbackServerResponseModel:
        """groups.addCallbackServer method
        :param group_id:
        :param url:
        :param title:
        :param secret_key:
        """

        params = self.get_set_params(locals())
        return groups.AddCallbackServerResponse(
            **await self.api.request("groups.addCallbackServer", params)
        ).response

    async def add_link(
        self, group_id: int, link: str, text: Optional[str] = None, **kwargs
    ) -> groups.AddLinkResponseModel:
        """Allows to add a link to the community.
        :param group_id: Community ID.
        :param link: Link URL.
        :param text: Description text for the link.
        """

        params = self.get_set_params(locals())
        return groups.AddLinkResponse(
            **await self.api.request("groups.addLink", params)
        ).response

    async def approve_request(
        self, group_id: int, user_id: int, **kwargs
    ) -> base.OkResponseModel:
        """Allows to approve join request to the community.
        :param group_id: Community ID.
        :param user_id: User ID.
        """

        params = self.get_set_params(locals())
        return base.OkResponse(
            **await self.api.request("groups.approveRequest", params)
        ).response

    async def ban(
        self,
        group_id: int,
        owner_id: Optional[int] = None,
        end_date: Optional[int] = None,
        reason: Optional[int] = None,
        comment: Optional[str] = None,
        comment_visible: Optional[bool] = None,
        **kwargs
    ) -> base.OkResponseModel:
        """groups.ban method
        :param group_id:
        :param owner_id:
        :param end_date:
        :param reason:
        :param comment:
        :param comment_visible:
        """

        params = self.get_set_params(locals())
        return base.OkResponse(**await self.api.request("groups.ban", params)).response

    async def create(
        self,
        title: str,
        description: Optional[str] = None,
        type: Optional[str] = None,
        public_category: Optional[int] = None,
        subtype: Optional[int] = None,
        **kwargs
    ) -> groups.CreateResponseModel:
        """Creates a new community.
        :param title: Community title.
        :param description: Community description (ignored for 'type' = 'public').
        :param type: Community type. Possible values: *'group' – group,, *'event' – event,, *'public' – public page
        :param public_category: Category ID (for 'type' = 'public' only).
        :param subtype: Public page subtype. Possible values: *'1' – place or small business,, *'2' – company, organization or website,, *'3' – famous person or group of people,, *'4' – product or work of art.
        """

        params = self.get_set_params(locals())
        return groups.CreateResponse(
            **await self.api.request("groups.create", params)
        ).response

    async def delete_callback_server(
        self, group_id: int, server_id: int, **kwargs
    ) -> base.OkResponseModel:
        """groups.deleteCallbackServer method
        :param group_id:
        :param server_id:
        """

        params = self.get_set_params(locals())
        return base.OkResponse(
            **await self.api.request("groups.deleteCallbackServer", params)
        ).response

    async def delete_link(
        self, group_id: int, link_id: int, **kwargs
    ) -> base.OkResponseModel:
        """Allows to delete a link from the community.
        :param group_id: Community ID.
        :param link_id: Link ID.
        """

        params = self.get_set_params(locals())
        return base.OkResponse(
            **await self.api.request("groups.deleteLink", params)
        ).response

    async def disable_online(self, group_id: int, **kwargs) -> base.OkResponseModel:
        """groups.disableOnline method
        :param group_id:
        """

        params = self.get_set_params(locals())
        return base.OkResponse(
            **await self.api.request("groups.disableOnline", params)
        ).response

    async def edit(
        self,
        group_id: int,
        title: Optional[str] = None,
        description: Optional[str] = None,
        screen_name: Optional[str] = None,
        access: Optional[int] = None,
        website: Optional[str] = None,
        subject: Optional[str] = None,
        email: Optional[str] = None,
        phone: Optional[str] = None,
        rss: Optional[str] = None,
        event_start_date: Optional[int] = None,
        event_finish_date: Optional[int] = None,
        event_group_id: Optional[int] = None,
        public_category: Optional[int] = None,
        public_subcategory: Optional[int] = None,
        public_date: Optional[str] = None,
        wall: Optional[int] = None,
        topics: Optional[int] = None,
        photos: Optional[int] = None,
        video: Optional[int] = None,
        audio: Optional[int] = None,
        links: Optional[bool] = None,
        events: Optional[bool] = None,
        places: Optional[bool] = None,
        contacts: Optional[bool] = None,
        docs: Optional[int] = None,
        wiki: Optional[int] = None,
        messages: Optional[bool] = None,
        articles: Optional[bool] = None,
        addresses: Optional[bool] = None,
        age_limits: Optional[int] = None,
        market: Optional[bool] = None,
        market_comments: Optional[bool] = None,
        market_country: Optional[List[int]] = None,
        market_city: Optional[List[int]] = None,
        market_currency: Optional[int] = None,
        market_contact: Optional[int] = None,
        market_wiki: Optional[int] = None,
        obscene_filter: Optional[bool] = None,
        obscene_stopwords: Optional[bool] = None,
        obscene_words: Optional[List[str]] = None,
        main_section: Optional[int] = None,
        secondary_section: Optional[int] = None,
        country: Optional[int] = None,
        city: Optional[int] = None,
        **kwargs
    ) -> base.OkResponseModel:
        """Edits a community.
        :param group_id: Community ID.
        :param title: Community title.
        :param description: Community description.
        :param screen_name: Community screen name.
        :param access: Community type. Possible values: *'0' – open,, *'1' – closed,, *'2' – private.
        :param website: Website that will be displayed in the community information field.
        :param subject: Community subject. Possible values: , *'1' – auto/moto,, *'2' – activity holidays,, *'3' – business,, *'4' – pets,, *'5' – health,, *'6' – dating and communication, , *'7' – games,, *'8' – IT (computers and software),, *'9' – cinema,, *'10' – beauty and fashion,, *'11' – cooking,, *'12' – art and culture,, *'13' – literature,, *'14' – mobile services and internet,, *'15' – music,, *'16' – science and technology,, *'17' – real estate,, *'18' – news and media,, *'19' – security,, *'20' – education,, *'21' – home and renovations,, *'22' – politics,, *'23' – food,, *'24' – industry,, *'25' – travel,, *'26' – work,, *'27' – entertainment,, *'28' – religion,, *'29' – family,, *'30' – sports,, *'31' – insurance,, *'32' – television,, *'33' – goods and services,, *'34' – hobbies,, *'35' – finance,, *'36' – photo,, *'37' – esoterics,, *'38' – electronics and appliances,, *'39' – erotic,, *'40' – humor,, *'41' – society, humanities,, *'42' – design and graphics.
        :param email: Organizer email (for events).
        :param phone: Organizer phone number (for events).
        :param rss: RSS feed address for import (available only to communities with special permission. Contact vk.com/support to get it.
        :param event_start_date: Event start date in Unixtime format.
        :param event_finish_date: Event finish date in Unixtime format.
        :param event_group_id: Organizer community ID (for events only).
        :param public_category: Public page category ID.
        :param public_subcategory: Public page subcategory ID.
        :param public_date: Founding date of a company or organization owning the community in "dd.mm.YYYY" format.
        :param wall: Wall settings. Possible values: *'0' – disabled,, *'1' – open,, *'2' – limited (groups and events only),, *'3' – closed (groups and events only).
        :param topics: Board topics settings. Possbile values: , *'0' – disabled,, *'1' – open,, *'2' – limited (for groups and events only).
        :param photos: Photos settings. Possible values: *'0' – disabled,, *'1' – open,, *'2' – limited (for groups and events only).
        :param video: Video settings. Possible values: *'0' – disabled,, *'1' – open,, *'2' – limited (for groups and events only).
        :param audio: Audio settings. Possible values: *'0' – disabled,, *'1' – open,, *'2' – limited (for groups and events only).
        :param links: Links settings (for public pages only). Possible values: *'0' – disabled,, *'1' – enabled.
        :param events: Events settings (for public pages only). Possible values: *'0' – disabled,, *'1' – enabled.
        :param places: Places settings (for public pages only). Possible values: *'0' – disabled,, *'1' – enabled.
        :param contacts: Contacts settings (for public pages only). Possible values: *'0' – disabled,, *'1' – enabled.
        :param docs: Documents settings. Possible values: *'0' – disabled,, *'1' – open,, *'2' – limited (for groups and events only).
        :param wiki: Wiki pages settings. Possible values: *'0' – disabled,, *'1' – open,, *'2' – limited (for groups and events only).
        :param messages: Community messages. Possible values: *'0' — disabled,, *'1' — enabled.
        :param articles:
        :param addresses:
        :param age_limits: Community age limits. Possible values: *'1' — no limits,, *'2' — 16+,, *'3' — 18+.
        :param market: Market settings. Possible values: *'0' – disabled,, *'1' – enabled.
        :param market_comments: market comments settings. Possible values: *'0' – disabled,, *'1' – enabled.
        :param market_country: Market delivery countries.
        :param market_city: Market delivery cities (if only one country is specified).
        :param market_currency: Market currency settings. Possbile values: , *'643' – Russian rubles,, *'980' – Ukrainian hryvnia,, *'398' – Kazakh tenge,, *'978' – Euro,, *'840' – US dollars
        :param market_contact: Seller contact for market. Set '0' for community messages.
        :param market_wiki: ID of a wiki page with market description.
        :param obscene_filter: Obscene expressions filter in comments. Possible values: , *'0' – disabled,, *'1' – enabled.
        :param obscene_stopwords: Stopwords filter in comments. Possible values: , *'0' – disabled,, *'1' – enabled.
        :param obscene_words: Keywords for stopwords filter.
        :param main_section:
        :param secondary_section:
        :param country: Country of the community.
        :param city: City of the community.
        """

        params = self.get_set_params(locals())
        return base.OkResponse(**await self.api.request("groups.edit", params)).response

    async def edit_address(
        self,
        group_id: int,
        address_id: int,
        title: Optional[str] = None,
        address: Optional[str] = None,
        additional_address: Optional[str] = None,
        country_id: Optional[int] = None,
        city_id: Optional[int] = None,
        metro_id: Optional[int] = None,
        latitude: Optional[float] = None,
        longitude: Optional[float] = None,
        phone: Optional[str] = None,
        work_info_status: Optional[str] = None,
        timetable: Optional[str] = None,
        is_main_address: Optional[bool] = None,
        **kwargs
    ) -> groups.EditAddressResponseModel:
        """groups.editAddress method
        :param group_id:
        :param address_id:
        :param title:
        :param address:
        :param additional_address:
        :param country_id:
        :param city_id:
        :param metro_id:
        :param latitude:
        :param longitude:
        :param phone:
        :param work_info_status:
        :param timetable:
        :param is_main_address:
        """

        params = self.get_set_params(locals())
        return groups.EditAddressResponse(
            **await self.api.request("groups.editAddress", params)
        ).response

    async def edit_callback_server(
        self,
        group_id: int,
        server_id: int,
        url: str,
        title: str,
        secret_key: Optional[str] = None,
        **kwargs
    ) -> base.OkResponseModel:
        """groups.editCallbackServer method
        :param group_id:
        :param server_id:
        :param url:
        :param title:
        :param secret_key:
        """

        params = self.get_set_params(locals())
        return base.OkResponse(
            **await self.api.request("groups.editCallbackServer", params)
        ).response

    async def edit_link(
        self, group_id: int, link_id: int, text: Optional[str] = None, **kwargs
    ) -> base.OkResponseModel:
        """Allows to edit a link in the community.
        :param group_id: Community ID.
        :param link_id: Link ID.
        :param text: New description text for the link.
        """

        params = self.get_set_params(locals())
        return base.OkResponse(
            **await self.api.request("groups.editLink", params)
        ).response

    async def edit_manager(
        self,
        group_id: int,
        user_id: int,
        role: Optional[str] = None,
        is_contact: Optional[bool] = None,
        contact_position: Optional[str] = None,
        contact_phone: Optional[str] = None,
        contact_email: Optional[str] = None,
        **kwargs
    ) -> base.OkResponseModel:
        """Allows to add, remove or edit the community manager.
        :param group_id: Community ID.
        :param user_id: User ID.
        :param role: Manager role. Possible values: *'moderator',, *'editor',, *'administrator',, *'advertiser'.
        :param is_contact: '1' — to show the manager in Contacts block of the community.
        :param contact_position: Position to show in Contacts block.
        :param contact_phone: Contact phone.
        :param contact_email: Contact e-mail.
        """

        params = self.get_set_params(locals())
        return base.OkResponse(
            **await self.api.request("groups.editManager", params)
        ).response

    async def enable_online(self, group_id: int, **kwargs) -> base.OkResponseModel:
        """groups.enableOnline method
        :param group_id:
        """

        params = self.get_set_params(locals())
        return base.OkResponse(
            **await self.api.request("groups.enableOnline", params)
        ).response

    async def get(
        self,
        user_id: Optional[int] = None,
        extended: Optional[bool] = None,
        filter: Optional[List["objects_groups.Filter"]] = None,
        fields: Optional[List["objects_groups.Fields"]] = None,
        offset: Optional[int] = None,
        count: Optional[int] = None,
        **kwargs
    ) -> groups.GetExtendedResponseModel:
        """Returns a list of the communities to which a user belongs.
        :param user_id: User ID.
        :param extended: '1' — to return complete information about a user's communities, '0' — to return a list of community IDs without any additional fields (default),
        :param filter: Types of communities to return: 'admin' — to return communities administered by the user , 'editor' — to return communities where the user is an administrator or editor, 'moder' — to return communities where the user is an administrator, editor, or moderator, 'groups' — to return only groups, 'publics' — to return only public pages, 'events' — to return only events
        :param fields: Profile fields to return.
        :param offset: Offset needed to return a specific subset of communities.
        :param count: Number of communities to return.
        """

        params = self.get_set_params(locals())
        return groups.GetExtendedResponse(
            **await self.api.request("groups.get", params)
        ).response

    async def get_addresses(
        self,
        group_id: int,
        address_ids: Optional[List[int]] = None,
        latitude: Optional[float] = None,
        longitude: Optional[float] = None,
        offset: Optional[int] = None,
        count: Optional[int] = None,
        fields: Optional[List["objects_addresses.Fields"]] = None,
        **kwargs
    ) -> groups.GetAddressesResponseModel:
        """Returns a list of community addresses.
        :param group_id: ID or screen name of the community.
        :param address_ids:
        :param latitude: Latitude of  the user geo position.
        :param longitude: Longitude of the user geo position.
        :param offset: Offset needed to return a specific subset of community addresses.
        :param count: Number of community addresses to return.
        :param fields: Address fields
        """

        params = self.get_set_params(locals())
        return groups.GetAddressesResponse(
            **await self.api.request("groups.getAddresses", params)
        ).response

    async def get_banned(
        self,
        group_id: int,
        offset: Optional[int] = None,
        count: Optional[int] = None,
        fields: Optional[List["objects_base.UserGroupFields"]] = None,
        owner_id: Optional[int] = None,
        **kwargs
    ) -> groups.GetBannedResponseModel:
        """Returns a list of users on a community blacklist.
        :param group_id: Community ID.
        :param offset: Offset needed to return a specific subset of users.
        :param count: Number of users to return.
        :param fields:
        :param owner_id:
        """

        params = self.get_set_params(locals())
        return groups.GetBannedResponse(
            **await self.api.request("groups.getBanned", params)
        ).response

    async def get_by_id(
        self,
        group_ids: Optional[List[int]] = None,
        group_id: Optional[str] = None,
        fields: Optional[List["objects_groups.Fields"]] = None,
        **kwargs
    ) -> groups.GetByIdResponseModel:
        """Returns information about communities by their IDs.
        :param group_ids: IDs or screen names of communities.
        :param group_id: ID or screen name of the community.
        :param fields: Group fields to return.
        """

        params = self.get_set_params(locals())
        return groups.GetByIdResponse(
            **await self.api.request("groups.getById", params)
        ).response

    async def get_callback_confirmation_code(
        self, group_id: int, **kwargs
    ) -> groups.GetCallbackConfirmationCodeResponseModel:
        """Returns Callback API confirmation code for the community.
        :param group_id: Community ID.
        """

        params = self.get_set_params(locals())
        return groups.GetCallbackConfirmationCodeResponse(
            **await self.api.request("groups.getCallbackConfirmationCode", params)
        ).response

    async def get_callback_servers(
        self, group_id: int, server_ids: Optional[List[int]] = None, **kwargs
    ) -> groups.GetCallbackServersResponseModel:
        """groups.getCallbackServers method
        :param group_id:
        :param server_ids:
        """

        params = self.get_set_params(locals())
        return groups.GetCallbackServersResponse(
            **await self.api.request("groups.getCallbackServers", params)
        ).response

    async def get_callback_settings(
        self, group_id: int, server_id: Optional[int] = None, **kwargs
    ) -> groups.GetCallbackSettingsResponseModel:
        """Returns [vk.com/dev/callback_api|Callback API] notifications settings.
        :param group_id: Community ID.
        :param server_id: Server ID.
        """

        params = self.get_set_params(locals())
        return groups.GetCallbackSettingsResponse(
            **await self.api.request("groups.getCallbackSettings", params)
        ).response

    async def get_catalog(
        self,
        category_id: Optional[int] = None,
        subcategory_id: Optional[int] = None,
        **kwargs
    ) -> groups.GetCatalogResponseModel:
        """Returns communities list for a catalog category.
        :param category_id: Category id received from [vk.com/dev/groups.getCatalogInfo|groups.getCatalogInfo].
        :param subcategory_id: Subcategory id received from [vk.com/dev/groups.getCatalogInfo|groups.getCatalogInfo].
        """

        params = self.get_set_params(locals())
        return groups.GetCatalogResponse(
            **await self.api.request("groups.getCatalog", params)
        ).response

    async def get_catalog_info(
        self,
        extended: Optional[bool] = None,
        subcategories: Optional[bool] = None,
        **kwargs
    ) -> groups.GetCatalogInfoExtendedResponseModel:
        """Returns categories list for communities catalog
        :param extended: 1 – to return communities count and three communities for preview. By default: 0.
        :param subcategories: 1 – to return subcategories info. By default: 0.
        """

        params = self.get_set_params(locals())
        return groups.GetCatalogInfoExtendedResponse(
            **await self.api.request("groups.getCatalogInfo", params)
        ).response

    async def get_invited_users(
        self,
        group_id: int,
        offset: Optional[int] = None,
        count: Optional[int] = None,
        fields: Optional[List["objects_users.Fields"]] = None,
        name_case: Optional[str] = None,
        **kwargs
    ) -> groups.GetInvitedUsersResponseModel:
        """Returns invited users list of a community
        :param group_id: Group ID to return invited users for.
        :param offset: Offset needed to return a specific subset of results.
        :param count: Number of results to return.
        :param fields: List of additional fields to be returned. Available values: 'sex, bdate, city, country, photo_50, photo_100, photo_200_orig, photo_200, photo_400_orig, photo_max, photo_max_orig, online, online_mobile, lists, domain, has_mobile, contacts, connections, site, education, universities, schools, can_post, can_see_all_posts, can_see_audio, can_write_private_message, status, last_seen, common_count, relation, relatives, counters'.
        :param name_case: Case for declension of user name and surname. Possible values: *'nom' — nominative (default),, *'gen' — genitive,, *'dat' — dative,, *'acc' — accusative, , *'ins' — instrumental,, *'abl' — prepositional.
        """

        params = self.get_set_params(locals())
        return groups.GetInvitedUsersResponse(
            **await self.api.request("groups.getInvitedUsers", params)
        ).response

    async def get_invites(
        self,
        offset: Optional[int] = None,
        count: Optional[int] = None,
        extended: Optional[bool] = None,
        **kwargs
    ) -> groups.GetInvitesExtendedResponseModel:
        """Returns a list of invitations to join communities and events.
        :param offset: Offset needed to return a specific subset of invitations.
        :param count: Number of invitations to return.
        :param extended: '1' — to return additional [vk.com/dev/fields_groups|fields] for communities..
        """

        params = self.get_set_params(locals())
        return groups.GetInvitesExtendedResponse(
            **await self.api.request("groups.getInvites", params)
        ).response

    async def get_long_poll_server(
        self, group_id: int, **kwargs
    ) -> groups.GetLongPollServerResponseModel:
        """Returns the data needed to query a Long Poll server for events
        :param group_id: Community ID
        """

        params = self.get_set_params(locals())
        return groups.GetLongPollServerResponse(
            **await self.api.request("groups.getLongPollServer", params)
        ).response

    async def get_long_poll_settings(
        self, group_id: int, **kwargs
    ) -> groups.GetLongPollSettingsResponseModel:
        """Returns Long Poll notification settings
        :param group_id: Community ID.
        """

        params = self.get_set_params(locals())
        return groups.GetLongPollSettingsResponse(
            **await self.api.request("groups.getLongPollSettings", params)
        ).response

    async def get_members(
        self,
        group_id: Optional[str] = None,
        sort: Optional[str] = None,
        offset: Optional[int] = None,
        count: Optional[int] = None,
        fields: Optional[List["objects_users.Fields"]] = None,
        filter: Optional[str] = None,
        **kwargs
    ) -> groups.GetMembersResponseModel:
        """Returns a list of community members.
        :param group_id: ID or screen name of the community.
        :param sort: Sort order. Available values: 'id_asc', 'id_desc', 'time_asc', 'time_desc'. 'time_asc' and 'time_desc' are availavle only if the method is called by the group's 'moderator'.
        :param offset: Offset needed to return a specific subset of community members.
        :param count: Number of community members to return.
        :param fields: List of additional fields to be returned. Available values: 'sex, bdate, city, country, photo_50, photo_100, photo_200_orig, photo_200, photo_400_orig, photo_max, photo_max_orig, online, online_mobile, lists, domain, has_mobile, contacts, connections, site, education, universities, schools, can_post, can_see_all_posts, can_see_audio, can_write_private_message, status, last_seen, common_count, relation, relatives, counters'.
        :param filter: *'friends' – only friends in this community will be returned,, *'unsure' – only those who pressed 'I may attend' will be returned (if it's an event).
        """

        params = self.get_set_params(locals())
        return groups.GetMembersResponse(
            **await self.api.request("groups.getMembers", params)
        ).response

    async def get_requests(
        self,
        group_id: int,
        offset: Optional[int] = None,
        count: Optional[int] = None,
        fields: Optional[List["str"]] = None,
        **kwargs
    ) -> groups.GetRequestsResponseModel:
        """Returns a list of requests to the community.
        :param group_id: Community ID.
        :param offset: Offset needed to return a specific subset of results.
        :param count: Number of results to return.
        :param fields: Profile fields to return.
        """

        params = self.get_set_params(locals())
        return groups.GetRequestsResponse(
            **await self.api.request("groups.getRequests", params)
        ).response

    async def get_settings(
        self, group_id: int, **kwargs
    ) -> groups.GetSettingsResponseModel:
        """Returns community settings.
        :param group_id: Community ID.
        """

        params = self.get_set_params(locals())
        return groups.GetSettingsResponse(
            **await self.api.request("groups.getSettings", params)
        ).response

    async def get_token_permissions(
        self, **kwargs
    ) -> groups.GetTokenPermissionsResponseModel:
        """groups.getTokenPermissions method"""

        params = self.get_set_params(locals())
        return groups.GetTokenPermissionsResponse(
            **await self.api.request("groups.getTokenPermissions", params)
        ).response

    async def invite(
        self, group_id: int, user_id: int, **kwargs
    ) -> base.OkResponseModel:
        """Allows to invite friends to the community.
        :param group_id: Community ID.
        :param user_id: User ID.
        """

        params = self.get_set_params(locals())
        return base.OkResponse(
            **await self.api.request("groups.invite", params)
        ).response

    async def is_member(
        self,
        group_id: str,
        user_id: Optional[int] = None,
        user_ids: Optional[List[int]] = None,
        extended: Optional[bool] = None,
        **kwargs
    ) -> groups.IsMemberExtendedResponseModel:
        """Returns information specifying whether a user is a member of a community.
        :param group_id: ID or screen name of the community.
        :param user_id: User ID.
        :param user_ids: User IDs.
        :param extended: '1' — to return an extended response with additional fields. By default: '0'.
        """

        params = self.get_set_params(locals())
        return groups.IsMemberExtendedResponse(
            **await self.api.request("groups.isMember", params)
        ).response

    async def join(
        self, group_id: Optional[int] = None, not_sure: Optional[str] = None, **kwargs
    ) -> base.OkResponseModel:
        """With this method you can join the group or public page, and also confirm your participation in an event.
        :param group_id: ID or screen name of the community.
        :param not_sure: Optional parameter which is taken into account when 'gid' belongs to the event: '1' — Perhaps I will attend, '0' — I will be there for sure (default), ,
        """

        params = self.get_set_params(locals())
        return base.OkResponse(**await self.api.request("groups.join", params)).response

    async def leave(self, group_id: int, **kwargs) -> base.OkResponseModel:
        """With this method you can leave a group, public page, or event.
        :param group_id: ID or screen name of the community.
        """

        params = self.get_set_params(locals())
        return base.OkResponse(
            **await self.api.request("groups.leave", params)
        ).response

    async def remove_user(
        self, group_id: int, user_id: int, **kwargs
    ) -> base.OkResponseModel:
        """Removes a user from the community.
        :param group_id: Community ID.
        :param user_id: User ID.
        """

        params = self.get_set_params(locals())
        return base.OkResponse(
            **await self.api.request("groups.removeUser", params)
        ).response

    async def reorder_link(
        self, group_id: int, link_id: int, after: Optional[int] = None, **kwargs
    ) -> base.OkResponseModel:
        """Allows to reorder links in the community.
        :param group_id: Community ID.
        :param link_id: Link ID.
        :param after: ID of the link after which to place the link with 'link_id'.
        """

        params = self.get_set_params(locals())
        return base.OkResponse(
            **await self.api.request("groups.reorderLink", params)
        ).response

    async def search(
        self,
        q: str,
        type: Optional[str] = None,
        country_id: Optional[int] = None,
        city_id: Optional[int] = None,
        future: Optional[bool] = None,
        market: Optional[bool] = None,
        sort: Optional[int] = None,
        offset: Optional[int] = None,
        count: Optional[int] = None,
        **kwargs
    ) -> groups.SearchResponseModel:
        """Returns a list of communities matching the search criteria.
        :param q: Search query string.
        :param type: Community type. Possible values: 'group, page, event.'
        :param country_id: Country ID.
        :param city_id: City ID. If this parameter is transmitted, country_id is ignored.
        :param future: '1' — to return only upcoming events. Works with the 'type' = 'event' only.
        :param market: '1' — to return communities with enabled market only.
        :param sort: Sort order. Possible values: *'0' — default sorting (similar the full version of the site),, *'1' — by growth speed,, *'2'— by the "day attendance/members number" ratio,, *'3' — by the "Likes number/members number" ratio,, *'4' — by the "comments number/members number" ratio,, *'5' — by the "boards entries number/members number" ratio.
        :param offset: Offset needed to return a specific subset of results.
        :param count: Number of communities to return. "Note that you can not receive more than first thousand of results, regardless of 'count' and 'offset' values."
        """

        params = self.get_set_params(locals())
        return groups.SearchResponse(
            **await self.api.request("groups.search", params)
        ).response

    async def set_callback_settings(
        self,
        group_id: int,
        server_id: Optional[int] = None,
        api_version: Optional[str] = None,
        message_new: Optional[bool] = None,
        message_reply: Optional[bool] = None,
        message_allow: Optional[bool] = None,
        message_edit: Optional[bool] = None,
        message_deny: Optional[bool] = None,
        message_typing_state: Optional[bool] = None,
        photo_new: Optional[bool] = None,
        audio_new: Optional[bool] = None,
        video_new: Optional[bool] = None,
        wall_reply_new: Optional[bool] = None,
        wall_reply_edit: Optional[bool] = None,
        wall_reply_delete: Optional[bool] = None,
        wall_reply_restore: Optional[bool] = None,
        wall_post_new: Optional[bool] = None,
        wall_repost: Optional[bool] = None,
        board_post_new: Optional[bool] = None,
        board_post_edit: Optional[bool] = None,
        board_post_restore: Optional[bool] = None,
        board_post_delete: Optional[bool] = None,
        photo_comment_new: Optional[bool] = None,
        photo_comment_edit: Optional[bool] = None,
        photo_comment_delete: Optional[bool] = None,
        photo_comment_restore: Optional[bool] = None,
        video_comment_new: Optional[bool] = None,
        video_comment_edit: Optional[bool] = None,
        video_comment_delete: Optional[bool] = None,
        video_comment_restore: Optional[bool] = None,
        market_comment_new: Optional[bool] = None,
        market_comment_edit: Optional[bool] = None,
        market_comment_delete: Optional[bool] = None,
        market_comment_restore: Optional[bool] = None,
        poll_vote_new: Optional[bool] = None,
        group_join: Optional[bool] = None,
        group_leave: Optional[bool] = None,
        group_change_settings: Optional[bool] = None,
        group_change_photo: Optional[bool] = None,
        group_officers_edit: Optional[bool] = None,
        user_block: Optional[bool] = None,
        user_unblock: Optional[bool] = None,
        lead_forms_new: Optional[bool] = None,
        like_add: Optional[bool] = None,
        like_remove: Optional[bool] = None,
        message_event: Optional[bool] = None,
        **kwargs
    ) -> base.OkResponseModel:
        """Allow to set notifications settings for group.
        :param group_id: Community ID.
        :param server_id: Server ID.
        :param api_version:
        :param message_new: A new incoming message has been received ('0' — disabled, '1' — enabled).
        :param message_reply: A new outcoming message has been received ('0' — disabled, '1' — enabled).
        :param message_allow: Allowed messages notifications ('0' — disabled, '1' — enabled).
        :param message_edit:
        :param message_deny: Denied messages notifications ('0' — disabled, '1' — enabled).
        :param message_typing_state:
        :param photo_new: New photos notifications ('0' — disabled, '1' — enabled).
        :param audio_new: New audios notifications ('0' — disabled, '1' — enabled).
        :param video_new: New videos notifications ('0' — disabled, '1' — enabled).
        :param wall_reply_new: New wall replies notifications ('0' — disabled, '1' — enabled).
        :param wall_reply_edit: Wall replies edited notifications ('0' — disabled, '1' — enabled).
        :param wall_reply_delete: A wall comment has been deleted ('0' — disabled, '1' — enabled).
        :param wall_reply_restore: A wall comment has been restored ('0' — disabled, '1' — enabled).
        :param wall_post_new: New wall posts notifications ('0' — disabled, '1' — enabled).
        :param wall_repost: New wall posts notifications ('0' — disabled, '1' — enabled).
        :param board_post_new: New board posts notifications ('0' — disabled, '1' — enabled).
        :param board_post_edit: Board posts edited notifications ('0' — disabled, '1' — enabled).
        :param board_post_restore: Board posts restored notifications ('0' — disabled, '1' — enabled).
        :param board_post_delete: Board posts deleted notifications ('0' — disabled, '1' — enabled).
        :param photo_comment_new: New comment to photo notifications ('0' — disabled, '1' — enabled).
        :param photo_comment_edit: A photo comment has been edited ('0' — disabled, '1' — enabled).
        :param photo_comment_delete: A photo comment has been deleted ('0' — disabled, '1' — enabled).
        :param photo_comment_restore: A photo comment has been restored ('0' — disabled, '1' — enabled).
        :param video_comment_new: New comment to video notifications ('0' — disabled, '1' — enabled).
        :param video_comment_edit: A video comment has been edited ('0' — disabled, '1' — enabled).
        :param video_comment_delete: A video comment has been deleted ('0' — disabled, '1' — enabled).
        :param video_comment_restore: A video comment has been restored ('0' — disabled, '1' — enabled).
        :param market_comment_new: New comment to market item notifications ('0' — disabled, '1' — enabled).
        :param market_comment_edit: A market comment has been edited ('0' — disabled, '1' — enabled).
        :param market_comment_delete: A market comment has been deleted ('0' — disabled, '1' — enabled).
        :param market_comment_restore: A market comment has been restored ('0' — disabled, '1' — enabled).
        :param poll_vote_new: A vote in a public poll has been added ('0' — disabled, '1' — enabled).
        :param group_join: Joined community notifications ('0' — disabled, '1' — enabled).
        :param group_leave: Left community notifications ('0' — disabled, '1' — enabled).
        :param group_change_settings:
        :param group_change_photo:
        :param group_officers_edit:
        :param user_block: User added to community blacklist
        :param user_unblock: User removed from community blacklist
        :param lead_forms_new: New form in lead forms
        :param like_add:
        :param like_remove:
        :param message_event:
        """

        params = self.get_set_params(locals())
        return base.OkResponse(
            **await self.api.request("groups.setCallbackSettings", params)
        ).response

    async def set_long_poll_settings(
        self,
        group_id: int,
        enabled: Optional[bool] = None,
        api_version: Optional[str] = None,
        message_new: Optional[bool] = None,
        message_reply: Optional[bool] = None,
        message_allow: Optional[bool] = None,
        message_deny: Optional[bool] = None,
        message_edit: Optional[bool] = None,
        message_typing_state: Optional[bool] = None,
        photo_new: Optional[bool] = None,
        audio_new: Optional[bool] = None,
        video_new: Optional[bool] = None,
        wall_reply_new: Optional[bool] = None,
        wall_reply_edit: Optional[bool] = None,
        wall_reply_delete: Optional[bool] = None,
        wall_reply_restore: Optional[bool] = None,
        wall_post_new: Optional[bool] = None,
        wall_repost: Optional[bool] = None,
        board_post_new: Optional[bool] = None,
        board_post_edit: Optional[bool] = None,
        board_post_restore: Optional[bool] = None,
        board_post_delete: Optional[bool] = None,
        photo_comment_new: Optional[bool] = None,
        photo_comment_edit: Optional[bool] = None,
        photo_comment_delete: Optional[bool] = None,
        photo_comment_restore: Optional[bool] = None,
        video_comment_new: Optional[bool] = None,
        video_comment_edit: Optional[bool] = None,
        video_comment_delete: Optional[bool] = None,
        video_comment_restore: Optional[bool] = None,
        market_comment_new: Optional[bool] = None,
        market_comment_edit: Optional[bool] = None,
        market_comment_delete: Optional[bool] = None,
        market_comment_restore: Optional[bool] = None,
        poll_vote_new: Optional[bool] = None,
        group_join: Optional[bool] = None,
        group_leave: Optional[bool] = None,
        group_change_settings: Optional[bool] = None,
        group_change_photo: Optional[bool] = None,
        group_officers_edit: Optional[bool] = None,
        user_block: Optional[bool] = None,
        user_unblock: Optional[bool] = None,
        like_add: Optional[bool] = None,
        like_remove: Optional[bool] = None,
        message_event: Optional[bool] = None,
        **kwargs
    ) -> base.OkResponseModel:
        """Sets Long Poll notification settings
        :param group_id: Community ID.
        :param enabled: Sets whether Long Poll is enabled ('0' — disabled, '1' — enabled).
        :param api_version:
        :param message_new: A new incoming message has been received ('0' — disabled, '1' — enabled).
        :param message_reply: A new outcoming message has been received ('0' — disabled, '1' — enabled).
        :param message_allow: Allowed messages notifications ('0' — disabled, '1' — enabled).
        :param message_deny: Denied messages notifications ('0' — disabled, '1' — enabled).
        :param message_edit: A message has been edited ('0' — disabled, '1' — enabled).
        :param message_typing_state:
        :param photo_new: New photos notifications ('0' — disabled, '1' — enabled).
        :param audio_new: New audios notifications ('0' — disabled, '1' — enabled).
        :param video_new: New videos notifications ('0' — disabled, '1' — enabled).
        :param wall_reply_new: New wall replies notifications ('0' — disabled, '1' — enabled).
        :param wall_reply_edit: Wall replies edited notifications ('0' — disabled, '1' — enabled).
        :param wall_reply_delete: A wall comment has been deleted ('0' — disabled, '1' — enabled).
        :param wall_reply_restore: A wall comment has been restored ('0' — disabled, '1' — enabled).
        :param wall_post_new: New wall posts notifications ('0' — disabled, '1' — enabled).
        :param wall_repost: New wall posts notifications ('0' — disabled, '1' — enabled).
        :param board_post_new: New board posts notifications ('0' — disabled, '1' — enabled).
        :param board_post_edit: Board posts edited notifications ('0' — disabled, '1' — enabled).
        :param board_post_restore: Board posts restored notifications ('0' — disabled, '1' — enabled).
        :param board_post_delete: Board posts deleted notifications ('0' — disabled, '1' — enabled).
        :param photo_comment_new: New comment to photo notifications ('0' — disabled, '1' — enabled).
        :param photo_comment_edit: A photo comment has been edited ('0' — disabled, '1' — enabled).
        :param photo_comment_delete: A photo comment has been deleted ('0' — disabled, '1' — enabled).
        :param photo_comment_restore: A photo comment has been restored ('0' — disabled, '1' — enabled).
        :param video_comment_new: New comment to video notifications ('0' — disabled, '1' — enabled).
        :param video_comment_edit: A video comment has been edited ('0' — disabled, '1' — enabled).
        :param video_comment_delete: A video comment has been deleted ('0' — disabled, '1' — enabled).
        :param video_comment_restore: A video comment has been restored ('0' — disabled, '1' — enabled).
        :param market_comment_new: New comment to market item notifications ('0' — disabled, '1' — enabled).
        :param market_comment_edit: A market comment has been edited ('0' — disabled, '1' — enabled).
        :param market_comment_delete: A market comment has been deleted ('0' — disabled, '1' — enabled).
        :param market_comment_restore: A market comment has been restored ('0' — disabled, '1' — enabled).
        :param poll_vote_new: A vote in a public poll has been added ('0' — disabled, '1' — enabled).
        :param group_join: Joined community notifications ('0' — disabled, '1' — enabled).
        :param group_leave: Left community notifications ('0' — disabled, '1' — enabled).
        :param group_change_settings:
        :param group_change_photo:
        :param group_officers_edit:
        :param user_block: User added to community blacklist
        :param user_unblock: User removed from community blacklist
        :param like_add:
        :param like_remove:
        :param message_event:
        """

        params = self.get_set_params(locals())
        return base.OkResponse(
            **await self.api.request("groups.setLongPollSettings", params)
        ).response

    async def unban(
        self, group_id: int, owner_id: Optional[int] = None, **kwargs
    ) -> base.OkResponseModel:
        """groups.unban method
        :param group_id:
        :param owner_id:
        """

        params = self.get_set_params(locals())
        return base.OkResponse(
            **await self.api.request("groups.unban", params)
        ).response
