import typing

from vkbottle_types.methods.base_category import BaseCategory
from vkbottle_types.responses.base import (
    BaseOkResponse,
    BaseOkResponseModel,
)
from vkbottle_types.responses.store import *  # noqa: F401,F403  # type: ignore


class StoreCategory(BaseCategory):
    async def add_stickers_to_favorite(
        self,
        sticker_ids: list[int],
        **kwargs: typing.Any,
    ) -> BaseOkResponseModel:
        """Method `store.addStickersToFavorite()`

        :param sticker_ids: Sticker IDs to be added
        """

        params = self.get_set_params(locals())
        response = await self.api.request("store.addStickersToFavorite", params)
        model = BaseOkResponse
        return model(**response).response

    async def get_favorite_stickers(
        self,
        **kwargs: typing.Any,
    ) -> StoreGetFavoriteStickersResponseModel:
        """Method `store.getFavoriteStickers()`"""

        params = self.get_set_params(locals())
        response = await self.api.request("store.getFavoriteStickers", params)
        model = StoreGetFavoriteStickersResponse
        return model(**response).response

    async def get_products(
        self,
        extended: bool | None = None,
        filters: list[str] | None = None,
        merchant: str | None = None,
        product_ids: list[int] | None = None,
        section: str | None = None,
        type: str | None = None,
        **kwargs: typing.Any,
    ) -> StoreGetProductsResponseModel:
        """Method `store.getProducts()`

        :param extended:
        :param filters:
        :param merchant:
        :param product_ids:
        :param section:
        :param type:
        """

        params = self.get_set_params(locals())
        response = await self.api.request("store.getProducts", params)
        model = StoreGetProductsResponse
        return model(**response).response

    async def get_stickers_keywords(
        self,
        aliases: bool | None = None,
        all_products: bool | None = None,
        need_stickers: bool | None = None,
        products_ids: list[int] | None = None,
        stickers_ids: list[int] | None = None,
        vmoji_promo: bool | None = None,
        **kwargs: typing.Any,
    ) -> StoreGetStickersKeywordsResponseModel:
        """Method `store.getStickersKeywords()`

        :param aliases:
        :param all_products:
        :param need_stickers:
        :param products_ids:
        :param stickers_ids:
        :param vmoji_promo:
        """

        params = self.get_set_params(locals())
        response = await self.api.request("store.getStickersKeywords", params)
        model = StoreGetStickersKeywordsResponse
        return model(**response).response

    async def remove_stickers_from_favorite(
        self,
        sticker_ids: list[int],
        **kwargs: typing.Any,
    ) -> BaseOkResponseModel:
        """Method `store.removeStickersFromFavorite()`

        :param sticker_ids: Sticker IDs to be removed
        """

        params = self.get_set_params(locals())
        response = await self.api.request("store.removeStickersFromFavorite", params)
        model = BaseOkResponse
        return model(**response).response


__all__ = ("StoreCategory",)
