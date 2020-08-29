import typing
from typing import Optional

from vkbottle_types.objects import base
from .base_response import BaseResponse


class BoolResponse(BaseResponse):
    response: Optional[typing.List["base.BoolInt"]] = None


class GetUploadServerResponse(BaseResponse):
    response: Optional[typing.List["base.UploadServer"]] = None


class OkResponse(BaseResponse):
    response: Optional[int] = None
