from .base_model import BaseObject
from typing import Optional, Union, Any, List
import typing
import enum


class Error(BaseObject):
    """VK Object oauth/Error"""

    error: Optional[str] = None
    error_description: Optional[str] = None
    redirect_uri: Optional[str] = None
