from .base_model import BaseObject
from . import wall, video, groups, market, users, base
from typing import Optional, Union, Any, List
import typing
import enum


class Bookmark(BaseObject):
    """VK Object fave/Bookmark"""

    added_date: Optional[int] = None
    link: Optional[base.Link] = None
    post: Optional[wall.WallpostFull] = None
    product: Optional[market.MarketItem] = None
    seen: Optional[bool] = None
    tags: Optional[List["Tag"]] = None
    type: Optional["BookmarkType"] = None
    video: Optional[video.Video] = None


class BookmarkType(enum.Enum):
    """ BookmarkType enum """

    POST = "post"
    VIDEO = "video"
    PRODUCT = "product"
    ARTICLE = "article"
    LINK = "link"


class Page(BaseObject):
    """VK Object fave/Page"""

    description: Optional[str] = None
    group: Optional[groups.GroupFull] = None
    tags: Optional[List["Tag"]] = None
    type: Optional["PageType"] = None
    updated_date: Optional[int] = None
    user: Optional[users.UserFull] = None


class PageType(enum.Enum):
    """ PageType enum """

    USER = "user"
    GROUP = "group"
    HINTS = "hints"


class Tag(BaseObject):
    """VK Object fave/Tag

    id - Tag id
    name - Tag name
    """

    id: Optional[int] = None
    name: Optional[str] = None
