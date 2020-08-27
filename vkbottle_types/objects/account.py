from .base_model import BaseObject
from . import base
from typing import Optional, Union, Any, List
import typing
import enum


class AccountCounters(BaseObject):
    """VK Object account/AccountCounters"""

    app_requests: Optional[int] = None
    events: Optional[int] = None
    faves: Optional[int] = None
    friends: Optional[int] = None
    friends_suggestions: Optional[int] = None
    friends_recommendations: Optional[int] = None
    gifts: Optional[int] = None
    groups: Optional[int] = None
    menu_discover_badge: Optional[int] = None
    messages: Optional[int] = None
    memories: Optional[int] = None
    notes: Optional[int] = None
    notifications: Optional[int] = None
    photos: Optional[int] = None
    sdk: Optional[int] = None


class Info(BaseObject):
    """VK Object account/Info"""

    wishlists_ae_promo_banner_show: Optional[base.BoolInt] = None
    _2fa_required: Optional[base.BoolInt] = None
    country: Optional[str] = None
    https_required: Optional[base.BoolInt] = None
    intro: Optional[base.BoolInt] = None
    show_vk_apps_intro: Optional[bool] = None
    mini_apps_ads_slot_id: Optional[int] = None
    qr_promotion: Optional[int] = None
    link_redirects: Optional[typing.Dict[Any, Any]] = None
    lang: Optional[int] = None
    no_wall_replies: Optional[base.BoolInt] = None
    own_posts_default: Optional[base.BoolInt] = None
    subscriptions: Optional[List[int]] = None


class NameRequest(BaseObject):
    """VK Object account/NameRequest"""

    first_name: Optional[str] = None
    id: Optional[int] = None
    last_name: Optional[str] = None
    status: Optional["NameRequestStatus"]
    lang: Optional[str] = None
    link_href: Optional[str] = None
    link_label: Optional[str] = None


class NameRequestStatus(enum.Enum):
    """ Request status """

    SUCCESS = "success"
    PROCESSING = "processing"
    DECLINED = "declined"
    WAS_ACCEPTED = "was_accepted"
    WAS_DECLINED = "was_declined"
    DECLINED_WITH_LINK = "declined_with_link"
    RESPONSE = "response"
    RESPONSE_WITH_LINK = "response_with_link"


class Offer(BaseObject):
    """VK Object account/Offer"""

    description: Optional[str] = None
    id: Optional[int] = None
    img: Optional[str] = None
    instruction: Optional[str] = None
    instruction_html: Optional[str] = None
    price: Optional[int] = None
    short_description: Optional[str] = None
    tag: Optional[str] = None
    title: Optional[str] = None
    currency_amount: Optional[float] = None
    link_id: Optional[int] = None
    link_type: Optional[str] = None


class PushConversations(BaseObject):
    """VK Object account/PushConversations"""

    count: Optional[int] = None
    items: Optional[List["PushConversationsItem"]]


class PushConversationsItem(BaseObject):
    """VK Object account/PushConversationsItem"""

    disabled_until: Optional[int] = None
    peer_id: Optional[int] = None
    sound: Optional[base.BoolInt] = None


class PushParams(BaseObject):
    """VK Object account/PushParams"""

    msg: Optional[List["PushParamsMode"]]
    chat: Optional[List["PushParamsMode"]]
    like: Optional[List["PushParamsSettings"]]
    repost: Optional[List["PushParamsSettings"]]
    comment: Optional[List["PushParamsSettings"]]
    mention: Optional[List["PushParamsSettings"]]
    reply: Optional[List["PushParamsOnoff"]]
    new_post: Optional[List["PushParamsOnoff"]]
    wall_post: Optional[List["PushParamsOnoff"]]
    wall_publish: Optional[List["PushParamsOnoff"]]
    friend: Optional[List["PushParamsOnoff"]]
    friend_found: Optional[List["PushParamsOnoff"]]
    friend_accepted: Optional[List["PushParamsOnoff"]]
    group_invite: Optional[List["PushParamsOnoff"]]
    group_accepted: Optional[List["PushParamsOnoff"]]
    birthday: Optional[List["PushParamsOnoff"]]
    event_soon: Optional[List["PushParamsOnoff"]]
    app_request: Optional[List["PushParamsOnoff"]]
    sdk_open: Optional[List["PushParamsOnoff"]]


class PushParamsMode(enum.Enum):
    """ Settings parameters """

    ON = "on"
    OFF = "off"
    NO_SOUND = "no_sound"
    NO_TEXT = "no_text"


class PushParamsOnoff(enum.Enum):
    """ Settings parameters """

    ON = "on"
    OFF = "off"


class PushParamsSettings(enum.Enum):
    """ Settings parameters """

    ON = "on"
    OFF = "off"
    FR_OF_FR = "fr_of_fr"


class PushSettings(BaseObject):
    """VK Object account/PushSettings"""

    disabled: Optional[base.BoolInt] = None
    disabled_until: Optional[int] = None
    settings: Optional["PushParams"]
    conversations: Optional["PushConversations"]


class UserSettings(BaseObject):
    """VK Object account/UserSettings"""


class UserSettingsInterest(BaseObject):
    """VK Object account/UserSettingsInterest"""

    title: Optional[str] = None
    value: Optional[str] = None


class UserSettingsInterests(BaseObject):
    """VK Object account/UserSettingsInterests"""

    activities: Optional["UserSettingsInterest"]
    interests: Optional["UserSettingsInterest"]
    music: Optional["UserSettingsInterest"]
    tv: Optional["UserSettingsInterest"]
    movies: Optional["UserSettingsInterest"]
    books: Optional["UserSettingsInterest"]
    games: Optional["UserSettingsInterest"]
    quotes: Optional["UserSettingsInterest"]
    about: Optional["UserSettingsInterest"]
