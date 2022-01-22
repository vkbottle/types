import typing
from typing_extensions import Literal
from .base_category import BaseCategory
from vkbottle_types.responses.base import OkResponse
from vkbottle_types.responses.newsfeed import (
    GetBannedExtendedResponse,
    GetBannedExtendedResponseModel,
    GetBannedResponse,
    GetBannedResponseModel,
    GetCommentsResponse,
    GetCommentsResponseModel,
    GetListsExtendedResponse,
    GetListsExtendedResponseModel,
    GetListsResponse,
    GetListsResponseModel,
    GetMentionsResponse,
    GetMentionsResponseModel,
    GetRecommendedResponse,
    GetRecommendedResponseModel,
    GetResponse,
    GetResponseModel,
    GetSuggestedSourcesResponse,
    GetSuggestedSourcesResponseModel,
    SaveListResponse,
    SearchExtendedResponse,
    SearchExtendedResponseModel,
    SearchResponse,
    SearchResponseModel,
)


class NewsfeedCategory(BaseCategory):
    async def add_ban(
        self,
        user_ids: typing.Optional[typing.List[int]] = None,
        group_ids: typing.Optional[typing.List[int]] = None,
        **kwargs
    ) -> int:
        """Prevents news from specified users and communities from appearing in the current user's newsfeed.

        :param user_ids:
        :param group_ids:
        """

        params = self.get_set_params(locals())
        response = await self.api.request("newsfeed.addBan", params)
        model = OkResponse
        return model(**response).response

    async def delete_ban(
        self,
        user_ids: typing.Optional[typing.List[int]] = None,
        group_ids: typing.Optional[typing.List[int]] = None,
        **kwargs
    ) -> int:
        """Allows news from previously banned users and communities to be shown in the current user's newsfeed.

        :param user_ids:
        :param group_ids:
        """

        params = self.get_set_params(locals())
        response = await self.api.request("newsfeed.deleteBan", params)
        model = OkResponse
        return model(**response).response

    async def delete_list(self, list_id: int, **kwargs) -> int:
        """newsfeed.deleteList method

        :param list_id:
        """

        params = self.get_set_params(locals())
        response = await self.api.request("newsfeed.deleteList", params)
        model = OkResponse
        return model(**response).response

    async def get(
        self,
        filters: typing.Optional[typing.List[str]] = None,
        return_banned: typing.Optional[bool] = None,
        start_time: typing.Optional[int] = None,
        end_time: typing.Optional[int] = None,
        max_photos: typing.Optional[int] = None,
        source_ids: typing.Optional[str] = None,
        start_from: typing.Optional[str] = None,
        count: typing.Optional[int] = None,
        fields: typing.Optional[typing.List[str]] = None,
        section: typing.Optional[str] = None,
        **kwargs
    ) -> GetResponseModel:
        """Returns data required to show newsfeed for the current user.

        :param filters: Filters to apply: 'post' — new wall posts, 'photo' — new photos, 'photo_tag' — new photo tags, 'wall_photo' — new wall photos, 'friend' — new friends
        :param return_banned: '1' — to return news items from banned sources
        :param start_time: Earliest timestamp (in Unix time) of a news item to return. By default, 24 hours ago.
        :param end_time: Latest timestamp (in Unix time) of a news item to return. By default, the current time.
        :param max_photos: Maximum number of photos to return. By default, '5'.
        :param source_ids: Sources to obtain news from, separated by commas. User IDs can be specified in formats '' or 'u' , where '' is the user's friend ID. Community IDs can be specified in formats '-' or 'g' , where '' is the community ID. If the parameter is not set, all of the user's friends and communities are returned, except for banned sources, which can be obtained with the [vk.com/dev/newsfeed.getBanned|newsfeed.getBanned] method.
        :param start_from: identifier required to get the next page of results. Value for this parameter is returned in 'next_from' field in a reply.
        :param count: Number of news items to return (default 50, maximum 100). For auto feed, you can use the 'new_offset' parameter returned by this method.
        :param fields: Additional fields of [vk.com/dev/fields|profiles] and [vk.com/dev/fields_groups|communities] to return.
        :param section:
        """

        params = self.get_set_params(locals())
        response = await self.api.request("newsfeed.get", params)
        model = GetResponse
        return model(**response).response

    @typing.overload
    async def get_banned(
        self,
        extended: typing.Optional[Literal[False]] = ...,
        fields: typing.Optional[typing.List[str]] = None,
        name_case: Literal["nom", "gen", "dat", "acc", "ins", "abl"] = None,
        **kwargs
    ) -> GetBannedResponseModel:
        ...

    @typing.overload
    async def get_banned(
        self,
        extended: Literal[True] = ...,
        fields: typing.Optional[typing.List[str]] = None,
        name_case: Literal["nom", "gen", "dat", "acc", "ins", "abl"] = None,
        **kwargs
    ) -> GetBannedExtendedResponseModel:
        ...

    async def get_banned(
        self, extended=None, fields=None, name_case=None, **kwargs
    ) -> typing.Union[GetBannedResponseModel, GetBannedExtendedResponseModel]:
        """Returns a list of users and communities banned from the current user's newsfeed.

        :param extended: '1' — return extra information about users and communities
        :param fields: Profile fields to return.
        :param name_case: Case for declension of user name and surname: 'nom' — nominative (default), 'gen' — genitive , 'dat' — dative, 'acc' — accusative , 'ins' — instrumental , 'abl' — prepositional
        """

        params = self.get_set_params(locals())
        response = await self.api.request("newsfeed.getBanned", params)
        model = self.get_model(
            ((("extended",), GetBannedExtendedResponse),),
            default=GetBannedResponse,
            params=params,
        )
        return model(**response).response

    async def get_comments(
        self,
        count: typing.Optional[int] = None,
        filters: typing.Optional[typing.List[str]] = None,
        reposts: typing.Optional[str] = None,
        start_time: typing.Optional[int] = None,
        end_time: typing.Optional[int] = None,
        last_comments_count: typing.Optional[int] = None,
        start_from: typing.Optional[str] = None,
        fields: typing.Optional[typing.List[str]] = None,
        **kwargs
    ) -> GetCommentsResponseModel:
        """Returns a list of comments in the current user's newsfeed.

        :param count: Number of comments to return. For auto feed, you can use the 'new_offset' parameter returned by this method.
        :param filters: Filters to apply: 'post' — new comments on wall posts, 'photo' — new comments on photos, 'video' — new comments on videos, 'topic' — new comments on discussions, 'note' — new comments on notes,
        :param reposts: Object ID, comments on repost of which shall be returned, e.g. 'wall1_45486'. (If the parameter is set, the 'filters' parameter is optional.),
        :param start_time: Earliest timestamp (in Unix time) of a comment to return. By default, 24 hours ago.
        :param end_time: Latest timestamp (in Unix time) of a comment to return. By default, the current time.
        :param last_comments_count:
        :param start_from: Identificator needed to return the next page with results. Value for this parameter returns in 'next_from' field.
        :param fields: Additional fields of [vk.com/dev/fields|profiles] and [vk.com/dev/fields_groups|communities] to return.
        """

        params = self.get_set_params(locals())
        response = await self.api.request("newsfeed.getComments", params)
        model = GetCommentsResponse
        return model(**response).response

    @typing.overload
    async def get_lists(
        self,
        list_ids: typing.Optional[typing.List[int]] = None,
        extended: typing.Optional[Literal[False]] = ...,
        **kwargs
    ) -> GetListsResponseModel:
        ...

    @typing.overload
    async def get_lists(
        self,
        list_ids: typing.Optional[typing.List[int]] = None,
        extended: Literal[True] = ...,
        **kwargs
    ) -> GetListsExtendedResponseModel:
        ...

    async def get_lists(
        self, list_ids=None, extended=None, **kwargs
    ) -> typing.Union[GetListsResponseModel, GetListsExtendedResponseModel]:
        """Returns a list of newsfeeds followed by the current user.

        :param list_ids: numeric list identifiers.
        :param extended: Return additional list info
        """

        params = self.get_set_params(locals())
        response = await self.api.request("newsfeed.getLists", params)
        model = self.get_model(
            ((("extended",), GetListsExtendedResponse),),
            default=GetListsResponse,
            params=params,
        )
        return model(**response).response

    async def get_mentions(
        self,
        owner_id: typing.Optional[int] = None,
        start_time: typing.Optional[int] = None,
        end_time: typing.Optional[int] = None,
        offset: typing.Optional[int] = None,
        count: typing.Optional[int] = None,
        **kwargs
    ) -> GetMentionsResponseModel:
        """Returns a list of posts on user walls in which the current user is mentioned.

        :param owner_id: Owner ID.
        :param start_time: Earliest timestamp (in Unix time) of a post to return. By default, 24 hours ago.
        :param end_time: Latest timestamp (in Unix time) of a post to return. By default, the current time.
        :param offset: Offset needed to return a specific subset of posts.
        :param count: Number of posts to return.
        """

        params = self.get_set_params(locals())
        response = await self.api.request("newsfeed.getMentions", params)
        model = GetMentionsResponse
        return model(**response).response

    async def get_recommended(
        self,
        start_time: typing.Optional[int] = None,
        end_time: typing.Optional[int] = None,
        max_photos: typing.Optional[int] = None,
        start_from: typing.Optional[str] = None,
        count: typing.Optional[int] = None,
        fields: typing.Optional[typing.List[str]] = None,
        **kwargs
    ) -> GetRecommendedResponseModel:
        """, Returns a list of newsfeeds recommended to the current user.

        :param start_time: Earliest timestamp (in Unix time) of a news item to return. By default, 24 hours ago.
        :param end_time: Latest timestamp (in Unix time) of a news item to return. By default, the current time.
        :param max_photos: Maximum number of photos to return. By default, '5'.
        :param start_from: 'new_from' value obtained in previous call.
        :param count: Number of news items to return.
        :param fields: Additional fields of [vk.com/dev/fields|profiles] and [vk.com/dev/fields_groups|communities] to return.
        """

        params = self.get_set_params(locals())
        response = await self.api.request("newsfeed.getRecommended", params)
        model = GetRecommendedResponse
        return model(**response).response

    async def get_suggested_sources(
        self,
        offset: typing.Optional[int] = None,
        count: typing.Optional[int] = None,
        shuffle: typing.Optional[bool] = None,
        fields: typing.Optional[typing.List[str]] = None,
        **kwargs
    ) -> GetSuggestedSourcesResponseModel:
        """Returns communities and users that current user is suggested to follow.

        :param offset: offset required to choose a particular subset of communities or users.
        :param count: amount of communities or users to return.
        :param shuffle: shuffle the returned list or not.
        :param fields: list of extra fields to be returned. See available fields for [vk.com/dev/fields|users] and [vk.com/dev/fields_groups|communities].
        """

        params = self.get_set_params(locals())
        response = await self.api.request("newsfeed.getSuggestedSources", params)
        model = GetSuggestedSourcesResponse
        return model(**response).response

    async def ignore_item(
        self,
        type: str,
        owner_id: typing.Optional[int] = None,
        item_id: typing.Optional[int] = None,
        **kwargs
    ) -> int:
        """Hides an item from the newsfeed.

        :param type: Item type. Possible values: *'wall' - post on the wall,, *'tag' - tag on a photo,, *'profilephoto' - profile photo,, *'video' - video,, *'audio' - audio.
        :param owner_id: Item owner's identifier (user or community), "Note that community id must be negative. 'owner_id=1' - user , 'owner_id=-1' - community "
        :param item_id: Item identifier
        """

        params = self.get_set_params(locals())
        response = await self.api.request("newsfeed.ignoreItem", params)
        model = OkResponse
        return model(**response).response

    async def save_list(
        self,
        title: str,
        list_id: typing.Optional[int] = None,
        source_ids: typing.Optional[typing.List[int]] = None,
        no_reposts: typing.Optional[bool] = None,
        **kwargs
    ) -> int:
        """Creates and edits user newsfeed lists

        :param title: list name.
        :param list_id: numeric list identifier (if not sent, will be set automatically).
        :param source_ids: users and communities identifiers to be added to the list. Community identifiers must be negative numbers.
        :param no_reposts: reposts display on and off ('1' is for off).
        """

        params = self.get_set_params(locals())
        response = await self.api.request("newsfeed.saveList", params)
        model = SaveListResponse
        return model(**response).response

    @typing.overload
    async def search(
        self,
        q: typing.Optional[str] = None,
        extended: typing.Optional[Literal[False]] = ...,
        count: typing.Optional[int] = None,
        latitude: typing.Optional[float] = None,
        longitude: typing.Optional[float] = None,
        start_time: typing.Optional[int] = None,
        end_time: typing.Optional[int] = None,
        start_from: typing.Optional[str] = None,
        fields: typing.Optional[typing.List[str]] = None,
        **kwargs
    ) -> SearchResponseModel:
        ...

    @typing.overload
    async def search(
        self,
        q: typing.Optional[str] = None,
        extended: Literal[True] = ...,
        count: typing.Optional[int] = None,
        latitude: typing.Optional[float] = None,
        longitude: typing.Optional[float] = None,
        start_time: typing.Optional[int] = None,
        end_time: typing.Optional[int] = None,
        start_from: typing.Optional[str] = None,
        fields: typing.Optional[typing.List[str]] = None,
        **kwargs
    ) -> SearchExtendedResponseModel:
        ...

    async def search(
        self,
        q=None,
        extended=None,
        count=None,
        latitude=None,
        longitude=None,
        start_time=None,
        end_time=None,
        start_from=None,
        fields=None,
        **kwargs
    ) -> typing.Union[SearchResponseModel, SearchExtendedResponseModel]:
        """Returns search results by statuses.

        :param q: Search query string (e.g., 'New Year').
        :param extended: '1' — to return additional information about the user or community that placed the post.
        :param count: Number of posts to return.
        :param latitude: Geographical latitude point (in degrees, -90 to 90) within which to search.
        :param longitude: Geographical longitude point (in degrees, -180 to 180) within which to search.
        :param start_time: Earliest timestamp (in Unix time) of a news item to return. By default, 24 hours ago.
        :param end_time: Latest timestamp (in Unix time) of a news item to return. By default, the current time.
        :param start_from:
        :param fields: Additional fields of [vk.com/dev/fields|profiles] and [vk.com/dev/fields_groups|communities] to return.
        """

        params = self.get_set_params(locals())
        response = await self.api.request("newsfeed.search", params)
        model = self.get_model(
            ((("extended",), SearchExtendedResponse),),
            default=SearchResponse,
            params=params,
        )
        return model(**response).response

    async def unignore_item(
        self,
        type: str,
        owner_id: int,
        item_id: int,
        track_code: typing.Optional[str] = None,
        **kwargs
    ) -> int:
        """Returns a hidden item to the newsfeed.

        :param type: Item type. Possible values: *'wall' - post on the wall,, *'tag' - tag on a photo,, *'profilephoto' - profile photo,, *'video' - video,, *'audio' - audio.
        :param owner_id: Item owner's identifier (user or community), "Note that community id must be negative. 'owner_id=1' - user , 'owner_id=-1' - community "
        :param item_id: Item identifier
        :param track_code: Track code of unignored item
        """

        params = self.get_set_params(locals())
        response = await self.api.request("newsfeed.unignoreItem", params)
        model = OkResponse
        return model(**response).response

    async def unsubscribe(
        self,
        type: Literal["note", "photo", "post", "topic", "video"],
        item_id: int,
        owner_id: typing.Optional[int] = None,
        **kwargs
    ) -> int:
        """Unsubscribes the current user from specified newsfeeds.

        :param type: Type of object from which to unsubscribe: 'note' — note, 'photo' — photo, 'post' — post on user wall or community wall, 'topic' — topic, 'video' — video
        :param item_id: Object ID.
        :param owner_id: Object owner ID.
        """

        params = self.get_set_params(locals())
        response = await self.api.request("newsfeed.unsubscribe", params)
        model = OkResponse
        return model(**response).response
