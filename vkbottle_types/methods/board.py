import typing
from .base_category import BaseCategory
from vkbottle_types.responses import base, board


class BoardCategory(BaseCategory):
    async def add_topic(
        self,
        group_id: int,
        title: str,
        text: typing.Optional[str] = None,
        from_group: typing.Optional[bool] = None,
        attachments: typing.Optional[typing.List[str]] = None,
        **kwargs
    ) -> board.AddTopicResponseModel:
        """Creates a new topic on a community's discussion board.
        :param group_id: ID of the community that owns the discussion board.
        :param title: Topic title.
        :param text: Text of the topic.
        :param from_group: For a community: '1' — to post the topic as by the community, '0' — to post the topic as by the user (default)
        :param attachments: List of media objects attached to the topic, in the following format: "<owner_id>_<media_id>,<owner_id>_<media_id>", '' — Type of media object: 'photo' — photo, 'video' — video, 'audio' — audio, 'doc' — document, '<owner_id>' — ID of the media owner. '<media_id>' — Media ID. Example: "photo100172_166443618,photo66748_265827614", , "NOTE: If you try to attach more than one reference, an error will be thrown.",
        """

        params = self.get_set_params(locals())
        response = await self.api.request("board.addTopic", params)
        model = board.AddTopicResponse
        return model(**response).response

    async def close_topic(
        self, group_id: int, topic_id: int, **kwargs
    ) -> base.OkResponseModel:
        """Closes a topic on a community's discussion board so that comments cannot be posted.
        :param group_id: ID of the community that owns the discussion board.
        :param topic_id: Topic ID.
        """

        params = self.get_set_params(locals())
        response = await self.api.request("board.closeTopic", params)
        model = base.OkResponse
        return model(**response).response

    async def create_comment(
        self,
        group_id: int,
        topic_id: int,
        message: typing.Optional[str] = None,
        attachments: typing.Optional[typing.List[str]] = None,
        from_group: typing.Optional[bool] = None,
        sticker_id: typing.Optional[int] = None,
        guid: typing.Optional[str] = None,
        **kwargs
    ) -> board.CreateCommentResponseModel:
        """Adds a comment on a topic on a community's discussion board.
        :param group_id: ID of the community that owns the discussion board.
        :param topic_id: ID of the topic to be commented on.
        :param message: (Required if 'attachments' is not set.) Text of the comment.
        :param attachments: (Required if 'text' is not set.) List of media objects attached to the comment, in the following format: "<owner_id>_<media_id>,<owner_id>_<media_id>", '' — Type of media object: 'photo' — photo, 'video' — video, 'audio' — audio, 'doc' — document, '<owner_id>' — ID of the media owner. '<media_id>' — Media ID.
        :param from_group: '1' — to post the comment as by the community, '0' — to post the comment as by the user (default)
        :param sticker_id: Sticker ID.
        :param guid: Unique identifier to avoid repeated comments.
        """

        params = self.get_set_params(locals())
        response = await self.api.request("board.createComment", params)
        model = board.CreateCommentResponse
        return model(**response).response

    async def delete_comment(
        self, group_id: int, topic_id: int, comment_id: int, **kwargs
    ) -> base.OkResponseModel:
        """Deletes a comment on a topic on a community's discussion board.
        :param group_id: ID of the community that owns the discussion board.
        :param topic_id: Topic ID.
        :param comment_id: Comment ID.
        """

        params = self.get_set_params(locals())
        response = await self.api.request("board.deleteComment", params)
        model = base.OkResponse
        return model(**response).response

    async def delete_topic(
        self, group_id: int, topic_id: int, **kwargs
    ) -> base.OkResponseModel:
        """Deletes a topic from a community's discussion board.
        :param group_id: ID of the community that owns the discussion board.
        :param topic_id: Topic ID.
        """

        params = self.get_set_params(locals())
        response = await self.api.request("board.deleteTopic", params)
        model = base.OkResponse
        return model(**response).response

    async def edit_comment(
        self,
        group_id: int,
        topic_id: int,
        comment_id: int,
        message: typing.Optional[str] = None,
        attachments: typing.Optional[typing.List[str]] = None,
        **kwargs
    ) -> base.OkResponseModel:
        """Edits a comment on a topic on a community's discussion board.
        :param group_id: ID of the community that owns the discussion board.
        :param topic_id: Topic ID.
        :param comment_id: ID of the comment on the topic.
        :param message: (Required if 'attachments' is not set). New comment text.
        :param attachments: (Required if 'message' is not set.) List of media objects attached to the comment, in the following format: "<owner_id>_<media_id>,<owner_id>_<media_id>", '' — Type of media object: 'photo' — photo, 'video' — video, 'audio' — audio, 'doc' — document, '<owner_id>' — ID of the media owner. '<media_id>' — Media ID. Example: "photo100172_166443618,photo66748_265827614"
        """

        params = self.get_set_params(locals())
        response = await self.api.request("board.editComment", params)
        model = base.OkResponse
        return model(**response).response

    async def edit_topic(
        self, group_id: int, topic_id: int, title: str, **kwargs
    ) -> base.OkResponseModel:
        """Edits the title of a topic on a community's discussion board.
        :param group_id: ID of the community that owns the discussion board.
        :param topic_id: Topic ID.
        :param title: New title of the topic.
        """

        params = self.get_set_params(locals())
        response = await self.api.request("board.editTopic", params)
        model = base.OkResponse
        return model(**response).response

    async def fix_topic(
        self, group_id: int, topic_id: int, **kwargs
    ) -> base.OkResponseModel:
        """Pins a topic (fixes its place) to the top of a community's discussion board.
        :param group_id: ID of the community that owns the discussion board.
        :param topic_id: Topic ID.
        """

        params = self.get_set_params(locals())
        response = await self.api.request("board.fixTopic", params)
        model = base.OkResponse
        return model(**response).response

    async def get_comments(
        self,
        group_id: int,
        topic_id: int,
        need_likes: typing.Optional[bool] = None,
        start_comment_id: typing.Optional[int] = None,
        offset: typing.Optional[int] = None,
        count: typing.Optional[int] = None,
        extended: typing.Optional[bool] = None,
        sort: typing.Optional[str] = None,
        **kwargs
    ) -> board.GetCommentsResponseModel:
        """Returns a list of comments on a topic on a community's discussion board.
        :param group_id: ID of the community that owns the discussion board.
        :param topic_id: Topic ID.
        :param need_likes: '1' — to return the 'likes' field, '0' — not to return the 'likes' field (default)
        :param start_comment_id:
        :param offset: Offset needed to return a specific subset of comments.
        :param count: Number of comments to return.
        :param extended: '1' — to return information about users who posted comments, '0' — to return no additional fields (default)
        :param sort: Sort order: 'asc' — by creation date in chronological order, 'desc' — by creation date in reverse chronological order,
        """

        params = self.get_set_params(locals())
        response = await self.api.request("board.getComments", params)
        model = self.get_model(
            {("extended",): board.GetCommentsExtendedResponse},
            default=board.GetCommentsResponse,
            params=params,
        )
        return model(**response).response

    async def get_topics(
        self,
        group_id: int,
        topic_ids: typing.Optional[typing.List[int]] = None,
        order: typing.Optional[int] = None,
        offset: typing.Optional[int] = None,
        count: typing.Optional[int] = None,
        extended: typing.Optional[bool] = None,
        preview: typing.Optional[int] = None,
        preview_length: typing.Optional[int] = None,
        **kwargs
    ) -> board.GetTopicsResponseModel:
        """Returns a list of topics on a community's discussion board.
        :param group_id: ID of the community that owns the discussion board.
        :param topic_ids: IDs of topics to be returned (100 maximum). By default, all topics are returned. If this parameter is set, the 'order', 'offset', and 'count' parameters are ignored.
        :param order: Sort order: '1' — by date updated in reverse chronological order. '2' — by date created in reverse chronological order. '-1' — by date updated in chronological order. '-2' — by date created in chronological order. If no sort order is specified, topics are returned in the order specified by the group administrator. Pinned topics are returned first, regardless of the sorting.
        :param offset: Offset needed to return a specific subset of topics.
        :param count: Number of topics to return.
        :param extended: '1' — to return information about users who created topics or who posted there last, '0' — to return no additional fields (default)
        :param preview: '1' — to return the first comment in each topic,, '2' — to return the last comment in each topic,, '0' — to return no comments. By default: '0'.
        :param preview_length: Number of characters after which to truncate the previewed comment. To preview the full comment, specify '0'.
        """

        params = self.get_set_params(locals())
        response = await self.api.request("board.getTopics", params)
        model = self.get_model(
            {("extended",): board.GetTopicsExtendedResponse},
            default=board.GetTopicsResponse,
            params=params,
        )
        return model(**response).response

    async def open_topic(
        self, group_id: int, topic_id: int, **kwargs
    ) -> base.OkResponseModel:
        """Re-opens a previously closed topic on a community's discussion board.
        :param group_id: ID of the community that owns the discussion board.
        :param topic_id: Topic ID.
        """

        params = self.get_set_params(locals())
        response = await self.api.request("board.openTopic", params)
        model = base.OkResponse
        return model(**response).response

    async def restore_comment(
        self, group_id: int, topic_id: int, comment_id: int, **kwargs
    ) -> base.OkResponseModel:
        """Restores a comment deleted from a topic on a community's discussion board.
        :param group_id: ID of the community that owns the discussion board.
        :param topic_id: Topic ID.
        :param comment_id: Comment ID.
        """

        params = self.get_set_params(locals())
        response = await self.api.request("board.restoreComment", params)
        model = base.OkResponse
        return model(**response).response

    async def unfix_topic(
        self, group_id: int, topic_id: int, **kwargs
    ) -> base.OkResponseModel:
        """Unpins a pinned topic from the top of a community's discussion board.
        :param group_id: ID of the community that owns the discussion board.
        :param topic_id: Topic ID.
        """

        params = self.get_set_params(locals())
        response = await self.api.request("board.unfixTopic", params)
        model = base.OkResponse
        return model(**response).response
