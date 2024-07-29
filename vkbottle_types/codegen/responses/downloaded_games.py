import typing

from vkbottle_types.base_model import Field
from vkbottle_types.responses.base_response import BaseResponse


class DownloadedGamesPaidStatusResponse(BaseResponse):
    response: typing.Dict[str, typing.Any] = Field()
