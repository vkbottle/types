from .base_response import BaseResponse
from vkbottle_types.objects import storage
from typing import Optional, Any, List, Union
import typing


class GetKeysResponse(BaseResponse):
    response: Optional["GetKeysResponseModel"] = None


class GetResponse(BaseResponse):
    response: Optional["GetResponseModel"] = None


class GetV5110Response(BaseResponse):
    response: Optional["GetV5110ResponseModel"] = None


class GetWithKeysResponse(BaseResponse):
    response: Optional["GetWithKeysResponseModel"] = None


GetKeysResponseModel = List[str]


GetResponseModel = str


GetV5110ResponseModel = List["storage.Value"]


GetWithKeysResponseModel = List["storage.Value"]
