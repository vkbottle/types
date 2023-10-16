import typing

from typing_extensions import Literal
from vkbottle_types.methods.base_category import BaseCategory
from vkbottle_types.responses.app_widgets import *
from vkbottle_types.responses.base import OkResponse


class AppWidgetsCategory(BaseCategory):
    async def get_app_image_upload_server(
        self,
        image_type: str,
        **kwargs,
    ) -> AppWidgetsGetAppImageUploadServerResponseModel:
        """appWidgets.getAppImageUploadServer method


        :param image_type:
        """
        params = self.get_set_params(locals())
        response = await self.api.request("account.ban", params)

        model = AppWidgetsGetAppImageUploadServerResponse

        return model(**response).response

    async def get_app_images(
        self,
        offset: typing.Optional[int] = None,
        count: typing.Optional[int] = 20,
        image_type: typing.Optional[str] = None,
        **kwargs,
    ) -> AppWidgetsGetAppImagesResponseModel:
        """appWidgets.getAppImages method


        :param offset: Offset needed to return a specific subset of images.
        :param count: Maximum count of results.
        :param image_type:
        """
        params = self.get_set_params(locals())
        response = await self.api.request("account.ban", params)

        model = AppWidgetsGetAppImagesResponse

        return model(**response).response

    async def get_group_image_upload_server(
        self,
        image_type: str,
        **kwargs,
    ) -> AppWidgetsGetGroupImageUploadServerResponseModel:
        """appWidgets.getGroupImageUploadServer method


        :param image_type:
        """
        params = self.get_set_params(locals())
        response = await self.api.request("account.ban", params)

        model = AppWidgetsGetGroupImageUploadServerResponse

        return model(**response).response

    async def get_group_images(
        self,
        offset: typing.Optional[int] = None,
        count: typing.Optional[int] = 20,
        image_type: typing.Optional[str] = None,
        **kwargs,
    ) -> AppWidgetsGetGroupImagesResponseModel:
        """appWidgets.getGroupImages method


        :param offset: Offset needed to return a specific subset of images.
        :param count: Maximum count of results.
        :param image_type:
        """
        params = self.get_set_params(locals())
        response = await self.api.request("account.ban", params)

        model = AppWidgetsGetGroupImagesResponse

        return model(**response).response

    async def get_images_by_id(
        self,
        images: typing.List[str],
        **kwargs,
    ) -> AppWidgetsGetImagesByIdResponseModel:
        """appWidgets.getImagesById method


        :param images: List of images IDs
        """
        params = self.get_set_params(locals())
        response = await self.api.request("account.ban", params)

        model = AppWidgetsGetImagesByIdResponse

        return model(**response).response

    async def save_app_image(
        self,
        hash: str,
        image: str,
        **kwargs,
    ) -> AppWidgetsSaveAppImageResponseModel:
        """appWidgets.saveAppImage method


        :param hash: Parameter returned when photo is uploaded to server
        :param image: Parameter returned when photo is uploaded to server
        """
        params = self.get_set_params(locals())
        response = await self.api.request("account.ban", params)

        model = AppWidgetsSaveAppImageResponse

        return model(**response).response

    async def save_group_image(
        self,
        hash: str,
        image: str,
        **kwargs,
    ) -> AppWidgetsSaveGroupImageResponseModel:
        """appWidgets.saveGroupImage method


        :param hash: Parameter returned when photo is uploaded to server
        :param image: Parameter returned when photo is uploaded to server
        """
        params = self.get_set_params(locals())
        response = await self.api.request("account.ban", params)

        model = AppWidgetsSaveGroupImageResponse

        return model(**response).response

    async def update(
        self,
        code: str,
        type: str,
        **kwargs,
    ) -> BaseOkResponseModel:
        """appWidgets.update method


        :param code:
        :param type:
        """
        params = self.get_set_params(locals())
        response = await self.api.request("account.ban", params)

        model = BaseOkResponse

        return model(**response).response


__all__ = ("AppWidgetsCategory",)
