import typing

from vkbottle_types.base_model import BaseModel, Field
from vkbottle_types.objects import CallsShortCredentials
from vkbottle_types.responses.base_response import BaseResponse


class CallsStartResponseModel(BaseModel):
    join_link: str = Field()
    ok_join_link: str = Field()
    call_id: typing.Optional[str] = Field(
        default=None,
    )
    broadcast_video_id: typing.Optional[str] = Field(
        default=None,
    )
    broadcast_ov_id: typing.Optional[str] = Field(
        default=None,
    )
    short_credentials: typing.Optional["CallsShortCredentials"] = Field(
        default=None,
    )


class CallsStartResponse(BaseResponse):
    response: "CallsStartResponseModel" = Field()
