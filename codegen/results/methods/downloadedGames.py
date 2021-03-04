from vkbottle_types.responses import downloadedGames, base



class DownloadedgamesCategory(BaseCategory):
    async def get_paid_status(
        self, user_id: Optional[int] = None, **kwargs
    ) -> downloadedGames.GetPaidStatusResponseModel:
        """downloadedGames.getPaidStatus method
		:param user_id: 
		"""

        params = self.get_set_params(locals())
        response = await self.api.request("downloadedGames.getPaidStatus", params)
        model = downloadedGames.GetPaidStatusResponse
        return model(**response).response