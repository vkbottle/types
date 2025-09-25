import typing

from vkbottle_types.methods.base_category import BaseCategory
from vkbottle_types.objects import (
    FriendsFriendExtendedStatus,
    FriendsFriendStatus,
    FriendsMutualFriend,
    FriendsOnlineUsers,
    FriendsOnlineUsersWithMobile,
    UsersFields,
)
from vkbottle_types.responses.base import (
    BaseOkResponse,
    BaseOkResponseModel,
)
from vkbottle_types.responses.friends import *  # noqa: F401,F403  # type: ignore


class FriendsCategory(BaseCategory):
    async def add(
        self,
        follow: typing.Optional[bool] = None,
        text: typing.Optional[str] = None,
        user_id: typing.Optional[int] = None,
        **kwargs: typing.Any,
    ) -> FriendsAddResponseModel:
        """Method `friends.add()`

        :param follow: '1' to pass an incoming request to followers list.
        :param text: Text of the message (up to 500 characters) for the friend request, if any.
        :param user_id: ID of the user whose friend request will be approved or to whom a friend request will be sent.
        """

        params = self.get_set_params(locals())
        response = await self.api.request("friends.add", params)
        model = FriendsAddResponse
        return model(**response).response

    async def add_list(
        self,
        name: str,
        user_ids: typing.Optional[typing.List[int]] = None,
        **kwargs: typing.Any,
    ) -> FriendsAddListResponseModel:
        """Method `friends.addList()`

        :param name: Name of the friend list.
        :param user_ids: IDs of users to be added to the friend list.
        """

        params = self.get_set_params(locals())
        response = await self.api.request("friends.addList", params)
        model = FriendsAddListResponse
        return model(**response).response

    @typing.overload
    async def are_friends(
        self,
        user_ids: typing.List[int],
        extended: typing.Literal[True],
        need_sign: typing.Optional[bool] = None,
        **kwargs: typing.Any,
    ) -> typing.List[FriendsFriendExtendedStatus]: ...

    @typing.overload
    async def are_friends(
        self,
        user_ids: typing.List[int],
        extended: typing.Optional[typing.Literal[False]] = None,
        need_sign: typing.Optional[bool] = None,
        **kwargs: typing.Any,
    ) -> typing.List[FriendsFriendStatus]: ...

    async def are_friends(
        self,
        user_ids: typing.List[int],
        extended: typing.Optional[bool] = None,
        need_sign: typing.Optional[bool] = None,
        **kwargs: typing.Any,
    ) -> typing.Union[typing.List[FriendsFriendExtendedStatus], typing.List[FriendsFriendStatus]]:
        """Method `friends.areFriends()`

        :param user_ids: IDs of the users whose friendship status to check.
        :param extended: Return friend request read_state field
        :param need_sign: '1' - to return 'sign' field. 'sign' is md5("{id}_{user_id}_{friends_status}_{application_secret}"), where id is current user ID. This field allows to check that data has not been modified by the client. By default: '0'.
        """

        params = self.get_set_params(locals())
        response = await self.api.request("friends.areFriends", params)
        model = self.get_model(
            ((("extended",), FriendsAreFriendsExtendedResponse),),
            default=FriendsAreFriendsResponse,
            params=params,
        )
        return model(**response).response

    async def delete(
        self,
        user_id: typing.Optional[int] = None,
        **kwargs: typing.Any,
    ) -> FriendsDeleteResponseModel:
        """Method `friends.delete()`

        :param user_id: ID of the user whose friend request is to be declined or who is to be deleted from the current user's friend list.
        """

        params = self.get_set_params(locals())
        response = await self.api.request("friends.delete", params)
        model = FriendsDeleteResponse
        return model(**response).response

    async def delete_all_requests(
        self,
        **kwargs: typing.Any,
    ) -> BaseOkResponseModel:
        """Method `friends.deleteAllRequests()`"""

        params = self.get_set_params(locals())
        response = await self.api.request("friends.deleteAllRequests", params)
        model = BaseOkResponse
        return model(**response).response

    async def delete_list(
        self,
        list_id: int,
        **kwargs: typing.Any,
    ) -> BaseOkResponseModel:
        """Method `friends.deleteList()`

        :param list_id: ID of the friend list to delete.
        """

        params = self.get_set_params(locals())
        response = await self.api.request("friends.deleteList", params)
        model = BaseOkResponse
        return model(**response).response

    async def edit(
        self,
        user_id: int,
        list_ids: typing.Optional[typing.List[int]] = None,
        **kwargs: typing.Any,
    ) -> BaseOkResponseModel:
        """Method `friends.edit()`

        :param user_id: ID of the user whose friend list is to be edited.
        :param list_ids: IDs of the friend lists to which to add the user.
        """

        params = self.get_set_params(locals())
        response = await self.api.request("friends.edit", params)
        model = BaseOkResponse
        return model(**response).response

    async def edit_list(
        self,
        list_id: int,
        add_user_ids: typing.Optional[typing.List[int]] = None,
        delete_user_ids: typing.Optional[typing.List[int]] = None,
        name: typing.Optional[str] = None,
        user_ids: typing.Optional[typing.List[int]] = None,
        **kwargs: typing.Any,
    ) -> BaseOkResponseModel:
        """Method `friends.editList()`

        :param list_id: Friend list ID.
        :param add_user_ids: (Applies if 'user_ids' parameter is not set.), User IDs to add to the friend list.
        :param delete_user_ids: (Applies if 'user_ids' parameter is not set.), User IDs to delete from the friend list.
        :param name: Name of the friend list.
        :param user_ids: IDs of users in the friend list.
        """

        params = self.get_set_params(locals())
        response = await self.api.request("friends.editList", params)
        model = BaseOkResponse
        return model(**response).response

    @typing.overload
    async def get(
        self,
        fields: typing.List[UsersFields],
        count: typing.Optional[int] = None,
        list_id: typing.Optional[int] = None,
        offset: typing.Optional[int] = None,
        order: typing.Optional[str] = None,
        ref: typing.Optional[str] = None,
        user_id: typing.Optional[int] = None,
        **kwargs: typing.Any,
    ) -> FriendsGetFieldsResponseModel: ...

    @typing.overload
    async def get(
        self,
        fields: typing.Optional[typing.List[UsersFields]] = None,
        count: typing.Optional[int] = None,
        list_id: typing.Optional[int] = None,
        offset: typing.Optional[int] = None,
        order: typing.Optional[str] = None,
        ref: typing.Optional[str] = None,
        user_id: typing.Optional[int] = None,
        **kwargs: typing.Any,
    ) -> FriendsGetResponseModel: ...

    async def get(
        self,
        fields: typing.Optional[typing.List[UsersFields]] = None,
        count: typing.Optional[int] = None,
        list_id: typing.Optional[int] = None,
        offset: typing.Optional[int] = None,
        order: typing.Optional[str] = None,
        ref: typing.Optional[str] = None,
        user_id: typing.Optional[int] = None,
        **kwargs: typing.Any,
    ) -> typing.Union[FriendsGetFieldsResponseModel, FriendsGetResponseModel]:
        """Method `friends.get()`

        :param fields: Profile fields to return. Sample values: 'uid', 'first_name', 'last_name', 'nickname', 'sex', 'bdate' (birthdate), 'city', 'country', 'timezone', 'photo', 'photo_medium', 'photo_big', 'domain', 'has_mobile', 'rate', 'contacts', 'education'.
        :param count: Number of friends to return.
        :param list_id: ID of the friend list returned by the [vk.ru/dev/friends.getLists|friends.getLists] method to be used as the source. This parameter is taken into account only when the uid parameter is set to the current user ID. This parameter is available only for [vk.ru/dev/standalone|desktop applications].
        :param offset: Offset needed to return a specific subset of friends.
        :param order: Sort order: , 'name' - by name (enabled only if the 'fields' parameter is used), 'hints' - by rating, similar to how friends are sorted in My friends section, , This parameter is available only for [vk.ru/dev/standalone|desktop applications].
        :param ref:
        :param user_id: User ID. By default, the current user ID.
        """

        params = self.get_set_params(locals())
        response = await self.api.request("friends.get", params)
        model = self.get_model(
            ((("fields",), FriendsGetFieldsResponse),),
            default=FriendsGetResponse,
            params=params,
        )
        return model(**response).response

    async def get_app_users(
        self,
        **kwargs: typing.Any,
    ) -> typing.List[int]:
        """Method `friends.getAppUsers()`"""

        params = self.get_set_params(locals())
        response = await self.api.request("friends.getAppUsers", params)
        model = FriendsGetAppUsersResponse
        return model(**response).response

    async def get_lists(
        self,
        return_system: typing.Optional[bool] = None,
        user_id: typing.Optional[int] = None,
        **kwargs: typing.Any,
    ) -> FriendsGetListsResponseModel:
        """Method `friends.getLists()`

        :param return_system: '1' - to return system friend lists. By default: '0'.
        :param user_id: User ID.
        """

        params = self.get_set_params(locals())
        response = await self.api.request("friends.getLists", params)
        model = FriendsGetListsResponse
        return model(**response).response

    @typing.overload
    async def get_mutual(
        self,
        target_uids: typing.List[int],
        count: typing.Optional[int] = None,
        need_common_count: typing.Optional[bool] = None,
        offset: typing.Optional[int] = None,
        order: typing.Optional[str] = None,
        source_uid: typing.Optional[int] = None,
        target_uid: typing.Optional[int] = None,
        **kwargs: typing.Any,
    ) -> typing.List[FriendsMutualFriend]: ...

    @typing.overload
    async def get_mutual(
        self,
        target_uids: typing.Optional[typing.List[int]] = None,
        count: typing.Optional[int] = None,
        need_common_count: typing.Optional[bool] = None,
        offset: typing.Optional[int] = None,
        order: typing.Optional[str] = None,
        source_uid: typing.Optional[int] = None,
        target_uid: typing.Optional[int] = None,
        **kwargs: typing.Any,
    ) -> "FriendsMutualFriend": ...

    @typing.overload
    async def get_mutual(
        self,
        target_uids: typing.List[int],
        count: typing.Optional[int] = None,
        need_common_count: typing.Optional[bool] = None,
        offset: typing.Optional[int] = None,
        order: typing.Optional[str] = None,
        source_uid: typing.Optional[int] = None,
        target_uid: typing.Optional[int] = None,
        **kwargs: typing.Any,
    ) -> typing.List[int]: ...

    async def get_mutual(
        self,
        target_uids: typing.Optional[typing.List[int]] = None,
        count: typing.Optional[int] = None,
        need_common_count: typing.Optional[bool] = None,
        offset: typing.Optional[int] = None,
        order: typing.Optional[str] = None,
        source_uid: typing.Optional[int] = None,
        target_uid: typing.Optional[int] = None,
        **kwargs: typing.Any,
    ) -> typing.Union[typing.List[FriendsMutualFriend], typing.List[int], "FriendsMutualFriend"]:
        """Method `friends.getMutual()`

        :param target_uids: IDs of the users whose friends will be checked against the friends of the user specified in 'source_uid'.
        :param count: Number of mutual friends to return.
        :param need_common_count: Return mutual friends total count
        :param offset: Offset needed to return a specific subset of mutual friends.
        :param order: Sort order: 'random' - random order
        :param source_uid: ID of the user whose friends will be checked against the friends of the user specified in 'target_uid'.
        :param target_uid: ID of the user whose friends will be checked against the friends of the user specified in 'source_uid'.
        """

        params = self.get_set_params(locals())
        response = await self.api.request("friends.getMutual", params)
        model = self.get_model(
            (
                (("target_uids",), FriendsGetMutualTargetUidsResponse),
                (("total_count",), FriendsGetMutualTotalCountResponse),
            ),
            default=FriendsGetMutualResponse,
            params=params,
        )
        return model(**response).response

    @typing.overload
    async def get_online(
        self,
        online_mobile: typing.Literal[True],
        count: typing.Optional[int] = None,
        list_id: typing.Optional[int] = None,
        offset: typing.Optional[int] = None,
        order: typing.Optional[str] = None,
        user_id: typing.Optional[int] = None,
        **kwargs: typing.Any,
    ) -> FriendsGetOnlineOnlineMobileResponseModel: ...

    @typing.overload
    async def get_online(
        self,
        online_mobile: typing.Optional[bool] = None,
        count: typing.Optional[int] = None,
        list_id: typing.Optional[int] = None,
        offset: typing.Optional[int] = None,
        order: typing.Optional[str] = None,
        user_id: typing.Optional[int] = None,
        **kwargs: typing.Any,
    ) -> "FriendsOnlineUsers": ...

    @typing.overload
    async def get_online(
        self,
        count: typing.Optional[int] = None,
        list_id: typing.Optional[int] = None,
        offset: typing.Optional[int] = None,
        online_mobile: typing.Optional[bool] = None,
        order: typing.Optional[str] = None,
        user_id: typing.Optional[int] = None,
        **kwargs: typing.Any,
    ) -> "FriendsOnlineUsersWithMobile": ...

    @typing.overload
    async def get_online(
        self,
        count: typing.Optional[int] = None,
        list_id: typing.Optional[int] = None,
        offset: typing.Optional[int] = None,
        online_mobile: typing.Optional[bool] = None,
        order: typing.Optional[str] = None,
        user_id: typing.Optional[int] = None,
        **kwargs: typing.Any,
    ) -> typing.List[int]: ...

    async def get_online(
        self,
        online_mobile: typing.Optional[bool] = None,
        count: typing.Optional[int] = None,
        list_id: typing.Optional[int] = None,
        offset: typing.Optional[int] = None,
        order: typing.Optional[str] = None,
        user_id: typing.Optional[int] = None,
        **kwargs: typing.Any,
    ) -> typing.Union[FriendsGetOnlineOnlineMobileResponseModel, typing.List[int], "FriendsOnlineUsersWithMobile", "FriendsOnlineUsers"]:
        """Method `friends.getOnline()`

        :param online_mobile: '1' - to return an additional 'online_mobile' field, '0' - (default),
        :param count: Number of friends to return.
        :param list_id: Friend list ID. If this parameter is not set, information about all online friends is returned.
        :param offset: Offset needed to return a specific subset of friends.
        :param order: Sort order: 'random' - random order
        :param user_id: User ID.
        """

        params = self.get_set_params(locals())
        response = await self.api.request("friends.getOnline", params)
        model = self.get_model(
            (
                (("online_mobile",), FriendsGetOnlineOnlineMobileResponse),
                (("extended",), FriendsGetOnlineExtendedResponse),
                (("online_mobile_extended",), FriendsGetOnlineOnlineMobileExtendedResponse),
            ),
            default=FriendsGetOnlineResponse,
            params=params,
        )
        return model(**response).response

    async def get_recent(
        self,
        count: typing.Optional[int] = None,
        **kwargs: typing.Any,
    ) -> typing.List[int]:
        """Method `friends.getRecent()`

        :param count: Number of recently added friends to return.
        """

        params = self.get_set_params(locals())
        response = await self.api.request("friends.getRecent", params)
        model = FriendsGetRecentResponse
        return model(**response).response

    @typing.overload
    async def get_requests(
        self,
        extended: typing.Literal[True],
        need_mutual: typing.Literal[True],
        count: typing.Optional[int] = None,
        fields: typing.Optional[typing.List[UsersFields]] = None,
        need_viewed: typing.Optional[bool] = None,
        offset: typing.Optional[int] = None,
        out: typing.Optional[bool] = None,
        ref: typing.Optional[str] = None,
        sort: typing.Optional[int] = None,
        suggested: typing.Optional[bool] = None,
        **kwargs: typing.Any,
    ) -> FriendsGetRequestsNeedMutualResponseModel: ...

    @typing.overload
    async def get_requests(
        self,
        extended: typing.Optional[bool] = None,
        need_mutual: typing.Optional[bool] = None,
        count: typing.Optional[int] = None,
        fields: typing.Optional[typing.List[UsersFields]] = None,
        need_viewed: typing.Optional[bool] = None,
        offset: typing.Optional[int] = None,
        out: typing.Optional[bool] = None,
        ref: typing.Optional[str] = None,
        sort: typing.Optional[int] = None,
        suggested: typing.Optional[bool] = None,
        **kwargs: typing.Any,
    ) -> FriendsGetRequestsExtendedResponseModel: ...

    @typing.overload
    async def get_requests(
        self,
        count: typing.Optional[int] = None,
        extended: typing.Optional[bool] = None,
        fields: typing.Optional[typing.List[UsersFields]] = None,
        need_mutual: typing.Optional[bool] = None,
        need_viewed: typing.Optional[bool] = None,
        offset: typing.Optional[int] = None,
        out: typing.Optional[bool] = None,
        ref: typing.Optional[str] = None,
        sort: typing.Optional[int] = None,
        suggested: typing.Optional[bool] = None,
        **kwargs: typing.Any,
    ) -> FriendsGetRequestsResponseModel: ...

    async def get_requests(
        self,
        extended: typing.Optional[bool] = None,
        need_mutual: typing.Optional[bool] = None,
        count: typing.Optional[int] = None,
        fields: typing.Optional[typing.List[UsersFields]] = None,
        need_viewed: typing.Optional[bool] = None,
        offset: typing.Optional[int] = None,
        out: typing.Optional[bool] = None,
        ref: typing.Optional[str] = None,
        sort: typing.Optional[int] = None,
        suggested: typing.Optional[bool] = None,
        **kwargs: typing.Any,
    ) -> typing.Union[FriendsGetRequestsResponseModel, FriendsGetRequestsExtendedResponseModel, FriendsGetRequestsNeedMutualResponseModel]:
        """Method `friends.getRequests()`

        :param extended: '1' - to return response messages from users who have sent a friend request or, if 'suggested' is set to '1', to return a list of suggested friends
        :param need_mutual: '1' - to return a list of mutual friends (up to 20), if any
        :param count: Number of friend requests to return (default 100, maximum 1000).
        :param fields:
        :param need_viewed:
        :param offset: Offset needed to return a specific subset of friend requests.
        :param out: '1' - to return outgoing requests, '0' - to return incoming requests (default)
        :param ref:
        :param sort: Sort order: '1' - by number of mutual friends, '0' - by date
        :param suggested: '1' - to return a list of suggested friends, '0' - to return friend requests (default)
        """

        params = self.get_set_params(locals())
        response = await self.api.request("friends.getRequests", params)
        model = self.get_model(
            (
                (("extended",), FriendsGetRequestsNeedMutualResponse),
                (("need_mutual",), FriendsGetRequestsNeedMutualResponse),
            ),
            default=FriendsGetRequestsResponse,
            params=params,
        )
        return model(**response).response

    async def get_suggestions(
        self,
        count: typing.Optional[int] = None,
        fields: typing.Optional[typing.List[UsersFields]] = None,
        filter: typing.Optional[typing.List[typing.Literal["contacts", "mutual", "mutual_contacts"]]] = None,
        name_case: typing.Optional[str] = None,
        offset: typing.Optional[int] = None,
        **kwargs: typing.Any,
    ) -> FriendsGetSuggestionsResponseModel:
        """Method `friends.getSuggestions()`

        :param count: Number of suggestions to return.
        :param fields: Profile fields to return. Sample values: 'nickname', 'screen_name', 'sex', 'bdate' (birthdate), 'city', 'country', 'timezone', 'photo', 'photo_medium', 'photo_big', 'has_mobile', 'rate', 'contacts', 'education', 'online', 'counters'.
        :param filter: Types of potential friends to return: 'mutual' - users with many mutual friends , 'contacts' - users found with the [vk.ru/dev/account.importContacts|account.importContacts] method , 'mutual_contacts' - users who imported the same contacts as the current user with the [vk.ru/dev/account.importContacts|account.importContacts] method
        :param name_case: Case for declension of user name and surname: , 'nom' - nominative (default) , 'gen' - genitive , 'dat' - dative , 'acc' - accusative , 'ins' - instrumental , 'abl' - prepositional
        :param offset: Offset needed to return a specific subset of suggestions.
        """

        params = self.get_set_params(locals())
        response = await self.api.request("friends.getSuggestions", params)
        model = FriendsGetSuggestionsResponse
        return model(**response).response

    async def search(
        self,
        count: typing.Optional[int] = None,
        fields: typing.Optional[typing.List[UsersFields]] = None,
        name_case: typing.Optional[str] = None,
        offset: typing.Optional[int] = None,
        q: typing.Optional[str] = None,
        user_id: typing.Optional[int] = None,
        **kwargs: typing.Any,
    ) -> FriendsSearchResponseModel:
        """Method `friends.search()`

        :param count: Number of friends to return.
        :param fields: Profile fields to return. Sample values: 'nickname', 'screen_name', 'sex', 'bdate' (birthdate), 'city', 'country', 'timezone', 'photo', 'photo_medium', 'photo_big', 'has_mobile', 'rate', 'contacts', 'education', 'online',
        :param name_case: Case for declension of user name and surname: 'nom' - nominative (default), 'gen' - genitive , 'dat' - dative, 'acc' - accusative , 'ins' - instrumental , 'abl' - prepositional
        :param offset: Offset needed to return a specific subset of friends.
        :param q: Search query string (e.g., 'Vasya Babich').
        :param user_id: User ID.
        """

        params = self.get_set_params(locals())
        response = await self.api.request("friends.search", params)
        model = FriendsSearchResponse
        return model(**response).response


__all__ = ("FriendsCategory",)
