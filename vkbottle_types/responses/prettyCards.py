from typing import Optional, List

from vkbottle_types.objects import PrettyCardsPrettyCard
from .base_response import BaseResponse


class CreateResponse(BaseResponse):
    response: Optional["CreateResponseModel"] = None


class DeleteResponse(BaseResponse):
    response: Optional["DeleteResponseModel"] = None


class EditResponse(BaseResponse):
    response: Optional["EditResponseModel"] = None


class GetByIdResponse(BaseResponse):
    response: Optional["GetByIdResponseModel"] = None


class GetUploadURLResponse(BaseResponse):
    response: Optional["GetUploadURLResponseModel"] = None


class GetResponse(BaseResponse):
    response: Optional["GetResponseModel"] = None


class CreateResponseModel(BaseResponse):
    owner_id: Optional[int] = None
    card_id: Optional[str] = None


class DeleteResponseModel(BaseResponse):
    owner_id: Optional[int] = None
    card_id: Optional[str] = None
    error: Optional[str] = None


class EditResponseModel(BaseResponse):
    owner_id: Optional[int] = None
    card_id: Optional[str] = None


GetByIdResponseModel = List[PrettyCardsPrettyCard]


GetUploadURLResponseModel = str


class GetResponseModel(BaseResponse):
    count: Optional[int] = None
    items: Optional[List["PrettyCardsPrettyCard"]] = None


CreateResponse.update_forward_refs()
DeleteResponse.update_forward_refs()
EditResponse.update_forward_refs()
GetByIdResponse.update_forward_refs()
GetUploadURLResponse.update_forward_refs()
GetResponse.update_forward_refs()
