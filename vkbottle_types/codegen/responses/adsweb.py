import typing

from vkbottle_types.base_model import BaseModel, Field
from vkbottle_types.objects import (
    AdswebGetAdCategoriesResponseCategoriesCategory,
    AdswebGetAdUnitsResponseAdUnitsAdUnit,
    AdswebGetFraudHistoryResponseEntriesEntry,
    AdswebGetSitesResponseSitesSite,
    AdswebGetStatisticsResponseItemsItem,
)
from vkbottle_types.responses.base_response import BaseResponse


class AdswebGetAdCategoriesResponseModel(BaseModel):
    categories: typing.List["AdswebGetAdCategoriesResponseCategoriesCategory"] = Field()


class AdswebGetAdCategoriesResponse(BaseResponse):
    response: "AdswebGetAdCategoriesResponseModel" = Field()


class AdswebGetAdUnitCodeResponseModel(BaseModel):
    html: str = Field()


class AdswebGetAdUnitCodeResponse(BaseResponse):
    response: "AdswebGetAdUnitCodeResponseModel" = Field()


class AdswebGetAdUnitsResponseModel(BaseModel):
    count: int = Field()
    ad_units: typing.Optional[typing.List["AdswebGetAdUnitsResponseAdUnitsAdUnit"]] = Field(
        default=None,
    )


class AdswebGetAdUnitsResponse(BaseResponse):
    response: "AdswebGetAdUnitsResponseModel" = Field()


class AdswebGetFraudHistoryResponseModel(BaseModel):
    count: int = Field()
    entries: typing.Optional[typing.List["AdswebGetFraudHistoryResponseEntriesEntry"]] = Field(
        default=None,
    )


class AdswebGetFraudHistoryResponse(BaseResponse):
    response: "AdswebGetFraudHistoryResponseModel" = Field()


class AdswebGetSitesResponseModel(BaseModel):
    count: int = Field()
    sites: typing.Optional[typing.List["AdswebGetSitesResponseSitesSite"]] = Field(
        default=None,
    )


class AdswebGetSitesResponse(BaseResponse):
    response: "AdswebGetSitesResponseModel" = Field()


class AdswebGetStatisticsResponseModel(BaseModel):
    items: typing.List["AdswebGetStatisticsResponseItemsItem"] = Field()
    next_page_id: typing.Optional[str] = Field(
        default=None,
    )


class AdswebGetStatisticsResponse(BaseResponse):
    response: "AdswebGetStatisticsResponseModel" = Field()
