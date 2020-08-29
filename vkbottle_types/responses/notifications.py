import typing
from typing import Optional

from vkbottle_types.objects import (
    photos,
    notifications,
    video,
    base,
    groups,
    apps,
    users,
)
from .base_response import BaseResponse


class GetResponse(BaseResponse):
    response: Optional["GetResponseModel"] = None


class MarkAsViewedResponse(BaseResponse):
    response: Optional[typing.List["base.BoolInt"]] = None


class SendMessageResponse(BaseResponse):
    response: Optional[typing.List["notifications.SendMessageItem"]] = None


class GetResponseModel(BaseResponse):
    count: Optional[int] = None
    items: Optional[typing.List["notifications.NotificationItem"]] = None
    profiles: Optional[typing.List["users.User"]] = None
    groups: Optional[typing.List["groups.Group"]] = None
    last_viewed: Optional[int] = None
    photos: Optional[typing.List["photos.Photo"]] = None
    videos: Optional[typing.List["video.Video"]] = None
    apps: Optional[typing.List["apps.App"]] = None
    next_from: Optional[str] = None
    ttl: Optional[int] = None
