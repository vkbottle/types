from .base_response import BaseResponse
from vkbottle_types.objects import pages
from typing import Optional, Any, List, Union
import typing


class GetHistoryResponse(BaseResponse):
    response: Optional["GetHistoryResponseModel"] = None


class GetTitlesResponse(BaseResponse):
    response: Optional["GetTitlesResponseModel"] = None


class GetVersionResponse(BaseResponse):
    response: Optional["GetVersionResponseModel"] = None


class GetResponse(BaseResponse):
    response: Optional["GetResponseModel"] = None


class ParseWikiResponse(BaseResponse):
    response: Optional["ParseWikiResponseModel"] = None


class SaveAccessResponse(BaseResponse):
    response: Optional["SaveAccessResponseModel"] = None


class SaveResponse(BaseResponse):
    response: Optional["SaveResponseModel"] = None


GetHistoryResponseModel = List["pages.WikipageHistory"]


GetTitlesResponseModel = List["pages.Wikipage"]


GetVersionResponseModel = Optional["pages.WikipageFull"]


GetResponseModel = Optional["pages.WikipageFull"]


ParseWikiResponseModel = str


SaveAccessResponseModel = int


SaveResponseModel = int
