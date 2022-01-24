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
    response: "GetChairsResponseModel"


class GetCitiesByIdResponse(BaseResponse):
    response: typing.List["BaseObject"]


class GetCitiesResponse(BaseResponse):
    response: "GetCitiesResponseModel"


class GetCountriesByIdResponse(BaseResponse):
    response: typing.List["BaseCountry"]


class GetCountriesResponse(BaseResponse):
    response: "GetCountriesResponseModel"


class GetFacultiesResponse(BaseResponse):
    response: "GetFacultiesResponseModel"


class GetMetroStationsByIdResponse(BaseResponse):
    response: typing.List["DatabaseStation"]


class GetMetroStationsResponse(BaseResponse):
    response: "GetMetroStationsResponseModel"


class GetRegionsResponse(BaseResponse):
    response: "GetRegionsResponseModel"


class GetSchoolClassesResponse(BaseResponse):
    response: typing.List[list]


class GetSchoolsResponse(BaseResponse):
    response: "GetSchoolsResponseModel"


class GetUniversitiesResponse(BaseResponse):
    response: "GetUniversitiesResponseModel"


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
