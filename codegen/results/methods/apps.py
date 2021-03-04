from vkbottle_types.responses import apps, base



class AppsCategory(BaseCategory):
    async def delete_app_requests(
        self, **kwargs
    ) -> base.OkResponseModel:
        """Deletes all request notifications from the current app."""

        params = self.get_set_params(locals())
        response = await self.api.request("apps.deleteAppRequests", params)
        model = base.OkResponse
        return model(**response).response

    async def get(
        self,
		app_id: Optional[int] = None,
		app_ids: Optional[List[str]] = None,
		platform: Optional[str] = None,
		extended: Optional[bool] = None,
		return_friends: Optional[bool] = None,
		fields: Optional[List[UsersFields]] = None,
		name_case: Optional[str] = None,
		**kwargs
    ) -> apps.GetResponseModel:
        """Returns applications data.
		:param app_id: Application ID
		:param app_ids: List of application ID
		:param platform: platform. Possible values: *'ios' — iOS,, *'android' — Android,, *'winphone' — Windows Phone,, *'web' — приложения на vk.com. By default: 'web'.
		:param extended: 
		:param return_friends: 
		:param fields: Profile fields to return. Sample values: 'nickname', 'screen_name', 'sex', 'bdate' (birthdate), 'city', 'country', 'timezone', 'photo', 'photo_medium', 'photo_big', 'has_mobile', 'contacts', 'education', 'online', 'counters', 'relation', 'last_seen', 'activity', 'can_write_private_message', 'can_see_all_posts', 'can_post', 'universities', (only if return_friends - 1)
		:param name_case: Case for declension of user name and surname: 'nom' — nominative (default),, 'gen' — genitive,, 'dat' — dative,, 'acc' — accusative,, 'ins' — instrumental,, 'abl' — prepositional. (only if 'return_friends' = '1')
		"""

        params = self.get_set_params(locals())
        response = await self.api.request("apps.get", params)
        model = apps.GetResponse
        return model(**response).response

    async def get_catalog(
        self,
		count: int,
		sort: Optional[str] = None,
		offset: Optional[int] = None,
		platform: Optional[str] = None,
		extended: Optional[bool] = None,
		return_friends: Optional[bool] = None,
		fields: Optional[List[UsersFields]] = None,
		name_case: Optional[str] = None,
		q: Optional[str] = None,
		genre_id: Optional[int] = None,
		filter: Optional[str] = None,
		**kwargs
    ) -> apps.GetCatalogResponseModel:
        """Returns a list of applications (apps) available to users in the App Catalog.
		:param count: Number of apps to return.
		:param sort: Sort order: 'popular_today' — popular for one day (default), 'visitors' — by visitors number , 'create_date' — by creation date, 'growth_rate' — by growth rate, 'popular_week' — popular for one week
		:param offset: Offset required to return a specific subset of apps.
		:param platform: 
		:param extended: '1' — to return additional fields 'screenshots', 'MAU', 'catalog_position', and 'international'. If set, 'count' must be less than or equal to '100'. '0' — not to return additional fields (default).
		:param return_friends: 
		:param fields: 
		:param name_case: 
		:param q: Search query string.
		:param genre_id: 
		:param filter: 'installed' — to return list of installed apps (only for mobile platform).
		"""

        params = self.get_set_params(locals())
        response = await self.api.request("apps.getCatalog", params)
        model = apps.GetCatalogResponse
        return model(**response).response

    async def get_friends_list(
        self,
		extended: Optional[bool] = None,
		count: Optional[int] = None,
		offset: Optional[int] = None,
		type: Optional[str] = None,
		fields: Optional[List[UsersFields]] = None,
		**kwargs
    ) -> apps.GetFriendsListResponseModel:
        """Creates friends list for requests and invites in current app.
		:param extended: 
		:param count: List size.
		:param offset: 
		:param type: List type. Possible values: * 'invite' — available for invites (don't play the game),, * 'request' — available for request (play the game). By default: 'invite'.
		:param fields: Additional profile fields, see [vk.com/dev/fields|description].
		"""

        params = self.get_set_params(locals())
        response = await self.api.request("apps.getFriendsList", params)
        model = apps.GetFriendsListResponse
        return model(**response).response

    async def get_leaderboard(
        self,
		type: str,
		global: Optional[bool] = None,
		extended: Optional[bool] = None,
		**kwargs
    ) -> apps.GetLeaderboardResponseModel:
        """Returns players rating in the game.
		:param type: Leaderboard type. Possible values: *'level' — by level,, *'points' — by mission points,, *'score' — by score ().
		:param global: Rating type. Possible values: *'1' — global rating among all players,, *'0' — rating among user friends.
		:param extended: 1 — to return additional info about users
		"""

        params = self.get_set_params(locals())
        response = await self.api.request("apps.getLeaderboard", params)
        model = apps.GetLeaderboardResponse
        return model(**response).response

    async def get_mini_app_policies(
        self, app_id: int, **kwargs
    ) -> apps.GetMiniAppPoliciesResponseModel:
        """Returns policies and terms given to a mini app.
		:param app_id: Mini App ID
		"""

        params = self.get_set_params(locals())
        response = await self.api.request("apps.getMiniAppPolicies", params)
        model = apps.GetMiniAppPoliciesResponse
        return model(**response).response

    async def get_scopes(
        self, type: Optional[str] = None, **kwargs
    ) -> apps.GetScopesResponseModel:
        """Returns scopes for auth
		:param type: 
		"""

        params = self.get_set_params(locals())
        response = await self.api.request("apps.getScopes", params)
        model = apps.GetScopesResponse
        return model(**response).response

    async def get_score(
        self, user_id: int, **kwargs
    ) -> apps.GetScoreResponseModel:
        """Returns user score in app
		:param user_id: 
		"""

        params = self.get_set_params(locals())
        response = await self.api.request("apps.getScore", params)
        model = apps.GetScoreResponse
        return model(**response).response

    async def promo_has_active_gift(
        self, promo_id: int, user_id: Optional[int] = None, **kwargs
    ) -> base.BoolResponseModel:
        """apps.promoHasActiveGift method
		:param promo_id: Id of game promo action
		:param user_id: 
		"""

        params = self.get_set_params(locals())
        response = await self.api.request("apps.promoHasActiveGift", params)
        model = base.BoolResponse
        return model(**response).response

    async def promo_use_gift(
        self, promo_id: int, user_id: Optional[int] = None, **kwargs
    ) -> base.BoolResponseModel:
        """apps.promoUseGift method
		:param promo_id: Id of game promo action
		:param user_id: 
		"""

        params = self.get_set_params(locals())
        response = await self.api.request("apps.promoUseGift", params)
        model = base.BoolResponse
        return model(**response).response

    async def send_request(
        self,
		user_id: int,
		text: Optional[str] = None,
		type: Optional[str] = None,
		name: Optional[str] = None,
		key: Optional[str] = None,
		separate: Optional[bool] = None,
		**kwargs
    ) -> apps.SendRequestResponseModel:
        """Sends a request to another user in an app that uses VK authorization.
		:param user_id: id of the user to send a request
		:param text: request text
		:param type: request type. Values: 'invite' – if the request is sent to a user who does not have the app installed,, 'request' – if a user has already installed the app
		:param name: 
		:param key: special string key to be sent with the request
		:param separate: 
		"""

        params = self.get_set_params(locals())
        response = await self.api.request("apps.sendRequest", params)
        model = apps.SendRequestResponse
        return model(**response).response