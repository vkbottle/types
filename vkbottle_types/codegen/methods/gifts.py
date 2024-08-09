import typing

from vkbottle_types.methods.base_category import BaseCategory
from vkbottle_types.responses.gifts import *  # noqa: F401,F403  # type: ignore


class GiftsCategory(BaseCategory):
    async def get(
        self,
        count: typing.Optional[int] = None,
        offset: typing.Optional[int] = None,
        user_id: typing.Optional[int] = None,
        **kwargs: typing.Any,
    ) -> GiftsGetResponseModel:
        """Method `gifts.get()`

        :param count: Number of gifts to return.
        :param offset: Offset needed to return a specific subset of results.
        :param user_id: User ID.
        """

        params = self.get_set_params(locals())
        response = await self.api.request("gifts.get", params)
        model = GiftsGetResponse
        return model(**response).response


__all__ = ("GiftsCategory",)
