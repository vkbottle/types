from .base_model import BaseObject
from typing import Optional, Union, Any, List
import typing
import enum


class City(BaseObject):
    """VK Object database/City"""


class Faculty(BaseObject):
    """VK Object database/Faculty"""

    id: Optional[int] = None
    title: Optional[str] = None


class Region(BaseObject):
    """VK Object database/Region"""

    id: Optional[int] = None
    title: Optional[str] = None


class School(BaseObject):
    """VK Object database/School"""

    id: Optional[int] = None
    title: Optional[str] = None


class Station(BaseObject):
    """VK Object database/Station"""

    city_id: Optional[int] = None
    color: Optional[str] = None
    id: Optional[int] = None
    name: Optional[str] = None


class University(BaseObject):
    """VK Object database/University"""

    id: Optional[int] = None
    title: Optional[str] = None
