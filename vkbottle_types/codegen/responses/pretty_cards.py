import typing

from vkbottle_types.base_model import Field
from vkbottle_types.objects import PrettyCardsPrettyCardOrError
from vkbottle_types.responses.base_response import BaseResponse


class PrettyCardsCreateResponse(BaseResponse):
    response: typing.Dict[str, typing.Any] = Field()


class PrettyCardsDeleteResponse(BaseResponse):
    response: typing.Dict[str, typing.Any] = Field()


class PrettyCardsEditResponse(BaseResponse):
    response: typing.Dict[str, typing.Any] = Field()


class PrettyCardsGetByIdResponse(BaseResponse):
    response: typing.List[PrettyCardsPrettyCardOrError] = Field()


class PrettyCardsGetUploadURLResponse(BaseResponse):
    response: str = Field()


class PrettyCardsGetResponse(BaseResponse):
    response: typing.Dict[str, typing.Any] = Field()
