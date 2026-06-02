import typing

from vkbottle_types.codegen.methods.photos import PhotosCategory as _PhotosCategory
from vkbottle_types.objects import *
from vkbottle_types.responses.base import BaseGetUploadServerResponse


class PhotosCategory(_PhotosCategory):
    async def get_owner_cover_photo_upload_server(
        self,
        crop_width: int | None = None,
        crop_height: int | None = None,
        crop_x: int | None = None,
        crop_x2: int | None = None,
        crop_y: int | None = None,
        crop_y2: int | None = None,
        group_id: int | None = None,
        is_video_cover: bool | None = None,
        **kwargs: typing.Any,
    ) -> "BaseUploadServer":
        """Method `photos.getOwnerCoverPhotoUploadServer()`

        :param crop_width: Width
        :param crop_height: Height
        :param crop_x: X coordinate of the left-upper corner
        :param crop_x2: X coordinate of the right-bottom corner
        :param crop_y: Y coordinate of the left-upper corner
        :param crop_y2: Y coordinate of the right-bottom corner
        :param group_id: ID of community that owns the album (if the photo will be uploaded to a community album).
        """

        params = self.get_set_params(locals())
        response = await self.api.request("photos.getOwnerCoverPhotoUploadServer", params)
        model = BaseGetUploadServerResponse
        return model(**response).response


__all__ = ("PhotosCategory",)
