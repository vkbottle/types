from typing import Optional

from .base_model import BaseObject


class Audio(BaseObject):
    """VK Object audio/Audio

    artist - Artist name
    id - Audio ID
    title - Title
    url - URL of mp3 file
    duration - Duration in seconds
    date - Date when uploaded
    album_id - Album ID
    genre_id - Genre ID
    performer - Performer name
    """

    artist: Optional[str] = None
    id: Optional[int] = None
    title: Optional[str] = None
    url: Optional[str] = None
    duration: Optional[int] = None
    date: Optional[int] = None
    album_id: Optional[int] = None
    genre_id: Optional[int] = None
    performer: Optional[str] = None
