import typing
from vkbottle_types.responses.base_response import BaseResponse, BaseModel
from vkbottle_types.base_model import Field

from vkbottle_types.objects import BaseBoolInt


class SecureGiveEventStickerItemResponseModel(BaseModel):
    user_id: typing.Optional[int] = Field(
        default=None,
    )

    status: typing.Optional[str] = Field(
        default=None,
    )


class SecureGiveEventStickerItemResponse(BaseResponse):
    response: "SecureGiveEventStickerItemResponseModel"


class SecureLevelResponseModel(BaseModel):
    level: typing.Optional[int] = Field(
        default=None,
        description="Level",
    )

    uid: typing.Optional[int] = Field(
        default=None,
        description="User ID",
    )


class SecureLevelResponse(BaseResponse):
    response: "SecureLevelResponseModel"


class SecureSetCounterItemResponseModel(BaseModel):
    id: int = Field(
        description="User ID",
    )

    result: bool = Field()


class SecureSetCounterItemResponse(BaseResponse):
    response: "SecureSetCounterItemResponseModel"


class SecureSmsNotificationResponseModel(BaseModel):
    app_id: typing.Optional[str] = Field(
        default=None,
        description="Application ID",
    )

    date: typing.Optional[str] = Field(
        default=None,
        description="Date when message has been sent in Unixtime",
    )

    id: typing.Optional[str] = Field(
        default=None,
        description="Notification ID",
    )

    message: typing.Optional[str] = Field(
        default=None,
        description="Messsage text",
    )

    user_id: typing.Optional[str] = Field(
        default=None,
        description="User ID",
    )


class SecureSmsNotificationResponse(BaseResponse):
    response: "SecureSmsNotificationResponseModel"


class SecureTokenCheckedResponseModel(BaseModel):
    date: typing.Optional[int] = Field(
        default=None,
        description="Date when access_token has been generated in Unixtime",
    )

    expire: typing.Optional[int] = Field(
        default=None,
        description="Date when access_token will expire in Unixtime",
    )

    success: typing.Optional[int] = Field(
        default=None,
        description="Returns if successfully processed",
    )

    user_id: typing.Optional[int] = Field(
        default=None,
        description="User ID",
    )


class SecureTokenCheckedResponse(BaseResponse):
    response: "SecureTokenCheckedResponseModel"


class SecureTransactionResponseModel(BaseModel):
    date: typing.Optional[int] = Field(
        default=None,
        description="Transaction date in Unixtime",
    )

    id: typing.Optional[int] = Field(
        default=None,
        description="Transaction ID",
    )

    uid_from: typing.Optional[int] = Field(
        default=None,
        description="From ID",
    )

    uid_to: typing.Optional[int] = Field(
        default=None,
        description="To ID",
    )

    votes: typing.Optional[int] = Field(
        default=None,
        description="Votes number",
    )


class SecureTransactionResponse(BaseResponse):
    response: "SecureTransactionResponseModel"
