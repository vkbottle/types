import typing
from typing import Optional

from vkbottle_types.objects import database, base
from .base_response import BaseResponse


class GetChairsResponse(BaseResponse):
    response: Optional["GetChairsResponseModel"] = None


class GetCitiesByIdResponse(BaseResponse):
    response: Optional[typing.List["base.Object"]] = None


class GetCitiesResponse(BaseResponse):
    response: Optional["GetCitiesResponseModel"] = None


class GetCountriesByIdResponse(BaseResponse):
    response: Optional[typing.List["base.Country"]] = None


class GetCountriesResponse(BaseResponse):
    response: Optional["GetCountriesResponseModel"] = None


class GetFacultiesResponse(BaseResponse):
    response: Optional["GetFacultiesResponseModel"] = None


class GetMetroStationsByIdResponse(BaseResponse):
    response: Optional[typing.List["database.Station"]] = None


class GetMetroStationsResponse(BaseResponse):
    response: Optional["GetMetroStationsResponseModel"] = None


class GetRegionsResponse(BaseResponse):
    response: Optional["GetRegionsResponseModel"] = None


class GetSchoolClassesResponse(BaseResponse):
    response: Optional[typing.List[typing.Union[str, int]]] = None


class GetSchoolsResponse(BaseResponse):
    response: Optional["GetSchoolsResponseModel"] = None


class GetUniversitiesResponse(BaseResponse):
    response: Optional["GetUniversitiesResponseModel"] = None


class GetChairsResponseModel(BaseResponse):
    count: Optional[int] = None
    items: Optional[typing.List["base.Object"]] = None


class GetCitiesResponseModel(BaseResponse):
    count: Optional[int] = None
    items: Optional[typing.List["database.City"]] = None


class GetCountriesResponseModel(BaseResponse):
    count: Optional[int] = None
    items: Optional[typing.List["base.Country"]] = None


class GetFacultiesResponseModel(BaseResponse):
    count: Optional[int] = None
    items: Optional[typing.List["database.Faculty"]] = None


class GetMetroStationsResponseModel(BaseResponse):
    count: Optional[int] = None
    items: Optional[typing.List["database.Station"]] = None


class GetRegionsResponseModel(BaseResponse):
    count: Optional[int] = None
    items: Optional[typing.List["database.Region"]] = None


class GetSchoolsResponseModel(BaseResponse):
    count: Optional[int] = None
    items: Optional[typing.List["database.School"]] = None


class GetUniversitiesResponseModel(BaseResponse):
    count: Optional[int] = None
    items: Optional[typing.List["database.University"]] = None
