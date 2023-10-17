import typing
from vkbottle_types.responses.base_response import BaseResponse, BaseModel
from vkbottle_types.base_model import Field

from vkbottle_types.objects import AppWidgetsPhoto, BaseImage


class AppWidgetsPhotoResponseModel(BaseModel):
    id: str = Field(
        description="Image ID",
    )

    images: typing.List[BaseImage] = Field()


class AppWidgetsPhotoResponse(BaseResponse):
    response: "AppWidgetsPhotoResponseModel"


class AppWidgetsPhotosResponseModel(BaseModel):
    count: typing.Optional[int] = Field(
        default=None,
    )

    items: typing.Optional[typing.List[AppWidgetsPhoto]] = Field(
        default=None,
    )


class AppWidgetsPhotosResponse(BaseResponse):
    response: "AppWidgetsPhotosResponseModel"
