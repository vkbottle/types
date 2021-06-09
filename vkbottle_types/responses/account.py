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
    response: "ChangePasswordResponseModel" = None


class GetActiveOffersResponse(BaseResponse):
    response: "GetActiveOffersResponseModel" = None


class GetAppPermissionsResponse(BaseResponse):
    response: int = None


class GetBannedResponse(BaseResponse):
    response: "GetBannedResponseModel" = None


class GetCountersResponse(BaseResponse):
    response: AccountAccountCounters = None


class GetInfoResponse(BaseResponse):
    response: AccountInfo = None


class GetProfileInfoResponse(BaseResponse):
    response: AccountUserSettings = None


class GetPushSettingsResponse(BaseResponse):
    response: AccountPushSettings = None


class SaveProfileInfoResponse(BaseResponse):
    response: "SaveProfileInfoResponseModel" = None


class ChangePasswordResponseModel(BaseResponse):
    token: typing.Optional[str] = None
    secret: typing.Optional[str] = None


class GetActiveOffersResponseModel(BaseResponse):
    count: typing.Optional[int] = None
    items: typing.Optional[typing.List["AccountOffer"]] = None


class GetBannedResponseModel(BaseResponse):
    count: typing.Optional[int] = None
    items: typing.Optional[typing.List[int]] = None
    profiles: typing.Optional[typing.List["UsersUserMin"]] = None
    groups: typing.Optional[typing.List["GroupsGroup"]] = None


class SaveProfileInfoResponseModel(BaseResponse):
    changed: typing.Optional["BaseBoolInt"] = None
    name_request: typing.Optional["AccountNameRequest"] = None


for item in locals().copy().values():
    if inspect.isclass(item) and issubclass(item, BaseResponse):
        item.update_forward_refs()
