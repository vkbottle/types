import typing
import enum
from vkbottle_types.responses.base_response import BaseResponse, BaseModel
from vkbottle_types.base_model import Field

from vkbottle_types.objects import BaseBoolInt


class DatabaseCityResponseModel(BaseObject):
    area: typing.Optional[str] = Field(
        default=None,
        description="Area title",
    )

    region: typing.Optional[str] = Field(
        default=None,
        description="Region title",
    )

    country: typing.Optional[str] = Field(
        default=None,
        description="Country title",
    )

    important: typing.Optional[bool] = Field(
        default=None,
        description="Information whether the city is included in important cities list",
    )


class DatabaseCityResponse(BaseResponse):
    response: "DatabaseCityResponseModel"


class DatabaseCityByIdResponseModel(BaseModel):
    pass


class DatabaseCityByIdResponse(BaseResponse):
    response: "DatabaseCityByIdResponseModel"


class DatabaseFacultyResponseModel(BaseModel):
    id: typing.Optional[int] = Field(
        default=None,
        description="Faculty ID",
    )

    title: typing.Optional[str] = Field(
        default=None,
        description="Faculty title",
    )


class DatabaseFacultyResponse(BaseResponse):
    response: "DatabaseFacultyResponseModel"


class DatabaseLanguageFullResponseModel(BaseModel):
    id: int = Field(
        description="Language ID",
    )

    native_name: str = Field(
        description="Language native name",
    )


class DatabaseLanguageFullResponse(BaseResponse):
    response: "DatabaseLanguageFullResponseModel"


class DatabaseRegionResponseModel(BaseModel):
    id: typing.Optional[int] = Field(
        default=None,
        description="Region ID",
    )

    title: typing.Optional[str] = Field(
        default=None,
        description="Region title",
    )


class DatabaseRegionResponse(BaseResponse):
    response: "DatabaseRegionResponseModel"


class DatabaseSchoolResponseModel(BaseModel):
    id: typing.Optional[int] = Field(
        default=None,
        description="School ID",
    )

    title: typing.Optional[str] = Field(
        default=None,
        description="School title",
    )


class DatabaseSchoolResponse(BaseResponse):
    response: "DatabaseSchoolResponseModel"


class DatabaseSchoolClassResponseModel(BaseModel):
    pass


class DatabaseSchoolClassResponse(BaseResponse):
    response: "DatabaseSchoolClassResponseModel"


class DatabaseStationResponseModel(BaseModel):
    id: int = Field(
        description="Station ID",
    )

    name: str = Field(
        description="Station name",
    )

    city_id: typing.Optional[int] = Field(
        default=None,
        description="City ID",
    )

    color: typing.Optional[str] = Field(
        default=None,
        description="Hex color code without #",
    )


class DatabaseStationResponse(BaseResponse):
    response: "DatabaseStationResponseModel"


class DatabaseUniversityResponseModel(BaseModel):
    id: typing.Optional[int] = Field(
        default=None,
        description="University ID",
    )

    title: typing.Optional[str] = Field(
        default=None,
        description="University title",
    )


class DatabaseUniversityResponse(BaseResponse):
    response: "DatabaseUniversityResponseModel"
