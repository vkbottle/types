from typing import Optional, List

from vkbottle_types.responses import notes, base
from .base_category import BaseCategory


class NotesCategory(BaseCategory):
    async def add(
        self,
        title: str,
        text: str,
        privacy_view: Optional[List[str]] = None,
        privacy_comment: Optional[List[str]] = None,
        **kwargs
    ) -> notes.AddResponseModel:
        """Creates a new note for the current user.
        :param title: Note title.
        :param text: Note text.
        :param privacy_view:
        :param privacy_comment:
        """

        params = self.get_set_params(locals())
        return notes.AddResponse(**await self.api.request("notes.add", params))

    async def create_comment(
        self,
        note_id: int,
        message: str,
        owner_id: Optional[int] = None,
        reply_to: Optional[int] = None,
        guid: Optional[str] = None,
        **kwargs
    ) -> notes.CreateCommentResponseModel:
        """Adds a new comment on a note.
        :param note_id: Note ID.
        :param message: Comment text.
        :param owner_id: Note owner ID.
        :param reply_to: ID of the user to whom the reply is addressed (if the comment is a reply to another comment).
        :param guid:
        """

        params = self.get_set_params(locals())
        return notes.CreateCommentResponse(
            **await self.api.request("notes.createComment", params)
        )

    async def delete(self, note_id: int, **kwargs) -> base.OkResponseModel:
        """Deletes a note of the current user.
        :param note_id: Note ID.
        """

        params = self.get_set_params(locals())
        return base.OkResponse(**await self.api.request("notes.delete", params))

    async def delete_comment(
        self, comment_id: int, owner_id: Optional[int] = None, **kwargs
    ) -> base.OkResponseModel:
        """Deletes a comment on a note.
        :param comment_id: Comment ID.
        :param owner_id: Note owner ID.
        """

        params = self.get_set_params(locals())
        return base.OkResponse(**await self.api.request("notes.deleteComment", params))

    async def edit(
        self,
        note_id: int,
        title: str,
        text: str,
        privacy_view: Optional[List[str]] = None,
        privacy_comment: Optional[List[str]] = None,
        **kwargs
    ) -> base.OkResponseModel:
        """Edits a note of the current user.
        :param note_id: Note ID.
        :param title: Note title.
        :param text: Note text.
        :param privacy_view:
        :param privacy_comment:
        """

        params = self.get_set_params(locals())
        return base.OkResponse(**await self.api.request("notes.edit", params))

    async def edit_comment(
        self, comment_id: int, message: str, owner_id: Optional[int] = None, **kwargs
    ) -> base.OkResponseModel:
        """Edits a comment on a note.
        :param comment_id: Comment ID.
        :param message: New comment text.
        :param owner_id: Note owner ID.
        """

        params = self.get_set_params(locals())
        return base.OkResponse(**await self.api.request("notes.editComment", params))

    async def get(
        self,
        note_ids: Optional[List[int]] = None,
        user_id: Optional[int] = None,
        offset: Optional[int] = None,
        count: Optional[int] = None,
        sort: Optional[int] = None,
        **kwargs
    ) -> notes.GetResponseModel:
        """Returns a list of notes created by a user.
        :param note_ids: Note IDs.
        :param user_id: Note owner ID.
        :param offset:
        :param count: Number of notes to return.
        :param sort:
        """

        params = self.get_set_params(locals())
        return notes.GetResponse(**await self.api.request("notes.get", params))

    async def get_by_id(
        self,
        note_id: int,
        owner_id: Optional[int] = None,
        need_wiki: Optional[bool] = None,
        **kwargs
    ) -> notes.GetByIdResponseModel:
        """Returns a note by its ID.
        :param note_id: Note ID.
        :param owner_id: Note owner ID.
        :param need_wiki:
        """

        params = self.get_set_params(locals())
        return notes.GetByIdResponse(**await self.api.request("notes.getById", params))

    async def get_comments(
        self,
        note_id: int,
        owner_id: Optional[int] = None,
        sort: Optional[int] = None,
        offset: Optional[int] = None,
        count: Optional[int] = None,
        **kwargs
    ) -> notes.GetCommentsResponseModel:
        """Returns a list of comments on a note.
        :param note_id: Note ID.
        :param owner_id: Note owner ID.
        :param sort:
        :param offset:
        :param count: Number of comments to return.
        """

        params = self.get_set_params(locals())
        return notes.GetCommentsResponse(
            **await self.api.request("notes.getComments", params)
        )

    async def restore_comment(
        self, comment_id: int, owner_id: Optional[int] = None, **kwargs
    ) -> base.OkResponseModel:
        """Restores a deleted comment on a note.
        :param comment_id: Comment ID.
        :param owner_id: Note owner ID.
        """

        params = self.get_set_params(locals())
        return base.OkResponse(**await self.api.request("notes.restoreComment", params))
