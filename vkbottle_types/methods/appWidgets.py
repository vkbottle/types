import typing

from vkbottle_types.responses import appWidgets, base

from .base_category import BaseCategory


class AppwidgetsCategory(BaseCategory):
    async def get_app_image_upload_server(
        self, image_type: str, **kwargs
    ) -> appWidgets.GetAppImageUploadServerResponseModel:
        """Returns a URL for uploading a photo to the community collection for community app widgets
        :param image_type:
        """

        params = self.get_set_params(locals())
        response = await self.api.request("appWidgets.getAppImageUploadServer", params)
        model = appWidgets.GetAppImageUploadServerResponse
        return model(**response).response

    async def get_app_images(
        self,
        offset: typing.Optional[int] = None,
        count: typing.Optional[int] = None,
        image_type: typing.Optional[str] = None,
        **kwargs
    ) -> appWidgets.GetAppImagesResponseModel:
        """Returns an app collection of images for community app widgets
        :param offset: Offset needed to return a specific subset of images.
        :param count: Maximum count of results.
        :param image_type:
        """

        params = self.get_set_params(locals())
        response = await self.api.request("appWidgets.getAppImages", params)
        model = appWidgets.GetAppImagesResponse
        return model(**response).response

    async def get_group_image_upload_server(
        self, image_type: str, **kwargs
    ) -> appWidgets.GetGroupImageUploadServerResponseModel:
        """Returns a URL for uploading a photo to the community collection for community app widgets
        :param image_type:
        """

        params = self.get_set_params(locals())
        response = await self.api.request(
            "appWidgets.getGroupImageUploadServer", params
        )
        model = appWidgets.GetGroupImageUploadServerResponse
        return model(**response).response

    async def get_group_images(
        self,
        offset: typing.Optional[int] = None,
        count: typing.Optional[int] = None,
        image_type: typing.Optional[str] = None,
        **kwargs
    ) -> appWidgets.GetGroupImagesResponseModel:
        """Returns a community collection of images for community app widgets
        :param offset: Offset needed to return a specific subset of images.
        :param count: Maximum count of results.
        :param image_type:
        """

        params = self.get_set_params(locals())
        response = await self.api.request("appWidgets.getGroupImages", params)
        model = appWidgets.GetGroupImagesResponse
        return model(**response).response

    async def get_images_by_id(
        self, images: typing.List[str], **kwargs
    ) -> appWidgets.GetImagesByIdResponseModel:
        """Returns an image for community app widgets by its ID
        :param images: List of images IDs
        """

        params = self.get_set_params(locals())
        response = await self.api.request("appWidgets.getImagesById", params)
        model = appWidgets.GetImagesByIdResponse
        return model(**response).response

    async def save_app_image(
        self, hash: str, image: str, **kwargs
    ) -> appWidgets.SaveAppImageResponseModel:
        """Allows to save image into app collection for community app widgets
        :param hash: Parameter returned when photo is uploaded to server
        :param image: Parameter returned when photo is uploaded to server
        """

        params = self.get_set_params(locals())
        response = await self.api.request("appWidgets.saveAppImage", params)
        model = appWidgets.SaveAppImageResponse
        return model(**response).response

    async def save_group_image(
        self, hash: str, image: str, **kwargs
    ) -> appWidgets.SaveGroupImageResponseModel:
        """Allows to save image into community collection for community app widgets
        :param hash: Parameter returned when photo is uploaded to server
        :param image: Parameter returned when photo is uploaded to server
        """

        params = self.get_set_params(locals())
        response = await self.api.request("appWidgets.saveGroupImage", params)
        model = appWidgets.SaveGroupImageResponse
        return model(**response).response

    async def update(self, code: str, type: str, **kwargs) -> base.OkResponseModel:
        """Allows to update community app widget
        :param code:
        :param type:
        """

        params = self.get_set_params(locals())
        response = await self.api.request("appWidgets.update", params)
        model = base.OkResponse
        return model(**response).response
