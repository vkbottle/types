import typing
import enum
from vkbottle_types.responses.base_response import BaseResponse, BaseModel
from vkbottle_types.base_model import Field

from vkbottle_types.objects import (
    PhotosPhotoSizesType,
    BaseBoolInt,
    DocsDocPreviewAudioMsg,
    DocsDocPreview,
    DocsDocPreviewVideo,
    DocsDocPreviewPhoto,
    DocsDocPreviewPhotoSizes,
    DocsDocPreviewGraffiti,
)


class DocsDocResponseModel(BaseModel):
    id: int = Field(
        description="Document ID",
    )

    owner_id: int = Field(
        description="Document owner ID",
    )

    title: str = Field(
        description="Document title",
    )

    size: int = Field(
        description="File size in bites",
    )

    ext: str = Field(
        description="File extension",
    )

    date: int = Field(
        description="Date when file has been uploaded in Unixtime",
    )

    type: int = Field(
        description="Document type",
    )

    url: typing.Optional[str] = Field(
        default=None,
        description="File URL",
    )

    preview: typing.Optional["DocsDocPreview"] = Field(
        default=None,
    )

    is_licensed: typing.Optional[bool] = Field(
        default=None,
    )

    access_key: typing.Optional[str] = Field(
        default=None,
        description="Access key for the document",
    )

    tags: typing.Optional[typing.List[str]] = Field(
        default=None,
        description="Document tags",
    )


class DocsDocResponse(BaseResponse):
    response: "DocsDocResponseModel"


class DocsDocAttachmentTypeResponseModel(enum.Enum):
    DOC = "doc"

    GRAFFITI = "graffiti"

    AUDIO_MESSAGE = "audio_message"


class DocsDocAttachmentTypeResponse(BaseResponse):
    response: "DocsDocAttachmentTypeResponseModel"


class DocsDocPreviewResponseModel(BaseModel):
    audio_msg: typing.Optional["DocsDocPreviewAudioMsg"] = Field(
        default=None,
    )

    graffiti: typing.Optional["DocsDocPreviewGraffiti"] = Field(
        default=None,
    )

    photo: typing.Optional["DocsDocPreviewPhoto"] = Field(
        default=None,
    )

    video: typing.Optional["DocsDocPreviewVideo"] = Field(
        default=None,
    )


class DocsDocPreviewResponse(BaseResponse):
    response: "DocsDocPreviewResponseModel"


class DocsDocPreviewAudioMsgResponseModel(BaseModel):
    duration: int = Field(
        description="Audio message duration in seconds",
    )

    link_mp3: str = Field(
        description="MP3 file URL",
    )

    link_ogg: str = Field(
        description="OGG file URL",
    )

    waveform: typing.List[int] = Field()


class DocsDocPreviewAudioMsgResponse(BaseResponse):
    response: "DocsDocPreviewAudioMsgResponseModel"


class DocsDocPreviewGraffitiResponseModel(BaseModel):
    src: str = Field(
        description="Graffiti file URL",
    )

    width: int = Field(
        description="Graffiti width",
    )

    height: int = Field(
        description="Graffiti height",
    )


class DocsDocPreviewGraffitiResponse(BaseResponse):
    response: "DocsDocPreviewGraffitiResponseModel"


class DocsDocPreviewPhotoResponseModel(BaseModel):
    sizes: typing.Optional[typing.List[DocsDocPreviewPhotoSizes]] = Field(
        default=None,
    )


class DocsDocPreviewPhotoResponse(BaseResponse):
    response: "DocsDocPreviewPhotoResponseModel"


class DocsDocPreviewPhotoSizesResponseModel(BaseModel):
    src: str = Field(
        description="URL of the image",
    )

    width: int = Field(
        description="Width in px",
    )

    height: int = Field(
        description="Height in px",
    )

    type: "PhotosPhotoSizesType" = Field()


class DocsDocPreviewPhotoSizesResponse(BaseResponse):
    response: "DocsDocPreviewPhotoSizesResponseModel"


class DocsDocPreviewVideoResponseModel(BaseModel):
    src: str = Field(
        description="Video URL",
    )

    width: int = Field(
        description="Video's width in pixels",
    )

    height: int = Field(
        description="Video's height in pixels",
    )

    file_size: int = Field(
        description="Video file size in bites",
    )


class DocsDocPreviewVideoResponse(BaseResponse):
    response: "DocsDocPreviewVideoResponseModel"


class DocsDocTypesResponseModel(BaseModel):
    id: int = Field(
        description="Doc type ID",
    )

    name: str = Field(
        description="Doc type title",
    )

    count: int = Field(
        description="Number of docs",
    )


class DocsDocTypesResponse(BaseResponse):
    response: "DocsDocTypesResponseModel"
