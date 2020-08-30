from .base_response import BaseResponse
from vkbottle_types.objects import polls, base
from typing import Optional, Any, List, Union
import typing


class AddVoteResponse(BaseResponse):
    response: Optional["AddVoteResponseModel"] = None


class CreateResponse(BaseResponse):
    response: Optional["CreateResponseModel"] = None


class DeleteVoteResponse(BaseResponse):
    response: Optional["DeleteVoteResponseModel"] = None


class GetByIdResponse(BaseResponse):
    response: Optional["GetByIdResponseModel"] = None


class GetVotersResponse(BaseResponse):
    response: Optional["GetVotersResponseModel"] = None


AddVoteResponseModel = Optional["base.BoolInt"]


CreateResponseModel = Optional["polls.Poll"]


DeleteVoteResponseModel = Optional["base.BoolInt"]


GetByIdResponseModel = Optional["polls.Poll"]


GetVotersResponseModel = List["polls.Voters"]
