from vkbottle_types.responses import friends, base



class FriendsCategory(BaseCategory):
    async def add(
        self,
		user_id: Optional[int] = None,
		text: Optional[str] = None,
		follow: Optional[bool] = None,
		**kwargs
    ) -> friends.AddResponseModel:
        """Approves or creates a friend request.
		:param user_id: ID of the user whose friend request will be approved or to whom a friend request will be sent.
		:param text: Text of the message (up to 500 characters) for the friend request, if any.
		:param follow: '1' to pass an incoming request to followers list.
		"""

        params = self.get_set_params(locals())
        response = await self.api.request("friends.add", params)
        model = friends.AddResponse
        return model(**response).response

    async def add_list(
        self, name: str, user_ids: Optional[List[int]] = None, **kwargs
    ) -> friends.AddListResponseModel:
        """Creates a new friend list for the current user.
		:param name: Name of the friend list.
		:param user_ids: IDs of users to be added to the friend list.
		"""

        params = self.get_set_params(locals())
        response = await self.api.request("friends.addList", params)
        model = friends.AddListResponse
        return model(**response).response

    async def are_friends(
        self,
		user_ids: List[int],
		need_sign: Optional[bool] = None,
		extended: Optional[bool] = None,
		**kwargs
    ) -> friends.AreFriendsResponseModel:
        """Checks the current user's friendship status with other specified users.
		:param user_ids: IDs of the users whose friendship status to check.
		:param need_sign: '1' — to return 'sign' field. 'sign' is md5("{id}_{user_id}_{friends_status}_{application_secret}"), where id is current user ID. This field allows to check that data has not been modified by the client. By default: '0'.
		:param extended: Return friend request read_state field
		"""

        params = self.get_set_params(locals())
        response = await self.api.request("friends.areFriends", params)
        model = friends.AreFriendsResponse
        return model(**response).response

    async def delete(
        self, user_id: Optional[int] = None, **kwargs
    ) -> friends.DeleteResponseModel:
        """Declines a friend request or deletes a user from the current user's friend list.
		:param user_id: ID of the user whose friend request is to be declined or who is to be deleted from the current user's friend list.
		"""

        params = self.get_set_params(locals())
        response = await self.api.request("friends.delete", params)
        model = friends.DeleteResponse
        return model(**response).response

    async def delete_all_requests(
        self, **kwargs
    ) -> base.OkResponseModel:
        """Marks all incoming friend requests as viewed."""

        params = self.get_set_params(locals())
        response = await self.api.request("friends.deleteAllRequests", params)
        model = base.OkResponse
        return model(**response).response

    async def delete_list(
        self, list_id: int, **kwargs
    ) -> base.OkResponseModel:
        """Deletes a friend list of the current user.
		:param list_id: ID of the friend list to delete.
		"""

        params = self.get_set_params(locals())
        response = await self.api.request("friends.deleteList", params)
        model = base.OkResponse
        return model(**response).response

    async def edit(
        self, user_id: int, list_ids: Optional[List[int]] = None, **kwargs
    ) -> base.OkResponseModel:
        """Edits the friend lists of the selected user.
		:param user_id: ID of the user whose friend list is to be edited.
		:param list_ids: IDs of the friend lists to which to add the user.
		"""

        params = self.get_set_params(locals())
        response = await self.api.request("friends.edit", params)
        model = base.OkResponse
        return model(**response).response

    async def edit_list(
        self,
		list_id: int,
		name: Optional[str] = None,
		user_ids: Optional[List[int]] = None,
		add_user_ids: Optional[List[int]] = None,
		delete_user_ids: Optional[List[int]] = None,
		**kwargs
    ) -> base.OkResponseModel:
        """Edits a friend list of the current user.
		:param list_id: Friend list ID.
		:param name: Name of the friend list.
		:param user_ids: IDs of users in the friend list.
		:param add_user_ids: (Applies if 'user_ids' parameter is not set.), User IDs to add to the friend list.
		:param delete_user_ids: (Applies if 'user_ids' parameter is not set.), User IDs to delete from the friend list.
		"""

        params = self.get_set_params(locals())
        response = await self.api.request("friends.editList", params)
        model = base.OkResponse
        return model(**response).response

    async def get(
        self,
		user_id: Optional[int] = None,
		order: Optional[str] = None,
		list_id: Optional[int] = None,
		count: Optional[int] = None,
		offset: Optional[int] = None,
		fields: Optional[List[UsersFields]] = None,
		name_case: Optional[str] = None,
		ref: Optional[str] = None,
		**kwargs
    ) -> friends.GetResponseModel:
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
        model = friends.GetResponse
        return model(**response).response

    async def get_app_users(
        self, **kwargs
    ) -> friends.GetAppUsersResponseModel:
        """Returns a list of IDs of the current user's friends who installed the application."""

        params = self.get_set_params(locals())
        response = await self.api.request("friends.getAppUsers", params)
        model = friends.GetAppUsersResponse
        return model(**response).response

    async def get_by_phones(
        self,
		phones: Optional[List[str]] = None,
		fields: Optional[List[UsersFields]] = None,
		**kwargs
    ) -> friends.GetByPhonesResponseModel:
        """Returns a list of the current user's friends whose phone numbers, validated or specified in a profile, are in a given list.
		:param phones: List of phone numbers in MSISDN format (maximum 1000). Example: "+79219876543,+79111234567"
		:param fields: Profile fields to return. Sample values: 'nickname', 'screen_name', 'sex', 'bdate' (birthdate), 'city', 'country', 'timezone', 'photo', 'photo_medium', 'photo_big', 'has_mobile', 'rate', 'contacts', 'education', 'online, counters'.
		"""

        params = self.get_set_params(locals())
        response = await self.api.request("friends.getByPhones", params)
        model = friends.GetByPhonesResponse
        return model(**response).response

    async def get_lists(
        self,
		user_id: Optional[int] = None,
		return_system: Optional[bool] = None,
		**kwargs
    ) -> friends.GetListsResponseModel:
        """Returns a list of the user's friend lists.
		:param user_id: User ID.
		:param return_system: '1' — to return system friend lists. By default: '0'.
		"""

        params = self.get_set_params(locals())
        response = await self.api.request("friends.getLists", params)
        model = friends.GetListsResponse
        return model(**response).response

    async def get_mutual(
        self,
		source_uid: Optional[int] = None,
		target_uid: Optional[int] = None,
		target_uids: Optional[List[int]] = None,
		order: Optional[str] = None,
		count: Optional[int] = None,
		offset: Optional[int] = None,
		**kwargs
    ) -> friends.GetMutualResponseModel:
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
        model = friends.GetMutualResponse
        return model(**response).response

    async def get_online(
        self,
		user_id: Optional[int] = None,
		list_id: Optional[int] = None,
		online_mobile: Optional[bool] = None,
		order: Optional[str] = None,
		count: Optional[int] = None,
		offset: Optional[int] = None,
		**kwargs
    ) -> friends.GetOnlineResponseModel:
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
        model = friends.GetOnlineResponse
        return model(**response).response

    async def get_recent(
        self, count: Optional[int] = None, **kwargs
    ) -> friends.GetRecentResponseModel:
        """Returns a list of user IDs of the current user's recently added friends.
		:param count: Number of recently added friends to return.
		"""

        params = self.get_set_params(locals())
        response = await self.api.request("friends.getRecent", params)
        model = friends.GetRecentResponse
        return model(**response).response

    async def get_requests(
        self,
		offset: Optional[int] = None,
		count: Optional[int] = None,
		extended: Optional[bool] = None,
		need_mutual: Optional[bool] = None,
		out: Optional[bool] = None,
		sort: Optional[int] = None,
		need_viewed: Optional[bool] = None,
		suggested: Optional[bool] = None,
		ref: Optional[str] = None,
		fields: Optional[List[UsersFields]] = None,
		**kwargs
    ) -> friends.GetRequestsResponseModel:
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
        model = friends.GetRequestsResponse
        return model(**response).response

    async def get_suggestions(
        self,
		filter: Optional[List[str]] = None,
		count: Optional[int] = None,
		offset: Optional[int] = None,
		fields: Optional[List[UsersFields]] = None,
		name_case: Optional[str] = None,
		**kwargs
    ) -> friends.GetSuggestionsResponseModel:
        """Returns a list of profiles of users whom the current user may know.
		:param filter: Types of potential friends to return: 'mutual' — users with many mutual friends , 'contacts' — users found with the [vk.com/dev/account.importContacts|account.importContacts] method , 'mutual_contacts' — users who imported the same contacts as the current user with the [vk.com/dev/account.importContacts|account.importContacts] method
		:param count: Number of suggestions to return.
		:param offset: Offset needed to return a specific subset of suggestions.
		:param fields: Profile fields to return. Sample values: 'nickname', 'screen_name', 'sex', 'bdate' (birthdate), 'city', 'country', 'timezone', 'photo', 'photo_medium', 'photo_big', 'has_mobile', 'rate', 'contacts', 'education', 'online', 'counters'.
		:param name_case: Case for declension of user name and surname: , 'nom' — nominative (default) , 'gen' — genitive , 'dat' — dative , 'acc' — accusative , 'ins' — instrumental , 'abl' — prepositional
		"""

        params = self.get_set_params(locals())
        response = await self.api.request("friends.getSuggestions", params)
        model = friends.GetSuggestionsResponse
        return model(**response).response

    async def search(
        self,
		user_id: int,
		q: Optional[str] = None,
		fields: Optional[List[UsersFields]] = None,
		name_case: Optional[str] = None,
		offset: Optional[int] = None,
		count: Optional[int] = None,
		**kwargs
    ) -> friends.SearchResponseModel:
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
        model = friends.SearchResponse
        return model(**response).response