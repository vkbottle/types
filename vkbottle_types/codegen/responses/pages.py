import typing

from vkbottle_types.objects import (
    PagesWikipage,
    PagesWikipageFull,
    PagesWikipageHistory,
)
from vkbottle_types.responses.base_response import BaseResponse


class GetHistoryResponse(BaseResponse):
    response: typing.List["PagesWikipageHistory"]


class GetTitlesResponse(BaseResponse):
    response: typing.List["PagesWikipage"]


class GetVersionResponse(BaseResponse):
    response: PagesWikipageFull


class GetResponse(BaseResponse):
    response: PagesWikipageFull


class ParseWikiResponse(BaseResponse):
    response: str


class SaveAccessResponse(BaseResponse):
    response: int


class SaveResponse(BaseResponse):
    response: int


__all__ = (
    "GetHistoryResponse",
    "GetResponse",
    "GetTitlesResponse",
    "GetVersionResponse",
    "PagesWikipage",
    "PagesWikipageFull",
    "PagesWikipageHistory",
    "ParseWikiResponse",
    "SaveAccessResponse",
    "SaveResponse",
)
