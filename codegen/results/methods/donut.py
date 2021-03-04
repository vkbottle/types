from vkbottle_types.responses import donut, base



class DonutCategory(BaseCategory):
    async def get_friends(
        self,
		owner_id: int,
		offset: Optional[int] = None,
		count: Optional[int] = None,
		fields: Optional[List[str]] = None,
		**kwargs
    ) -> donut.GetFriendsResponseModel:
        """donut.getFriends method
		:param owner_id: 
		:param offset: 
		:param count: 
		:param fields: 
		"""

        params = self.get_set_params(locals())
        response = await self.api.request("donut.getFriends", params)
        model = donut.GetFriendsResponse
        return model(**response).response

    async def get_subscription(
        self, owner_id: int, **kwargs
    ) -> donut.GetSubscriptionResponseModel:
        """donut.getSubscription method
		:param owner_id: 
		"""

        params = self.get_set_params(locals())
        response = await self.api.request("donut.getSubscription", params)
        model = donut.GetSubscriptionResponse
        return model(**response).response

    async def get_subscriptions(
        self,
		fields: Optional[List[BaseUserGroupFields]] = None,
		offset: Optional[int] = None,
		count: Optional[int] = None,
		**kwargs
    ) -> donut.GetSubscriptionsResponseModel:
        """Returns a list of user's VK Donut subscriptions.
		:param fields: 
		:param offset: 
		:param count: 
		"""

        params = self.get_set_params(locals())
        response = await self.api.request("donut.getSubscriptions", params)
        model = donut.GetSubscriptionsResponse
        return model(**response).response

    async def is_don(
        self, owner_id: int, **kwargs
    ) -> base.BoolResponseModel:
        """donut.isDon method
		:param owner_id: 
		"""

        params = self.get_set_params(locals())
        response = await self.api.request("donut.isDon", params)
        model = base.BoolResponse
        return model(**response).response