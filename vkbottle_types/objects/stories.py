from .base_model import BaseObject
from . import photos, audio, market, video, apps, base, polls, users
from typing import Optional, Union, Any, List
import typing
import enum


class ClickableArea(BaseObject):
    """VK Object stories/ClickableArea"""

    x: Optional[int] = None
    y: Optional[int] = None


class ClickableSticker(BaseObject):
    """VK Object stories/ClickableSticker"""

    clickable_area: Optional[List["ClickableArea"]]
    id: Optional[int] = None
    hashtag: Optional[str] = None
    link_object: Optional[base.Link] = None
    mention: Optional[str] = None
    tooltip_text: Optional[str] = None
    owner_id: Optional[int] = None
    story_id: Optional[int] = None
    question: Optional[str] = None
    question_button: Optional[str] = None
    place_id: Optional[int] = None
    market_item: Optional[market.MarketItem] = None
    audio: Optional[audio.Audio] = None
    audio_start_time: Optional[int] = None
    style: Optional[str] = None
    type: Optional[str] = None
    subtype: Optional[str] = None
    post_owner_id: Optional[int] = None
    post_id: Optional[int] = None
    poll: Optional[polls.Poll] = None
    color: Optional[str] = None
    sticker_id: Optional[int] = None
    sticker_pack_id: Optional[int] = None
    app: Optional[apps.AppMin] = None
    app_context: Optional[str] = None
    has_new_interactions: Optional[bool] = None
    is_broadcast_notify_allowed: Optional[bool] = None


class ClickableStickers(BaseObject):
    """VK Object stories/ClickableStickers"""

    clickable_stickers: Optional[List["ClickableSticker"]]
    original_height: Optional[int] = None
    original_width: Optional[int] = None


class FeedItem(BaseObject):
    """VK Object stories/FeedItem"""

    type: Optional[str] = None
    stories: Optional[List["Story"]]
    grouped: Optional[List["FeedItem"]]
    app: Optional[apps.AppMin] = None
    promo_data: Optional["PromoBlock"]


class PromoBlock(BaseObject):
    """VK Object stories/PromoBlock"""

    name: Optional[str] = None
    photo_50: Optional[str] = None
    photo_100: Optional[str] = None
    not_animated: Optional[bool] = None


class Replies(BaseObject):
    """VK Object stories/Replies"""

    count: Optional[int] = None
    new: Optional[int] = None


class StatLine(BaseObject):
    """VK Object stories/StatLine"""

    name: Optional[str] = None
    counter: Optional[int] = None
    is_unavailable: Optional[bool] = None


class Story(BaseObject):
    """VK Object stories/Story"""

    access_key: Optional[str] = None
    can_comment: Optional[base.BoolInt] = None
    can_reply: Optional[base.BoolInt] = None
    can_see: Optional[base.BoolInt] = None
    can_like: Optional[bool] = None
    can_share: Optional[base.BoolInt] = None
    can_hide: Optional[base.BoolInt] = None
    date: Optional[int] = None
    expires_at: Optional[int] = None
    id: Optional[int] = None
    is_deleted: Optional[bool] = None
    is_expired: Optional[bool] = None
    link: Optional["StoryLink"]
    owner_id: Optional[int] = None
    parent_story: Optional["Story"]
    parent_story_access_key: Optional[str] = None
    parent_story_id: Optional[int] = None
    parent_story_owner_id: Optional[int] = None
    photo: Optional[photos.Photo] = None
    replies: Optional["Replies"]
    seen: Optional[base.BoolInt] = None
    type: Optional["StoryType"]
    clickable_stickers: Optional["ClickableStickers"]
    video: Optional[video.Video] = None
    views: Optional[int] = None
    can_ask: Optional[base.BoolInt] = None
    can_ask_anonymous: Optional[base.BoolInt] = None
    narratives_count: Optional[int] = None
    first_narrative_title: Optional[str] = None
    birthday_wish_user_id: Optional[int] = None


class StoryLink(BaseObject):
    """VK Object stories/StoryLink"""

    text: Optional[str] = None
    url: Optional[str] = None


class StoryStats(BaseObject):
    """VK Object stories/StoryStats"""

    answer: Optional["StoryStatsStat"]
    bans: Optional["StoryStatsStat"]
    open_link: Optional["StoryStatsStat"]
    replies: Optional["StoryStatsStat"]
    shares: Optional["StoryStatsStat"]
    subscribers: Optional["StoryStatsStat"]
    views: Optional["StoryStatsStat"]
    likes: Optional["StoryStatsStat"]


class StoryStatsStat(BaseObject):
    """VK Object stories/StoryStatsStat"""

    count: Optional[int] = None
    state: Optional["StoryStatsState"]


class StoryStatsState(enum.Enum):
    """ Statistic state """

    ON = "on"
    OFF = "off"
    HIDDEN = "hidden"


class StoryType(enum.Enum):
    """ Story type. """

    PHOTO = "photo"
    VIDEO = "video"
    LIVE_ACTIVE = "live_active"
    LIVE_FINISHED = "live_finished"


class UploadLinkText(enum.Enum):
    """ UploadLinkText enum """

    TO_STORE = "to_store"
    VOTE = "vote"
    MORE = "more"
    BOOK = "book"
    ORDER = "order"
    ENROLL = "enroll"
    FILL = "fill"
    SIGNUP = "signup"
    BUY = "buy"
    TICKET = "ticket"
    WRITE = "write"
    OPEN = "open"
    LEARN_MORE = "learn_more"
    VIEW = "view"
    GO_TO = "go_to"
    CONTACT = "contact"
    WATCH = "watch"
    PLAY = "play"
    INSTALL = "install"
    READ = "read"
    CALENDAR = "calendar"


class ViewersItem(BaseObject):
    """VK Object stories/ViewersItem"""

    is_liked: Optional[bool] = None
    user_id: Optional[int] = None
    user: Optional[users.UserFull] = None
