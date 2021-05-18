from typing import Optional

from vkbottle_types.objects import StatusStatus

from .base_response import BaseResponse


class GetResponse(BaseResponse):
    response: Optional["GetResponseModel"] = None


GetResponseModel = Optional[StatusStatus]

GetResponse.update_forward_refs()
