import typing

from vkbottle_types.codegen.responses.utils import *  # noqa: F403,F401  # type: ignore


class UtilsResolveScreenNameResponse(BaseResponse):  # type: ignore
    response: "UtilsDomainResolved | list[typing.Any]" = Field(  # type: ignore
        default_factory=lambda: [],
    )
