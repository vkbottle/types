import typing

from vkbottle_types.codegen.methods.newsfeed import NewsfeedCategory as _NewsfeedCategory  # type: ignore
from vkbottle_types.objects import BaseUserGroupFields
from vkbottle_types.responses.newsfeed import (
    NewsfeedSearchExtendedResponse,
    NewsfeedSearchExtendedResponseModel,
    NewsfeedSearchExtendedStrictResponse,
    NewsfeedSearchExtendedStrictResponseModel,
    NewsfeedSearchResponse,
    NewsfeedSearchResponseModel,
    NewsfeedSearchStrictResponse,
    NewsfeedSearchStrictResponseModel,
)


class NewsfeedCategory(_NewsfeedCategory):  # type: ignore
    @typing.overload  # type: ignore
    async def search(
        self,
        *,
        strict: typing.Literal[True],
        count: int | None = None,
        end_time: int | None = None,
        fields: list[BaseUserGroupFields] | None = None,
        latitude: float | None = None,
        longitude: float | None = None,
        q: str | None = None,
        start_from: str | None = None,
        start_time: int | None = None,
    ) -> NewsfeedSearchStrictResponseModel: ...

    @typing.overload
    async def search(
        self,
        *,
        extended: typing.Literal[True],
        count: int | None = None,
        end_time: int | None = None,
        fields: list[BaseUserGroupFields] | None = None,
        latitude: float | None = None,
        longitude: float | None = None,
        q: str | None = None,
        start_from: str | None = None,
        start_time: int | None = None,
    ) -> NewsfeedSearchExtendedResponseModel: ...

    @typing.overload
    async def search(
        self,
        *,
        strict: typing.Literal[True],
        extended: typing.Literal[True],
        count: int | None = None,
        end_time: int | None = None,
        fields: list[BaseUserGroupFields] | None = None,
        latitude: float | None = None,
        longitude: float | None = None,
        q: str | None = None,
        start_from: str | None = None,
        start_time: int | None = None,
    ) -> NewsfeedSearchExtendedStrictResponseModel: ...

    @typing.overload
    async def search(
        self,
        *,
        count: int | None = None,
        end_time: int | None = None,
        fields: list[BaseUserGroupFields] | None = None,
        latitude: float | None = None,
        longitude: float | None = None,
        q: str | None = None,
        start_from: str | None = None,
        start_time: int | None = None,
    ) -> NewsfeedSearchResponseModel: ...

    async def search(
        self,
        *,
        extended: bool | None = None,
        strict: bool | None = None,
        count: int | None = None,
        end_time: int | None = None,
        fields: list[BaseUserGroupFields] | None = None,
        latitude: float | None = None,
        longitude: float | None = None,
        q: str | None = None,
        start_from: str | None = None,
        start_time: int | None = None,
        **kwargs: typing.Any,
    ) -> (
        NewsfeedSearchResponseModel
        | NewsfeedSearchExtendedResponseModel
        | NewsfeedSearchExtendedStrictResponseModel
        | NewsfeedSearchStrictResponseModel
    ):
        """Method `newsfeed.search()`

        :param extended: '1' - to return additional information about the user or community that placed the post.
        :param count: Number of posts to return.
        :param end_time: Latest timestamp (in Unix time) of a news item to return. By default, the current time.
        :param fields: Additional fields of [vk.ru/dev/fields|profiles] and [vk.ru/dev/fields_groups|communities] to return.
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
                (("strict",), NewsfeedSearchStrictResponse),
                (("extended",), NewsfeedSearchExtendedResponse),
                (("extended", "strict"), NewsfeedSearchExtendedStrictResponse),
            ),
            default=NewsfeedSearchResponse,
            params=params,
        )
        return model(**response).response
