import enum
from typing import Optional

from . import users, groups, apps, base
from .base_model import BaseObject


class Hint(BaseObject):
    """VK Object search/Hint"""

    app: Optional[apps.App] = None
    description: Optional[str] = None
    _global: Optional[base.BoolInt] = None
    group: Optional[groups.Group] = None
    profile: Optional[users.UserMin] = None
    section: Optional["HintSection"] = None
    type: Optional["HintType"] = None


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
