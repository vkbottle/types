import inspect
import typing
from .base_response import BaseResponse
from vkbottle_types.objects import AppWidgetsPhoto, AppWidgetsPhotos


class GetAppImageUploadServerResponse(BaseResponse):
    response: "GetAppImageUploadServerResponseModel" = None


class GetAppImagesResponse(BaseResponse):
    response: AppWidgetsPhotos = None


class GetGroupImageUploadServerResponse(BaseResponse):
    response: "GetGroupImageUploadServerResponseModel" = None


class GetGroupImagesResponse(BaseResponse):
    response: AppWidgetsPhotos = None


class GetImagesByIdResponse(BaseResponse):
    response: typing.List["AppWidgetsPhoto"] = None


class SaveAppImageResponse(BaseResponse):
    response: AppWidgetsPhoto = None


class SaveGroupImageResponse(BaseResponse):
    response: AppWidgetsPhoto = None


class GetAppImageUploadServerResponseModel(BaseResponse):
    upload_url: typing.Optional[str] = None


class GetGroupImageUploadServerResponseModel(BaseResponse):
    upload_url: typing.Optional[str] = None


for item in locals().copy().values():
    if inspect.isclass(item) and issubclass(item, BaseResponse):
        item.update_forward_refs()
