from vkbottle_types.objects import StatusStatus
from vkbottle_types.responses.base_response import BaseResponse


class GetResponse(BaseResponse):
    response: StatusStatus


__all__ = (
    "GetResponse",
    "StatusStatus",
)
