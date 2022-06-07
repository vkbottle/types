import typing

from vkbottle_types.objects import BaseBoolInt, PollsBackground, PollsPoll, PollsVoters
from vkbottle_types.responses.base_response import BaseResponse


class AddVoteResponse(BaseResponse):
    response: BaseBoolInt


class CreateResponse(BaseResponse):
    response: PollsPoll


class DeleteVoteResponse(BaseResponse):
    response: BaseBoolInt


class GetBackgroundsResponse(BaseResponse):
    response: typing.List["PollsBackground"]


class GetByIdResponse(BaseResponse):
    response: PollsPoll


class GetVotersResponse(BaseResponse):
    response: typing.List["PollsVoters"]


class SavePhotoResponse(BaseResponse):
    response: PollsBackground


__all__ = (
    "AddVoteResponse",
    "BaseBoolInt",
    "CreateResponse",
    "DeleteVoteResponse",
    "GetBackgroundsResponse",
    "GetByIdResponse",
    "GetVotersResponse",
    "PollsBackground",
    "PollsPoll",
    "PollsVoters",
    "SavePhotoResponse",
)
