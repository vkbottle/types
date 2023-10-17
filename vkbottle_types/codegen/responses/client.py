import typing
import enum
from vkbottle_types.responses.base_response import BaseResponse, BaseModel
from vkbottle_types.base_model import Field

from vkbottle_types.objects import MessagesTemplateActionTypeNames


class ClientInfoForBotsResponseModel(BaseModel):
    button_actions: typing.Optional[
        typing.List[MessagesTemplateActionTypeNames]
    ] = Field(
        default=None,
    )

    keyboard: typing.Optional[bool] = Field(
        default=None,
        description="client has support keyboard",
    )

    inline_keyboard: typing.Optional[bool] = Field(
        default=None,
        description="client has support inline keyboard",
    )

    carousel: typing.Optional[bool] = Field(
        default=None,
        description="client has support carousel",
    )

    lang_id: typing.Optional[int] = Field(
        default=None,
        description="client or user language id",
    )


class ClientInfoForBotsResponse(BaseResponse):
    response: "ClientInfoForBotsResponseModel"
