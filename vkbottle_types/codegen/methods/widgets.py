import typing

from vkbottle_types.methods.base_category import BaseCategory
from vkbottle_types.responses.widgets import (
    GetCommentsResponse,
    GetCommentsResponseModel,
    GetPagesResponse,
    GetPagesResponseModel,
)


class WidgetsCategory(BaseCategory):
    async def get_comments(
        self,
        widget_api_id: typing.Optional[int] = None,
        url: typing.Optional[str] = None,
        page_id: typing.Optional[str] = None,
        order: typing.Optional[str] = None,
        fields: typing.Optional[typing.List[str]] = None,
        offset: typing.Optional[int] = None,
        count: typing.Optional[int] = None,
        **kwargs
    ) -> GetCommentsResponseModel:
        """Gets a list of comments for the page added through the [vk.com/dev/Comments|Comments widget].

        :param widget_api_id:
        :param url:
        :param page_id:
        :param order:
        :param fields:
        :param offset:
        :param count:
        """

        params = self.get_set_params(locals())
        response = await self.api.request("widgets.getComments", params)
        model = GetCommentsResponse
        return model(**response).response

    async def get_pages(
        self,
        widget_api_id: typing.Optional[int] = None,
        order: typing.Optional[str] = None,
        period: typing.Optional[str] = None,
        offset: typing.Optional[int] = None,
        count: typing.Optional[int] = None,
        **kwargs
    ) -> GetPagesResponseModel:
        """Gets a list of application/site pages where the [vk.com/dev/Comments|Comments widget] or [vk.com/dev/Like|Like widget] is installed.

        :param widget_api_id:
        :param order:
        :param period:
        :param offset:
        :param count:
        """

        params = self.get_set_params(locals())
        response = await self.api.request("widgets.getPages", params)
        model = GetPagesResponse
        return model(**response).response


__all__ = ("WidgetsCategory",)
