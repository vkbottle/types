from typing import List, Optional

from vkbottle_types.objects import BaseBoolInt, PollsPoll, PollsVoters

from .base_response import BaseResponse


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


AddVoteResponseModel = Optional[BaseBoolInt]

CreateResponseModel = Optional[PollsPoll]

DeleteVoteResponseModel = Optional[BaseBoolInt]

GetByIdResponseModel = Optional[PollsPoll]

GetVotersResponseModel = List[PollsVoters]

AddVoteResponse.update_forward_refs()
CreateResponse.update_forward_refs()
DeleteVoteResponse.update_forward_refs()
GetByIdResponse.update_forward_refs()
GetVotersResponse.update_forward_refs()
