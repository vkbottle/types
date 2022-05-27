import inspect
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


for item in locals().copy().values():
    if inspect.isclass(item) and issubclass(item, BaseResponse):
        item.update_forward_refs()


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
