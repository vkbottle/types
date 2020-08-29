import enum
from typing import Optional, List

from . import photos, video, polls, apps, market, audio, users, base
from .base_model import BaseObject


class ClickableArea(BaseObject):
    """VK Object stories/ClickableArea"""

    x: Optional[int] = None
    y: Optional[int] = None


class ClickableSticker(BaseObject):
    """VK Object stories/ClickableSticker

    id - Clickable sticker ID
    color - Color, hex format
    sticker_id - Sticker ID
    sticker_pack_id - Sticker pack ID
    app_context - Additional context for app sticker
    has_new_interactions - Whether current user has unread interaction with this app
    is_broadcast_notify_allowed - Whether current user allowed broadcast notify from this app
    """

    clickable_area: Optional[List["ClickableArea"]] = None
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

    clickable_stickers: Optional[List["ClickableSticker"]] = None
    original_height: Optional[int] = None
    original_width: Optional[int] = None


class FeedItem(BaseObject):
    """VK Object stories/FeedItem

    type - Type of Feed Item
    stories - Author stories
    grouped - Grouped stories of various authors (for types community_grouped_stories/app_grouped_stories type)
    app - App, which stories has been grouped (for type app_grouped_stories)
    promo_data - Additional data for promo stories (for type promo_stories)
    """

    type: Optional[str] = None
    stories: Optional[List["Story"]] = None
    grouped: Optional[List["FeedItem"]] = None
    app: Optional[apps.AppMin] = None
    promo_data: Optional["PromoBlock"] = None


class PromoBlock(BaseObject):
    """VK Object stories/PromoBlock

    name - Promo story title
    photo_50 - RL of square photo of the story with 50 pixels in width
    photo_100 - RL of square photo of the story with 100 pixels in width
    not_animated - Hide animation for promo story
    """

    name: Optional[str] = None
    photo_50: Optional[str] = None
    photo_100: Optional[str] = None
    not_animated: Optional[bool] = None


class Replies(BaseObject):
    """VK Object stories/Replies

    count - Replies number.
    new - New replies number.
    """

    count: Optional[int] = None
    new: Optional[int] = None


class StatLine(BaseObject):
    """VK Object stories/StatLine"""

    name: Optional[str] = None
    counter: Optional[int] = None
    is_unavailable: Optional[bool] = None


class Story(BaseObject):
    """VK Object stories/Story

    access_key - Access key for private object.
    can_comment - Information whether current user can comment the story (0 - no, 1 - yes).
    can_reply - Information whether current user can reply to the story (0 - no, 1 - yes).
    can_see - Information whether current user can see the story (0 - no, 1 - yes).
    can_like - Information whether current user can like the story.
    can_share - Information whether current user can share the story (0 - no, 1 - yes).
    can_hide - Information whether current user can hide the story (0 - no, 1 - yes).
    date - Date when story has been added in Unixtime.
    expires_at - Story expiration time. Unixtime.
    id - Story ID.
    is_deleted - Information whether the story is deleted (false - no, true - yes).
    is_expired - Information whether the story is expired (false - no, true - yes).
    owner_id - Story owner's ID.
    parent_story_access_key - Access key for private object.
    parent_story_id - Parent story ID.
    parent_story_owner_id - Parent story owner's ID.
    replies - Replies counters to current story.
    seen - Information whether current user has seen the story or not (0 - no, 1 - yes).
    views - Views number.
    can_ask - Information whether story has question sticker and current user can send question to the author
    can_ask_anonymous - Information whether story has question sticker and current user can send anonymous question to the author
    """

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
    link: Optional["StoryLink"] = None
    owner_id: Optional[int] = None
    parent_story: Optional["Story"] = None
    parent_story_access_key: Optional[str] = None
    parent_story_id: Optional[int] = None
    parent_story_owner_id: Optional[int] = None
    photo: Optional[photos.Photo] = None
    replies: Optional["Replies"] = None
    seen: Optional[base.BoolInt] = None
    type: Optional["StoryType"] = None
    clickable_stickers: Optional["ClickableStickers"] = None
    video: Optional[video.Video] = None
    views: Optional[int] = None
    can_ask: Optional[base.BoolInt] = None
    can_ask_anonymous: Optional[base.BoolInt] = None
    narratives_count: Optional[int] = None
    first_narrative_title: Optional[str] = None
    birthday_wish_user_id: Optional[int] = None


class StoryLink(BaseObject):
    """VK Object stories/StoryLink

    text - Link text
    url - Link URL
    """

    text: Optional[str] = None
    url: Optional[str] = None


class StoryStats(BaseObject):
    """VK Object stories/StoryStats"""

    answer: Optional["StoryStatsStat"] = None
    bans: Optional["StoryStatsStat"] = None
    open_link: Optional["StoryStatsStat"] = None
    replies: Optional["StoryStatsStat"] = None
    shares: Optional["StoryStatsStat"] = None
    subscribers: Optional["StoryStatsStat"] = None
    views: Optional["StoryStatsStat"] = None
    likes: Optional["StoryStatsStat"] = None


class StoryStatsStat(BaseObject):
    """VK Object stories/StoryStatsStat"""

    count: Optional[int] = None
    state: Optional["StoryStatsState"] = None


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
    """VK Object stories/ViewersItem

    is_liked - user has like for this object
    user_id - user id
    """

    is_liked: Optional[bool] = None
    user_id: Optional[int] = None
    user: Optional[users.UserFull] = None
