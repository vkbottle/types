import inspect
import typing
from .base_response import BaseResponse
from vkbottle_types.objects import (
    PagesWikipage,
    PagesWikipageFull,
    PagesWikipageHistory,
)


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


for item in locals().copy().values():
    if inspect.isclass(item) and issubclass(item, BaseResponse):
        item.update_forward_refs()
