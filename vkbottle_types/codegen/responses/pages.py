import typing

from vkbottle_types.base_model import Field
from vkbottle_types.objects import PagesWikipage, PagesWikipageFull, PagesWikipageHistory
from vkbottle_types.responses.base_response import BaseResponse


class PagesGetHistoryResponse(BaseResponse):
    response: typing.List["PagesWikipageHistory"] = Field()


class PagesGetTitlesResponse(BaseResponse):
    response: typing.List["PagesWikipage"] = Field()


class PagesGetVersionResponse(BaseResponse):
    response: "PagesWikipageFull" = Field()


class PagesGetResponse(BaseResponse):
    response: "PagesWikipageFull" = Field()


class PagesParseWikiResponse(BaseResponse):
    response: str = Field()


class PagesSaveAccessResponse(BaseResponse):
    response: int = Field()


class PagesSaveResponse(BaseResponse):
    response: int = Field()
