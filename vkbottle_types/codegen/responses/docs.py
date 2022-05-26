import inspect
import typing

from vkbottle_types.objects import (
    BaseUploadServer,
    DocsDoc,
    DocsDocAttachmentType,
    DocsDocTypes,
    MessagesAudioMessage,
    MessagesGraffiti,
)

from .base_response import BaseResponse


class AddResponse(BaseResponse):
    response: int


class DocUploadResponse(BaseResponse):
    response: "DocUploadResponseModel"


class GetByIdResponse(BaseResponse):
    response: typing.List["DocsDoc"]


class GetTypesResponse(BaseResponse):
    response: "GetTypesResponseModel"


class GetUploadServerResponse(BaseResponse):
    response: BaseUploadServer


class GetResponse(BaseResponse):
    response: "GetResponseModel"


class SaveResponse(BaseResponse):
    response: "SaveResponseModel"


class SearchResponse(BaseResponse):
    response: "SearchResponseModel"


class DocUploadResponseModel(BaseResponse):
    file: typing.Optional[str] = None


class GetTypesResponseModel(BaseResponse):
    count: typing.Optional[int] = None
    items: typing.Optional[typing.List["DocsDocTypes"]] = None


class GetResponseModel(BaseResponse):
    count: typing.Optional[int] = None
    items: typing.Optional[typing.List["DocsDoc"]] = None


class SaveResponseModel(BaseResponse):
    type: typing.Optional["DocsDocAttachmentType"] = None
    audio_message: typing.Optional["MessagesAudioMessage"] = None
    doc: typing.Optional["DocsDoc"] = None
    graffiti: typing.Optional["MessagesGraffiti"] = None


class SearchResponseModel(BaseResponse):
    count: typing.Optional[int] = None
    items: typing.Optional[typing.List["DocsDoc"]] = None


for item in locals().copy().values():
    if inspect.isclass(item) and issubclass(item, BaseResponse):
        item.update_forward_refs()


__all__ = (
    "AddResponse",
    "DocUploadResponse",
    "GetByIdResponse",
    "GetTypesResponse",
    "GetUploadServerResponse",
    "GetResponse",
    "SaveResponse",
    "SearchResponse",
)
