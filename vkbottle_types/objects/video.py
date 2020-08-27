from .base_model import BaseObject
from . import base
from typing import Optional, Union, Any, List
import typing
import enum


class LiveSettings(BaseObject):
    """VK Object video/LiveSettings"""

    can_rewind: Optional[base.BoolInt] = None
    is_endless: Optional[base.BoolInt] = None
    max_duration: Optional[int] = None


class RestrictionButton(BaseObject):
    """VK Object video/RestrictionButton"""

    action: Optional[str] = None
    title: Optional[str] = None


class SaveResult(BaseObject):
    """VK Object video/SaveResult"""

    access_key: Optional[str] = None
    description: Optional[str] = None
    owner_id: Optional[int] = None
    title: Optional[str] = None
    upload_url: Optional[str] = None
    video_id: Optional[int] = None


class Video(BaseObject):
    """VK Object video/Video"""


class VideoAlbumFull(BaseObject):
    """VK Object video/VideoAlbumFull"""

    count: Optional[int] = None
    id: Optional[int] = None
    image: Optional[List["VideoImage"]]
    image_blur: Optional[base.PropertyExists] = None
    is_system: Optional[base.PropertyExists] = None
    owner_id: Optional[int] = None
    title: Optional[str] = None
    updated_time: Optional[int] = None


class VideoFiles(BaseObject):
    """VK Object video/VideoFiles"""

    external: Optional[str] = None
    mp4_240: Optional[str] = None
    mp4_360: Optional[str] = None
    mp4_480: Optional[str] = None
    mp4_720: Optional[str] = None
    mp4_1080: Optional[str] = None
    flv_320: Optional[str] = None


class VideoFull(BaseObject):
    """VK Object video/VideoFull"""


class VideoImage(BaseObject):
    """VK Object video/VideoImage"""
