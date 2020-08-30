from .base_response import BaseResponse
from vkbottle_types.objects import utils
from typing import Optional, Any, List, Union
import typing


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


CheckLinkResponseModel = Optional["utils.LinkChecked"]


class GetLastShortenedLinksResponseModel(BaseResponse):
    count: Optional[int] = None
    items: Optional[List["utils.LastShortenedLink"]] = None


GetLinkStatsExtendedResponseModel = Optional["utils.LinkStatsExtended"]


GetLinkStatsResponseModel = Optional["utils.LinkStats"]


GetServerTimeResponseModel = int


GetShortLinkResponseModel = Optional["utils.ShortLink"]


ResolveScreenNameResponseModel = Optional["utils.DomainResolved"]
