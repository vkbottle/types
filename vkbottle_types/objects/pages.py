from .base_model import BaseObject
from . import base
from typing import Optional, Union, Any, List
import typing
import enum


class PrivacySettings(enum.IntEnum):
    """ PrivacySettings enum """

    community_managers_only = 0
    community_members_only = 1
    everyone = 2


class Wikipage(BaseObject):
    """VK Object pages/Wikipage"""

    creator_id: Optional[int] = None
    creator_name: Optional[int] = None
    editor_id: Optional[int] = None
    editor_name: Optional[str] = None
    group_id: Optional[int] = None
    id: Optional[int] = None
    title: Optional[str] = None
    views: Optional[int] = None
    who_can_edit: Optional["PrivacySettings"]
    who_can_view: Optional["PrivacySettings"]


class WikipageFull(BaseObject):
    """VK Object pages/WikipageFull"""

    created: Optional[int] = None
    creator_id: Optional[int] = None
    current_user_can_edit: Optional[base.BoolInt] = None
    current_user_can_edit_access: Optional[base.BoolInt] = None
    edited: Optional[int] = None
    editor_id: Optional[int] = None
    group_id: Optional[int] = None
    html: Optional[str] = None
    id: Optional[int] = None
    source: Optional[str] = None
    title: Optional[str] = None
    view_url: Optional[str] = None
    views: Optional[int] = None
    who_can_edit: Optional["PrivacySettings"]
    who_can_view: Optional["PrivacySettings"]


class WikipageHistory(BaseObject):
    """VK Object pages/WikipageHistory"""

    id: Optional[int] = None
    length: Optional[int] = None
    date: Optional[int] = None
    editor_id: Optional[int] = None
    editor_name: Optional[str] = None
