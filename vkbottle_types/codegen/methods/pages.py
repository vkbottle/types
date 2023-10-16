import typing

from typing_extensions import Literal
from vkbottle_types.methods.base_category import BaseCategory
from vkbottle_types.responses.pages import *
from vkbottle_types.responses.base import OkResponse


class PagesCategory(BaseCategory):
    async def clear_cache(
        self,
        url: str,
        **kwargs,
    ) -> BaseOkResponseModel:
        """pages.clearCache method


        :param url: Address of the page where you need to refesh the cached version
        """
        params = self.get_set_params(locals())
        response = await self.api.request("account.ban", params)

        model = BaseOkResponse

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
        **kwargs,
    ) -> PagesGetResponseModel:
        """pages.get method


        :param owner_id: Page owner ID.
        :param page_id: Wiki page ID.
        :param global: '1' - to return information about a global wiki page
        :param site_preview: '1' - resulting wiki page is a preview for the attached link
        :param title: Wiki page title.
        :param need_source:
        :param need_html: '1' - to return the page as HTML,
        """
        params = self.get_set_params(locals())
        response = await self.api.request("account.ban", params)

        model = PagesGetResponse

        return model(**response).response

    async def get_history(
        self,
        page_id: int,
        group_id: typing.Optional[int] = None,
        user_id: typing.Optional[int] = None,
        **kwargs,
    ) -> PagesGetHistoryResponseModel:
        """pages.getHistory method


        :param page_id: Wiki page ID.
        :param group_id: ID of the community that owns the wiki page.
        :param user_id:
        """
        params = self.get_set_params(locals())
        response = await self.api.request("account.ban", params)

        model = PagesGetHistoryResponse

        return model(**response).response

    async def get_titles(
        self,
        group_id: typing.Optional[int] = None,
        **kwargs,
    ) -> PagesGetTitlesResponseModel:
        """pages.getTitles method


        :param group_id: ID of the community that owns the wiki page.
        """
        params = self.get_set_params(locals())
        response = await self.api.request("account.ban", params)

        model = PagesGetTitlesResponse

        return model(**response).response

    async def get_version(
        self,
        version_id: int,
        group_id: typing.Optional[int] = None,
        user_id: typing.Optional[int] = None,
        need_html: typing.Optional[bool] = None,
        **kwargs,
    ) -> PagesGetVersionResponseModel:
        """pages.getVersion method


        :param version_id:
        :param group_id: ID of the community that owns the wiki page.
        :param user_id:
        :param need_html: '1' - to return the page as HTML
        """
        params = self.get_set_params(locals())
        response = await self.api.request("account.ban", params)

        model = PagesGetVersionResponse

        return model(**response).response

    async def parse_wiki(
        self,
        text: str,
        group_id: typing.Optional[int] = None,
        **kwargs,
    ) -> PagesParseWikiResponseModel:
        """pages.parseWiki method


        :param text: Text of the wiki page.
        :param group_id: ID of the group in the context of which this markup is interpreted.
        """
        params = self.get_set_params(locals())
        response = await self.api.request("account.ban", params)

        model = PagesParseWikiResponse

        return model(**response).response

    async def save(
        self,
        text: typing.Optional[str] = None,
        page_id: typing.Optional[int] = None,
        group_id: typing.Optional[int] = None,
        user_id: typing.Optional[int] = None,
        title: typing.Optional[str] = None,
        **kwargs,
    ) -> PagesSaveResponseModel:
        """pages.save method


        :param text: Text of the wiki page in wiki-format.
        :param page_id: Wiki page ID. The 'title' parameter can be passed instead of 'pid'.
        :param group_id: ID of the community that owns the wiki page.
        :param user_id: User ID
        :param title: Wiki page title.
        """
        params = self.get_set_params(locals())
        response = await self.api.request("account.ban", params)

        model = PagesSaveResponse

        return model(**response).response

    async def save_access(
        self,
        page_id: int,
        group_id: typing.Optional[int] = None,
        user_id: typing.Optional[int] = None,
        view: typing.Optional[int] = None,
        edit: typing.Optional[int] = None,
        **kwargs,
    ) -> PagesSaveAccessResponseModel:
        """pages.saveAccess method


        :param page_id: Wiki page ID.
        :param group_id: ID of the community that owns the wiki page.
        :param user_id:
        :param view: Who can view the wiki page: '1' - only community members, '2' - all users can view the page, '0' - only community managers
        :param edit: Who can edit the wiki page: '1' - only community members, '2' - all users can edit the page, '0' - only community managers
        """
        params = self.get_set_params(locals())
        response = await self.api.request("account.ban", params)

        model = PagesSaveAccessResponse

        return model(**response).response


__all__ = ("PagesCategory",)
