from vkbottle_types.base_model import BaseModel, Field
from vkbottle_types.objects import BaseUploadServer, DocsDoc, DocsDocAttachmentType, DocsDocTypes, MessagesAudioMessage, MessagesGraffiti
from vkbottle_types.responses.base_response import BaseResponse


class DocsAddResponse(BaseResponse):
    response: int = Field()


class DocsDocUploadResponseModel(BaseModel):
    file: str | None = Field(
        default=None,
    )


class DocsDocUploadResponse(BaseResponse):
    response: "DocsDocUploadResponseModel" = Field()


class DocsGetByIdResponse(BaseResponse):
    response: list["DocsDoc"] = Field()


class DocsGetTypesResponseModel(BaseModel):
    count: int = Field()
    items: list["DocsDocTypes"] = Field()


class DocsGetTypesResponse(BaseResponse):
    response: "DocsGetTypesResponseModel" = Field()


class DocsGetUploadServerResponse(BaseResponse):
    response: "BaseUploadServer" = Field()


class DocsGetResponseModel(BaseModel):
    count: int = Field()
    items: list["DocsDoc"] = Field()


class DocsGetResponse(BaseResponse):
    response: "DocsGetResponseModel" = Field()


class DocsSaveResponseModel(BaseModel):
    type: "DocsDocAttachmentType | None" = Field(
        default=None,
    )
    audio_message: "MessagesAudioMessage | None" = Field(
        default=None,
    )
    doc: "DocsDoc | None" = Field(
        default=None,
    )
    graffiti: "MessagesGraffiti | None" = Field(
        default=None,
    )


class DocsSaveResponse(BaseResponse):
    response: "DocsSaveResponseModel" = Field()


class DocsSearchResponseModel(BaseModel):
    count: int = Field()
    items: list["DocsDoc"] = Field()


class DocsSearchResponse(BaseResponse):
    response: "DocsSearchResponseModel" = Field()
