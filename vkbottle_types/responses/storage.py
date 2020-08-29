import typing
from typing import Optional

from vkbottle_types.objects import storage
from .base_response import BaseResponse


class GetKeysResponse(BaseResponse):
    response: Optional[typing.List[str]] = None


class GetResponse(BaseResponse):
    response: Optional[str] = None


class GetV5110Response(BaseResponse):
    response: Optional[typing.List["storage.Value"]] = None


class GetWithKeysResponse(BaseResponse):
    response: Optional[typing.List["storage.Value"]] = None
