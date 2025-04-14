import typing

from vkbottle_types.base_model import BaseModel, Field
from vkbottle_types.objects import PagesWikipage, PagesWikipageFull, PagesWikipageHistory
from vkbottle_types.responses.base_response import BaseResponse


class PagesGetHistoryResponse(BaseResponse):
    response: typing.List["PagesWikipageHistory"] = Field()


class PagesGetTitlesResponse(BaseResponse):
    response: typing.List["PagesWikipage"] = Field()


class PagesGetVersionResponseModel(BaseModel):
    id: int = Field()
    page_id: int = Field()
    group_id: int = Field()
    title: str = Field()
    source: str = Field()
    current_user_can_edit: int = Field()
    who_can_view: int = Field()
    who_can_edit: int = Field()
    version_created: int = Field()
    creator_id: typing.Optional[int] = Field(
        default=None,
    )
    parent: typing.Optional[str] = Field(
        default=None,
    )
    parent2: typing.Optional[str] = Field(
        default=None,
    )
    html: typing.Optional[str] = Field(
        default=None,
    )


class PagesGetVersionResponse(BaseResponse):
    response: "PagesGetVersionResponseModel" = Field()


class PagesGetResponse(BaseResponse):
    response: "PagesWikipageFull" = Field()


class PagesParseWikiResponse(BaseResponse):
    response: str = Field()


class PagesSaveAccessResponse(BaseResponse):
    response: int = Field()


class PagesSaveResponse(BaseResponse):
    response: int = Field()
