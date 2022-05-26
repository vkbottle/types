import typing

from vkbottle_types.responses.pretty_cards import (
    CreateResponse,
    CreateResponseModel,
    DeleteResponse,
    DeleteResponseModel,
    EditResponse,
    EditResponseModel,
    GetByIdResponse,
    GetResponse,
    GetResponseModel,
    GetUploadURLResponse,
    PrettyCardsPrettyCardOrError,
)

from .base_category import BaseCategory


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
    ) -> CreateResponseModel:
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
        model = CreateResponse
        return model(**response).response

    async def delete(
        self, owner_id: int, card_id: int, **kwargs
    ) -> DeleteResponseModel:
        """prettyCards.delete method

        :param owner_id:
        :param card_id:
        """

        params = self.get_set_params(locals())
        response = await self.api.request("prettyCards.delete", params)
        model = DeleteResponse
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
    ) -> EditResponseModel:
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
        model = EditResponse
        return model(**response).response

    async def get(
        self,
        owner_id: int,
        offset: typing.Optional[int] = None,
        count: typing.Optional[int] = None,
        **kwargs
    ) -> GetResponseModel:
        """prettyCards.get method

        :param owner_id:
        :param offset:
        :param count:
        """

        params = self.get_set_params(locals())
        response = await self.api.request("prettyCards.get", params)
        model = GetResponse
        return model(**response).response

    async def get_by_id(
        self, owner_id: int, card_ids: typing.List[int], **kwargs
    ) -> typing.List[PrettyCardsPrettyCardOrError]:
        """prettyCards.getById method

        :param owner_id:
        :param card_ids:
        """

        params = self.get_set_params(locals())
        response = await self.api.request("prettyCards.getById", params)
        model = GetByIdResponse
        return model(**response).response

    async def get_upload_url(self, **kwargs) -> str:
        """prettyCards.getUploadURL method"""

        params = self.get_set_params(locals())
        response = await self.api.request("prettyCards.getUploadURL", params)
        model = GetUploadURLResponse
        return model(**response).response


__all__ = ("PrettyCardsCategory",)
