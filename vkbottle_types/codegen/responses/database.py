import typing

from vkbottle_types.base_model import Field
from vkbottle_types.objects import BaseCountry, DatabaseCityById, DatabaseSchoolClass, DatabaseStation
from vkbottle_types.responses.base_response import BaseResponse


class DatabaseGetChairsResponse(BaseResponse):
    response: typing.Dict[str, typing.Any] = Field()


class DatabaseGetCitiesByIdResponse(BaseResponse):
    response: typing.List[DatabaseCityById] = Field()


class DatabaseGetCitiesResponse(BaseResponse):
    response: typing.Dict[str, typing.Any] = Field()


class DatabaseGetCountriesByIdResponse(BaseResponse):
    response: typing.List[BaseCountry] = Field()


class DatabaseGetCountriesResponse(BaseResponse):
    response: typing.Dict[str, typing.Any] = Field()


class DatabaseGetFacultiesResponse(BaseResponse):
    response: typing.Dict[str, typing.Any] = Field()


class DatabaseGetMetroStationsByIdResponse(BaseResponse):
    response: typing.List[DatabaseStation] = Field()


class DatabaseGetMetroStationsResponse(BaseResponse):
    response: typing.Dict[str, typing.Any] = Field()


class DatabaseGetRegionsResponse(BaseResponse):
    response: typing.Dict[str, typing.Any] = Field()


class DatabaseGetSchoolClassesNewResponse(BaseResponse):
    response: typing.List[DatabaseSchoolClass] = Field()


class DatabaseGetSchoolsResponse(BaseResponse):
    response: typing.Dict[str, typing.Any] = Field()


class DatabaseGetUniversitiesResponse(BaseResponse):
    response: typing.Dict[str, typing.Any] = Field()
