from vkbottle_types.base_model import Field
from vkbottle_types.objects import StatusStatus
from vkbottle_types.responses.base_response import BaseResponse


class StatusGetResponse(BaseResponse):
    response: "StatusStatus" = Field()
