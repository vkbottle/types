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
    response: typing.Optional["AddResponseModel"] = None


class DocUploadResponse(BaseResponse):
    response: typing.Optional["DocUploadResponseModel"] = None


class GetByIdResponse(BaseResponse):
    response: typing.Optional["GetByIdResponseModel"] = None


class GetTypesResponse(BaseResponse):
    response: typing.Optional["GetTypesResponseModel"] = None


class GetUploadServer(BaseResponse):
    response: typing.Optional["GetUploadServerModel"] = None


class GetResponse(BaseResponse):
    response: typing.Optional["GetResponseModel"] = None


class SaveResponse(BaseResponse):
    response: typing.Optional["SaveResponseModel"] = None


class SearchResponse(BaseResponse):
    response: typing.Optional["SearchResponseModel"] = None


AddResponseModel = int


class DocUploadResponseModel(BaseResponse):
    file: typing.Optional[str] = None


GetByIdResponseModel = typing.List[DocsDoc]


class GetTypesResponseModel(BaseResponse):
    count: typing.Optional[int] = None
    items: typing.Optional[typing.List["DocsDocTypes"]] = None


GetUploadServerModel = BaseUploadServer


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
