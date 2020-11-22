from vkbottle_types.responses import likes
from typing import Optional, Any, List
from .base_category import BaseCategory


class LikesCategory(BaseCategory):
    async def add(
        self,
        type: str,
        item_id: int,
        owner_id: Optional[int] = None,
        access_key: Optional[str] = None,
        **kwargs
    ) -> likes.AddResponseModel:
        """Adds the specified object to the 'Likes' list of the current user.
        :param type: Object type: 'post' — post on user or community wall, 'comment' — comment on a wall post, 'photo' — photo, 'audio' — audio, 'video' — video, 'note' — note, 'photo_comment' — comment on the photo, 'video_comment' — comment on the video, 'topic_comment' — comment in the discussion, 'sitepage' — page of the site where the [vk.com/dev/Like|Like widget] is installed
        :param item_id: Object ID.
        :param owner_id: ID of the user or community that owns the object.
        :param access_key: Access key required for an object owned by a private entity.
        """

        params = self.get_set_params(locals())
        response = await self.api.request("likes.add", params)
        model = likes.AddResponse
        return model(**response).response

    async def delete(
        self,
        type: str,
        item_id: int,
        owner_id: Optional[int] = None,
        access_key: Optional[str] = None,
        **kwargs
    ) -> likes.DeleteResponseModel:
        """Deletes the specified object from the 'Likes' list of the current user.
        :param type: Object type: 'post' — post on user or community wall, 'comment' — comment on a wall post, 'photo' — photo, 'audio' — audio, 'video' — video, 'note' — note, 'photo_comment' — comment on the photo, 'video_comment' — comment on the video, 'topic_comment' — comment in the discussion, 'sitepage' — page of the site where the [vk.com/dev/Like|Like widget] is installed
        :param item_id: Object ID.
        :param owner_id: ID of the user or community that owns the object.
        :param access_key: Access key required for an object owned by a private entity.
        """

        params = self.get_set_params(locals())
        response = await self.api.request("likes.delete", params)
        model = likes.DeleteResponse
        return model(**response).response

    async def get_list(
        self,
        type: str,
        owner_id: Optional[int] = None,
        item_id: Optional[int] = None,
        page_url: Optional[str] = None,
        filter: Optional[str] = None,
        friends_only: Optional[int] = None,
        extended: Optional[bool] = None,
        offset: Optional[int] = None,
        count: Optional[int] = None,
        skip_own: Optional[bool] = None,
        **kwargs
    ) -> likes.GetListResponseModel:
        """Returns a list of IDs of users who added the specified object to their 'Likes' list.
        :param type: , Object type: 'post' — post on user or community wall, 'comment' — comment on a wall post, 'photo' — photo, 'audio' — audio, 'video' — video, 'note' — note, 'photo_comment' — comment on the photo, 'video_comment' — comment on the video, 'topic_comment' — comment in the discussion, 'sitepage' — page of the site where the [vk.com/dev/Like|Like widget] is installed
        :param owner_id: ID of the user, community, or application that owns the object. If the 'type' parameter is set as 'sitepage', the application ID is passed as 'owner_id'. Use negative value for a community id. If the 'type' parameter is not set, the 'owner_id' is assumed to be either the current user or the same application ID as if the 'type' parameter was set to 'sitepage'.
        :param item_id: Object ID. If 'type' is set as 'sitepage', 'item_id' can include the 'page_id' parameter value used during initialization of the [vk.com/dev/Like|Like widget].
        :param page_url: URL of the page where the [vk.com/dev/Like|Like widget] is installed. Used instead of the 'item_id' parameter.
        :param filter: Filters to apply: 'likes' — returns information about all users who liked the object (default), 'copies' — returns information only about users who told their friends about the object
        :param friends_only: Specifies which users are returned: '1' — to return only the current user's friends, '0' — to return all users (default)
        :param extended: Specifies whether extended information will be returned. '1' — to return extended information about users and communities from the 'Likes' list, '0' — to return no additional information (default)
        :param offset: Offset needed to select a specific subset of users.
        :param count: Number of user IDs to return (maximum '1000'). Default is '100' if 'friends_only' is set to '0', otherwise, the default is '10' if 'friends_only' is set to '1'.
        :param skip_own:
        """

        params = self.get_set_params(locals())
        response = await self.api.request("likes.getList", params)
        model = self.get_model(
            {("extended",): likes.GetListExtendedResponse},
            default=likes.GetListResponse,
            params=params,
        )
        return model(**response).response

    async def is_liked(
        self,
        type: str,
        item_id: int,
        user_id: Optional[int] = None,
        owner_id: Optional[int] = None,
        **kwargs
    ) -> likes.IsLikedResponseModel:
        """Checks for the object in the 'Likes' list of the specified user.
        :param type: Object type: 'post' — post on user or community wall, 'comment' — comment on a wall post, 'photo' — photo, 'audio' — audio, 'video' — video, 'note' — note, 'photo_comment' — comment on the photo, 'video_comment' — comment on the video, 'topic_comment' — comment in the discussion
        :param item_id: Object ID.
        :param user_id: User ID.
        :param owner_id: ID of the user or community that owns the object.
        """

        params = self.get_set_params(locals())
        response = await self.api.request("likes.isLiked", params)
        model = likes.IsLikedResponse
        return model(**response).response
