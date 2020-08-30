from typing import Optional

from vkbottle_types.responses import pages, base
from .base_category import BaseCategory


class PagesCategory(BaseCategory):
    async def clear_cache(self, url: str, **kwargs) -> base.OkResponseModel:
        """Allows to clear the cache of particular 'external' pages which may be attached to VK posts.
        :param url: Address of the page where you need to refesh the cached version
        """

        params = self.get_set_params(locals())
        return base.OkResponse(
            **await self.api.request("pages.clearCache", params)
        ).response

    async def get(
        self,
        owner_id: Optional[int] = None,
        page_id: Optional[int] = None,
        global_: Optional[bool] = None,
        site_preview: Optional[bool] = None,
        title: Optional[str] = None,
        need_source: Optional[bool] = None,
        need_html: Optional[bool] = None,
        **kwargs
    ) -> pages.GetResponseModel:
        """Returns information about a wiki page.
        :param owner_id: Page owner ID.
        :param page_id: Wiki page ID.
        :param global: '1' — to return information about a global wiki page
        :param site_preview: '1' — resulting wiki page is a preview for the attached link
        :param title: Wiki page title.
        :param need_source:
        :param need_html: '1' — to return the page as HTML,
        """

        params = self.get_set_params(locals())
        return pages.GetResponse(**await self.api.request("pages.get", params)).response

    async def get_history(
        self,
        page_id: int,
        group_id: Optional[int] = None,
        user_id: Optional[int] = None,
        **kwargs
    ) -> pages.GetHistoryResponseModel:
        """Returns a list of all previous versions of a wiki page.
        :param page_id: Wiki page ID.
        :param group_id: ID of the community that owns the wiki page.
        :param user_id:
        """

        params = self.get_set_params(locals())
        return pages.GetHistoryResponse(
            **await self.api.request("pages.getHistory", params)
        ).response

    async def get_titles(
        self, group_id: Optional[int] = None, **kwargs
    ) -> pages.GetTitlesResponseModel:
        """Returns a list of wiki pages in a group.
        :param group_id: ID of the community that owns the wiki page.
        """

        params = self.get_set_params(locals())
        return pages.GetTitlesResponse(
            **await self.api.request("pages.getTitles", params)
        ).response

    async def get_version(
        self,
        version_id: int,
        group_id: Optional[int] = None,
        user_id: Optional[int] = None,
        need_html: Optional[bool] = None,
        **kwargs
    ) -> pages.GetVersionResponseModel:
        """Returns the text of one of the previous versions of a wiki page.
        :param version_id:
        :param group_id: ID of the community that owns the wiki page.
        :param user_id:
        :param need_html: '1' — to return the page as HTML
        """

        params = self.get_set_params(locals())
        return pages.GetVersionResponse(
            **await self.api.request("pages.getVersion", params)
        ).response

    async def parse_wiki(
        self, text: str, group_id: Optional[int] = None, **kwargs
    ) -> pages.ParseWikiResponseModel:
        """Returns HTML representation of the wiki markup.
        :param text: Text of the wiki page.
        :param group_id: ID of the group in the context of which this markup is interpreted.
        """

        params = self.get_set_params(locals())
        return pages.ParseWikiResponse(
            **await self.api.request("pages.parseWiki", params)
        ).response

    async def save(
        self,
        text: Optional[str] = None,
        page_id: Optional[int] = None,
        group_id: Optional[int] = None,
        user_id: Optional[int] = None,
        title: Optional[str] = None,
        **kwargs
    ) -> pages.SaveResponseModel:
        """Saves the text of a wiki page.
        :param text: Text of the wiki page in wiki-format.
        :param page_id: Wiki page ID. The 'title' parameter can be passed instead of 'pid'.
        :param group_id: ID of the community that owns the wiki page.
        :param user_id: User ID
        :param title: Wiki page title.
        """

        params = self.get_set_params(locals())
        return pages.SaveResponse(
            **await self.api.request("pages.save", params)
        ).response

    async def save_access(
        self,
        page_id: int,
        group_id: Optional[int] = None,
        user_id: Optional[int] = None,
        view: Optional[int] = None,
        edit: Optional[int] = None,
        **kwargs
    ) -> pages.SaveAccessResponseModel:
        """Saves modified read and edit access settings for a wiki page.
        :param page_id: Wiki page ID.
        :param group_id: ID of the community that owns the wiki page.
        :param user_id:
        :param view: Who can view the wiki page: '1' — only community members, '2' — all users can view the page, '0' — only community managers
        :param edit: Who can edit the wiki page: '1' — only community members, '2' — all users can edit the page, '0' — only community managers
        """

        params = self.get_set_params(locals())
        return pages.SaveAccessResponse(
            **await self.api.request("pages.saveAccess", params)
        ).response
