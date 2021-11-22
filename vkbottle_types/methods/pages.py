import typing
from .base_category import BaseCategory
from vkbottle_types.responses.base import OkResponse
from vkbottle_types.responses.pages import (
    GetHistoryResponse,
    GetResponse,
    GetTitlesResponse,
    GetVersionResponse,
    PagesWikipage,
    PagesWikipageFull,
    PagesWikipageHistory,
    ParseWikiResponse,
    SaveAccessResponse,
    SaveResponse
)


class PagesCategory(BaseCategory):
    async def clear_cache(
        self, url: str, **kwargs
    ) -> int:
        """Allows to clear the cache of particular 'external' pages which may be attached to VK posts.

        :param url: Address of the page where you need to refesh the cached version
        """

        params = self.get_set_params(locals())
        response = await self.api.request("pages.clearCache", params)
        model = OkResponse
        return model(**response).response

    async def get(
        self,
        owner_id: typing.Optional[int] = None,
        page_id: typing.Optional[int] = None,
        _global: typing.Optional[bool] = None,
        site_preview: typing.Optional[bool] = None,
        title: typing.Optional[str] = None,
        need_source: typing.Optional[bool] = None,
        need_html: typing.Optional[bool] = None,
        **kwargs
    ) -> PagesWikipageFull:
        """Returns information about a wiki page.

        :param owner_id: Page owner ID.
        :param page_id: Wiki page ID.
        :param _global: '1' — to return information about a global wiki page
        :param site_preview: '1' — resulting wiki page is a preview for the attached link
        :param title: Wiki page title.
        :param need_source:
        :param need_html: '1' — to return the page as HTML,
        """

        params = self.get_set_params(locals())
        response = await self.api.request("pages.get", params)
        model = GetResponse
        return model(**response).response

    async def get_history(
        self,
        page_id: int,
        group_id: typing.Optional[int] = None,
        user_id: typing.Optional[int] = None,
        **kwargs
    ) -> typing.List[PagesWikipageHistory]:
        """Returns a list of all previous versions of a wiki page.

        :param page_id: Wiki page ID.
        :param group_id: ID of the community that owns the wiki page.
        :param user_id:
        """

        params = self.get_set_params(locals())
        response = await self.api.request("pages.getHistory", params)
        model = GetHistoryResponse
        return model(**response).response

    async def get_titles(
        self, group_id: typing.Optional[int] = None, **kwargs
    ) -> typing.List[PagesWikipage]:
        """Returns a list of wiki pages in a group.

        :param group_id: ID of the community that owns the wiki page.
        """

        params = self.get_set_params(locals())
        response = await self.api.request("pages.getTitles", params)
        model = GetTitlesResponse
        return model(**response).response

    async def get_version(
        self,
        version_id: int,
        group_id: typing.Optional[int] = None,
        user_id: typing.Optional[int] = None,
        need_html: typing.Optional[bool] = None,
        **kwargs
    ) -> PagesWikipageFull:
        """Returns the text of one of the previous versions of a wiki page.

        :param version_id:
        :param group_id: ID of the community that owns the wiki page.
        :param user_id:
        :param need_html: '1' — to return the page as HTML
        """

        params = self.get_set_params(locals())
        response = await self.api.request("pages.getVersion", params)
        model = GetVersionResponse
        return model(**response).response

    async def parse_wiki(
        self, text: str, group_id: typing.Optional[int] = None, **kwargs
    ) -> str:
        """Returns HTML representation of the wiki markup.

        :param text: Text of the wiki page.
        :param group_id: ID of the group in the context of which this markup is interpreted.
        """

        params = self.get_set_params(locals())
        response = await self.api.request("pages.parseWiki", params)
        model = ParseWikiResponse
        return model(**response).response

    async def save(
        self,
        text: typing.Optional[str] = None,
        page_id: typing.Optional[int] = None,
        group_id: typing.Optional[int] = None,
        user_id: typing.Optional[int] = None,
        title: typing.Optional[str] = None,
        **kwargs
    ) -> int:
        """Saves the text of a wiki page.

        :param text: Text of the wiki page in wiki-format.
        :param page_id: Wiki page ID. The 'title' parameter can be passed instead of 'pid'.
        :param group_id: ID of the community that owns the wiki page.
        :param user_id: User ID
        :param title: Wiki page title.
        """

        params = self.get_set_params(locals())
        response = await self.api.request("pages.save", params)
        model = SaveResponse
        return model(**response).response

    async def save_access(
        self,
        page_id: int,
        group_id: typing.Optional[int] = None,
        user_id: typing.Optional[int] = None,
        view: typing.Optional[int] = None,
        edit: typing.Optional[int] = None,
        **kwargs
    ) -> int:
        """Saves modified read and edit access settings for a wiki page.

        :param page_id: Wiki page ID.
        :param group_id: ID of the community that owns the wiki page.
        :param user_id:
        :param view: Who can view the wiki page: '1' — only community members, '2' — all users can view the page, '0' — only community managers
        :param edit: Who can edit the wiki page: '1' — only community members, '2' — all users can edit the page, '0' — only community managers
        """

        params = self.get_set_params(locals())
        response = await self.api.request("pages.saveAccess", params)
        model = SaveAccessResponse
        return model(**response).response
