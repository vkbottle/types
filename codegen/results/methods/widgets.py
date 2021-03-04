from vkbottle_types.responses import widgets, base



class WidgetsCategory(BaseCategory):
    async def get_comments(
        self,
		widget_api_id: Optional[int] = None,
		url: Optional[str] = None,
		page_id: Optional[str] = None,
		order: Optional[str] = None,
		fields: Optional[List[UsersFields]] = None,
		offset: Optional[int] = None,
		count: Optional[int] = None,
		**kwargs
    ) -> widgets.GetCommentsResponseModel:
        """Gets a list of comments for the page added through the [vk.com/dev/Comments|Comments widget].
		:param widget_api_id: 
		:param url: 
		:param page_id: 
		:param order: 
		:param fields: 
		:param offset: 
		:param count: 
		"""

        params = self.get_set_params(locals())
        response = await self.api.request("widgets.getComments", params)
        model = widgets.GetCommentsResponse
        return model(**response).response

    async def get_pages(
        self,
		widget_api_id: Optional[int] = None,
		order: Optional[str] = None,
		period: Optional[str] = None,
		offset: Optional[int] = None,
		count: Optional[int] = None,
		**kwargs
    ) -> widgets.GetPagesResponseModel:
        """Gets a list of application/site pages where the [vk.com/dev/Comments|Comments widget] or [vk.com/dev/Like|Like widget] is installed.
		:param widget_api_id: 
		:param order: 
		:param period: 
		:param offset: 
		:param count: 
		"""

        params = self.get_set_params(locals())
        response = await self.api.request("widgets.getPages", params)
        model = widgets.GetPagesResponse
        return model(**response).response