import typing

from vkbottle_types.methods.base_category import BaseCategory
from vkbottle_types.objects import BaseUserGroupFields
from vkbottle_types.responses.newsfeed import *  # noqa: F401,F403


class NewsfeedCategory(BaseCategory):
    async def search(
        self,
        count: typing.Optional[int] = None,
        end_time: typing.Optional[int] = None,
        fields: typing.Optional[typing.List[BaseUserGroupFields]] = None,
        latitude: typing.Optional[float] = None,
        longitude: typing.Optional[float] = None,
        q: typing.Optional[str] = None,
        start_from: typing.Optional[str] = None,
        start_time: typing.Optional[int] = None,
        extended: typing.Optional[bool] = None,
        strict: typing.Optional[bool] = None,
        extended_strict: typing.Optional[bool] = None,
        **kwargs: typing.Any,
    ) -> typing.Dict[str, typing.Any]:
        """Method `newsfeed.search()`

        :param extended: '1' - to return additional information about the user or community that placed the post.
        :param count: Number of posts to return.
        :param end_time: Latest timestamp (in Unix time) of a news item to return. By default, the current time.
        :param fields: Additional fields of [vk.com/dev/fields|profiles] and [vk.com/dev/fields_groups|communities] to return.
        :param latitude: Geographical latitude point (in degrees, -90 to 90) within which to search.
        :param longitude: Geographical longitude point (in degrees, -180 to 180) within which to search.
        :param q: Search query string (e.g., 'New Year').
        :param start_from:
        :param start_time: Earliest timestamp (in Unix time) of a news item to return. By default, 24 hours ago.
        """

        params = self.get_set_params(locals())
        response = await self.api.request("newsfeed.search", params)
        model = self.get_model(
            (
                (("extended",), NewsfeedSearchExtendedResponse),
                (("strict",), NewsfeedSearchStrictResponse),
                (("extended_strict",), NewsfeedSearchExtendedStrictResponse),
            ),
            default=NewsfeedSearchResponse,
            params=params,
        )
        return model(**response).response
