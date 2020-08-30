from vkbottle_types.responses import base, stories as stories_responses
from typing import Optional, Any, List
import typing
from .base_category import BaseCategory

if typing.TYPE_CHECKING:
    from vkbottle_types.objects import base as objects_base


class StoriesCategory(BaseCategory):
    async def ban_owner(self, owners_ids: List[int]) -> base.OkResponseModel:
        """Allows to hide stories from chosen sources from current user's feed.
        :param owners_ids: List of sources IDs
        """

        params = self.get_set_params(locals())
        return base.OkResponse(**await self.api.request("stories.banOwner", params))

    async def delete(self, owner_id: int, story_id: int) -> base.OkResponseModel:
        """Allows to delete story.
        :param owner_id: Story owner's ID. Current user id is used by default.
        :param story_id: Story ID.
        """

        params = self.get_set_params(locals())
        return base.OkResponse(**await self.api.request("stories.delete", params))

    async def get(
        self,
        owner_id: Optional[int] = None,
        extended: Optional[bool] = None,
        fields: Optional[List["objects_base.UserGroupFields"]] = None,
    ) -> stories_responses.GetV5113ResponseModel:
        """Returns stories available for current user.
        :param owner_id: Owner ID.
        :param extended: '1' — to return additional fields for users and communities. Default value is 0.
        :param fields:
        """

        params = self.get_set_params(locals())
        return stories_responses.GetV5113Response(
            **await self.api.request("stories.get", params)
        )

    async def get_banned(
        self,
        extended: Optional[bool] = None,
        fields: Optional[List["objects_base.UserGroupFields"]] = None,
    ) -> stories_responses.GetBannedExtendedResponseModel:
        """Returns list of sources hidden from current user's feed.
        :param extended: '1' — to return additional fields for users and communities. Default value is 0.
        :param fields: Additional fields to return
        """

        params = self.get_set_params(locals())
        return stories_responses.GetBannedExtendedResponse(
            **await self.api.request("stories.getBanned", params)
        )

    async def get_by_id(
        self,
        stories: List[str],
        extended: Optional[bool] = None,
        fields: Optional[List["objects_base.UserGroupFields"]] = None,
    ) -> stories_responses.GetByIdExtendedResponseModel:
        """Returns story by its ID.
        :param stories: Stories IDs separated by commas. Use format {owner_id}+'_'+{story_id}, for example, 12345_54331.
        :param extended: '1' — to return additional fields for users and communities. Default value is 0.
        :param fields: Additional fields to return
        """

        params = self.get_set_params(locals())
        return stories_responses.GetByIdExtendedResponse(
            **await self.api.request("stories.getById", params)
        )

    async def get_photo_upload_server(
        self,
        add_to_news: Optional[bool] = None,
        user_ids: Optional[List[int]] = None,
        reply_to_story: Optional[str] = None,
        link_text: Optional[str] = None,
        link_url: Optional[str] = None,
        group_id: Optional[int] = None,
        clickable_stickers: Optional[str] = None,
    ) -> stories_responses.GetPhotoUploadServerResponseModel:
        """Returns URL for uploading a story with photo.
        :param add_to_news: 1 — to add the story to friend's feed.
        :param user_ids: List of users IDs who can see the story.
        :param reply_to_story: ID of the story to reply with the current.
        :param link_text: Link text (for community's stories only).
        :param link_url: Link URL. Internal links on https://vk.com only.
        :param group_id: ID of the community to upload the story (should be verified or with the "fire" icon).
        :param clickable_stickers:
        """

        params = self.get_set_params(locals())
        return stories_responses.GetPhotoUploadServerResponse(
            **await self.api.request("stories.getPhotoUploadServer", params)
        )

    async def get_replies(
        self,
        owner_id: int,
        story_id: int,
        access_key: Optional[str] = None,
        extended: Optional[bool] = None,
        fields: Optional[List["objects_base.UserGroupFields"]] = None,
    ) -> stories_responses.GetV5113ResponseModel:
        """Returns replies to the story.
        :param owner_id: Story owner ID.
        :param story_id: Story ID.
        :param access_key: Access key for the private object.
        :param extended: '1' — to return additional fields for users and communities. Default value is 0.
        :param fields: Additional fields to return
        """

        params = self.get_set_params(locals())
        return stories_responses.GetV5113Response(
            **await self.api.request("stories.getReplies", params)
        )

    async def get_stats(
        self, owner_id: int, story_id: int
    ) -> stories_responses.GetStatsResponseModel:
        """Returns stories available for current user.
        :param owner_id: Story owner ID.
        :param story_id: Story ID.
        """

        params = self.get_set_params(locals())
        return stories_responses.GetStatsResponse(
            **await self.api.request("stories.getStats", params)
        )

    async def get_video_upload_server(
        self,
        add_to_news: Optional[bool] = None,
        user_ids: Optional[List[int]] = None,
        reply_to_story: Optional[str] = None,
        link_text: Optional[str] = None,
        link_url: Optional[str] = None,
        group_id: Optional[int] = None,
        clickable_stickers: Optional[str] = None,
    ) -> stories_responses.GetVideoUploadServerResponseModel:
        """Allows to receive URL for uploading story with video.
        :param add_to_news: 1 — to add the story to friend's feed.
        :param user_ids: List of users IDs who can see the story.
        :param reply_to_story: ID of the story to reply with the current.
        :param link_text: Link text (for community's stories only).
        :param link_url: Link URL. Internal links on https://vk.com only.
        :param group_id: ID of the community to upload the story (should be verified or with the "fire" icon).
        :param clickable_stickers:
        """

        params = self.get_set_params(locals())
        return stories_responses.GetVideoUploadServerResponse(
            **await self.api.request("stories.getVideoUploadServer", params)
        )

    async def get_viewers(
        self,
        owner_id: int,
        story_id: int,
        count: Optional[int] = None,
        offset: Optional[int] = None,
        extended: Optional[bool] = None,
    ) -> stories_responses.GetViewersExtendedV5115ResponseModel:
        """Returns a list of story viewers.
        :param owner_id: Story owner ID.
        :param story_id: Story ID.
        :param count: Maximum number of results.
        :param offset: Offset needed to return a specific subset of results.
        :param extended: '1' — to return detailed information about photos
        """

        params = self.get_set_params(locals())
        return stories_responses.GetViewersExtendedV5115Response(
            **await self.api.request("stories.getViewers", params)
        )

    async def hide_all_replies(
        self, owner_id: int, group_id: Optional[int] = None
    ) -> base.OkResponseModel:
        """Hides all replies in the last 24 hours from the user to current user's stories.
        :param owner_id: ID of the user whose replies should be hidden.
        :param group_id:
        """

        params = self.get_set_params(locals())
        return base.OkResponse(
            **await self.api.request("stories.hideAllReplies", params)
        )

    async def hide_reply(self, owner_id: int, story_id: int) -> base.OkResponseModel:
        """Hides the reply to the current user's story.
        :param owner_id: ID of the user whose replies should be hidden.
        :param story_id: Story ID.
        """

        params = self.get_set_params(locals())
        return base.OkResponse(**await self.api.request("stories.hideReply", params))

    async def search(
        self,
        q: Optional[str] = None,
        place_id: Optional[int] = None,
        latitude: Optional[float] = None,
        longitude: Optional[float] = None,
        radius: Optional[int] = None,
        mentioned_id: Optional[int] = None,
        count: Optional[int] = None,
        extended: Optional[bool] = None,
        fields: Optional[List[str]] = None,
    ) -> stories_responses.GetV5113ResponseModel:
        """stories.search method
        :param q:
        :param place_id:
        :param latitude:
        :param longitude:
        :param radius:
        :param mentioned_id:
        :param count:
        :param extended:
        :param fields:
        """

        params = self.get_set_params(locals())
        return stories_responses.GetV5113Response(
            **await self.api.request("stories.search", params)
        )

    async def unban_owner(self, owners_ids: List[int]) -> base.OkResponseModel:
        """Allows to show stories from hidden sources in current user's feed.
        :param owners_ids: List of hidden sources to show stories from.
        """

        params = self.get_set_params(locals())
        return base.OkResponse(**await self.api.request("stories.unbanOwner", params))
