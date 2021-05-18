import inspect
import typing

from vkbottle_types.objects import (
    AppsApp,
    BaseBoolInt,
    GroupsGroup,
    NotificationsNotificationItem,
    NotificationsSendMessageItem,
    PhotosPhoto,
    UsersUser,
    VideoVideo,
)

from .base_response import BaseResponse


class GetResponse(BaseResponse):
    response: typing.Optional["GetResponseModel"] = None


class MarkAsViewedResponse(BaseResponse):
    response: typing.Optional["MarkAsViewedResponseModel"] = None


class SendMessageResponse(BaseResponse):
    response: typing.Optional["SendMessageResponseModel"] = None


class GetResponseModel(BaseResponse):
    count: typing.Optional[int] = None
    items: typing.Optional[typing.List["NotificationsNotificationItem"]] = None
    profiles: typing.Optional[typing.List["UsersUser"]] = None
    groups: typing.Optional[typing.List["GroupsGroup"]] = None
    last_viewed: typing.Optional[int] = None
    photos: typing.Optional[typing.List["PhotosPhoto"]] = None
    videos: typing.Optional[typing.List["VideoVideo"]] = None
    apps: typing.Optional[typing.List["AppsApp"]] = None
    next_from: typing.Optional[str] = None
    ttl: typing.Optional[int] = None


MarkAsViewedResponseModel = BaseBoolInt


SendMessageResponseModel = typing.List[NotificationsSendMessageItem]


for item in locals().copy().values():
    if inspect.isclass(item) and issubclass(item, BaseResponse):
        item.update_forward_refs()
