from vkbottle_types.base_model import BaseModel, Field
from vkbottle_types.responses.base_response import BaseResponse


class AuthRestoreResponseModel(BaseModel):
    success: int | None = Field(
        default=None,
    )
    sid: str | None = Field(
        default=None,
    )


class AuthRestoreResponse(BaseResponse):
    response: "AuthRestoreResponseModel" = Field()


__all__ = (
    "AuthRestoreResponse",
    "AuthRestoreResponseModel",
)
