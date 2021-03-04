from vkbottle_types.responses import newsfeed, base



class NewsfeedCategory(BaseCategory):
    async def add_ban(
        self,
		user_ids: Optional[List[int]] = None,
		group_ids: Optional[List[int]] = None,
		**kwargs
    ) -> base.OkResponseModel:
        """Prevents news from specified users and communities from appearing in the current user's newsfeed.
		:param user_ids: 
		:param group_ids: 
		"""

        params = self.get_set_params(locals())
        response = await self.api.request("newsfeed.addBan", params)
        model = base.OkResponse
        return model(**response).response

    async def delete_ban(
        self,
		user_ids: Optional[List[int]] = None,
		group_ids: Optional[List[int]] = None,
		**kwargs
    ) -> base.OkResponseModel:
        """Allows news from previously banned users and communities to be shown in the current user's newsfeed.
		:param user_ids: 
		:param group_ids: 
		"""

        params = self.get_set_params(locals())
        response = await self.api.request("newsfeed.deleteBan", params)
        model = base.OkResponse
        return model(**response).response

    async def delete_list(
        self, list_id: int, **kwargs
    ) -> base.OkResponseModel:
        """newsfeed.deleteList method
		:param list_id: 
		"""

        params = self.get_set_params(locals())
        response = await self.api.request("newsfeed.deleteList", params)
        model = base.OkResponse
        return model(**response).response

    async def get(
        self,
		filters: Optional[List[NewsfeedFilters]] = None,
		return_banned: Optional[bool] = None,
		start_time: Optional[int] = None,
		end_time: Optional[int] = None,
		max_photos: Optional[int] = None,
		source_ids: Optional[str] = None,
		start_from: Optional[str] = None,
		count: Optional[int] = None,
		fields: Optional[List[BaseUserGroupFields]] = None,
		section: Optional[str] = None,
		**kwargs
    ) -> newsfeed.GetResponseModel:
        """Returns data required to show newsfeed for the current user.
		:param filters: Filters to apply: 'post' — new wall posts, 'photo' — new photos, 'photo_tag' — new photo tags, 'wall_photo' — new wall photos, 'friend' — new friends
		:param return_banned: '1' — to return news items from banned sources
		:param start_time: Earliest timestamp (in Unix time) of a news item to return. By default, 24 hours ago.
		:param end_time: Latest timestamp (in Unix time) of a news item to return. By default, the current time.
		:param max_photos: Maximum number of photos to return. By default, '5'.
		:param source_ids: Sources to obtain news from, separated by commas. User IDs can be specified in formats '' or 'u' , where '' is the user's friend ID. Community IDs can be specified in formats '-' or 'g' , where '' is the community ID. If the parameter is not set, all of the user's friends and communities are returned, except for banned sources, which can be obtained with the [vk.com/dev/newsfeed.getBanned|newsfeed.getBanned] method.
		:param start_from: identifier required to get the next page of results. Value for this parameter is returned in 'next_from' field in a reply.
		:param count: Number of news items to return (default 50, maximum 100). For auto feed, you can use the 'new_offset' parameter returned by this method.
		:param fields: Additional fields of [vk.com/dev/fields|profiles] and [vk.com/dev/fields_groups|communities] to return.
		:param section: 
		"""

        params = self.get_set_params(locals())
        response = await self.api.request("newsfeed.get", params)
        model = newsfeed.GetResponse
        return model(**response).response

    async def get_banned(
        self,
		extended: Optional[bool] = None,
		fields: Optional[List[UsersFields]] = None,
		name_case: Optional[str] = None,
		**kwargs
    ) -> newsfeed.GetBannedResponseModel:
        """Returns a list of users and communities banned from the current user's newsfeed.
		:param extended: '1' — return extra information about users and communities
		:param fields: Profile fields to return.
		:param name_case: Case for declension of user name and surname: 'nom' — nominative (default), 'gen' — genitive , 'dat' — dative, 'acc' — accusative , 'ins' — instrumental , 'abl' — prepositional
		"""

        params = self.get_set_params(locals())
        response = await self.api.request("newsfeed.getBanned", params)
        model = newsfeed.GetBannedResponse
        return model(**response).response

    async def get_comments(
        self,
		count: Optional[int] = None,
		filters: Optional[List[NewsfeedCommentsFilters]] = None,
		reposts: Optional[str] = None,
		start_time: Optional[int] = None,
		end_time: Optional[int] = None,
		last_comments_count: Optional[int] = None,
		start_from: Optional[str] = None,
		fields: Optional[List[BaseUserGroupFields]] = None,
		**kwargs
    ) -> newsfeed.GetCommentsResponseModel:
        """Returns a list of comments in the current user's newsfeed.
		:param count: Number of comments to return. For auto feed, you can use the 'new_offset' parameter returned by this method.
		:param filters: Filters to apply: 'post' — new comments on wall posts, 'photo' — new comments on photos, 'video' — new comments on videos, 'topic' — new comments on discussions, 'note' — new comments on notes,
		:param reposts: Object ID, comments on repost of which shall be returned, e.g. 'wall1_45486'. (If the parameter is set, the 'filters' parameter is optional.),
		:param start_time: Earliest timestamp (in Unix time) of a comment to return. By default, 24 hours ago.
		:param end_time: Latest timestamp (in Unix time) of a comment to return. By default, the current time.
		:param last_comments_count: 
		:param start_from: Identificator needed to return the next page with results. Value for this parameter returns in 'next_from' field.
		:param fields: Additional fields of [vk.com/dev/fields|profiles] and [vk.com/dev/fields_groups|communities] to return.
		"""

        params = self.get_set_params(locals())
        response = await self.api.request("newsfeed.getComments", params)
        model = newsfeed.GetCommentsResponse
        return model(**response).response

    async def get_lists(
        self,
		list_ids: Optional[List[int]] = None,
		extended: Optional[bool] = None,
		**kwargs
    ) -> newsfeed.GetListsResponseModel:
        """Returns a list of newsfeeds followed by the current user.
		:param list_ids: numeric list identifiers.
		:param extended: Return additional list info
		"""

        params = self.get_set_params(locals())
        response = await self.api.request("newsfeed.getLists", params)
        model = newsfeed.GetListsResponse
        return model(**response).response

    async def get_mentions(
        self,
		owner_id: Optional[int] = None,
		start_time: Optional[int] = None,
		end_time: Optional[int] = None,
		offset: Optional[int] = None,
		count: Optional[int] = None,
		**kwargs
    ) -> newsfeed.GetMentionsResponseModel:
        """Returns a list of posts on user walls in which the current user is mentioned.
		:param owner_id: Owner ID.
		:param start_time: Earliest timestamp (in Unix time) of a post to return. By default, 24 hours ago.
		:param end_time: Latest timestamp (in Unix time) of a post to return. By default, the current time.
		:param offset: Offset needed to return a specific subset of posts.
		:param count: Number of posts to return.
		"""

        params = self.get_set_params(locals())
        response = await self.api.request("newsfeed.getMentions", params)
        model = newsfeed.GetMentionsResponse
        return model(**response).response

    async def get_recommended(
        self,
		start_time: Optional[int] = None,
		end_time: Optional[int] = None,
		max_photos: Optional[int] = None,
		start_from: Optional[str] = None,
		count: Optional[int] = None,
		fields: Optional[List[BaseUserGroupFields]] = None,
		**kwargs
    ) -> newsfeed.GetRecommendedResponseModel:
        """, Returns a list of newsfeeds recommended to the current user.
		:param start_time: Earliest timestamp (in Unix time) of a news item to return. By default, 24 hours ago.
		:param end_time: Latest timestamp (in Unix time) of a news item to return. By default, the current time.
		:param max_photos: Maximum number of photos to return. By default, '5'.
		:param start_from: 'new_from' value obtained in previous call.
		:param count: Number of news items to return.
		:param fields: Additional fields of [vk.com/dev/fields|profiles] and [vk.com/dev/fields_groups|communities] to return.
		"""

        params = self.get_set_params(locals())
        response = await self.api.request("newsfeed.getRecommended", params)
        model = newsfeed.GetRecommendedResponse
        return model(**response).response

    async def get_suggested_sources(
        self,
		offset: Optional[int] = None,
		count: Optional[int] = None,
		shuffle: Optional[bool] = None,
		fields: Optional[List[BaseUserGroupFields]] = None,
		**kwargs
    ) -> newsfeed.GetSuggestedSourcesResponseModel:
        """Returns communities and users that current user is suggested to follow.
		:param offset: offset required to choose a particular subset of communities or users.
		:param count: amount of communities or users to return.
		:param shuffle: shuffle the returned list or not.
		:param fields: list of extra fields to be returned. See available fields for [vk.com/dev/fields|users] and [vk.com/dev/fields_groups|communities].
		"""

        params = self.get_set_params(locals())
        response = await self.api.request("newsfeed.getSuggestedSources", params)
        model = newsfeed.GetSuggestedSourcesResponse
        return model(**response).response

    async def ignore_item(
        self,
		type: str,
		owner_id: Optional[int] = None,
		item_id: Optional[int] = None,
		**kwargs
    ) -> base.OkResponseModel:
        """Hides an item from the newsfeed.
		:param type: Item type. Possible values: *'wall' – post on the wall,, *'tag' – tag on a photo,, *'profilephoto' – profile photo,, *'video' – video,, *'audio' – audio.
		:param owner_id: Item owner's identifier (user or community), "Note that community id must be negative. 'owner_id=1' – user , 'owner_id=-1' – community "
		:param item_id: Item identifier
		"""

        params = self.get_set_params(locals())
        response = await self.api.request("newsfeed.ignoreItem", params)
        model = base.OkResponse
        return model(**response).response

    async def save_list(
        self,
		title: str,
		list_id: Optional[int] = None,
		source_ids: Optional[List[int]] = None,
		no_reposts: Optional[bool] = None,
		**kwargs
    ) -> newsfeed.SaveListResponseModel:
        """Creates and edits user newsfeed lists
		:param title: list name.
		:param list_id: numeric list identifier (if not sent, will be set automatically).
		:param source_ids: users and communities identifiers to be added to the list. Community identifiers must be negative numbers.
		:param no_reposts: reposts display on and off ('1' is for off).
		"""

        params = self.get_set_params(locals())
        response = await self.api.request("newsfeed.saveList", params)
        model = newsfeed.SaveListResponse
        return model(**response).response

    async def search(
        self,
		q: Optional[str] = None,
		extended: Optional[bool] = None,
		count: Optional[int] = None,
		latitude: Optional[number] = None,
		longitude: Optional[number] = None,
		start_time: Optional[int] = None,
		end_time: Optional[int] = None,
		start_from: Optional[str] = None,
		fields: Optional[List[BaseUserGroupFields]] = None,
		**kwargs
    ) -> newsfeed.SearchResponseModel:
        """Returns search results by statuses.
		:param q: Search query string (e.g., 'New Year').
		:param extended: '1' — to return additional information about the user or community that placed the post.
		:param count: Number of posts to return.
		:param latitude: Geographical latitude point (in degrees, -90 to 90) within which to search.
		:param longitude: Geographical longitude point (in degrees, -180 to 180) within which to search.
		:param start_time: Earliest timestamp (in Unix time) of a news item to return. By default, 24 hours ago.
		:param end_time: Latest timestamp (in Unix time) of a news item to return. By default, the current time.
		:param start_from: 
		:param fields: Additional fields of [vk.com/dev/fields|profiles] and [vk.com/dev/fields_groups|communities] to return.
		"""

        params = self.get_set_params(locals())
        response = await self.api.request("newsfeed.search", params)
        model = newsfeed.SearchResponse
        return model(**response).response

    async def unignore_item(
        self,
		type: str,
		owner_id: int,
		item_id: int,
		track_code: Optional[str] = None,
		**kwargs
    ) -> base.OkResponseModel:
        """Returns a hidden item to the newsfeed.
		:param type: Item type. Possible values: *'wall' – post on the wall,, *'tag' – tag on a photo,, *'profilephoto' – profile photo,, *'video' – video,, *'audio' – audio.
		:param owner_id: Item owner's identifier (user or community), "Note that community id must be negative. 'owner_id=1' – user , 'owner_id=-1' – community "
		:param item_id: Item identifier
		:param track_code: Track code of unignored item
		"""

        params = self.get_set_params(locals())
        response = await self.api.request("newsfeed.unignoreItem", params)
        model = base.OkResponse
        return model(**response).response

    async def unsubscribe(
        self, type: str, item_id: int, owner_id: Optional[int] = None, **kwargs
    ) -> base.OkResponseModel:
        """Unsubscribes the current user from specified newsfeeds.
		:param type: Type of object from which to unsubscribe: 'note' — note, 'photo' — photo, 'post' — post on user wall or community wall, 'topic' — topic, 'video' — video
		:param item_id: Object ID.
		:param owner_id: Object owner ID.
		"""

        params = self.get_set_params(locals())
        response = await self.api.request("newsfeed.unsubscribe", params)
        model = base.OkResponse
        return model(**response).response