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

localns = locals().copy()
for item in localns.values():
    if not (isinstance(item, type) and item is not BaseModel and issubclass(item, BaseModel)):
        continue

    item.model_rebuild(force=True, _types_namespace=localns)

    for parent in item.__bases__:
        if parent.__name__ == item.__name__ and issubclass(parent, BaseModel):
            parent.__pydantic_fields__.update(item.__pydantic_fields__)
            parent.model_rebuild(force=True, _types_namespace=localns)
            item.__pydantic_fields__.update(
                {name: field for name, field in parent.__pydantic_fields__.items() if name not in item.__pydantic_fields__},
            )
