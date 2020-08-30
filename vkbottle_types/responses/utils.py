from typing import Optional, List

from vkbottle_types.objects import (
    UtilsLinkStatsExtended,
    UtilsLinkChecked,
    UtilsShortLink,
    UtilsLinkStats,
    UtilsLastShortenedLink,
    UtilsDomainResolved,
)
from .base_response import BaseResponse


class CheckLinkResponse(BaseResponse):
    response: Optional["CheckLinkResponseModel"] = None


class GetLastShortenedLinksResponse(BaseResponse):
    response: Optional["GetLastShortenedLinksResponseModel"] = None


class GetLinkStatsExtendedResponse(BaseResponse):
    response: Optional["GetLinkStatsExtendedResponseModel"] = None


class GetLinkStatsResponse(BaseResponse):
    response: Optional["GetLinkStatsResponseModel"] = None


class GetServerTimeResponse(BaseResponse):
    response: Optional["GetServerTimeResponseModel"] = None


class GetShortLinkResponse(BaseResponse):
    response: Optional["GetShortLinkResponseModel"] = None


class ResolveScreenNameResponse(BaseResponse):
    response: Optional["ResolveScreenNameResponseModel"] = None


CheckLinkResponseModel = Optional[UtilsLinkChecked]


class GetLastShortenedLinksResponseModel(BaseResponse):
    count: Optional[int] = None
    items: Optional[List["UtilsLastShortenedLink"]] = None


GetLinkStatsExtendedResponseModel = Optional[UtilsLinkStatsExtended]

GetLinkStatsResponseModel = Optional[UtilsLinkStats]


GetServerTimeResponseModel = int

GetShortLinkResponseModel = Optional[UtilsShortLink]

ResolveScreenNameResponseModel = Optional[UtilsDomainResolved]

CheckLinkResponse.update_forward_refs()
GetLastShortenedLinksResponse.update_forward_refs()
GetLinkStatsExtendedResponse.update_forward_refs()
GetLinkStatsResponse.update_forward_refs()
GetServerTimeResponse.update_forward_refs()
GetShortLinkResponse.update_forward_refs()
ResolveScreenNameResponse.update_forward_refs()
