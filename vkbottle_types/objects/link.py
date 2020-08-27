from .base_model import BaseObject
from typing import Optional, Union, Any, List
import typing
import enum


class TargetObject(BaseObject):
    """VK Object link/TargetObject"""

    type: Optional[str] = None
    owner_id: Optional[int] = None
    item_id: Optional[int] = None
