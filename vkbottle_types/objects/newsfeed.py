import enum
from typing import Optional, List

from . import audio, groups, video, base
from .base_model import BaseObject


class CommentsFilters(enum.Enum):
    """ CommentsFilters enum """

    POST = "post"
    PHOTO = "photo"
    VIDEO = "video"
    TOPIC = "topic"
    NOTE = "note"


class EventActivity(BaseObject):
    """VK Object newsfeed/EventActivity"""

    address: Optional[str] = None
    button_text: Optional[str] = None
    friends: Optional[List[int]] = None
    member_status: Optional[groups.GroupFullMemberStatus] = None
    text: Optional[str] = None
    time: Optional[int] = None


class Filters(enum.Enum):
    """ Filters enum """

    POST = "post"
    PHOTO = "photo"
    PHOTO_TAG = "photo_tag"
    WALL_PHOTO = "wall_photo"
    FRIEND = "friend"
    RECOMMENDED_GROUPS = "recommended_groups"
    NOTE = "note"
    AUDIO = "audio"
    VIDEO = "video"
    AUDIO_PLAYLIST = "audio_playlist"
    CLIP = "clip"


class IgnoreItemType(enum.Enum):
    """ IgnoreItemType enum """

    WALL = "wall"
    TAG = "tag"
    PROFILEPHOTO = "profilephoto"
    VIDEO = "video"
    PHOTO = "photo"
    AUDIO = "audio"


class ItemAudio(BaseObject):
    """VK Object newsfeed/ItemAudio"""


class ItemAudioAudio(BaseObject):
    """VK Object newsfeed/ItemAudioAudio

    count - Audios number
    """

    count: Optional[int] = None
    items: Optional[List[audio.Audio]] = None


class ItemBase(BaseObject):
    """VK Object newsfeed/ItemBase

    source_id - Item source ID
    date - Date when item has been added in Unixtime
    """

    type: Optional["NewsfeedItemType"] = None
    source_id: Optional[int] = None
    date: Optional[int] = None


class ItemDigest(BaseObject):
    """VK Object newsfeed/ItemDigest"""


class ItemFriend(BaseObject):
    """VK Object newsfeed/ItemFriend"""


class ItemFriendFriends(BaseObject):
    """VK Object newsfeed/ItemFriendFriends

    count - Number of friends has been added
    """

    count: Optional[int] = None
    items: Optional[List[base.UserId]] = None


class ItemHolidayRecommendationsBlockHeader(BaseObject):
    """VK Object newsfeed/ItemHolidayRecommendationsBlockHeader

    title - Title of the header
    subtitle - Subtitle of the header
    """

    title: Optional[str] = None
    subtitle: Optional[str] = None
    image: Optional[List[base.Image]] = None
    action: Optional[base.LinkButtonAction] = None


class ItemNote(BaseObject):
    """VK Object newsfeed/ItemNote"""


class ItemNoteNotes(BaseObject):
    """VK Object newsfeed/ItemNoteNotes

    count - Notes number
    """

    count: Optional[int] = None
    items: Optional[List["NewsfeedNote"]] = None


class ItemPhoto(BaseObject):
    """VK Object newsfeed/ItemPhoto"""


class ItemPhotoPhotos(BaseObject):
    """VK Object newsfeed/ItemPhotoPhotos

    count - Photos number
    """

    count: Optional[int] = None
    items: Optional[List["NewsfeedPhoto"]] = None


class ItemPhotoTag(BaseObject):
    """VK Object newsfeed/ItemPhotoTag"""


class ItemPhotoTagPhotoTags(BaseObject):
    """VK Object newsfeed/ItemPhotoTagPhotoTags

    count - Tags number
    """

    count: Optional[int] = None
    items: Optional[List["NewsfeedPhoto"]] = None


class ItemPromoButton(BaseObject):
    """VK Object newsfeed/ItemPromoButton"""


class ItemPromoButtonAction(BaseObject):
    """VK Object newsfeed/ItemPromoButtonAction"""

    url: Optional[str] = None
    type: Optional[str] = None
    target: Optional[str] = None


class ItemPromoButtonImage(BaseObject):
    """VK Object newsfeed/ItemPromoButtonImage"""

    width: Optional[int] = None
    height: Optional[int] = None
    url: Optional[str] = None


class ItemTopic(BaseObject):
    """VK Object newsfeed/ItemTopic"""


class ItemVideo(BaseObject):
    """VK Object newsfeed/ItemVideo"""


class ItemVideoVideo(BaseObject):
    """VK Object newsfeed/ItemVideoVideo

    count - Tags number
    """

    count: Optional[int] = None
    items: Optional[List[video.Video]] = None


class ItemWallpost(BaseObject):
    """VK Object newsfeed/ItemWallpost"""


class ItemWallpostFeedback(BaseObject):
    """VK Object newsfeed/ItemWallpostFeedback"""

    type: Optional["ItemWallpostFeedbackType"] = None
    question: Optional[str] = None
    answers: Optional[List["ItemWallpostFeedbackAnswer"]] = None
    stars_count: Optional[int] = None
    gratitude: Optional[str] = None


class ItemWallpostFeedbackAnswer(BaseObject):
    """VK Object newsfeed/ItemWallpostFeedbackAnswer"""

    title: Optional[str] = None
    id: Optional[str] = None


class ItemWallpostFeedbackType(enum.Enum):
    """ ItemWallpostFeedbackType enum """

    BUTTONS = "buttons"
    STARS = "stars"


class ItemWallpostType(enum.Enum):
    """ Post type """

    POST = "post"
    COPY = "copy"
    REPLY = "reply"


class List(BaseObject):
    """VK Object newsfeed/List

    id - List ID
    title - List title
    """

    id: Optional[int] = None
    title: Optional[str] = None


class ListFull(BaseObject):
    """VK Object newsfeed/ListFull"""


class NewsfeedItem(BaseObject):
    """VK Object newsfeed/NewsfeedItem"""


class NewsfeedItemType(enum.Enum):
    """ Item type """

    POST = "post"
    PHOTO = "photo"
    PHOTO_TAG = "photo_tag"
    WALL_PHOTO = "wall_photo"
    FRIEND = "friend"
    NOTE = "note"
    AUDIO = "audio"
    VIDEO = "video"
    TOPIC = "topic"
    DIGEST = "digest"
    STORIES = "stories"
    TAGS_SUGGESTIONS = "tags_suggestions"


class NewsfeedNote(BaseObject):
    """VK Object newsfeed/NewsfeedNote

    comments - Comments Number
    id - Note ID
    owner_id - integer
    title - Note title
    """

    comments: Optional[int] = None
    id: Optional[int] = None
    owner_id: Optional[int] = None
    title: Optional[str] = None


class NewsfeedPhoto(BaseObject):
    """VK Object newsfeed/NewsfeedPhoto"""
