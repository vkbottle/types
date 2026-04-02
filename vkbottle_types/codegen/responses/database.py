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
    items: list["BaseObject"] = Field()


class DatabaseGetChairsResponse(BaseResponse):
    response: "DatabaseGetChairsResponseModel" = Field()


class DatabaseGetCitiesByIdResponse(BaseResponse):
    response: list["DatabaseCityById"] = Field()


class DatabaseGetCitiesResponseModel(BaseModel):
    count: int = Field()
    items: list["DatabaseCity"] = Field()


class DatabaseGetCitiesResponse(BaseResponse):
    response: "DatabaseGetCitiesResponseModel" = Field()


class DatabaseGetCountriesByIdResponse(BaseResponse):
    response: list["BaseCountry"] = Field()


class DatabaseGetCountriesResponseModel(BaseModel):
    count: int = Field()
    items: list["BaseCountry"] = Field()


class DatabaseGetCountriesResponse(BaseResponse):
    response: "DatabaseGetCountriesResponseModel" = Field()


class DatabaseGetFacultiesResponseModel(BaseModel):
    count: int = Field()
    items: list["DatabaseFaculty"] = Field()


class DatabaseGetFacultiesResponse(BaseResponse):
    response: "DatabaseGetFacultiesResponseModel" = Field()


class DatabaseGetMetroStationsByIdResponse(BaseResponse):
    response: list["DatabaseStation"] = Field()


class DatabaseGetMetroStationsResponseModel(BaseModel):
    count: int = Field()
    items: list["DatabaseStation"] = Field()


class DatabaseGetMetroStationsResponse(BaseResponse):
    response: "DatabaseGetMetroStationsResponseModel" = Field()


class DatabaseGetRegionsResponseModel(BaseModel):
    count: int = Field()
    items: list["DatabaseRegion"] = Field()


class DatabaseGetRegionsResponse(BaseResponse):
    response: "DatabaseGetRegionsResponseModel" = Field()


class DatabaseGetSchoolClassesNewResponse(BaseResponse):
    response: list["DatabaseSchoolClass"] = Field()


class DatabaseGetSchoolsResponseModel(BaseModel):
    count: int = Field()
    items: list["DatabaseSchool"] = Field()


class DatabaseGetSchoolsResponse(BaseResponse):
    response: "DatabaseGetSchoolsResponseModel" = Field()


class DatabaseGetUniversitiesResponseModel(BaseModel):
    count: int = Field()
    items: list["DatabaseUniversity"] = Field()


class DatabaseGetUniversitiesResponse(BaseResponse):
    response: "DatabaseGetUniversitiesResponseModel" = Field()


__all__ = (
    "DatabaseGetChairsResponse",
    "DatabaseGetChairsResponseModel",
    "DatabaseGetCitiesByIdResponse",
    "DatabaseGetCitiesResponse",
    "DatabaseGetCitiesResponseModel",
    "DatabaseGetCountriesByIdResponse",
    "DatabaseGetCountriesResponse",
    "DatabaseGetCountriesResponseModel",
    "DatabaseGetFacultiesResponse",
    "DatabaseGetFacultiesResponseModel",
    "DatabaseGetMetroStationsByIdResponse",
    "DatabaseGetMetroStationsResponse",
    "DatabaseGetMetroStationsResponseModel",
    "DatabaseGetRegionsResponse",
    "DatabaseGetRegionsResponseModel",
    "DatabaseGetSchoolClassesNewResponse",
    "DatabaseGetSchoolsResponse",
    "DatabaseGetSchoolsResponseModel",
    "DatabaseGetUniversitiesResponse",
    "DatabaseGetUniversitiesResponseModel",
)
