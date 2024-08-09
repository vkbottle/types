import typing

from vkbottle_types.methods.base_category import BaseCategory
from vkbottle_types.responses.adsweb import *  # noqa: F401,F403  # type: ignore


class AdswebCategory(BaseCategory):
    async def get_ad_categories(
        self,
        office_id: int,
        **kwargs: typing.Any,
    ) -> AdswebGetAdCategoriesResponseModel:
        """Method `adsweb.getAdCategories()`

        :param office_id:
        """

        params = self.get_set_params(locals())
        response = await self.api.request("adsweb.getAdCategories", params)
        model = AdswebGetAdCategoriesResponse
        return model(**response).response

    async def get_ad_unit_code(
        self,
        **kwargs: typing.Any,
    ) -> AdswebGetAdUnitCodeResponseModel:
        """Method `adsweb.getAdUnitCode()`"""

        params = self.get_set_params(locals())
        response = await self.api.request("adsweb.getAdUnitCode", params)
        model = AdswebGetAdUnitCodeResponse
        return model(**response).response

    async def get_ad_units(
        self,
        office_id: int,
        ad_units_ids: typing.Optional[str] = None,
        fields: typing.Optional[str] = None,
        limit: typing.Optional[int] = None,
        offset: typing.Optional[int] = None,
        sites_ids: typing.Optional[str] = None,
        **kwargs: typing.Any,
    ) -> AdswebGetAdUnitsResponseModel:
        """Method `adsweb.getAdUnits()`

        :param office_id:
        :param ad_units_ids:
        :param fields:
        :param limit:
        :param offset:
        :param sites_ids:
        """

        params = self.get_set_params(locals())
        response = await self.api.request("adsweb.getAdUnits", params)
        model = AdswebGetAdUnitsResponse
        return model(**response).response

    async def get_fraud_history(
        self,
        office_id: int,
        limit: typing.Optional[int] = None,
        offset: typing.Optional[int] = None,
        sites_ids: typing.Optional[str] = None,
        **kwargs: typing.Any,
    ) -> AdswebGetFraudHistoryResponseModel:
        """Method `adsweb.getFraudHistory()`

        :param office_id:
        :param limit:
        :param offset:
        :param sites_ids:
        """

        params = self.get_set_params(locals())
        response = await self.api.request("adsweb.getFraudHistory", params)
        model = AdswebGetFraudHistoryResponse
        return model(**response).response

    async def get_sites(
        self,
        office_id: int,
        fields: typing.Optional[str] = None,
        limit: typing.Optional[int] = None,
        offset: typing.Optional[int] = None,
        sites_ids: typing.Optional[str] = None,
        **kwargs: typing.Any,
    ) -> AdswebGetSitesResponseModel:
        """Method `adsweb.getSites()`

        :param office_id:
        :param fields:
        :param limit:
        :param offset:
        :param sites_ids:
        """

        params = self.get_set_params(locals())
        response = await self.api.request("adsweb.getSites", params)
        model = AdswebGetSitesResponse
        return model(**response).response

    async def get_statistics(
        self,
        date_from: str,
        date_to: str,
        ids: str,
        ids_type: str,
        office_id: int,
        period: str,
        fields: typing.Optional[str] = None,
        limit: typing.Optional[int] = None,
        page_id: typing.Optional[str] = None,
        **kwargs: typing.Any,
    ) -> AdswebGetStatisticsResponseModel:
        """Method `adsweb.getStatistics()`

        :param date_from:
        :param date_to:
        :param ids:
        :param ids_type:
        :param office_id:
        :param period:
        :param fields:
        :param limit:
        :param page_id:
        """

        params = self.get_set_params(locals())
        response = await self.api.request("adsweb.getStatistics", params)
        model = AdswebGetStatisticsResponse
        return model(**response).response


__all__ = ("AdswebCategory",)
