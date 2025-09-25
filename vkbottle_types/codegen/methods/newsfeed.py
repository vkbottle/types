import typing

from vkbottle_types.methods.base_category import BaseCategory
from vkbottle_types.objects import BaseUserGroupFields, NewsfeedCommentsFilters, NewsfeedNewsfeedItemType, UsersFields
from vkbottle_types.responses.base import (
    BaseBoolResponse,
    BaseOkResponse,
    BaseOkResponseModel,
)
from vkbottle_types.responses.newsfeed import *  # noqa: F401,F403  # type: ignore


class NewsfeedCategory(BaseCategory):
    async def add_ban(
        self,
        group_ids: typing.Optional[typing.List[int]] = None,
        user_ids: typing.Optional[typing.List[int]] = None,
        **kwargs: typing.Any,
    ) -> bool:
        """Method `newsfeed.addBan()`

        :param group_ids:
        :param user_ids:
        """

        params = self.get_set_params(locals())
        response = await self.api.request("newsfeed.addBan", params)
        model = BaseBoolResponse
        return model(**response).response

    async def delete_ban(
        self,
        group_ids: typing.Optional[typing.List[int]] = None,
        user_ids: typing.Optional[typing.List[int]] = None,
        **kwargs: typing.Any,
    ) -> BaseOkResponseModel:
        """Method `newsfeed.deleteBan()`

        :param group_ids:
        :param user_ids:
        """

        params = self.get_set_params(locals())
        response = await self.api.request("newsfeed.deleteBan", params)
        model = BaseOkResponse
        return model(**response).response

    async def delete_list(
        self,
        list_id: int,
        **kwargs: typing.Any,
    ) -> BaseOkResponseModel:
        """Method `newsfeed.deleteList()`

        :param list_id:
        """

        params = self.get_set_params(locals())
        response = await self.api.request("newsfeed.deleteList", params)
        model = BaseOkResponse
        return model(**response).response

    async def get(
        self,
        count: typing.Optional[int] = None,
        end_time: typing.Optional[int] = None,
        fields: typing.Optional[typing.List[BaseUserGroupFields]] = None,
        filters: typing.Optional[typing.List[NewsfeedNewsfeedItemType]] = None,
        max_photos: typing.Optional[int] = None,
        return_banned: typing.Optional[bool] = None,
        section: typing.Optional[str] = None,
        source_ids: typing.Optional[str] = None,
        start_from: typing.Optional[str] = None,
        start_time: typing.Optional[int] = None,
        **kwargs: typing.Any,
    ) -> NewsfeedGenericResponseModel:
        """Method `newsfeed.get()`

        :param count: Number of news items to return (default 50, maximum 100). For auto feed, you can use the 'new_offset' parameter returned by this method.
        :param end_time: Latest timestamp (in Unix time) of a news item to return. By default, the current time.
        :param fields: Additional fields of [vk.ru/dev/fields|profiles] and [vk.ru/dev/fields_groups|communities] to return.
        :param filters: Filters to apply: 'post' - new wall posts, 'photo' - new photos, 'photo_tag' - new photo tags, 'wall_photo' - new wall photos, 'friend' - new friends
        :param max_photos: Maximum number of photos to return. By default, '5'.
        :param return_banned: '1' - to return news items from banned sources
        :param section:
        :param source_ids: Sources to obtain news from, separated by commas. User IDs can be specified in formats '' or 'u' , where '' is the user's friend ID. Community IDs can be specified in formats '-' or 'g' , where '' is the community ID. If the parameter is not set, all of the user's friends and communities are returned, except for banned sources, which can be obtained with the [vk.ru/dev/newsfeed.getBanned|newsfeed.getBanned] method.
        :param start_from: identifier required to get the next page of results. Value for this parameter is returned in 'next_from' field in a reply.
        :param start_time: Earliest timestamp (in Unix time) of a news item to return. By default, 24 hours ago.
        """

        params = self.get_set_params(locals())
        response = await self.api.request("newsfeed.get", params)
        model = NewsfeedGenericResponse
        return model(**response).response

    @typing.overload
    async def get_banned(
        self,
        extended: typing.Literal[True],
        fields: typing.Optional[typing.List[UsersFields]] = None,
        name_case: typing.Optional[str] = None,
        **kwargs: typing.Any,
    ) -> NewsfeedGetBannedExtendedResponseModel: ...

    @typing.overload
    async def get_banned(
        self,
        extended: typing.Optional[typing.Literal[False]] = None,
        fields: typing.Optional[typing.List[UsersFields]] = None,
        name_case: typing.Optional[str] = None,
        **kwargs: typing.Any,
    ) -> NewsfeedGetBannedResponseModel: ...

    async def get_banned(
        self,
        extended: typing.Optional[bool] = None,
        fields: typing.Optional[typing.List[UsersFields]] = None,
        name_case: typing.Optional[str] = None,
        **kwargs: typing.Any,
    ) -> typing.Union[NewsfeedGetBannedResponseModel, NewsfeedGetBannedExtendedResponseModel]:
        """Method `newsfeed.getBanned()`

        :param extended: '1' - return extra information about users and communities
        :param fields: Profile fields to return.
        :param name_case: Case for declension of user name and surname: 'nom' - nominative (default), 'gen' - genitive , 'dat' - dative, 'acc' - accusative , 'ins' - instrumental , 'abl' - prepositional
        """

        params = self.get_set_params(locals())
        response = await self.api.request("newsfeed.getBanned", params)
        model = self.get_model(
            ((("extended",), NewsfeedGetBannedExtendedResponse),),
            default=NewsfeedGetBannedResponse,
            params=params,
        )
        return model(**response).response

    async def get_comments(
        self,
        count: typing.Optional[int] = None,
        end_time: typing.Optional[int] = None,
        fields: typing.Optional[typing.List[BaseUserGroupFields]] = None,
        filters: typing.Optional[typing.List[NewsfeedCommentsFilters]] = None,
        last_comments_count: typing.Optional[int] = None,
        reposts: typing.Optional[str] = None,
        start_from: typing.Optional[str] = None,
        start_time: typing.Optional[int] = None,
        **kwargs: typing.Any,
    ) -> NewsfeedGetCommentsResponseModel:
        """Method `newsfeed.getComments()`

        :param count: Number of comments to return. For auto feed, you can use the 'new_offset' parameter returned by this method.
        :param end_time: Latest timestamp (in Unix time) of a comment to return. By default, the current time.
        :param fields: Additional fields of [vk.ru/dev/fields|profiles] and [vk.ru/dev/fields_groups|communities] to return.
        :param filters: Filters to apply: 'post' - new comments on wall posts, 'photo' - new comments on photos, 'video' - new comments on videos, 'topic' - new comments on discussions, 'note' - new comments on notes,
        :param last_comments_count:
        :param reposts: Object ID, comments on repost of which shall be returned, e.g. 'wall1_45486'. (If the parameter is set, the 'filters' parameter is optional.),
        :param start_from: Identificator needed to return the next page with results. Value for this parameter returns in 'next_from' field.
        :param start_time: Earliest timestamp (in Unix time) of a comment to return. By default, 24 hours ago.
        """

        params = self.get_set_params(locals())
        response = await self.api.request("newsfeed.getComments", params)
        model = NewsfeedGetCommentsResponse
        return model(**response).response

    @typing.overload
    async def get_lists(
        self,
        extended: typing.Literal[True],
        list_ids: typing.Optional[typing.List[int]] = None,
        **kwargs: typing.Any,
    ) -> NewsfeedGetListsExtendedResponseModel: ...

    @typing.overload
    async def get_lists(
        self,
        extended: typing.Optional[typing.Literal[False]] = None,
        list_ids: typing.Optional[typing.List[int]] = None,
        **kwargs: typing.Any,
    ) -> NewsfeedGetListsResponseModel: ...

    async def get_lists(
        self,
        extended: typing.Optional[bool] = None,
        list_ids: typing.Optional[typing.List[int]] = None,
        **kwargs: typing.Any,
    ) -> typing.Union[NewsfeedGetListsResponseModel, NewsfeedGetListsExtendedResponseModel]:
        """Method `newsfeed.getLists()`

        :param extended: Return additional list info
        :param list_ids: numeric list identifiers.
        """

        params = self.get_set_params(locals())
        response = await self.api.request("newsfeed.getLists", params)
        model = self.get_model(
            ((("extended",), NewsfeedGetListsExtendedResponse),),
            default=NewsfeedGetListsResponse,
            params=params,
        )
        return model(**response).response

    async def get_mentions(
        self,
        count: typing.Optional[int] = None,
        end_time: typing.Optional[int] = None,
        offset: typing.Optional[int] = None,
        owner_id: typing.Optional[int] = None,
        start_time: typing.Optional[int] = None,
        **kwargs: typing.Any,
    ) -> NewsfeedGetMentionsResponseModel:
        """Method `newsfeed.getMentions()`

        :param count: Number of posts to return.
        :param end_time: Latest timestamp (in Unix time) of a post to return. By default, the current time.
        :param offset: Offset needed to return a specific subset of posts.
        :param owner_id: Owner ID.
        :param start_time: Earliest timestamp (in Unix time) of a post to return. By default, 24 hours ago.
        """

        params = self.get_set_params(locals())
        response = await self.api.request("newsfeed.getMentions", params)
        model = NewsfeedGetMentionsResponse
        return model(**response).response

    async def get_recommended(
        self,
        count: typing.Optional[int] = None,
        end_time: typing.Optional[int] = None,
        fields: typing.Optional[typing.List[BaseUserGroupFields]] = None,
        max_photos: typing.Optional[int] = None,
        start_from: typing.Optional[str] = None,
        start_time: typing.Optional[int] = None,
        **kwargs: typing.Any,
    ) -> NewsfeedGenericResponseModel:
        """Method `newsfeed.getRecommended()`

        :param count: Number of news items to return.
        :param end_time: Latest timestamp (in Unix time) of a news item to return. By default, the current time.
        :param fields: Additional fields of [vk.ru/dev/fields|profiles] and [vk.ru/dev/fields_groups|communities] to return.
        :param max_photos: Maximum number of photos to return. By default, '5'.
        :param start_from: 'new_from' value obtained in previous call.
        :param start_time: Earliest timestamp (in Unix time) of a news item to return. By default, 24 hours ago.
        """

        params = self.get_set_params(locals())
        response = await self.api.request("newsfeed.getRecommended", params)
        model = NewsfeedGenericResponse
        return model(**response).response

    async def get_suggested_sources(
        self,
        count: typing.Optional[int] = None,
        fields: typing.Optional[typing.List[BaseUserGroupFields]] = None,
        offset: typing.Optional[int] = None,
        shuffle: typing.Optional[bool] = None,
        **kwargs: typing.Any,
    ) -> NewsfeedGetSuggestedSourcesResponseModel:
        """Method `newsfeed.getSuggestedSources()`

        :param count: amount of communities or users to return.
        :param fields: list of extra fields to be returned. See available fields for [vk.ru/dev/fields|users] and [vk.ru/dev/fields_groups|communities].
        :param offset: offset required to choose a particular subset of communities or users.
        :param shuffle: shuffle the returned list or not.
        """

        params = self.get_set_params(locals())
        response = await self.api.request("newsfeed.getSuggestedSources", params)
        model = NewsfeedGetSuggestedSourcesResponse
        return model(**response).response

    async def ignore_item(
        self,
        type: str,
        item_id: typing.Optional[int] = None,
        owner_id: typing.Optional[int] = None,
        **kwargs: typing.Any,
    ) -> NewsfeedIgnoreItemResponseModel:
        """Method `newsfeed.ignoreItem()`

        :param type: Item type. Possible values: *'wall' - post on the wall,, *'tag' - tag on a photo,, *'profilephoto' - profile photo,, *'video' - video,, *'audio' - audio.
        :param item_id: Item identifier
        :param owner_id: Item owner's identifier (user or community), "Note that community id must be negative. 'owner_id=1' - user , 'owner_id=-1' - community "
        """

        params = self.get_set_params(locals())
        response = await self.api.request("newsfeed.ignoreItem", params)
        model = NewsfeedIgnoreItemResponse
        return model(**response).response

    async def save_list(
        self,
        source_ids: typing.List[int],
        title: str,
        list_id: typing.Optional[int] = None,
        no_reposts: typing.Optional[bool] = None,
        **kwargs: typing.Any,
    ) -> int:
        """Method `newsfeed.saveList()`

        :param source_ids: users and communities identifiers to be added to the list. Community identifiers must be negative numbers.
        :param title: list name.
        :param list_id: numeric list identifier (if not sent, will be set automatically).
        :param no_reposts: reposts display on and off ('1' is for off).
        """

        params = self.get_set_params(locals())
        response = await self.api.request("newsfeed.saveList", params)
        model = NewsfeedSaveListResponse
        return model(**response).response

    @typing.overload
    async def search(
        self,
        extended: typing.Literal[True],
        count: typing.Optional[int] = None,
        end_time: typing.Optional[int] = None,
        fields: typing.Optional[typing.List[BaseUserGroupFields]] = None,
        latitude: typing.Optional[float] = None,
        longitude: typing.Optional[float] = None,
        q: typing.Optional[str] = None,
        start_from: typing.Optional[str] = None,
        start_time: typing.Optional[int] = None,
        **kwargs: typing.Any,
    ) -> NewsfeedSearchStrictResponseModel: ...

    @typing.overload
    async def search(
        self,
        extended: typing.Optional[bool] = None,
        count: typing.Optional[int] = None,
        end_time: typing.Optional[int] = None,
        fields: typing.Optional[typing.List[BaseUserGroupFields]] = None,
        latitude: typing.Optional[float] = None,
        longitude: typing.Optional[float] = None,
        q: typing.Optional[str] = None,
        start_from: typing.Optional[str] = None,
        start_time: typing.Optional[int] = None,
        **kwargs: typing.Any,
    ) -> NewsfeedSearchExtendedResponseModel: ...

    @typing.overload
    async def search(
        self,
        count: typing.Optional[int] = None,
        end_time: typing.Optional[int] = None,
        extended: typing.Optional[bool] = None,
        fields: typing.Optional[typing.List[BaseUserGroupFields]] = None,
        latitude: typing.Optional[float] = None,
        longitude: typing.Optional[float] = None,
        q: typing.Optional[str] = None,
        start_from: typing.Optional[str] = None,
        start_time: typing.Optional[int] = None,
        **kwargs: typing.Any,
    ) -> NewsfeedSearchExtendedStrictResponseModel: ...

    @typing.overload
    async def search(
        self,
        count: typing.Optional[int] = None,
        end_time: typing.Optional[int] = None,
        extended: typing.Optional[bool] = None,
        fields: typing.Optional[typing.List[BaseUserGroupFields]] = None,
        latitude: typing.Optional[float] = None,
        longitude: typing.Optional[float] = None,
        q: typing.Optional[str] = None,
        start_from: typing.Optional[str] = None,
        start_time: typing.Optional[int] = None,
        **kwargs: typing.Any,
    ) -> NewsfeedSearchResponseModel: ...

    async def search(
        self,
        extended: typing.Optional[bool] = None,
        count: typing.Optional[int] = None,
        end_time: typing.Optional[int] = None,
        fields: typing.Optional[typing.List[BaseUserGroupFields]] = None,
        latitude: typing.Optional[float] = None,
        longitude: typing.Optional[float] = None,
        q: typing.Optional[str] = None,
        start_from: typing.Optional[str] = None,
        start_time: typing.Optional[int] = None,
        **kwargs: typing.Any,
    ) -> typing.Union[NewsfeedSearchResponseModel, NewsfeedSearchStrictResponseModel, NewsfeedSearchExtendedResponseModel]:
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
                (("extended",), NewsfeedSearchStrictResponse),
                (("strict",), NewsfeedSearchStrictResponse),
                (("extended_strict",), NewsfeedSearchExtendedStrictResponse),
            ),
            default=NewsfeedSearchResponse,
            params=params,
        )
        return model(**response).response

    async def unignore_item(
        self,
        type: str,
        item_id: typing.Optional[int] = None,
        owner_id: typing.Optional[int] = None,
        track_code: typing.Optional[str] = None,
        **kwargs: typing.Any,
    ) -> BaseOkResponseModel:
        """Method `newsfeed.unignoreItem()`

        :param type: Item type. Possible values: *'wall' - post on the wall,, *'tag' - tag on a photo,, *'profilephoto' - profile photo,, *'video' - video,, *'audio' - audio.
        :param item_id: Item identifier
        :param owner_id: Item owner's identifier (user or community), "Note that community id must be negative. 'owner_id=1' - user , 'owner_id=-1' - community "
        :param track_code: Track code of unignored item
        """

        params = self.get_set_params(locals())
        response = await self.api.request("newsfeed.unignoreItem", params)
        model = BaseOkResponse
        return model(**response).response

    async def unsubscribe(
        self,
        item_id: int,
        type: str,
        owner_id: typing.Optional[int] = None,
        **kwargs: typing.Any,
    ) -> BaseOkResponseModel:
        """Method `newsfeed.unsubscribe()`

        :param item_id: Object ID.
        :param type: Type of object from which to unsubscribe: 'note' - note, 'photo' - photo, 'post' - post on user wall or community wall, 'topic' - topic, 'video' - video
        :param owner_id: Object owner ID.
        """

        params = self.get_set_params(locals())
        response = await self.api.request("newsfeed.unsubscribe", params)
        model = BaseOkResponse
        return model(**response).response


__all__ = ("NewsfeedCategory",)
