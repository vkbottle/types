from .base_response import BaseResponse
from vkbottle_types.objects import status
from typing import Optional, Any, List, Union
import typing


class GetResponse(BaseResponse):
    response: Optional["GetResponseModel"] = None


GetResponseModel = Optional["status.Status"]
