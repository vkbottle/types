import typing

from vkbottle_types.base_model import Field
from vkbottle_types.objects import FaveTag
from vkbottle_types.responses.base_response import BaseResponse


class FaveAddTagResponse(BaseResponse):
    response: "FaveTag" = Field()


class FaveGetPagesResponse(BaseResponse):
    response: typing.Dict[str, typing.Any] = Field()


class FaveGetTagsResponse(BaseResponse):
    response: typing.Dict[str, typing.Any] = Field()


class FaveGetExtendedResponse(BaseResponse):
    response: typing.Dict[str, typing.Any] = Field()


class FaveGetResponse(BaseResponse):
    response: typing.Dict[str, typing.Any] = Field()
