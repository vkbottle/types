import typing
from vkbottle_types.responses.base_response import BaseResponse, BaseModel
from vkbottle_types.base_model import Field


class OauthErrorResponseModel(BaseModel):
    error: str = Field(
        description="Error type",
    )

    error_description: str = Field(
        description="Error description",
    )

    redirect_uri: typing.Optional[str] = Field(
        default=None,
        description="URI for validation",
    )


class OauthErrorResponse(BaseResponse):
    response: "OauthErrorResponseModel"
