import typing

from vkbottle_types.base_model import BaseModel, Field
from vkbottle_types.objects import BaseUploadServer, DocsDoc, DocsDocAttachmentType, DocsDocTypes, MessagesAudioMessage, MessagesGraffiti
from vkbottle_types.responses.base_response import BaseResponse


class DocsAddResponse(BaseResponse):
    response: int = Field()


class DocsDocUploadResponseModel(BaseModel):
    file: typing.Optional[str] = Field(
        default=None,
    )


class DocsDocUploadResponse(BaseResponse):
    response: "DocsDocUploadResponseModel" = Field()


class DocsGetByIdResponse(BaseResponse):
    response: typing.List["DocsDoc"] = Field()


class DocsGetTypesResponseModel(BaseModel):
    count: int = Field()
    items: typing.List["DocsDocTypes"] = Field()


class DocsGetTypesResponse(BaseResponse):
    response: "DocsGetTypesResponseModel" = Field()


class DocsGetUploadServerResponse(BaseResponse):
    response: "BaseUploadServer" = Field()


class DocsGetResponseModel(BaseModel):
    count: int = Field()
    items: typing.List["DocsDoc"] = Field()


class DocsGetResponse(BaseResponse):
    response: "DocsGetResponseModel" = Field()


class DocsSaveResponseModel(BaseModel):
    type: typing.Optional["DocsDocAttachmentType"] = Field(
        default=None,
    )
    audio_message: typing.Optional["MessagesAudioMessage"] = Field(
        default=None,
    )
    doc: typing.Optional["DocsDoc"] = Field(
        default=None,
    )
    graffiti: typing.Optional["MessagesGraffiti"] = Field(
        default=None,
    )


class DocsSaveResponse(BaseResponse):
    response: "DocsSaveResponseModel" = Field()


class DocsSearchResponseModel(BaseModel):
    count: int = Field()
    items: typing.List["DocsDoc"] = Field()


class DocsSearchResponse(BaseResponse):
    response: "DocsSearchResponseModel" = Field()
