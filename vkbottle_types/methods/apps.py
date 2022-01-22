import typing
from typing_extensions import Literal
from .base_category import BaseCategory
from vkbottle_types.responses.base import BaseBoolInt, BoolResponse, OkResponse
from vkbottle_types.responses.apps import (
    AppsCatalogList,
    GetCatalogResponse,
    GetFriendsListResponse,
    GetFriendsListResponseModel,
    GetLeaderboardExtendedResponse,
    GetLeaderboardExtendedResponseModel,
    GetLeaderboardResponse,
    GetLeaderboardResponseModel,
    GetMiniAppPoliciesResponse,
    GetMiniAppPoliciesResponseModel,
    GetResponse,
    GetResponseModel,
    GetScopesResponse,
    GetScopesResponseModel,
    GetScoreResponse,
    SendRequestResponse,
)


class AppsCategory(BaseCategory):
    async def delete_app_requests(self, **kwargs) -> int:
        """Deletes all request notifications from the current app."""

        params = self.get_set_params(locals())
        response = await self.api.request("apps.deleteAppRequests", params)
        model = OkResponse
        return model(**response).response

    async def get(
        self,
        app_id: typing.Optional[int] = None,
        app_ids: typing.Optional[typing.List[str]] = None,
        platform: Literal["android", "ios", "web", "winphone"] = None,
        extended: typing.Optional[bool] = None,
        return_friends: typing.Optional[bool] = None,
        fields: typing.Optional[typing.List[str]] = None,
        name_case: Literal["nom", "gen", "dat", "acc", "ins", "abl"] = None,
        **kwargs
    ) -> GetResponseModel:
        """Returns applications data.

        :param app_id: Application ID
        :param app_ids: List of application ID
        :param platform: platform. Possible values: *'ios' — iOS,, *'android' — Android,, *'winphone' — Windows Phone,, *'web' — приложения на vk.com. By default: 'web'.
        :param extended:
        :param return_friends:
        :param fields: Profile fields to return. Sample values: 'nickname', 'screen_name', 'sex', 'bdate' (birthdate), 'city', 'country', 'timezone', 'photo', 'photo_medium', 'photo_big', 'has_mobile', 'contacts', 'education', 'online', 'counters', 'relation', 'last_seen', 'activity', 'can_write_private_message', 'can_see_all_posts', 'can_post', 'universities', (only if return_friends - 1)
        :param name_case: Case for declension of user name and surname: 'nom' — nominative (default),, 'gen' — genitive,, 'dat' — dative,, 'acc' — accusative,, 'ins' — instrumental,, 'abl' — prepositional. (only if 'return_friends' = '1')
        """

        params = self.get_set_params(locals())
        response = await self.api.request("apps.get", params)
        model = GetResponse
        return model(**response).response

    async def get_catalog(
        self,
        count: int,
        sort: Literal[
            "popular_today", "visitors", "create_date", "growth_rate", "popular_week"
        ] = None,
        offset: typing.Optional[int] = None,
        platform: typing.Optional[str] = None,
        extended: typing.Optional[bool] = None,
        return_friends: typing.Optional[bool] = None,
        fields: typing.Optional[typing.List[str]] = None,
        name_case: typing.Optional[str] = None,
        q: typing.Optional[str] = None,
        genre_id: typing.Optional[int] = None,
        filter: Literal["favorite", "featured", "installed", "new"] = None,
        **kwargs
    ) -> AppsCatalogList:
        """Returns a list of applications (apps) available to users in the App Catalog.

        :param count: Number of apps to return.
        :param sort: Sort order: 'popular_today' — popular for one day (default), 'visitors' — by visitors number , 'create_date' — by creation date, 'growth_rate' — by growth rate, 'popular_week' — popular for one week
        :param offset: Offset required to return a specific subset of apps.
        :param platform:
        :param extended: '1' — to return additional fields 'screenshots', 'MAU', 'catalog_position', and 'international'. If set, 'count' must be less than or equal to '100'. '0' — not to return additional fields (default).
        :param return_friends:
        :param fields:
        :param name_case:
        :param q: Search query string.
        :param genre_id:
        :param filter: 'installed' — to return list of installed apps (only for mobile platform).
        """

        params = self.get_set_params(locals())
        response = await self.api.request("apps.getCatalog", params)
        model = GetCatalogResponse
        return model(**response).response

    async def get_friends_list(
        self,
        extended: typing.Optional[bool] = None,
        count: typing.Optional[int] = None,
        offset: typing.Optional[int] = None,
        type: Literal["invite", "request"] = None,
        fields: typing.Optional[typing.List[str]] = None,
        **kwargs
    ) -> GetFriendsListResponseModel:
        """Creates friends list for requests and invites in current app.

        :param extended:
        :param count: List size.
        :param offset:
        :param type: List type. Possible values: * 'invite' — available for invites (don't play the game),, * 'request' — available for request (play the game). By default: 'invite'.
        :param fields: Additional profile fields, see [vk.com/dev/fields|description].
        """

        params = self.get_set_params(locals())
        response = await self.api.request("apps.getFriendsList", params)
        model = GetFriendsListResponse
        return model(**response).response

    @typing.overload
    async def get_leaderboard(
        self,
        type: Literal["level", "points", "score"],
        _global: typing.Optional[bool] = None,
        extended: typing.Optional[Literal[False]] = ...,
        **kwargs
    ) -> GetLeaderboardResponseModel:
        ...

    @typing.overload
    async def get_leaderboard(
        self,
        type: Literal["level", "points", "score"],
        _global: typing.Optional[bool] = None,
        extended: Literal[True] = ...,
        **kwargs
    ) -> GetLeaderboardExtendedResponseModel:
        ...

    async def get_leaderboard(
        self, type=None, _global=None, extended=None, **kwargs
    ) -> typing.Union[GetLeaderboardResponseModel, GetLeaderboardExtendedResponseModel]:
        """Returns players rating in the game.

        :param type: Leaderboard type. Possible values: *'level' — by level,, *'points' — by mission points,, *'score' — by score ().
        :param _global: Rating type. Possible values: *'1' — global rating among all players,, *'0' — rating among user friends.
        :param extended: 1 — to return additional info about users
        """

        params = self.get_set_params(locals())
        response = await self.api.request("apps.getLeaderboard", params)
        model = self.get_model(
            ((("extended",), GetLeaderboardExtendedResponse),),
            default=GetLeaderboardResponse,
            params=params,
        )
        return model(**response).response

    async def get_mini_app_policies(
        self, app_id: int, **kwargs
    ) -> GetMiniAppPoliciesResponseModel:
        """Returns policies and terms given to a mini app.

        :param app_id: Mini App ID
        """

        params = self.get_set_params(locals())
        response = await self.api.request("apps.getMiniAppPolicies", params)
        model = GetMiniAppPoliciesResponse
        return model(**response).response

    async def get_scopes(
        self, type: Literal["group", "user"] = None, **kwargs
    ) -> GetScopesResponseModel:
        """Returns scopes for auth

        :param type:
        """

        params = self.get_set_params(locals())
        response = await self.api.request("apps.getScopes", params)
        model = GetScopesResponse
        return model(**response).response

    async def get_score(self, user_id: int, **kwargs) -> int:
        """Returns user score in app

        :param user_id:
        """

        params = self.get_set_params(locals())
        response = await self.api.request("apps.getScore", params)
        model = GetScoreResponse
        return model(**response).response

    async def promo_has_active_gift(
        self, promo_id: int, user_id: typing.Optional[int] = None, **kwargs
    ) -> BaseBoolInt:
        """apps.promoHasActiveGift method

        :param promo_id: Id of game promo action
        :param user_id:
        """

        params = self.get_set_params(locals())
        response = await self.api.request("apps.promoHasActiveGift", params)
        model = BoolResponse
        return model(**response).response

    async def promo_use_gift(
        self, promo_id: int, user_id: typing.Optional[int] = None, **kwargs
    ) -> BaseBoolInt:
        """apps.promoUseGift method

        :param promo_id: Id of game promo action
        :param user_id:
        """

        params = self.get_set_params(locals())
        response = await self.api.request("apps.promoUseGift", params)
        model = BoolResponse
        return model(**response).response

    async def send_request(
        self,
        user_id: int,
        text: typing.Optional[str] = None,
        type: Literal["invite", "request"] = None,
        name: typing.Optional[str] = None,
        key: typing.Optional[str] = None,
        separate: typing.Optional[bool] = None,
        **kwargs
    ) -> int:
        """Sends a request to another user in an app that uses VK authorization.

        :param user_id: id of the user to send a request
        :param text: request text
        :param type: request type. Values: 'invite' - if the request is sent to a user who does not have the app installed,, 'request' - if a user has already installed the app
        :param name:
        :param key: special string key to be sent with the request
        :param separate:
        """

        params = self.get_set_params(locals())
        response = await self.api.request("apps.sendRequest", params)
        model = SendRequestResponse
        return model(**response).response
