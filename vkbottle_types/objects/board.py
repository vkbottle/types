from .base_model import BaseObject
from . import base, polls, wall
from typing import Optional, Union, Any, List
import typing
import enum


class DefaultOrder(enum.IntEnum):
    """ Sort type """

    desc_updated = 1
    desc_created = 2
    asc_updated = -1
    asc_created = -2


class Topic(BaseObject):
    """VK Object board/Topic"""

    comments: Optional[int] = None
    created: Optional[int] = None
    created_by: Optional[int] = None
    id: Optional[int] = None
    is_closed: Optional[base.BoolInt] = None
    is_fixed: Optional[base.BoolInt] = None
    title: Optional[str] = None
    updated: Optional[int] = None
    updated_by: Optional[int] = None


class TopicComment(BaseObject):
    """VK Object board/TopicComment"""

    attachments: Optional[List[wall.CommentAttachment]] = None
    date: Optional[int] = None
    from_id: Optional[int] = None
    id: Optional[int] = None
    real_offset: Optional[int] = None
    text: Optional[str] = None
    can_edit: Optional[base.BoolInt] = None
    likes: Optional[base.LikesInfo] = None


class TopicPoll(BaseObject):
    """VK Object board/TopicPoll"""

    answer_id: Optional[int] = None
    answers: Optional[List[polls.Answer]] = None
    created: Optional[int] = None
    is_closed: Optional[base.BoolInt] = None
    owner_id: Optional[int] = None
    poll_id: Optional[int] = None
    question: Optional[str] = None
    votes: Optional[str] = None
