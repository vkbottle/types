import typing

from vkbottle_types.objects import AppWidgetsPhoto, AppWidgetsPhotos
from vkbottle_types.responses.base_response import BaseResponse


class GetAppImageUploadServerResponse(BaseResponse):
    response: "GetAppImageUploadServerResponseModel"


class GetAppImagesResponse(BaseResponse):
    response: AppWidgetsPhotos


class GetGroupImageUploadServerResponse(BaseResponse):
    response: "GetGroupImageUploadServerResponseModel"


class GetGroupImagesResponse(BaseResponse):
    response: AppWidgetsPhotos


class GetImagesByIdResponse(BaseResponse):
    response: typing.List["AppWidgetsPhoto"]


class SaveAppImageResponse(BaseResponse):
    response: AppWidgetsPhoto


class SaveGroupImageResponse(BaseResponse):
    response: AppWidgetsPhoto


class GetAppImageUploadServerResponseModel(BaseResponse):
    upload_url: typing.Optional[str] = None


class GetGroupImageUploadServerResponseModel(BaseResponse):
    upload_url: typing.Optional[str] = None


__all__ = (
    "AppWidgetsPhoto",
    "AppWidgetsPhotos",
    "GetAppImageUploadServerResponse",
    "GetAppImageUploadServerResponseModel",
    "GetAppImagesResponse",
    "GetGroupImageUploadServerResponse",
    "GetGroupImageUploadServerResponseModel",
    "GetGroupImagesResponse",
    "GetImagesByIdResponse",
    "SaveAppImageResponse",
    "SaveGroupImageResponse",
)
