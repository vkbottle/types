from .base_model import BaseObject
from . import base, wall, polls
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
    """VK Object board/Topic

    comments - Comments number
    created - Date when the topic has been created in Unixtime
    created_by - Creator ID
    id - Topic ID
    is_closed - Information whether the topic is closed
    is_fixed - Information whether the topic is fixed
    title - Topic title
    updated - Date when the topic has been updated in Unixtime
    updated_by - ID of user who updated the topic
    """

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
    """VK Object board/TopicComment

    date - Date when the comment has been added in Unixtime
    from_id - Author ID
    id - Comment ID
    real_offset - Real position of the comment
    text - Comment text
    can_edit - Information whether current user can edit the comment
    """

    attachments: Optional[List[wall.CommentAttachment]] = None
    date: Optional[int] = None
    from_id: Optional[int] = None
    id: Optional[int] = None
    real_offset: Optional[int] = None
    text: Optional[str] = None
    can_edit: Optional[base.BoolInt] = None
    likes: Optional[base.LikesInfo] = None


class TopicPoll(BaseObject):
    """VK Object board/TopicPoll

    answer_id - Current user's answer ID
    created - Date when poll has been created in Unixtime
    is_closed - Information whether the poll is closed
    owner_id - Poll owner's ID
    poll_id - Poll ID
    question - Poll question
    votes - Votes number
    """

    answer_id: Optional[int] = None
    answers: Optional[List[polls.Answer]] = None
    created: Optional[int] = None
    is_closed: Optional[base.BoolInt] = None
    owner_id: Optional[int] = None
    poll_id: Optional[int] = None
    question: Optional[str] = None
    votes: Optional[str] = None
