import typing

from vkbottle_types.methods.base_category import BaseCategory
from vkbottle_types.objects import UsersFields, UsersUserFull
from vkbottle_types.responses.base import (
    BaseOkResponse,
    BaseOkResponseModel,
)
from vkbottle_types.responses.users import *  # noqa: F401,F403  # type: ignore


class UsersCategory(BaseCategory):
    async def get(
        self,
        fields: list[UsersFields] | None = None,
        from_group_id: int | None = None,
        name_case: str | None = None,
        user_ids: list[int | str] | None = None,
        **kwargs: typing.Any,
    ) -> list[UsersUserFull]:
        """Method `users.get()`

        :param fields: Profile fields to return. Sample values: 'nickname', 'screen_name', 'sex', 'bdate' (birthdate), 'city', 'country', 'timezone', 'photo', 'photo_medium', 'photo_big', 'has_mobile', 'contacts', 'education', 'online', 'counters', 'relation', 'last_seen', 'activity', 'can_write_private_message', 'can_see_all_posts', 'can_post', 'universities', 'can_invite_to_chats'
        :param from_group_id:
        :param name_case: Case for declension of user name and surname: 'nom' - nominative (default), 'gen' - genitive , 'dat' - dative, 'acc' - accusative , 'ins' - instrumental , 'abl' - prepositional
        :param user_ids: User IDs or screen names ('screen_name'). By default, current user ID.
        """

        params = self.get_set_params(locals())
        response = await self.api.request("users.get", params)
        model = UsersGetResponse
        return model(**response).response

    @typing.overload
    async def get_followers(
        self,
        fields: list[UsersFields],
        count: int | None = None,
        name_case: str | None = None,
        offset: int | None = None,
        user_id: int | None = None,
        **kwargs: typing.Any,
    ) -> UsersGetFollowersFieldsResponseModel: ...

    @typing.overload
    async def get_followers(
        self,
        fields: list[UsersFields] | None = None,
        count: int | None = None,
        name_case: str | None = None,
        offset: int | None = None,
        user_id: int | None = None,
        **kwargs: typing.Any,
    ) -> UsersGetFollowersResponseModel: ...

    async def get_followers(
        self,
        fields: list[UsersFields] | None = None,
        count: int | None = None,
        name_case: str | None = None,
        offset: int | None = None,
        user_id: int | None = None,
        **kwargs: typing.Any,
    ) -> UsersGetFollowersResponseModel | UsersGetFollowersFieldsResponseModel:
        """Method `users.getFollowers()`

        :param fields: Profile fields to return. Sample values: 'nickname', 'screen_name', 'sex', 'bdate' (birthdate), 'city', 'country', 'timezone', 'photo', 'photo_medium', 'photo_big', 'has_mobile', 'rate', 'contacts', 'education', 'online'.
        :param count: Number of followers to return.
        :param name_case: Case for declension of user name and surname: 'nom' - nominative (default), 'gen' - genitive , 'dat' - dative, 'acc' - accusative , 'ins' - instrumental , 'abl' - prepositional
        :param offset: Offset needed to return a specific subset of followers.
        :param user_id: User ID.
        """

        params = self.get_set_params(locals())
        response = await self.api.request("users.getFollowers", params)
        model = self.get_model(
            ((("fields",), UsersGetFollowersFieldsResponse),),
            default=UsersGetFollowersResponse,
            params=params,
        )
        return model(**response).response

    @typing.overload
    async def get_subscriptions(
        self,
        extended: typing.Literal[True],
        count: int | None = None,
        fields: list[UsersFields] | None = None,
        offset: int | None = None,
        user_id: int | None = None,
        **kwargs: typing.Any,
    ) -> UsersGetSubscriptionsExtendedResponseModel: ...

    @typing.overload
    async def get_subscriptions(
        self,
        extended: typing.Literal[False] | None = None,
        count: int | None = None,
        fields: list[UsersFields] | None = None,
        offset: int | None = None,
        user_id: int | None = None,
        **kwargs: typing.Any,
    ) -> UsersGetSubscriptionsResponseModel: ...

    async def get_subscriptions(
        self,
        extended: bool | None = None,
        count: int | None = None,
        fields: list[UsersFields] | None = None,
        offset: int | None = None,
        user_id: int | None = None,
        **kwargs: typing.Any,
    ) -> UsersGetSubscriptionsExtendedResponseModel | UsersGetSubscriptionsResponseModel:
        """Method `users.getSubscriptions()`

        :param extended: '1' - to return a combined list of users and communities, '0' - to return separate lists of users and communities (default)
        :param count: Number of users and communities to return.
        :param fields:
        :param offset: Offset needed to return a specific subset of subscriptions.
        :param user_id: User ID.
        """

        params = self.get_set_params(locals())
        response = await self.api.request("users.getSubscriptions", params)
        model = self.get_model(
            ((("extended",), UsersGetSubscriptionsExtendedResponse),),
            default=UsersGetSubscriptionsResponse,
            params=params,
        )
        return model(**response).response

    async def report(
        self,
        type: str,
        user_id: int,
        comment: str | None = None,
        **kwargs: typing.Any,
    ) -> BaseOkResponseModel:
        """Method `users.report()`

        :param type: Type of complaint: 'porn' - pornography, 'spam' - spamming, 'insult' - abusive behavior, 'advertisement' - disruptive advertisements
        :param user_id: ID of the user about whom a complaint is being made.
        :param comment: Comment describing the complaint.
        """

        params = self.get_set_params(locals())
        response = await self.api.request("users.report", params)
        model = BaseOkResponse
        return model(**response).response

    async def search(
        self,
        age_from: int | None = None,
        age_to: int | None = None,
        birth_day: int | None = None,
        birth_month: int | None = None,
        birth_year: int | None = None,
        city: int | None = None,
        city_id: int | None = None,
        company: str | None = None,
        count: int | None = None,
        country: int | None = None,
        country_id: int | None = None,
        fields: list[UsersFields] | None = None,
        from_group_id: int | None = None,
        from_list: list[str] | None = None,
        group_id: int | None = None,
        has_photo: bool | None = None,
        hometown: str | None = None,
        offset: int | None = None,
        online: bool | None = None,
        position: str | None = None,
        q: str | None = None,
        religion: str | None = None,
        school: int | None = None,
        school_city: int | None = None,
        school_class: int | None = None,
        school_country: int | None = None,
        school_year: int | None = None,
        screen_ref: str | None = None,
        sex: int | None = None,
        sort: int | None = None,
        status: int | None = None,
        university: int | None = None,
        university_chair: int | None = None,
        university_country: int | None = None,
        university_faculty: int | None = None,
        university_year: int | None = None,
        **kwargs: typing.Any,
    ) -> UsersSearchResponseModel:
        """Method `users.search()`

        :param age_from: Minimum age.
        :param age_to: Maximum age.
        :param birth_day: Day of birth.
        :param birth_month: Month of birth.
        :param birth_year: Year of birth.
        :param city: City ID.
        :param city_id: City ID. Use parameter city instead
        :param company: Name of the company where users work.
        :param count: Number of users to return.
        :param country: Country ID.
        :param country_id: Country ID. Use parameter country instead
        :param fields: Profile fields to return. Sample values: 'nickname', 'screen_name', 'sex', 'bdate' (birthdate), 'city', 'country', 'timezone', 'photo', 'photo_medium', 'photo_big', 'has_mobile', 'rate', 'contacts', 'education', 'online',
        :param from_group_id:
        :param from_list:
        :param group_id: ID of a community to search in communities.
        :param has_photo: '1' - with photo only, '0' - all users
        :param hometown: City name in a string.
        :param offset: Offset needed to return a specific subset of users.
        :param online: '1' - online only, '0' - all users
        :param position: Job position.
        :param q: Search query string (e.g., 'Vasya Babich').
        :param religion: Users' religious affiliation.
        :param school: ID of the school.
        :param school_city: ID of the city where users finished school.
        :param school_class:
        :param school_country: ID of the country where users finished school.
        :param school_year: School graduation year.
        :param screen_ref:
        :param sex: '1' - female, '2' - male, '0' - any (default)
        :param sort: Sort order: '1' - by date registered, '0' - by rating
        :param status: Relationship status: '0' - Not specified, '1' - Not married, '2' - In a relationship, '3' - Engaged, '4' - Married, '5' - It's complicated, '6' - Actively searching, '7' - In love, '8' - In a civil union
        :param university: ID of the institution of higher education.
        :param university_chair: Chair ID.
        :param university_country: ID of the country where the user graduated.
        :param university_faculty: Faculty ID.
        :param university_year: Year of graduation from an institution of higher education.
        """

        params = self.get_set_params(locals())
        response = await self.api.request("users.search", params)
        model = UsersSearchResponse
        return model(**response).response


__all__ = ("UsersCategory",)
