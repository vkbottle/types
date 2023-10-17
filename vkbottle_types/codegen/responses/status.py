import typing
import enum
from vkbottle_types.responses.base_response import BaseResponse, BaseModel
from vkbottle_types.base_model import Field

from vkbottle_types.objects import AudioAudio


class StatusStatusResponseModel(BaseModel):
    text: str = Field(
        description="Status text",
    )

    audio: typing.Optional["AudioAudio"] = Field(
        default=None,
    )


class StatusStatusResponse(BaseResponse):
    response: "StatusStatusResponseModel"
