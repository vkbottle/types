import typing
from typing import Optional

from vkbottle_types.objects import secure
from .base_response import BaseResponse


class CheckTokenResponse(BaseResponse):
    response: Optional[typing.List["secure.TokenChecked"]] = None


class GetAppBalanceResponse(BaseResponse):
    response: Optional[int] = None


class GetSMSHistoryResponse(BaseResponse):
    response: Optional[typing.List["secure.SmsNotification"]] = None


class GetTransactionsHistoryResponse(BaseResponse):
    response: Optional[typing.List["secure.Transaction"]] = None


class GetUserLevelResponse(BaseResponse):
    response: Optional[typing.List["secure.Level"]] = None


class GiveEventStickerResponseModel(BaseResponse):
    user_id: Optional[int] = None
    status: Optional[str] = None


class GiveEventStickerResponse(BaseResponse):
    response: Optional[typing.List["GiveEventStickerResponseModel"]] = None


class SendNotificationResponse(BaseResponse):
    response: Optional[typing.List[int]] = None
