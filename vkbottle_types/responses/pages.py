import typing
from typing import Optional

from vkbottle_types.objects import pages
from .base_response import BaseResponse


class GetHistoryResponse(BaseResponse):
    response: Optional[typing.List["pages.WikipageHistory"]] = None


class GetTitlesResponse(BaseResponse):
    response: Optional[typing.List["pages.Wikipage"]] = None


class GetVersionResponse(BaseResponse):
    response: Optional[typing.List["pages.WikipageFull"]] = None


class GetResponse(BaseResponse):
    response: Optional[typing.List["pages.WikipageFull"]] = None


class ParseWikiResponse(BaseResponse):
    response: Optional[str] = None


class SaveAccessResponse(BaseResponse):
    response: Optional[int] = None


class SaveResponse(BaseResponse):
    response: Optional[int] = None
