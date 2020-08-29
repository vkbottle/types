import enum
from typing import Optional, List

from . import (
    docs,
    events,
    pages,
    photos,
    video,
    polls,
    groups,
    market,
    audio,
    comment,
    base,
)
from .base_model import BaseObject


class AppPost(BaseObject):
    """VK Object wall/AppPost

    id - Application ID
    name - Application name
    photo_130 - URL of the preview image with 130 px in width
    photo_604 - URL of the preview image with 604 px in width
    """

    id: Optional[int] = None
    name: Optional[str] = None
    photo_130: Optional[str] = None
    photo_604: Optional[str] = None


class AttachedNote(BaseObject):
    """VK Object wall/AttachedNote

    comments - Comments number
    date - Date when the note has been created in Unixtime
    id - Note ID
    owner_id - Note owner's ID
    read_comments - Read comments number
    title - Note title
    view_url - URL of the page with note preview
    """

    comments: Optional[int] = None
    date: Optional[int] = None
    id: Optional[int] = None
    owner_id: Optional[int] = None
    read_comments: Optional[int] = None
    title: Optional[str] = None
    view_url: Optional[str] = None


class CarouselBase(BaseObject):
    """VK Object wall/CarouselBase

    carousel_offset - Index of current carousel element
    """

    carousel_offset: Optional[int] = None


class CommentAttachment(BaseObject):
    """VK Object wall/CommentAttachment"""

    audio: Optional[audio.Audio] = None
    doc: Optional[docs.Doc] = None
    link: Optional[base.Link] = None
    market: Optional[market.MarketItem] = None
    market_market_album: Optional[market.MarketAlbum] = None
    note: Optional["AttachedNote"] = None
    page: Optional[pages.WikipageFull] = None
    photo: Optional[photos.Photo] = None
    sticker: Optional[base.Sticker] = None
    type: Optional["CommentAttachmentType"] = None
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
    """VK Object wall/Geo

    coordinates - Coordinates as string. <latitude> <longtitude>
    showmap - Information whether a map is showed
    type - Place type
    """

    coordinates: Optional[str] = None
    place: Optional[base.Place] = None
    showmap: Optional[int] = None
    type: Optional[str] = None


class Graffiti(BaseObject):
    """VK Object wall/Graffiti

    id - Graffiti ID
    owner_id - Graffiti owner's ID
    photo_200 - URL of the preview image with 200 px in width
    photo_586 - URL of the preview image with 586 px in width
    """

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
    type: Optional["PostSourceType"] = None
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
    """VK Object wall/PostedPhoto

    id - Photo ID
    owner_id - Photo owner's ID
    photo_130 - URL of the preview image with 130 px in width
    photo_604 - URL of the preview image with 604 px in width
    """

    id: Optional[int] = None
    owner_id: Optional[int] = None
    photo_130: Optional[str] = None
    photo_604: Optional[str] = None


class Views(BaseObject):
    """VK Object wall/Views

    count - Count
    """

    count: Optional[int] = None


class WallComment(BaseObject):
    """VK Object wall/WallComment

    date - Date when the comment has been added in Unixtime
    from_id - Author ID
    id - Comment ID
    real_offset - Real position of the comment
    reply_to_comment - Replied comment ID
    reply_to_user - Replied user ID
    text - Comment text
    """

    attachments: Optional[List["CommentAttachment"]] = None
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
    """VK Object wall/Wallpost

    access_key - Access key to private object
    copyright - Information about the source of the post
    date - Date of publishing in Unixtime
    edited - Date of editing in Unixtime
    from_id - Post author ID
    id - Post ID
    is_archived - Is post archived, only for post owners
    is_favorite - Information whether the post in favorites list
    likes - Count of likes
    owner_id - Wall owner's ID
    reposts - Count of views
    signer_id - Post signer ID
    text - Post text
    views - Count of views
    """

    access_key: Optional[str] = None
    attachments: Optional[List["WallpostAttachment"]] = None
    copyright: Optional["PostCopyright"] = None
    date: Optional[int] = None
    edited: Optional[int] = None
    from_id: Optional[int] = None
    geo: Optional["Geo"] = None
    id: Optional[int] = None
    is_archived: Optional[bool] = None
    is_favorite: Optional[bool] = None
    likes: Optional[base.LikesInfo] = None
    owner_id: Optional[int] = None
    post_source: Optional["PostSource"] = None
    post_type: Optional["PostType"] = None
    reposts: Optional[base.RepostsInfo] = None
    signer_id: Optional[int] = None
    text: Optional[str] = None
    views: Optional["Views"] = None


class WallpostAttachment(BaseObject):
    """VK Object wall/WallpostAttachment"""

    access_key: Optional[str] = None
    album: Optional[photos.PhotoAlbum] = None
    app: Optional["AppPost"] = None
    audio: Optional[audio.Audio] = None
    doc: Optional[docs.Doc] = None
    event: Optional[events.EventAttach] = None
    group: Optional[groups.GroupAttach] = None
    graffiti: Optional["Graffiti"] = None
    link: Optional[base.Link] = None
    market: Optional[market.MarketItem] = None
    market_album: Optional[market.MarketAlbum] = None
    note: Optional["AttachedNote"] = None
    page: Optional[pages.WikipageFull] = None
    photo: Optional[photos.Photo] = None
    photos_list: Optional[List[str]] = None
    poll: Optional[polls.Poll] = None
    posted_photo: Optional["PostedPhoto"] = None
    type: Optional["WallpostAttachmentType"] = None
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
    """VK Object wall/WallpostToId

    copy_owner_id - ID of the source post owner
    copy_post_id - ID of the source post
    date - Date of publishing in Unixtime
    from_id - Post author ID
    id - Post ID
    is_favorite - Information whether the post in favorites list
    post_id - wall post ID (if comment)
    signer_id - Post signer ID
    text - Post text
    to_id - Wall owner's ID
    """

    attachments: Optional[List["WallpostAttachment"]] = None
    comments: Optional[base.CommentsInfo] = None
    copy_owner_id: Optional[int] = None
    copy_post_id: Optional[int] = None
    date: Optional[int] = None
    from_id: Optional[int] = None
    geo: Optional["Geo"] = None
    id: Optional[int] = None
    is_favorite: Optional[bool] = None
    likes: Optional[base.LikesInfo] = None
    post_id: Optional[int] = None
    post_source: Optional["PostSource"] = None
    post_type: Optional["PostType"] = None
    reposts: Optional[base.RepostsInfo] = None
    signer_id: Optional[int] = None
    text: Optional[str] = None
    to_id: Optional[int] = None
