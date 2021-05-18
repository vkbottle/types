import typing

from vkbottle_types.responses import base, streaming

from .base_category import BaseCategory


class StreamingCategory(BaseCategory):
    async def get_server_url(self, **kwargs) -> streaming.GetServerUrlResponseModel:
        """Allows to receive data for the connection to Streaming API."""

        params = self.get_set_params(locals())
        response = await self.api.request("streaming.getServerUrl", params)
        model = streaming.GetServerUrlResponse
        return model(**response).response

    async def set_settings(
        self, monthly_tier: typing.Optional[str] = None, **kwargs
    ) -> base.OkResponseModel:
        """streaming.setSettings method
        :param monthly_tier:
        """

        params = self.get_set_params(locals())
        response = await self.api.request("streaming.setSettings", params)
        model = base.OkResponse
        return model(**response).response
