from .base_model import BaseObject
from . import base
from typing import Optional, Union, Any, List
import typing
import enum


class Note(BaseObject):
    """VK Object notes/Note"""

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
    """VK Object notes/NoteComment"""

    date: Optional[int] = None
    id: Optional[int] = None
    message: Optional[str] = None
    nid: Optional[int] = None
    oid: Optional[int] = None
    reply_to: Optional[int] = None
    uid: Optional[int] = None
