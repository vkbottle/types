import inspect
import typing

from vkbottle_types.objects import AppWidgetsPhoto, AppWidgetsPhotos

from .base_response import BaseResponse


class GetAppImageUploadServerResponse(BaseResponse):
    response: typing.Optional["GetAppImageUploadServerResponseModel"] = None


class GetAppImagesResponse(BaseResponse):
    response: typing.Optional["GetAppImagesResponseModel"] = None


class GetGroupImageUploadServerResponse(BaseResponse):
    response: typing.Optional["GetGroupImageUploadServerResponseModel"] = None


class GetGroupImagesResponse(BaseResponse):
    response: typing.Optional["GetGroupImagesResponseModel"] = None


class GetImagesByIdResponse(BaseResponse):
    response: typing.Optional["GetImagesByIdResponseModel"] = None


class SaveAppImageResponse(BaseResponse):
    response: typing.Optional["SaveAppImageResponseModel"] = None


class SaveGroupImageResponse(BaseResponse):
    response: typing.Optional["SaveGroupImageResponseModel"] = None


class GetAppImageUploadServerResponseModel(BaseResponse):
    upload_url: typing.Optional[str] = None


GetAppImagesResponseModel = AppWidgetsPhotos


class GetGroupImageUploadServerResponseModel(BaseResponse):
    upload_url: typing.Optional[str] = None


GetGroupImagesResponseModel = AppWidgetsPhotos


GetImagesByIdResponseModel = typing.List[AppWidgetsPhoto]


SaveAppImageResponseModel = AppWidgetsPhoto


SaveGroupImageResponseModel = AppWidgetsPhoto


for item in locals().copy().values():
    if inspect.isclass(item) and issubclass(item, BaseResponse):
        item.update_forward_refs()
