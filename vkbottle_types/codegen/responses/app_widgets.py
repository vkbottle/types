import typing

from vkbottle_types.base_model import Field
from vkbottle_types.objects import AppWidgetsPhoto, AppWidgetsPhotos
from vkbottle_types.responses.base_response import BaseResponse


class AppWidgetsGetAppImageUploadServerResponse(BaseResponse):
    response: typing.Dict[str, typing.Any] = Field()


class AppWidgetsGetAppImagesResponse(BaseResponse):
    response: "AppWidgetsPhotos" = Field()


class AppWidgetsGetGroupImageUploadServerResponse(BaseResponse):
    response: typing.Dict[str, typing.Any] = Field()


class AppWidgetsGetGroupImagesResponse(BaseResponse):
    response: "AppWidgetsPhotos" = Field()


class AppWidgetsGetImagesByIdResponse(BaseResponse):
    response: typing.List[AppWidgetsPhoto] = Field()


class AppWidgetsSaveAppImageResponse(BaseResponse):
    response: "AppWidgetsPhoto" = Field()


class AppWidgetsSaveGroupImageResponse(BaseResponse):
    response: "AppWidgetsPhoto" = Field()
