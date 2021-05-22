import inspect
import typing
from .base_response import BaseResponse
from vkbottle_types.objects import BaseBoolInt, PollsBackground, PollsPoll, PollsVoters


class AddVoteResponse(BaseResponse):
    response: typing.Optional["AddVoteResponseModel"] = None


class CreateResponse(BaseResponse):
    response: typing.Optional["CreateResponseModel"] = None


class DeleteVoteResponse(BaseResponse):
    response: typing.Optional["DeleteVoteResponseModel"] = None


class GetBackgroundsResponse(BaseResponse):
    response: typing.Optional["GetBackgroundsResponseModel"] = None


class GetByIdResponse(BaseResponse):
    response: typing.Optional["GetByIdResponseModel"] = None


class GetVotersResponse(BaseResponse):
    response: typing.Optional["GetVotersResponseModel"] = None


class SavePhotoResponse(BaseResponse):
    response: typing.Optional["SavePhotoResponseModel"] = None


AddVoteResponseModel = BaseBoolInt


CreateResponseModel = PollsPoll


DeleteVoteResponseModel = BaseBoolInt


GetBackgroundsResponseModel = typing.List[PollsBackground]


GetByIdResponseModel = PollsPoll


GetVotersResponseModel = typing.List[PollsVoters]


SavePhotoResponseModel = PollsBackground


for item in locals().copy().values():
    if inspect.isclass(item) and issubclass(item, BaseResponse):
        item.update_forward_refs()
