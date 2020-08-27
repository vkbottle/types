from .base_model import BaseObject
from . import (
    photos,
    audio,
    docs,
    pages,
    events,
    market,
    video,
    groups,
    base,
    polls,
    comment,
)
from typing import Optional, Union, Any, List
import typing
import enum


class AppPost(BaseObject):
    """VK Object wall/AppPost"""

    id: Optional[int] = None
    name: Optional[str] = None
    photo_130: Optional[str] = None
    photo_604: Optional[str] = None


class AttachedNote(BaseObject):
    """VK Object wall/AttachedNote"""

    comments: Optional[int] = None
    date: Optional[int] = None
    id: Optional[int] = None
    owner_id: Optional[int] = None
    read_comments: Optional[int] = None
    title: Optional[str] = None
    view_url: Optional[str] = None


class CarouselBase(BaseObject):
    """VK Object wall/CarouselBase"""

    carousel_offset: Optional[int] = None


class CommentAttachment(BaseObject):
    """VK Object wall/CommentAttachment"""

    audio: Optional[audio.Audio] = None
    doc: Optional[docs.Doc] = None
    link: Optional[base.Link] = None
    market: Optional[market.MarketItem] = None
    market_market_album: Optional[market.MarketAlbum] = None
    note: Optional["AttachedNote"]
    page: Optional[pages.WikipageFull] = None
    photo: Optional[photos.Photo] = None
    sticker: Optional[base.Sticker] = None
    type: Optional["CommentAttachmentType"]
    video: Optional[video.Video] = None


class CommentAttachmentType(enum.Enum):
    """ Attachment type """

    PHOTO = "photo"
    AUDIO = "audio"
    VIDEO = "video"
    DOC = "doc"
    LINK = "link"
    NOTE = "note"
    PAGE = "page"
    MARKET_MARKET_ALBUM = "market_market_album"
    MARKET = "market"
    STICKER = "sticker"


class Geo(BaseObject):
    """VK Object wall/Geo"""

    coordinates: Optional[str] = None
    place: Optional[base.Place] = None
    showmap: Optional[int] = None
    type: Optional[str] = None


class Graffiti(BaseObject):
    """VK Object wall/Graffiti"""

    id: Optional[int] = None
    owner_id: Optional[int] = None
    photo_200: Optional[str] = None
    photo_586: Optional[str] = None


class PostCopyright(BaseObject):
    """VK Object wall/PostCopyright"""

    id: Optional[int] = None
    link: Optional[str] = None
    name: Optional[str] = None
    type: Optional[str] = None


class PostSource(BaseObject):
    """VK Object wall/PostSource"""

    data: Optional[str] = None
    platform: Optional[str] = None
    type: Optional["PostSourceType"]
    url: Optional[str] = None


class PostSourceType(enum.Enum):
    """ Type of post source """

    VK = "vk"
    WIDGET = "widget"
    API = "api"
    RSS = "rss"
    SMS = "sms"


class PostType(enum.Enum):
    """ Post type """

    POST = "post"
    COPY = "copy"
    REPLY = "reply"
    POSTPONE = "postpone"
    SUGGEST = "suggest"


class PostedPhoto(BaseObject):
    """VK Object wall/PostedPhoto"""

    id: Optional[int] = None
    owner_id: Optional[int] = None
    photo_130: Optional[str] = None
    photo_604: Optional[str] = None


class Views(BaseObject):
    """VK Object wall/Views"""

    count: Optional[int] = None


class WallComment(BaseObject):
    """VK Object wall/WallComment"""

    attachments: Optional[List["CommentAttachment"]]
    date: Optional[int] = None
    from_id: Optional[int] = None
    id: Optional[int] = None
    likes: Optional[base.LikesInfo] = None
    real_offset: Optional[int] = None
    reply_to_comment: Optional[int] = None
    reply_to_user: Optional[int] = None
    text: Optional[str] = None
    thread: Optional[comment.Thread] = None
    post_id: Optional[int] = None
    owner_id: Optional[int] = None
    parents_stack: Optional[List[int]] = None
    deleted: Optional[bool] = None


class Wallpost(BaseObject):
    """VK Object wall/Wallpost"""

    access_key: Optional[str] = None
    attachments: Optional[List["WallpostAttachment"]]
    copyright: Optional["PostCopyright"]
    date: Optional[int] = None
    edited: Optional[int] = None
    from_id: Optional[int] = None
    geo: Optional["Geo"]
    id: Optional[int] = None
    is_archived: Optional[bool] = None
    is_favorite: Optional[bool] = None
    likes: Optional[base.LikesInfo] = None
    owner_id: Optional[int] = None
    post_source: Optional["PostSource"]
    post_type: Optional["PostType"]
    reposts: Optional[base.RepostsInfo] = None
    signer_id: Optional[int] = None
    text: Optional[str] = None
    views: Optional["Views"]


class WallpostAttachment(BaseObject):
    """VK Object wall/WallpostAttachment"""

    access_key: Optional[str] = None
    album: Optional[photos.PhotoAlbum] = None
    app: Optional["AppPost"]
    audio: Optional[audio.Audio] = None
    doc: Optional[docs.Doc] = None
    event: Optional[events.EventAttach] = None
    group: Optional[groups.GroupAttach] = None
    graffiti: Optional["Graffiti"]
    link: Optional[base.Link] = None
    market: Optional[market.MarketItem] = None
    market_album: Optional[market.MarketAlbum] = None
    note: Optional["AttachedNote"]
    page: Optional[pages.WikipageFull] = None
    photo: Optional[photos.Photo] = None
    photos_list: Optional[List[str]] = None
    poll: Optional[polls.Poll] = None
    posted_photo: Optional["PostedPhoto"]
    type: Optional["WallpostAttachmentType"]
    video: Optional[video.Video] = None


class WallpostAttachmentType(enum.Enum):
    """ Attachment type """

    PHOTO = "photo"
    POSTED_PHOTO = "posted_photo"
    AUDIO = "audio"
    VIDEO = "video"
    DOC = "doc"
    LINK = "link"
    GRAFFITI = "graffiti"
    NOTE = "note"
    APP = "app"
    POLL = "poll"
    PAGE = "page"
    ALBUM = "album"
    PHOTOS_LIST = "photos_list"
    MARKET_MARKET_ALBUM = "market_market_album"
    MARKET = "market"
    EVENT = "event"


class WallpostFull(BaseObject):
    """VK Object wall/WallpostFull"""


class WallpostToId(BaseObject):
    """VK Object wall/WallpostToId"""

    attachments: Optional[List["WallpostAttachment"]]
    comments: Optional[base.CommentsInfo] = None
    copy_owner_id: Optional[int] = None
    copy_post_id: Optional[int] = None
    date: Optional[int] = None
    from_id: Optional[int] = None
    geo: Optional["Geo"]
    id: Optional[int] = None
    is_favorite: Optional[bool] = None
    likes: Optional[base.LikesInfo] = None
    post_id: Optional[int] = None
    post_source: Optional["PostSource"]
    post_type: Optional["PostType"]
    reposts: Optional[base.RepostsInfo] = None
    signer_id: Optional[int] = None
    text: Optional[str] = None
    to_id: Optional[int] = None
