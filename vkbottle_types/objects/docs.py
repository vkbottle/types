from .base_model import BaseObject
from . import base, photos
from typing import Optional, Union, Any, List
import typing
import enum


class Doc(BaseObject):
    """VK Object docs/Doc"""

    id: Optional[int] = None
    owner_id: Optional[int] = None
    title: Optional[str] = None
    size: Optional[int] = None
    ext: Optional[str] = None
    url: Optional[str] = None
    date: Optional[int] = None
    type: Optional[int] = None
    preview: Optional["DocPreview"]
    is_licensed: Optional[base.BoolInt] = None
    access_key: Optional[str] = None
    tags: Optional[List[str]] = None


class DocAttachmentType(enum.Enum):
    """ Doc attachment type """

    DOC = "doc"
    GRAFFITI = "graffiti"
    AUDIO_MESSAGE = "audio_message"


class DocPreview(BaseObject):
    """VK Object docs/DocPreview"""

    audio_msg: Optional["DocPreviewAudioMsg"]
    graffiti: Optional["DocPreviewGraffiti"]
    photo: Optional["DocPreviewPhoto"]
    video: Optional["DocPreviewVideo"]


class DocPreviewAudioMsg(BaseObject):
    """VK Object docs/DocPreviewAudioMsg"""

    duration: Optional[int] = None
    link_mp3: Optional[str] = None
    link_ogg: Optional[str] = None
    waveform: Optional[List[int]] = None


class DocPreviewGraffiti(BaseObject):
    """VK Object docs/DocPreviewGraffiti"""

    src: Optional[str] = None
    width: Optional[int] = None
    height: Optional[int] = None


class DocPreviewPhoto(BaseObject):
    """VK Object docs/DocPreviewPhoto"""

    sizes: Optional[List["DocPreviewPhotoSizes"]]


class DocPreviewPhotoSizes(BaseObject):
    """VK Object docs/DocPreviewPhotoSizes"""

    src: Optional[str] = None
    width: Optional[int] = None
    height: Optional[int] = None
    type: Optional[photos.PhotoSizesType] = None


class DocPreviewVideo(BaseObject):
    """VK Object docs/DocPreviewVideo"""

    src: Optional[str] = None
    width: Optional[int] = None
    height: Optional[int] = None
    file_size: Optional[int] = None


class DocTypes(BaseObject):
    """VK Object docs/DocTypes"""

    id: Optional[int] = None
    name: Optional[str] = None
    count: Optional[int] = None


class DocUploadResponse(BaseObject):
    """VK Object docs/DocUploadResponse"""

    file: Optional[str] = None
