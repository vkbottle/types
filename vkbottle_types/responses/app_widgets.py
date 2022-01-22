import inspect
import typing
from .base_response import BaseResponse
from vkbottle_types.objects import AppWidgetsPhoto, AppWidgetsPhotos


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


for item in locals().copy().values():
    if inspect.isclass(item) and issubclass(item, BaseResponse):
        item.update_forward_refs()
