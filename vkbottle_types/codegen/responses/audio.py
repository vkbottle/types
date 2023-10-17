import typing
import enum
from vkbottle_types.responses.base_response import BaseResponse, BaseModel
from vkbottle_types.base_model import Field


class AudioAudioResponseModel(BaseModel):
    artist: str = Field(
        description="Artist name",
    )

    id: int = Field(
        description="Audio ID",
    )

    owner_id: int = Field(
        description="Audio owner's ID",
    )

    title: str = Field(
        description="Title",
    )

    duration: int = Field(
        description="Duration in seconds",
    )

    access_key: typing.Optional[str] = Field(
        default=None,
        description="Access key for the audio",
    )

    url: typing.Optional[str] = Field(
        default=None,
        description="URL of mp3 file",
    )

    date: typing.Optional[int] = Field(
        default=None,
        description="Date when uploaded",
    )

    album_id: typing.Optional[int] = Field(
        default=None,
        description="Album ID",
    )

    performer: typing.Optional[str] = Field(
        default=None,
        description="Performer name",
    )


class AudioAudioResponse(BaseResponse):
    response: "AudioAudioResponseModel"
