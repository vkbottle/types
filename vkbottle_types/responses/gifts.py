from .base_response import BaseResponse
from vkbottle_types.objects import gifts
from typing import Optional, Any, List, Union
import typing


class GetResponse(BaseResponse):
    response: Optional["GetResponseModel"] = None


class GetResponseModel(BaseResponse):
    count: Optional[int] = None
    items: Optional[List["gifts.Gift"]] = None
