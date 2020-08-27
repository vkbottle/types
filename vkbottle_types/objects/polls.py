from .base_model import BaseObject
from . import base
from typing import Optional, Union, Any, List
import typing
import enum


class Answer(BaseObject):
    """VK Object polls/Answer"""

    id: Optional[int] = None
    rate: Optional[float] = None
    text: Optional[str] = None
    votes: Optional[int] = None


class Background(BaseObject):
    """VK Object polls/Background"""

    angle: Optional[int] = None
    color: Optional[str] = None
    height: Optional[int] = None
    id: Optional[int] = None
    name: Optional[str] = None
    images: Optional[List[base.Image]] = None
    points: Optional[List[base.GradientPoint]] = None
    type: Optional[str] = None
    width: Optional[int] = None


class Friend(BaseObject):
    """VK Object polls/Friend"""

    id: Optional[int] = None


class Poll(BaseObject):
    """VK Object polls/Poll"""

    anonymous: Optional["PollAnonymous"]
    friends: Optional[List["Friend"]]
    multiple: Optional[bool] = None
    answer_id: Optional[int] = None
    end_date: Optional[int] = None
    answer_ids: Optional[List[int]] = None
    closed: Optional[bool] = None
    is_board: Optional[bool] = None
    can_edit: Optional[bool] = None
    can_vote: Optional[bool] = None
    can_report: Optional[bool] = None
    can_share: Optional[bool] = None
    photo: Optional["Background"]
    answers: Optional[List["Answer"]]
    created: Optional[int] = None
    id: Optional[int] = None
    owner_id: Optional[int] = None
    author_id: Optional[int] = None
    question: Optional[str] = None
    background: Optional["Background"]
    votes: Optional[int] = None
    disable_unvote: Optional[bool] = None


PollAnonymous = Optional[bool]  # Information whether the field is anonymous


class Voters(BaseObject):
    """VK Object polls/Voters"""

    answer_id: Optional[int] = None
    users: Optional["VotersUsers"]


class VotersUsers(BaseObject):
    """VK Object polls/VotersUsers"""

    count: Optional[int] = None
    items: Optional[List[int]] = None
