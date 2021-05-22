import inspect
import typing
from .base_response import BaseResponse
from vkbottle_types.objects import (
    AccountAccountCounters,
    AccountInfo,
    AccountNameRequest,
    AccountOffer,
    AccountPushSettings,
    AccountUserSettings,
    BaseBoolInt,
    GroupsGroup,
    UsersUserMin
)


class ChangePasswordResponse(BaseResponse):
    response: typing.Optional["ChangePasswordResponseModel"] = None


class GetActiveOffersResponse(BaseResponse):
    response: typing.Optional["GetActiveOffersResponseModel"] = None


class GetAppPermissionsResponse(BaseResponse):
    response: typing.Optional["GetAppPermissionsResponseModel"] = None


class GetBannedResponse(BaseResponse):
    response: typing.Optional["GetBannedResponseModel"] = None


class GetCountersResponse(BaseResponse):
    response: typing.Optional["GetCountersResponseModel"] = None


class GetInfoResponse(BaseResponse):
    response: typing.Optional["GetInfoResponseModel"] = None


class GetProfileInfoResponse(BaseResponse):
    response: typing.Optional["GetProfileInfoResponseModel"] = None


class GetPushSettingsResponse(BaseResponse):
    response: typing.Optional["GetPushSettingsResponseModel"] = None


class SaveProfileInfoResponse(BaseResponse):
    response: typing.Optional["SaveProfileInfoResponseModel"] = None


class ChangePasswordResponseModel(BaseResponse):
    token: typing.Optional[str] = None
    secret: typing.Optional[str] = None


class GetActiveOffersResponseModel(BaseResponse):
    count: typing.Optional[int] = None
    items: typing.Optional[typing.List["AccountOffer"]] = None


GetAppPermissionsResponseModel = int


class GetBannedResponseModel(BaseResponse):
    count: typing.Optional[int] = None
    items: typing.Optional[typing.List[int]] = None
    profiles: typing.Optional[typing.List["UsersUserMin"]] = None
    groups: typing.Optional[typing.List["GroupsGroup"]] = None


GetCountersResponseModel = AccountAccountCounters


GetInfoResponseModel = AccountInfo


GetProfileInfoResponseModel = AccountUserSettings


GetPushSettingsResponseModel = AccountPushSettings


class SaveProfileInfoResponseModel(BaseResponse):
    changed: typing.Optional["BaseBoolInt"] = None
    name_request: typing.Optional["AccountNameRequest"] = None


for item in locals().copy().values():
    if inspect.isclass(item) and issubclass(item, BaseResponse):
        item.update_forward_refs()
