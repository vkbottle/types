from typing import TYPE_CHECKING, Any, List, Optional, Union, overload

from typing_extensions import Literal

from vkbottle_types.codegen.methods.groups import GroupsCategory as _GroupsCategory  # type: ignore
from vkbottle_types.objects import GroupsMemberStatus, GroupsMemberStatusFull
from vkbottle_types.responses.base import BaseBoolResponse
from vkbottle_types.responses.groups import (
    GetMembersFieldsFilterManagersResponse,
    GetMembersFieldsFilterManagersResponseModel,
    GetMembersFilterManagersResponse,
    GetMembersFilterManagersResponseModel,
    GroupsGetMembersFieldsResponse,
    GroupsGetMembersFieldsResponseModel,
    GroupsGetMembersFilterResponse,
    GroupsGetMembersFilterResponseModel,
    GroupsGetMembersResponse,
    GroupsGetMembersResponseModel,
    GroupsIsMemberExtendedResponse,
    GroupsIsMemberExtendedResponseModel,
    GroupsIsMemberUserIdsExtendedResponse,
    GroupsIsMemberUserIdsResponse,
)

if TYPE_CHECKING:
    from vkbottle import ABCAPI  # type: ignore


class GroupsCategory(_GroupsCategory):  # type: ignore
    def __init__(self, api: "ABCAPI") -> None:
        super().__init__(api)

    @overload  # type: ignore
    async def get_members(
        self,
        group_id: Optional[Union[str, int]],
        sort: Optional[Literal["id_asc", "id_desc", "time_asc", "time_desc"]] = None,
        offset: Optional[int] = None,
        count: Optional[int] = None,
        fields: Optional[Literal[None]] = ...,
        filter: Optional[Literal["friends", "unsure", "donut"]] = ...,
    ) -> GroupsGetMembersFilterResponseModel: ...

    @overload
    async def get_members(
        self,
        group_id: Optional[str] = None,
        sort: Optional[Literal["id_asc", "id_desc", "time_asc", "time_desc"]] = None,
        offset: Optional[int] = None,
        count: Optional[int] = None,
        fields: List[str] = ...,
        filter: Optional[Literal[None]] = ...,
    ) -> GroupsGetMembersFieldsResponseModel: ...

    @overload
    async def get_members(
        self,
        group_id: Optional[str] = None,
        sort: Optional[Literal["id_asc", "id_desc", "time_asc", "time_desc"]] = None,
        offset: Optional[int] = None,
        count: Optional[int] = None,
        fields: Optional[Literal[None]] = ...,
        filter: Literal["managers"] = ...,
    ) -> GetMembersFilterManagersResponseModel: ...

    @overload
    async def get_members(
        self,
        group_id: Optional[str] = None,
        sort: Optional[Literal["id_asc", "id_desc", "time_asc", "time_desc"]] = None,
        offset: Optional[int] = None,
        count: Optional[int] = None,
        fields: List[str] = ...,
        filter: Literal["managers"] = ...,
    ) -> GetMembersFieldsFilterManagersResponseModel: ...

    async def get_members(
        self,
        group_id=None,
        sort=None,
        offset=None,
        count=None,
        fields=None,
        filter=None,
        **kwargs,
    ) -> Union[
        GetMembersFilterManagersResponseModel,
        GetMembersFieldsFilterManagersResponseModel,
        GroupsGetMembersResponseModel,
        GroupsGetMembersFilterResponseModel,
        GroupsGetMembersFieldsResponseModel,
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
                ((("filter", "managers"),), GetMembersFilterManagersResponse),
                (
                    (("filter", "managers"), "fields"),
                    GetMembersFieldsFilterManagersResponse,
                ),
                (("fields",), GroupsGetMembersFieldsResponse),
                (("filter",), GroupsGetMembersFilterResponse),
            ),
            default=GroupsGetMembersResponse,
            params=params,
        )
        return model(**response).response

    @overload  # type: ignore
    async def is_member(
        self,
        *,
        group_id: Union[int, str],
        user_ids: List[int],
        extended: Literal[True],
    ) -> List[GroupsMemberStatusFull]: ...

    @overload
    async def is_member(
        self,
        *,
        group_id: Union[int, str],
        user_id: int,
        extended: Literal[True],
    ) -> GroupsIsMemberExtendedResponseModel: ...

    @overload
    async def is_member(
        self,
        *,
        group_id: Union[int, str],
        user_ids: List[int],
    ) -> List[GroupsMemberStatus]: ...

    @overload
    async def is_member(
        self,
        *,
        group_id: Union["int", "str"],
        user_id: int,
    ) -> bool: ...

    async def is_member(
        self,
        *,
        group_id: Union[int, str],
        extended: Optional[bool] = None,
        user_ids: Optional[List[int]] = None,
        user_id: Optional[int] = None,
        **kwargs: Any,
    ) -> Union[
        List[GroupsMemberStatus],
        bool,
        GroupsIsMemberExtendedResponseModel,
        List[GroupsMemberStatusFull],
    ]:
        """Method `groups.isMember()`

        :param group_id: ID or screen name of the community.
        :param extended: '1' - to return an extended response with additional fields. By default: '0'.
        :param user_ids: User IDs.
        :param user_id: User ID.
        """

        params = self.get_set_params(locals())
        response = await self.api.request("groups.isMember", params)
        model = self.get_model(
            (
                (("user_id", "extended"), GroupsIsMemberExtendedResponse),
                (("user_ids", "extended"), GroupsIsMemberUserIdsExtendedResponse),
                (("user_ids",), GroupsIsMemberUserIdsResponse),
            ),
            default=BaseBoolResponse,
            params=params,
        )
        return model(**response).response


__all__ = ("GroupsCategory",)
