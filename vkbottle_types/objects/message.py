from .base_model import BaseObject
from typing import Optional, Union, Any, List
import typing
import enum


class ChatPreview(BaseObject):
    """VK Object message/ChatPreview"""

    admin_id: Optional[int] = None
    joined: Optional[bool] = None
    local_id: Optional[int] = None
    members: Optional[List[int]] = None
    members_count: Optional[int] = None
    title: Optional[str] = None
