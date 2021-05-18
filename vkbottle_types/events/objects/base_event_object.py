from typing import Optional

from pydantic import BaseModel

from vkbottle_types.state import StatePeer


class BaseEventObject(BaseModel):
    state_peer: Optional[StatePeer] = None
