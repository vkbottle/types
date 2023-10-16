import typing
from vkbottle_types.responses.base_response import BaseResponse, BaseModel
from vkbottle_types.base_model import Field


class OwnerStateResponseModel(BaseModel):
    state: typing.Optional[int] = Field(
        default=None,
    )

    description: typing.Optional[str] = Field(
        default=None,
        description="wiki text to describe user state",
    )


class OwnerStateResponse(BaseResponse):
    response: "OwnerStateResponseModel"
