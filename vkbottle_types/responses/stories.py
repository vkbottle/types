import typing
from typing import Optional

from vkbottle_types.objects import groups, users, stories
from .base_response import BaseResponse


class GetBannedExtendedResponse(BaseResponse):
    response: Optional["GetBannedExtendedResponseModel"] = None


class GetBannedResponse(BaseResponse):
    response: Optional["GetBannedResponseModel"] = None


class GetByIdExtendedResponse(BaseResponse):
    response: Optional["GetByIdExtendedResponseModel"] = None


class GetByIdResponse(BaseResponse):
    response: Optional["GetByIdResponseModel"] = None


class GetPhotoUploadServerResponse(BaseResponse):
    response: Optional["GetPhotoUploadServerResponseModel"] = None


class GetStatsResponse(BaseResponse):
    response: Optional[typing.List["stories.StoryStats"]] = None


class GetVideoUploadServerResponse(BaseResponse):
    response: Optional["GetVideoUploadServerResponseModel"] = None


class GetViewersExtendedV5115Response(BaseResponse):
    response: Optional["GetViewersExtendedV5115ResponseModel"] = None


class GetViewersExtendedResponse(BaseResponse):
    response: Optional["GetViewersExtendedResponseModel"] = None


class GetV5113Response(BaseResponse):
    response: Optional["GetV5113ResponseModel"] = None


class GetResponse(BaseResponse):
    response: Optional["GetResponseModel"] = None


class UploadResponse(BaseResponse):
    response: Optional["UploadResponseModel"] = None


class GetBannedExtendedResponseModel(BaseResponse):
    count: Optional[int] = None
    items: Optional[typing.List[int]] = None
    profiles: Optional[typing.List["users.UserFull"]] = None
    groups: Optional[typing.List["groups.GroupFull"]] = None


class GetBannedResponseModel(BaseResponse):
    count: Optional[int] = None
    items: Optional[typing.List[int]] = None


class GetByIdExtendedResponseModel(BaseResponse):
    count: Optional[int] = None
    items: Optional[typing.List["stories.Story"]] = None
    profiles: Optional[typing.List["users.UserFull"]] = None
    groups: Optional[typing.List["groups.GroupFull"]] = None


class GetByIdResponseModel(BaseResponse):
    count: Optional[int] = None
    items: Optional[typing.List["stories.Story"]] = None


class GetPhotoUploadServerResponseModel(BaseResponse):
    upload_url: Optional[str] = None
    user_ids: Optional[typing.List[int]] = None


class GetVideoUploadServerResponseModel(BaseResponse):
    upload_url: Optional[str] = None
    user_ids: Optional[typing.List[int]] = None


class GetViewersExtendedV5115ResponseModel(BaseResponse):
    count: Optional[int] = None
    items: Optional[typing.List["stories.ViewersItem"]] = None
    hidden_reason: Optional[str] = None


class GetViewersExtendedResponseModel(BaseResponse):
    count: Optional[int] = None
    items: Optional[typing.List["users.UserFull"]] = None


class GetV5113ResponseModel(BaseResponse):
    count: Optional[int] = None
    items: Optional[typing.List["stories.FeedItem"]] = None
    profiles: Optional[typing.List["users.User"]] = None
    groups: Optional[typing.List["groups.Group"]] = None
    need_upload_screen: Optional[bool] = None


class GetResponseModel(BaseResponse):
    count: Optional[int] = None
    promo_data: Optional[typing.List["stories.PromoBlock"]] = None
    profiles: Optional[typing.List["users.User"]] = None
    groups: Optional[typing.List["groups.Group"]] = None
    need_upload_screen: Optional[bool] = None
    items: Optional[typing.List[typing.List[stories.Story]]] = None


class UploadResponseModel(BaseResponse):
    upload_result: Optional[str] = None
