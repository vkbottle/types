import typing
from vkbottle_types.responses.base_response import BaseResponse, BaseModel
from vkbottle_types.base_model import Field

from vkbottle_types.objects import (
    UtilsStatsCountry,
    UtilsLinkCheckedStatus,
    UtilsStatsCity,
    UtilsStatsSexAge,
    UtilsStats,
    UtilsStatsExtended,
    UtilsDomainResolvedType,
)


class UtilsDomainResolvedResponseModel(BaseModel):
    object_id: typing.Optional[int] = Field(
        default=None,
        description="Object ID",
    )

    group_id: typing.Optional[int] = Field(
        default=None,
        description="Group ID",
    )

    type: typing.Optional["UtilsDomainResolvedType"] = Field(
        default=None,
    )


class UtilsDomainResolvedResponse(BaseResponse):
    response: "UtilsDomainResolvedResponseModel"


class UtilsDomainResolvedTypeResponseModel(enum.Enum):
    USER = "user"

    GROUP = "group"

    APPLICATION = "application"

    PAGE = "page"

    VK_APP = "vk_app"

    COMMUNITY_APPLICATION = "community_application"


class UtilsDomainResolvedTypeResponse(BaseResponse):
    response: "UtilsDomainResolvedTypeResponseModel"


class UtilsLastShortenedLinkResponseModel(BaseModel):
    access_key: typing.Optional[str] = Field(
        default=None,
        description="Access key for private stats",
    )

    key: typing.Optional[str] = Field(
        default=None,
        description="Link key (characters after vk.cc/)",
    )

    short_url: typing.Optional[str] = Field(
        default=None,
        description="Short link URL",
    )

    timestamp: typing.Optional[int] = Field(
        default=None,
        description="Creation time in Unixtime",
    )

    url: typing.Optional[str] = Field(
        default=None,
        description="Full URL",
    )

    views: typing.Optional[int] = Field(
        default=None,
        description="Total views number",
    )


class UtilsLastShortenedLinkResponse(BaseResponse):
    response: "UtilsLastShortenedLinkResponseModel"


class UtilsLinkCheckedResponseModel(BaseModel):
    link: typing.Optional[str] = Field(
        default=None,
        description="Link URL",
    )

    status: typing.Optional["UtilsLinkCheckedStatus"] = Field(
        default=None,
    )


class UtilsLinkCheckedResponse(BaseResponse):
    response: "UtilsLinkCheckedResponseModel"


class UtilsLinkCheckedStatusResponseModel(enum.Enum):
    NOT_BANNED = "not_banned"

    BANNED = "banned"

    PROCESSING = "processing"


class UtilsLinkCheckedStatusResponse(BaseResponse):
    response: "UtilsLinkCheckedStatusResponseModel"


class UtilsLinkStatsResponseModel(BaseModel):
    key: typing.Optional[str] = Field(
        default=None,
        description="Link key (characters after vk.cc/)",
    )

    stats: typing.Optional[typing.List[UtilsStats]] = Field(
        default=None,
    )


class UtilsLinkStatsResponse(BaseResponse):
    response: "UtilsLinkStatsResponseModel"


class UtilsLinkStatsExtendedResponseModel(BaseModel):
    key: typing.Optional[str] = Field(
        default=None,
        description="Link key (characters after vk.cc/)",
    )

    stats: typing.Optional[typing.List[UtilsStatsExtended]] = Field(
        default=None,
    )


class UtilsLinkStatsExtendedResponse(BaseResponse):
    response: "UtilsLinkStatsExtendedResponseModel"


class UtilsShortLinkResponseModel(BaseModel):
    access_key: typing.Optional[str] = Field(
        default=None,
        description="Access key for private stats",
    )

    key: typing.Optional[str] = Field(
        default=None,
        description="Link key (characters after vk.cc/)",
    )

    short_url: typing.Optional[str] = Field(
        default=None,
        description="Short link URL",
    )

    url: typing.Optional[str] = Field(
        default=None,
        description="Full URL",
    )


class UtilsShortLinkResponse(BaseResponse):
    response: "UtilsShortLinkResponseModel"


class UtilsStatsResponseModel(BaseModel):
    timestamp: typing.Optional[int] = Field(
        default=None,
        description="Start time",
    )

    views: typing.Optional[int] = Field(
        default=None,
        description="Total views number",
    )


class UtilsStatsResponse(BaseResponse):
    response: "UtilsStatsResponseModel"


class UtilsStatsCityResponseModel(BaseModel):
    city_id: typing.Optional[int] = Field(
        default=None,
        description="City ID",
    )

    views: typing.Optional[int] = Field(
        default=None,
        description="Views number",
    )


class UtilsStatsCityResponse(BaseResponse):
    response: "UtilsStatsCityResponseModel"


class UtilsStatsCountryResponseModel(BaseModel):
    country_id: typing.Optional[int] = Field(
        default=None,
        description="Country ID",
    )

    views: typing.Optional[int] = Field(
        default=None,
        description="Views number",
    )


class UtilsStatsCountryResponse(BaseResponse):
    response: "UtilsStatsCountryResponseModel"


class UtilsStatsExtendedResponseModel(BaseModel):
    cities: typing.Optional[typing.List[UtilsStatsCity]] = Field(
        default=None,
    )

    countries: typing.Optional[typing.List[UtilsStatsCountry]] = Field(
        default=None,
    )

    sex_age: typing.Optional[typing.List[UtilsStatsSexAge]] = Field(
        default=None,
    )

    timestamp: typing.Optional[int] = Field(
        default=None,
        description="Start time",
    )

    views: typing.Optional[int] = Field(
        default=None,
        description="Total views number",
    )


class UtilsStatsExtendedResponse(BaseResponse):
    response: "UtilsStatsExtendedResponseModel"


class UtilsStatsSexAgeResponseModel(BaseModel):
    age_range: typing.Optional[str] = Field(
        default=None,
        description="Age denotation",
    )

    female: typing.Optional[int] = Field(
        default=None,
        description=" Views by female users",
    )

    male: typing.Optional[int] = Field(
        default=None,
        description=" Views by male users",
    )


class UtilsStatsSexAgeResponse(BaseResponse):
    response: "UtilsStatsSexAgeResponseModel"
