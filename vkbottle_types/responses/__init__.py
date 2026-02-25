import importlib
import sys

from typing import TYPE_CHECKING
from pydantic import BaseModel

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


_loaded: dict[str, object] = {}
_rebuilt: set[type] = set()


def _build_namespace_for(model: type) -> dict:
    ns = {}

    module = sys.modules.get(model.__module__)
    if module:
        ns.update(vars(module))

    for m in _loaded.values():
        ns.update(vars(m))

    return ns


def _merge_with_same_named_parent(model: type[BaseModel], namespace: dict):
    for parent in model.__bases__:
        if (
            parent.__name__ == model.__name__
            and issubclass(parent, BaseModel)
        ):
            parent.__pydantic_fields__.update(model.__pydantic_fields__)
            parent.model_rebuild(force=True, _types_namespace=namespace)

            missing = {
                name: field
                for name, field in parent.__pydantic_fields__.items()
                if name not in model.__pydantic_fields__
            }
            if missing:
                model.__pydantic_fields__.update(missing)


def _rebuild_model(model: type[BaseModel]):
    if model in _rebuilt:
        return model

    namespace = _build_namespace_for(model)

    model.model_rebuild(force=True, _types_namespace=namespace)
    _merge_with_same_named_parent(model, namespace)

    _rebuilt.add(model)
    return model


def __getattr__(name: str):
    for module_name in _MODULES:
        if module_name not in _loaded:
            module = importlib.import_module(f"{__name__}.{module_name}")
            _loaded[module_name] = module

        module = _loaded[module_name]

        if hasattr(module, name):
            value = getattr(module, name)

            if (
                isinstance(value, type)
                and issubclass(value, BaseModel)
                and value is not BaseModel
            ):
                _rebuild_model(value)

            print('item', value)
            return value

    raise AttributeError(f"module {__name__} has no attribute {name}")






# ==================================================================================================================== #


# from .account import *
# from .ads import *
# from .app_widgets import *
# from .apps import *
# from .auth import *
# from .base import *
# from .base_response import *
# from .board import *
# from .bugtracker import *
# from .calls import *
# from .database import *
# from .docs import *
# from .donut import *
# from .downloaded_games import *
# from .fave import *
# from .friends import *
# from .gifts import *
# from .groups import *
# from .lead_forms import *
# from .likes import *
# from .market import *
# from .messages import *
# from .newsfeed import *
# from .notes import *
# from .notifications import *
# from .orders import *
# from .pages import *
# from .photos import *
# from .podcasts import *
# from .polls import *
# from .pretty_cards import *
# from .search import *
# from .secure import *
# from .stats import *
# from .status import *
# from .storage import *
# from .store import *
# from .stories import *
# from .streaming import *
# from .translations import *
# from .users import *
# from .utils import *
# from .video import *
# from .wall import *
# from .widgets import *

# localns = locals().copy()
# for item in localns.values():
#     if not (isinstance(item, type) and item is not BaseModel and issubclass(item, BaseModel)):
#         continue

#     item.model_rebuild(force=True, _types_namespace=localns)

#     for parent in item.__bases__:
#         if parent.__name__ == item.__name__ and issubclass(parent, BaseModel):
#             parent.__pydantic_fields__.update(item.__pydantic_fields__)
#             parent.model_rebuild(force=True, _types_namespace=localns)
#             item.__pydantic_fields__.update(
#                 {name: field for name, field in parent.__pydantic_fields__.items() if name not in item.__pydantic_fields__},
#             )
