import typing

from vkbottle_types.base_model import Field
from vkbottle_types.objects import AsrTask
from vkbottle_types.responses.base_response import BaseResponse


class AsrCheckStatusResponse(BaseResponse):
    response: "AsrTask" = Field()


class AsrProcessResponse(BaseResponse):
    response: typing.Dict[str, typing.Any] = Field()
