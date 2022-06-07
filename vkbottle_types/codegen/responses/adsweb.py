import typing

from vkbottle_types.objects import (
    AdswebGetAdCategoriesResponseCategoriesCategory,
    AdswebGetAdUnitsResponseAdUnitsAdUnit,
    AdswebGetFraudHistoryResponseEntriesEntry,
    AdswebGetSitesResponseSitesSite,
    AdswebGetStatisticsResponseItemsItem,
)
from vkbottle_types.responses.base_response import BaseResponse


class GetAdCategoriesResponse(BaseResponse):
    response: "GetAdCategoriesResponseModel"


class GetAdUnitCodeResponse(BaseResponse):
    response: "GetAdUnitCodeResponseModel"


class GetAdUnitsResponse(BaseResponse):
    response: "GetAdUnitsResponseModel"


class GetFraudHistoryResponse(BaseResponse):
    response: "GetFraudHistoryResponseModel"


class GetSitesResponse(BaseResponse):
    response: "GetSitesResponseModel"


class GetStatisticsResponse(BaseResponse):
    response: "GetStatisticsResponseModel"


class GetAdCategoriesResponseModel(BaseResponse):
    categories: typing.Optional[
        typing.List["AdswebGetAdCategoriesResponseCategoriesCategory"]
    ] = None


class GetAdUnitCodeResponseModel(BaseResponse):
    html: typing.Optional[str] = None


class GetAdUnitsResponseModel(BaseResponse):
    count: typing.Optional[int] = None
    ad_units: typing.Optional[
        typing.List["AdswebGetAdUnitsResponseAdUnitsAdUnit"]
    ] = None


class GetFraudHistoryResponseModel(BaseResponse):
    count: typing.Optional[int] = None
    entries: typing.Optional[
        typing.List["AdswebGetFraudHistoryResponseEntriesEntry"]
    ] = None


class GetSitesResponseModel(BaseResponse):
    count: typing.Optional[int] = None
    sites: typing.Optional[typing.List["AdswebGetSitesResponseSitesSite"]] = None


class GetStatisticsResponseModel(BaseResponse):
    next_page_id: typing.Optional[str] = None
    items: typing.Optional[typing.List["AdswebGetStatisticsResponseItemsItem"]] = None


__all__ = (
    "AdswebGetAdCategoriesResponseCategoriesCategory",
    "AdswebGetAdUnitsResponseAdUnitsAdUnit",
    "AdswebGetFraudHistoryResponseEntriesEntry",
    "AdswebGetSitesResponseSitesSite",
    "AdswebGetStatisticsResponseItemsItem",
    "GetAdCategoriesResponse",
    "GetAdCategoriesResponseModel",
    "GetAdUnitCodeResponse",
    "GetAdUnitCodeResponseModel",
    "GetAdUnitsResponse",
    "GetAdUnitsResponseModel",
    "GetFraudHistoryResponse",
    "GetFraudHistoryResponseModel",
    "GetSitesResponse",
    "GetSitesResponseModel",
    "GetStatisticsResponse",
    "GetStatisticsResponseModel",
)
