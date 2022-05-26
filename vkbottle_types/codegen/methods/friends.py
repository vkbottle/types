import typing

from typing_extensions import Literal
from vkbottle_types.responses.base import OkResponse
from vkbottle_types.responses.friends import (
    AddListResponse,
    AddListResponseModel,
    AddResponse,
    AreFriendsExtendedResponse,
    AreFriendsResponse,
    DeleteResponse,
    DeleteResponseModel,
    FriendsFriendExtendedStatus,
    FriendsFriendStatus,
    FriendsMutualFriend,
    FriendsUserXtrPhone,
    GetAppUsersResponse,
    GetByPhonesResponse,
    GetFieldsResponse,
    GetFieldsResponseModel,
    GetListsResponse,
    GetListsResponseModel,
    GetMutualResponse,
    GetMutualTargetUidsResponse,
    GetOnlineOnlineMobileResponse,
    GetOnlineOnlineMobileResponseModel,
    GetOnlineResponse,
    GetRecentResponse,
    GetRequestsExtendedResponse,
    GetRequestsExtendedResponseModel,
    GetRequestsNeedMutualResponse,
    GetRequestsNeedMutualResponseModel,
    GetRequestsResponse,
    GetRequestsResponseModel,
    GetResponse,
    GetResponseModel,
    GetSuggestionsResponse,
    GetSuggestionsResponseModel,
    SearchResponse,
    SearchResponseModel,
)

from .base_category import BaseCategory


class FriendsCategory(BaseCategory):
    async def add(
        self,
        user_id: typing.Optional[int] = None,
        text: typing.Optional[str] = None,
        follow: typing.Optional[bool] = None,
        **kwargs
    ) -> int:
        """Approves or creates a friend request.

        :param user_id: ID of the user whose friend request will be approved or to whom a friend request will be sent.
        :param text: Text of the message (up to 500 characters) for the friend request, if any.
        :param follow: '1' to pass an incoming request to followers list.
        """

        params = self.get_set_params(locals())
        response = await self.api.request("friends.add", params)
        model = AddResponse
        return model(**response).response

    async def add_list(
        self, name: str, user_ids: typing.Optional[typing.List[int]] = None, **kwargs
    ) -> AddListResponseModel:
        """Creates a new friend list for the current user.

        :param name: Name of the friend list.
        :param user_ids: IDs of users to be added to the friend list.
        """

        params = self.get_set_params(locals())
        response = await self.api.request("friends.addList", params)
        model = AddListResponse
        return model(**response).response

    @typing.overload
    async def are_friends(
        self,
        user_ids: typing.List[int],
        need_sign: typing.Optional[bool] = None,
        extended: typing.Optional[Literal[False]] = ...,
        **kwargs
    ) -> typing.List[FriendsFriendStatus]:
        ...

    @typing.overload
    async def are_friends(
        self,
        user_ids: typing.List[int],
        need_sign: typing.Optional[bool] = None,
        extended: Literal[True] = ...,
        **kwargs
    ) -> typing.List[FriendsFriendExtendedStatus]:
        ...

    async def are_friends(
        self, user_ids=None, need_sign=None, extended=None, **kwargs
    ) -> typing.Union[
        typing.List[FriendsFriendStatus], typing.List[FriendsFriendExtendedStatus]
    ]:
        """Checks the current user's friendship status with other specified users.

        :param user_ids: IDs of the users whose friendship status to check.
        :param need_sign: '1' — to return 'sign' field. 'sign' is md5("{id}_{user_id}_{friends_status}_{application_secret}"), where id is current user ID. This field allows to check that data has not been modified by the client. By default: '0'.
        :param extended: Return friend request read_state field
        """

        params = self.get_set_params(locals())
        response = await self.api.request("friends.areFriends", params)
        model = self.get_model(
            ((("extended",), AreFriendsExtendedResponse),),
            default=AreFriendsResponse,
            params=params,
        )
        return model(**response).response

    async def delete(
        self, user_id: typing.Optional[int] = None, **kwargs
    ) -> DeleteResponseModel:
        """Declines a friend request or deletes a user from the current user's friend list.

        :param user_id: ID of the user whose friend request is to be declined or who is to be deleted from the current user's friend list.
        """

        params = self.get_set_params(locals())
        response = await self.api.request("friends.delete", params)
        model = DeleteResponse
        return model(**response).response

    async def delete_all_requests(self, **kwargs) -> int:
        """Marks all incoming friend requests as viewed."""

        params = self.get_set_params(locals())
        response = await self.api.request("friends.deleteAllRequests", params)
        model = OkResponse
        return model(**response).response

    async def delete_list(self, list_id: int, **kwargs) -> int:
        """Deletes a friend list of the current user.

        :param list_id: ID of the friend list to delete.
        """

        params = self.get_set_params(locals())
        response = await self.api.request("friends.deleteList", params)
        model = OkResponse
        return model(**response).response

    async def edit(
        self, user_id: int, list_ids: typing.Optional[typing.List[int]] = None, **kwargs
    ) -> int:
        """Edits the friend lists of the selected user.

        :param user_id: ID of the user whose friend list is to be edited.
        :param list_ids: IDs of the friend lists to which to add the user.
        """

        params = self.get_set_params(locals())
        response = await self.api.request("friends.edit", params)
        model = OkResponse
        return model(**response).response

    async def edit_list(
        self,
        list_id: int,
        name: typing.Optional[str] = None,
        user_ids: typing.Optional[typing.List[int]] = None,
        add_user_ids: typing.Optional[typing.List[int]] = None,
        delete_user_ids: typing.Optional[typing.List[int]] = None,
        **kwargs
    ) -> int:
        """Edits a friend list of the current user.

        :param list_id: Friend list ID.
        :param name: Name of the friend list.
        :param user_ids: IDs of users in the friend list.
        :param add_user_ids: (Applies if 'user_ids' parameter is not set.), User IDs to add to the friend list.
        :param delete_user_ids: (Applies if 'user_ids' parameter is not set.), User IDs to delete from the friend list.
        """

        params = self.get_set_params(locals())
        response = await self.api.request("friends.editList", params)
        model = OkResponse
        return model(**response).response

    @typing.overload
    async def get(
        self,
        user_id: typing.Optional[int] = None,
        order: typing.Optional[
            Literal["hints", "random", "mobile", "name", "smart"]
        ] = None,
        list_id: typing.Optional[int] = None,
        count: typing.Optional[int] = None,
        offset: typing.Optional[int] = None,
        fields: typing.Optional[Literal[None]] = ...,
        name_case: typing.Optional[
            Literal["nom", "gen", "dat", "acc", "ins", "abl"]
        ] = None,
        ref: typing.Optional[str] = None,
        **kwargs
    ) -> GetResponseModel:
        ...

    @typing.overload
    async def get(
        self,
        user_id: typing.Optional[int] = None,
        order: typing.Optional[
            Literal["hints", "random", "mobile", "name", "smart"]
        ] = None,
        list_id: typing.Optional[int] = None,
        count: typing.Optional[int] = None,
        offset: typing.Optional[int] = None,
        fields: typing.List[str] = ...,
        name_case: typing.Optional[
            Literal["nom", "gen", "dat", "acc", "ins", "abl"]
        ] = None,
        ref: typing.Optional[str] = None,
        **kwargs
    ) -> GetFieldsResponseModel:
        ...

    async def get(
        self,
        user_id=None,
        order=None,
        list_id=None,
        count=None,
        offset=None,
        fields=None,
        name_case=None,
        ref=None,
        **kwargs
    ) -> typing.Union[GetResponseModel, GetFieldsResponseModel]:
        """Returns a list of user IDs or detailed information about a user's friends.

        :param user_id: User ID. By default, the current user ID.
        :param order: Sort order: , 'name' — by name (enabled only if the 'fields' parameter is used), 'hints' — by rating, similar to how friends are sorted in My friends section, , This parameter is available only for [vk.com/dev/standalone|desktop applications].
        :param list_id: ID of the friend list returned by the [vk.com/dev/friends.getLists|friends.getLists] method to be used as the source. This parameter is taken into account only when the uid parameter is set to the current user ID. This parameter is available only for [vk.com/dev/standalone|desktop applications].
        :param count: Number of friends to return.
        :param offset: Offset needed to return a specific subset of friends.
        :param fields: Profile fields to return. Sample values: 'uid', 'first_name', 'last_name', 'nickname', 'sex', 'bdate' (birthdate), 'city', 'country', 'timezone', 'photo', 'photo_medium', 'photo_big', 'domain', 'has_mobile', 'rate', 'contacts', 'education'.
        :param name_case: Case for declension of user name and surname: , 'nom' — nominative (default) , 'gen' — genitive , 'dat' — dative , 'acc' — accusative , 'ins' — instrumental , 'abl' — prepositional
        :param ref:
        """

        params = self.get_set_params(locals())
        response = await self.api.request("friends.get", params)
        model = self.get_model(
            ((("fields",), GetFieldsResponse),),
            default=GetResponse,
            params=params,
        )
        return model(**response).response

    async def get_app_users(self, **kwargs) -> typing.List[int]:
        """Returns a list of IDs of the current user's friends who installed the application."""

        params = self.get_set_params(locals())
        response = await self.api.request("friends.getAppUsers", params)
        model = GetAppUsersResponse
        return model(**response).response

    async def get_by_phones(
        self,
        phones: typing.Optional[typing.List[str]] = None,
        fields: typing.Optional[typing.List[str]] = None,
        **kwargs
    ) -> typing.List[FriendsUserXtrPhone]:
        """Returns a list of the current user's friends whose phone numbers, validated or specified in a profile, are in a given list.

        :param phones: List of phone numbers in MSISDN format (maximum 1000). Example: "+79219876543,+79111234567"
        :param fields: Profile fields to return. Sample values: 'nickname', 'screen_name', 'sex', 'bdate' (birthdate), 'city', 'country', 'timezone', 'photo', 'photo_medium', 'photo_big', 'has_mobile', 'rate', 'contacts', 'education', 'online, counters'.
        """

        params = self.get_set_params(locals())
        response = await self.api.request("friends.getByPhones", params)
        model = GetByPhonesResponse
        return model(**response).response

    async def get_lists(
        self,
        user_id: typing.Optional[int] = None,
        return_system: typing.Optional[bool] = None,
        **kwargs
    ) -> GetListsResponseModel:
        """Returns a list of the user's friend lists.

        :param user_id: User ID.
        :param return_system: '1' — to return system friend lists. By default: '0'.
        """

        params = self.get_set_params(locals())
        response = await self.api.request("friends.getLists", params)
        model = GetListsResponse
        return model(**response).response

    @typing.overload
    async def get_mutual(
        self,
        source_uid: typing.Optional[int] = None,
        target_uid: typing.Optional[int] = None,
        target_uids: typing.Optional[Literal[None]] = ...,
        order: typing.Optional[str] = None,
        count: typing.Optional[int] = None,
        offset: typing.Optional[int] = None,
        **kwargs
    ) -> typing.List[int]:
        ...

    @typing.overload
    async def get_mutual(
        self,
        source_uid: typing.Optional[int] = None,
        target_uid: typing.Optional[int] = None,
        target_uids: typing.List[int] = ...,
        order: typing.Optional[str] = None,
        count: typing.Optional[int] = None,
        offset: typing.Optional[int] = None,
        **kwargs
    ) -> typing.List[FriendsMutualFriend]:
        ...

    async def get_mutual(
        self,
        source_uid=None,
        target_uid=None,
        target_uids=None,
        order=None,
        count=None,
        offset=None,
        **kwargs
    ) -> typing.Union[typing.List[int], typing.List[FriendsMutualFriend]]:
        """Returns a list of user IDs of the mutual friends of two users.

        :param source_uid: ID of the user whose friends will be checked against the friends of the user specified in 'target_uid'.
        :param target_uid: ID of the user whose friends will be checked against the friends of the user specified in 'source_uid'.
        :param target_uids: IDs of the users whose friends will be checked against the friends of the user specified in 'source_uid'.
        :param order: Sort order: 'random' — random order
        :param count: Number of mutual friends to return.
        :param offset: Offset needed to return a specific subset of mutual friends.
        """

        params = self.get_set_params(locals())
        response = await self.api.request("friends.getMutual", params)
        model = self.get_model(
            ((("target_uids",), GetMutualTargetUidsResponse),),
            default=GetMutualResponse,
            params=params,
        )
        return model(**response).response

    @typing.overload
    async def get_online(
        self,
        user_id: typing.Optional[int] = None,
        list_id: typing.Optional[int] = None,
        online_mobile: typing.Optional[Literal[False]] = ...,
        order: typing.Optional[str] = None,
        count: typing.Optional[int] = None,
        offset: typing.Optional[int] = None,
        **kwargs
    ) -> typing.List[int]:
        ...

    @typing.overload
    async def get_online(
        self,
        user_id: typing.Optional[int] = None,
        list_id: typing.Optional[int] = None,
        online_mobile: Literal[True] = ...,
        order: typing.Optional[str] = None,
        count: typing.Optional[int] = None,
        offset: typing.Optional[int] = None,
        **kwargs
    ) -> GetOnlineOnlineMobileResponseModel:
        ...

    async def get_online(
        self,
        user_id=None,
        list_id=None,
        online_mobile=None,
        order=None,
        count=None,
        offset=None,
        **kwargs
    ) -> typing.Union[typing.List[int], GetOnlineOnlineMobileResponseModel]:
        """Returns a list of user IDs of a user's friends who are online.

        :param user_id: User ID.
        :param list_id: Friend list ID. If this parameter is not set, information about all online friends is returned.
        :param online_mobile: '1' — to return an additional 'online_mobile' field, '0' — (default),
        :param order: Sort order: 'random' — random order
        :param count: Number of friends to return.
        :param offset: Offset needed to return a specific subset of friends.
        """

        params = self.get_set_params(locals())
        response = await self.api.request("friends.getOnline", params)
        model = self.get_model(
            ((("online_mobile",), GetOnlineOnlineMobileResponse),),
            default=GetOnlineResponse,
            params=params,
        )
        return model(**response).response

    async def get_recent(
        self, count: typing.Optional[int] = None, **kwargs
    ) -> typing.List[int]:
        """Returns a list of user IDs of the current user's recently added friends.

        :param count: Number of recently added friends to return.
        """

        params = self.get_set_params(locals())
        response = await self.api.request("friends.getRecent", params)
        model = GetRecentResponse
        return model(**response).response

    @typing.overload
    async def get_requests(
        self,
        offset: typing.Optional[int] = None,
        count: typing.Optional[int] = None,
        extended: typing.Optional[Literal[False]] = ...,
        need_mutual: typing.Optional[Literal[False]] = ...,
        out: typing.Optional[bool] = None,
        sort: typing.Optional[Literal[0, 1, 2]] = None,
        need_viewed: typing.Optional[bool] = None,
        suggested: typing.Optional[bool] = None,
        ref: typing.Optional[str] = None,
        fields: typing.Optional[typing.List[str]] = None,
        **kwargs
    ) -> GetRequestsResponseModel:
        ...

    @typing.overload
    async def get_requests(
        self,
        offset: typing.Optional[int] = None,
        count: typing.Optional[int] = None,
        extended: typing.Optional[Literal[False]] = ...,
        need_mutual: Literal[True] = ...,
        out: typing.Optional[bool] = None,
        sort: typing.Optional[Literal[0, 1, 2]] = None,
        need_viewed: typing.Optional[bool] = None,
        suggested: typing.Optional[bool] = None,
        ref: typing.Optional[str] = None,
        fields: typing.Optional[typing.List[str]] = None,
        **kwargs
    ) -> GetRequestsNeedMutualResponseModel:
        ...

    @typing.overload
    async def get_requests(
        self,
        offset: typing.Optional[int] = None,
        count: typing.Optional[int] = None,
        extended: Literal[True] = ...,
        need_mutual: typing.Optional[Literal[False]] = ...,
        out: typing.Optional[bool] = None,
        sort: typing.Optional[Literal[0, 1, 2]] = None,
        need_viewed: typing.Optional[bool] = None,
        suggested: typing.Optional[bool] = None,
        ref: typing.Optional[str] = None,
        fields: typing.Optional[typing.List[str]] = None,
        **kwargs
    ) -> GetRequestsExtendedResponseModel:
        ...

    async def get_requests(
        self,
        offset=None,
        count=None,
        extended=None,
        need_mutual=None,
        out=None,
        sort=None,
        need_viewed=None,
        suggested=None,
        ref=None,
        fields=None,
        **kwargs
    ) -> typing.Union[
        GetRequestsResponseModel,
        GetRequestsNeedMutualResponseModel,
        GetRequestsExtendedResponseModel,
    ]:
        """Returns information about the current user's incoming and outgoing friend requests.

        :param offset: Offset needed to return a specific subset of friend requests.
        :param count: Number of friend requests to return (default 100, maximum 1000).
        :param extended: '1' — to return response messages from users who have sent a friend request or, if 'suggested' is set to '1', to return a list of suggested friends
        :param need_mutual: '1' — to return a list of mutual friends (up to 20), if any
        :param out: '1' — to return outgoing requests, '0' — to return incoming requests (default)
        :param sort: Sort order: '1' — by number of mutual friends, '0' — by date
        :param need_viewed:
        :param suggested: '1' — to return a list of suggested friends, '0' — to return friend requests (default)
        :param ref:
        :param fields:
        """

        params = self.get_set_params(locals())
        response = await self.api.request("friends.getRequests", params)
        model = self.get_model(
            (
                (("need_mutual",), GetRequestsNeedMutualResponse),
                (("extended",), GetRequestsExtendedResponse),
            ),
            default=GetRequestsResponse,
            params=params,
        )
        return model(**response).response

    async def get_suggestions(
        self,
        filter: typing.Optional[typing.List[str]] = None,
        count: typing.Optional[int] = None,
        offset: typing.Optional[int] = None,
        fields: typing.Optional[typing.List[str]] = None,
        name_case: typing.Optional[
            Literal["nom", "gen", "dat", "acc", "ins", "abl"]
        ] = None,
        **kwargs
    ) -> GetSuggestionsResponseModel:
        """Returns a list of profiles of users whom the current user may know.

        :param filter: Types of potential friends to return: 'mutual' — users with many mutual friends , 'contacts' — users found with the [vk.com/dev/account.importContacts|account.importContacts] method , 'mutual_contacts' — users who imported the same contacts as the current user with the [vk.com/dev/account.importContacts|account.importContacts] method
        :param count: Number of suggestions to return.
        :param offset: Offset needed to return a specific subset of suggestions.
        :param fields: Profile fields to return. Sample values: 'nickname', 'screen_name', 'sex', 'bdate' (birthdate), 'city', 'country', 'timezone', 'photo', 'photo_medium', 'photo_big', 'has_mobile', 'rate', 'contacts', 'education', 'online', 'counters'.
        :param name_case: Case for declension of user name and surname: , 'nom' — nominative (default) , 'gen' — genitive , 'dat' — dative , 'acc' — accusative , 'ins' — instrumental , 'abl' — prepositional
        """

        params = self.get_set_params(locals())
        response = await self.api.request("friends.getSuggestions", params)
        model = GetSuggestionsResponse
        return model(**response).response

    async def search(
        self,
        user_id: typing.Optional[int] = None,
        q: typing.Optional[str] = None,
        fields: typing.Optional[typing.List[str]] = None,
        name_case: typing.Optional[
            Literal["nom", "gen", "dat", "acc", "ins", "abl"]
        ] = None,
        offset: typing.Optional[int] = None,
        count: typing.Optional[int] = None,
        **kwargs
    ) -> SearchResponseModel:
        """Returns a list of friends matching the search criteria.

        :param user_id: User ID.
        :param q: Search query string (e.g., 'Vasya Babich').
        :param fields: Profile fields to return. Sample values: 'nickname', 'screen_name', 'sex', 'bdate' (birthdate), 'city', 'country', 'timezone', 'photo', 'photo_medium', 'photo_big', 'has_mobile', 'rate', 'contacts', 'education', 'online',
        :param name_case: Case for declension of user name and surname: 'nom' — nominative (default), 'gen' — genitive , 'dat' — dative, 'acc' — accusative , 'ins' — instrumental , 'abl' — prepositional
        :param offset: Offset needed to return a specific subset of friends.
        :param count: Number of friends to return.
        """

        params = self.get_set_params(locals())
        response = await self.api.request("friends.search", params)
        model = SearchResponse
        return model(**response).response


__all__ = ("FriendsCategory",)
