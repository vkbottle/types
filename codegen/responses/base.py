import enum
import typing

from vkbottle_types.base_model import Field
from vkbottle_types.objects import BaseUploadServer
from vkbottle_types.responses.base_response import BaseResponse


class BaseBoolResponse(BaseResponse):
    response: bool = Field()


class BaseGetUploadServerResponse(BaseResponse):
    response: "BaseUploadServer" = Field()


class BaseOkResponseModel(enum.IntEnum):
    OK = 1


class BaseOkResponse(BaseResponse):
    response: "BaseOkResponseModel" = Field(default=BaseOkResponseModel.OK)


class BaseUndefinedResponse(BaseResponse):
    response: typing.Dict[str, typing.Any] = Field()
