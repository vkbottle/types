from typing import Optional

from .base_model import BaseObject


class City(BaseObject):
    """VK Object database/City"""


class Faculty(BaseObject):
    """VK Object database/Faculty

    id - Faculty ID
    title - Faculty title
    """

    id: Optional[int] = None
    title: Optional[str] = None


class Region(BaseObject):
    """VK Object database/Region

    id - Region ID
    title - Region title
    """

    id: Optional[int] = None
    title: Optional[str] = None


class School(BaseObject):
    """VK Object database/School

    id - School ID
    title - School title
    """

    id: Optional[int] = None
    title: Optional[str] = None


class Station(BaseObject):
    """VK Object database/Station

    city_id - City ID
    color - Hex color code without #
    id - Station ID
    name - Station name
    """

    city_id: Optional[int] = None
    color: Optional[str] = None
    id: Optional[int] = None
    name: Optional[str] = None


class University(BaseObject):
    """VK Object database/University

    id - University ID
    title - University title
    """

    id: Optional[int] = None
    title: Optional[str] = None
