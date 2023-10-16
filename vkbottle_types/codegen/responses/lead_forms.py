import typing
from vkbottle_types.responses.base_response import BaseResponse, BaseModel
from vkbottle_types.base_model import Field

from vkbottle_types.objects import (
    LeadFormsAnswer,
    LeadFormsQuestionItemOption,
    BaseBoolInt,
    LeadFormsAnswerOneOf,
    LeadFormsQuestionItem,
)


class LeadFormsAnswerResponseModel(BaseModel):
    key: str = Field()

    answer: "LeadFormsAnswerOneOf" = Field()


class LeadFormsAnswerResponse(BaseResponse):
    response: "LeadFormsAnswerResponseModel"


class LeadFormsAnswerItemResponseModel(BaseModel):
    value: str = Field()

    key: typing.Optional[str] = Field(
        default=None,
    )


class LeadFormsAnswerItemResponse(BaseResponse):
    response: "LeadFormsAnswerItemResponseModel"


class LeadFormsAnswerOneOfResponseModel(BaseModel):
    pass


class LeadFormsAnswerOneOfResponse(BaseResponse):
    response: "LeadFormsAnswerOneOfResponseModel"


class LeadFormsFormResponseModel(BaseModel):
    form_id: int = Field()

    group_id: int = Field()

    leads_count: int = Field()

    url: str = Field()

    photo: typing.Optional[str] = Field(
        default=None,
    )

    name: typing.Optional[str] = Field(
        default=None,
    )

    title: typing.Optional[str] = Field(
        default=None,
    )

    description: typing.Optional[str] = Field(
        default=None,
    )

    confirmation: typing.Optional[str] = Field(
        default=None,
    )

    site_link_url: typing.Optional[str] = Field(
        default=None,
    )

    policy_link_url: typing.Optional[str] = Field(
        default=None,
    )

    questions: typing.Optional[typing.List[LeadFormsQuestionItem]] = Field(
        default=None,
    )

    active: typing.Optional[bool] = Field(
        default=None,
    )

    pixel_code: typing.Optional[str] = Field(
        default=None,
    )

    once_per_user: typing.Optional[int] = Field(
        default=None,
    )

    notify_admins: typing.Optional[str] = Field(
        default=None,
    )

    notify_emails: typing.Optional[str] = Field(
        default=None,
    )


class LeadFormsFormResponse(BaseResponse):
    response: "LeadFormsFormResponseModel"


class LeadFormsLeadResponseModel(BaseModel):
    lead_id: int = Field()

    user_id: int = Field()

    date: int = Field()

    answers: typing.List[LeadFormsAnswer] = Field()

    ad_id: typing.Optional[int] = Field(
        default=None,
    )


class LeadFormsLeadResponse(BaseResponse):
    response: "LeadFormsLeadResponseModel"


class LeadFormsQuestionItemResponseModel(BaseModel):
    key: str = Field()

    type: typing.Literal["input", "textarea", "radio", "checkbox", "select"] = Field()

    label: typing.Optional[str] = Field(
        default=None,
    )

    options: typing.Optional[typing.List[LeadFormsQuestionItemOption]] = Field(
        default=None,
        description="Опции выбора для типов radio, checkbox, select",
    )


class LeadFormsQuestionItemResponse(BaseResponse):
    response: "LeadFormsQuestionItemResponseModel"


class LeadFormsQuestionItemOptionResponseModel(BaseModel):
    label: str = Field()

    key: typing.Optional[str] = Field(
        default=None,
    )


class LeadFormsQuestionItemOptionResponse(BaseResponse):
    response: "LeadFormsQuestionItemOptionResponseModel"
