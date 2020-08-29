import typing
from typing import Optional

from vkbottle_types.objects import polls, base
from .base_response import BaseResponse


class AddVoteResponse(BaseResponse):
    response: Optional[typing.List["base.BoolInt"]] = None


class CreateResponse(BaseResponse):
    response: Optional[typing.List["polls.Poll"]] = None


class DeleteVoteResponse(BaseResponse):
    response: Optional[typing.List["base.BoolInt"]] = None


class GetByIdResponse(BaseResponse):
    response: Optional[typing.List["polls.Poll"]] = None


class GetVotersResponse(BaseResponse):
    response: Optional[typing.List["polls.Voters"]] = None
