from typing import Optional

from .base_model import BaseObject


class Value(BaseObject):
    """VK Object storage/Value"""

    key: Optional[str] = None
    value: Optional[str] = None
