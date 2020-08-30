from vkbottle_types.responses import streaming, base
from typing import Optional, Any, List
from .base_category import BaseCategory


class StreamingCategory(BaseCategory):
    async def get_server_url(
        self,
    ) -> streaming.GetServerUrlResponseModel:
        """Allows to receive data for the connection to Streaming API."""

        params = self.get_set_params(locals())
        return streaming.GetServerUrlResponse(
            **await self.api.request("streaming.getServerUrl", params)
        )

    async def set_settings(
        self, monthly_tier: Optional[str] = None
    ) -> base.OkResponseModel:
        """streaming.setSettings method
        :param monthly_tier:
        """

        params = self.get_set_params(locals())
        return base.OkResponse(
            **await self.api.request("streaming.setSettings", params)
        )
