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
        fields: typing.Optional[typing.List[UsersFields]] = None,
        from_group_id: typing.Optional[int] = None,
        name_case: typing.Optional[str] = None,
        user_ids: typing.Optional[typing.List[typing.Union["int", "str"]]] = None,
        **kwargs: typing.Any,
    ) -> typing.List[UsersUserFull]:
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
        fields: typing.List[UsersFields],
        count: typing.Optional[int] = None,
        name_case: typing.Optional[str] = None,
        offset: typing.Optional[int] = None,
        user_id: typing.Optional[int] = None,
        **kwargs: typing.Any,
    ) -> UsersGetFollowersFieldsResponseModel: ...

    @typing.overload
    async def get_followers(
        self,
        fields: typing.Optional[typing.List[UsersFields]] = None,
        count: typing.Optional[int] = None,
        name_case: typing.Optional[str] = None,
        offset: typing.Optional[int] = None,
        user_id: typing.Optional[int] = None,
        **kwargs: typing.Any,
    ) -> UsersGetFollowersResponseModel: ...

    async def get_followers(
        self,
        fields: typing.Optional[typing.List[UsersFields]] = None,
        count: typing.Optional[int] = None,
        name_case: typing.Optional[str] = None,
        offset: typing.Optional[int] = None,
        user_id: typing.Optional[int] = None,
        **kwargs: typing.Any,
    ) -> typing.Union[UsersGetFollowersResponseModel, UsersGetFollowersFieldsResponseModel]:
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
        count: typing.Optional[int] = None,
        fields: typing.Optional[typing.List[UsersFields]] = None,
        offset: typing.Optional[int] = None,
        user_id: typing.Optional[int] = None,
        **kwargs: typing.Any,
    ) -> UsersGetSubscriptionsExtendedResponseModel: ...

    @typing.overload
    async def get_subscriptions(
        self,
        extended: typing.Optional[typing.Literal[False]] = None,
        count: typing.Optional[int] = None,
        fields: typing.Optional[typing.List[UsersFields]] = None,
        offset: typing.Optional[int] = None,
        user_id: typing.Optional[int] = None,
        **kwargs: typing.Any,
    ) -> UsersGetSubscriptionsResponseModel: ...

    async def get_subscriptions(
        self,
        extended: typing.Optional[bool] = None,
        count: typing.Optional[int] = None,
        fields: typing.Optional[typing.List[UsersFields]] = None,
        offset: typing.Optional[int] = None,
        user_id: typing.Optional[int] = None,
        **kwargs: typing.Any,
    ) -> typing.Union[UsersGetSubscriptionsResponseModel, UsersGetSubscriptionsExtendedResponseModel]:
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
        comment: typing.Optional[str] = None,
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
        age_from: typing.Optional[int] = None,
        age_to: typing.Optional[int] = None,
        birth_day: typing.Optional[int] = None,
        birth_month: typing.Optional[int] = None,
        birth_year: typing.Optional[int] = None,
        city: typing.Optional[int] = None,
        city_id: typing.Optional[int] = None,
        company: typing.Optional[str] = None,
        count: typing.Optional[int] = None,
        country: typing.Optional[int] = None,
        country_id: typing.Optional[int] = None,
        fields: typing.Optional[typing.List[UsersFields]] = None,
        from_group_id: typing.Optional[int] = None,
        from_list: typing.Optional[typing.List[str]] = None,
        group_id: typing.Optional[int] = None,
        has_photo: typing.Optional[bool] = None,
        hometown: typing.Optional[str] = None,
        offset: typing.Optional[int] = None,
        online: typing.Optional[bool] = None,
        position: typing.Optional[str] = None,
        q: typing.Optional[str] = None,
        religion: typing.Optional[str] = None,
        school: typing.Optional[int] = None,
        school_city: typing.Optional[int] = None,
        school_class: typing.Optional[int] = None,
        school_country: typing.Optional[int] = None,
        school_year: typing.Optional[int] = None,
        screen_ref: typing.Optional[str] = None,
        sex: typing.Optional[int] = None,
        sort: typing.Optional[int] = None,
        status: typing.Optional[int] = None,
        university: typing.Optional[int] = None,
        university_chair: typing.Optional[int] = None,
        university_country: typing.Optional[int] = None,
        university_faculty: typing.Optional[int] = None,
        university_year: typing.Optional[int] = None,
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
