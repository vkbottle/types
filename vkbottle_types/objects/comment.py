from typing import Optional, List

from . import wall
from .base_model import BaseObject


class Thread(BaseObject):
    """VK Object comment/Thread

    can_post - Information whether current user can comment the post
    count - Comments number
    groups_can_post - Information whether groups can comment the post
    show_reply_button - Information whether recommended to display reply button
    """

    can_post: Optional[bool] = None
    count: Optional[int] = None
    groups_can_post: Optional[bool] = None
    items: Optional[List[wall.WallComment]] = None
    show_reply_button: Optional[bool] = None
