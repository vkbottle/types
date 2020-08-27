from .base_model import BaseObject
from typing import Optional, Union, Any, List
import typing
import enum


class Error(BaseObject):
    """VK Object oauth/Error

    error - Error type
    error_description - Error description
    redirect_uri - URI for validation
    """

    error: Optional[str] = None
    error_description: Optional[str] = None
    redirect_uri: Optional[str] = None
