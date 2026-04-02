from vkbottle_types.base_model import Field
from vkbottle_types.objects import (
    SecureGiveEventStickerItem,
    SecureLevel,
    SecureSetCounterItem,
    SecureSmsNotification,
    SecureTokenChecked,
    SecureTransaction,
)
from vkbottle_types.responses.base_response import BaseResponse


class SecureCheckTokenResponse(BaseResponse):
    response: "SecureTokenChecked" = Field()


class SecureGetAppBalanceResponse(BaseResponse):
    response: int = Field()


class SecureGetSMSHistoryResponse(BaseResponse):
    response: list["SecureSmsNotification"] = Field()


class SecureGetTransactionsHistoryResponse(BaseResponse):
    response: list["SecureTransaction"] = Field()


class SecureGetUserLevelResponse(BaseResponse):
    response: list["SecureLevel"] = Field()


class SecureGiveEventStickerResponse(BaseResponse):
    response: list["SecureGiveEventStickerItem"] = Field()


class SecureSendNotificationResponse(BaseResponse):
    response: list[int] = Field()


class SecureSetCounterArrayResponse(BaseResponse):
    response: list["SecureSetCounterItem"] = Field()


__all__ = (
    "SecureCheckTokenResponse",
    "SecureGetAppBalanceResponse",
    "SecureGetSMSHistoryResponse",
    "SecureGetTransactionsHistoryResponse",
    "SecureGetUserLevelResponse",
    "SecureGiveEventStickerResponse",
    "SecureSendNotificationResponse",
    "SecureSetCounterArrayResponse",
)
