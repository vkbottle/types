from typing import Optional, List

from vkbottle_types.objects import (
    AccountNameRequest,
    AccountOffer,
    UsersUserMin,
    AccountPushSettings,
    AccountInfo,
    AccountUserSettings,
    GroupsGroup,
    BaseBoolInt,
    AccountAccountCounters,
)
from .base_response import BaseResponse


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
    items: Optional[List["AccountOffer"]] = None


GetAppPermissionsResponseModel = int


class GetBannedResponseModel(BaseResponse):
    count: Optional[int] = None
    items: Optional[List[int]] = None
    profiles: Optional[List["UsersUserMin"]] = None
    groups: Optional[List["GroupsGroup"]] = None


GetCountersResponseModel = Optional[AccountAccountCounters]

GetInfoResponseModel = Optional[AccountInfo]

GetProfileInfoResponseModel = Optional[AccountUserSettings]

GetPushSettingsResponseModel = Optional[AccountPushSettings]


class SaveProfileInfoResponseModel(BaseResponse):
    changed: Optional["BaseBoolInt"] = None
    name_request: Optional["AccountNameRequest"] = None


ChangePasswordResponse.update_forward_refs()
GetActiveOffersResponse.update_forward_refs()
GetAppPermissionsResponse.update_forward_refs()
GetBannedResponse.update_forward_refs()
GetCountersResponse.update_forward_refs()
GetInfoResponse.update_forward_refs()
GetProfileInfoResponse.update_forward_refs()
GetPushSettingsResponse.update_forward_refs()
SaveProfileInfoResponse.update_forward_refs()
