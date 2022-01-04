import inspect
import typing
from .base_response import BaseResponse
from vkbottle_types.objects import (
    BaseCountry,
    BaseObject,
    DatabaseCity,
    DatabaseFaculty,
    DatabaseRegion,
    DatabaseSchool,
    DatabaseStation,
    DatabaseUniversity,
)


class GetChairsResponse(BaseResponse):
    response: "GetChairsResponseModel" = None


class GetCitiesByIdResponse(BaseResponse):
    response: typing.List["BaseObject"] = None


class GetCitiesResponse(BaseResponse):
    response: "GetCitiesResponseModel" = None


class GetCountriesByIdResponse(BaseResponse):
    response: typing.List["BaseCountry"] = None


class GetCountriesResponse(BaseResponse):
    response: "GetCountriesResponseModel" = None


class GetFacultiesResponse(BaseResponse):
    response: "GetFacultiesResponseModel" = None


class GetMetroStationsByIdResponse(BaseResponse):
    response: typing.List["DatabaseStation"] = None


class GetMetroStationsResponse(BaseResponse):
    response: "GetMetroStationsResponseModel" = None


class GetRegionsResponse(BaseResponse):
    response: "GetRegionsResponseModel" = None


class GetSchoolClassesResponse(BaseResponse):
    response: typing.List[list] = None


class GetSchoolsResponse(BaseResponse):
    response: "GetSchoolsResponseModel" = None


class GetUniversitiesResponse(BaseResponse):
    response: "GetUniversitiesResponseModel" = None


class GetChairsResponseModel(BaseResponse):
    count: typing.Optional[int] = None
    items: typing.Optional[typing.List["BaseObject"]] = None


class GetCitiesResponseModel(BaseResponse):
    count: typing.Optional[int] = None
    items: typing.Optional[typing.List["DatabaseCity"]] = None


class GetCountriesResponseModel(BaseResponse):
    count: typing.Optional[int] = None
    items: typing.Optional[typing.List["BaseCountry"]] = None


class GetFacultiesResponseModel(BaseResponse):
    count: typing.Optional[int] = None
    items: typing.Optional[typing.List["DatabaseFaculty"]] = None


class GetMetroStationsResponseModel(BaseResponse):
    count: typing.Optional[int] = None
    items: typing.Optional[typing.List["DatabaseStation"]] = None


class GetRegionsResponseModel(BaseResponse):
    count: typing.Optional[int] = None
    items: typing.Optional[typing.List["DatabaseRegion"]] = None


class GetSchoolsResponseModel(BaseResponse):
    count: typing.Optional[int] = None
    items: typing.Optional[typing.List["DatabaseSchool"]] = None


class GetUniversitiesResponseModel(BaseResponse):
    count: typing.Optional[int] = None
    items: typing.Optional[typing.List["DatabaseUniversity"]] = None


for item in locals().copy().values():
    if inspect.isclass(item) and issubclass(item, BaseResponse):
        item.update_forward_refs()
