from vkbottle_types.base_model import BaseModel, Field
from vkbottle_types.objects import (
    AppsApp,
    GroupsGroup,
    NotificationsNotificationItem,
    NotificationsSendMessageItem,
    PhotosPhoto,
    UsersUser,
    VideoVideoFull,
)
from vkbottle_types.responses.base_response import BaseResponse


class NotificationsGetResponseModel(BaseModel):
    count: int = Field()
    items: list["NotificationsNotificationItem"] = Field()
    profiles: list["UsersUser"] | None = Field(
        default=None,
    )
    groups: list["GroupsGroup"] | None = Field(
        default=None,
    )
    last_viewed: int | None = Field(
        default=None,
    )
    photos: list["PhotosPhoto"] | None = Field(
        default=None,
    )
    videos: list["VideoVideoFull"] | None = Field(
        default=None,
    )
    apps: list["AppsApp"] | None = Field(
        default=None,
    )
    next_from: str | None = Field(
        default=None,
    )
    ttl: int | None = Field(
        default=None,
    )


class NotificationsGetResponse(BaseResponse):
    response: "NotificationsGetResponseModel" = Field()


class NotificationsSendMessageResponse(BaseResponse):
    response: list["NotificationsSendMessageItem"] = Field()


__all__ = (
    "NotificationsGetResponse",
    "NotificationsGetResponseModel",
    "NotificationsSendMessageResponse",
)
