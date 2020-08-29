import enum
from typing import Optional

from .base_model import BaseObject


class App(BaseObject):
    """VK Object apps/App"""


class AppLeaderboardType(enum.IntEnum):
    """ Leaderboard type """

    not_supported = 0
    levels = 1
    points = 2


class AppMin(BaseObject):
    """VK Object apps/AppMin"""

    type: Optional["AppType"] = None
    id: Optional[int] = None
    title: Optional[str] = None
    author_owner_id: Optional[int] = None
    is_installed: Optional[bool] = None
    icon_139: Optional[str] = None
    icon_150: Optional[str] = None
    icon_278: Optional[str] = None
    icon_576: Optional[str] = None
    background_loader_color: Optional[str] = None
    loader_icon: Optional[str] = None
    icon_75: Optional[str] = None


class AppType(enum.Enum):
    """ Application type """

    APP = "app"
    GAME = "game"
    SITE = "site"
    STANDALONE = "standalone"
    VK_APP = "vk_app"
    COMMUNITY_APP = "community_app"
    HTML5_GAME = "html5_game"
    MINI_APP = "mini_app"


class Leaderboard(BaseObject):
    """VK Object apps/Leaderboard

    level - Level
    points - Points number
    score - Score number
    user_id - User ID
    """

    level: Optional[int] = None
    points: Optional[int] = None
    score: Optional[int] = None
    user_id: Optional[int] = None


class Scope(BaseObject):
    """VK Object apps/Scope

    name - Scope name
    title - Scope title
    """

    name: Optional[str] = None
    title: Optional[str] = None
