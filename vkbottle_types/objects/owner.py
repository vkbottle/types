from typing import Optional

from .base_model import BaseObject


class State(BaseObject):
    """VK Object owner/State

    description - wiki text to describe user state
    """

    state: Optional[int] = None
    description: Optional[str] = None
