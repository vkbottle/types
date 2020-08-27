from .base_model import BaseObject
from . import photos, gifts, audio, docs, stories, market, video, wall, base
from typing import Optional, Union, Any, List
import typing
import enum


class AudioMessage(BaseObject):
    """VK Object messages/AudioMessage"""

    access_key: Optional[str] = None
    duration: Optional[int] = None
    id: Optional[int] = None
    link_mp3: Optional[str] = None
    link_ogg: Optional[str] = None
    owner_id: Optional[int] = None
    waveform: Optional[List[int]] = None


class Chat(BaseObject):
    """VK Object messages/Chat"""

    admin_id: Optional[int] = None
    id: Optional[int] = None
    kicked: Optional[base.BoolInt] = None
    left: Optional[base.BoolInt] = None
    photo_100: Optional[str] = None
    photo_200: Optional[str] = None
    photo_50: Optional[str] = None
    push_settings: Optional["ChatPushSettings"]
    title: Optional[str] = None
    type: Optional[str] = None
    users: Optional[List[int]] = None
    is_default_photo: Optional[bool] = None


class ChatFull(BaseObject):
    """VK Object messages/ChatFull"""

    admin_id: Optional[int] = None
    id: Optional[int] = None
    kicked: Optional[base.BoolInt] = None
    left: Optional[base.BoolInt] = None
    photo_100: Optional[str] = None
    photo_200: Optional[str] = None
    photo_50: Optional[str] = None
    push_settings: Optional["ChatPushSettings"]
    title: Optional[str] = None
    type: Optional[str] = None
    users: Optional[List["UserXtrInvitedBy"]]


class ChatPushSettings(BaseObject):
    """VK Object messages/ChatPushSettings"""

    disabled_until: Optional[int] = None
    sound: Optional[base.BoolInt] = None


class ChatRestrictions(BaseObject):
    """VK Object messages/ChatRestrictions"""

    admins_promote_users: Optional[bool] = None
    only_admins_edit_info: Optional[bool] = None
    only_admins_edit_pin: Optional[bool] = None
    only_admins_invite: Optional[bool] = None
    only_admins_kick: Optional[bool] = None


class Conversation(BaseObject):
    """VK Object messages/Conversation"""

    peer: Optional["ConversationPeer"]
    last_message_id: Optional[int] = None
    in_read: Optional[int] = None
    out_read: Optional[int] = None
    unread_count: Optional[int] = None
    is_marked_unread: Optional[bool] = None
    important: Optional[bool] = None
    unanswered: Optional[bool] = None
    special_service_type: Optional[str] = None
    message_request_data: Optional["MessageRequestData"]
    mentions: Optional[List[int]] = None
    current_keyboard: Optional["Keyboard"]


class ConversationMember(BaseObject):
    """VK Object messages/ConversationMember"""

    can_kick: Optional[bool] = None
    invited_by: Optional[int] = None
    is_admin: Optional[bool] = None
    is_owner: Optional[bool] = None
    is_message_request: Optional[bool] = None
    join_date: Optional[int] = None
    request_date: Optional[int] = None
    member_id: Optional[int] = None


class ConversationPeer(BaseObject):
    """VK Object messages/ConversationPeer"""

    id: Optional[int] = None
    local_id: Optional[int] = None
    type: Optional["ConversationPeerType"]


class ConversationPeerType(enum.Enum):
    """ Peer type """

    CHAT = "chat"
    EMAIL = "email"
    USER = "user"
    GROUP = "group"


class ConversationWithMessage(BaseObject):
    """VK Object messages/ConversationWithMessage"""

    conversation: Optional["Conversation"]
    last_message: Optional["Message"]


class ForeignMessage(BaseObject):
    """VK Object messages/ForeignMessage"""

    attachments: Optional[List["MessageAttachment"]]
    conversation_message_id: Optional[int] = None
    date: Optional[int] = None
    from_id: Optional[int] = None
    fwd_messages: Optional[List["ForeignMessage"]]
    geo: Optional[base.Geo] = None
    id: Optional[int] = None
    peer_id: Optional[int] = None
    reply_message: Optional["ForeignMessage"]
    text: Optional[str] = None
    update_time: Optional[int] = None
    was_listened: Optional[bool] = None
    payload: Optional[str] = None


class Graffiti(BaseObject):
    """VK Object messages/Graffiti"""

    access_key: Optional[str] = None
    height: Optional[int] = None
    id: Optional[int] = None
    owner_id: Optional[int] = None
    url: Optional[str] = None
    width: Optional[int] = None


class HistoryAttachment(BaseObject):
    """VK Object messages/HistoryAttachment"""

    attachment: Optional["HistoryMessageAttachment"]
    message_id: Optional[int] = None
    from_id: Optional[int] = None


class HistoryMessageAttachment(BaseObject):
    """VK Object messages/HistoryMessageAttachment"""

    audio: Optional[audio.Audio] = None
    audio_message: Optional["AudioMessage"]
    doc: Optional[docs.Doc] = None
    graffiti: Optional["Graffiti"]
    link: Optional[base.Link] = None
    market: Optional[base.Link] = None
    photo: Optional[photos.Photo] = None
    share: Optional[base.Link] = None
    type: Optional["HistoryMessageAttachmentType"]
    video: Optional[video.Video] = None
    wall: Optional[base.Link] = None


class HistoryMessageAttachmentType(enum.Enum):
    """ Attachments type """

    PHOTO = "photo"
    VIDEO = "video"
    AUDIO = "audio"
    DOC = "doc"
    LINK = "link"
    MARKET = "market"
    WALL = "wall"
    SHARE = "share"
    GRAFFITI = "graffiti"
    AUDIO_MESSAGE = "audio_message"


class Keyboard(BaseObject):
    """VK Object messages/Keyboard"""

    author_id: Optional[int] = None
    buttons: Optional[List[dict]] = None
    one_time: Optional[bool] = None
    inline: Optional[bool] = None


class KeyboardButton(BaseObject):
    """VK Object messages/KeyboardButton"""

    action: Optional["KeyboardButtonAction"]
    color: Optional[str] = None


class KeyboardButtonAction(BaseObject):
    """VK Object messages/KeyboardButtonAction"""

    app_id: Optional[int] = None
    hash: Optional[str] = None
    label: Optional[str] = None
    link: Optional[str] = None
    owner_id: Optional[int] = None
    payload: Optional[str] = None
    type: Optional["TemplateActionTypeNames"]


class LastActivity(BaseObject):
    """VK Object messages/LastActivity"""

    online: Optional[base.BoolInt] = None
    time: Optional[int] = None


class LongpollMessages(BaseObject):
    """VK Object messages/LongpollMessages"""

    count: Optional[int] = None
    items: Optional[List["Message"]]


class LongpollParams(BaseObject):
    """VK Object messages/LongpollParams"""

    key: Optional[str] = None
    pts: Optional[int] = None
    server: Optional[str] = None
    ts: Optional[str] = None


class Message(BaseObject):
    """VK Object messages/Message"""

    action: Optional["MessageAction"]
    admin_author_id: Optional[int] = None
    attachments: Optional[List["MessageAttachment"]]
    conversation_message_id: Optional[int] = None
    date: Optional[int] = None
    deleted: Optional[base.BoolInt] = None
    from_id: Optional[int] = None
    fwd_messages: Optional[List["ForeignMessage"]]
    geo: Optional[base.Geo] = None
    id: Optional[int] = None
    important: Optional[bool] = None
    is_hidden: Optional[bool] = None
    is_cropped: Optional[bool] = None
    keyboard: Optional["Keyboard"]
    members_count: Optional[int] = None
    out: Optional[base.BoolInt] = None
    payload: Optional[str] = None
    peer_id: Optional[int] = None
    random_id: Optional[int] = None
    ref: Optional[str] = None
    ref_source: Optional[str] = None
    reply_message: Optional["ForeignMessage"]
    text: Optional[str] = None
    update_time: Optional[int] = None
    was_listened: Optional[bool] = None
    pinned_at: Optional[int] = None


class MessageAction(BaseObject):
    """VK Object messages/MessageAction"""

    conversation_message_id: Optional[int] = None
    email: Optional[str] = None
    member_id: Optional[int] = None
    message: Optional[str] = None
    photo: Optional["MessageActionPhoto"]
    text: Optional[str] = None
    type: Optional["MessageActionStatus"]


class MessageActionPhoto(BaseObject):
    """VK Object messages/MessageActionPhoto"""

    photo_100: Optional[str] = None
    photo_200: Optional[str] = None
    photo_50: Optional[str] = None


class MessageActionStatus(enum.Enum):
    """ Action status """

    CHAT_PHOTO_UPDATE = "chat_photo_update"
    CHAT_PHOTO_REMOVE = "chat_photo_remove"
    CHAT_CREATE = "chat_create"
    CHAT_TITLE_UPDATE = "chat_title_update"
    CHAT_INVITE_USER = "chat_invite_user"
    CHAT_KICK_USER = "chat_kick_user"
    CHAT_PIN_MESSAGE = "chat_pin_message"
    CHAT_UNPIN_MESSAGE = "chat_unpin_message"
    CHAT_INVITE_USER_BY_LINK = "chat_invite_user_by_link"


class MessageAttachment(BaseObject):
    """VK Object messages/MessageAttachment"""

    audio: Optional[audio.Audio] = None
    audio_message: Optional["AudioMessage"]
    doc: Optional[docs.Doc] = None
    gift: Optional[gifts.Layout] = None
    graffiti: Optional["Graffiti"]
    link: Optional[base.Link] = None
    market: Optional[market.MarketItem] = None
    market_market_album: Optional[market.MarketAlbum] = None
    photo: Optional[photos.Photo] = None
    sticker: Optional[base.Sticker] = None
    story: Optional[stories.Story] = None
    type: Optional["MessageAttachmentType"]
    video: Optional[video.Video] = None
    wall: Optional[wall.WallpostFull] = None
    wall_reply: Optional[wall.WallComment] = None


class MessageAttachmentType(enum.Enum):
    """ Attachment type """

    PHOTO = "photo"
    AUDIO = "audio"
    VIDEO = "video"
    DOC = "doc"
    LINK = "link"
    MARKET = "market"
    MARKET_ALBUM = "market_album"
    GIFT = "gift"
    STICKER = "sticker"
    WALL = "wall"
    WALL_REPLY = "wall_reply"
    ARTICLE = "article"
    GRAFFITI = "graffiti"
    AUDIO_MESSAGE = "audio_message"


class MessageRequestData(BaseObject):
    """VK Object messages/MessageRequestData"""

    status: Optional[str] = None
    inviter_id: Optional[int] = None
    request_date: Optional[int] = None


class PinnedMessage(BaseObject):
    """VK Object messages/PinnedMessage"""

    attachments: Optional[List["MessageAttachment"]]
    conversation_message_id: Optional[int] = None
    date: Optional[int] = None
    from_id: Optional[int] = None
    fwd_messages: Optional[List["ForeignMessage"]]
    geo: Optional[base.Geo] = None
    id: Optional[int] = None
    peer_id: Optional[int] = None
    reply_message: Optional["ForeignMessage"]
    text: Optional[str] = None
    keyboard: Optional["Keyboard"]


class TemplateActionTypeNames(enum.Enum):
    """ Template action type names """

    TEXT = "text"
    START = "start"
    LOCATION = "location"
    VKPAY = "vkpay"
    OPEN_APP = "open_app"
    OPEN_PHOTO = "open_photo"
    OPEN_LINK = "open_link"


class UserXtrInvitedBy(BaseObject):
    """VK Object messages/UserXtrInvitedBy"""
