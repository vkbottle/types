import typing

from vkbottle_types.objects import LeadFormsForm, LeadFormsLead
from vkbottle_types.responses.base_response import BaseResponse


class CreateResponse(BaseResponse):
    response: "CreateResponseModel"


class DeleteResponse(BaseResponse):
    response: "DeleteResponseModel"


class GetLeadsResponse(BaseResponse):
    response: "GetLeadsResponseModel"


class GetResponse(BaseResponse):
    response: LeadFormsForm


class ListResponse(BaseResponse):
    response: typing.List["LeadFormsForm"]


class UploadUrlResponse(BaseResponse):
    response: str


class CreateResponseModel(BaseResponse):
    form_id: typing.Optional[int] = None
    url: typing.Optional[str] = None


class DeleteResponseModel(BaseResponse):
    form_id: typing.Optional[int] = None


class GetLeadsResponseModel(BaseResponse):
    leads: typing.Optional[typing.List["LeadFormsLead"]] = None
    next_page_token: typing.Optional[str] = None


__all__ = (
    "CreateResponse",
    "CreateResponseModel",
    "DeleteResponse",
    "DeleteResponseModel",
    "GetLeadsResponse",
    "GetLeadsResponseModel",
    "GetResponse",
    "LeadFormsForm",
    "LeadFormsLead",
    "ListResponse",
    "UploadUrlResponse",
)
