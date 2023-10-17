import typing
import enum
from vkbottle_types.responses.base_response import BaseResponse, BaseModel
from vkbottle_types.base_model import Field

from vkbottle_types.objects import BaseImage


class StickersImageSetResponseModel(BaseModel):
    base_url: str = Field(
        description="Base URL for images in set",
    )

    version: typing.Optional[int] = Field(
        default=None,
        description="Version number to be appended to the image URL",
    )

    images: typing.Optional[typing.List[BaseImage]] = Field(
        default=None,
    )


class StickersImageSetResponse(BaseResponse):
    response: "StickersImageSetResponseModel"
