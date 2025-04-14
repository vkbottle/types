import typing

from vkbottle_types.base_model import BaseModel, Field
from vkbottle_types.responses.base_response import BaseResponse


class AuthRestoreResponseModel(BaseModel):
    success: typing.Optional[int] = Field(
        default=None,
    )
    sid: typing.Optional[str] = Field(
        default=None,
    )


class AuthRestoreResponse(BaseResponse):
    response: "AuthRestoreResponseModel" = Field()
