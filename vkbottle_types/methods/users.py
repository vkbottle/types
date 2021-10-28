import typing
from .base_category import BaseCategory
from vkbottle_types.responses.users import (
    GetFollowersFieldsResponse,
    GetFollowersResponse,
    GetFollowersResponseModel,
    GetResponse,
    GetSubscriptionsExtendedResponse,
    GetSubscriptionsResponse,
    GetSubscriptionsResponseModel,
    SearchResponse,
    SearchResponseModel,
    UsersUserFull
)
from vkbottle_types.responses.base import OkResponse


class UsersCategory(BaseCategory):
    async def get(
        self,
        user_ids: typing.Optional[typing.List[str]] = None,
        fields: typing.Optional[typing.List[str]] = None,
        name_case: typing.Optional[str] = None,
        **kwargs
    ) -> typing.List[UsersUserFull]:
        """Returns detailed information on users.
        :param user_ids: User IDs or screen names ('screen_name'). By default, current user ID.
        :param fields: Profile fields to return. Sample values: 'nickname', 'screen_name', 'sex', 'bdate' (birthdate), 'city', 'country', 'timezone', 'photo', 'photo_medium', 'photo_big', 'has_mobile', 'contacts', 'education', 'online', 'counters', 'relation', 'last_seen', 'activity', 'can_write_private_message', 'can_see_all_posts', 'can_post', 'universities', 'can_invite_to_chats'
        :param name_case: Case for declension of user name and surname: 'nom' — nominative (default), 'gen' — genitive , 'dat' — dative, 'acc' — accusative , 'ins' — instrumental , 'abl' — prepositional
        """

        params = self.get_set_params(locals())
        response = await self.api.request("users.get", params)
        model = GetResponse
        return model(**response).response

    async def get_followers(
        self,
        user_id: typing.Optional[int] = None,
        offset: typing.Optional[int] = None,
        count: typing.Optional[int] = None,
        fields: typing.Optional[typing.List[str]] = None,
        name_case: typing.Optional[str] = None,
        **kwargs
    ) -> GetFollowersResponseModel:
        """Returns a list of IDs of followers of the user in question, sorted by date added, most recent first.
        :param user_id: User ID.
        :param offset: Offset needed to return a specific subset of followers.
        :param count: Number of followers to return.
        :param fields: Profile fields to return. Sample values: 'nickname', 'screen_name', 'sex', 'bdate' (birthdate), 'city', 'country', 'timezone', 'photo', 'photo_medium', 'photo_big', 'has_mobile', 'rate', 'contacts', 'education', 'online'.
        :param name_case: Case for declension of user name and surname: 'nom' — nominative (default), 'gen' — genitive , 'dat' — dative, 'acc' — accusative , 'ins' — instrumental , 'abl' — prepositional
        """

        params = self.get_set_params(locals())
        response = await self.api.request("users.getFollowers", params)
        model = self.get_model(
            {("fields",): GetFollowersFieldsResponse},
            default=GetFollowersResponse,
            params=params,
        )
        return model(**response).response

    async def get_subscriptions(
        self,
        user_id: typing.Optional[int] = None,
        extended: typing.Optional[bool] = None,
        offset: typing.Optional[int] = None,
        count: typing.Optional[int] = None,
        fields: typing.Optional[typing.List[str]] = None,
        **kwargs
    ) -> GetSubscriptionsResponseModel:
        """Returns a list of IDs of users and communities followed by the user.
        :param user_id: User ID.
        :param extended: '1' — to return a combined list of users and communities, '0' — to return separate lists of users and communities (default)
        :param offset: Offset needed to return a specific subset of subscriptions.
        :param count: Number of users and communities to return.
        :param fields:
        """

        params = self.get_set_params(locals())
        response = await self.api.request("users.getSubscriptions", params)
        model = self.get_model(
            {("extended",): GetSubscriptionsExtendedResponse},
            default=GetSubscriptionsResponse,
            params=params,
        )
        return model(**response).response

    async def report(
        self, user_id: int, type: str, comment: typing.Optional[str] = None, **kwargs
    ) -> int:
        """Reports (submits a complain about) a user.
        :param user_id: ID of the user about whom a complaint is being made.
        :param type: Type of complaint: 'porn' - pornography, 'spam' - spamming, 'insult' - abusive behavior, 'advertisement' - disruptive advertisements
        :param comment: Comment describing the complaint.
        """

        params = self.get_set_params(locals())
        response = await self.api.request("users.report", params)
        model = OkResponse
        return model(**response).response

    async def search(
        self,
        q: typing.Optional[str] = None,
        sort: typing.Optional[int] = None,
        offset: typing.Optional[int] = None,
        count: typing.Optional[int] = None,
        fields: typing.Optional[typing.List[str]] = None,
        city: typing.Optional[int] = None,
        country: typing.Optional[int] = None,
        hometown: typing.Optional[str] = None,
        university_country: typing.Optional[int] = None,
        university: typing.Optional[int] = None,
        university_year: typing.Optional[int] = None,
        university_faculty: typing.Optional[int] = None,
        university_chair: typing.Optional[int] = None,
        sex: typing.Optional[int] = None,
        status: typing.Optional[int] = None,
        age_from: typing.Optional[int] = None,
        age_to: typing.Optional[int] = None,
        birth_day: typing.Optional[int] = None,
        birth_month: typing.Optional[int] = None,
        birth_year: typing.Optional[int] = None,
        online: typing.Optional[bool] = None,
        has_photo: typing.Optional[bool] = None,
        school_country: typing.Optional[int] = None,
        school_city: typing.Optional[int] = None,
        school_class: typing.Optional[int] = None,
        school: typing.Optional[int] = None,
        school_year: typing.Optional[int] = None,
        religion: typing.Optional[str] = None,
        company: typing.Optional[str] = None,
        position: typing.Optional[str] = None,
        group_id: typing.Optional[int] = None,
        from_list: typing.Optional[typing.List[str]] = None,
        **kwargs
    ) -> SearchResponseModel:
        """Returns a list of users matching the search criteria.
        :param q: Search query string (e.g., 'Vasya Babich').
        :param sort: Sort order: '1' — by date registered, '0' — by rating
        :param offset: Offset needed to return a specific subset of users.
        :param count: Number of users to return.
        :param fields: Profile fields to return. Sample values: 'nickname', 'screen_name', 'sex', 'bdate' (birthdate), 'city', 'country', 'timezone', 'photo', 'photo_medium', 'photo_big', 'has_mobile', 'rate', 'contacts', 'education', 'online',
        :param city: City ID.
        :param country: Country ID.
        :param hometown: City name in a string.
        :param university_country: ID of the country where the user graduated.
        :param university: ID of the institution of higher education.
        :param university_year: Year of graduation from an institution of higher education.
        :param university_faculty: Faculty ID.
        :param university_chair: Chair ID.
        :param sex: '1' — female, '2' — male, '0' — any (default)
        :param status: Relationship status: '1' — Not married, '2' — In a relationship, '3' — Engaged, '4' — Married, '5' — It's complicated, '6' — Actively searching, '7' — In love
        :param age_from: Minimum age.
        :param age_to: Maximum age.
        :param birth_day: Day of birth.
        :param birth_month: Month of birth.
        :param birth_year: Year of birth.
        :param online: '1' — online only, '0' — all users
        :param has_photo: '1' — with photo only, '0' — all users
        :param school_country: ID of the country where users finished school.
        :param school_city: ID of the city where users finished school.
        :param school_class:
        :param school: ID of the school.
        :param school_year: School graduation year.
        :param religion: Users' religious affiliation.
        :param company: Name of the company where users work.
        :param position: Job position.
        :param group_id: ID of a community to search in communities.
        :param from_list:
        """

        params = self.get_set_params(locals())
        response = await self.api.request("users.search", params)
        model = SearchResponse
        return model(**response).response
