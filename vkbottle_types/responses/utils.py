import inspect
import typing

from vkbottle_types.objects import (
    UtilsDomainResolved,
    UtilsLastShortenedLink,
    UtilsLinkChecked,
    UtilsLinkStats,
    UtilsLinkStatsExtended,
    UtilsShortLink,
)

from .base_response import BaseResponse


class CheckLinkResponse(BaseResponse):
    response: typing.Optional["CheckLinkResponseModel"] = None


class GetLastShortenedLinksResponse(BaseResponse):
    response: typing.Optional["GetLastShortenedLinksResponseModel"] = None


class GetLinkStatsExtendedResponse(BaseResponse):
    response: typing.Optional["GetLinkStatsExtendedResponseModel"] = None


class GetLinkStatsResponse(BaseResponse):
    response: typing.Optional["GetLinkStatsResponseModel"] = None


class GetServerTimeResponse(BaseResponse):
    response: typing.Optional["GetServerTimeResponseModel"] = None


class GetShortLinkResponse(BaseResponse):
    response: typing.Optional["GetShortLinkResponseModel"] = None


class ResolveScreenNameResponse(BaseResponse):
    response: typing.Optional["ResolveScreenNameResponseModel"] = None


CheckLinkResponseModel = UtilsLinkChecked


class GetLastShortenedLinksResponseModel(BaseResponse):
    count: typing.Optional[int] = None
    items: typing.Optional[typing.List["UtilsLastShortenedLink"]] = None


GetLinkStatsExtendedResponseModel = UtilsLinkStatsExtended


GetLinkStatsResponseModel = UtilsLinkStats


GetServerTimeResponseModel = int


GetShortLinkResponseModel = UtilsShortLink


ResolveScreenNameResponseModel = UtilsDomainResolved


for item in locals().copy().values():
    if inspect.isclass(item) and issubclass(item, BaseResponse):
        item.update_forward_refs()
