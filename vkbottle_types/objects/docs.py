import enum
from typing import Optional, List

from . import photos, base
from .base_model import BaseObject


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
    preview: Optional["DocPreview"] = None
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

    audio_msg: Optional["DocPreviewAudioMsg"] = None
    graffiti: Optional["DocPreviewGraffiti"] = None
    photo: Optional["DocPreviewPhoto"] = None
    video: Optional["DocPreviewVideo"] = None


class DocPreviewAudioMsg(BaseObject):
    """VK Object docs/DocPreviewAudioMsg

    duration - Audio message duration in seconds
    link_mp3 - MP3 file URL
    link_ogg - OGG file URL
    """

    duration: Optional[int] = None
    link_mp3: Optional[str] = None
    link_ogg: Optional[str] = None
    waveform: Optional[List[int]] = None


class DocPreviewGraffiti(BaseObject):
    """VK Object docs/DocPreviewGraffiti

    src - Graffiti file URL
    width - Graffiti width
    height - Graffiti height
    """

    src: Optional[str] = None
    width: Optional[int] = None
    height: Optional[int] = None


class DocPreviewPhoto(BaseObject):
    """VK Object docs/DocPreviewPhoto"""

    sizes: Optional[List["DocPreviewPhotoSizes"]] = None


class DocPreviewPhotoSizes(BaseObject):
    """VK Object docs/DocPreviewPhotoSizes

    src - URL of the image
    width - Width in px
    height - Height in px
    """

    src: Optional[str] = None
    width: Optional[int] = None
    height: Optional[int] = None
    type: Optional[photos.PhotoSizesType] = None


class DocPreviewVideo(BaseObject):
    """VK Object docs/DocPreviewVideo

    src - Video URL
    width - Video's width in pixels
    height - Video's height in pixels
    file_size - Video file size in bites
    """

    src: Optional[str] = None
    width: Optional[int] = None
    height: Optional[int] = None
    file_size: Optional[int] = None


class DocTypes(BaseObject):
    """VK Object docs/DocTypes

    id - Doc type ID
    name - Doc type title
    count - Number of docs
    """

    id: Optional[int] = None
    name: Optional[str] = None
    count: Optional[int] = None


class DocUploadResponse(BaseObject):
    """VK Object docs/DocUploadResponse

    file - Uploaded file data
    """

    file: Optional[str] = None
