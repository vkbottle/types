from .base_response import BaseResponse
from vkbottle_types.objects import messages, docs, base
from typing import Optional, Any, List, Union
import typing


class AddResponse(BaseResponse):
    response: Optional["AddResponseModel"] = None


class GetByIdResponse(BaseResponse):
    response: Optional["GetByIdResponseModel"] = None


class GetTypesResponse(BaseResponse):
    response: Optional["GetTypesResponseModel"] = None


class GetUploadServer(BaseResponse):
    response: Optional["GetUploadServerModel"] = None


class GetResponse(BaseResponse):
    response: Optional["GetResponseModel"] = None


class SaveResponse(BaseResponse):
    response: Optional["SaveResponseModel"] = None


class SearchResponse(BaseResponse):
    response: Optional["SearchResponseModel"] = None


class AddResponseModel(BaseResponse):
    id: Optional[int] = None


GetByIdResponseModel = List["docs.Doc"]


class GetTypesResponseModel(BaseResponse):
    count: Optional[int] = None
    items: Optional[List["docs.DocTypes"]] = None


GetUploadServerModel = Optional["base.UploadServer"]


class GetResponseModel(BaseResponse):
    count: Optional[int] = None
    items: Optional[List["docs.Doc"]] = None


class SaveResponseModel(BaseResponse):
    type: Optional["docs.DocAttachmentType"] = None
    audio_message: Optional["messages.AudioMessage"] = None
    doc: Optional["docs.Doc"] = None
    graffiti: Optional["messages.Graffiti"] = None


class SearchResponseModel(BaseResponse):
    count: Optional[int] = None
    items: Optional[List["docs.Doc"]] = None
