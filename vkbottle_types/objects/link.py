from typing import Optional

from .base_model import BaseObject


class TargetObject(BaseObject):
    """VK Object link/TargetObject

    type - Object type
    owner_id - Owner ID
    item_id - Item ID
    """

    type: Optional[str] = None
    owner_id: Optional[int] = None
    item_id: Optional[int] = None
