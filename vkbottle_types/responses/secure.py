from .base_response import BaseResponse
from vkbottle_types.objects import secure
from typing import Optional, Any, List, Union
import typing


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


CheckTokenResponseModel = Optional["secure.TokenChecked"]


GetAppBalanceResponseModel = int


GetSMSHistoryResponseModel = List["secure.SmsNotification"]


GetTransactionsHistoryResponseModel = List["secure.Transaction"]


GetUserLevelResponseModel = List["secure.Level"]


class GiveEventStickerResponseModel(BaseResponse):
    user_id: Optional[int] = None
    status: Optional[str] = None


SendNotificationResponseModel = List[int]
