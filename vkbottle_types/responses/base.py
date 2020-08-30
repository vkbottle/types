from typing import Optional

from vkbottle_types.objects import BaseUploadServer, BaseBoolInt
from .base_response import BaseResponse


class BoolResponse(BaseResponse):
    response: Optional["BoolResponseModel"] = None


class GetUploadServerResponse(BaseResponse):
    response: Optional["GetUploadServerResponseModel"] = None


class OkResponse(BaseResponse):
    response: Optional["OkResponseModel"] = None


BoolResponseModel = Optional[BaseBoolInt]

GetUploadServerResponseModel = Optional[BaseUploadServer]

OkResponseModel = int

BoolResponse.update_forward_refs()
GetUploadServerResponse.update_forward_refs()
OkResponse.update_forward_refs()
