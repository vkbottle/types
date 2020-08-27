from .base_model import BaseObject
from typing import Optional, Union, Any, List
import typing
import enum


class Audio(BaseObject):
    """VK Object audio/Audio"""

    artist: Optional[str] = None
    id: Optional[int] = None
    title: Optional[str] = None
    url: Optional[str] = None
    duration: Optional[int] = None
    date: Optional[int] = None
    album_id: Optional[int] = None
    genre_id: Optional[int] = None
    performer: Optional[str] = None
