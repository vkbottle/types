import typing

from vkbottle_types.base_model import Field
from vkbottle_types.objects import PollsBackground, PollsFieldsVoters, PollsPoll, PollsPollExtended, PollsVoters
from vkbottle_types.responses.base_response import BaseResponse


class PollsCreateResponse(BaseResponse):
    response: "PollsPoll" = Field()


class PollsGetBackgroundsResponse(BaseResponse):
    response: typing.List["PollsBackground"] = Field()


class PollsGetByIdResponse(BaseResponse):
    response: "PollsPollExtended" = Field()


class PollsGetVotersFieldsResponse(BaseResponse):
    response: typing.List["PollsFieldsVoters"] = Field()


class PollsGetVotersResponse(BaseResponse):
    response: typing.List["PollsVoters"] = Field()


class PollsSavePhotoResponse(BaseResponse):
    response: "PollsBackground" = Field()
