# noqa: F401,F403
# type: ignore

import vkbottle_types.codegen.responses.groups
from vkbottle_types.codegen.responses.groups import *
from vkbottle_types.objects import GroupsMemberRole, GroupsUserXtrRole
from vkbottle_types.responses.base_response import BaseResponse


class GetMembersFilterManagersResponseModel(BaseResponse):
    count: int | None = None
    items: list[GroupsMemberRole] | None = None


class GetMembersFieldsFilterManagersResponseModel(BaseResponse):
    count: int | None = None
    items: list[GroupsUserXtrRole] | None = None


class GetMembersFilterManagersResponse(BaseResponse):
    response: GetMembersFilterManagersResponseModel


class GetMembersFieldsFilterManagersResponse(BaseResponse):
    response: GetMembersFieldsFilterManagersResponseModel


__all__ = (
    "GetMembersFieldsFilterManagersResponse",
    "GetMembersFieldsFilterManagersResponseModel",
    "GetMembersFilterManagersResponse",
    "GetMembersFilterManagersResponseModel",
)
__all__ += vkbottle_types.codegen.responses.groups.__all__  # type: ignore
