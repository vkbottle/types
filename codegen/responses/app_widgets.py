import typing

from vkbottle_types.base_model import BaseModel, Field
from vkbottle_types.objects import AppWidgetsPhoto, AppWidgetsPhotos
from vkbottle_types.responses.base_response import BaseResponse


class AppWidgetsGetAppImageUploadServerResponseModel(BaseModel):
    upload_url: typing.Optional[str] = Field(
        default=None,
    )


class AppWidgetsGetAppImageUploadServerResponse(BaseResponse):
    response: "AppWidgetsGetAppImageUploadServerResponseModel" = Field()


class AppWidgetsGetAppImagesResponse(BaseResponse):
    response: "AppWidgetsPhotos" = Field()


class AppWidgetsGetGroupImageUploadServerResponseModel(BaseModel):
    upload_url: typing.Optional[str] = Field(
        default=None,
    )


class AppWidgetsGetGroupImageUploadServerResponse(BaseResponse):
    response: "AppWidgetsGetGroupImageUploadServerResponseModel" = Field()


class AppWidgetsGetGroupImagesResponse(BaseResponse):
    response: "AppWidgetsPhotos" = Field()


class AppWidgetsGetImagesByIdResponse(BaseResponse):
    response: typing.List["AppWidgetsPhoto"] = Field()


class AppWidgetsSaveAppImageResponse(BaseResponse):
    response: "AppWidgetsPhoto" = Field()


class AppWidgetsSaveGroupImageResponse(BaseResponse):
    response: "AppWidgetsPhoto" = Field()
