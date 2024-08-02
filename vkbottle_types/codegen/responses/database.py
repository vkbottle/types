import typing

from vkbottle_types.base_model import BaseModel, Field
from vkbottle_types.objects import (
    BaseCountry,
    BaseObject,
    DatabaseCity,
    DatabaseCityById,
    DatabaseFaculty,
    DatabaseRegion,
    DatabaseSchool,
    DatabaseSchoolClass,
    DatabaseStation,
    DatabaseUniversity,
)
from vkbottle_types.responses.base_response import BaseResponse


class DatabaseGetChairsResponseModel(BaseModel):
    count: int = Field()
    items: typing.List["BaseObject"] = Field()


class DatabaseGetChairsResponse(BaseResponse):
    response: "DatabaseGetChairsResponseModel" = Field()


class DatabaseGetCitiesByIdResponse(BaseResponse):
    response: typing.List["DatabaseCityById"] = Field()


class DatabaseGetCitiesResponseModel(BaseModel):
    count: int = Field()
    items: typing.List["DatabaseCity"] = Field()


class DatabaseGetCitiesResponse(BaseResponse):
    response: "DatabaseGetCitiesResponseModel" = Field()


class DatabaseGetCountriesByIdResponse(BaseResponse):
    response: typing.List["BaseCountry"] = Field()


class DatabaseGetCountriesResponseModel(BaseModel):
    count: int = Field()
    items: typing.List["BaseCountry"] = Field()


class DatabaseGetCountriesResponse(BaseResponse):
    response: "DatabaseGetCountriesResponseModel" = Field()


class DatabaseGetFacultiesResponseModel(BaseModel):
    count: int = Field()
    items: typing.List["DatabaseFaculty"] = Field()


class DatabaseGetFacultiesResponse(BaseResponse):
    response: "DatabaseGetFacultiesResponseModel" = Field()


class DatabaseGetMetroStationsByIdResponse(BaseResponse):
    response: typing.List["DatabaseStation"] = Field()


class DatabaseGetMetroStationsResponseModel(BaseModel):
    count: int = Field()
    items: typing.List["DatabaseStation"] = Field()


class DatabaseGetMetroStationsResponse(BaseResponse):
    response: "DatabaseGetMetroStationsResponseModel" = Field()


class DatabaseGetRegionsResponseModel(BaseModel):
    count: int = Field()
    items: typing.List["DatabaseRegion"] = Field()


class DatabaseGetRegionsResponse(BaseResponse):
    response: "DatabaseGetRegionsResponseModel" = Field()


class DatabaseGetSchoolClassesNewResponse(BaseResponse):
    response: typing.List["DatabaseSchoolClass"] = Field()


class DatabaseGetSchoolsResponseModel(BaseModel):
    count: int = Field()
    items: typing.List["DatabaseSchool"] = Field()


class DatabaseGetSchoolsResponse(BaseResponse):
    response: "DatabaseGetSchoolsResponseModel" = Field()


class DatabaseGetUniversitiesResponseModel(BaseModel):
    count: int = Field()
    items: typing.List["DatabaseUniversity"] = Field()


class DatabaseGetUniversitiesResponse(BaseResponse):
    response: "DatabaseGetUniversitiesResponseModel" = Field()
