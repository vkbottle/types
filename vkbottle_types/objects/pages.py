import enum
from typing import Optional

from . import base
from .base_model import BaseObject


class PrivacySettings(enum.IntEnum):
    """ PrivacySettings enum """

    community_managers_only = 0
    community_members_only = 1
    everyone = 2


class Wikipage(BaseObject):
    """VK Object pages/Wikipage

    creator_id - Page creator ID
    creator_name - Page creator name
    editor_id - Last editor ID
    editor_name - Last editor name
    group_id - Community ID
    id - Page ID
    title - Page title
    views - Views number
    who_can_edit - Edit settings of the page
    who_can_view - View settings of the page
    """

    creator_id: Optional[int] = None
    creator_name: Optional[int] = None
    editor_id: Optional[int] = None
    editor_name: Optional[str] = None
    group_id: Optional[int] = None
    id: Optional[int] = None
    title: Optional[str] = None
    views: Optional[int] = None
    who_can_edit: Optional["PrivacySettings"] = None
    who_can_view: Optional["PrivacySettings"] = None


class WikipageFull(BaseObject):
    """VK Object pages/WikipageFull

    created - Date when the page has been created in Unixtime
    creator_id - Page creator ID
    current_user_can_edit - Information whether current user can edit the page
    current_user_can_edit_access - Information whether current user can edit the page access settings
    edited - Date when the page has been edited in Unixtime
    editor_id - Last editor ID
    group_id - Community ID
    html - Page content, HTML
    id - Page ID
    source - Page content, wiki
    title - Page title
    view_url - URL of the page preview
    views - Views number
    who_can_edit - Edit settings of the page
    who_can_view - View settings of the page
    """

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
    who_can_edit: Optional["PrivacySettings"] = None
    who_can_view: Optional["PrivacySettings"] = None


class WikipageHistory(BaseObject):
    """VK Object pages/WikipageHistory

    id - Version ID
    length - Page size in bytes
    date - Date when the page has been edited in Unixtime
    editor_id - Last editor ID
    editor_name - Last editor name
    """

    id: Optional[int] = None
    length: Optional[int] = None
    date: Optional[int] = None
    editor_id: Optional[int] = None
    editor_name: Optional[str] = None
