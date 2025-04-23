import typing

from vkbottle_types.codegen.responses.utils import *  # noqa: F403,F401  # type: ignore


class UtilsResolveScreenNameResponse(BaseResponse):
    response: typing.Union["UtilsDomainResolved", typing.List[typing.Any]] = Field(
        default_factory=lambda: [],
    )
