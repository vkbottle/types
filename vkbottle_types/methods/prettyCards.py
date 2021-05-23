import typing
from .base_category import BaseCategory
from vkbottle_types.responses import prettyCards


class PrettyCardsCategory(BaseCategory):
    async def create(
        self,
        owner_id: int,
        photo: str,
        title: str,
        link: str,
        price: typing.Optional[str] = None,
        price_old: typing.Optional[str] = None,
        button: typing.Optional[str] = None,
        **kwargs
    ) -> prettyCards.CreateResponseModel:
        """prettyCards.create method
        :param owner_id:
        :param photo:
        :param title:
        :param link:
        :param price:
        :param price_old:
        :param button:
        """

        params = self.get_set_params(locals())
        response = await self.api.request("prettyCards.create", params)
        model = prettyCards.CreateResponse
        return model(**response).response

    async def delete(
        self, owner_id: int, card_id: int, **kwargs
    ) -> prettyCards.DeleteResponseModel:
        """prettyCards.delete method
        :param owner_id:
        :param card_id:
        """

        params = self.get_set_params(locals())
        response = await self.api.request("prettyCards.delete", params)
        model = prettyCards.DeleteResponse
        return model(**response).response

    async def edit(
        self,
        owner_id: int,
        card_id: int,
        photo: typing.Optional[str] = None,
        title: typing.Optional[str] = None,
        link: typing.Optional[str] = None,
        price: typing.Optional[str] = None,
        price_old: typing.Optional[str] = None,
        button: typing.Optional[str] = None,
        **kwargs
    ) -> prettyCards.EditResponseModel:
        """prettyCards.edit method
        :param owner_id:
        :param card_id:
        :param photo:
        :param title:
        :param link:
        :param price:
        :param price_old:
        :param button:
        """

        params = self.get_set_params(locals())
        response = await self.api.request("prettyCards.edit", params)
        model = prettyCards.EditResponse
        return model(**response).response

    async def get(
        self,
        owner_id: int,
        offset: typing.Optional[int] = None,
        count: typing.Optional[int] = None,
        **kwargs
    ) -> prettyCards.GetResponseModel:
        """prettyCards.get method
        :param owner_id:
        :param offset:
        :param count:
        """

        params = self.get_set_params(locals())
        response = await self.api.request("prettyCards.get", params)
        model = prettyCards.GetResponse
        return model(**response).response

    async def get_by_id(
        self, owner_id: int, card_ids: typing.List[int], **kwargs
    ) -> prettyCards.GetByIdResponseModel:
        """prettyCards.getById method
        :param owner_id:
        :param card_ids:
        """

        params = self.get_set_params(locals())
        response = await self.api.request("prettyCards.getById", params)
        model = prettyCards.GetByIdResponse
        return model(**response).response

    async def get_upload_u_r_l(
        self, **kwargs
    ) -> prettyCards.GetUploadURLResponseModel:
        """prettyCards.getUploadURL method"""

        params = self.get_set_params(locals())
        response = await self.api.request("prettyCards.getUploadURL", params)
        model = prettyCards.GetUploadURLResponse
        return model(**response).response
