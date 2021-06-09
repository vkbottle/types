import inspect
import typing
from .base_response import BaseResponse
from vkbottle_types.objects import BaseBoolInt, PollsBackground, PollsPoll, PollsVoters


class AddVoteResponse(BaseResponse):
    response: BaseBoolInt = None


class CreateResponse(BaseResponse):
    response: PollsPoll = None


class DeleteVoteResponse(BaseResponse):
    response: BaseBoolInt = None


class GetBackgroundsResponse(BaseResponse):
    response: typing.List["PollsBackground"] = None


class GetByIdResponse(BaseResponse):
    response: PollsPoll = None


class GetVotersResponse(BaseResponse):
    response: typing.List["PollsVoters"] = None


class SavePhotoResponse(BaseResponse):
    response: PollsBackground = None


for item in locals().copy().values():
    if inspect.isclass(item) and issubclass(item, BaseResponse):
        item.update_forward_refs()
