import typing

from vkbottle_types.methods.base_category import BaseCategory
from vkbottle_types.responses.base import (
    BaseOkResponse,
    BaseOkResponseModel,
)
from vkbottle_types.responses.board import *  # noqa: F401,F403  # type: ignore


class BoardCategory(BaseCategory):
    async def add_topic(
        self,
        group_id: int,
        title: str,
        attachments: typing.Optional[typing.List[str]] = None,
        from_group: typing.Optional[bool] = None,
        text: typing.Optional[str] = None,
        **kwargs: typing.Any,
    ) -> int:
        """Method `board.addTopic()`

        :param group_id: ID of the community that owns the discussion board.
        :param title: Topic title.
        :param attachments: List of media objects attached to the topic, in the following format: "<owner_id>_<media_id>,<owner_id>_<media_id>", '' - Type of media object: 'photo' - photo, 'video' - video, 'audio' - audio, 'doc' - document, '<owner_id>' - ID of the media owner. '<media_id>' - Media ID. Example: "photo100172_166443618,photo66748_265827614", , "NOTE: If you try to attach more than one reference, an error will be thrown.",
        :param from_group: For a community: '1' - to post the topic as by the community, '0' - to post the topic as by the user (default)
        :param text: Text of the topic.
        """

        params = self.get_set_params(locals())
        response = await self.api.request("board.addTopic", params)
        model = BoardAddTopicResponse
        return model(**response).response

    async def close_topic(
        self,
        group_id: int,
        topic_id: int,
        **kwargs: typing.Any,
    ) -> BaseOkResponseModel:
        """Method `board.closeTopic()`

        :param group_id: ID of the community that owns the discussion board.
        :param topic_id: Topic ID.
        """

        params = self.get_set_params(locals())
        response = await self.api.request("board.closeTopic", params)
        model = BaseOkResponse
        return model(**response).response

    async def create_comment(
        self,
        group_id: int,
        topic_id: int,
        attachments: typing.Optional[typing.List[str]] = None,
        from_group: typing.Optional[bool] = None,
        guid: typing.Optional[str] = None,
        message: typing.Optional[str] = None,
        sticker_id: typing.Optional[int] = None,
        **kwargs: typing.Any,
    ) -> int:
        """Method `board.createComment()`

        :param group_id: ID of the community that owns the discussion board.
        :param topic_id: ID of the topic to be commented on.
        :param attachments: (Required if 'text' is not set.) List of media objects attached to the comment, in the following format: "<owner_id>_<media_id>,<owner_id>_<media_id>", '' - Type of media object: 'photo' - photo, 'video' - video, 'audio' - audio, 'doc' - document, '<owner_id>' - ID of the media owner. '<media_id>' - Media ID.
        :param from_group: '1' - to post the comment as by the community, '0' - to post the comment as by the user (default)
        :param guid: Unique identifier to avoid repeated comments.
        :param message: (Required if 'attachments' is not set.) Text of the comment.
        :param sticker_id: Sticker ID.
        """

        params = self.get_set_params(locals())
        response = await self.api.request("board.createComment", params)
        model = BoardCreateCommentResponse
        return model(**response).response

    async def delete_comment(
        self,
        comment_id: int,
        group_id: int,
        topic_id: int,
        **kwargs: typing.Any,
    ) -> BaseOkResponseModel:
        """Method `board.deleteComment()`

        :param comment_id: Comment ID.
        :param group_id: ID of the community that owns the discussion board.
        :param topic_id: Topic ID.
        """

        params = self.get_set_params(locals())
        response = await self.api.request("board.deleteComment", params)
        model = BaseOkResponse
        return model(**response).response

    async def delete_topic(
        self,
        group_id: int,
        topic_id: int,
        **kwargs: typing.Any,
    ) -> BaseOkResponseModel:
        """Method `board.deleteTopic()`

        :param group_id: ID of the community that owns the discussion board.
        :param topic_id: Topic ID.
        """

        params = self.get_set_params(locals())
        response = await self.api.request("board.deleteTopic", params)
        model = BaseOkResponse
        return model(**response).response

    async def edit_comment(
        self,
        comment_id: int,
        group_id: int,
        topic_id: int,
        attachments: typing.Optional[typing.List[str]] = None,
        message: typing.Optional[str] = None,
        **kwargs: typing.Any,
    ) -> BaseOkResponseModel:
        """Method `board.editComment()`

        :param comment_id: ID of the comment on the topic.
        :param group_id: ID of the community that owns the discussion board.
        :param topic_id: Topic ID.
        :param attachments: (Required if 'message' is not set.) List of media objects attached to the comment, in the following format: "<owner_id>_<media_id>,<owner_id>_<media_id>", '' - Type of media object: 'photo' - photo, 'video' - video, 'audio' - audio, 'doc' - document, '<owner_id>' - ID of the media owner. '<media_id>' - Media ID. Example: "photo100172_166443618,photo66748_265827614"
        :param message: (Required if 'attachments' is not set). New comment text.
        """

        params = self.get_set_params(locals())
        response = await self.api.request("board.editComment", params)
        model = BaseOkResponse
        return model(**response).response

    async def edit_topic(
        self,
        group_id: int,
        title: str,
        topic_id: int,
        **kwargs: typing.Any,
    ) -> BaseOkResponseModel:
        """Method `board.editTopic()`

        :param group_id: ID of the community that owns the discussion board.
        :param title: New title of the topic.
        :param topic_id: Topic ID.
        """

        params = self.get_set_params(locals())
        response = await self.api.request("board.editTopic", params)
        model = BaseOkResponse
        return model(**response).response

    async def fix_topic(
        self,
        group_id: int,
        topic_id: int,
        **kwargs: typing.Any,
    ) -> BaseOkResponseModel:
        """Method `board.fixTopic()`

        :param group_id: ID of the community that owns the discussion board.
        :param topic_id: Topic ID.
        """

        params = self.get_set_params(locals())
        response = await self.api.request("board.fixTopic", params)
        model = BaseOkResponse
        return model(**response).response

    @typing.overload
    async def get_comments(
        self,
        group_id: int,
        topic_id: int,
        extended: typing.Literal[True],
        count: typing.Optional[int] = None,
        need_likes: typing.Optional[bool] = None,
        offset: typing.Optional[int] = None,
        sort: typing.Optional[str] = None,
        start_comment_id: typing.Optional[int] = None,
        **kwargs: typing.Any,
    ) -> BoardGetCommentsExtendedResponseModel: ...

    @typing.overload
    async def get_comments(
        self,
        group_id: int,
        topic_id: int,
        extended: typing.Optional[typing.Literal[False]] = None,
        count: typing.Optional[int] = None,
        need_likes: typing.Optional[bool] = None,
        offset: typing.Optional[int] = None,
        sort: typing.Optional[str] = None,
        start_comment_id: typing.Optional[int] = None,
        **kwargs: typing.Any,
    ) -> BoardGetCommentsResponseModel: ...

    async def get_comments(
        self,
        group_id: int,
        topic_id: int,
        extended: typing.Optional[bool] = None,
        count: typing.Optional[int] = None,
        need_likes: typing.Optional[bool] = None,
        offset: typing.Optional[int] = None,
        sort: typing.Optional[str] = None,
        start_comment_id: typing.Optional[int] = None,
        **kwargs: typing.Any,
    ) -> typing.Union[BoardGetCommentsResponseModel, BoardGetCommentsExtendedResponseModel]:
        """Method `board.getComments()`

        :param group_id: ID of the community that owns the discussion board.
        :param topic_id: Topic ID.
        :param extended: '1' - to return information about users who posted comments, '0' - to return no additional fields (default)
        :param count: Number of comments to return.
        :param need_likes: '1' - to return the 'likes' field, '0' - not to return the 'likes' field (default)
        :param offset: Offset needed to return a specific subset of comments.
        :param sort: Sort order: 'asc' - by creation date in chronological order, 'desc' - by creation date in reverse chronological order,
        :param start_comment_id:
        """

        params = self.get_set_params(locals())
        response = await self.api.request("board.getComments", params)
        model = self.get_model(
            ((("extended",), BoardGetCommentsExtendedResponse),),
            default=BoardGetCommentsResponse,
            params=params,
        )
        return model(**response).response

    @typing.overload
    async def get_topics(
        self,
        group_id: int,
        extended: typing.Literal[True],
        count: typing.Optional[int] = None,
        offset: typing.Optional[int] = None,
        order: typing.Optional[int] = None,
        preview: typing.Optional[int] = None,
        preview_length: typing.Optional[int] = None,
        topic_ids: typing.Optional[typing.List[int]] = None,
        **kwargs: typing.Any,
    ) -> BoardGetTopicsExtendedResponseModel: ...

    @typing.overload
    async def get_topics(
        self,
        group_id: int,
        extended: typing.Optional[typing.Literal[False]] = None,
        count: typing.Optional[int] = None,
        offset: typing.Optional[int] = None,
        order: typing.Optional[int] = None,
        preview: typing.Optional[int] = None,
        preview_length: typing.Optional[int] = None,
        topic_ids: typing.Optional[typing.List[int]] = None,
        **kwargs: typing.Any,
    ) -> BoardGetTopicsResponseModel: ...

    async def get_topics(
        self,
        group_id: int,
        extended: typing.Optional[bool] = None,
        count: typing.Optional[int] = None,
        offset: typing.Optional[int] = None,
        order: typing.Optional[int] = None,
        preview: typing.Optional[int] = None,
        preview_length: typing.Optional[int] = None,
        topic_ids: typing.Optional[typing.List[int]] = None,
        **kwargs: typing.Any,
    ) -> typing.Union[BoardGetTopicsExtendedResponseModel, BoardGetTopicsResponseModel]:
        """Method `board.getTopics()`

        :param group_id: ID of the community that owns the discussion board.
        :param extended: '1' - to return information about users who created topics or who posted there last, '0' - to return no additional fields (default)
        :param count: Number of topics to return.
        :param offset: Offset needed to return a specific subset of topics.
        :param order: Sort order: '1' - by date updated in reverse chronological order. '2' - by date created in reverse chronological order. '-1' - by date updated in chronological order. '-2' - by date created in chronological order. If no sort order is specified, topics are returned in the order specified by the group administrator. Pinned topics are returned first, regardless of the sorting.
        :param preview: '1' - to return the first comment in each topic,, '2' - to return the last comment in each topic,, '0' - to return no comments. By default: '0'.
        :param preview_length: Number of characters after which to truncate the previewed comment. To preview the full comment, specify '0'.
        :param topic_ids: IDs of topics to be returned (100 maximum). By default, all topics are returned. If this parameter is set, the 'order', 'offset', and 'count' parameters are ignored.
        """

        params = self.get_set_params(locals())
        response = await self.api.request("board.getTopics", params)
        model = self.get_model(
            ((("extended",), BoardGetTopicsExtendedResponse),),
            default=BoardGetTopicsResponse,
            params=params,
        )
        return model(**response).response

    async def open_topic(
        self,
        group_id: int,
        topic_id: int,
        **kwargs: typing.Any,
    ) -> BaseOkResponseModel:
        """Method `board.openTopic()`

        :param group_id: ID of the community that owns the discussion board.
        :param topic_id: Topic ID.
        """

        params = self.get_set_params(locals())
        response = await self.api.request("board.openTopic", params)
        model = BaseOkResponse
        return model(**response).response

    async def restore_comment(
        self,
        comment_id: int,
        group_id: int,
        topic_id: int,
        **kwargs: typing.Any,
    ) -> BaseOkResponseModel:
        """Method `board.restoreComment()`

        :param comment_id: Comment ID.
        :param group_id: ID of the community that owns the discussion board.
        :param topic_id: Topic ID.
        """

        params = self.get_set_params(locals())
        response = await self.api.request("board.restoreComment", params)
        model = BaseOkResponse
        return model(**response).response

    async def unfix_topic(
        self,
        group_id: int,
        topic_id: int,
        **kwargs: typing.Any,
    ) -> BaseOkResponseModel:
        """Method `board.unfixTopic()`

        :param group_id: ID of the community that owns the discussion board.
        :param topic_id: Topic ID.
        """

        params = self.get_set_params(locals())
        response = await self.api.request("board.unfixTopic", params)
        model = BaseOkResponse
        return model(**response).response


__all__ = ("BoardCategory",)
