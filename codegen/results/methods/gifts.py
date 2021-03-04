from vkbottle_types.responses import gifts, base



class GiftsCategory(BaseCategory):
    async def get(
        self,
		user_id: Optional[int] = None,
		count: Optional[int] = None,
		offset: Optional[int] = None,
		**kwargs
    ) -> gifts.GetResponseModel:
        """Returns a list of user gifts.
		:param user_id: User ID.
		:param count: Number of gifts to return.
		:param offset: Offset needed to return a specific subset of results.
		"""

        params = self.get_set_params(locals())
        response = await self.api.request("gifts.get", params)
        model = gifts.GetResponse
        return model(**response).response