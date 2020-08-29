import typing
from typing import Optional

from vkbottle_types.objects import status
from .base_response import BaseResponse


class GetResponse(BaseResponse):
    response: Optional[typing.List["status.Status"]] = None
