from pydantic import BaseModel
from typing import Optional
from vkbottle_types.state import StatePeer


class BaseEventObject(BaseModel):
    state: Optional[StatePeer] = None

