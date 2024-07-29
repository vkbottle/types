import typing

from vkbottle_types.base_model import Field
from vkbottle_types.objects import (
    UtilsDomainResolved,
    UtilsLinkChecked,
    UtilsLinkStats,
    UtilsLinkStatsExtended,
    UtilsShortLink,
)
from vkbottle_types.responses.base_response import BaseResponse


class UtilsCheckLinkResponse(BaseResponse):
    response: "UtilsLinkChecked" = Field()


class UtilsGetLastShortenedLinksResponse(BaseResponse):
    response: typing.Dict[str, typing.Any] = Field()


class UtilsGetLinkStatsExtendedResponse(BaseResponse):
    response: "UtilsLinkStatsExtended" = Field()


class UtilsGetLinkStatsResponse(BaseResponse):
    response: "UtilsLinkStats" = Field()


class UtilsGetServerTimeResponse(BaseResponse):
    response: int = Field()


class UtilsGetShortLinkResponse(BaseResponse):
    response: "UtilsShortLink" = Field()


class UtilsResolveScreenNameResponse(BaseResponse):
    response: "UtilsDomainResolved" = Field()
