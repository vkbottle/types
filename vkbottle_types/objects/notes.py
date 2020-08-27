from .base_model import BaseObject
from . import base
from typing import Optional, Union, Any, List
import typing
import enum


class Note(BaseObject):
    """VK Object notes/Note

    can_comment - Information whether current user can comment the note
    comments - Comments number
    date - Date when the note has been created in Unixtime
    id - Note ID
    owner_id - Note owner's ID
    text - Note text
    text_wiki - Note text in wiki format
    title - Note title
    view_url - URL of the page with note preview
    """

    read_comments: Optional[int] = None
    can_comment: Optional[base.BoolInt] = None
    comments: Optional[int] = None
    date: Optional[int] = None
    id: Optional[int] = None
    owner_id: Optional[int] = None
    text: Optional[str] = None
    text_wiki: Optional[str] = None
    title: Optional[str] = None
    view_url: Optional[str] = None


class NoteComment(BaseObject):
    """VK Object notes/NoteComment

    date - Date when the comment has beed added in Unixtime
    id - Comment ID
    message - Comment text
    nid - Note ID
    oid - Note ID
    reply_to - ID of replied comment
    uid - Comment author's ID
    """

    date: Optional[int] = None
    id: Optional[int] = None
    message: Optional[str] = None
    nid: Optional[int] = None
    oid: Optional[int] = None
    reply_to: Optional[int] = None
    uid: Optional[int] = None
