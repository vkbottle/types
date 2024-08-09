import typing

from vkbottle_types.methods.base_category import BaseCategory
from vkbottle_types.objects import PrettyCardsPrettyCardOrError
from vkbottle_types.responses.pretty_cards import *  # noqa: F401,F403  # type: ignore


class PrettyCardsCategory(BaseCategory):
    async def create(
        self,
        link: str,
        owner_id: int,
        photo: str,
        title: str,
        button: typing.Optional[str] = None,
        price: typing.Optional[str] = None,
        price_old: typing.Optional[str] = None,
        **kwargs: typing.Any,
    ) -> PrettyCardsCreateResponseModel:
        """Method `prettyCards.create()`

        :param link:
        :param owner_id:
        :param photo:
        :param title:
        :param button:
        :param price:
        :param price_old:
        """

        params = self.get_set_params(locals())
        response = await self.api.request("prettyCards.create", params)
        model = PrettyCardsCreateResponse
        return model(**response).response

    async def delete(
        self,
        card_id: int,
        owner_id: int,
        **kwargs: typing.Any,
    ) -> PrettyCardsDeleteResponseModel:
        """Method `prettyCards.delete()`

        :param card_id:
        :param owner_id:
        """

        params = self.get_set_params(locals())
        response = await self.api.request("prettyCards.delete", params)
        model = PrettyCardsDeleteResponse
        return model(**response).response

    async def edit(
        self,
        card_id: int,
        owner_id: int,
        button: typing.Optional[str] = None,
        link: typing.Optional[str] = None,
        photo: typing.Optional[str] = None,
        price: typing.Optional[str] = None,
        price_old: typing.Optional[str] = None,
        title: typing.Optional[str] = None,
        **kwargs: typing.Any,
    ) -> PrettyCardsEditResponseModel:
        """Method `prettyCards.edit()`

        :param card_id:
        :param owner_id:
        :param button:
        :param link:
        :param photo:
        :param price:
        :param price_old:
        :param title:
        """

        params = self.get_set_params(locals())
        response = await self.api.request("prettyCards.edit", params)
        model = PrettyCardsEditResponse
        return model(**response).response

    async def get(
        self,
        owner_id: int,
        count: typing.Optional[int] = None,
        offset: typing.Optional[int] = None,
        **kwargs: typing.Any,
    ) -> PrettyCardsGetResponseModel:
        """Method `prettyCards.get()`

        :param owner_id:
        :param count:
        :param offset:
        """

        params = self.get_set_params(locals())
        response = await self.api.request("prettyCards.get", params)
        model = PrettyCardsGetResponse
        return model(**response).response

    async def get_by_id(
        self,
        card_ids: typing.List[int],
        owner_id: int,
        **kwargs: typing.Any,
    ) -> typing.List[PrettyCardsPrettyCardOrError]:
        """Method `prettyCards.getById()`

        :param card_ids:
        :param owner_id:
        """

        params = self.get_set_params(locals())
        response = await self.api.request("prettyCards.getById", params)
        model = PrettyCardsGetByIdResponse
        return model(**response).response

    async def get_upload_url(
        self,
        **kwargs: typing.Any,
    ) -> str:
        """Method `prettyCards.getUploadURL()`"""

        params = self.get_set_params(locals())
        response = await self.api.request("prettyCards.getUploadURL", params)
        model = PrettyCardsGetUploadURLResponse
        return model(**response).response


__all__ = ("PrettyCardsCategory",)
