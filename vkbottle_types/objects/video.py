from typing import Optional, List

from . import base
from .base_model import BaseObject


class LiveSettings(BaseObject):
    """VK Object video/LiveSettings

    can_rewind - If user car rewind live or not
    is_endless - If live is endless or not
    max_duration - Max possible time for rewind
    """

    can_rewind: Optional[base.BoolInt] = None
    is_endless: Optional[base.BoolInt] = None
    max_duration: Optional[int] = None


class RestrictionButton(BaseObject):
    """VK Object video/RestrictionButton"""

    action: Optional[str] = None
    title: Optional[str] = None


class SaveResult(BaseObject):
    """VK Object video/SaveResult

    access_key - Video access key
    description - Video description
    owner_id - Video owner ID
    title - Video title
    upload_url - URL for the video uploading
    video_id - Video ID
    """

    access_key: Optional[str] = None
    description: Optional[str] = None
    owner_id: Optional[int] = None
    title: Optional[str] = None
    upload_url: Optional[str] = None
    video_id: Optional[int] = None


class Video(BaseObject):
    """VK Object video/Video"""


class VideoAlbumFull(BaseObject):
    """VK Object video/VideoAlbumFull

    count - Total number of videos in album
    id - Album ID
    image - Album cover image in different sizes
    image_blur - Need blur album thumb or not
    is_system - Information whether album is system
    owner_id - Album owner's ID
    title - Album title
    updated_time - Date when the album has been updated last time in Unixtime
    """

    count: Optional[int] = None
    id: Optional[int] = None
    image: Optional[List["VideoImage"]] = None
    image_blur: Optional[base.PropertyExists] = None
    is_system: Optional[base.PropertyExists] = None
    owner_id: Optional[int] = None
    title: Optional[str] = None
    updated_time: Optional[int] = None


class VideoFiles(BaseObject):
    """VK Object video/VideoFiles

    external - URL of the external player
    mp4_240 - URL of the mpeg4 file with 240p quality
    mp4_360 - URL of the mpeg4 file with 360p quality
    mp4_480 - URL of the mpeg4 file with 480p quality
    mp4_720 - URL of the mpeg4 file with 720p quality
    mp4_1080 - URL of the mpeg4 file with 1080p quality
    flv_320 - URL of the flv file with 320p quality
    """

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
