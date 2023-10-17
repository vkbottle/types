import typing
import enum
from vkbottle_types.responses.base_response import BaseResponse, BaseModel
from vkbottle_types.base_model import Field

from vkbottle_types.objects import CallsParticipants, CallsEndState


class CallsCallResponseModel(BaseModel):
    initiator_id: int = Field(
        description="Caller initiator",
    )

    receiver_id: int = Field(
        description="Caller receiver",
    )

    state: "CallsEndState" = Field()

    time: int = Field(
        description="Timestamp for call",
    )

    duration: typing.Optional[int] = Field(
        default=None,
        description="Call duration",
    )

    video: typing.Optional[bool] = Field(
        default=None,
        description="Was this call initiated as video call",
    )

    participants: typing.Optional["CallsParticipants"] = Field(
        default=None,
    )


class CallsCallResponse(BaseResponse):
    response: "CallsCallResponseModel"


class CallsEndStateResponseModel(enum.Enum):
    CANCELED_BY_INITIATOR = "canceled_by_initiator"

    CANCELED_BY_RECEIVER = "canceled_by_receiver"

    REACHED = "reached"


class CallsEndStateResponse(BaseResponse):
    response: "CallsEndStateResponseModel"


class CallsParticipantsResponseModel(BaseModel):
    list: typing.Optional[typing.List[int]] = Field(
        default=None,
    )

    count: typing.Optional[int] = Field(
        default=None,
        description="Participants count",
    )


class CallsParticipantsResponse(BaseResponse):
    response: "CallsParticipantsResponseModel"
