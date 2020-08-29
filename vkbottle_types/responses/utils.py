import typing
from typing import Optional

from vkbottle_types.objects import utils
from .base_response import BaseResponse


class CheckLinkResponse(BaseResponse):
    response: Optional[typing.List["utils.LinkChecked"]] = None


class GetLastShortenedLinksResponse(BaseResponse):
    response: Optional["GetLastShortenedLinksResponseModel"] = None


class GetLinkStatsExtendedResponse(BaseResponse):
    response: Optional[typing.List["utils.LinkStatsExtended"]] = None


class GetLinkStatsResponse(BaseResponse):
    response: Optional[typing.List["utils.LinkStats"]] = None


class GetServerTimeResponse(BaseResponse):
    response: Optional[int] = None


class GetShortLinkResponse(BaseResponse):
    response: Optional[typing.List["utils.ShortLink"]] = None


class ResolveScreenNameResponse(BaseResponse):
    response: Optional[typing.List["utils.DomainResolved"]] = None


class GetLastShortenedLinksResponseModel(BaseResponse):
    count: Optional[int] = None
    items: Optional[typing.List["utils.LastShortenedLink"]] = None
