# type: ignore
# noqa: F401,F403

import typing

import vkbottle_types.codegen.responses.utils
from vkbottle_types.base_model import Field
from vkbottle_types.codegen.responses.utils import *
from vkbottle_types.objects import UtilsDomainResolved
from vkbottle_types.responses.base_response import BaseResponse


class UtilsResolveScreenNameResponse(BaseResponse):
    response: UtilsDomainResolved | list[typing.Any] = Field(
        default_factory=lambda: [],
    )


__all__ = ("UtilsResolveScreenNameResponse",)
__all__ += vkbottle_types.codegen.responses.utils.__all__
