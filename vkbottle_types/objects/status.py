from typing import Optional

from . import audio
from .base_model import BaseObject


class Status(BaseObject):
    """VK Object status/Status

    text - Status text
    """

    text: Optional[str] = None
    audio: Optional[audio.Audio] = None
