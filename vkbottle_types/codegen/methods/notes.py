import typing

from vkbottle_types.methods.base_category import BaseCategory
from vkbottle_types.objects import NotesNote
from vkbottle_types.responses.base import (
    BaseOkResponse,
    BaseOkResponseModel,
)
from vkbottle_types.responses.notes import *  # noqa: F401,F403  # type: ignore


class NotesCategory(BaseCategory):
    async def add(
        self,
        text: str,
        title: str,
        privacy_comment: typing.Optional[typing.List[str]] = None,
        privacy_view: typing.Optional[typing.List[str]] = None,
        **kwargs: typing.Any,
    ) -> int:
        """Method `notes.add()`

        :param text: Note text.
        :param title: Note title.
        :param privacy_comment:
        :param privacy_view:
        """

        params = self.get_set_params(locals())
        response = await self.api.request("notes.add", params)
        model = NotesAddResponse
        return model(**response).response

    async def create_comment(
        self,
        message: str,
        note_id: int,
        guid: typing.Optional[str] = None,
        owner_id: typing.Optional[int] = None,
        reply_to: typing.Optional[int] = None,
        **kwargs: typing.Any,
    ) -> int:
        """Method `notes.createComment()`

        :param message: Comment text.
        :param note_id: Note ID.
        :param guid:
        :param owner_id: Note owner ID.
        :param reply_to: ID of the user to whom the reply is addressed (if the comment is a reply to another comment).
        """

        params = self.get_set_params(locals())
        response = await self.api.request("notes.createComment", params)
        model = NotesCreateCommentResponse
        return model(**response).response

    async def delete(
        self,
        note_id: int,
        **kwargs: typing.Any,
    ) -> BaseOkResponseModel:
        """Method `notes.delete()`

        :param note_id: Note ID.
        """

        params = self.get_set_params(locals())
        response = await self.api.request("notes.delete", params)
        model = BaseOkResponse
        return model(**response).response

    async def delete_comment(
        self,
        comment_id: int,
        owner_id: typing.Optional[int] = None,
        **kwargs: typing.Any,
    ) -> BaseOkResponseModel:
        """Method `notes.deleteComment()`

        :param comment_id: Comment ID.
        :param owner_id: Note owner ID.
        """

        params = self.get_set_params(locals())
        response = await self.api.request("notes.deleteComment", params)
        model = BaseOkResponse
        return model(**response).response

    async def edit(
        self,
        note_id: int,
        text: str,
        title: str,
        privacy_comment: typing.Optional[typing.List[str]] = None,
        privacy_view: typing.Optional[typing.List[str]] = None,
        **kwargs: typing.Any,
    ) -> BaseOkResponseModel:
        """Method `notes.edit()`

        :param note_id: Note ID.
        :param text: Note text.
        :param title: Note title.
        :param privacy_comment:
        :param privacy_view:
        """

        params = self.get_set_params(locals())
        response = await self.api.request("notes.edit", params)
        model = BaseOkResponse
        return model(**response).response

    async def edit_comment(
        self,
        comment_id: int,
        message: str,
        owner_id: typing.Optional[int] = None,
        **kwargs: typing.Any,
    ) -> BaseOkResponseModel:
        """Method `notes.editComment()`

        :param comment_id: Comment ID.
        :param message: New comment text.
        :param owner_id: Note owner ID.
        """

        params = self.get_set_params(locals())
        response = await self.api.request("notes.editComment", params)
        model = BaseOkResponse
        return model(**response).response

    async def get(
        self,
        count: typing.Optional[int] = None,
        note_ids: typing.Optional[typing.List[int]] = None,
        offset: typing.Optional[int] = None,
        sort: typing.Optional[int] = None,
        user_id: typing.Optional[int] = None,
        **kwargs: typing.Any,
    ) -> NotesGetResponseModel:
        """Method `notes.get()`

        :param count: Number of notes to return.
        :param note_ids: Note IDs.
        :param offset:
        :param sort:
        :param user_id: Note owner ID.
        """

        params = self.get_set_params(locals())
        response = await self.api.request("notes.get", params)
        model = NotesGetResponse
        return model(**response).response

    async def get_by_id(
        self,
        note_id: int,
        need_wiki: typing.Optional[bool] = None,
        owner_id: typing.Optional[int] = None,
        **kwargs: typing.Any,
    ) -> "NotesNote":
        """Method `notes.getById()`

        :param note_id: Note ID.
        :param need_wiki:
        :param owner_id: Note owner ID.
        """

        params = self.get_set_params(locals())
        response = await self.api.request("notes.getById", params)
        model = NotesGetByIdResponse
        return model(**response).response

    async def get_comments(
        self,
        note_id: int,
        count: typing.Optional[int] = None,
        offset: typing.Optional[int] = None,
        owner_id: typing.Optional[int] = None,
        sort: typing.Optional[int] = None,
        **kwargs: typing.Any,
    ) -> NotesGetCommentsResponseModel:
        """Method `notes.getComments()`

        :param note_id: Note ID.
        :param count: Number of comments to return.
        :param offset:
        :param owner_id: Note owner ID.
        :param sort:
        """

        params = self.get_set_params(locals())
        response = await self.api.request("notes.getComments", params)
        model = NotesGetCommentsResponse
        return model(**response).response

    async def restore_comment(
        self,
        comment_id: int,
        owner_id: typing.Optional[int] = None,
        **kwargs: typing.Any,
    ) -> BaseOkResponseModel:
        """Method `notes.restoreComment()`

        :param comment_id: Comment ID.
        :param owner_id: Note owner ID.
        """

        params = self.get_set_params(locals())
        response = await self.api.request("notes.restoreComment", params)
        model = BaseOkResponse
        return model(**response).response


__all__ = ("NotesCategory",)
