import typing

from vkbottle_types.base_model import BaseModel, Field
from vkbottle_types.objects import (
    AccountAccountCounters,
    AccountInfo,
    AccountNameRequest,
    AccountOffer,
    AccountPushSettings,
    AccountUserSettings,
    GroupsGroup,
    UsersUserFull,
)
from vkbottle_types.responses.base_response import BaseResponse


class AccountChangePasswordResponseModel(BaseModel):
    token: str = Field()
    secret: typing.Optional[str] = Field(
        default=None,
    )


class AccountChangePasswordResponse(BaseResponse):
    response: "AccountChangePasswordResponseModel" = Field()


class AccountGetActiveOffersResponseModel(BaseModel):
    count: int = Field()
    items: typing.List["AccountOffer"] = Field()


class AccountGetActiveOffersResponse(BaseResponse):
    response: "AccountGetActiveOffersResponseModel" = Field()


class AccountGetAppPermissionsResponse(BaseResponse):
    response: int = Field()


class AccountGetBannedResponseModel(BaseModel):
    count: int = Field()
    items: typing.List[int] = Field()
    profiles: typing.Optional[typing.List["UsersUserFull"]] = Field(
        default=None,
    )
    groups: typing.Optional[typing.List["GroupsGroup"]] = Field(
        default=None,
    )


class AccountGetBannedResponse(BaseResponse):
    response: "AccountGetBannedResponseModel" = Field()


class AccountGetCountersResponse(BaseResponse):
    response: "AccountAccountCounters" = Field()


class AccountGetInfoResponse(BaseResponse):
    response: "AccountInfo" = Field()


class AccountGetProfileInfoResponse(BaseResponse):
    response: "AccountUserSettings" = Field()


class AccountGetPushSettingsResponse(BaseResponse):
    response: "AccountPushSettings" = Field()


class AccountSaveProfileInfoResponseModel(BaseModel):
    changed: bool = Field()
    name_request: typing.Optional["AccountNameRequest"] = Field(
        default=None,
    )


class AccountSaveProfileInfoResponse(BaseResponse):
    response: "AccountSaveProfileInfoResponseModel" = Field()
