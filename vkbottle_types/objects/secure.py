from .base_model import BaseObject
from typing import Optional, Union, Any, List
import typing
import enum


class Level(BaseObject):
    """VK Object secure/Level"""

    level: Optional[int] = None
    uid: Optional[int] = None


class SmsNotification(BaseObject):
    """VK Object secure/SmsNotification"""

    app_id: Optional[str] = None
    date: Optional[str] = None
    id: Optional[str] = None
    message: Optional[str] = None
    user_id: Optional[str] = None


class TokenChecked(BaseObject):
    """VK Object secure/TokenChecked"""

    date: Optional[int] = None
    expire: Optional[int] = None
    success: Optional[int] = None
    user_id: Optional[int] = None


class Transaction(BaseObject):
    """VK Object secure/Transaction"""

    date: Optional[int] = None
    id: Optional[int] = None
    uid_from: Optional[int] = None
    uid_to: Optional[int] = None
    votes: Optional[int] = None
