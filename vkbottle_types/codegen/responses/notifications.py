import typing
from vkbottle_types.responses.base_response import BaseResponse, BaseModel
from vkbottle_types.base_model import Field

from vkbottle_types.objects import (
    NotificationsNotification,
    BaseLikesInfo,
    WallWallpostAttachment,
    NotificationsReply,
    NotificationsSendMessageError,
    BaseGeo,
    NotificationsFeedback,
)


class NotificationsFeedbackResponseModel(BaseModel):
    attachments: typing.Optional[typing.List[WallWallpostAttachment]] = Field(
        default=None,
    )

    from_id: typing.Optional[int] = Field(
        default=None,
        description="Reply author's ID",
    )

    geo: typing.Optional["BaseGeo"] = Field(
        default=None,
    )

    id: typing.Optional[int] = Field(
        default=None,
        description="Item ID",
    )

    likes: typing.Optional["BaseLikesInfo"] = Field(
        default=None,
    )

    text: typing.Optional[str] = Field(
        default=None,
        description="Reply text",
    )

    to_id: typing.Optional[int] = Field(
        default=None,
        description="Wall owner's ID",
    )


class NotificationsFeedbackResponse(BaseResponse):
    response: "NotificationsFeedbackResponseModel"


class NotificationsNotificationResponseModel(BaseModel):
    date: typing.Optional[int] = Field(
        default=None,
        description="Date when the event has been occurred",
    )

    feedback: typing.Optional["NotificationsFeedback"] = Field(
        default=None,
    )

    parent: typing.Optional["NotificationsNotification"] = Field(
        default=None,
    )

    reply: typing.Optional["NotificationsReply"] = Field(
        default=None,
    )

    type: typing.Optional[str] = Field(
        default=None,
        description="Notification type",
    )


class NotificationsNotificationResponse(BaseResponse):
    response: "NotificationsNotificationResponseModel"


class NotificationsNotificationItemResponseModel(BaseModel):
    pass


class NotificationsNotificationItemResponse(BaseResponse):
    response: "NotificationsNotificationItemResponseModel"


class NotificationsReplyResponseModel(BaseModel):
    date: typing.Optional[int] = Field(
        default=None,
        description="Date when the reply has been created in Unixtime",
    )

    id: typing.Optional[int] = Field(
        default=None,
        description="Reply ID",
    )

    text: typing.Optional[int] = Field(
        default=None,
        description="Reply text",
    )


class NotificationsReplyResponse(BaseResponse):
    response: "NotificationsReplyResponseModel"


class NotificationsSendMessageErrorResponseModel(BaseModel):
    code: typing.Optional[int] = Field(
        default=None,
        description="Error code",
    )

    description: typing.Optional[str] = Field(
        default=None,
        description="Error description",
    )


class NotificationsSendMessageErrorResponse(BaseResponse):
    response: "NotificationsSendMessageErrorResponseModel"


class NotificationsSendMessageItemResponseModel(BaseModel):
    user_id: typing.Optional[int] = Field(
        default=None,
        description="User ID",
    )

    status: typing.Optional[bool] = Field(
        default=None,
        description="Notification status",
    )

    error: typing.Optional["NotificationsSendMessageError"] = Field(
        default=None,
    )


class NotificationsSendMessageItemResponse(BaseResponse):
    response: "NotificationsSendMessageItemResponseModel"
