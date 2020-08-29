import typing
from typing import Optional

from vkbottle_types.objects import gifts
from .base_response import BaseResponse


class GetResponse(BaseResponse):
    response: Optional["GetResponseModel"] = None


class GetResponseModel(BaseResponse):
    count: Optional[int] = None
    items: Optional[typing.List["gifts.Gift"]] = None
