from .base_model import BaseObject
from typing import Optional, Union, Any, List
import typing
import enum


class State(BaseObject):
    """VK Object owner/State

    description - wiki text to describe user state
    """

    state: Optional[int] = None
    description: Optional[str] = None
