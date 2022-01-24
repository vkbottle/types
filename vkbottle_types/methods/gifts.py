import typing

from vkbottle_types.responses.gifts import GetResponse, GetResponseModel

from .base_category import BaseCategory


class GiftsCategory(BaseCategory):
    async def get(
        self,
        user_id: typing.Optional[int] = None,
        count: typing.Optional[int] = None,
        offset: typing.Optional[int] = None,
        **kwargs
    ) -> GetResponseModel:
        """Returns a list of user gifts.

        :param user_id: User ID.
        :param count: Number of gifts to return.
        :param offset: Offset needed to return a specific subset of results.
        """

        params = self.get_set_params(locals())
        response = await self.api.request("gifts.get", params)
        model = GetResponse
        return model(**response).response
