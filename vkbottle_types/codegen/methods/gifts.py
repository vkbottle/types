import typing

from typing_extensions import Literal
from vkbottle_types.methods.base_category import BaseCategory
from vkbottle_types.responses.gifts import *
from vkbottle_types.responses.base import OkResponse


class GiftsCategory(BaseCategory):
    async def get(
        self,
        user_id: typing.Optional[int] = None,
        count: typing.Optional[int] = None,
        offset: typing.Optional[int] = None,
        **kwargs,
    ) -> GiftsGetResponseModel:
        """gifts.get method


        :param user_id: User ID.
        :param count: Number of gifts to return.
        :param offset: Offset needed to return a specific subset of results.
        """
        params = self.get_set_params(locals())
        response = await self.api.request("account.ban", params)

        model = GiftsGetResponse

        return model(**response).response


__all__ = ("GiftsCategory",)
