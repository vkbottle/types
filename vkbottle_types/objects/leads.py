from .base_model import BaseObject
from . import base
from typing import Optional, Union, Any, List
import typing
import enum


class Checked(BaseObject):
    """VK Object leads/Checked"""

    reason: Optional[str] = None
    result: Optional["CheckedResult"] = None
    sid: Optional[str] = None
    start_link: Optional[str] = None


class CheckedResult(enum.Enum):
    """ Information whether user can start the lead """

    TRUE = "true"
    FALSE = "false"


class Complete(BaseObject):
    """VK Object leads/Complete

    cost - Offer cost
    limit - Offer limit
    spent - Amount of spent votes
    test_mode - Information whether test mode is enabled
    """

    cost: Optional[int] = None
    limit: Optional[int] = None
    spent: Optional[int] = None
    success: Optional[int] = None
    test_mode: Optional[base.BoolInt] = None


class Entry(BaseObject):
    """VK Object leads/Entry

    aid - Application ID
    comment - Comment text
    date - Date when the action has been started in Unixtime
    sid - Session string ID
    start_date - Start date in Unixtime (for status=2)
    status - Action type
    test_mode - Information whether test mode is enabled
    uid - User ID
    """

    aid: Optional[int] = None
    comment: Optional[str] = None
    date: Optional[int] = None
    sid: Optional[str] = None
    start_date: Optional[int] = None
    status: Optional[int] = None
    test_mode: Optional[base.BoolInt] = None
    uid: Optional[int] = None


class Lead(BaseObject):
    """VK Object leads/Lead

    completed - Completed offers number
    cost - Offer cost
    impressions - Impressions number
    limit - Lead limit
    spent - Amount of spent votes
    started - Started offers number
    """

    completed: Optional[int] = None
    cost: Optional[int] = None
    days: Optional["LeadDays"] = None
    impressions: Optional[int] = None
    limit: Optional[int] = None
    spent: Optional[int] = None
    started: Optional[int] = None


class LeadDays(BaseObject):
    """VK Object leads/LeadDays

    completed - Completed offers number
    impressions - Impressions number
    spent - Amount of spent votes
    started - Started offers number
    """

    completed: Optional[int] = None
    impressions: Optional[int] = None
    spent: Optional[int] = None
    started: Optional[int] = None


class Start(BaseObject):
    """VK Object leads/Start

    test_mode - Information whether test mode is enabled
    vk_sid - Session data
    """

    test_mode: Optional[base.BoolInt] = None
    vk_sid: Optional[str] = None
