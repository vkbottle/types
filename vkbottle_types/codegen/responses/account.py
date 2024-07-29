import typing

from vkbottle_types.base_model import Field
from vkbottle_types.objects import (
    AccountAccountCounters,
    AccountInfo,
    AccountPushSettings,
    AccountUserSettings,
)
from vkbottle_types.responses.base_response import BaseResponse


class AccountChangePasswordResponse(BaseResponse):
    response: typing.Dict[str, typing.Any] = Field()


class AccountGetActiveOffersResponse(BaseResponse):
    response: typing.Dict[str, typing.Any] = Field()


class AccountGetAppPermissionsResponse(BaseResponse):
    response: int = Field()


class AccountGetBannedResponse(BaseResponse):
    response: typing.Dict[str, typing.Any] = Field()


class AccountGetCountersResponse(BaseResponse):
    response: "AccountAccountCounters" = Field()


class AccountGetInfoResponse(BaseResponse):
    response: "AccountInfo" = Field()


class AccountGetProfileInfoResponse(BaseResponse):
    response: "AccountUserSettings" = Field()


class AccountGetPushSettingsResponse(BaseResponse):
    response: "AccountPushSettings" = Field()


class AccountSaveProfileInfoResponse(BaseResponse):
    response: typing.Dict[str, typing.Any] = Field()
