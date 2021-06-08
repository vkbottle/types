import inspect
import typing
from .base_response import BaseResponse
from vkbottle_types.objects import (
    BaseUploadServer,
    DocsDoc,
    DocsDocAttachmentType,
    DocsDocTypes,
    MessagesAudioMessage,
    MessagesGraffiti
)


class AddResponse(BaseResponse):
    response: int = None


class DocUploadResponse(BaseResponse):
    response: "DocUploadResponseModel" = None


class GetByIdResponse(BaseResponse):
    response: typing.List["DocsDoc"] = None


class GetTypesResponse(BaseResponse):
    response: "GetTypesResponseModel" = None


class GetUploadServer(BaseResponse):
    response: BaseUploadServer = None


class GetResponse(BaseResponse):
    response: "GetResponseModel" = None


class SaveResponse(BaseResponse):
    response: "SaveResponseModel" = None


class SearchResponse(BaseResponse):
    response: "SearchResponseModel" = None


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
