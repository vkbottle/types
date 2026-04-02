import typing

from vkbottle_types.methods.base_category import BaseCategory
from vkbottle_types.objects import *
from vkbottle_types.responses.likes import *  # noqa: F401,F403  # type: ignore


class LikesCategory(BaseCategory):
    async def add(
        self,
        item_id: int,
        type: str,
        access_key: str | None = None,
        from_group: bool | None = None,
        owner_id: int | None = None,
        **kwargs: typing.Any,
    ) -> LikesAddResponseModel:
        """Method `likes.add()`

        :param item_id: Object ID.
        :param type: Object type: 'post' - post on user or community wall, 'comment' - comment on a wall post, 'photo' - photo, 'audio' - audio, 'video' - video, 'story' - story, 'note' - note, 'photo_comment' - comment on the photo, 'video_comment' - comment on the video, 'topic_comment' - comment in the discussion, 'sitepage' - page of the site where the [vk.com/dev/Like|Like widget] is installed
        :param access_key: Access key required for an object owned by a private entity.
        :param from_group: Impersonate group
        :param owner_id: ID of the user or community that owns the object.
        """

        params = self.get_set_params(locals())
        response = await self.api.request("likes.add", params)
        model = LikesAddResponse
        return model(**response).response

    async def delete(
        self,
        item_id: int,
        type: str,
        access_key: str | None = None,
        from_group: bool | None = None,
        owner_id: int | None = None,
        **kwargs: typing.Any,
    ) -> LikesDeleteResponseModel:
        """Method `likes.delete()`

        :param item_id: Object ID.
        :param type: Object type: 'post' - post on user or community wall, 'comment' - comment on a wall post, 'photo' - photo, 'audio' - audio, 'video' - video, 'story' - story, 'note' - note, 'photo_comment' - comment on the photo, 'video_comment' - comment on the video, 'topic_comment' - comment in the discussion, 'sitepage' - page of the site where the [vk.com/dev/Like|Like widget] is installed
        :param access_key: Access key required for an object owned by a private entity.
        :param from_group: Impersonate group
        :param owner_id: ID of the user or community that owns the object.
        """

        params = self.get_set_params(locals())
        response = await self.api.request("likes.delete", params)
        model = LikesDeleteResponse
        return model(**response).response

    @typing.overload
    async def get_list(
        self,
        type: str,
        extended: typing.Literal[True],
        count: int | None = None,
        fields: list[str] | None = None,
        filter: str | None = None,
        friends_only: int | None = None,
        item_id: int | None = None,
        offset: int | None = None,
        owner_id: int | None = None,
        page_url: str | None = None,
        skip_own: bool | None = None,
        **kwargs: typing.Any,
    ) -> LikesGetListExtendedResponseModel: ...

    @typing.overload
    async def get_list(
        self,
        type: str,
        extended: typing.Literal[False] | None = None,
        count: int | None = None,
        fields: list[str] | None = None,
        filter: str | None = None,
        friends_only: int | None = None,
        item_id: int | None = None,
        offset: int | None = None,
        owner_id: int | None = None,
        page_url: str | None = None,
        skip_own: bool | None = None,
        **kwargs: typing.Any,
    ) -> LikesGetListResponseModel: ...

    async def get_list(
        self,
        type: str,
        extended: bool | None = None,
        count: int | None = None,
        fields: list[str] | None = None,
        filter: str | None = None,
        friends_only: int | None = None,
        item_id: int | None = None,
        offset: int | None = None,
        owner_id: int | None = None,
        page_url: str | None = None,
        skip_own: bool | None = None,
        **kwargs: typing.Any,
    ) -> LikesGetListResponseModel | LikesGetListExtendedResponseModel:
        """Method `likes.getList()`

        :param type: , Object type: 'post' - post on user or community wall, 'comment' - comment on a wall post, 'photo' - photo, 'audio' - audio, 'video' - video, 'story' - story, 'note' - note, 'photo_comment' - comment on the photo, 'video_comment' - comment on the video, 'topic_comment' - comment in the discussion, 'sitepage' - page of the site where the [vk.com/dev/Like|Like widget] is installed
        :param extended: Specifies whether extended information will be returned. '1' - to return extended information about users and communities from the 'Likes' list, '0' - to return no additional information (default)
        :param count: Number of user IDs to return (maximum '1000'). Default is '100' if 'friends_only' is set to '0', otherwise, the default is '10' if 'friends_only' is set to '1'.
        :param fields:
        :param filter: Filters to apply: 'likes' - returns information about all users who liked the object (default), 'copies' - returns information only about users who told their friends about the object
        :param friends_only: Specifies which users are returned: '1' - to return only the current user's friends, '0' - to return all users (default)
        :param item_id: Object ID. If 'type' is set as 'sitepage', 'item_id' can include the 'page_id' parameter value used during initialization of the [vk.com/dev/Like|Like widget].
        :param offset: Offset needed to select a specific subset of users.
        :param owner_id: ID of the user, community, or application that owns the object. If the 'type' parameter is set as 'sitepage', the application ID is passed as 'owner_id'. Use negative value for a community id. If the 'type' parameter is not set, the 'owner_id' is assumed to be either the current user or the same application ID as if the 'type' parameter was set to 'sitepage'.
        :param page_url: URL of the page where the [vk.com/dev/Like|Like widget] is installed. Used instead of the 'item_id' parameter.
        :param skip_own:
        """

        params = self.get_set_params(locals())
        response = await self.api.request("likes.getList", params)
        model = self.get_model(
            ((("extended",), LikesGetListExtendedResponse),),
            default=LikesGetListResponse,
            params=params,
        )
        return model(**response).response

    async def is_liked(
        self,
        item_id: int,
        type: str,
        owner_id: int | None = None,
        user_id: int | None = None,
        **kwargs: typing.Any,
    ) -> LikesIsLikedResponseModel:
        """Method `likes.isLiked()`

        :param item_id: Object ID.
        :param type: Object type: 'post' - post on user or community wall, 'comment' - comment on a wall post, 'photo' - photo, 'audio' - audio, 'video' - video, 'story' - story, 'note' - note, 'photo_comment' - comment on the photo, 'video_comment' - comment on the video, 'topic_comment' - comment in the discussion
        :param owner_id: ID of the user or community that owns the object.
        :param user_id: User ID.
        """

        params = self.get_set_params(locals())
        response = await self.api.request("likes.isLiked", params)
        model = LikesIsLikedResponse
        return model(**response).response


__all__ = ("LikesCategory",)
