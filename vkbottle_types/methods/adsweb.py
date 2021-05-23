import typing
from .base_category import BaseCategory
from vkbottle_types.responses import adsweb


class AdswebCategory(BaseCategory):
    async def get_ad_categories(
        self, office_id: int, **kwargs
    ) -> adsweb.GetAdCategoriesResponseModel:
        """adsweb.getAdCategories method
        :param office_id:
        """

        params = self.get_set_params(locals())
        response = await self.api.request("adsweb.getAdCategories", params)
        model = adsweb.GetAdCategoriesResponse
        return model(**response).response

    async def get_ad_unit_code(
        self, **kwargs
    ) -> adsweb.GetAdUnitCodeResponseModel:
        """adsweb.getAdUnitCode method"""

        params = self.get_set_params(locals())
        response = await self.api.request("adsweb.getAdUnitCode", params)
        model = adsweb.GetAdUnitCodeResponse
        return model(**response).response

    async def get_ad_units(
        self,
        office_id: int,
        sites_ids: typing.Optional[str] = None,
        ad_units_ids: typing.Optional[str] = None,
        fields: typing.Optional[str] = None,
        limit: typing.Optional[int] = None,
        offset: typing.Optional[int] = None,
        **kwargs
    ) -> adsweb.GetAdUnitsResponseModel:
        """adsweb.getAdUnits method
        :param office_id:
        :param sites_ids:
        :param ad_units_ids:
        :param fields:
        :param limit:
        :param offset:
        """

        params = self.get_set_params(locals())
        response = await self.api.request("adsweb.getAdUnits", params)
        model = adsweb.GetAdUnitsResponse
        return model(**response).response

    async def get_fraud_history(
        self,
        office_id: int,
        sites_ids: typing.Optional[str] = None,
        limit: typing.Optional[int] = None,
        offset: typing.Optional[int] = None,
        **kwargs
    ) -> adsweb.GetFraudHistoryResponseModel:
        """adsweb.getFraudHistory method
        :param office_id:
        :param sites_ids:
        :param limit:
        :param offset:
        """

        params = self.get_set_params(locals())
        response = await self.api.request("adsweb.getFraudHistory", params)
        model = adsweb.GetFraudHistoryResponse
        return model(**response).response

    async def get_sites(
        self,
        office_id: int,
        sites_ids: typing.Optional[str] = None,
        fields: typing.Optional[str] = None,
        limit: typing.Optional[int] = None,
        offset: typing.Optional[int] = None,
        **kwargs
    ) -> adsweb.GetSitesResponseModel:
        """adsweb.getSites method
        :param office_id:
        :param sites_ids:
        :param fields:
        :param limit:
        :param offset:
        """

        params = self.get_set_params(locals())
        response = await self.api.request("adsweb.getSites", params)
        model = adsweb.GetSitesResponse
        return model(**response).response

    async def get_statistics(
        self,
        office_id: int,
        ids_type: str,
        ids: str,
        period: str,
        date_from: str,
        date_to: str,
        fields: typing.Optional[str] = None,
        limit: typing.Optional[int] = None,
        page_id: typing.Optional[str] = None,
        **kwargs
    ) -> adsweb.GetStatisticsResponseModel:
        """adsweb.getStatistics method
        :param office_id:
        :param ids_type:
        :param ids:
        :param period:
        :param date_from:
        :param date_to:
        :param fields:
        :param limit:
        :param page_id:
        """

        params = self.get_set_params(locals())
        response = await self.api.request("adsweb.getStatistics", params)
        model = adsweb.GetStatisticsResponse
        return model(**response).response
