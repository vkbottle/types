import typing

from vkbottle_types.base_model import Field
from vkbottle_types.objects import LeadFormsForm
from vkbottle_types.responses.base_response import BaseResponse


class LeadFormsCreateResponse(BaseResponse):
    response: typing.Dict[str, typing.Any] = Field()


class LeadFormsDeleteResponse(BaseResponse):
    response: typing.Dict[str, typing.Any] = Field()


class LeadFormsGetLeadsResponse(BaseResponse):
    response: typing.Dict[str, typing.Any] = Field()


class LeadFormsGetResponse(BaseResponse):
    response: "LeadFormsForm" = Field()


class LeadFormsListResponse(BaseResponse):
    response: typing.List[LeadFormsForm] = Field()


class LeadFormsUploadUrlResponse(BaseResponse):
    response: str = Field()
