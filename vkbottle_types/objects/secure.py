from typing import Optional

from .base_model import BaseObject


class Level(BaseObject):
    """VK Object secure/Level

    level - Level
    uid - User ID
    """

    level: Optional[int] = None
    uid: Optional[int] = None


class SmsNotification(BaseObject):
    """VK Object secure/SmsNotification

    app_id - Application ID
    date - Date when message has been sent in Unixtime
    id - Notification ID
    message - Messsage text
    user_id - User ID
    """

    app_id: Optional[str] = None
    date: Optional[str] = None
    id: Optional[str] = None
    message: Optional[str] = None
    user_id: Optional[str] = None


class TokenChecked(BaseObject):
    """VK Object secure/TokenChecked

    date - Date when access_token has been generated in Unixtime
    expire - Date when access_token will expire in Unixtime
    success - Returns if successfully processed
    user_id - User ID
    """

    date: Optional[int] = None
    expire: Optional[int] = None
    success: Optional[int] = None
    user_id: Optional[int] = None


class Transaction(BaseObject):
    """VK Object secure/Transaction

    date - Transaction date in Unixtime
    id - Transaction ID
    uid_from - From ID
    uid_to - To ID
    votes - Votes number
    """

    date: Optional[int] = None
    id: Optional[int] = None
    uid_from: Optional[int] = None
    uid_to: Optional[int] = None
    votes: Optional[int] = None
