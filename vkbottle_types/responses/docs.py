import typing
from typing import Optional

from vkbottle_types.objects import docs, base, messages
from .base_response import BaseResponse


class AddResponse(BaseResponse):
    response: Optional["AddResponseModel"] = None


class GetByIdResponse(BaseResponse):
    response: Optional[typing.List["docs.Doc"]] = None


class GetTypesResponse(BaseResponse):
    response: Optional["GetTypesResponseModel"] = None


class GetUploadServer(BaseResponse):
    response: Optional[typing.List["base.UploadServer"]] = None


class GetResponse(BaseResponse):
    response: Optional["GetResponseModel"] = None


class SaveResponse(BaseResponse):
    response: Optional["SaveResponseModel"] = None


class SearchResponse(BaseResponse):
    response: Optional["SearchResponseModel"] = None


class AddResponseModel(BaseResponse):
    id: Optional[int] = None


class GetTypesResponseModel(BaseResponse):
    count: Optional[int] = None
    items: Optional[typing.List["docs.DocTypes"]] = None


class GetResponseModel(BaseResponse):
    count: Optional[int] = None
    items: Optional[typing.List["docs.Doc"]] = None


class SaveResponseModel(BaseResponse):
    type: Optional[typing.List["docs.DocAttachmentType"]] = None
    audio_message: Optional[typing.List["messages.AudioMessage"]] = None
    doc: Optional[typing.List["docs.Doc"]] = None
    graffiti: Optional[typing.List["messages.Graffiti"]] = None


class SearchResponseModel(BaseResponse):
    count: Optional[int] = None
    items: Optional[typing.List["docs.Doc"]] = None
