from .base_model import BaseObject
from . import audio
from typing import Optional, Union, Any, List
import typing
import enum


class Status(BaseObject):
    """VK Object status/Status"""

    text: Optional[str] = None
    audio: Optional[audio.Audio] = None
