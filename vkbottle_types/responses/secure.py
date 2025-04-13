import inspect

from vkbottle_types.codegen.responses.secure import *  # noqa: F403,F401

from .base_response import BaseResponse


class SecureSetCounterIntegerResponse(BaseResponse):
    response: int
