import inspect
import typing
from .base_response import BaseResponse
from vkbottle_types.objects import SecureLevel, SecureSmsNotification, SecureTokenChecked, SecureTransaction


class CheckTokenResponse(BaseResponse):
    response: typing.Optional["CheckTokenResponseModel"] = None


class GetAppBalanceResponse(BaseResponse):
    response: typing.Optional["GetAppBalanceResponseModel"] = None


class GetSMSHistoryResponse(BaseResponse):
    response: typing.Optional["GetSMSHistoryResponseModel"] = None


class GetTransactionsHistoryResponse(BaseResponse):
    response: typing.Optional["GetTransactionsHistoryResponseModel"] = None


class GetUserLevelResponse(BaseResponse):
    response: typing.Optional["GetUserLevelResponseModel"] = None


class GiveEventStickerResponse(BaseResponse):
    response: typing.Optional["GiveEventStickerResponseModel"] = None


class SendNotificationResponse(BaseResponse):
    response: typing.Optional["SendNotificationResponseModel"] = None


CheckTokenResponseModel = SecureTokenChecked


GetAppBalanceResponseModel = int


GetSMSHistoryResponseModel = typing.List[SecureSmsNotification]


GetTransactionsHistoryResponseModel = typing.List[SecureTransaction]


GetUserLevelResponseModel = typing.List[SecureLevel]


GiveEventStickerResponseModel = typing.List["typing.Any"]


SendNotificationResponseModel = typing.List[int]


for item in locals().copy().values():
    if inspect.isclass(item) and issubclass(item, BaseResponse):
        item.update_forward_refs()
