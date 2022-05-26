import typing

from typing_extensions import Literal
from vkbottle_types.responses.base import OkResponse
from vkbottle_types.responses.notes import (
    AddResponse,
    CreateCommentResponse,
    GetByIdResponse,
    GetCommentsResponse,
    GetCommentsResponseModel,
    GetResponse,
    GetResponseModel,
    NotesNote,
)

from .base_category import BaseCategory


class NotesCategory(BaseCategory):
    async def add(
        self,
        title: str,
        text: str,
        privacy_view: typing.Optional[typing.List[str]] = None,
        privacy_comment: typing.Optional[typing.List[str]] = None,
        **kwargs
    ) -> int:
        """Creates a new note for the current user.

        :param title: Note title.
        :param text: Note text.
        :param privacy_view:
        :param privacy_comment:
        """

        params = self.get_set_params(locals())
        response = await self.api.request("notes.add", params)
        model = AddResponse
        return model(**response).response

    async def create_comment(
        self,
        note_id: int,
        message: str,
        owner_id: typing.Optional[int] = None,
        reply_to: typing.Optional[int] = None,
        guid: typing.Optional[str] = None,
        **kwargs
    ) -> int:
        """Adds a new comment on a note.

        :param note_id: Note ID.
        :param message: Comment text.
        :param owner_id: Note owner ID.
        :param reply_to: ID of the user to whom the reply is addressed (if the comment is a reply to another comment).
        :param guid:
        """

        params = self.get_set_params(locals())
        response = await self.api.request("notes.createComment", params)
        model = CreateCommentResponse
        return model(**response).response

    async def delete(self, note_id: int, **kwargs) -> int:
        """Deletes a note of the current user.

        :param note_id: Note ID.
        """

        params = self.get_set_params(locals())
        response = await self.api.request("notes.delete", params)
        model = OkResponse
        return model(**response).response

    async def delete_comment(
        self, comment_id: int, owner_id: typing.Optional[int] = None, **kwargs
    ) -> int:
        """Deletes a comment on a note.

        :param comment_id: Comment ID.
        :param owner_id: Note owner ID.
        """

        params = self.get_set_params(locals())
        response = await self.api.request("notes.deleteComment", params)
        model = OkResponse
        return model(**response).response

    async def edit(
        self,
        note_id: int,
        title: str,
        text: str,
        privacy_view: typing.Optional[typing.List[str]] = None,
        privacy_comment: typing.Optional[typing.List[str]] = None,
        **kwargs
    ) -> int:
        """Edits a note of the current user.

        :param note_id: Note ID.
        :param title: Note title.
        :param text: Note text.
        :param privacy_view:
        :param privacy_comment:
        """

        params = self.get_set_params(locals())
        response = await self.api.request("notes.edit", params)
        model = OkResponse
        return model(**response).response

    async def edit_comment(
        self,
        comment_id: int,
        message: str,
        owner_id: typing.Optional[int] = None,
        **kwargs
    ) -> int:
        """Edits a comment on a note.

        :param comment_id: Comment ID.
        :param message: New comment text.
        :param owner_id: Note owner ID.
        """

        params = self.get_set_params(locals())
        response = await self.api.request("notes.editComment", params)
        model = OkResponse
        return model(**response).response

    async def get(
        self,
        note_ids: typing.Optional[typing.List[int]] = None,
        user_id: typing.Optional[int] = None,
        offset: typing.Optional[int] = None,
        count: typing.Optional[int] = None,
        sort: typing.Optional[Literal[0, 1]] = None,
        **kwargs
    ) -> GetResponseModel:
        """Returns a list of notes created by a user.

        :param note_ids: Note IDs.
        :param user_id: Note owner ID.
        :param offset:
        :param count: Number of notes to return.
        :param sort:
        """

        params = self.get_set_params(locals())
        response = await self.api.request("notes.get", params)
        model = GetResponse
        return model(**response).response

    async def get_by_id(
        self,
        note_id: int,
        owner_id: typing.Optional[int] = None,
        need_wiki: typing.Optional[bool] = None,
        **kwargs
    ) -> NotesNote:
        """Returns a note by its ID.

        :param note_id: Note ID.
        :param owner_id: Note owner ID.
        :param need_wiki:
        """

        params = self.get_set_params(locals())
        response = await self.api.request("notes.getById", params)
        model = GetByIdResponse
        return model(**response).response

    async def get_comments(
        self,
        note_id: int,
        owner_id: typing.Optional[int] = None,
        sort: typing.Optional[Literal[0, 1]] = None,
        offset: typing.Optional[int] = None,
        count: typing.Optional[int] = None,
        **kwargs
    ) -> GetCommentsResponseModel:
        """Returns a list of comments on a note.

        :param note_id: Note ID.
        :param owner_id: Note owner ID.
        :param sort:
        :param offset:
        :param count: Number of comments to return.
        """

        params = self.get_set_params(locals())
        response = await self.api.request("notes.getComments", params)
        model = GetCommentsResponse
        return model(**response).response

    async def restore_comment(
        self, comment_id: int, owner_id: typing.Optional[int] = None, **kwargs
    ) -> int:
        """Restores a deleted comment on a note.

        :param comment_id: Comment ID.
        :param owner_id: Note owner ID.
        """

        params = self.get_set_params(locals())
        response = await self.api.request("notes.restoreComment", params)
        model = OkResponse
        return model(**response).response


__all__ = ("NotesCategory",)
