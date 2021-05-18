import inspect
import typing

from vkbottle_types.objects import (
    PagesWikipage,
    PagesWikipageFull,
    PagesWikipageHistory,
)

from .base_response import BaseResponse


class GetHistoryResponse(BaseResponse):
    response: typing.Optional["GetHistoryResponseModel"] = None


class GetTitlesResponse(BaseResponse):
    response: typing.Optional["GetTitlesResponseModel"] = None


class GetVersionResponse(BaseResponse):
    response: typing.Optional["GetVersionResponseModel"] = None


class GetResponse(BaseResponse):
    response: typing.Optional["GetResponseModel"] = None


class ParseWikiResponse(BaseResponse):
    response: typing.Optional["ParseWikiResponseModel"] = None


class SaveAccessResponse(BaseResponse):
    response: typing.Optional["SaveAccessResponseModel"] = None


class SaveResponse(BaseResponse):
    response: typing.Optional["SaveResponseModel"] = None


GetHistoryResponseModel = typing.List[PagesWikipageHistory]


GetTitlesResponseModel = typing.List[PagesWikipage]


GetVersionResponseModel = PagesWikipageFull


GetResponseModel = PagesWikipageFull


ParseWikiResponseModel = str


SaveAccessResponseModel = int


SaveResponseModel = int


for item in locals().copy().values():
    if inspect.isclass(item) and issubclass(item, BaseResponse):
        item.update_forward_refs()
