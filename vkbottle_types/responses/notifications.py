from .base_response import BaseResponse
from vkbottle_types.objects import (
    users,
    groups,
    apps,
    photos,
    video,
    notifications,
    base,
)
from typing import Optional, Any, List, Union
import typing


class GetResponse(BaseResponse):
    response: Optional["GetResponseModel"] = None


class MarkAsViewedResponse(BaseResponse):
    response: Optional["MarkAsViewedResponseModel"] = None


class SendMessageResponse(BaseResponse):
    response: Optional["SendMessageResponseModel"] = None


class GetResponseModel(BaseResponse):
    count: Optional[int] = None
    items: Optional[List["notifications.NotificationItem"]] = None
    profiles: Optional[List["users.User"]] = None
    groups: Optional[List["groups.Group"]] = None
    last_viewed: Optional[int] = None
    photos: Optional[List["photos.Photo"]] = None
    videos: Optional[List["video.Video"]] = None
    apps: Optional[List["apps.App"]] = None
    next_from: Optional[str] = None
    ttl: Optional[int] = None


MarkAsViewedResponseModel = Optional["base.BoolInt"]


SendMessageResponseModel = List["notifications.SendMessageItem"]
