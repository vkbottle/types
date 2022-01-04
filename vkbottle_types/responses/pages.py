import inspect
import typing
from .base_response import BaseResponse
from vkbottle_types.objects import (
    PagesWikipage,
    PagesWikipageFull,
    PagesWikipageHistory,
)


class GetHistoryResponse(BaseResponse):
    response: typing.List["PagesWikipageHistory"] = None


class GetTitlesResponse(BaseResponse):
    response: typing.List["PagesWikipage"] = None


class GetVersionResponse(BaseResponse):
    response: PagesWikipageFull = None


class GetResponse(BaseResponse):
    response: PagesWikipageFull = None


class ParseWikiResponse(BaseResponse):
    response: str = None


class SaveAccessResponse(BaseResponse):
    response: int = None


class SaveResponse(BaseResponse):
    response: int = None


for item in locals().copy().values():
    if inspect.isclass(item) and issubclass(item, BaseResponse):
        item.update_forward_refs()
