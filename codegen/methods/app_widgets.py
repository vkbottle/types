import typing

from vkbottle_types.methods.base_category import BaseCategory
from vkbottle_types.objects import AppWidgetsPhoto, AppWidgetsPhotos
from vkbottle_types.responses.app_widgets import *  # noqa: F401,F403  # type: ignore
from vkbottle_types.responses.base import (
    BaseOkResponse,
    BaseOkResponseModel,
)


class AppWidgetsCategory(BaseCategory):
    async def get_app_image_upload_server(
        self,
        image_type: str,
        **kwargs: typing.Any,
    ) -> AppWidgetsGetAppImageUploadServerResponseModel:
        """Method `appWidgets.getAppImageUploadServer()`

        :param image_type:
        """

        params = self.get_set_params(locals())
        response = await self.api.request("appWidgets.getAppImageUploadServer", params)
        model = AppWidgetsGetAppImageUploadServerResponse
        return model(**response).response

    async def get_app_images(
        self,
        count: typing.Optional[int] = None,
        image_type: typing.Optional[str] = None,
        offset: typing.Optional[int] = None,
        **kwargs: typing.Any,
    ) -> "AppWidgetsPhotos":
        """Method `appWidgets.getAppImages()`

        :param count: Maximum count of results.
        :param image_type:
        :param offset: Offset needed to return a specific subset of images.
        """

        params = self.get_set_params(locals())
        response = await self.api.request("appWidgets.getAppImages", params)
        model = AppWidgetsGetAppImagesResponse
        return model(**response).response

    async def get_group_image_upload_server(
        self,
        image_type: str,
        **kwargs: typing.Any,
    ) -> AppWidgetsGetGroupImageUploadServerResponseModel:
        """Method `appWidgets.getGroupImageUploadServer()`

        :param image_type:
        """

        params = self.get_set_params(locals())
        response = await self.api.request("appWidgets.getGroupImageUploadServer", params)
        model = AppWidgetsGetGroupImageUploadServerResponse
        return model(**response).response

    async def get_group_images(
        self,
        count: typing.Optional[int] = None,
        image_type: typing.Optional[str] = None,
        offset: typing.Optional[int] = None,
        **kwargs: typing.Any,
    ) -> "AppWidgetsPhotos":
        """Method `appWidgets.getGroupImages()`

        :param count: Maximum count of results.
        :param image_type:
        :param offset: Offset needed to return a specific subset of images.
        """

        params = self.get_set_params(locals())
        response = await self.api.request("appWidgets.getGroupImages", params)
        model = AppWidgetsGetGroupImagesResponse
        return model(**response).response

    async def get_images_by_id(
        self,
        images: typing.List[str],
        **kwargs: typing.Any,
    ) -> typing.List[AppWidgetsPhoto]:
        """Method `appWidgets.getImagesById()`

        :param images: List of images IDs
        """

        params = self.get_set_params(locals())
        response = await self.api.request("appWidgets.getImagesById", params)
        model = AppWidgetsGetImagesByIdResponse
        return model(**response).response

    async def save_app_image(
        self,
        hash: str,
        image: str,
        **kwargs: typing.Any,
    ) -> "AppWidgetsPhoto":
        """Method `appWidgets.saveAppImage()`

        :param hash: Parameter returned when photo is uploaded to server
        :param image: Parameter returned when photo is uploaded to server
        """

        params = self.get_set_params(locals())
        response = await self.api.request("appWidgets.saveAppImage", params)
        model = AppWidgetsSaveAppImageResponse
        return model(**response).response

    async def save_group_image(
        self,
        hash: str,
        image: str,
        **kwargs: typing.Any,
    ) -> "AppWidgetsPhoto":
        """Method `appWidgets.saveGroupImage()`

        :param hash: Parameter returned when photo is uploaded to server
        :param image: Parameter returned when photo is uploaded to server
        """

        params = self.get_set_params(locals())
        response = await self.api.request("appWidgets.saveGroupImage", params)
        model = AppWidgetsSaveGroupImageResponse
        return model(**response).response

    async def update(
        self,
        code: str,
        type: str,
        **kwargs: typing.Any,
    ) -> BaseOkResponseModel:
        """Method `appWidgets.update()`

        :param code:
        :param type:
        """

        params = self.get_set_params(locals())
        response = await self.api.request("appWidgets.update", params)
        model = BaseOkResponse
        return model(**response).response


__all__ = ("AppWidgetsCategory",)
