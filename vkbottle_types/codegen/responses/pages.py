from vkbottle_types.base_model import BaseModel, Field
from vkbottle_types.objects import PagesWikipage, PagesWikipageFull, PagesWikipageHistory
from vkbottle_types.responses.base_response import BaseResponse


class PagesGetHistoryResponse(BaseResponse):
    response: list["PagesWikipageHistory"] = Field()


class PagesGetTitlesResponse(BaseResponse):
    response: list["PagesWikipage"] = Field()


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
    creator_id: int | None = Field(
        default=None,
    )
    parent: str | None = Field(
        default=None,
    )
    parent2: str | None = Field(
        default=None,
    )
    html: str | None = Field(
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


__all__ = (
    "PagesGetHistoryResponse",
    "PagesGetResponse",
    "PagesGetTitlesResponse",
    "PagesGetVersionResponse",
    "PagesGetVersionResponseModel",
    "PagesParseWikiResponse",
    "PagesSaveAccessResponse",
    "PagesSaveResponse",
)
