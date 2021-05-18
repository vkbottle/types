import inspect
import typing

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

from .base_response import BaseResponse


class GetChairsResponse(BaseResponse):
    response: typing.Optional["GetChairsResponseModel"] = None


class GetCitiesByIdResponse(BaseResponse):
    response: typing.Optional["GetCitiesByIdResponseModel"] = None


class GetCitiesResponse(BaseResponse):
    response: typing.Optional["GetCitiesResponseModel"] = None


class GetCountriesByIdResponse(BaseResponse):
    response: typing.Optional["GetCountriesByIdResponseModel"] = None


class GetCountriesResponse(BaseResponse):
    response: typing.Optional["GetCountriesResponseModel"] = None


class GetFacultiesResponse(BaseResponse):
    response: typing.Optional["GetFacultiesResponseModel"] = None


class GetMetroStationsByIdResponse(BaseResponse):
    response: typing.Optional["GetMetroStationsByIdResponseModel"] = None


class GetMetroStationsResponse(BaseResponse):
    response: typing.Optional["GetMetroStationsResponseModel"] = None


class GetRegionsResponse(BaseResponse):
    response: typing.Optional["GetRegionsResponseModel"] = None


class GetSchoolClassesResponse(BaseResponse):
    response: typing.Optional["GetSchoolClassesResponseModel"] = None


class GetSchoolsResponse(BaseResponse):
    response: typing.Optional["GetSchoolsResponseModel"] = None


class GetUniversitiesResponse(BaseResponse):
    response: typing.Optional["GetUniversitiesResponseModel"] = None


class GetChairsResponseModel(BaseResponse):
    count: typing.Optional[int] = None
    items: typing.Optional[typing.List["BaseObject"]] = None


GetCitiesByIdResponseModel = typing.List[BaseObject]


class GetCitiesResponseModel(BaseResponse):
    count: typing.Optional[int] = None
    items: typing.Optional[typing.List["DatabaseCity"]] = None


GetCountriesByIdResponseModel = typing.List[BaseCountry]


class GetCountriesResponseModel(BaseResponse):
    count: typing.Optional[int] = None
    items: typing.Optional[typing.List["BaseCountry"]] = None


class GetFacultiesResponseModel(BaseResponse):
    count: typing.Optional[int] = None
    items: typing.Optional[typing.List["DatabaseFaculty"]] = None


GetMetroStationsByIdResponseModel = typing.List[DatabaseStation]


class GetMetroStationsResponseModel(BaseResponse):
    count: typing.Optional[int] = None
    items: typing.Optional[typing.List["DatabaseStation"]] = None


class GetRegionsResponseModel(BaseResponse):
    count: typing.Optional[int] = None
    items: typing.Optional[typing.List["DatabaseRegion"]] = None


GetSchoolClassesResponseModel = typing.List["list"]


class GetSchoolsResponseModel(BaseResponse):
    count: typing.Optional[int] = None
    items: typing.Optional[typing.List["DatabaseSchool"]] = None


class GetUniversitiesResponseModel(BaseResponse):
    count: typing.Optional[int] = None
    items: typing.Optional[typing.List["DatabaseUniversity"]] = None


for item in locals().copy().values():
    if inspect.isclass(item) and issubclass(item, BaseResponse):
        item.update_forward_refs()
