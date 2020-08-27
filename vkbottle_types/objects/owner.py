from .base_model import BaseObject
from typing import Optional, Union, Any, List
import typing
import enum


class State(BaseObject):
    """VK Object owner/State"""

    state: Optional[int] = None
    description: Optional[str] = None
