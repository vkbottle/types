import typing

from typing_extensions import Literal
from vkbottle_types.methods.base_category import BaseCategory
from vkbottle_types.responses.groups import *
from vkbottle_types.responses.base import OkResponse


class GroupsCategory(BaseCategory):
    async def add_address(
        self,
        group_id: int,
        title: str,
        address: str,
        city_id: int,
        latitude: float,
        longitude: float,
        additional_address: typing.Optional[str] = None,
        metro_id: typing.Optional[int] = None,
        phone: typing.Optional[str] = None,
        work_info_status: typing.Optional[str] = "no_information",
        timetable: typing.Optional[str] = None,
        is_main_address: typing.Optional[bool] = None,
        **kwargs,
    ) -> GroupsAddAddressResponseModel:
        """groups.addAddress method


        :param group_id:
        :param title:
        :param address:
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
        response = await self.api.request("account.ban", params)

        model = GroupsAddAddressResponse

        return model(**response).response

    async def add_callback_server(
        self,
        group_id: int,
        url: str,
        title: str,
        secret_key: typing.Optional[str] = None,
        **kwargs,
    ) -> GroupsAddCallbackServerResponseModel:
        """groups.addCallbackServer method


        :param group_id:
        :param url:
        :param title:
        :param secret_key:
        """
        params = self.get_set_params(locals())
        response = await self.api.request("account.ban", params)

        model = GroupsAddCallbackServerResponse

        return model(**response).response

    async def add_link(
        self,
        group_id: int,
        link: str,
        text: typing.Optional[str] = None,
        **kwargs,
    ) -> GroupsAddLinkResponseModel:
        """groups.addLink method


        :param group_id: Community ID.
        :param link: Link URL.
        :param text: Description text for the link.
        """
        params = self.get_set_params(locals())
        response = await self.api.request("account.ban", params)

        model = GroupsAddLinkResponse

        return model(**response).response

    async def approve_request(
        self,
        group_id: int,
        user_id: int,
        **kwargs,
    ) -> BaseOkResponseModel:
        """groups.approveRequest method


        :param group_id: Community ID.
        :param user_id: User ID.
        """
        params = self.get_set_params(locals())
        response = await self.api.request("account.ban", params)

        model = BaseOkResponse

        return model(**response).response

    async def ban(
        self,
        group_id: int,
        owner_id: typing.Optional[int] = None,
        end_date: typing.Optional[int] = None,
        reason: typing.Optional[int] = None,
        comment: typing.Optional[str] = None,
        comment_visible: typing.Optional[bool] = None,
        **kwargs,
    ) -> BaseOkResponseModel:
        """groups.ban method


        :param group_id:
        :param owner_id:
        :param end_date:
        :param reason:
        :param comment:
        :param comment_visible:
        """
        params = self.get_set_params(locals())
        response = await self.api.request("account.ban", params)

        model = BaseOkResponse

        return model(**response).response

    async def create(
        self,
        title: str,
        description: typing.Optional[str] = None,
        type: typing.Optional[str] = "group",
        public_category: typing.Optional[int] = None,
        public_subcategory: typing.Optional[int] = None,
        subtype: typing.Optional[int] = None,
        **kwargs,
    ) -> GroupsCreateResponseModel:
        """groups.create method


        :param title: Community title.
        :param description: Community description (ignored for 'type' = 'public').
        :param type: Community type. Possible values: *'group' - group,, *'event' - event,, *'public' - public page
        :param public_category: Category ID (for 'type' = 'public' only).
        :param public_subcategory: Public page subcategory ID.
        :param subtype: Public page subtype. Possible values: *'1' - place or small business,, *'2' - company, organization or website,, *'3' - famous person or group of people,, *'4' - product or work of art.
        """
        params = self.get_set_params(locals())
        response = await self.api.request("account.ban", params)

        model = GroupsCreateResponse

        return model(**response).response

    async def delete_address(
        self,
        group_id: int,
        address_id: int,
        **kwargs,
    ) -> BaseOkResponseModel:
        """groups.deleteAddress method


        :param group_id:
        :param address_id:
        """
        params = self.get_set_params(locals())
        response = await self.api.request("account.ban", params)

        model = BaseOkResponse

        return model(**response).response

    async def delete_callback_server(
        self,
        group_id: int,
        server_id: int,
        **kwargs,
    ) -> BaseOkResponseModel:
        """groups.deleteCallbackServer method


        :param group_id:
        :param server_id:
        """
        params = self.get_set_params(locals())
        response = await self.api.request("account.ban", params)

        model = BaseOkResponse

        return model(**response).response

    async def delete_link(
        self,
        group_id: int,
        link_id: int,
        **kwargs,
    ) -> BaseOkResponseModel:
        """groups.deleteLink method


        :param group_id: Community ID.
        :param link_id: Link ID.
        """
        params = self.get_set_params(locals())
        response = await self.api.request("account.ban", params)

        model = BaseOkResponse

        return model(**response).response

    async def disable_online(
        self,
        group_id: int,
        **kwargs,
    ) -> BaseOkResponseModel:
        """groups.disableOnline method


        :param group_id:
        """
        params = self.get_set_params(locals())
        response = await self.api.request("account.ban", params)

        model = BaseOkResponse

        return model(**response).response

    async def edit(
        self,
        group_id: int,
        title: typing.Optional[str] = None,
        description: typing.Optional[str] = None,
        screen_name: typing.Optional[str] = None,
        access: typing.Optional[int] = None,
        website: typing.Optional[str] = None,
        subject: typing.Optional[int] = None,
        email: typing.Optional[str] = None,
        phone: typing.Optional[str] = None,
        rss: typing.Optional[str] = None,
        event_start_date: typing.Optional[int] = None,
        event_finish_date: typing.Optional[int] = None,
        event_group_id: typing.Optional[int] = None,
        public_category: typing.Optional[int] = None,
        public_subcategory: typing.Optional[int] = None,
        public_date: typing.Optional[str] = None,
        wall: typing.Optional[int] = None,
        topics: typing.Optional[int] = None,
        photos: typing.Optional[int] = None,
        video: typing.Optional[int] = None,
        audio: typing.Optional[int] = None,
        links: typing.Optional[bool] = None,
        events: typing.Optional[bool] = None,
        places: typing.Optional[bool] = None,
        contacts: typing.Optional[bool] = None,
        docs: typing.Optional[int] = None,
        wiki: typing.Optional[int] = None,
        messages: typing.Optional[bool] = None,
        articles: typing.Optional[bool] = None,
        addresses: typing.Optional[bool] = None,
        age_limits: typing.Optional[int] = 1,
        market: typing.Optional[bool] = None,
        market_buttons: typing.Optional[str] = None,
        market_comments: typing.Optional[bool] = None,
        market_country: typing.Optional[typing.List[int]] = None,
        market_city: typing.Optional[typing.List[int]] = None,
        market_currency: typing.Optional[int] = None,
        market_contact: typing.Optional[int] = None,
        market_wiki: typing.Optional[int] = None,
        obscene_filter: typing.Optional[bool] = None,
        obscene_stopwords: typing.Optional[bool] = None,
        obscene_words: typing.Optional[typing.List[str]] = None,
        main_section: typing.Optional[int] = None,
        secondary_section: typing.Optional[int] = None,
        country: typing.Optional[int] = None,
        city: typing.Optional[int] = None,
        **kwargs,
    ) -> BaseOkResponseModel:
        """groups.edit method


        :param group_id: Community ID.
        :param title: Community title.
        :param description: Community description.
        :param screen_name: Community screen name.
        :param access: Community type. Possible values: *'0' - open,, *'1' - closed,, *'2' - private.
        :param website: Website that will be displayed in the community information field.
        :param subject: Community subject. Possible values: , *'1' - auto/moto,, *'2' - activity holidays,, *'3' - business,, *'4' - pets,, *'5' - health,, *'6' - dating and communication, , *'7' - games,, *'8' - IT (computers and software),, *'9' - cinema,, *'10' - beauty and fashion,, *'11' - cooking,, *'12' - art and culture,, *'13' - literature,, *'14' - mobile services and internet,, *'15' - music,, *'16' - science and technology,, *'17' - real estate,, *'18' - news and media,, *'19' - security,, *'20' - education,, *'21' - home and renovations,, *'22' - politics,, *'23' - food,, *'24' - industry,, *'25' - travel,, *'26' - work,, *'27' - entertainment,, *'28' - religion,, *'29' - family,, *'30' - sports,, *'31' - insurance,, *'32' - television,, *'33' - goods and services,, *'34' - hobbies,, *'35' - finance,, *'36' - photo,, *'37' - esoterics,, *'38' - electronics and appliances,, *'39' - erotic,, *'40' - humor,, *'41' - society, humanities,, *'42' - design and graphics.
        :param email: Organizer email (for events).
        :param phone: Organizer phone number (for events).
        :param rss: RSS feed address for import (available only to communities with special permission. Contact vk.com/support to get it.
        :param event_start_date: Event start date in Unixtime format.
        :param event_finish_date: Event finish date in Unixtime format.
        :param event_group_id: Organizer community ID (for events only).
        :param public_category: Public page category ID.
        :param public_subcategory: Public page subcategory ID.
        :param public_date: Founding date of a company or organization owning the community in "dd.mm.YYYY" format.
        :param wall: Wall settings. Possible values: *'0' - disabled,, *'1' - open,, *'2' - limited (groups and events only),, *'3' - closed (groups and events only).
        :param topics: Board topics settings. Possbile values: , *'0' - disabled,, *'1' - open,, *'2' - limited (for groups and events only).
        :param photos: Photos settings. Possible values: *'0' - disabled,, *'1' - open,, *'2' - limited (for groups and events only).
        :param video: Video settings. Possible values: *'0' - disabled,, *'1' - open,, *'2' - limited (for groups and events only).
        :param audio: Audio settings. Possible values: *'0' - disabled,, *'1' - open,, *'2' - limited (for groups and events only).
        :param links: Links settings (for public pages only). Possible values: *'0' - disabled,, *'1' - enabled.
        :param events: Events settings (for public pages only). Possible values: *'0' - disabled,, *'1' - enabled.
        :param places: Places settings (for public pages only). Possible values: *'0' - disabled,, *'1' - enabled.
        :param contacts: Contacts settings (for public pages only). Possible values: *'0' - disabled,, *'1' - enabled.
        :param docs: Documents settings. Possible values: *'0' - disabled,, *'1' - open,, *'2' - limited (for groups and events only).
        :param wiki: Wiki pages settings. Possible values: *'0' - disabled,, *'1' - open,, *'2' - limited (for groups and events only).
        :param messages: Community messages. Possible values: *'0' - disabled,, *'1' - enabled.
        :param articles:
        :param addresses:
        :param age_limits: Community age limits. Possible values: *'1' - no limits,, *'2' - 16+,, *'3' - 18+.
        :param market: Market settings. Possible values: *'0' - disabled,, *'1' - enabled.
        :param market_buttons: Buttons details, see market/objects.json#/definitions/market_custom_button
        :param market_comments: market comments settings. Possible values: *'0' - disabled,, *'1' - enabled.
        :param market_country: Market delivery countries.
        :param market_city: Market delivery cities (if only one country is specified).
        :param market_currency: Market currency settings. Possbile values: , *'643' - Russian rubles,, *'980' - Ukrainian hryvnia,, *'398' - Kazakh tenge,, *'978' - Euro,, *'840' - US dollars
        :param market_contact: Seller contact for market. Set '0' for community messages.
        :param market_wiki: ID of a wiki page with market description.
        :param obscene_filter: Obscene expressions filter in comments. Possible values: , *'0' - disabled,, *'1' - enabled.
        :param obscene_stopwords: Stopwords filter in comments. Possible values: , *'0' - disabled,, *'1' - enabled.
        :param obscene_words: Keywords for stopwords filter.
        :param main_section:
        :param secondary_section:
        :param country: Country of the community.
        :param city: City of the community.
        """
        params = self.get_set_params(locals())
        response = await self.api.request("account.ban", params)

        model = BaseOkResponse

        return model(**response).response

    async def edit_address(
        self,
        group_id: int,
        address_id: int,
        title: typing.Optional[str] = None,
        address: typing.Optional[str] = None,
        additional_address: typing.Optional[str] = None,
        city_id: typing.Optional[int] = None,
        metro_id: typing.Optional[int] = None,
        latitude: typing.Optional[float] = None,
        longitude: typing.Optional[float] = None,
        phone: typing.Optional[str] = None,
        work_info_status: typing.Optional[str] = None,
        timetable: typing.Optional[str] = None,
        is_main_address: typing.Optional[bool] = None,
        **kwargs,
    ) -> GroupsEditAddressResponseModel:
        """groups.editAddress method


        :param group_id:
        :param address_id:
        :param title:
        :param address:
        :param additional_address:
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
        response = await self.api.request("account.ban", params)

        model = GroupsEditAddressResponse

        return model(**response).response

    async def edit_callback_server(
        self,
        group_id: int,
        server_id: int,
        url: str,
        title: str,
        secret_key: typing.Optional[str] = None,
        **kwargs,
    ) -> BaseOkResponseModel:
        """groups.editCallbackServer method


        :param group_id:
        :param server_id:
        :param url:
        :param title:
        :param secret_key:
        """
        params = self.get_set_params(locals())
        response = await self.api.request("account.ban", params)

        model = BaseOkResponse

        return model(**response).response

    async def edit_link(
        self,
        group_id: int,
        link_id: int,
        text: typing.Optional[str] = None,
        **kwargs,
    ) -> BaseOkResponseModel:
        """groups.editLink method


        :param group_id: Community ID.
        :param link_id: Link ID.
        :param text: New description text for the link.
        """
        params = self.get_set_params(locals())
        response = await self.api.request("account.ban", params)

        model = BaseOkResponse

        return model(**response).response

    async def edit_manager(
        self,
        group_id: int,
        user_id: int,
        role: typing.Optional[str] = None,
        is_call_operator: typing.Optional[bool] = None,
        is_contact: typing.Optional[bool] = None,
        contact_position: typing.Optional[str] = None,
        contact_phone: typing.Optional[str] = None,
        contact_email: typing.Optional[str] = None,
        **kwargs,
    ) -> BaseOkResponseModel:
        """groups.editManager method


        :param group_id: Community ID.
        :param user_id: User ID.
        :param role: Manager role. Possible values: *'moderator',, *'editor',, *'administrator',, *'advertiser'.
        :param is_call_operator: '1' — allow the manager to accept community calls.
        :param is_contact: '1' - to show the manager in Contacts block of the community.
        :param contact_position: Position to show in Contacts block.
        :param contact_phone: Contact phone.
        :param contact_email: Contact e-mail.
        """
        params = self.get_set_params(locals())
        response = await self.api.request("account.ban", params)

        model = BaseOkResponse

        return model(**response).response

    async def enable_online(
        self,
        group_id: int,
        **kwargs,
    ) -> BaseOkResponseModel:
        """groups.enableOnline method


        :param group_id:
        """
        params = self.get_set_params(locals())
        response = await self.api.request("account.ban", params)

        model = BaseOkResponse

        return model(**response).response

    @typing.overload
    async def get(
        self,
        extended: typing.Literal[True] = True,
        user_id: typing.Optional[int] = None,
        filter: typing.Optional[typing.List[GroupsFilter]] = None,
        fields: typing.Optional[typing.List[GroupsFields]] = None,
        offset: typing.Optional[int] = None,
        count: typing.Optional[int] = None,
        **kwargs,
    ) -> GroupsGetObjectExtendedResponseModel:
        ...

    async def get(
        self,
        user_id: typing.Optional[int] = None,
        extended: typing.Optional[bool] = None,
        filter: typing.Optional[typing.List[GroupsFilter]] = None,
        fields: typing.Optional[typing.List[GroupsFields]] = None,
        offset: typing.Optional[int] = None,
        count: typing.Optional[int] = None,
        **kwargs,
    ) -> GroupsGetResponseModel:
        """groups.get method


        :param user_id: User ID.
        :param extended: '1' - to return complete information about a user's communities, '0' - to return a list of community IDs without any additional fields (default),
        :param filter: Types of communities to return: 'admin' - to return communities administered by the user , 'editor' - to return communities where the user is an administrator or editor, 'moder' - to return communities where the user is an administrator, editor, or moderator, 'groups' - to return only groups, 'publics' - to return only public pages, 'events' - to return only events
        :param fields: Profile fields to return.
        :param offset: Offset needed to return a specific subset of communities.
        :param count: Number of communities to return.
        """
        params = self.get_set_params(locals())
        response = await self.api.request("account.ban", params)

        model = self.get_model(
            ((("extended",), GroupsGetObjectExtendedResponse),),
            default=GroupsGetResponse,
            params=params,
        )

        return model(**response).response

    async def get_addresses(
        self,
        group_id: int,
        address_ids: typing.Optional[typing.List[int]] = None,
        latitude: typing.Optional[float] = None,
        longitude: typing.Optional[float] = None,
        offset: typing.Optional[int] = None,
        count: typing.Optional[int] = 10,
        fields: typing.Optional[typing.List[AddressFields]] = None,
        **kwargs,
    ) -> GroupsGetAddressesResponseModel:
        """groups.getAddresses method


        :param group_id: ID or screen name of the community.
        :param address_ids:
        :param latitude: Latitude of  the user geo position.
        :param longitude: Longitude of the user geo position.
        :param offset: Offset needed to return a specific subset of community addresses.
        :param count: Number of community addresses to return.
        :param fields: Address fields
        """
        params = self.get_set_params(locals())
        response = await self.api.request("account.ban", params)

        model = GroupsGetAddressesResponse

        return model(**response).response

    async def get_banned(
        self,
        group_id: int,
        offset: typing.Optional[int] = None,
        count: typing.Optional[int] = 20,
        fields: typing.Optional[typing.List[BaseUserGroupFields]] = None,
        owner_id: typing.Optional[int] = None,
        **kwargs,
    ) -> GroupsGetBannedResponseModel:
        """groups.getBanned method


        :param group_id: Community ID.
        :param offset: Offset needed to return a specific subset of users.
        :param count: Number of users to return.
        :param fields:
        :param owner_id:
        """
        params = self.get_set_params(locals())
        response = await self.api.request("account.ban", params)

        model = GroupsGetBannedResponse

        return model(**response).response

    async def get_by_id(
        self,
        group_ids: typing.Optional[typing.List[typing.Union["int", "str"]]] = None,
        group_id: typing.Optional[typing.Union["int", "str"]] = None,
        fields: typing.Optional[typing.List[GroupsFields]] = None,
        **kwargs,
    ) -> GroupsGetByIdObjectResponseModel:
        """groups.getById method


        :param group_ids: IDs or screen names of communities.
        :param group_id: ID or screen name of the community.
        :param fields: Group fields to return.
        """
        params = self.get_set_params(locals())
        response = await self.api.request("account.ban", params)

        model = GroupsGetByIdObjectResponse

        return model(**response).response

    async def get_callback_confirmation_code(
        self,
        group_id: int,
        **kwargs,
    ) -> GroupsGetCallbackConfirmationCodeResponseModel:
        """groups.getCallbackConfirmationCode method


        :param group_id: Community ID.
        """
        params = self.get_set_params(locals())
        response = await self.api.request("account.ban", params)

        model = GroupsGetCallbackConfirmationCodeResponse

        return model(**response).response

    async def get_callback_servers(
        self,
        group_id: int,
        server_ids: typing.Optional[typing.List[int]] = None,
        **kwargs,
    ) -> GroupsGetCallbackServersResponseModel:
        """groups.getCallbackServers method


        :param group_id:
        :param server_ids:
        """
        params = self.get_set_params(locals())
        response = await self.api.request("account.ban", params)

        model = GroupsGetCallbackServersResponse

        return model(**response).response

    async def get_callback_settings(
        self,
        group_id: int,
        server_id: typing.Optional[int] = None,
        **kwargs,
    ) -> GroupsGetCallbackSettingsResponseModel:
        """groups.getCallbackSettings method


        :param group_id: Community ID.
        :param server_id: Server ID.
        """
        params = self.get_set_params(locals())
        response = await self.api.request("account.ban", params)

        model = GroupsGetCallbackSettingsResponse

        return model(**response).response

    @typing.overload
    async def get_catalog_info(
        self,
        extended: typing.Literal[True] = True,
        subcategories: typing.Optional[bool] = 0,
        **kwargs,
    ) -> GroupsGetCatalogInfoExtendedResponseModel:
        ...

    async def get_catalog_info(
        self,
        extended: typing.Optional[bool] = 0,
        subcategories: typing.Optional[bool] = 0,
        **kwargs,
    ) -> GroupsGetCatalogInfoResponseModel:
        """groups.getCatalogInfo method


        :param extended: 1 - to return communities count and three communities for preview. By default: 0.
        :param subcategories: 1 - to return subcategories info. By default: 0.
        """
        params = self.get_set_params(locals())
        response = await self.api.request("account.ban", params)

        model = self.get_model(
            ((("extended",), GroupsGetCatalogInfoExtendedResponse),),
            default=GroupsGetCatalogInfoResponse,
            params=params,
        )

        return model(**response).response

    async def get_invited_users(
        self,
        group_id: int,
        offset: typing.Optional[int] = None,
        count: typing.Optional[int] = 20,
        fields: typing.Optional[typing.List[UsersFields]] = None,
        name_case: typing.Optional[str] = None,
        **kwargs,
    ) -> GroupsGetInvitedUsersResponseModel:
        """groups.getInvitedUsers method


        :param group_id: Group ID to return invited users for.
        :param offset: Offset needed to return a specific subset of results.
        :param count: Number of results to return.
        :param fields: List of additional fields to be returned. Available values: 'sex, bdate, city, country, photo_50, photo_100, photo_200_orig, photo_200, photo_400_orig, photo_max, photo_max_orig, online, online_mobile, lists, domain, has_mobile, contacts, connections, site, education, universities, schools, can_post, can_see_all_posts, can_see_audio, can_write_private_message, status, last_seen, common_count, relation, relatives, counters'.
        :param name_case: Case for declension of user name and surname. Possible values: *'nom' - nominative (default),, *'gen' - genitive,, *'dat' - dative,, *'acc' - accusative, , *'ins' - instrumental,, *'abl' - prepositional.
        """
        params = self.get_set_params(locals())
        response = await self.api.request("account.ban", params)

        model = GroupsGetInvitedUsersResponse

        return model(**response).response

    @typing.overload
    async def get_invites(
        self,
        extended: typing.Literal[True] = True,
        offset: typing.Optional[int] = None,
        count: typing.Optional[int] = 20,
        **kwargs,
    ) -> GroupsGetInvitesExtendedResponseModel:
        ...

    async def get_invites(
        self,
        offset: typing.Optional[int] = None,
        count: typing.Optional[int] = 20,
        extended: typing.Optional[bool] = None,
        **kwargs,
    ) -> GroupsGetInvitesResponseModel:
        """groups.getInvites method


        :param offset: Offset needed to return a specific subset of invitations.
        :param count: Number of invitations to return.
        :param extended: '1' - to return additional [vk.com/dev/fields_groups|fields] for communities..
        """
        params = self.get_set_params(locals())
        response = await self.api.request("account.ban", params)

        model = self.get_model(
            ((("extended",), GroupsGetInvitesExtendedResponse),),
            default=GroupsGetInvitesResponse,
            params=params,
        )

        return model(**response).response

    async def get_long_poll_server(
        self,
        group_id: int,
        **kwargs,
    ) -> GroupsGetLongPollServerResponseModel:
        """groups.getLongPollServer method


        :param group_id: Community ID.
        """
        params = self.get_set_params(locals())
        response = await self.api.request("account.ban", params)

        model = GroupsGetLongPollServerResponse

        return model(**response).response

    async def get_long_poll_settings(
        self,
        group_id: int,
        **kwargs,
    ) -> GroupsGetLongPollSettingsResponseModel:
        """groups.getLongPollSettings method


        :param group_id: Community ID.
        """
        params = self.get_set_params(locals())
        response = await self.api.request("account.ban", params)

        model = GroupsGetLongPollSettingsResponse

        return model(**response).response

    @typing.overload
    async def get_members(
        self,
        fields: typing.List[UsersFields],
        group_id: typing.Optional[typing.Union["int", "str"]] = None,
        sort: typing.Optional[str] = "id_asc",
        offset: typing.Optional[int] = None,
        count: typing.Optional[int] = 1000,
        filter: typing.Optional[str] = None,
        **kwargs,
    ) -> GroupsGetMembersFieldsResponseModel:
        ...

    @typing.overload
    async def get_members(
        self,
        filter: str,
        group_id: typing.Optional[typing.Union["int", "str"]] = None,
        sort: typing.Optional[str] = "id_asc",
        offset: typing.Optional[int] = None,
        count: typing.Optional[int] = 1000,
        fields: typing.Optional[typing.List[UsersFields]] = None,
        **kwargs,
    ) -> GroupsGetMembersFilterResponseModel:
        ...

    async def get_members(
        self,
        group_id: typing.Optional[typing.Union["int", "str"]] = None,
        sort: typing.Optional[str] = "id_asc",
        offset: typing.Optional[int] = None,
        count: typing.Optional[int] = 1000,
        fields: typing.Optional[typing.List[UsersFields]] = None,
        filter: typing.Optional[str] = None,
        **kwargs,
    ) -> GroupsGetMembersResponseModel:
        """groups.getMembers method


        :param group_id: ID or screen name of the community.
        :param sort: Sort order. Available values: 'id_asc', 'id_desc', 'time_asc', 'time_desc'. 'time_asc' and 'time_desc' are availavle only if the method is called by the group's 'moderator'.
        :param offset: Offset needed to return a specific subset of community members.
        :param count: Number of community members to return.
        :param fields: List of additional fields to be returned. Available values: 'sex, bdate, city, country, photo_50, photo_100, photo_200_orig, photo_200, photo_400_orig, photo_max, photo_max_orig, online, online_mobile, lists, domain, has_mobile, contacts, connections, site, education, universities, schools, can_post, can_see_all_posts, can_see_audio, can_write_private_message, status, last_seen, common_count, relation, relatives, counters'.
        :param filter: *'friends' - only friends in this community will be returned,, *'unsure' - only those who pressed 'I may attend' will be returned (if it's an event).
        """
        params = self.get_set_params(locals())
        response = await self.api.request("account.ban", params)

        model = self.get_model(
            (
                (("fields",), GroupsGetMembersFieldsResponse),
                (("filter",), GroupsGetMembersFilterResponse),
            ),
            default=GroupsGetMembersResponse,
            params=params,
        )

        return model(**response).response

    async def get_online_status(
        self,
        group_id: int,
        **kwargs,
    ) -> GroupsGetOnlineStatusResponseModel:
        """groups.getOnlineStatus method


        :param group_id:
        """
        params = self.get_set_params(locals())
        response = await self.api.request("account.ban", params)

        model = GroupsGetOnlineStatusResponse

        return model(**response).response

    @typing.overload
    async def get_requests(
        self,
        group_id: int,
        fields: typing.List[UsersFields],
        offset: typing.Optional[int] = None,
        count: typing.Optional[int] = 20,
        **kwargs,
    ) -> GroupsGetRequestsFieldsResponseModel:
        ...

    async def get_requests(
        self,
        group_id: int,
        offset: typing.Optional[int] = None,
        count: typing.Optional[int] = 20,
        fields: typing.Optional[typing.List[UsersFields]] = None,
        **kwargs,
    ) -> GroupsGetRequestsResponseModel:
        """groups.getRequests method


        :param group_id: Community ID.
        :param offset: Offset needed to return a specific subset of results.
        :param count: Number of results to return.
        :param fields: Profile fields to return.
        """
        params = self.get_set_params(locals())
        response = await self.api.request("account.ban", params)

        model = self.get_model(
            ((("fields",), GroupsGetRequestsFieldsResponse),),
            default=GroupsGetRequestsResponse,
            params=params,
        )

        return model(**response).response

    async def get_settings(
        self,
        group_id: typing.Union["int", "str"],
        **kwargs,
    ) -> GroupsGetSettingsResponseModel:
        """groups.getSettings method


        :param group_id: Community ID.
        """
        params = self.get_set_params(locals())
        response = await self.api.request("account.ban", params)

        model = GroupsGetSettingsResponse

        return model(**response).response

    async def get_tag_list(
        self,
        group_id: int,
        **kwargs,
    ) -> GroupsGetTagListResponseModel:
        """groups.getTagList method


        :param group_id:
        """
        params = self.get_set_params(locals())
        response = await self.api.request("account.ban", params)

        model = GroupsGetTagListResponse

        return model(**response).response

    async def get_token_permissions(
        self,
        **kwargs,
    ) -> GroupsGetTokenPermissionsResponseModel:
        """groups.getTokenPermissions method"""
        params = self.get_set_params(locals())
        response = await self.api.request("account.ban", params)

        model = GroupsGetTokenPermissionsResponse

        return model(**response).response

    @typing.overload
    async def invite(
        self,
        group_id: int,
        user_id: typing.Optional[int] = None,
        user_ids_list: typing.Optional[typing.List[int]] = None,
        **kwargs,
    ) -> GroupsInviteUserIdsListResponseModel:
        ...

    async def invite(
        self,
        group_id: int,
        user_id: typing.Optional[int] = None,
        user_ids_list: typing.Optional[typing.List[int]] = None,
        **kwargs,
    ) -> BaseOkResponseModel:
        """groups.invite method


        :param group_id: Community ID.
        :param user_id: User ID.
        :param user_ids_list: User IDs.
        """
        params = self.get_set_params(locals())
        response = await self.api.request("account.ban", params)

        model = self.get_model(
            ((("user_ids",), GroupsInviteUserIdsListResponse),),
            default=BaseOkResponse,
            params=params,
        )

        return model(**response).response

    @typing.overload
    async def is_member(
        self,
        group_id: typing.Union["int", "str"],
        user_ids: typing.List[int],
        user_id: typing.Optional[int] = None,
        extended: typing.Optional[bool] = None,
        **kwargs,
    ) -> GroupsIsMemberUserIdsResponseModel:
        ...

    @typing.overload
    async def is_member(
        self,
        group_id: typing.Union["int", "str"],
        extended: typing.Literal[True] = True,
        user_id: typing.Optional[int] = None,
        user_ids: typing.Optional[typing.List[int]] = None,
        **kwargs,
    ) -> GroupsIsMemberExtendedResponseModel:
        ...

    @typing.overload
    async def is_member(
        self,
        group_id: typing.Union["int", "str"],
        user_id: typing.Optional[int] = None,
        user_ids: typing.Optional[typing.List[int]] = None,
        extended: typing.Optional[bool] = None,
        **kwargs,
    ) -> GroupsIsMemberUserIdsExtendedResponseModel:
        ...

    async def is_member(
        self,
        group_id: typing.Union["int", "str"],
        user_id: typing.Optional[int] = None,
        user_ids: typing.Optional[typing.List[int]] = None,
        extended: typing.Optional[bool] = None,
        **kwargs,
    ) -> BaseBoolResponseModel:
        """groups.isMember method


        :param group_id: ID or screen name of the community.
        :param user_id: User ID.
        :param user_ids: User IDs.
        :param extended: '1' - to return an extended response with additional fields. By default: '0'.
        """
        params = self.get_set_params(locals())
        response = await self.api.request("account.ban", params)

        model = self.get_model(
            (
                (("user_ids",), GroupsIsMemberUserIdsResponse),
                (("extended",), GroupsIsMemberExtendedResponse),
                (("user_ids__extended_",), GroupsIsMemberUserIdsExtendedResponse),
            ),
            default=BaseBoolResponse,
            params=params,
        )

        return model(**response).response

    async def join(
        self,
        group_id: typing.Optional[int] = None,
        not_sure: typing.Optional[str] = None,
        **kwargs,
    ) -> BaseOkResponseModel:
        """groups.join method


        :param group_id: ID or screen name of the community.
        :param not_sure: Optional parameter which is taken into account when 'gid' belongs to the event: '1' - Perhaps I will attend, '0' - I will be there for sure (default), ,
        """
        params = self.get_set_params(locals())
        response = await self.api.request("account.ban", params)

        model = BaseOkResponse

        return model(**response).response

    async def leave(
        self,
        group_id: int,
        **kwargs,
    ) -> BaseOkResponseModel:
        """groups.leave method


        :param group_id: ID or screen name of the community.
        """
        params = self.get_set_params(locals())
        response = await self.api.request("account.ban", params)

        model = BaseOkResponse

        return model(**response).response

    async def remove_user(
        self,
        group_id: int,
        user_id: int,
        **kwargs,
    ) -> BaseOkResponseModel:
        """groups.removeUser method


        :param group_id: Community ID.
        :param user_id: User ID.
        """
        params = self.get_set_params(locals())
        response = await self.api.request("account.ban", params)

        model = BaseOkResponse

        return model(**response).response

    async def reorder_link(
        self,
        group_id: int,
        link_id: int,
        after: typing.Optional[int] = None,
        **kwargs,
    ) -> BaseOkResponseModel:
        """groups.reorderLink method


        :param group_id: Community ID.
        :param link_id: Link ID.
        :param after: ID of the link after which to place the link with 'link_id'.
        """
        params = self.get_set_params(locals())
        response = await self.api.request("account.ban", params)

        model = BaseOkResponse

        return model(**response).response

    async def search(
        self,
        q: str,
        type: typing.Optional[str] = None,
        country_id: typing.Optional[int] = None,
        city_id: typing.Optional[int] = None,
        future: typing.Optional[bool] = None,
        market: typing.Optional[bool] = None,
        sort: typing.Optional[int] = None,
        offset: typing.Optional[int] = None,
        count: typing.Optional[int] = 20,
        **kwargs,
    ) -> GroupsSearchResponseModel:
        """groups.search method


        :param q: Search query string.
        :param type: Community type. Possible values: 'group, page, event.'
        :param country_id: Country ID.
        :param city_id: City ID. If this parameter is transmitted, country_id is ignored.
        :param future: '1' - to return only upcoming events. Works with the 'type' = 'event' only.
        :param market: '1' - to return communities with enabled market only.
        :param sort: Sort order. Possible values: *'0' - default sorting (similar the full version of the site),, *'1' - by growth speed,, *'2'- by the "day attendance/members number" ratio,, *'3' - by the "Likes number/members number" ratio,, *'4' - by the "comments number/members number" ratio,, *'5' - by the "boards entries number/members number" ratio.
        :param offset: Offset needed to return a specific subset of results.
        :param count: Number of communities to return. "Note that you can not receive more than first thousand of results, regardless of 'count' and 'offset' values."
        """
        params = self.get_set_params(locals())
        response = await self.api.request("account.ban", params)

        model = GroupsSearchResponse

        return model(**response).response

    async def set_callback_settings(
        self,
        group_id: int,
        server_id: typing.Optional[int] = None,
        api_version: typing.Optional[str] = None,
        message_new: typing.Optional[bool] = None,
        message_reply: typing.Optional[bool] = None,
        message_allow: typing.Optional[bool] = None,
        message_edit: typing.Optional[bool] = None,
        message_deny: typing.Optional[bool] = None,
        message_typing_state: typing.Optional[bool] = None,
        message_read: typing.Optional[bool] = None,
        photo_new: typing.Optional[bool] = None,
        audio_new: typing.Optional[bool] = None,
        video_new: typing.Optional[bool] = None,
        wall_reply_new: typing.Optional[bool] = None,
        wall_reply_edit: typing.Optional[bool] = None,
        wall_reply_delete: typing.Optional[bool] = None,
        wall_reply_restore: typing.Optional[bool] = None,
        wall_post_new: typing.Optional[bool] = None,
        wall_repost: typing.Optional[bool] = None,
        board_post_new: typing.Optional[bool] = None,
        board_post_edit: typing.Optional[bool] = None,
        board_post_restore: typing.Optional[bool] = None,
        board_post_delete: typing.Optional[bool] = None,
        photo_comment_new: typing.Optional[bool] = None,
        photo_comment_edit: typing.Optional[bool] = None,
        photo_comment_delete: typing.Optional[bool] = None,
        photo_comment_restore: typing.Optional[bool] = None,
        video_comment_new: typing.Optional[bool] = None,
        video_comment_edit: typing.Optional[bool] = None,
        video_comment_delete: typing.Optional[bool] = None,
        video_comment_restore: typing.Optional[bool] = None,
        market_comment_new: typing.Optional[bool] = None,
        market_comment_edit: typing.Optional[bool] = None,
        market_comment_delete: typing.Optional[bool] = None,
        market_comment_restore: typing.Optional[bool] = None,
        market_order_new: typing.Optional[bool] = None,
        market_order_edit: typing.Optional[bool] = None,
        poll_vote_new: typing.Optional[bool] = None,
        group_join: typing.Optional[bool] = None,
        group_leave: typing.Optional[bool] = None,
        group_change_settings: typing.Optional[bool] = None,
        group_change_photo: typing.Optional[bool] = None,
        group_officers_edit: typing.Optional[bool] = None,
        user_block: typing.Optional[bool] = None,
        user_unblock: typing.Optional[bool] = None,
        lead_forms_new: typing.Optional[bool] = None,
        like_add: typing.Optional[bool] = None,
        like_remove: typing.Optional[bool] = None,
        message_event: typing.Optional[bool] = None,
        message_reaction_event: typing.Optional[bool] = None,
        donut_subscription_create: typing.Optional[bool] = None,
        donut_subscription_prolonged: typing.Optional[bool] = None,
        donut_subscription_cancelled: typing.Optional[bool] = None,
        donut_subscription_price_changed: typing.Optional[bool] = None,
        donut_subscription_expired: typing.Optional[bool] = None,
        donut_money_withdraw: typing.Optional[bool] = None,
        donut_money_withdraw_error: typing.Optional[bool] = None,
        **kwargs,
    ) -> BaseOkResponseModel:
        """groups.setCallbackSettings method


        :param group_id: Community ID.
        :param server_id: Server ID.
        :param api_version:
        :param message_new: A new incoming message has been received ('0' - disabled, '1' - enabled).
        :param message_reply: A new outcoming message has been received ('0' - disabled, '1' - enabled).
        :param message_allow: Allowed messages notifications ('0' - disabled, '1' - enabled).
        :param message_edit:
        :param message_deny: Denied messages notifications ('0' - disabled, '1' - enabled).
        :param message_typing_state:
        :param message_read: Messages read notifications ('0' - disabled, '1' - enabled).
        :param photo_new: New photos notifications ('0' - disabled, '1' - enabled).
        :param audio_new: New audios notifications ('0' - disabled, '1' - enabled).
        :param video_new: New videos notifications ('0' - disabled, '1' - enabled).
        :param wall_reply_new: New wall replies notifications ('0' - disabled, '1' - enabled).
        :param wall_reply_edit: Wall replies edited notifications ('0' - disabled, '1' - enabled).
        :param wall_reply_delete: A wall comment has been deleted ('0' - disabled, '1' - enabled).
        :param wall_reply_restore: A wall comment has been restored ('0' - disabled, '1' - enabled).
        :param wall_post_new: New wall posts notifications ('0' - disabled, '1' - enabled).
        :param wall_repost: New wall posts notifications ('0' - disabled, '1' - enabled).
        :param board_post_new: New board posts notifications ('0' - disabled, '1' - enabled).
        :param board_post_edit: Board posts edited notifications ('0' - disabled, '1' - enabled).
        :param board_post_restore: Board posts restored notifications ('0' - disabled, '1' - enabled).
        :param board_post_delete: Board posts deleted notifications ('0' - disabled, '1' - enabled).
        :param photo_comment_new: New comment to photo notifications ('0' - disabled, '1' - enabled).
        :param photo_comment_edit: A photo comment has been edited ('0' - disabled, '1' - enabled).
        :param photo_comment_delete: A photo comment has been deleted ('0' - disabled, '1' - enabled).
        :param photo_comment_restore: A photo comment has been restored ('0' - disabled, '1' - enabled).
        :param video_comment_new: New comment to video notifications ('0' - disabled, '1' - enabled).
        :param video_comment_edit: A video comment has been edited ('0' - disabled, '1' - enabled).
        :param video_comment_delete: A video comment has been deleted ('0' - disabled, '1' - enabled).
        :param video_comment_restore: A video comment has been restored ('0' - disabled, '1' - enabled).
        :param market_comment_new: New comment to market item notifications ('0' - disabled, '1' - enabled).
        :param market_comment_edit: A market comment has been edited ('0' - disabled, '1' - enabled).
        :param market_comment_delete: A market comment has been deleted ('0' - disabled, '1' - enabled).
        :param market_comment_restore: A market comment has been restored ('0' - disabled, '1' - enabled).
        :param market_order_new:
        :param market_order_edit:
        :param poll_vote_new: A vote in a public poll has been added ('0' - disabled, '1' - enabled).
        :param group_join: Joined community notifications ('0' - disabled, '1' - enabled).
        :param group_leave: Left community notifications ('0' - disabled, '1' - enabled).
        :param group_change_settings:
        :param group_change_photo:
        :param group_officers_edit:
        :param user_block: User added to community blacklist
        :param user_unblock: User removed from community blacklist
        :param lead_forms_new: New form in lead forms
        :param like_add:
        :param like_remove:
        :param message_event:
        :param message_reaction_event:
        :param donut_subscription_create:
        :param donut_subscription_prolonged:
        :param donut_subscription_cancelled:
        :param donut_subscription_price_changed:
        :param donut_subscription_expired:
        :param donut_money_withdraw:
        :param donut_money_withdraw_error:
        """
        params = self.get_set_params(locals())
        response = await self.api.request("account.ban", params)

        model = BaseOkResponse

        return model(**response).response

    async def set_long_poll_settings(
        self,
        group_id: int,
        enabled: typing.Optional[bool] = None,
        api_version: typing.Optional[str] = None,
        message_new: typing.Optional[bool] = None,
        message_reply: typing.Optional[bool] = None,
        message_allow: typing.Optional[bool] = None,
        message_deny: typing.Optional[bool] = None,
        message_edit: typing.Optional[bool] = None,
        message_typing_state: typing.Optional[bool] = None,
        message_read: typing.Optional[bool] = None,
        photo_new: typing.Optional[bool] = None,
        audio_new: typing.Optional[bool] = None,
        video_new: typing.Optional[bool] = None,
        wall_reply_new: typing.Optional[bool] = None,
        wall_reply_edit: typing.Optional[bool] = None,
        wall_reply_delete: typing.Optional[bool] = None,
        wall_reply_restore: typing.Optional[bool] = None,
        wall_post_new: typing.Optional[bool] = None,
        wall_repost: typing.Optional[bool] = None,
        board_post_new: typing.Optional[bool] = None,
        board_post_edit: typing.Optional[bool] = None,
        board_post_restore: typing.Optional[bool] = None,
        board_post_delete: typing.Optional[bool] = None,
        photo_comment_new: typing.Optional[bool] = None,
        photo_comment_edit: typing.Optional[bool] = None,
        photo_comment_delete: typing.Optional[bool] = None,
        photo_comment_restore: typing.Optional[bool] = None,
        video_comment_new: typing.Optional[bool] = None,
        video_comment_edit: typing.Optional[bool] = None,
        video_comment_delete: typing.Optional[bool] = None,
        video_comment_restore: typing.Optional[bool] = None,
        market_comment_new: typing.Optional[bool] = None,
        market_comment_edit: typing.Optional[bool] = None,
        market_comment_delete: typing.Optional[bool] = None,
        market_comment_restore: typing.Optional[bool] = None,
        poll_vote_new: typing.Optional[bool] = None,
        group_join: typing.Optional[bool] = None,
        group_leave: typing.Optional[bool] = None,
        group_change_settings: typing.Optional[bool] = None,
        group_change_photo: typing.Optional[bool] = None,
        group_officers_edit: typing.Optional[bool] = None,
        user_block: typing.Optional[bool] = None,
        user_unblock: typing.Optional[bool] = None,
        like_add: typing.Optional[bool] = None,
        like_remove: typing.Optional[bool] = None,
        message_event: typing.Optional[bool] = None,
        message_reaction_event: typing.Optional[bool] = None,
        donut_subscription_create: typing.Optional[bool] = None,
        donut_subscription_prolonged: typing.Optional[bool] = None,
        donut_subscription_cancelled: typing.Optional[bool] = None,
        donut_subscription_price_changed: typing.Optional[bool] = None,
        donut_subscription_expired: typing.Optional[bool] = None,
        donut_money_withdraw: typing.Optional[bool] = None,
        donut_money_withdraw_error: typing.Optional[bool] = None,
        **kwargs,
    ) -> BaseOkResponseModel:
        """groups.setLongPollSettings method


        :param group_id: Community ID.
        :param enabled: Sets whether Long Poll is enabled ('0' - disabled, '1' - enabled).
        :param api_version:
        :param message_new: A new incoming message has been received ('0' - disabled, '1' - enabled).
        :param message_reply: A new outcoming message has been received ('0' - disabled, '1' - enabled).
        :param message_allow: Allowed messages notifications ('0' - disabled, '1' - enabled).
        :param message_deny: Denied messages notifications ('0' - disabled, '1' - enabled).
        :param message_edit: A message has been edited ('0' - disabled, '1' - enabled).
        :param message_typing_state:
        :param message_read: Messages read notifications ('0' - disabled, '1' - enabled).
        :param photo_new: New photos notifications ('0' - disabled, '1' - enabled).
        :param audio_new: New audios notifications ('0' - disabled, '1' - enabled).
        :param video_new: New videos notifications ('0' - disabled, '1' - enabled).
        :param wall_reply_new: New wall replies notifications ('0' - disabled, '1' - enabled).
        :param wall_reply_edit: Wall replies edited notifications ('0' - disabled, '1' - enabled).
        :param wall_reply_delete: A wall comment has been deleted ('0' - disabled, '1' - enabled).
        :param wall_reply_restore: A wall comment has been restored ('0' - disabled, '1' - enabled).
        :param wall_post_new: New wall posts notifications ('0' - disabled, '1' - enabled).
        :param wall_repost: New wall posts notifications ('0' - disabled, '1' - enabled).
        :param board_post_new: New board posts notifications ('0' - disabled, '1' - enabled).
        :param board_post_edit: Board posts edited notifications ('0' - disabled, '1' - enabled).
        :param board_post_restore: Board posts restored notifications ('0' - disabled, '1' - enabled).
        :param board_post_delete: Board posts deleted notifications ('0' - disabled, '1' - enabled).
        :param photo_comment_new: New comment to photo notifications ('0' - disabled, '1' - enabled).
        :param photo_comment_edit: A photo comment has been edited ('0' - disabled, '1' - enabled).
        :param photo_comment_delete: A photo comment has been deleted ('0' - disabled, '1' - enabled).
        :param photo_comment_restore: A photo comment has been restored ('0' - disabled, '1' - enabled).
        :param video_comment_new: New comment to video notifications ('0' - disabled, '1' - enabled).
        :param video_comment_edit: A video comment has been edited ('0' - disabled, '1' - enabled).
        :param video_comment_delete: A video comment has been deleted ('0' - disabled, '1' - enabled).
        :param video_comment_restore: A video comment has been restored ('0' - disabled, '1' - enabled).
        :param market_comment_new: New comment to market item notifications ('0' - disabled, '1' - enabled).
        :param market_comment_edit: A market comment has been edited ('0' - disabled, '1' - enabled).
        :param market_comment_delete: A market comment has been deleted ('0' - disabled, '1' - enabled).
        :param market_comment_restore: A market comment has been restored ('0' - disabled, '1' - enabled).
        :param poll_vote_new: A vote in a public poll has been added ('0' - disabled, '1' - enabled).
        :param group_join: Joined community notifications ('0' - disabled, '1' - enabled).
        :param group_leave: Left community notifications ('0' - disabled, '1' - enabled).
        :param group_change_settings:
        :param group_change_photo:
        :param group_officers_edit:
        :param user_block: User added to community blacklist
        :param user_unblock: User removed from community blacklist
        :param like_add:
        :param like_remove:
        :param message_event:
        :param message_reaction_event:
        :param donut_subscription_create:
        :param donut_subscription_prolonged:
        :param donut_subscription_cancelled:
        :param donut_subscription_price_changed:
        :param donut_subscription_expired:
        :param donut_money_withdraw:
        :param donut_money_withdraw_error:
        """
        params = self.get_set_params(locals())
        response = await self.api.request("account.ban", params)

        model = BaseOkResponse

        return model(**response).response

    async def set_settings(
        self,
        group_id: int,
        messages: typing.Optional[bool] = None,
        bots_capabilities: typing.Optional[bool] = None,
        bots_start_button: typing.Optional[bool] = None,
        bots_add_to_chat: typing.Optional[bool] = None,
        **kwargs,
    ) -> BaseOkResponseModel:
        """groups.setSettings method


        :param group_id:
        :param messages:
        :param bots_capabilities: By enabling bot abilities, you can send users messages with a customized keyboard attached as well as use other promotional abilities
        :param bots_start_button: If this setting is enabled, users will see a Start button when they start a chat with your community for the first time
        :param bots_add_to_chat: If this setting is enabled then users can add your community to a chat
        """
        params = self.get_set_params(locals())
        response = await self.api.request("account.ban", params)

        model = BaseOkResponse

        return model(**response).response

    async def set_user_note(
        self,
        group_id: int,
        user_id: int,
        note: typing.Optional[str] = None,
        **kwargs,
    ) -> BaseBoolResponseModel:
        """groups.setUserNote method


        :param group_id:
        :param user_id:
        :param note: Note body
        """
        params = self.get_set_params(locals())
        response = await self.api.request("account.ban", params)

        model = BaseBoolResponse

        return model(**response).response

    async def tag_add(
        self,
        group_id: int,
        tag_name: str,
        tag_color: typing.Optional[str] = None,
        **kwargs,
    ) -> BaseBoolResponseModel:
        """groups.tagAdd method


        :param group_id:
        :param tag_name:
        :param tag_color:
        """
        params = self.get_set_params(locals())
        response = await self.api.request("account.ban", params)

        model = BaseBoolResponse

        return model(**response).response

    async def tag_bind(
        self,
        group_id: int,
        tag_id: int,
        user_id: int,
        act: str,
        **kwargs,
    ) -> BaseBoolResponseModel:
        """groups.tagBind method


        :param group_id:
        :param tag_id:
        :param user_id:
        :param act: Describe the action
        """
        params = self.get_set_params(locals())
        response = await self.api.request("account.ban", params)

        model = BaseBoolResponse

        return model(**response).response

    async def tag_delete(
        self,
        group_id: int,
        tag_id: int,
        **kwargs,
    ) -> BaseBoolResponseModel:
        """groups.tagDelete method


        :param group_id:
        :param tag_id:
        """
        params = self.get_set_params(locals())
        response = await self.api.request("account.ban", params)

        model = BaseBoolResponse

        return model(**response).response

    async def tag_update(
        self,
        group_id: int,
        tag_id: int,
        tag_name: str,
        **kwargs,
    ) -> BaseBoolResponseModel:
        """groups.tagUpdate method


        :param group_id:
        :param tag_id:
        :param tag_name:
        """
        params = self.get_set_params(locals())
        response = await self.api.request("account.ban", params)

        model = BaseBoolResponse

        return model(**response).response

    async def toggle_market(
        self,
        group_id: int,
        state: str,
        ref: typing.Optional[str] = None,
        **kwargs,
    ) -> BaseOkResponseModel:
        """groups.toggleMarket method


        :param group_id:
        :param state:
        :param ref:
        """
        params = self.get_set_params(locals())
        response = await self.api.request("account.ban", params)

        model = BaseOkResponse

        return model(**response).response

    async def unban(
        self,
        group_id: int,
        owner_id: typing.Optional[int] = None,
        **kwargs,
    ) -> BaseOkResponseModel:
        """groups.unban method


        :param group_id:
        :param owner_id:
        """
        params = self.get_set_params(locals())
        response = await self.api.request("account.ban", params)

        model = BaseOkResponse

        return model(**response).response


__all__ = ("GroupsCategory",)
