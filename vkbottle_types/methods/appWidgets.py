from vkbottle_types.responses import base
from .base_category import BaseCategory


class AppWidgetsCategory(BaseCategory):
    async def update(self, code: str, type: str, **kwargs) -> base.OkResponseModel:
        """Allows to update community app widget
        :param code:
        :param type:
        """

        params = self.get_set_params(locals())
        return base.OkResponse(**await self.api.request("appWidgets.update", params))
