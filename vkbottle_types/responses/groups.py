from typing import List, Optional

from vkbottle_types.codegen.responses.groups import *  # noqa: F403,F401
from vkbottle_types.objects import GroupsMemberRole, GroupsUserXtrRole
from vkbottle_types.responses.base_response import BaseResponse


class GetMembersFilterManagersResponse(BaseResponse):
    response: "GetMembersFilterManagersResponseModel"


class GetMembersFieldsFilterManagersResponse(BaseResponse):
    response: "GetMembersFieldsFilterManagersResponseModel"


class GetMembersFilterManagersResponseModel(BaseResponse):
    count: Optional[int] = None
    items: Optional[List["GroupsMemberRole"]] = None


class GetMembersFieldsFilterManagersResponseModel(BaseResponse):
    count: Optional[int] = None
    items: Optional[List["GroupsUserXtrRole"]] = None
