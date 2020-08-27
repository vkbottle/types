from .base_model import BaseObject
from typing import Optional, Union, Any, List
import typing
import enum


class Value(BaseObject):
    """VK Object storage/Value"""

    key: Optional[str] = None
    value: Optional[str] = None
