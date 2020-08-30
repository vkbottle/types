from typing import Optional, List

from vkbottle_types.objects import (
    SecureTokenChecked,
    SecureTransaction,
    SecureLevel,
    SecureSmsNotification,
)
from .base_response import BaseResponse


class CheckTokenResponse(BaseResponse):
    response: Optional["CheckTokenResponseModel"] = None


class GetAppBalanceResponse(BaseResponse):
    response: Optional["GetAppBalanceResponseModel"] = None


class GetSMSHistoryResponse(BaseResponse):
    response: Optional["GetSMSHistoryResponseModel"] = None


class GetTransactionsHistoryResponse(BaseResponse):
    response: Optional["GetTransactionsHistoryResponseModel"] = None


class GetUserLevelResponse(BaseResponse):
    response: Optional["GetUserLevelResponseModel"] = None


class GiveEventStickerResponse(BaseResponse):
    response: Optional["GiveEventStickerResponseModel"] = None


class SendNotificationResponse(BaseResponse):
    response: Optional["SendNotificationResponseModel"] = None


CheckTokenResponseModel = Optional[SecureTokenChecked]

GetAppBalanceResponseModel = int

GetSMSHistoryResponseModel = List[SecureSmsNotification]

GetTransactionsHistoryResponseModel = List[SecureTransaction]

GetUserLevelResponseModel = List[SecureLevel]


class GiveEventStickerResponseModel(BaseResponse):
    user_id: Optional[int] = None
    status: Optional[str] = None


SendNotificationResponseModel = List[int]


CheckTokenResponse.update_forward_refs()
GetAppBalanceResponse.update_forward_refs()
GetSMSHistoryResponse.update_forward_refs()
GetTransactionsHistoryResponse.update_forward_refs()
GetUserLevelResponse.update_forward_refs()
GiveEventStickerResponse.update_forward_refs()
SendNotificationResponse.update_forward_refs()
