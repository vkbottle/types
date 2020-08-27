from .base_model import BaseObject
from . import media, base, comment, wall
from typing import Optional, Union, Any, List
import typing
import enum


class CommentXtrPid(BaseObject):
    """VK Object photos/CommentXtrPid"""

    attachments: Optional[List[wall.CommentAttachment]] = None
    date: Optional[int] = None
    from_id: Optional[int] = None
    id: Optional[int] = None
    likes: Optional[base.LikesInfo] = None
    pid: Optional[int] = None
    reply_to_comment: Optional[int] = None
    reply_to_user: Optional[int] = None
    text: Optional[str] = None
    parents_stack: Optional[List[int]] = None
    thread: Optional[comment.Thread] = None


class Image(BaseObject):
    """VK Object photos/Image"""

    height: Optional[int] = None
    type: Optional["ImageType"]
    url: Optional[str] = None
    width: Optional[int] = None


class ImageType(enum.Enum):
    """ Photo's type. """

    S = "s"
    M = "m"
    X = "x"
    L = "l"
    O = "o"
    P = "p"
    Q = "q"
    R = "r"
    Y = "y"
    Z = "z"
    W = "w"


class MarketAlbumUploadResponse(BaseObject):
    """VK Object photos/MarketAlbumUploadResponse"""

    gid: Optional[int] = None
    hash: Optional[str] = None
    photo: Optional[str] = None
    server: Optional[int] = None


class MarketUploadResponse(BaseObject):
    """VK Object photos/MarketUploadResponse"""

    crop_data: Optional[str] = None
    crop_hash: Optional[str] = None
    group_id: Optional[int] = None
    hash: Optional[str] = None
    photo: Optional[str] = None
    server: Optional[int] = None


class MessageUploadResponse(BaseObject):
    """VK Object photos/MessageUploadResponse"""

    hash: Optional[str] = None
    photo: Optional[str] = None
    server: Optional[int] = None


class OwnerUploadResponse(BaseObject):
    """VK Object photos/OwnerUploadResponse"""

    hash: Optional[str] = None
    photo: Optional[str] = None
    server: Optional[int] = None


class Photo(BaseObject):
    """VK Object photos/Photo"""

    access_key: Optional[str] = None
    album_id: Optional[int] = None
    date: Optional[int] = None
    height: Optional[int] = None
    id: Optional[int] = None
    images: Optional[List["Image"]]
    lat: Optional[float] = None
    long: Optional[float] = None
    owner_id: Optional[int] = None
    photo_256: Optional[str] = None
    can_comment: Optional[base.BoolInt] = None
    place: Optional[str] = None
    post_id: Optional[int] = None
    sizes: Optional[List["PhotoSizes"]]
    text: Optional[str] = None
    user_id: Optional[int] = None
    width: Optional[int] = None
    has_tags: Optional[bool] = None
    restrictions: Optional[media.Restriction] = None


class PhotoAlbum(BaseObject):
    """VK Object photos/PhotoAlbum"""

    created: Optional[int] = None
    description: Optional[str] = None
    id: Optional[int] = None
    owner_id: Optional[int] = None
    size: Optional[int] = None
    thumb: Optional["Photo"]
    title: Optional[str] = None
    updated: Optional[int] = None


class PhotoAlbumFull(BaseObject):
    """VK Object photos/PhotoAlbumFull"""

    can_upload: Optional[base.BoolInt] = None
    comments_disabled: Optional[base.BoolInt] = None
    created: Optional[int] = None
    description: Optional[str] = None
    id: Optional[int] = None
    owner_id: Optional[int] = None
    size: Optional[int] = None
    sizes: Optional[List["PhotoSizes"]]
    thumb_id: Optional[int] = None
    thumb_is_last: Optional[base.BoolInt] = None
    thumb_src: Optional[str] = None
    title: Optional[str] = None
    updated: Optional[int] = None
    upload_by_admins_only: Optional[base.BoolInt] = None


class PhotoFull(BaseObject):
    """VK Object photos/PhotoFull"""

    access_key: Optional[str] = None
    album_id: Optional[int] = None
    can_comment: Optional[base.BoolInt] = None
    comments: Optional[base.ObjectCount] = None
    date: Optional[int] = None
    height: Optional[int] = None
    id: Optional[int] = None
    images: Optional[List["Image"]]
    lat: Optional[float] = None
    likes: Optional[base.Likes] = None
    long: Optional[float] = None
    owner_id: Optional[int] = None
    post_id: Optional[int] = None
    reposts: Optional[base.ObjectCount] = None
    tags: Optional[base.ObjectCount] = None
    text: Optional[str] = None
    user_id: Optional[int] = None
    width: Optional[int] = None


class PhotoFullXtrRealOffset(BaseObject):
    """VK Object photos/PhotoFullXtrRealOffset"""

    access_key: Optional[str] = None
    album_id: Optional[int] = None
    can_comment: Optional[base.BoolInt] = None
    comments: Optional[base.ObjectCount] = None
    date: Optional[int] = None
    height: Optional[int] = None
    hidden: Optional[base.PropertyExists] = None
    id: Optional[int] = None
    lat: Optional[float] = None
    likes: Optional[base.Likes] = None
    long: Optional[float] = None
    owner_id: Optional[int] = None
    photo_1280: Optional[str] = None
    photo_130: Optional[str] = None
    photo_2560: Optional[str] = None
    photo_604: Optional[str] = None
    photo_75: Optional[str] = None
    photo_807: Optional[str] = None
    post_id: Optional[int] = None
    real_offset: Optional[int] = None
    reposts: Optional[base.ObjectCount] = None
    sizes: Optional[List["PhotoSizes"]]
    tags: Optional[base.ObjectCount] = None
    text: Optional[str] = None
    user_id: Optional[int] = None
    width: Optional[int] = None


class PhotoSizes(BaseObject):
    """VK Object photos/PhotoSizes"""

    height: Optional[int] = None
    url: Optional[str] = None
    src: Optional[str] = None
    type: Optional["PhotoSizesType"]
    width: Optional[int] = None


class PhotoSizesType(enum.Enum):
    """ Size type """

    S = "s"
    M = "m"
    X = "x"
    O = "o"
    P = "p"
    Q = "q"
    R = "r"
    K = "k"
    L = "l"
    Y = "y"
    Z = "z"
    C = "c"
    W = "w"


class PhotoTag(BaseObject):
    """VK Object photos/PhotoTag"""

    date: Optional[int] = None
    id: Optional[int] = None
    placer_id: Optional[int] = None
    tagged_name: Optional[str] = None
    user_id: Optional[int] = None
    viewed: Optional[base.BoolInt] = None
    x: Optional[float] = None
    x2: Optional[float] = None
    y: Optional[float] = None
    y2: Optional[float] = None


class PhotoUpload(BaseObject):
    """VK Object photos/PhotoUpload"""

    album_id: Optional[int] = None
    upload_url: Optional[str] = None
    fallback_upload_url: Optional[str] = None
    user_id: Optional[int] = None
    group_id: Optional[int] = None


class PhotoUploadResponse(BaseObject):
    """VK Object photos/PhotoUploadResponse"""

    aid: Optional[int] = None
    hash: Optional[str] = None
    photos_list: Optional[str] = None
    server: Optional[int] = None


class PhotoXtrRealOffset(BaseObject):
    """VK Object photos/PhotoXtrRealOffset"""

    access_key: Optional[str] = None
    album_id: Optional[int] = None
    date: Optional[int] = None
    height: Optional[int] = None
    hidden: Optional[base.PropertyExists] = None
    id: Optional[int] = None
    lat: Optional[float] = None
    long: Optional[float] = None
    owner_id: Optional[int] = None
    photo_1280: Optional[str] = None
    photo_130: Optional[str] = None
    photo_2560: Optional[str] = None
    photo_604: Optional[str] = None
    photo_75: Optional[str] = None
    photo_807: Optional[str] = None
    post_id: Optional[int] = None
    real_offset: Optional[int] = None
    sizes: Optional[List["PhotoSizes"]]
    text: Optional[str] = None
    user_id: Optional[int] = None
    width: Optional[int] = None


class PhotoXtrTagInfo(BaseObject):
    """VK Object photos/PhotoXtrTagInfo"""

    access_key: Optional[str] = None
    album_id: Optional[int] = None
    date: Optional[int] = None
    height: Optional[int] = None
    id: Optional[int] = None
    lat: Optional[float] = None
    long: Optional[float] = None
    owner_id: Optional[int] = None
    photo_1280: Optional[str] = None
    photo_130: Optional[str] = None
    photo_2560: Optional[str] = None
    photo_604: Optional[str] = None
    photo_75: Optional[str] = None
    photo_807: Optional[str] = None
    placer_id: Optional[int] = None
    post_id: Optional[int] = None
    sizes: Optional[List["PhotoSizes"]]
    tag_created: Optional[int] = None
    tag_id: Optional[int] = None
    text: Optional[str] = None
    user_id: Optional[int] = None
    width: Optional[int] = None


class TagsSuggestionItem(BaseObject):
    """VK Object photos/TagsSuggestionItem"""

    title: Optional[str] = None
    type: Optional[str] = None
    buttons: Optional[List["TagsSuggestionItemButton"]]
    photo: Optional["Photo"]
    tags: Optional[List["PhotoTag"]]


class TagsSuggestionItemButton(BaseObject):
    """VK Object photos/TagsSuggestionItemButton"""

    title: Optional[str] = None
    action: Optional[str] = None
    style: Optional[str] = None


class WallUploadResponse(BaseObject):
    """VK Object photos/WallUploadResponse"""

    hash: Optional[str] = None
    photo: Optional[str] = None
    server: Optional[int] = None
