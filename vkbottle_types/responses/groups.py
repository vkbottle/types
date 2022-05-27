from typing import List, Optional
from vkbottle_types.objects import GroupsMemberRole, GroupsUserXtrRole
from vkbottle_types.responses.base_response import BaseResponse
from vkbottle_types.codegen.responses.groups import *  # noqa: F403,F401


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


GetMembersFilterManagersResponse.update_forward_refs()
GetMembersFieldsFilterManagersResponse.update_forward_refs()
GetMembersFilterManagersResponseModel.update_forward_refs()
GetMembersFieldsFilterManagersResponseModel.update_forward_refs()
