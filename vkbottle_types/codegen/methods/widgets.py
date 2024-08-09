import typing

from vkbottle_types.methods.base_category import BaseCategory
from vkbottle_types.objects import UsersFields
from vkbottle_types.responses.widgets import *  # noqa: F401,F403  # type: ignore


class WidgetsCategory(BaseCategory):
    async def get_comments(
        self,
        count: typing.Optional[int] = None,
        fields: typing.Optional[typing.List[UsersFields]] = None,
        offset: typing.Optional[int] = None,
        order: typing.Optional[str] = None,
        page_id: typing.Optional[str] = None,
        url: typing.Optional[str] = None,
        widget_api_id: typing.Optional[int] = None,
        **kwargs: typing.Any,
    ) -> WidgetsGetCommentsResponseModel:
        """Method `widgets.getComments()`

        :param count:
        :param fields:
        :param offset:
        :param order:
        :param page_id:
        :param url:
        :param widget_api_id:
        """

        params = self.get_set_params(locals())
        response = await self.api.request("widgets.getComments", params)
        model = WidgetsGetCommentsResponse
        return model(**response).response

    async def get_pages(
        self,
        count: typing.Optional[int] = None,
        offset: typing.Optional[int] = None,
        order: typing.Optional[str] = None,
        period: typing.Optional[str] = None,
        widget_api_id: typing.Optional[int] = None,
        **kwargs: typing.Any,
    ) -> WidgetsGetPagesResponseModel:
        """Method `widgets.getPages()`

        :param count:
        :param offset:
        :param order:
        :param period:
        :param widget_api_id:
        """

        params = self.get_set_params(locals())
        response = await self.api.request("widgets.getPages", params)
        model = WidgetsGetPagesResponse
        return model(**response).response


__all__ = ("WidgetsCategory",)
