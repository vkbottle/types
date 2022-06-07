import typing

from vkbottle_types.objects import (
    SecureGiveEventStickerItem,
    SecureLevel,
    SecureSetCounterItem,
    SecureSmsNotification,
    SecureTokenChecked,
    SecureTransaction,
)
from vkbottle_types.responses.base_response import BaseResponse


class CheckTokenResponse(BaseResponse):
    response: SecureTokenChecked


class GetAppBalanceResponse(BaseResponse):
    response: int


class GetSMSHistoryResponse(BaseResponse):
    response: typing.List["SecureSmsNotification"]


class GetTransactionsHistoryResponse(BaseResponse):
    response: typing.List["SecureTransaction"]


class GetUserLevelResponse(BaseResponse):
    response: typing.List["SecureLevel"]


class GiveEventStickerResponse(BaseResponse):
    response: typing.List["SecureGiveEventStickerItem"]


class SendNotificationResponse(BaseResponse):
    response: typing.List[int]


class SetCounterArrayResponse(BaseResponse):
    response: typing.List["SecureSetCounterItem"]


__all__ = (
    "CheckTokenResponse",
    "GetAppBalanceResponse",
    "GetSMSHistoryResponse",
    "GetTransactionsHistoryResponse",
    "GetUserLevelResponse",
    "GiveEventStickerResponse",
    "SecureGiveEventStickerItem",
    "SecureLevel",
    "SecureSetCounterItem",
    "SecureSmsNotification",
    "SecureTokenChecked",
    "SecureTransaction",
    "SendNotificationResponse",
    "SetCounterArrayResponse",
)
