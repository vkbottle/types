from .base_response import BaseResponse
from vkbottle_types.objects import database, base
from typing import Optional, Any, List, Union
import typing


class GetChairsResponse(BaseResponse):
    response: Optional["GetChairsResponseModel"] = None


class GetCitiesByIdResponse(BaseResponse):
    response: Optional["GetCitiesByIdResponseModel"] = None


class GetCitiesResponse(BaseResponse):
    response: Optional["GetCitiesResponseModel"] = None


class GetCountriesByIdResponse(BaseResponse):
    response: Optional["GetCountriesByIdResponseModel"] = None


class GetCountriesResponse(BaseResponse):
    response: Optional["GetCountriesResponseModel"] = None


class GetFacultiesResponse(BaseResponse):
    response: Optional["GetFacultiesResponseModel"] = None


class GetMetroStationsByIdResponse(BaseResponse):
    response: Optional["GetMetroStationsByIdResponseModel"] = None


class GetMetroStationsResponse(BaseResponse):
    response: Optional["GetMetroStationsResponseModel"] = None


class GetRegionsResponse(BaseResponse):
    response: Optional["GetRegionsResponseModel"] = None


class GetSchoolClassesResponse(BaseResponse):
    response: Optional["GetSchoolClassesResponseModel"] = None


class GetSchoolsResponse(BaseResponse):
    response: Optional["GetSchoolsResponseModel"] = None


class GetUniversitiesResponse(BaseResponse):
    response: Optional["GetUniversitiesResponseModel"] = None


class GetChairsResponseModel(BaseResponse):
    count: Optional[int] = None
    items: Optional[List["base.Object"]] = None


GetCitiesByIdResponseModel = List["base.Object"]


class GetCitiesResponseModel(BaseResponse):
    count: Optional[int] = None
    items: Optional[List["database.City"]] = None


GetCountriesByIdResponseModel = List["base.Country"]


class GetCountriesResponseModel(BaseResponse):
    count: Optional[int] = None
    items: Optional[List["base.Country"]] = None


class GetFacultiesResponseModel(BaseResponse):
    count: Optional[int] = None
    items: Optional[List["database.Faculty"]] = None


GetMetroStationsByIdResponseModel = List["database.Station"]


class GetMetroStationsResponseModel(BaseResponse):
    count: Optional[int] = None
    items: Optional[List["database.Station"]] = None


class GetRegionsResponseModel(BaseResponse):
    count: Optional[int] = None
    items: Optional[List["database.Region"]] = None


GetSchoolClassesResponseModel = List[List[Union[str, int]]]


class GetSchoolsResponseModel(BaseResponse):
    count: Optional[int] = None
    items: Optional[List["database.School"]] = None


class GetUniversitiesResponseModel(BaseResponse):
    count: Optional[int] = None
    items: Optional[List["database.University"]] = None
