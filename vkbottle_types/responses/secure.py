# noqa: F401,F403
# type: ignore

import vkbottle_types.codegen.responses.secure
from vkbottle_types.codegen.responses.secure import *
from vkbottle_types.responses.base_response import BaseResponse


class SecureSetCounterIntegerResponse(BaseResponse):
    response: int


__all__ = ("SecureSetCounterIntegerResponse",)
__all__ += vkbottle_types.codegen.responses.secure.__all__
