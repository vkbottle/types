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
        sticker_ids: typing.List[int],
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
        extended: typing.Optional[bool] = None,
        filters: typing.Optional[typing.List[str]] = None,
        merchant: typing.Optional[str] = None,
        product_ids: typing.Optional[typing.List[int]] = None,
        section: typing.Optional[str] = None,
        type: typing.Optional[str] = None,
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
        aliases: typing.Optional[bool] = None,
        all_products: typing.Optional[bool] = None,
        need_stickers: typing.Optional[bool] = None,
        products_ids: typing.Optional[typing.List[int]] = None,
        stickers_ids: typing.Optional[typing.List[int]] = None,
        vmoji_promo: typing.Optional[bool] = None,
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
        sticker_ids: typing.List[int],
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
