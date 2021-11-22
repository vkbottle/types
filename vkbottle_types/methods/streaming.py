import typing
from .base_category import BaseCategory
from vkbottle_types.responses.streaming import GetServerUrlResponse, GetServerUrlResponseModel
from vkbottle_types.responses.base import OkResponse


class StreamingCategory(BaseCategory):
    async def get_server_url(
        self, **kwargs
    ) -> GetServerUrlResponseModel:
        """Allows to receive data for the connection to Streaming API."""

        params = self.get_set_params(locals())
        response = await self.api.request("streaming.getServerUrl", params)
        model = GetServerUrlResponse
        return model(**response).response

    async def set_settings(
        self, monthly_tier: typing.Optional[str] = None, **kwargs
    ) -> int:
        """streaming.setSettings method

        :param monthly_tier:
        """

        params = self.get_set_params(locals())
        response = await self.api.request("streaming.setSettings", params)
        model = OkResponse
        return model(**response).response
