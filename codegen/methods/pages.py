import typing

from vkbottle_types.methods.base_category import BaseCategory
from vkbottle_types.objects import PagesWikipage, PagesWikipageFull, PagesWikipageHistory
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
        global_: typing.Optional[bool] = None,
        need_html: typing.Optional[bool] = None,
        need_source: typing.Optional[bool] = None,
        owner_id: typing.Optional[int] = None,
        page_id: typing.Optional[int] = None,
        site_preview: typing.Optional[bool] = None,
        title: typing.Optional[str] = None,
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
        group_id: typing.Optional[int] = None,
        user_id: typing.Optional[int] = None,
        **kwargs: typing.Any,
    ) -> typing.List[PagesWikipageHistory]:
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
        group_id: typing.Optional[int] = None,
        **kwargs: typing.Any,
    ) -> typing.List[PagesWikipage]:
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
        group_id: typing.Optional[int] = None,
        need_html: typing.Optional[bool] = None,
        user_id: typing.Optional[int] = None,
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
        group_id: typing.Optional[int] = None,
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
        group_id: typing.Optional[int] = None,
        page_id: typing.Optional[int] = None,
        text: typing.Optional[str] = None,
        title: typing.Optional[str] = None,
        user_id: typing.Optional[int] = None,
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
        edit: typing.Optional[int] = None,
        group_id: typing.Optional[int] = None,
        user_id: typing.Optional[int] = None,
        view: typing.Optional[int] = None,
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
