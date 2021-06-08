import inspect
import typing
from .base_response import BaseResponse
from vkbottle_types.objects import (
    UtilsDomainResolved,
    UtilsLastShortenedLink,
    UtilsLinkChecked,
    UtilsLinkStats,
    UtilsLinkStatsExtended,
    UtilsShortLink
)


class CheckLinkResponse(BaseResponse):
    response: UtilsLinkChecked = None


class GetLastShortenedLinksResponse(BaseResponse):
    response: "GetLastShortenedLinksResponseModel" = None


class GetLinkStatsExtendedResponse(BaseResponse):
    response: UtilsLinkStatsExtended = None


class GetLinkStatsResponse(BaseResponse):
    response: UtilsLinkStats = None


class GetServerTimeResponse(BaseResponse):
    response: int = None


class GetShortLinkResponse(BaseResponse):
    response: UtilsShortLink = None


class ResolveScreenNameResponse(BaseResponse):
    response: UtilsDomainResolved = None


class GetLastShortenedLinksResponseModel(BaseResponse):
    count: typing.Optional[int] = None
    items: typing.Optional[typing.List["UtilsLastShortenedLink"]] = None


for item in locals().copy().values():
    if inspect.isclass(item) and issubclass(item, BaseResponse):
        item.update_forward_refs()
