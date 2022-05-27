from vkbottle_types.responses.groups import (
    GetMembersResponse,
    GetMembersResponseModel,
    GetMembersFieldsResponse,
    GetMembersFieldsResponseModel,
    GetMembersFilterManagersResponse,
    GetMembersFilterManagersResponseModel,
    GetMembersFieldsFilterManagersResponse,
    GetMembersFieldsFilterManagersResponseModel,
)

from vkbottle_types.codegen.methods.groups import GroupsCategory
from typing_extensions import Literal
from typing import Optional, List, overload, Union


class GroupsCategory(GroupsCategory):
    @overload
    async def get_members(
        self,
        group_id: Optional[str] = None,
        sort: Optional[Literal["id_asc", "id_desc", "time_asc", "time_desc"]] = None,
        offset: Optional[int] = None,
        count: Optional[int] = None,
        fields: Optional[Literal[None]] = ...,
        filter: Optional[Literal["friends", "unsure", "donut"]] = ...,
        **kwargs
    ) -> GetMembersResponseModel:
        ...

    @overload
    async def get_members(
        self,
        group_id: Optional[str] = None,
        sort: Optional[Literal["id_asc", "id_desc", "time_asc", "time_desc"]] = None,
        offset: Optional[int] = None,
        count: Optional[int] = None,
        fields: List[str] = ...,
        filter: Optional[Literal[None]] = ...,
        **kwargs
    ) -> GetMembersFieldsResponseModel:
        ...

    @overload
    async def get_members(
        self,
        group_id: Optional[str] = None,
        sort: Optional[Literal["id_asc", "id_desc", "time_asc", "time_desc"]] = None,
        offset: Optional[int] = None,
        count: Optional[int] = None,
        fields: Optional[Literal[None]] = ...,
        filter: Literal["managers"] = ...,
        **kwargs
    ) -> GetMembersFilterManagersResponseModel:
        ...

    @overload
    async def get_members(
        self,
        group_id: Optional[str] = None,
        sort: Optional[Literal["id_asc", "id_desc", "time_asc", "time_desc"]] = None,
        offset: Optional[int] = None,
        count: Optional[int] = None,
        fields: List[str] = ...,
        filter: Literal["managers"] = ...,
        **kwargs
    ) -> GetMembersFieldsFilterManagersResponseModel:
        ...

    async def get_members(
        self,
        group_id=None,
        sort=None,
        offset=None,
        count=None,
        fields=None,
        filter=None,
        **kwargs
    ) -> Union[
        GetMembersResponseModel,
        GetMembersFieldsResponseModel,
        GetMembersFilterManagersResponseModel,
        GetMembersFieldsFilterManagersResponseModel,
    ]:
        """Returns a list of community members.

        :param group_id: ID or screen name of the community.
        :param sort: Sort order. Available values: 'id_asc', 'id_desc', 'time_asc', 'time_desc'. 'time_asc' and 'time_desc' are availavle only if the method is called by the group's 'moderator'.
        :param offset: Offset needed to return a specific subset of community members.
        :param count: Number of community members to return.
        :param fields: List of additional fields to be returned. Available values: 'sex, bdate, city, country, photo_50, photo_100, photo_200_orig, photo_200, photo_400_orig, photo_max, photo_max_orig, online, online_mobile, lists, domain, has_mobile, contacts, connections, site, education, universities, schools, can_post, can_see_all_posts, can_see_audio, can_write_private_message, status, last_seen, common_count, relation, relatives, counters'.
        :param filter: *'friends' - only friends in this community will be returned,, *'unsure' - only those who pressed 'I may attend' will be returned (if it's an event).
        """

        params = self.get_set_params(locals())
        response = await self.api.request("groups.getMembers", params)
        model = self.get_model(
            (
                (("fields",), GetMembersFieldsResponse),
                ((["filter", "managers"],), GetMembersFilterManagersResponse),
                (
                    (["filter", "managers"], "fields"),
                    GetMembersFieldsFilterManagersResponse,
                ),
            ),
            default=GetMembersResponse,
            params=params,
        )
        return model(**response).response
