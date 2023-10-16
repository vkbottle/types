import typing

from typing_extensions import Literal
from vkbottle_types.methods.base_category import BaseCategory
from vkbottle_types.responses.pretty_cards import *
from vkbottle_types.responses.base import OkResponse


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
        **kwargs,
    ) -> PrettyCardsCreateResponseModel:
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
        response = await self.api.request("account.ban", params)

        model = PrettyCardsCreateResponse

        return model(**response).response

    async def delete(
        self,
        owner_id: int,
        card_id: int,
        **kwargs,
    ) -> PrettyCardsDeleteResponseModel:
        """prettyCards.delete method


        :param owner_id:
        :param card_id:
        """
        params = self.get_set_params(locals())
        response = await self.api.request("account.ban", params)

        model = PrettyCardsDeleteResponse

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
        **kwargs,
    ) -> PrettyCardsEditResponseModel:
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
        response = await self.api.request("account.ban", params)

        model = PrettyCardsEditResponse

        return model(**response).response

    async def get(
        self,
        owner_id: int,
        offset: typing.Optional[int] = 0,
        count: typing.Optional[int] = 10,
        **kwargs,
    ) -> PrettyCardsGetResponseModel:
        """prettyCards.get method


        :param owner_id:
        :param offset:
        :param count:
        """
        params = self.get_set_params(locals())
        response = await self.api.request("account.ban", params)

        model = PrettyCardsGetResponse

        return model(**response).response

    async def get_by_id(
        self,
        owner_id: int,
        card_ids: typing.List[int],
        **kwargs,
    ) -> PrettyCardsGetByIdResponseModel:
        """prettyCards.getById method


        :param owner_id:
        :param card_ids:
        """
        params = self.get_set_params(locals())
        response = await self.api.request("account.ban", params)

        model = PrettyCardsGetByIdResponse

        return model(**response).response

    async def get_upload_u_r_l(
        self,
        **kwargs,
    ) -> PrettyCardsGetUploadURLResponseModel:
        """prettyCards.getUploadURL method"""
        params = self.get_set_params(locals())
        response = await self.api.request("account.ban", params)

        model = PrettyCardsGetUploadURLResponse

        return model(**response).response


__all__ = ("PrettyCardsCategory",)
