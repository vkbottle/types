from .base_response import BaseResponse
from vkbottle_types.objects import users, account, base, groups
from typing import Optional, Any, List, Union
import typing


class ChangePasswordResponse(BaseResponse):
    response: Optional["ChangePasswordResponseModel"] = None


class GetActiveOffersResponse(BaseResponse):
    response: Optional["GetActiveOffersResponseModel"] = None


class GetAppPermissionsResponse(BaseResponse):
    response: Optional["GetAppPermissionsResponseModel"] = None


class GetBannedResponse(BaseResponse):
    response: Optional["GetBannedResponseModel"] = None


class GetCountersResponse(BaseResponse):
    response: Optional["GetCountersResponseModel"] = None


class GetInfoResponse(BaseResponse):
    response: Optional["GetInfoResponseModel"] = None


class GetProfileInfoResponse(BaseResponse):
    response: Optional["GetProfileInfoResponseModel"] = None


class GetPushSettingsResponse(BaseResponse):
    response: Optional["GetPushSettingsResponseModel"] = None


class SaveProfileInfoResponse(BaseResponse):
    response: Optional["SaveProfileInfoResponseModel"] = None


class ChangePasswordResponseModel(BaseResponse):
    token: Optional[str] = None
    secret: Optional[str] = None


class GetActiveOffersResponseModel(BaseResponse):
    count: Optional[int] = None
    items: Optional[List["account.Offer"]] = None


GetAppPermissionsResponseModel = int


class GetBannedResponseModel(BaseResponse):
    count: Optional[int] = None
    items: Optional[List[int]] = None
    profiles: Optional[List["users.UserMin"]] = None
    groups: Optional[List["groups.Group"]] = None


GetCountersResponseModel = Optional["account.AccountCounters"]


GetInfoResponseModel = Optional["account.Info"]


GetProfileInfoResponseModel = Optional["account.UserSettings"]


GetPushSettingsResponseModel = Optional["account.PushSettings"]


class SaveProfileInfoResponseModel(BaseResponse):
    changed: Optional["base.BoolInt"] = None
    name_request: Optional["account.NameRequest"] = None
