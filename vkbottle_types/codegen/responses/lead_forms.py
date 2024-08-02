import typing

from vkbottle_types.base_model import BaseModel, Field
from vkbottle_types.objects import LeadFormsForm, LeadFormsLead
from vkbottle_types.responses.base_response import BaseResponse


class LeadFormsCreateResponseModel(BaseModel):
    form_id: int = Field()
    url: str = Field()


class LeadFormsCreateResponse(BaseResponse):
    response: "LeadFormsCreateResponseModel" = Field()


class LeadFormsDeleteResponseModel(BaseModel):
    form_id: int = Field()


class LeadFormsDeleteResponse(BaseResponse):
    response: "LeadFormsDeleteResponseModel" = Field()


class LeadFormsGetLeadsResponseModel(BaseModel):
    leads: typing.List["LeadFormsLead"] = Field()
    next_page_token: typing.Optional[str] = Field(
        default=None,
    )


class LeadFormsGetLeadsResponse(BaseResponse):
    response: "LeadFormsGetLeadsResponseModel" = Field()


class LeadFormsGetResponse(BaseResponse):
    response: "LeadFormsForm" = Field()


class LeadFormsListResponse(BaseResponse):
    response: typing.List["LeadFormsForm"] = Field()


class LeadFormsUploadUrlResponse(BaseResponse):
    response: str = Field()
