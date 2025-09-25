import typing

from vkbottle_types.methods.base_category import BaseCategory
from vkbottle_types.objects import BaseUserGroupFields, StoriesStoryStats
from vkbottle_types.responses.base import (
    BaseOkResponse,
    BaseOkResponseModel,
)
from vkbottle_types.responses.stories import *  # noqa: F401,F403  # type: ignore


class StoriesCategory(BaseCategory):
    async def ban_owner(
        self,
        owners_ids: typing.List[int],
        **kwargs: typing.Any,
    ) -> BaseOkResponseModel:
        """Method `stories.banOwner()`

        :param owners_ids: List of sources IDs
        """

        params = self.get_set_params(locals())
        response = await self.api.request("stories.banOwner", params)
        model = BaseOkResponse
        return model(**response).response

    async def delete(
        self,
        owner_id: typing.Optional[int] = None,
        stories: typing.Optional[typing.List[str]] = None,
        story_id: typing.Optional[int] = None,
        **kwargs: typing.Any,
    ) -> BaseOkResponseModel:
        """Method `stories.delete()`

        :param owner_id: Story owner's ID. Current user id is used by default.
        :param stories:
        :param story_id: Story ID.
        """

        params = self.get_set_params(locals())
        response = await self.api.request("stories.delete", params)
        model = BaseOkResponse
        return model(**response).response

    async def get(
        self,
        extended: typing.Optional[bool] = None,
        fields: typing.Optional[typing.List[BaseUserGroupFields]] = None,
        owner_id: typing.Optional[int] = None,
        **kwargs: typing.Any,
    ) -> StoriesGetV5113ResponseModel:
        """Method `stories.get()`

        :param extended: '1' - to return additional fields for users and communities. Default value is 0.
        :param fields:
        :param owner_id: Owner ID.
        """

        params = self.get_set_params(locals())
        response = await self.api.request("stories.get", params)
        model = StoriesGetV5113Response
        return model(**response).response

    @typing.overload
    async def get_banned(
        self,
        extended: typing.Literal[True],
        fields: typing.Optional[typing.List[BaseUserGroupFields]] = None,
        **kwargs: typing.Any,
    ) -> StoriesGetBannedExtendedResponseModel: ...

    @typing.overload
    async def get_banned(
        self,
        extended: typing.Optional[typing.Literal[False]] = None,
        fields: typing.Optional[typing.List[BaseUserGroupFields]] = None,
        **kwargs: typing.Any,
    ) -> StoriesGetBannedResponseModel: ...

    async def get_banned(
        self,
        extended: typing.Optional[bool] = None,
        fields: typing.Optional[typing.List[BaseUserGroupFields]] = None,
        **kwargs: typing.Any,
    ) -> typing.Union[StoriesGetBannedExtendedResponseModel, StoriesGetBannedResponseModel]:
        """Method `stories.getBanned()`

        :param extended: '1' - to return additional fields for users and communities. Default value is 0.
        :param fields: Additional fields to return
        """

        params = self.get_set_params(locals())
        response = await self.api.request("stories.getBanned", params)
        model = self.get_model(
            ((("extended",), StoriesGetBannedExtendedResponse),),
            default=StoriesGetBannedResponse,
            params=params,
        )
        return model(**response).response

    async def get_by_id(
        self,
        stories: typing.List[str],
        extended: typing.Optional[bool] = None,
        fields: typing.Optional[typing.List[BaseUserGroupFields]] = None,
        **kwargs: typing.Any,
    ) -> StoriesGetByIdExtendedResponseModel:
        """Method `stories.getById()`

        :param stories: Stories IDs separated by commas. Use format {owner_id}+'_'+{story_id}, for example, 12345_54331.
        :param extended: '1' - to return additional fields for users and communities. Default value is 0.
        :param fields: Additional fields to return
        """

        params = self.get_set_params(locals())
        response = await self.api.request("stories.getById", params)
        model = StoriesGetByIdExtendedResponse
        return model(**response).response

    async def get_photo_upload_server(
        self,
        add_to_news: typing.Optional[bool] = None,
        clickable_stickers: typing.Optional[str] = None,
        group_id: typing.Optional[int] = None,
        link_text: typing.Optional[str] = None,
        link_url: typing.Optional[str] = None,
        reply_to_story: typing.Optional[str] = None,
        user_ids: typing.Optional[typing.List[int]] = None,
        **kwargs: typing.Any,
    ) -> StoriesGetPhotoUploadServerResponseModel:
        """Method `stories.getPhotoUploadServer()`

        :param add_to_news: 1 - to add the story to friend's feed.
        :param clickable_stickers:
        :param group_id: ID of the community to upload the story (should be verified or with the "fire" icon).
        :param link_text: Link text (for community's stories only).
        :param link_url: Link URL. Internal links on https://vk.ru only.
        :param reply_to_story: ID of the story to reply with the current.
        :param user_ids: List of users IDs who can see the story.
        """

        params = self.get_set_params(locals())
        response = await self.api.request("stories.getPhotoUploadServer", params)
        model = StoriesGetPhotoUploadServerResponse
        return model(**response).response

    async def get_replies(
        self,
        owner_id: int,
        story_id: int,
        access_key: typing.Optional[str] = None,
        extended: typing.Optional[bool] = None,
        fields: typing.Optional[typing.List[BaseUserGroupFields]] = None,
        **kwargs: typing.Any,
    ) -> StoriesGetV5113ResponseModel:
        """Method `stories.getReplies()`

        :param owner_id: Story owner ID.
        :param story_id: Story ID.
        :param access_key: Access key for the private object.
        :param extended: '1' - to return additional fields for users and communities. Default value is 0.
        :param fields: Additional fields to return
        """

        params = self.get_set_params(locals())
        response = await self.api.request("stories.getReplies", params)
        model = StoriesGetV5113Response
        return model(**response).response

    async def get_stats(
        self,
        owner_id: int,
        story_id: int,
        **kwargs: typing.Any,
    ) -> "StoriesStoryStats":
        """Method `stories.getStats()`

        :param owner_id: Story owner ID.
        :param story_id: Story ID.
        """

        params = self.get_set_params(locals())
        response = await self.api.request("stories.getStats", params)
        model = StoriesGetStatsResponse
        return model(**response).response

    async def get_video_upload_server(
        self,
        add_to_news: typing.Optional[bool] = None,
        clickable_stickers: typing.Optional[str] = None,
        group_id: typing.Optional[int] = None,
        link_text: typing.Optional[str] = None,
        link_url: typing.Optional[str] = None,
        reply_to_story: typing.Optional[str] = None,
        user_ids: typing.Optional[typing.List[int]] = None,
        **kwargs: typing.Any,
    ) -> StoriesGetVideoUploadServerResponseModel:
        """Method `stories.getVideoUploadServer()`

        :param add_to_news: 1 - to add the story to friend's feed.
        :param clickable_stickers:
        :param group_id: ID of the community to upload the story (should be verified or with the "fire" icon).
        :param link_text: Link text (for community's stories only).
        :param link_url: Link URL. Internal links on https://vk.ru only.
        :param reply_to_story: ID of the story to reply with the current.
        :param user_ids: List of users IDs who can see the story.
        """

        params = self.get_set_params(locals())
        response = await self.api.request("stories.getVideoUploadServer", params)
        model = StoriesGetVideoUploadServerResponse
        return model(**response).response

    async def get_viewers(
        self,
        story_id: int,
        count: typing.Optional[int] = None,
        extended: typing.Optional[bool] = None,
        fields: typing.Optional[typing.List[BaseUserGroupFields]] = None,
        offset: typing.Optional[int] = None,
        owner_id: typing.Optional[int] = None,
        **kwargs: typing.Any,
    ) -> StoriesGetViewersExtendedV5115ResponseModel:
        """Method `stories.getViewers()`

        :param story_id: Story ID.
        :param count: Maximum number of results.
        :param extended: '1' - to return detailed information about photos
        :param fields:
        :param offset: Offset needed to return a specific subset of results.
        :param owner_id: Story owner ID.
        """

        params = self.get_set_params(locals())
        response = await self.api.request("stories.getViewers", params)
        model = StoriesGetViewersExtendedV5115Response
        return model(**response).response

    async def hide_all_replies(
        self,
        owner_id: int,
        group_id: typing.Optional[int] = None,
        **kwargs: typing.Any,
    ) -> BaseOkResponseModel:
        """Method `stories.hideAllReplies()`

        :param owner_id: ID of the user whose replies should be hidden.
        :param group_id:
        """

        params = self.get_set_params(locals())
        response = await self.api.request("stories.hideAllReplies", params)
        model = BaseOkResponse
        return model(**response).response

    async def hide_reply(
        self,
        owner_id: int,
        story_id: int,
        **kwargs: typing.Any,
    ) -> BaseOkResponseModel:
        """Method `stories.hideReply()`

        :param owner_id: ID of the user whose replies should be hidden.
        :param story_id: Story ID.
        """

        params = self.get_set_params(locals())
        response = await self.api.request("stories.hideReply", params)
        model = BaseOkResponse
        return model(**response).response

    async def save(
        self,
        extended: typing.Optional[bool] = None,
        fields: typing.Optional[typing.List[BaseUserGroupFields]] = None,
        upload_results: typing.Optional[typing.List[str]] = None,
        upload_results_json: typing.Optional[str] = None,
        **kwargs: typing.Any,
    ) -> StoriesSaveResponseModel:
        """Method `stories.save()`

        :param extended:
        :param fields:
        :param upload_results:
        :param upload_results_json:
        """

        params = self.get_set_params(locals())
        response = await self.api.request("stories.save", params)
        model = StoriesSaveResponse
        return model(**response).response

    async def search(
        self,
        count: typing.Optional[int] = None,
        extended: typing.Optional[bool] = None,
        fields: typing.Optional[typing.List[BaseUserGroupFields]] = None,
        latitude: typing.Optional[float] = None,
        longitude: typing.Optional[float] = None,
        mentioned_id: typing.Optional[int] = None,
        place_id: typing.Optional[int] = None,
        q: typing.Optional[str] = None,
        radius: typing.Optional[int] = None,
        **kwargs: typing.Any,
    ) -> StoriesGetV5113ResponseModel:
        """Method `stories.search()`

        :param count:
        :param extended:
        :param fields:
        :param latitude:
        :param longitude:
        :param mentioned_id:
        :param place_id:
        :param q:
        :param radius:
        """

        params = self.get_set_params(locals())
        response = await self.api.request("stories.search", params)
        model = StoriesGetV5113Response
        return model(**response).response

    async def send_interaction(
        self,
        access_key: str,
        is_anonymous: typing.Optional[bool] = None,
        is_broadcast: typing.Optional[bool] = None,
        message: typing.Optional[str] = None,
        unseen_marker: typing.Optional[bool] = None,
        **kwargs: typing.Any,
    ) -> BaseOkResponseModel:
        """Method `stories.sendInteraction()`

        :param access_key:
        :param is_anonymous:
        :param is_broadcast:
        :param message:
        :param unseen_marker:
        """

        params = self.get_set_params(locals())
        response = await self.api.request("stories.sendInteraction", params)
        model = BaseOkResponse
        return model(**response).response

    async def unban_owner(
        self,
        owners_ids: typing.List[int],
        **kwargs: typing.Any,
    ) -> BaseOkResponseModel:
        """Method `stories.unbanOwner()`

        :param owners_ids: List of hidden sources to show stories from.
        """

        params = self.get_set_params(locals())
        response = await self.api.request("stories.unbanOwner", params)
        model = BaseOkResponse
        return model(**response).response


__all__ = ("StoriesCategory",)
