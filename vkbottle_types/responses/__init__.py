from vkbottle_types.tools import ModelLoader
from typing import TYPE_CHECKING

if TYPE_CHECKING:
    from .account import *
    from .ads import *
    from .app_widgets import *
    from .apps import *
    from .auth import *
    from .base import *
    from .base_response import *
    from .board import *
    from .bugtracker import *
    from .calls import *
    from .database import *
    from .docs import *
    from .donut import *
    from .downloaded_games import *
    from .fave import *
    from .friends import *
    from .gifts import *
    from .groups import *
    from .lead_forms import *
    from .likes import *
    from .market import *
    from .messages import *
    from .newsfeed import *
    from .notes import *
    from .notifications import *
    from .orders import *
    from .pages import *
    from .photos import *
    from .podcasts import *
    from .polls import *
    from .pretty_cards import *
    from .search import *
    from .secure import *
    from .stats import *
    from .status import *
    from .storage import *
    from .store import *
    from .stories import *
    from .streaming import *
    from .translations import *
    from .users import *
    from .utils import *
    from .video import *
    from .wall import *
    from .widgets import *


_MODULES = [
    "account",
    "ads",
    "app_widgets",
    "apps",
    "auth",
    "base",
    "base_response",
    "board",
    "bugtracker",
    "calls",
    "database",
    "docs",
    "donut",
    "downloaded_games",
    "fave",
    "friends",
    "gifts",
    "groups",
    "lead_forms",
    "likes",
    "market",
    "messages",
    "newsfeed",
    "notes",
    "notifications",
    "orders",
    "pages",
    "photos",
    "podcasts",
    "polls",
    "pretty_cards",
    "search",
    "secure",
    "stats",
    "status",
    "storage",
    "store",
    "stories",
    "streaming",
    "translations",
    "users",
    "utils",
    "video",
    "wall",
    "widgets",
]


loader = ModelLoader(
    base_package=__name__,
    module_names=_MODULES
)


def __getattr__(name: str):
    return loader.load(name)
