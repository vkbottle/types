import typing
from vkbottle_types.responses.base_response import BaseResponse, BaseModel
from vkbottle_types.base_model import Field

from vkbottle_types.objects import WallCommentAttachment, BaseLikesInfo, BaseBoolInt


class BoardDefaultOrderResponseModel(enum.IntEnum):
    DESC_UPDATED = 1

    DESC_CREATED = 2

    ASC_UPDATED = -1

    ASC_CREATED = -2


class BoardDefaultOrderResponse(BaseResponse):
    response: "BoardDefaultOrderResponseModel"


class BoardTopicResponseModel(BaseModel):
    comments: typing.Optional[int] = Field(
        default=None,
        description="Comments number",
    )

    created: typing.Optional[int] = Field(
        default=None,
        description="Date when the topic has been created in Unixtime",
    )

    created_by: typing.Optional[int] = Field(
        default=None,
        description="Creator ID",
    )

    id: typing.Optional[int] = Field(
        default=None,
        description="Topic ID",
    )

    is_closed: typing.Optional[bool] = Field(
        default=None,
        description="Information whether the topic is closed",
    )

    is_fixed: typing.Optional[bool] = Field(
        default=None,
        description="Information whether the topic is fixed",
    )

    title: typing.Optional[str] = Field(
        default=None,
        description="Topic title",
    )

    updated: typing.Optional[int] = Field(
        default=None,
        description="Date when the topic has been updated in Unixtime",
    )

    updated_by: typing.Optional[int] = Field(
        default=None,
        description="ID of user who updated the topic",
    )

    first_comment: typing.Optional[str] = Field(
        default=None,
        description="First comment text",
    )

    last_comment: typing.Optional[str] = Field(
        default=None,
        description="Last comment text",
    )


class BoardTopicResponse(BaseResponse):
    response: "BoardTopicResponseModel"


class BoardTopicCommentResponseModel(BaseModel):
    date: int = Field(
        description="Date when the comment has been added in Unixtime",
    )

    from_id: int = Field(
        description="Author ID",
    )

    id: int = Field(
        description="Comment ID",
    )

    text: str = Field(
        description="Comment text",
    )

    attachments: typing.Optional[typing.List[WallCommentAttachment]] = Field(
        default=None,
    )

    real_offset: typing.Optional[int] = Field(
        default=None,
        description="Real position of the comment",
    )

    can_edit: typing.Optional[bool] = Field(
        default=None,
        description="Information whether current user can edit the comment",
    )

    likes: typing.Optional["BaseLikesInfo"] = Field(
        default=None,
    )


class BoardTopicCommentResponse(BaseResponse):
    response: "BoardTopicCommentResponseModel"
