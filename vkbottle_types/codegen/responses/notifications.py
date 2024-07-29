import typing

from vkbottle_types.base_model import Field
from vkbottle_types.objects import NotificationsSendMessageItem
from vkbottle_types.responses.base_response import BaseResponse


class NotificationsGetResponse(BaseResponse):
    response: typing.Dict[str, typing.Any] = Field()


class NotificationsSendMessageResponse(BaseResponse):
    response: typing.List[NotificationsSendMessageItem] = Field()
