import typing

from typing_extensions import Literal
from vkbottle_types.methods.base_category import BaseCategory
from vkbottle_types.responses.base import OkResponse
from vkbottle_types.responses.board import (
    AddTopicResponse,
    CreateCommentResponse,
    GetCommentsExtendedResponse,
    GetCommentsExtendedResponseModel,
    GetCommentsResponse,
    GetCommentsResponseModel,
    GetTopicsExtendedResponse,
    GetTopicsExtendedResponseModel,
    GetTopicsResponse,
    GetTopicsResponseModel,
)


class BoardCategory(BaseCategory):
    async def add_topic(
        self,
        group_id: int,
        title: str,
        text: typing.Optional[str] = None,
        from_group: typing.Optional[bool] = None,
        attachments: typing.Optional[typing.List[str]] = None,
        **kwargs
    ) -> int:
        """Creates a new topic on a community's discussion board.

        :param group_id: ID of the community that owns the discussion board.
        :param title: Topic title.
        :param text: Text of the topic.
        :param from_group: For a community: '1' — to post the topic as by the community, '0' — to post the topic as by the user (default)
        :param attachments: List of media objects attached to the topic, in the following format: "<owner_id>_<media_id>,<owner_id>_<media_id>", '' — Type of media object: 'photo' — photo, 'video' — video, 'audio' — audio, 'doc' — document, '<owner_id>' — ID of the media owner. '<media_id>' — Media ID. Example: "photo100172_166443618,photo66748_265827614", , "NOTE: If you try to attach more than one reference, an error will be thrown.",
        """

        params = self.get_set_params(locals())
        response = await self.api.request("board.addTopic", params)
        model = AddTopicResponse
        return model(**response).response

    async def close_topic(self, group_id: int, topic_id: int, **kwargs) -> int:
        """Closes a topic on a community's discussion board so that comments cannot be posted.

        :param group_id: ID of the community that owns the discussion board.
        :param topic_id: Topic ID.
        """

        params = self.get_set_params(locals())
        response = await self.api.request("board.closeTopic", params)
        model = OkResponse
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
    ) -> int:
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
        model = CreateCommentResponse
        return model(**response).response

    async def delete_comment(
        self, group_id: int, topic_id: int, comment_id: int, **kwargs
    ) -> int:
        """Deletes a comment on a topic on a community's discussion board.

        :param group_id: ID of the community that owns the discussion board.
        :param topic_id: Topic ID.
        :param comment_id: Comment ID.
        """

        params = self.get_set_params(locals())
        response = await self.api.request("board.deleteComment", params)
        model = OkResponse
        return model(**response).response

    async def delete_topic(self, group_id: int, topic_id: int, **kwargs) -> int:
        """Deletes a topic from a community's discussion board.

        :param group_id: ID of the community that owns the discussion board.
        :param topic_id: Topic ID.
        """

        params = self.get_set_params(locals())
        response = await self.api.request("board.deleteTopic", params)
        model = OkResponse
        return model(**response).response

    async def edit_comment(
        self,
        group_id: int,
        topic_id: int,
        comment_id: int,
        message: typing.Optional[str] = None,
        attachments: typing.Optional[typing.List[str]] = None,
        **kwargs
    ) -> int:
        """Edits a comment on a topic on a community's discussion board.

        :param group_id: ID of the community that owns the discussion board.
        :param topic_id: Topic ID.
        :param comment_id: ID of the comment on the topic.
        :param message: (Required if 'attachments' is not set). New comment text.
        :param attachments: (Required if 'message' is not set.) List of media objects attached to the comment, in the following format: "<owner_id>_<media_id>,<owner_id>_<media_id>", '' — Type of media object: 'photo' — photo, 'video' — video, 'audio' — audio, 'doc' — document, '<owner_id>' — ID of the media owner. '<media_id>' — Media ID. Example: "photo100172_166443618,photo66748_265827614"
        """

        params = self.get_set_params(locals())
        response = await self.api.request("board.editComment", params)
        model = OkResponse
        return model(**response).response

    async def edit_topic(
        self, group_id: int, topic_id: int, title: str, **kwargs
    ) -> int:
        """Edits the title of a topic on a community's discussion board.

        :param group_id: ID of the community that owns the discussion board.
        :param topic_id: Topic ID.
        :param title: New title of the topic.
        """

        params = self.get_set_params(locals())
        response = await self.api.request("board.editTopic", params)
        model = OkResponse
        return model(**response).response

    async def fix_topic(self, group_id: int, topic_id: int, **kwargs) -> int:
        """Pins a topic (fixes its place) to the top of a community's discussion board.

        :param group_id: ID of the community that owns the discussion board.
        :param topic_id: Topic ID.
        """

        params = self.get_set_params(locals())
        response = await self.api.request("board.fixTopic", params)
        model = OkResponse
        return model(**response).response

    @typing.overload
    async def get_comments(
        self,
        group_id: int,
        topic_id: int,
        need_likes: typing.Optional[bool] = None,
        start_comment_id: typing.Optional[int] = None,
        offset: typing.Optional[int] = None,
        count: typing.Optional[int] = None,
        extended: typing.Optional[Literal[False]] = ...,
        sort: typing.Optional[Literal["asc", "desc"]] = None,
        **kwargs
    ) -> GetCommentsResponseModel:
        ...

    @typing.overload
    async def get_comments(
        self,
        group_id: int,
        topic_id: int,
        need_likes: typing.Optional[bool] = None,
        start_comment_id: typing.Optional[int] = None,
        offset: typing.Optional[int] = None,
        count: typing.Optional[int] = None,
        extended: Literal[True] = ...,
        sort: typing.Optional[Literal["asc", "desc"]] = None,
        **kwargs
    ) -> GetCommentsExtendedResponseModel:
        ...

    async def get_comments(
        self,
        group_id=None,
        topic_id=None,
        need_likes=None,
        start_comment_id=None,
        offset=None,
        count=None,
        extended=None,
        sort=None,
        **kwargs
    ) -> typing.Union[GetCommentsResponseModel, GetCommentsExtendedResponseModel]:
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
            ((("extended",), GetCommentsExtendedResponse),),
            default=GetCommentsResponse,
            params=params,
        )
        return model(**response).response

    @typing.overload
    async def get_topics(
        self,
        group_id: int,
        topic_ids: typing.Optional[typing.List[int]] = None,
        order: typing.Optional[Literal[-2, -1, 0, 1, 2]] = None,
        offset: typing.Optional[int] = None,
        count: typing.Optional[int] = None,
        extended: typing.Optional[Literal[False]] = ...,
        preview: typing.Optional[Literal[0, 1, 2]] = None,
        preview_length: typing.Optional[int] = None,
        **kwargs
    ) -> GetTopicsResponseModel:
        ...

    @typing.overload
    async def get_topics(
        self,
        group_id: int,
        topic_ids: typing.Optional[typing.List[int]] = None,
        order: typing.Optional[Literal[-2, -1, 0, 1, 2]] = None,
        offset: typing.Optional[int] = None,
        count: typing.Optional[int] = None,
        extended: Literal[True] = ...,
        preview: typing.Optional[Literal[0, 1, 2]] = None,
        preview_length: typing.Optional[int] = None,
        **kwargs
    ) -> GetTopicsExtendedResponseModel:
        ...

    async def get_topics(
        self,
        group_id=None,
        topic_ids=None,
        order=None,
        offset=None,
        count=None,
        extended=None,
        preview=None,
        preview_length=None,
        **kwargs
    ) -> typing.Union[GetTopicsResponseModel, GetTopicsExtendedResponseModel]:
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
            ((("extended",), GetTopicsExtendedResponse),),
            default=GetTopicsResponse,
            params=params,
        )
        return model(**response).response

    async def open_topic(self, group_id: int, topic_id: int, **kwargs) -> int:
        """Re-opens a previously closed topic on a community's discussion board.

        :param group_id: ID of the community that owns the discussion board.
        :param topic_id: Topic ID.
        """

        params = self.get_set_params(locals())
        response = await self.api.request("board.openTopic", params)
        model = OkResponse
        return model(**response).response

    async def restore_comment(
        self, group_id: int, topic_id: int, comment_id: int, **kwargs
    ) -> int:
        """Restores a comment deleted from a topic on a community's discussion board.

        :param group_id: ID of the community that owns the discussion board.
        :param topic_id: Topic ID.
        :param comment_id: Comment ID.
        """

        params = self.get_set_params(locals())
        response = await self.api.request("board.restoreComment", params)
        model = OkResponse
        return model(**response).response

    async def unfix_topic(self, group_id: int, topic_id: int, **kwargs) -> int:
        """Unpins a pinned topic from the top of a community's discussion board.

        :param group_id: ID of the community that owns the discussion board.
        :param topic_id: Topic ID.
        """

        params = self.get_set_params(locals())
        response = await self.api.request("board.unfixTopic", params)
        model = OkResponse
        return model(**response).response


__all__ = ("BoardCategory",)
