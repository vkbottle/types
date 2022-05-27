from vkbottle_types.responses.base_response import BaseResponse
from vkbottle_types.codegen.responses.secure import *  # noqa: F403,F401


class SetCounterIntegerResponse(BaseResponse):
    response: int


SetCounterIntegerResponse.update_forward_refs()
