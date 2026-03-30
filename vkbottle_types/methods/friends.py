import typing

from vkbottle_types.codegen.methods.friends import FriendsCategory as _FriendsCategory  # type: ignore
from vkbottle_types.objects import (
    FriendsMutualFriend,
    FriendsOnlineUsers,
    FriendsOnlineUsersWithMobile,
    UsersFields,
)
from vkbottle_types.responses.friends import (
    FriendsGetMutualResponse,
    FriendsGetMutualTargetUidsResponse,
    FriendsGetMutualTotalCountResponse,
    FriendsGetOnlineExtendedResponse,
    FriendsGetOnlineOnlineMobileExtendedResponse,
    FriendsGetOnlineOnlineMobileResponse,
    FriendsGetOnlineOnlineMobileResponseModel,
    FriendsGetOnlineResponse,
    FriendsGetRequestsExtendedResponse,
    FriendsGetRequestsExtendedResponseModel,
    FriendsGetRequestsNeedMutualResponse,
    FriendsGetRequestsNeedMutualResponseModel,
    FriendsGetRequestsResponse,
    FriendsGetRequestsResponseModel,
    FriendsMutualFriend,
    FriendsOnlineUsers,
    FriendsOnlineUsersWithMobile,
)

if typing.TYPE_CHECKING:
    from vkbottle import ABCAPI  # type: ignore


class FriendsCategory(_FriendsCategory):  # type: ignore
    def __init__(self, api: "ABCAPI") -> None:
        super().__init__(api)

    @typing.overload
    async def get_mutual(
        self,
        *,
        total_count: int,
        count: int | None = None,
        need_common_count: bool | None = None,
        offset: int | None = None,
        order: str | None = None,
        source_uid: int | None = None,
        target_uid: int | None = None,
    ) -> "FriendsMutualFriend": ...

    @typing.overload
    async def get_mutual(
        self,
        *,
        target_uids: list[int],
        count: int | None = None,
        need_common_count: bool | None = None,
        offset: int | None = None,
        order: str | None = None,
        source_uid: int | None = None,
        target_uid: int | None = None,
    ) -> list[FriendsMutualFriend]: ...

    @typing.overload
    async def get_mutual(
        self,
        *,
        count: int | None = None,
        need_common_count: bool | None = None,
        offset: int | None = None,
        order: str | None = None,
        source_uid: int | None = None,
        target_uid: int | None = None,
    ) -> list[int]: ...

    async def get_mutual(
        self,
        *,
        target_uids: list[int] | None = None,
        total_count: int | None = None,
        count: int | None = None,
        need_common_count: bool | None = None,
        offset: int | None = None,
        order: str | None = None,
        source_uid: int | None = None,
        target_uid: int | None = None,
        **kwargs: typing.Any,
    ) -> FriendsMutualFriend | list[int] | list[FriendsMutualFriend]:
        """Method `friends.getMutual()`

        :param target_uids: IDs of the users whose friends will be checked against the friends of the user specified in 'source_uid'.
        :param count: Number of mutual friends to return.
        :param need_common_count: Return mutual friends total count
        :param offset: Offset needed to return a specific subset of mutual friends.
        :param order: Sort order: 'random' - random order
        :param source_uid: ID of the user whose friends will be checked against the friends of the user specified in 'target_uid'.
        :param target_uid: ID of the user whose friends will be checked against the friends of the user specified in 'source_uid'.
        """

        params = self.get_set_params(locals())
        response = await self.api.request("friends.getMutual", params)
        model = self.get_model(
            (
                (("target_uids",), FriendsGetMutualTargetUidsResponse),
                (("total_count",), FriendsGetMutualTotalCountResponse),
            ),
            default=FriendsGetMutualResponse,
            params=params,
        )
        return model(**response).response

    @typing.overload
    async def get_online(
        self,
        *,
        online_mobile: typing.Literal[True],
        count: int | None = None,
        list_id: int | None = None,
        offset: int | None = None,
        order: str | None = None,
        user_id: int | None = None,
    ) -> FriendsGetOnlineOnlineMobileResponseModel: ...

    @typing.overload
    async def get_online(
        self,
        *,
        extended: typing.Literal[True],
        count: int | None = None,
        list_id: int | None = None,
        offset: int | None = None,
        order: str | None = None,
        user_id: int | None = None,
    ) -> "FriendsOnlineUsers": ...

    @typing.overload
    async def get_online(
        self,
        *,
        online_mobile_extended: typing.Literal[True],
        count: int | None = None,
        list_id: int | None = None,
        offset: int | None = None,
        online_mobile: bool | None = None,
        order: str | None = None,
        user_id: int | None = None,
    ) -> "FriendsOnlineUsersWithMobile": ...

    @typing.overload
    async def get_online(
        self,
        *,
        count: int | None = None,
        list_id: int | None = None,
        offset: int | None = None,
        order: str | None = None,
        user_id: int | None = None,
    ) -> list[int]: ...

    async def get_online(
        self,
        *,
        online_mobile: bool | None = None,
        extended: bool | None = None,
        online_mobile_extended: bool | None = None,
        count: int | None = None,
        list_id: int | None = None,
        offset: int | None = None,
        order: str | None = None,
        user_id: int | None = None,
        **kwargs: typing.Any,
    ) -> FriendsOnlineUsersWithMobile | list[int] | FriendsGetOnlineOnlineMobileResponseModel | FriendsOnlineUsers:
        """Method `friends.getOnline()`

        :param online_mobile: '1' - to return an additional 'online_mobile' field, '0' - (default),
        :param count: Number of friends to return.
        :param list_id: Friend list ID. If this parameter is not set, information about all online friends is returned.
        :param offset: Offset needed to return a specific subset of friends.
        :param order: Sort order: 'random' - random order
        :param user_id: User ID.
        """

        params = self.get_set_params(locals())
        response = await self.api.request("friends.getOnline", params)
        model = self.get_model(
            (
                (("online_mobile",), FriendsGetOnlineOnlineMobileResponse),
                (("extended",), FriendsGetOnlineExtendedResponse),
                (("online_mobile_extended",), FriendsGetOnlineOnlineMobileExtendedResponse),
            ),
            default=FriendsGetOnlineResponse,
            params=params,
        )
        return model(**response).response

    @typing.overload
    async def get_requests(
        self,
        *,
        need_mutual: typing.Literal[True],
        count: int | None = None,
        fields: list[UsersFields] | None = None,
        need_viewed: bool | None = None,
        offset: int | None = None,
        out: bool | None = None,
        ref: str | None = None,
        sort: int | None = None,
        suggested: bool | None = None,
    ) -> FriendsGetRequestsNeedMutualResponseModel: ...

    @typing.overload
    async def get_requests(
        self,
        *,
        extended: typing.Literal[True],
        count: int | None = None,
        fields: list[UsersFields] | None = None,
        need_viewed: bool | None = None,
        offset: int | None = None,
        out: bool | None = None,
        ref: str | None = None,
        sort: int | None = None,
        suggested: bool | None = None,
    ) -> FriendsGetRequestsExtendedResponseModel: ...

    @typing.overload
    async def get_requests(
        self,
        *,
        count: int | None = None,
        fields: list[UsersFields] | None = None,
        need_viewed: bool | None = None,
        offset: int | None = None,
        out: bool | None = None,
        ref: str | None = None,
        sort: int | None = None,
        suggested: bool | None = None,
    ) -> FriendsGetRequestsResponseModel: ...

    async def get_requests(
        self,
        *,
        need_mutual: bool | None = None,
        extended: bool | None = None,
        count: int | None = None,
        fields: list[UsersFields] | None = None,
        need_viewed: bool | None = None,
        offset: int | None = None,
        out: bool | None = None,
        ref: str | None = None,
        sort: int | None = None,
        suggested: bool | None = None,
        **kwargs: typing.Any,
    ) -> FriendsGetRequestsNeedMutualResponseModel | FriendsGetRequestsResponseModel | FriendsGetRequestsExtendedResponseModel:
        """Method `friends.getRequests()`

        :param need_mutual: '1' - to return a list of mutual friends (up to 20), if any
        :param extended: '1' - to return response messages from users who have sent a friend request or, if 'suggested' is set to '1', to return a list of suggested friends
        :param count: Number of friend requests to return (default 100, maximum 1000).
        :param fields:
        :param need_viewed:
        :param offset: Offset needed to return a specific subset of friend requests.
        :param out: '1' - to return outgoing requests, '0' - to return incoming requests (default)
        :param ref:
        :param sort: Sort order: '1' - by number of mutual friends, '0' - by date
        :param suggested: '1' - to return a list of suggested friends, '0' - to return friend requests (default)
        """

        params = self.get_set_params(locals())
        response = await self.api.request("friends.getRequests", params)
        model = self.get_model(
            (
                (("need_mutual",), FriendsGetRequestsNeedMutualResponse),
                (("extended",), FriendsGetRequestsExtendedResponse),
            ),
            default=FriendsGetRequestsResponse,
            params=params,
        )
        return model(**response).response
