import typing
from typing import Optional

from vkbottle_types.objects import groups, account, base, users
from .base_response import BaseResponse


class ChangePasswordResponse(BaseResponse):
    response: Optional["ChangePasswordResponseModel"] = None


class GetActiveOffersResponse(BaseResponse):
    response: Optional["GetActiveOffersResponseModel"] = None


class GetAppPermissionsResponse(BaseResponse):
    response: Optional[int] = None


class GetBannedResponse(BaseResponse):
    response: Optional["GetBannedResponseModel"] = None


class GetCountersResponse(BaseResponse):
    response: Optional[typing.List["account.AccountCounters"]] = None


class GetInfoResponse(BaseResponse):
    response: Optional[typing.List["account.Info"]] = None


class GetProfileInfoResponse(BaseResponse):
    response: Optional[typing.List["account.UserSettings"]] = None


class GetPushSettingsResponse(BaseResponse):
    response: Optional[typing.List["account.PushSettings"]] = None


class SaveProfileInfoResponse(BaseResponse):
    response: Optional["SaveProfileInfoResponseModel"] = None


class ChangePasswordResponseModel(BaseResponse):
    token: Optional[str] = None
    secret: Optional[str] = None


class GetActiveOffersResponseModel(BaseResponse):
    count: Optional[int] = None
    items: Optional[typing.List["account.Offer"]] = None


class GetBannedResponseModel(BaseResponse):
    count: Optional[int] = None
    items: Optional[typing.List[int]] = None
    profiles: Optional[typing.List["users.UserMin"]] = None
    groups: Optional[typing.List["groups.Group"]] = None


class SaveProfileInfoResponseModel(BaseResponse):
    changed: Optional[typing.List["base.BoolInt"]] = None
    name_request: Optional[typing.List["account.NameRequest"]] = None
