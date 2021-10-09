import inspect
import typing
from .base_response import BaseResponse
from vkbottle_types.objects import (
    GroupsGroup,
    GroupsGroupFull,
    StoriesFeedItem,
    StoriesPromoBlock,
    StoriesStory,
    StoriesStoryStats,
    StoriesViewersItem,
    UsersUser,
    UsersUserFull
)


class GetBannedExtendedResponse(BaseResponse):
    response: "GetBannedExtendedResponseModel" = None


class GetBannedResponse(BaseResponse):
    response: "GetBannedResponseModel" = None


class GetByIdExtendedResponse(BaseResponse):
    response: "GetByIdExtendedResponseModel" = None


class GetByIdResponse(BaseResponse):
    response: "GetByIdResponseModel" = None


class GetPhotoUploadServerResponse(BaseResponse):
    response: "GetPhotoUploadServerResponseModel" = None


class GetStatsResponse(BaseResponse):
    response: StoriesStoryStats = None


class GetVideoUploadServerResponse(BaseResponse):
    response: "GetVideoUploadServerResponseModel" = None


class GetViewersExtendedV5115Response(BaseResponse):
    response: "GetViewersExtendedV5115ResponseModel" = None


class GetViewersExtendedResponse(BaseResponse):
    response: "GetViewersExtendedResponseModel" = None


class GetV5113Response(BaseResponse):
    response: "GetV5113ResponseModel" = None


class GetResponse(BaseResponse):
    response: "GetResponseModel" = None


class SaveResponse(BaseResponse):
    response: "SaveResponseModel" = None


class UploadResponse(BaseResponse):
    response: "UploadResponseModel" = None


class GetBannedExtendedResponseModel(BaseResponse):
    count: typing.Optional[int] = None
    items: typing.Optional[typing.List[int]] = None
    profiles: typing.Optional[typing.List["UsersUserFull"]] = None
    groups: typing.Optional[typing.List["GroupsGroupFull"]] = None


class GetBannedResponseModel(BaseResponse):
    count: typing.Optional[int] = None
    items: typing.Optional[typing.List[int]] = None


class GetByIdExtendedResponseModel(BaseResponse):
    count: typing.Optional[int] = None
    items: typing.Optional[typing.List["StoriesStory"]] = None
    profiles: typing.Optional[typing.List["UsersUserFull"]] = None
    groups: typing.Optional[typing.List["GroupsGroupFull"]] = None


class GetByIdResponseModel(BaseResponse):
    count: typing.Optional[int] = None
    items: typing.Optional[typing.List["StoriesStory"]] = None


class GetPhotoUploadServerResponseModel(BaseResponse):
    upload_url: typing.Optional[str] = None
    user_ids: typing.Optional[typing.List[int]] = None


class GetVideoUploadServerResponseModel(BaseResponse):
    upload_url: typing.Optional[str] = None
    user_ids: typing.Optional[typing.List[int]] = None


class GetViewersExtendedV5115ResponseModel(BaseResponse):
    count: typing.Optional[int] = None
    items: typing.Optional[typing.List["StoriesViewersItem"]] = None
    hidden_reason: typing.Optional[str] = None
    next_from: typing.Optional[str] = None


class GetViewersExtendedResponseModel(BaseResponse):
    count: typing.Optional[int] = None
    items: typing.Optional[typing.List["UsersUserFull"]] = None


class GetV5113ResponseModel(BaseResponse):
    count: typing.Optional[int] = None
    items: typing.Optional[typing.List["StoriesFeedItem"]] = None
    profiles: typing.Optional[typing.List["UsersUserFull"]] = None
    groups: typing.Optional[typing.List["GroupsGroup"]] = None
    need_upload_screen: typing.Optional[bool] = None


class GetResponseModel(BaseResponse):
    count: typing.Optional[int] = None
    items: typing.Optional[typing.List["list"]] = None
    promo_data: typing.Optional["StoriesPromoBlock"] = None
    profiles: typing.Optional[typing.List["UsersUserFull"]] = None
    groups: typing.Optional[typing.List["GroupsGroup"]] = None
    need_upload_screen: typing.Optional[bool] = None


class SaveResponseModel(BaseResponse):
    count: typing.Optional[int] = None
    items: typing.Optional[typing.List["StoriesStory"]] = None
    profiles: typing.Optional[typing.List["UsersUser"]] = None
    groups: typing.Optional[typing.List["GroupsGroup"]] = None


class UploadResponseModel(BaseResponse):
    upload_result: typing.Optional[str] = None


for item in locals().copy().values():
    if inspect.isclass(item) and issubclass(item, BaseResponse):
        item.update_forward_refs()
