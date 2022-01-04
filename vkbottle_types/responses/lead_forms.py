import inspect
import typing
from .base_response import BaseResponse
from vkbottle_types.objects import LeadFormsForm, LeadFormsLead


class CreateResponse(BaseResponse):
    response: "CreateResponseModel" = None


class DeleteResponse(BaseResponse):
    response: "DeleteResponseModel" = None


class GetLeadsResponse(BaseResponse):
    response: "GetLeadsResponseModel" = None


class GetResponse(BaseResponse):
    response: LeadFormsForm = None


class ListResponse(BaseResponse):
    response: typing.List["LeadFormsForm"] = None


class UploadUrlResponse(BaseResponse):
    response: str = None


class CreateResponseModel(BaseResponse):
    form_id: typing.Optional[int] = None
    url: typing.Optional[str] = None


class DeleteResponseModel(BaseResponse):
    form_id: typing.Optional[int] = None


class GetLeadsResponseModel(BaseResponse):
    leads: typing.Optional[typing.List["LeadFormsLead"]] = None
    next_page_token: typing.Optional[str] = None


for item in locals().copy().values():
    if inspect.isclass(item) and issubclass(item, BaseResponse):
        item.update_forward_refs()
