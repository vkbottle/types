import inspect
import typing
from .base_response import BaseResponse
from vkbottle_types.objects import (
    AdswebGetAdCategoriesResponseCategoriesCategory,
    AdswebGetAdUnitsResponseAdUnitsAdUnit,
    AdswebGetFraudHistoryResponseEntriesEntry,
    AdswebGetSitesResponseSitesSite,
    AdswebGetStatisticsResponseItemsItem
)


class GetAdCategoriesResponse(BaseResponse):
    response: typing.Optional["GetAdCategoriesResponseModel"] = None


class GetAdUnitCodeResponse(BaseResponse):
    response: typing.Optional["GetAdUnitCodeResponseModel"] = None


class GetAdUnitsResponse(BaseResponse):
    response: typing.Optional["GetAdUnitsResponseModel"] = None


class GetFraudHistoryResponse(BaseResponse):
    response: typing.Optional["GetFraudHistoryResponseModel"] = None


class GetSitesResponse(BaseResponse):
    response: typing.Optional["GetSitesResponseModel"] = None


class GetStatisticsResponse(BaseResponse):
    response: typing.Optional["GetStatisticsResponseModel"] = None


class GetAdCategoriesResponseModel(BaseResponse):
    categories: typing.Optional[typing.List["AdswebGetAdCategoriesResponseCategoriesCategory"]] = None


class GetAdUnitCodeResponseModel(BaseResponse):
    html: typing.Optional[str] = None


class GetAdUnitsResponseModel(BaseResponse):
    count: typing.Optional[int] = None
    ad_units: typing.Optional[typing.List["AdswebGetAdUnitsResponseAdUnitsAdUnit"]] = None


class GetFraudHistoryResponseModel(BaseResponse):
    count: typing.Optional[int] = None
    entries: typing.Optional[typing.List["AdswebGetFraudHistoryResponseEntriesEntry"]] = None


class GetSitesResponseModel(BaseResponse):
    count: typing.Optional[int] = None
    sites: typing.Optional[typing.List["AdswebGetSitesResponseSitesSite"]] = None


class GetStatisticsResponseModel(BaseResponse):
    next_page_id: typing.Optional[str] = None
    items: typing.Optional[typing.List["AdswebGetStatisticsResponseItemsItem"]] = None


for item in locals().copy().values():
    if inspect.isclass(item) and issubclass(item, BaseResponse):
        item.update_forward_refs()
