import typing

from vkbottle_types.responses import base, store

from .base_category import BaseCategory


class StoreCategory(BaseCategory):
    async def add_stickers_to_favorite(
        self, sticker_ids: typing.List[int], **kwargs
    ) -> base.OkResponseModel:
        """Adds given sticker IDs to the list of user's favorite stickers
        :param sticker_ids: Sticker IDs to be added
        """

        params = self.get_set_params(locals())
        response = await self.api.request("store.addStickersToFavorite", params)
        model = base.OkResponse
        return model(**response).response

    async def get_favorite_stickers(
        self, **kwargs
    ) -> store.GetFavoriteStickersResponseModel:
        """store.getFavoriteStickers method"""

        params = self.get_set_params(locals())
        response = await self.api.request("store.getFavoriteStickers", params)
        model = store.GetFavoriteStickersResponse
        return model(**response).response

    async def get_products(
        self,
        type: typing.Optional[str] = None,
        merchant: typing.Optional[str] = None,
        section: typing.Optional[str] = None,
        product_ids: typing.Optional[typing.List[int]] = None,
        filters: typing.Optional[typing.List[str]] = None,
        extended: typing.Optional[bool] = None,
        **kwargs
    ) -> store.GetProductsResponseModel:
        """store.getProducts method
        :param type:
        :param merchant:
        :param section:
        :param product_ids:
        :param filters:
        :param extended:
        """

        params = self.get_set_params(locals())
        response = await self.api.request("store.getProducts", params)
        model = store.GetProductsResponse
        return model(**response).response

    async def get_stickers_keywords(
        self,
        stickers_ids: typing.Optional[typing.List[int]] = None,
        products_ids: typing.Optional[typing.List[int]] = None,
        aliases: typing.Optional[bool] = None,
        all_products: typing.Optional[bool] = None,
        need_stickers: typing.Optional[bool] = None,
        **kwargs
    ) -> store.GetStickersKeywordsResponseModel:
        """store.getStickersKeywords method
        :param stickers_ids:
        :param products_ids:
        :param aliases:
        :param all_products:
        :param need_stickers:
        """

        params = self.get_set_params(locals())
        response = await self.api.request("store.getStickersKeywords", params)
        model = store.GetStickersKeywordsResponse
        return model(**response).response

    async def remove_stickers_from_favorite(
        self, sticker_ids: typing.List[int], **kwargs
    ) -> base.OkResponseModel:
        """Removes given sticker IDs from the list of user's favorite stickers
        :param sticker_ids: Sticker IDs to be removed
        """

        params = self.get_set_params(locals())
        response = await self.api.request("store.removeStickersFromFavorite", params)
        model = base.OkResponse
        return model(**response).response
