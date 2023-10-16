import typing
from vkbottle_types.responses.base_response import BaseResponse, BaseModel
from vkbottle_types.base_model import Field


class LinkTargetObjectResponseModel(BaseModel):
    type: typing.Optional[str] = Field(
        default=None,
        description="Object type",
    )

    owner_id: typing.Optional[int] = Field(
        default=None,
        description="Owner ID",
    )

    item_id: typing.Optional[int] = Field(
        default=None,
        description="Item ID",
    )


class LinkTargetObjectResponse(BaseResponse):
    response: "LinkTargetObjectResponseModel"
