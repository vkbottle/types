import inspect
import typing
from .base_response import BaseResponse
from vkbottle_types.objects import SecureLevel, SecureSmsNotification, SecureTokenChecked, SecureTransaction


class CheckTokenResponse(BaseResponse):
    response: SecureTokenChecked = None


class GetAppBalanceResponse(BaseResponse):
    response: int = None


class GetSMSHistoryResponse(BaseResponse):
    response: typing.List["SecureSmsNotification"] = None


class GetTransactionsHistoryResponse(BaseResponse):
    response: typing.List["SecureTransaction"] = None


class GetUserLevelResponse(BaseResponse):
    response: typing.List["SecureLevel"] = None


class GiveEventStickerResponse(BaseResponse):
    response: typing.List["GiveEventStickerResponseModel"] = None


class SendNotificationResponse(BaseResponse):
    response: typing.List[int] = None


class GiveEventStickerResponseModel(BaseResponse):
    user_id: typing.Optional[int] = None
    status: typing.Optional[str] = None


for item in locals().copy().values():
    if inspect.isclass(item) and issubclass(item, BaseResponse):
        item.update_forward_refs()
