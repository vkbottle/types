import typing

from vkbottle_types.methods.base_category import BaseCategory
from vkbottle_types.responses.downloaded_games import *  # noqa: F401,F403  # type: ignore


class DownloadedGamesCategory(BaseCategory):
    async def get_paid_status(
        self,
        user_id: typing.Optional[int] = None,
        **kwargs: typing.Any,
    ) -> DownloadedGamesPaidStatusResponseModel:
        """Method `downloadedGames.getPaidStatus()`

        :param user_id:
        """

        params = self.get_set_params(locals())
        response = await self.api.request("downloadedGames.getPaidStatus", params)
        model = DownloadedGamesPaidStatusResponse
        return model(**response).response


__all__ = ("DownloadedGamesCategory",)
