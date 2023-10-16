import typing
from vkbottle_types.responses.base_response import BaseResponse, BaseModel
from vkbottle_types.base_model import Field


class AdswebGetAdCategoriesResponseCategoriesCategoryResponseModel(BaseModel):
    id: int = Field()

    name: str = Field()


class AdswebGetAdCategoriesResponseCategoriesCategoryResponse(BaseResponse):
    response: "AdswebGetAdCategoriesResponseCategoriesCategoryResponseModel"


class AdswebGetAdUnitsResponseAdUnitsAdUnitResponseModel(BaseModel):
    id: int = Field()

    site_id: int = Field()

    name: typing.Optional[str] = Field(
        default=None,
    )


class AdswebGetAdUnitsResponseAdUnitsAdUnitResponse(BaseResponse):
    response: "AdswebGetAdUnitsResponseAdUnitsAdUnitResponseModel"


class AdswebGetFraudHistoryResponseEntriesEntryResponseModel(BaseModel):
    site_id: int = Field()

    day: str = Field()


class AdswebGetFraudHistoryResponseEntriesEntryResponse(BaseResponse):
    response: "AdswebGetFraudHistoryResponseEntriesEntryResponseModel"


class AdswebGetSitesResponseSitesSiteResponseModel(BaseModel):
    id: int = Field()

    status_user: typing.Optional[str] = Field(
        default=None,
    )

    status_moder: typing.Optional[str] = Field(
        default=None,
    )

    domains: typing.Optional[str] = Field(
        default=None,
    )


class AdswebGetSitesResponseSitesSiteResponse(BaseResponse):
    response: "AdswebGetSitesResponseSitesSiteResponseModel"


class AdswebGetStatisticsResponseItemsItemResponseModel(BaseModel):
    site_id: typing.Optional[int] = Field(
        default=None,
    )

    ad_unit_id: typing.Optional[int] = Field(
        default=None,
    )

    overall_count: typing.Optional[int] = Field(
        default=None,
    )

    months_count: typing.Optional[int] = Field(
        default=None,
    )

    month_min: typing.Optional[str] = Field(
        default=None,
    )

    month_max: typing.Optional[str] = Field(
        default=None,
    )

    days_count: typing.Optional[int] = Field(
        default=None,
    )

    day_min: typing.Optional[str] = Field(
        default=None,
    )

    day_max: typing.Optional[str] = Field(
        default=None,
    )

    hours_count: typing.Optional[int] = Field(
        default=None,
    )

    hour_min: typing.Optional[str] = Field(
        default=None,
    )

    hour_max: typing.Optional[str] = Field(
        default=None,
    )


class AdswebGetStatisticsResponseItemsItemResponse(BaseResponse):
    response: "AdswebGetStatisticsResponseItemsItemResponseModel"
