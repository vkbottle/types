import typing

from vkbottle_types.methods.base_category import BaseCategory
from vkbottle_types.objects import *
from vkbottle_types.responses.base import (
    BaseOkResponse,
    BaseOkResponseModel,
)
from vkbottle_types.responses.pages import *  # noqa: F401,F403  # type: ignore


class PagesCategory(BaseCategory):
    async def clear_cache(
        self,
        url: str,
        **kwargs: typing.Any,
    ) -> BaseOkResponseModel:
        """Method `pages.clearCache()`

        :param url: Address of the page where you need to refesh the cached version
        """

        params = self.get_set_params(locals())
        response = await self.api.request("pages.clearCache", params)
        model = BaseOkResponse
        return model(**response).response

    async def get(
        self,
        global_: bool | None = None,
        need_html: bool | None = None,
        need_source: bool | None = None,
        owner_id: int | None = None,
        page_id: int | None = None,
        site_preview: bool | None = None,
        title: str | None = None,
        **kwargs: typing.Any,
    ) -> "PagesWikipageFull":
        """Method `pages.get()`

        :param global: '1' - to return information about a global wiki page
        :param need_html: '1' - to return the page as HTML,
        :param need_source:
        :param owner_id: Page owner ID.
        :param page_id: Wiki page ID.
        :param site_preview: '1' - resulting wiki page is a preview for the attached link
        :param title: Wiki page title.
        """

        params = self.get_set_params(locals())
        response = await self.api.request("pages.get", params)
        model = PagesGetResponse
        return model(**response).response

    async def get_history(
        self,
        page_id: int,
        group_id: int | None = None,
        user_id: int | None = None,
        **kwargs: typing.Any,
    ) -> list[PagesWikipageHistory]:
        """Method `pages.getHistory()`

        :param page_id: Wiki page ID.
        :param group_id: ID of the community that owns the wiki page.
        :param user_id:
        """

        params = self.get_set_params(locals())
        response = await self.api.request("pages.getHistory", params)
        model = PagesGetHistoryResponse
        return model(**response).response

    async def get_titles(
        self,
        group_id: int | None = None,
        **kwargs: typing.Any,
    ) -> list[PagesWikipage]:
        """Method `pages.getTitles()`

        :param group_id: ID of the community that owns the wiki page.
        """

        params = self.get_set_params(locals())
        response = await self.api.request("pages.getTitles", params)
        model = PagesGetTitlesResponse
        return model(**response).response

    async def get_version(
        self,
        version_id: int,
        group_id: int | None = None,
        need_html: bool | None = None,
        user_id: int | None = None,
        **kwargs: typing.Any,
    ) -> PagesGetVersionResponseModel:
        """Method `pages.getVersion()`

        :param version_id:
        :param group_id: ID of the community that owns the wiki page.
        :param need_html: '1' - to return the page as HTML
        :param user_id:
        """

        params = self.get_set_params(locals())
        response = await self.api.request("pages.getVersion", params)
        model = PagesGetVersionResponse
        return model(**response).response

    async def parse_wiki(
        self,
        text: str,
        group_id: int | None = None,
        **kwargs: typing.Any,
    ) -> str:
        """Method `pages.parseWiki()`

        :param text: Text of the wiki page.
        :param group_id: ID of the group in the context of which this markup is interpreted.
        """

        params = self.get_set_params(locals())
        response = await self.api.request("pages.parseWiki", params)
        model = PagesParseWikiResponse
        return model(**response).response

    async def save(
        self,
        group_id: int | None = None,
        page_id: int | None = None,
        text: str | None = None,
        title: str | None = None,
        user_id: int | None = None,
        **kwargs: typing.Any,
    ) -> int:
        """Method `pages.save()`

        :param group_id: ID of the community that owns the wiki page.
        :param page_id: Wiki page ID. The 'title' parameter can be passed instead of 'pid'.
        :param text: Text of the wiki page in wiki-format.
        :param title: Wiki page title.
        :param user_id: User ID
        """

        params = self.get_set_params(locals())
        response = await self.api.request("pages.save", params)
        model = PagesSaveResponse
        return model(**response).response

    async def save_access(
        self,
        page_id: int,
        edit: int | None = None,
        group_id: int | None = None,
        user_id: int | None = None,
        view: int | None = None,
        **kwargs: typing.Any,
    ) -> int:
        """Method `pages.saveAccess()`

        :param page_id: Wiki page ID.
        :param edit: Who can edit the wiki page: '1' - only community members, '2' - all users can edit the page, '0' - only community managers
        :param group_id: ID of the community that owns the wiki page.
        :param user_id:
        :param view: Who can view the wiki page: '1' - only community members, '2' - all users can view the page, '0' - only community managers
        """

        params = self.get_set_params(locals())
        response = await self.api.request("pages.saveAccess", params)
        model = PagesSaveAccessResponse
        return model(**response).response


__all__ = ("PagesCategory",)
