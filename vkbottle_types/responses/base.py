from .base_response import BaseResponse
from vkbottle_types.objects import base
from typing import Optional, Any, List, Union
import typing


class BoolResponse(BaseResponse):
    response: Optional["BoolResponseModel"] = None


class GetUploadServerResponse(BaseResponse):
    response: Optional["GetUploadServerResponseModel"] = None


class OkResponse(BaseResponse):
    response: Optional["OkResponseModel"] = None


BoolResponseModel = Optional["base.BoolInt"]


GetUploadServerResponseModel = Optional["base.UploadServer"]


OkResponseModel = int
