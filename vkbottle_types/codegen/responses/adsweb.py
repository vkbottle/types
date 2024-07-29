import typing

from vkbottle_types.base_model import Field
from vkbottle_types.responses.base_response import BaseResponse


class AdswebGetAdCategoriesResponse(BaseResponse):
    response: typing.Dict[str, typing.Any] = Field()


class AdswebGetAdUnitCodeResponse(BaseResponse):
    response: typing.Dict[str, typing.Any] = Field()


class AdswebGetAdUnitsResponse(BaseResponse):
    response: typing.Dict[str, typing.Any] = Field()


class AdswebGetFraudHistoryResponse(BaseResponse):
    response: typing.Dict[str, typing.Any] = Field()


class AdswebGetSitesResponse(BaseResponse):
    response: typing.Dict[str, typing.Any] = Field()


class AdswebGetStatisticsResponse(BaseResponse):
    response: typing.Dict[str, typing.Any] = Field()
