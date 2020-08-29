import typing
from typing import Optional

from vkbottle_types.objects import prettyCards
from .base_response import BaseResponse


class CreateResponse(BaseResponse):
    response: Optional["CreateResponseModel"] = None


class DeleteResponse(BaseResponse):
    response: Optional["DeleteResponseModel"] = None


class EditResponse(BaseResponse):
    response: Optional["EditResponseModel"] = None


class GetByIdResponse(BaseResponse):
    response: Optional[typing.List["prettyCards.PrettyCard"]] = None


class GetUploadURLResponse(BaseResponse):
    response: Optional[str] = None


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


class GetResponseModel(BaseResponse):
    count: Optional[int] = None
    items: Optional[typing.List["prettyCards.PrettyCard"]] = None
