from .base_model import BaseObject
from . import base, groups, users, apps
from typing import Optional, Union, Any, List
import typing
import enum


class Hint(BaseObject):
    """VK Object search/Hint"""

    app: Optional[apps.App] = None
    description: Optional[str] = None
    _global: Optional[base.BoolInt] = None
    group: Optional[groups.Group] = None
    profile: Optional[users.UserMin] = None
    section: Optional["HintSection"]
    type: Optional["HintType"]


class HintSection(enum.Enum):
    """ Section title """

    GROUPS = "groups"
    EVENTS = "events"
    PUBLICS = "publics"
    CORRESPONDENTS = "correspondents"
    PEOPLE = "people"
    FRIENDS = "friends"
    MUTUAL_FRIENDS = "mutual_friends"


class HintType(enum.Enum):
    """ Object type """

    GROUP = "group"
    PROFILE = "profile"
    VK_APP = "vk_app"
    APP = "app"
    HTML5_GAME = "html5_game"
