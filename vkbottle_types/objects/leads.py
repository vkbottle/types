from .base_model import BaseObject
from . import base
from typing import Optional, Union, Any, List
import typing
import enum


class Checked(BaseObject):
    """VK Object leads/Checked"""

    reason: Optional[str] = None
    result: Optional["CheckedResult"]
    sid: Optional[str] = None
    start_link: Optional[str] = None


class CheckedResult(enum.Enum):
    """ Information whether user can start the lead """

    TRUE = "true"
    FALSE = "false"


class Complete(BaseObject):
    """VK Object leads/Complete"""

    cost: Optional[int] = None
    limit: Optional[int] = None
    spent: Optional[int] = None
    success: Optional[int] = None
    test_mode: Optional[base.BoolInt] = None


class Entry(BaseObject):
    """VK Object leads/Entry"""

    aid: Optional[int] = None
    comment: Optional[str] = None
    date: Optional[int] = None
    sid: Optional[str] = None
    start_date: Optional[int] = None
    status: Optional[int] = None
    test_mode: Optional[base.BoolInt] = None
    uid: Optional[int] = None


class Lead(BaseObject):
    """VK Object leads/Lead"""

    completed: Optional[int] = None
    cost: Optional[int] = None
    days: Optional["LeadDays"]
    impressions: Optional[int] = None
    limit: Optional[int] = None
    spent: Optional[int] = None
    started: Optional[int] = None


class LeadDays(BaseObject):
    """VK Object leads/LeadDays"""

    completed: Optional[int] = None
    impressions: Optional[int] = None
    spent: Optional[int] = None
    started: Optional[int] = None


class Start(BaseObject):
    """VK Object leads/Start"""

    test_mode: Optional[base.BoolInt] = None
    vk_sid: Optional[str] = None
