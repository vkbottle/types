import typing

from vkbottle_types.objects import (
    UtilsDomainResolved,
    UtilsLastShortenedLink,
    UtilsLinkChecked,
    UtilsLinkStats,
    UtilsLinkStatsExtended,
    UtilsShortLink,
)
from vkbottle_types.responses.base_response import BaseResponse


class CheckLinkResponse(BaseResponse):
    response: UtilsLinkChecked


class GetLastShortenedLinksResponse(BaseResponse):
    response: "GetLastShortenedLinksResponseModel"


class GetLinkStatsExtendedResponse(BaseResponse):
    response: UtilsLinkStatsExtended


class GetLinkStatsResponse(BaseResponse):
    response: UtilsLinkStats


class GetServerTimeResponse(BaseResponse):
    response: int


class GetShortLinkResponse(BaseResponse):
    response: UtilsShortLink


class ResolveScreenNameResponse(BaseResponse):
    response: UtilsDomainResolved


class GetLastShortenedLinksResponseModel(BaseResponse):
    count: typing.Optional[int] = None
    items: typing.Optional[typing.List["UtilsLastShortenedLink"]] = None


__all__ = (
    "CheckLinkResponse",
    "GetLastShortenedLinksResponse",
    "GetLastShortenedLinksResponseModel",
    "GetLinkStatsExtendedResponse",
    "GetLinkStatsResponse",
    "GetServerTimeResponse",
    "GetShortLinkResponse",
    "ResolveScreenNameResponse",
    "UtilsDomainResolved",
    "UtilsLastShortenedLink",
    "UtilsLinkChecked",
    "UtilsLinkStats",
    "UtilsLinkStatsExtended",
    "UtilsShortLink",
)
