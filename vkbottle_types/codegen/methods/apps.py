import typing

from vkbottle_types.methods.base_category import BaseCategory
from vkbottle_types.objects import AppsAppFields, AppsTestingGroup, UsersFields
from vkbottle_types.responses.apps import *  # noqa: F401,F403  # type: ignore
from vkbottle_types.responses.base import (
    BaseBoolResponse,
    BaseOkResponse,
    BaseOkResponseModel,
)


class AppsCategory(BaseCategory):
    async def add_snippet(
        self,
        button: typing.Optional[str] = None,
        description: typing.Optional[str] = None,
        group_id: typing.Optional[typing.List[int]] = None,
        hash: typing.Optional[typing.List[str]] = None,
        image_url: typing.Optional[str] = None,
        small_image_url: typing.Optional[str] = None,
        snippet_id: typing.Optional[int] = None,
        title: typing.Optional[str] = None,
        vk_ref: typing.Optional[typing.List[typing.Literal["snippet_im", "snippet_post"]]] = None,
        **kwargs: typing.Any,
    ) -> AppsAddSnippetResponseModel:
        """Method `apps.addSnippet()`

        :param button:
        :param description:
        :param group_id:
        :param hash:
        :param image_url:
        :param small_image_url:
        :param snippet_id:
        :param title:
        :param vk_ref:
        """

        params = self.get_set_params(locals())
        response = await self.api.request("apps.addSnippet", params)
        model = AppsAddSnippetResponse
        return model(**response).response

    async def add_users_to_testing_group(
        self,
        group_id: int,
        user_ids: typing.List[int],
        **kwargs: typing.Any,
    ) -> bool:
        """Method `apps.addUsersToTestingGroup()`

        :param group_id:
        :param user_ids:
        """

        params = self.get_set_params(locals())
        response = await self.api.request("apps.addUsersToTestingGroup", params)
        model = BaseBoolResponse
        return model(**response).response

    async def delete_app_requests(
        self,
        **kwargs: typing.Any,
    ) -> BaseOkResponseModel:
        """Method `apps.deleteAppRequests()`"""

        params = self.get_set_params(locals())
        response = await self.api.request("apps.deleteAppRequests", params)
        model = BaseOkResponse
        return model(**response).response

    async def delete_snippet(
        self,
        id: typing.Optional[int] = None,
        **kwargs: typing.Any,
    ) -> BaseOkResponseModel:
        """Method `apps.deleteSnippet()`

        :param id:
        """

        params = self.get_set_params(locals())
        response = await self.api.request("apps.deleteSnippet", params)
        model = BaseOkResponse
        return model(**response).response

    async def get(
        self,
        app_fields: typing.Optional[typing.List[AppsAppFields]] = None,
        app_id: typing.Optional[int] = None,
        app_ids: typing.Optional[typing.List[int]] = None,
        extended: typing.Optional[bool] = None,
        fields: typing.Optional[typing.List[UsersFields]] = None,
        name_case: typing.Optional[str] = None,
        platform: typing.Optional[str] = None,
        return_friends: typing.Optional[bool] = None,
        **kwargs: typing.Any,
    ) -> AppsGetResponseModel:
        """Method `apps.get()`

        :param app_fields: List of app fields to return. Fields 'id', 'type' and 'title' will always be in response. Leave this field empty to get all fields
        :param app_id: Application ID
        :param app_ids: List of application ID
        :param extended:
        :param fields: Profile fields to return. Sample values: 'nickname', 'screen_name', 'sex', 'bdate' (birthdate), 'city', 'country', 'timezone', 'photo', 'photo_medium', 'photo_big', 'has_mobile', 'contacts', 'education', 'online', 'counters', 'relation', 'last_seen', 'activity', 'can_write_private_message', 'can_see_all_posts', 'can_post', 'universities', (only if return_friends - 1)
        :param name_case: Case for declension of user name and surname: 'nom' - nominative (default),, 'gen' - genitive,, 'dat' - dative,, 'acc' - accusative,, 'ins' - instrumental,, 'abl' - prepositional. (only if 'return_friends' = '1')
        :param platform: platform. Possible values: *'ios' - iOS,, *'android' - Android,, *'winphone' - Windows Phone,, *'web' - приложения на vk.ru. By default: 'web'.
        :param return_friends:
        """

        params = self.get_set_params(locals())
        response = await self.api.request("apps.get", params)
        model = AppsGetResponse
        return model(**response).response

    async def get_catalog(
        self,
        count: typing.Optional[int] = None,
        extended: typing.Optional[bool] = None,
        fields: typing.Optional[typing.List[UsersFields]] = None,
        filter: typing.Optional[str] = None,
        genre_id: typing.Optional[int] = None,
        name_case: typing.Optional[str] = None,
        offset: typing.Optional[int] = None,
        platform: typing.Optional[str] = None,
        q: typing.Optional[str] = None,
        return_friends: typing.Optional[bool] = None,
        sort: typing.Optional[str] = None,
        **kwargs: typing.Any,
    ) -> "AppsCatalogList":
        """Method `apps.getCatalog()`

        :param count: Number of apps to return.
        :param extended: '1' - to return additional fields 'screenshots', 'MAU', 'catalog_position', and 'international'. If set, 'count' must be less than or equal to '100'. '0' - not to return additional fields (default).
        :param fields:
        :param filter: 'installed' - to return list of installed apps (only for mobile platform).
        :param genre_id:
        :param name_case:
        :param offset: Offset required to return a specific subset of apps.
        :param platform:
        :param q: Search query string.
        :param return_friends:
        :param sort: Sort order: 'popular_today' - popular for one day (default), 'visitors' - by visitors number , 'create_date' - by creation date, 'growth_rate' - by growth rate, 'popular_week' - popular for one week
        """

        params = self.get_set_params(locals())
        response = await self.api.request("apps.getCatalog", params)
        model = AppsGetCatalogResponse
        return model(**response).response

    @typing.overload
    async def get_friends_list(
        self,
        extended: typing.Literal[True],
        count: typing.Optional[int] = None,
        fields: typing.Optional[typing.List[UsersFields]] = None,
        offset: typing.Optional[int] = None,
        query: typing.Optional[str] = None,
        type: typing.Optional[str] = None,
        **kwargs: typing.Any,
    ) -> AppsGetFriendsListExtendedResponseModel: ...

    @typing.overload
    async def get_friends_list(
        self,
        extended: typing.Optional[typing.Literal[False]] = None,
        count: typing.Optional[int] = None,
        fields: typing.Optional[typing.List[UsersFields]] = None,
        offset: typing.Optional[int] = None,
        query: typing.Optional[str] = None,
        type: typing.Optional[str] = None,
        **kwargs: typing.Any,
    ) -> AppsGetFriendsListResponseModel: ...

    async def get_friends_list(
        self,
        extended: typing.Optional[bool] = None,
        count: typing.Optional[int] = None,
        fields: typing.Optional[typing.List[UsersFields]] = None,
        offset: typing.Optional[int] = None,
        query: typing.Optional[str] = None,
        type: typing.Optional[str] = None,
        **kwargs: typing.Any,
    ) -> typing.Union[AppsGetFriendsListResponseModel, AppsGetFriendsListExtendedResponseModel]:
        """Method `apps.getFriendsList()`

        :param extended:
        :param count: List size.
        :param fields: Additional profile fields, see [vk.ru/dev/fields|description].
        :param offset:
        :param query: Search query string (e.g., 'Vasya Babich').
        :param type: List type. Possible values: * 'invite' - available for invites (don't play the game),, * 'request' - available for request (play the game). By default: 'invite'.
        """

        params = self.get_set_params(locals())
        response = await self.api.request("apps.getFriendsList", params)
        model = self.get_model(
            ((("extended",), AppsGetFriendsListExtendedResponse),),
            default=AppsGetFriendsListResponse,
            params=params,
        )
        return model(**response).response

    @typing.overload
    async def get_leaderboard(
        self,
        type: str,
        extended: typing.Literal[True],
        global_: typing.Optional[bool] = None,
        **kwargs: typing.Any,
    ) -> AppsGetLeaderboardExtendedResponseModel: ...

    @typing.overload
    async def get_leaderboard(
        self,
        type: str,
        extended: typing.Optional[typing.Literal[False]] = None,
        global_: typing.Optional[bool] = None,
        **kwargs: typing.Any,
    ) -> AppsGetLeaderboardResponseModel: ...

    async def get_leaderboard(
        self,
        type: str,
        extended: typing.Optional[bool] = None,
        global_: typing.Optional[bool] = None,
        **kwargs: typing.Any,
    ) -> typing.Union[AppsGetLeaderboardExtendedResponseModel, AppsGetLeaderboardResponseModel]:
        """Method `apps.getLeaderboard()`

        :param type: Leaderboard type. Possible values: *'level' - by level,, *'points' - by mission points,, *'score' - by score ().
        :param extended: 1 - to return additional info about users
        :param global: Rating type. Possible values: *'1' - global rating among all players,, *'0' - rating among user friends.
        """

        params = self.get_set_params(locals())
        response = await self.api.request("apps.getLeaderboard", params)
        model = self.get_model(
            ((("extended",), AppsGetLeaderboardExtendedResponse),),
            default=AppsGetLeaderboardResponse,
            params=params,
        )
        return model(**response).response

    async def get_mini_app_policies(
        self,
        app_id: int,
        **kwargs: typing.Any,
    ) -> AppsGetMiniAppPoliciesResponseModel:
        """Method `apps.getMiniAppPolicies()`

        :param app_id: Mini App ID
        """

        params = self.get_set_params(locals())
        response = await self.api.request("apps.getMiniAppPolicies", params)
        model = AppsGetMiniAppPoliciesResponse
        return model(**response).response

    async def get_scopes(
        self,
        type: typing.Optional[str] = None,
        **kwargs: typing.Any,
    ) -> AppsGetScopesResponseModel:
        """Method `apps.getScopes()`

        :param type:
        """

        params = self.get_set_params(locals())
        response = await self.api.request("apps.getScopes", params)
        model = AppsGetScopesResponse
        return model(**response).response

    async def get_score(
        self,
        user_id: typing.Optional[int] = None,
        **kwargs: typing.Any,
    ) -> int:
        """Method `apps.getScore()`

        :param user_id:
        """

        params = self.get_set_params(locals())
        response = await self.api.request("apps.getScore", params)
        model = AppsGetScoreResponse
        return model(**response).response

    async def get_snippets(
        self,
        **kwargs: typing.Any,
    ) -> AppsGetSnippetsResponseModel:
        """Method `apps.getSnippets()`"""

        params = self.get_set_params(locals())
        response = await self.api.request("apps.getSnippets", params)
        model = AppsGetSnippetsResponse
        return model(**response).response

    async def get_testing_groups(
        self,
        group_id: typing.Optional[int] = None,
        **kwargs: typing.Any,
    ) -> typing.List[AppsTestingGroup]:
        """Method `apps.getTestingGroups()`

        :param group_id:
        """

        params = self.get_set_params(locals())
        response = await self.api.request("apps.getTestingGroups", params)
        model = AppsGetTestingGroupsResponse
        return model(**response).response

    async def is_notifications_allowed(
        self,
        user_id: typing.Optional[int] = None,
        **kwargs: typing.Any,
    ) -> AppsIsNotificationsAllowedResponseModel:
        """Method `apps.isNotificationsAllowed()`

        :param user_id:
        """

        params = self.get_set_params(locals())
        response = await self.api.request("apps.isNotificationsAllowed", params)
        model = AppsIsNotificationsAllowedResponse
        return model(**response).response

    async def promo_has_active_gift(
        self,
        promo_id: int,
        user_id: typing.Optional[int] = None,
        **kwargs: typing.Any,
    ) -> bool:
        """Method `apps.promoHasActiveGift()`

        :param promo_id: Id of game promo action
        :param user_id:
        """

        params = self.get_set_params(locals())
        response = await self.api.request("apps.promoHasActiveGift", params)
        model = BaseBoolResponse
        return model(**response).response

    async def promo_use_gift(
        self,
        promo_id: int,
        user_id: typing.Optional[int] = None,
        **kwargs: typing.Any,
    ) -> bool:
        """Method `apps.promoUseGift()`

        :param promo_id: Id of game promo action
        :param user_id:
        """

        params = self.get_set_params(locals())
        response = await self.api.request("apps.promoUseGift", params)
        model = BaseBoolResponse
        return model(**response).response

    async def remove_testing_group(
        self,
        group_id: int,
        **kwargs: typing.Any,
    ) -> bool:
        """Method `apps.removeTestingGroup()`

        :param group_id:
        """

        params = self.get_set_params(locals())
        response = await self.api.request("apps.removeTestingGroup", params)
        model = BaseBoolResponse
        return model(**response).response

    async def remove_users_from_testing_groups(
        self,
        user_ids: typing.List[int],
        **kwargs: typing.Any,
    ) -> bool:
        """Method `apps.removeUsersFromTestingGroups()`

        :param user_ids:
        """

        params = self.get_set_params(locals())
        response = await self.api.request("apps.removeUsersFromTestingGroups", params)
        model = BaseBoolResponse
        return model(**response).response

    async def send_request(
        self,
        user_id: int,
        key: typing.Optional[str] = None,
        name: typing.Optional[str] = None,
        separate: typing.Optional[bool] = None,
        text: typing.Optional[str] = None,
        type: typing.Optional[str] = None,
        **kwargs: typing.Any,
    ) -> int:
        """Method `apps.sendRequest()`

        :param user_id: id of the user to send a request
        :param key: special string key to be sent with the request
        :param name:
        :param separate:
        :param text: request text
        :param type: request type. Values: 'invite' - if the request is sent to a user who does not have the app installed,, 'request' - if a user has already installed the app
        """

        params = self.get_set_params(locals())
        response = await self.api.request("apps.sendRequest", params)
        model = AppsSendRequestResponse
        return model(**response).response

    async def update_meta_for_testing_group(
        self,
        name: str,
        platforms: typing.List[typing.Literal["mobile", "web", "mvk"]],
        webview: str,
        group_id: typing.Optional[int] = None,
        user_ids: typing.Optional[typing.List[int]] = None,
        **kwargs: typing.Any,
    ) -> AppsCreatedGroupResponseModel:
        """Method `apps.updateMetaForTestingGroup()`

        :param name:
        :param platforms:
        :param webview:
        :param group_id:
        :param user_ids:
        """

        params = self.get_set_params(locals())
        response = await self.api.request("apps.updateMetaForTestingGroup", params)
        model = AppsCreatedGroupResponse
        return model(**response).response


__all__ = ("AppsCategory",)
