import typing
from vkbottle_types.responses.base_response import BaseResponse, BaseModel
from vkbottle_types.base_model import Field

from vkbottle_types.objects import GroupsGroupFullMemberStatus


class EventsEventAttachResponseModel(BaseModel):
    button_text: str = Field(
        description="text of attach",
    )

    friends: typing.List[int] = Field(
        description="array of friends ids",
    )

    id: int = Field(
        description="event ID",
    )

    is_favorite: bool = Field(
        description="is favorite",
    )

    text: str = Field(
        description="text of attach",
    )

    address: typing.Optional[str] = Field(
        default=None,
        description="address of event",
    )

    member_status: typing.Optional["GroupsGroupFullMemberStatus"] = Field(
        default=None,
        description="Current user's member status",
    )

    time: typing.Optional[int] = Field(
        default=None,
        description="event start time",
    )


class EventsEventAttachResponse(BaseResponse):
    response: "EventsEventAttachResponseModel"
